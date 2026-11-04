"""Bounded adversarial tests of COUNT input restoration; no native inequalities."""
from pathlib import Path
from copy import deepcopy
import argparse
import hashlib
import json
import stat
import sys
import tempfile
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import install_count_candidates as installer


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--archive', type=Path, required=True)
    a = p.parse_args()
    rejected = []

    def reject(label, action):
        try:
            action()
        except (ValueError, FileNotFoundError, OSError):
            rejected.append(label)
        else:
            raise AssertionError('Malformed input accepted: ' + label)

    with zipfile.ZipFile(a.archive) as z:
        raw = z.read('MANIFEST.json')
        expected = installer.candidate_inventory(raw)
        infos = z.infolist()
        installer.namespace(infos, expected)
        reject('manifest-byte-corruption', lambda: installer.candidate_inventory(raw[:-1] + b'!'))
        reject('duplicate-json-key', lambda: json.loads('{"a":1,"a":2}', object_pairs_hook=installer.unique))
        reject('missing-member', lambda: installer.namespace(infos[:-1], expected))
        reject('duplicate-member', lambda: installer.namespace(infos + [infos[-1]], expected))
        for label, name in [('absolute-name', '/escape'), ('parent-name', '../escape'),
                            ('backslash-name', 'blobs\\escape'), ('empty-name', ''),
                            ('dot-alias', './MANIFEST.json'), ('case-alias', 'manifest.json'),
                            ('unknown-member', 'blobs/' + '0' * 64)]:
            altered = deepcopy(infos)
            altered[-1].filename = name
            reject(label, lambda x=altered: installer.namespace(x, expected))
        for label, mutate in [
            ('wrong-size', lambda x: setattr(x, 'file_size', x.file_size + 1)),
            ('symlink-member', lambda x: setattr(x, 'external_attr', (stat.S_IFLNK | 0o777) << 16)),
            ('fifo-member', lambda x: setattr(x, 'external_attr', (stat.S_IFIFO | 0o600) << 16)),
            ('encrypted-member', lambda x: setattr(x, 'flag_bits', x.flag_bits | 1)),
            ('unknown-compression', lambda x: setattr(x, 'compress_type', 99))]:
            altered = deepcopy(infos)
            mutate(altered[-1])
            reject(label, lambda x=altered: installer.namespace(x, expected))

    with tempfile.TemporaryDirectory(prefix='count-installer-controls-') as temporary:
        root = Path(temporary).resolve()
        body = b'ordinary exact input\n'
        pin = (len(body), hashlib.sha256(body).hexdigest())
        fake = {'MANIFEST.json': pin, 'blobs/' + pin[1]: pin}
        target = root / 'inputs'
        target.mkdir()
        (target / 'MANIFEST.json').write_bytes(body)
        assert installer.destination_preflight(target, fake) == {'MANIFEST.json'}
        reject('incomplete-installed-tree', lambda: installer.destination_preflight(target, fake, complete=True))
        (target / 'unknown.txt').write_bytes(b'preserve me')
        reject('extra-destination-file', lambda: installer.destination_preflight(target, fake))
        assert (target / 'unknown.txt').read_bytes() == b'preserve me'
        (target / 'unknown.txt').unlink()
        (target / 'MANIFEST.json').write_bytes(b'preserve mismatch')
        reject('existing-different-input', lambda: installer.destination_preflight(target, fake))
        assert (target / 'MANIFEST.json').read_bytes() == b'preserve mismatch'
        (root / 'linked').symlink_to(target, target_is_directory=True)
        reject('destination-symlink', lambda: installer.destination_preflight(root / 'linked', fake))
        reject('ancestor-symlink', lambda: installer.destination_preflight(root / 'linked/new', fake))
        small = root / 'wrong.zip'
        small.write_bytes(b'not the archive')
        reject('wrong-archive-size', lambda: installer.install(small, root))
        with small.open('wb') as f:
            f.truncate(installer.ARCHIVE_BYTES)
        reject('wrong-archive-hash-same-size', lambda: installer.install(small, root))
        assert not (root / installer.DESTINATION).exists()
    print(json.dumps(dict(status='PASS_BOUNDED_COUNT_INSTALLER_CONTROLS',
         controls=rejected, total=len(rejected), native_arithmetic_executed=False,
         all_law_theorem_verified=False), sort_keys=True))


if __name__ == '__main__':
    main()

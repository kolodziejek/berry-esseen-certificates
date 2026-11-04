"""Small adversarial fixtures for byte preservation; no mathematical tests."""
from pathlib import Path
import argparse
import copy
import gzip
import hashlib
import importlib.util
import io
import json
import shutil
import tarfile

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('evidence_pack', HERE/'evidence_pack_v2.py')
pack = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pack)


def main(output):
    output.mkdir(parents=True, exist_ok=False)
    work = output/'source'
    (work/'runs/case').mkdir(parents=True)
    data = b'{"actual_path":"/original/workspace/runs/case","returncode":0}\n'
    (work/'runs/case/PROCESS.json').write_bytes(data)
    (work/'runs/case/PROCESS-copy.json').write_bytes(data)
    (work/'runs/case/stderr.txt').write_bytes(b'')
    files = {str(p.relative_to(work)):dict(bytes=p.stat().st_size, sha256=pack.sha(p))
             for p in work.rglob('*') if p.is_file()}
    manifest = dict(schema='BE_PRESERVED_EXECUTION_BYTES_V1', files=files,
                    selection={'scope':'test fixture only'}, mathematical_acceptance_claimed=False)
    inventory = output/'inventory.json'
    inventory.write_bytes(pack.encoded(manifest))
    archive = output/'archive'
    result = pack.build(work, inventory, archive, chunk_bytes=113)
    restored = output/'restored'
    baseline = pack.restore(archive/'PACK.json', result['pack_sha256'], restored)
    pack.need({str(p.relative_to(restored)):p.read_bytes() for p in restored.rglob('*') if p.is_file()} ==
              {str(p.relative_to(work)):p.read_bytes() for p in work.rglob('*') if p.is_file()},
              'Exact byte and namespace roundtrip, including original absolute path')
    pack.need(result['files'] == 3 and result['unique_blobs'] == 2 and len(result['chunks']) > 1,
              'Real deduplication and multiple chunks exercised')
    controls = []

    def reject(name, action):
        try:
            action()
        except (ValueError, OSError, KeyError, tarfile.TarError) as error:
            controls.append(dict(name=name, rejected=True, exception=type(error).__name__, reason=str(error)))
        else:
            raise AssertionError('Accepted malformed fixture: '+name)

    reject('wrong pack hash', lambda: pack.restore(archive/'PACK.json', '0'*64, output/'bad-hash'))
    reject('existing destination', lambda: pack.restore(archive/'PACK.json', result['pack_sha256'], restored))
    reject('existing build output', lambda: pack.build(work, inventory, archive))

    def alter_pack(name, mutate):
        directory = output/name
        shutil.copytree(archive, directory)
        value = json.loads((directory/'PACK.json').read_text())
        mutate(value, directory)
        (directory/'PACK.json').write_bytes(pack.encoded(value))
        return lambda: pack.restore(directory/'PACK.json', pack.sha(directory/'PACK.json'), output/(name+'-restore'))

    reject('missing chunk', alter_pack('missing-chunk', lambda p,d:(d/p['chunks'][0]['name']).unlink()))
    reject('reordered chunks', alter_pack('reordered', lambda p,d:p['chunks'].reverse()))
    reject('duplicated chunk', alter_pack('duplicated', lambda p,d:p['chunks'].append(p['chunks'][0])))
    reject('corrupted chunk', alter_pack('corrupt', lambda p,d:(d/p['chunks'][0]['name']).write_bytes(b'x'*p['chunks'][0]['bytes'])))
    reject('wrong whole archive hash', alter_pack('whole-hash', lambda p,d:p['archive'].update(sha256='0'*64)))
    reject('false theorem scope', alter_pack('scope', lambda p,d:p.update(mathematical_acceptance_claimed=True)))
    reject('boolean file count', alter_pack('boolean', lambda p,d:p.update(files=True)))
    reject('wrong complete count', alter_pack('count', lambda p,d:p.update(files=4)))
    reject('chunk path traversal', alter_pack('chunk-path', lambda p,d:p['chunks'][0].update(name='../outside')))

    blob_rows = [('blobs/'+h, next(p.read_bytes() for p in work.rglob('*') if p.is_file() and pack.sha(p)==h))
                 for h in sorted({r['sha256'] for r in files.values()})]

    def malformed_archive(name, raw, blobs):
        directory = output/name
        directory.mkdir()
        buffer = io.BytesIO()
        with gzip.GzipFile(filename='', fileobj=buffer, mode='wb', mtime=0) as gz:
            with tarfile.open(fileobj=gz, mode='w|', format=tarfile.USTAR_FORMAT) as tar:
                pack.add(tar, 'CAPTURE_MANIFEST.json', raw)
                for item, data in blobs:
                    pack.add(tar, item, data)
        data = buffer.getvalue()
        name0 = 'captures.tar.gz.part0000'
        (directory/name0).write_bytes(data)
        value = copy.deepcopy(result)
        value.pop('pack_sha256')
        value['chunks'] = [dict(name=name0, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())]
        value['archive'] = {k:value['chunks'][0][k] for k in ('bytes','sha256')}
        value['manifest'] = dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        (directory/'PACK.json').write_bytes(pack.encoded(value))
        return lambda: pack.restore(directory/'PACK.json', pack.sha(directory/'PACK.json'), output/(name+'-restore'))

    reject('duplicate JSON key', malformed_archive('duplicate-json',
        pack.encoded(manifest).replace(b'"schema":', b'"schema":"bad","schema":', 1), blob_rows))
    for name in ('../outside', '/absolute', '.', 'a/../b', 'a//b', 'a\\b'):
        value = copy.deepcopy(manifest)
        value['files'][name] = value['files'].pop('runs/case/PROCESS-copy.json')
        label = 'bad-path-%02d' % len(controls)
        reject('invalid evidence path '+repr(name), malformed_archive(label, pack.encoded(value), blob_rows))
    value = copy.deepcopy(manifest)
    value['files']['runs/case'] = value['files'].pop('runs/case/PROCESS-copy.json')
    reject('file-directory collision', malformed_archive('path-collision', pack.encoded(value), blob_rows))
    reject('omitted blob', malformed_archive('omitted', pack.encoded(manifest), blob_rows[:-1]))
    reject('duplicate blob', malformed_archive('duplicate-blob', pack.encoded(manifest), blob_rows+blob_rows[:1]))
    reject('undeclared blob', malformed_archive('undeclared', pack.encoded(manifest), blob_rows+[('blobs/'+'0'*64,b'')]))
    nonempty = next(i for i, (_, data) in enumerate(blob_rows) if data)
    h, data = blob_rows[nonempty]
    altered = list(blob_rows)
    altered[nonempty] = (h, b'x'*len(data))
    reject('wrong blob contents', malformed_archive('blob-contents', pack.encoded(manifest), altered))
    linked = output/'symlink'
    linked.symlink_to(restored, target_is_directory=True)
    reject('symlink ancestor', lambda: pack.restore(archive/'PACK.json', result['pack_sha256'], linked/'child'))
    value = copy.deepcopy(manifest)
    value['files']['runs/case/PROCESS.json']['sha256'] = '0'*64
    wrong = output/'wrong-input.json'
    wrong.write_bytes(pack.encoded(value))
    reject('changed selected source', lambda: pack.build(work, wrong, output/'wrong-input-archive'))
    original_chunk_limit, original_archive_limit = pack.MAX_CHUNKS, pack.MAX_ARCHIVE_BYTES
    try:
        pack.MAX_CHUNKS = 1
        reject('builder chunk count exceeds restorer limit',
               lambda: pack.build(work, inventory, output/'too-many-chunks', chunk_bytes=113))
        pack.MAX_CHUNKS = original_chunk_limit
        pack.MAX_ARCHIVE_BYTES = 1
        reject('builder stream size exceeds restorer limit',
               lambda: pack.build(work, inventory, output/'too-many-bytes'))
    finally:
        pack.MAX_CHUNKS, pack.MAX_ARCHIVE_BYTES = original_chunk_limit, original_archive_limit
    report = dict(status='PASS_BYTE_ARCHIVE_CONTROLS', baseline=baseline, controls=controls,
                  control_count=len(controls), real_numerical_arithmetic_executed=False,
                  mathematical_acceptance_claimed=False,
                  tool_sha256=pack.sha(HERE/'evidence_pack_v2.py'), test_sha256=pack.sha(__file__))
    (output/'RESULT.json').write_bytes(pack.encoded(report))
    print(json.dumps(dict(status=report['status'], controls=len(controls))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    main(parser.parse_args().output)

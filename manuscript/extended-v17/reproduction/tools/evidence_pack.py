"""Preserve selected execution bytes in a deduplicated, chunked archive.

This tool checks byte integrity only. It does not execute a certificate checker,
infer completion from logs, or reinterpret recorded absolute paths. A caller
must first select completed immutable evidence using the component inventories.
"""
from pathlib import Path, PurePosixPath
import argparse
import gzip
import hashlib
import io
import json
import os
import re
import tarfile
import tempfile

MAX_FILE = 256 * 1024**2
MAX_MANIFEST = 64 * 1024**2
DEFAULT_CHUNK = 90 * 1024**2


def need(value, message):
    if not value:
        raise ValueError(message)


def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def encoded(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n').encode()


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'Duplicate JSON key')
        result[key] = value
    return result


def parsed(raw):
    def nonfinite(value):
        raise ValueError('Nonfinite JSON: '+value)
    return json.loads(raw, object_pairs_hook=unique, parse_constant=nonfinite)


def relative(name):
    need(type(name) is str and name and '\\' not in name and '\0' not in name,
         'Ordinary relative path')
    p = PurePosixPath(name)
    need(p.parts and not p.is_absolute() and p.as_posix() == name and all(x not in ('.', '..') for x in p.parts),
         'Canonical contained path')
    return p.parts


def ordinary(path):
    path = Path(path).absolute()
    for p in (path, *path.parents):
        need(not p.is_symlink(), 'No symlink ancestor: '+str(p))
    return path


def pin(row, maximum=MAX_FILE):
    need(type(row) is dict and set(row) == {'sha256', 'bytes'}, 'Exact byte pin')
    need(type(row['sha256']) is str and re.fullmatch('[0-9a-f]{64}', row['sha256']), 'SHA256 pin')
    need(type(row['bytes']) is int and 0 <= row['bytes'] <= maximum, 'Bounded integer size')


def validate_manifest(value):
    need(type(value) is dict and set(value) == {'schema', 'files', 'selection', 'mathematical_acceptance_claimed'},
         'Exact evidence manifest schema')
    need(value['schema'] == 'BE_PRESERVED_EXECUTION_BYTES_V1'
         and value['mathematical_acceptance_claimed'] is False, 'Byte preservation only')
    need(type(value['selection']) is dict, 'Explicit selection provenance')
    files = value['files']
    need(type(files) is dict and files, 'Nonempty explicit evidence selection')
    for name, row in files.items():
        relative(name)
        pin(row)
    names = set(files)
    for name in names:
        need(not any(p.as_posix() in names for p in PurePosixPath(name).parents),
             'No file/directory path collision')
    return files


def add(tar, name, data):
    info = tarfile.TarInfo(name)
    info.size, info.mode, info.mtime = len(data), 0o644, 0
    info.uid = info.gid = 0
    info.uname = info.gname = ''
    tar.addfile(info, io.BytesIO(data))


def build(workspace, inventory, output, chunk_bytes=DEFAULT_CHUNK):
    workspace, output = ordinary(workspace), ordinary(output)
    need(type(chunk_bytes) is int and 1 <= chunk_bytes <= DEFAULT_CHUNK, 'Bounded positive chunk size')
    need(not output.exists(), 'Create-only archive directory')
    raw = Path(inventory).read_bytes()
    need(len(raw) <= MAX_MANIFEST, 'Bounded input manifest')
    value = parsed(raw)
    files = validate_manifest(value)
    raw = encoded(value)
    need(len(raw) <= MAX_MANIFEST, 'Bounded canonical manifest')
    blobs = {}
    for name, row in sorted(files.items()):
        source = ordinary(workspace.joinpath(*relative(name)))
        need(source.is_file() and source.stat().st_size == row['bytes'] and sha(source) == row['sha256'],
             'Selected source bytes: '+name)
        if row['sha256'] in blobs:
            need(blobs[row['sha256']][1] == row['bytes'], 'Consistent repeated blob size')
        else:
            blobs[row['sha256']] = (source, row['bytes'])
    output.mkdir(parents=True)
    (output/'CAPTURE_MANIFEST.json').write_bytes(raw)
    # Temporary complete stream is removed after its pinned chunks are written.
    with tempfile.TemporaryFile(dir=output) as stream:
        with gzip.GzipFile(filename='', fileobj=stream, mode='wb', mtime=0, compresslevel=6) as gz:
            with tarfile.open(fileobj=gz, mode='w|', format=tarfile.USTAR_FORMAT) as tar:
                add(tar, 'CAPTURE_MANIFEST.json', raw)
                for h, (source, length) in sorted(blobs.items()):
                    data = source.read_bytes()
                    need(len(data) == length and hashlib.sha256(data).hexdigest() == h, 'Stable archive input')
                    add(tar, 'blobs/'+h, data)
        stream.seek(0)
        digest, total, chunks = hashlib.sha256(), 0, []
        while data := stream.read(chunk_bytes):
            name = 'captures.tar.gz.part%04d' % len(chunks)
            (output/name).write_bytes(data)
            digest.update(data)
            total += len(data)
            chunks.append(dict(name=name, bytes=len(data), sha256=hashlib.sha256(data).hexdigest()))
    pack = dict(schema='BE_CHUNKED_EXECUTION_ARCHIVE_V1', chunks=chunks,
                archive=dict(bytes=total, sha256=digest.hexdigest()),
                manifest=dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest()),
                files=len(files), unique_blobs=len(blobs),
                logical_bytes=sum(r['bytes'] for r in files.values()),
                unique_bytes=sum(v[1] for v in blobs.values()),
                mathematical_acceptance_claimed=False, recorded_paths_rewritten=False)
    (output/'PACK.json').write_bytes(encoded(pack))
    return dict(pack_sha256=sha(output/'PACK.json'), **pack)


def restore(pack_path, pack_sha256, workspace):
    pack_path, workspace = ordinary(pack_path), ordinary(workspace)
    need(pack_path.is_file() and pack_path.stat().st_size <= MAX_MANIFEST, 'Bounded pack description')
    need(sha(pack_path) == pack_sha256, 'Trusted pack description hash')
    pack = parsed(pack_path.read_bytes())
    need(type(pack) is dict and set(pack) == {'schema', 'chunks', 'archive', 'manifest', 'files',
        'unique_blobs', 'logical_bytes', 'unique_bytes', 'mathematical_acceptance_claimed',
        'recorded_paths_rewritten'}, 'Exact pack schema')
    need(pack['schema'] == 'BE_CHUNKED_EXECUTION_ARCHIVE_V1'
         and pack['mathematical_acceptance_claimed'] is False and pack['recorded_paths_rewritten'] is False,
         'Literal preservation scope')
    pin(pack['archive'], 64*1024**3)
    pin(pack['manifest'], MAX_MANIFEST)
    need(type(pack['chunks']) is list and 0 < len(pack['chunks']) <= 10000, 'Bounded nonempty chunk sequence')
    need(not workspace.exists(), 'Restore into an absent workspace only')
    workspace.parent.mkdir(parents=True, exist_ok=True)
    # Validate the entire compressed stream before creating any restored file.
    with tempfile.TemporaryFile(dir=workspace.parent) as stream:
        digest, total = hashlib.sha256(), 0
        for i, row in enumerate(pack['chunks']):
            need(type(row) is dict and set(row) == {'name', 'bytes', 'sha256'}, 'Exact chunk entry')
            need(row['name'] == 'captures.tar.gz.part%04d' % i, 'Complete ordered chunk sequence')
            pin({k: row[k] for k in ('bytes', 'sha256')}, DEFAULT_CHUNK)
            path = ordinary(pack_path.parent/row['name'])
            need(path.is_file() and path.stat().st_size == row['bytes'], 'Present complete chunk')
            data = path.read_bytes()
            need(hashlib.sha256(data).hexdigest() == row['sha256'], 'Whole chunk hash')
            stream.write(data)
            digest.update(data)
            total += len(data)
        need(total == pack['archive']['bytes'] and digest.hexdigest() == pack['archive']['sha256'],
             'Whole compressed archive identity')
        stream.seek(0)
        with tarfile.open(fileobj=stream, mode='r:gz') as tar:
            first = tar.next()
            need(first is not None and first.name == 'CAPTURE_MANIFEST.json' and first.isfile()
                 and first.size == pack['manifest']['bytes'], 'One leading regular pinned manifest')
            raw = tar.extractfile(first).read()
            need(hashlib.sha256(raw).hexdigest() == pack['manifest']['sha256'], 'Whole manifest hash')
            manifest = parsed(raw)
            files = validate_manifest(manifest)
            destinations = {}
            for name, row in files.items():
                destinations.setdefault(row['sha256'], []).append((name, row['bytes']))
            need(all(type(pack[k]) is int for k in ('files', 'unique_blobs', 'logical_bytes', 'unique_bytes')),
                 'Integer inventory counts')
            need((len(files), len(destinations), sum(r['bytes'] for r in files.values()),
                  sum(rows[0][1] for rows in destinations.values())) ==
                 tuple(pack[k] for k in ('files', 'unique_blobs', 'logical_bytes', 'unique_bytes')),
                 'Exact complete inventory counts')
            workspace.mkdir()
            seen = set()
            while member := tar.next():
                need(member.isfile() and member.name.startswith('blobs/') and len(member.name) == 70,
                     'Regular closed blob namespace')
                h = member.name[6:]
                need(h in destinations and h not in seen, 'Unique declared evidence blob')
                rows = destinations[h]
                need(all(length == member.size <= MAX_FILE for _, length in rows), 'Whole blob length')
                data = tar.extractfile(member).read()
                need(len(data) == member.size and hashlib.sha256(data).hexdigest() == h, 'Whole evidence hash')
                for name, _ in rows:
                    target = ordinary(workspace.joinpath(*relative(name)))
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with target.open('xb') as destination:
                        destination.write(data)
                    os.chmod(target, 0o644)
                seen.add(h)
            need(seen == set(destinations), 'No missing evidence blob')
    return dict(status='PASS_BYTE_PRESERVATION_ONLY', files=len(files), unique_blobs=len(seen),
                pack_sha256=pack_sha256, recorded_paths_rewritten=False,
                mathematical_acceptance_claimed=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    b = sub.add_parser('build')
    b.add_argument('--workspace', type=Path, required=True)
    b.add_argument('--inventory', type=Path, required=True)
    b.add_argument('--output', type=Path, required=True)
    r = sub.add_parser('restore')
    r.add_argument('--pack', type=Path, required=True)
    r.add_argument('--pack-sha256', required=True)
    r.add_argument('--workspace', type=Path, required=True)
    args = parser.parse_args()
    result = build(args.workspace, args.inventory, args.output) if args.action == 'build' else restore(
        args.pack, args.pack_sha256, args.workspace)
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()

"""Restore the pinned public COUNT candidate inputs, without running checkers.

No network access, historical PASS adoption, or replacement of existing files.
All archive bytes and members are checked before destination writes begin.
"""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import os
import re
import stat
import sys
import zipfile

ARCHIVE_BYTES = 94179896
ARCHIVE_SHA256 = '5c08ddbd642e5da7eea9d7053df721a89bdce1e91a17c82cc46b2a66c34a84e0'
MANIFEST_BYTES = 1762067
MANIFEST_SHA256 = '0431403e05326655f316991eae6fcdaa8c64bef244f055a40e1dc6958c892f5f'
REGISTRY_SHA256 = 'f5ddd40aefe85b5ce036b2c23fe540c2032997bf8a51f4999a08573e9a4c34f7'
DESTINATION = Path('work/unconditional_legacy_20261030/certificates/count')
URL = 'https://github.com/rodziewiczk/berry-esseen-certificates/releases/download/v0.1.0/count-candidates.zip'
TOTAL_BYTES = 1249228509
MIB = 1024 * 1024


def need(ok, message):
    if not ok:
        raise ValueError(message)


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'Duplicate JSON key: ' + key)
        result[key] = value
    return result


def stream_pin(stream):
    h = hashlib.sha256()
    size = 0
    while True:
        block = stream.read(MIB)
        if not block:
            return size, h.hexdigest()
        size += len(block)
        h.update(block)


def ordinary_path(path, directory=False, missing=False):
    """Do not resolve away a symlink before inspecting every existing ancestor."""
    p = Path(os.path.abspath(os.fspath(path)))
    for node in [*reversed(p.parents), p]:
        try:
            mode = node.lstat().st_mode
        except FileNotFoundError:
            need(missing, 'Missing required path: ' + str(node))
            continue
        wanted = stat.S_ISDIR if node != p or directory else stat.S_ISREG
        need(wanted(mode), 'Only ordinary files/directories, no links: ' + str(node))
    return p


def file_pin(path):
    p = ordinary_path(path)
    with p.open('rb') as stream:
        return stream_pin(stream)


def candidate_inventory(raw):
    need(len(raw) == MANIFEST_BYTES and hashlib.sha256(raw).hexdigest() == MANIFEST_SHA256,
         'Pinned complete original candidate manifest')
    d = json.loads(raw, object_pairs_hook=unique)
    need(d['schema'] == 'be.public-untrusted-count-candidates/1'
         and d['registry_sha256'] == REGISTRY_SHA256
         and d['required_jobs'] == d['available_jobs'] == d['unique_candidate_blobs'] == 1243
         and len(d['jobs']) == 1243 and not d['missing_jobs'] and not d['rejected_locators']
         and d['all_required_candidates_available'] is True,
         'Complete public candidate selection')
    for key in ('all_index_full_pass', 'authority_executed', 'historical_acceptance_adopted',
                'mathematical_proof_accepted', 'private_control_payloads_read'):
        need(d[key] is False, 'Inputs have no verification authority')
    expected = {'MANIFEST.json': (MANIFEST_BYTES, MANIFEST_SHA256)}
    roles = Counter()
    for job, row in d['jobs'].items():
        need(re.fullmatch(r'[A-Za-z0-9_.-]+', job) is not None, 'Safe original job ID')
        c = row['candidate']
        name, pin, size = c['path'], c['sha256'], c['bytes']
        need(re.fullmatch(r'[0-9a-f]{64}', pin) is not None
             and name == 'blobs/' + pin and name not in expected
             and type(size) is int and 0 < size <= 32 * MIB
             and row['fresh_native_accept_required'] is True
             and row['mathematical_acceptance'] is False,
             'Distinct bounded original untrusted candidate')
        expected[name] = (size, pin)
        roles[row['role']] += 1
    need(dict(roles) == d['role_counts'] == {'C5-one-free': 295, 'current-C2639': 300,
         'projected-C1019': 364, 'projected-C69': 284}
         and sum(size for size, _ in expected.values()) == TOTAL_BYTES
         and d['unique_candidate_bytes'] == TOTAL_BYTES - MANIFEST_BYTES,
         'Whole job and byte census')
    return expected


def namespace(infos, expected):
    """Reject aliases, duplicates, extra entries and special archive members."""
    seen = set()
    folded = set()
    for info in infos:
        name = info.filename
        need(name == 'MANIFEST.json' or re.fullmatch(r'blobs/[0-9a-f]{64}', name) is not None,
             'Literal closed COUNT namespace')
        need(name not in seen and name.casefold() not in folded, 'Unique archive member')
        seen.add(name)
        folded.add(name.casefold())
        mode = info.external_attr >> 16
        need(not info.is_dir() and stat.S_IFMT(mode) in (0, stat.S_IFREG)
             and not info.flag_bits & 1 and info.compress_type in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED),
             'Only unencrypted ordinary data members')
        need(name in expected and info.file_size == expected[name][0], 'Exact member size and identity')
    need(seen == set(expected), 'Complete exact archive namespace')


def destination_preflight(destination, expected, complete=False):
    destination = ordinary_path(destination, directory=True, missing=not complete)
    found = set()
    if destination.exists():
        for path in destination.rglob('*'):
            name = path.relative_to(destination).as_posix()
            mode = path.lstat().st_mode
            if stat.S_ISDIR(mode):
                need(name == 'blobs', 'No unknown destination directories')
            else:
                need(stat.S_ISREG(mode) and name in expected, 'No destination links or extra files')
                need(file_pin(path) == expected[name], 'Existing input differs; never overwrite: ' + name)
                found.add(name)
    need(not complete or found == set(expected), 'Every original input must be installed')
    return found


def install(archive, workspace, verify_only=False):
    need(__debug__ and not sys.flags.optimize, 'Unoptimized Python required')
    archive = ordinary_path(archive)
    workspace = ordinary_path(workspace, directory=True)
    destination = workspace / DESTINATION
    need(file_pin(archive) == (ARCHIVE_BYTES, ARCHIVE_SHA256), 'Whole pinned public ZIP size/SHA')
    with zipfile.ZipFile(archive) as z:
        infos = z.infolist()
        need(len(infos) == 1244, 'Exactly1244 original file members')
        manifests = [x for x in infos if x.filename == 'MANIFEST.json']
        need(len(manifests) == 1 and manifests[0].file_size == MANIFEST_BYTES,
             'Unique bounded candidate manifest')
        expected = candidate_inventory(z.read(manifests[0]))
        namespace(infos, expected)
        # This full pass also checks CRCs and bounds every decompressed member
        # before creating any target file or directory.
        for info in infos:
            with z.open(info) as stream:
                need(stream_pin(stream) == expected[info.filename], 'Whole original member SHA: ' + info.filename)
        found = destination_preflight(destination, expected, complete=verify_only)
        created = 0
        if not verify_only:
            destination.mkdir(parents=True, exist_ok=True)
            ordinary_path(destination, directory=True)
            for info in infos:
                target = destination / info.filename
                if info.filename in found:
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                ordinary_path(target.parent, directory=True)
                # Exclusive creation never truncates an existing source/result.
                flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_NOFOLLOW', 0)
                descriptor = os.open(target, flags, 0o644)
                with os.fdopen(descriptor, 'wb') as out, z.open(info) as source:
                    while True:
                        block = source.read(MIB)
                        if not block:
                            break
                        out.write(block)
                need(file_pin(target) == expected[info.filename], 'New input byte equality')
                created += 1
        destination_preflight(destination, expected, complete=True)
    need(file_pin(archive) == (ARCHIVE_BYTES, ARCHIVE_SHA256), 'Archive unchanged during restoration')
    return dict(schema='PORTABLE_PUBLIC_COUNT_INPUT_RESTORATION_V1',
         archive=str(archive), archive_bytes=ARCHIVE_BYTES, archive_sha256=ARCHIVE_SHA256,
         asset_url=URL, destination=str(destination), manifest_sha256=MANIFEST_SHA256,
         files=1244, candidates=1243, uncompressed_bytes=TOTAL_BYTES,
         files_created=created, identical_existing_files=len(found), verify_only=verify_only,
         network_used=False, existing_files_overwritten=False, native_arithmetic_executed=False,
         historical_acceptance_adopted=False, all_law_theorem_verified=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--verify-only', action='store_true')
    a = parser.parse_args()
    print(json.dumps(install(a.archive, a.workspace, a.verify_only), sort_keys=True))


if __name__ == '__main__':
    main()

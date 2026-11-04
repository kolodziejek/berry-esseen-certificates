"""One bounded integrity pass over the actual publication assets; no restore."""
from pathlib import Path
import hashlib
import json
import stat

BASE = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
PUB = BASE / 'work/manuscript_revision_20261029/manuscript/extended-v17/reproduction'
RELEASE = BASE / 'work/extension_release_20261030'
PACK_PINS = {
    'evidence-base01': '70a93bf2d51fdba55c4bd4ed353f80f1fe011d7e5e9e86cc39445b3d7d3137d3',
    'evidence-finite01': 'e46d1622b8c4cbe4d43566d22d3af4c5a4cdee4888a7f91b156cc6f2d0ebc3d9',
    'evidence-final01': '2f37b3754679b774a7caba1f5deb52b98a607057c25eb4d33fe3f1983e04cca1',
}
UNFROZEN_DOCS = {'COMPLETION.md', 'COMPLETION_LEDGER.json', 'EVIDENCE.md'}
hashes = {}


def read(path):
    return json.loads(path.read_text())


def digest(path, combined=None):
    key = str(path)
    if key in hashes:
        assert combined is None, 'No duplicated large chunk pass'
        return hashes[key]
    assert path.is_file() and not path.is_symlink()
    assert all(not parent.is_symlink() for parent in path.parents)
    before = path.stat()
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
            if combined is not None:
                combined.update(block)
    after = path.stat()
    assert (before.st_ino, before.st_size, before.st_mtime_ns) == (after.st_ino, after.st_size, after.st_mtime_ns)
    hashes[key] = h.hexdigest()
    return hashes[key]


assert __debug__
source_path = PUB / 'SOURCE_ASSETS_V3.json'
assert digest(source_path) == digest(RELEASE / 'SOURCE_ASSETS_V3.json')
source = read(source_path)
assert source['schema'] == 'BE_EXTENSION_SOURCE_ASSETS_V3'
assert len(source['assets']) == 4 and len(source['tools']) == 9
assert [row['id'] for row in source['assets']] == ['framework', 'foundations', 'n5', 'finite']
assets = []
framework_entries = None
for row in source['assets']:
    archive = PUB / row['archive']
    manifest = PUB / row['manifest']
    assert archive.stat().st_size == row['bytes'] and digest(archive) == row['archive_sha256']
    assert digest(manifest) == row['manifest_sha256']
    data = read(manifest)
    assert list(sorted(data['trees'])) == list(sorted(row['trees']))
    entries = {tree + '/' + name: pin for tree, files in data['trees'].items() for name, pin in files.items()}
    assert len(entries) == row['logical_files']
    if row['id'] == 'framework':
        framework_entries = entries
    assets.append(dict(id=row['id'], archive=row['archive'], archive_bytes=archive.stat().st_size,
        archive_sha256=digest(archive), manifest=row['manifest'], manifest_sha256=digest(manifest),
        logical_files=len(entries)))

tools = {}
for name, pin in source['tools'].items():
    path = PUB / 'tools' / name
    assert path.stat().st_size == pin['bytes'] and digest(path) == pin['sha256']
    tools[name] = pin
inventory = PUB / source['framework_inventory']
assert digest(inventory) == source['framework_inventory_sha256']
assert len(read(inventory)['files']) == 4700 and read(inventory)['files'] == framework_entries
index = PUB / 'REPRODUCTION_INDEX_V1.json'
assert digest(index) == source['reproduction_index_sha256']
assert len(read(index)['nodes']) == 114 and len(read(index)['sequential_order']) == 114
for name, pin in source['framework_supplements'].items():
    assert digest(PUB / 'manifests' / name) == pin
assert read(PUB / 'COUNT_CANDIDATE_ASSET.json') == source['external_count_asset']
assert digest(PUB / 'tools/install_count_candidates.py') == source['external_count_asset']['installer_sha256']

packs = []
for name, expected in PACK_PINS.items():
    directory = PUB / 'assets' / name
    pack_path = directory / 'PACK.json'
    assert digest(pack_path) == expected
    pack = read(pack_path)
    assert pack['schema'] == 'BE_CHUNKED_EXECUTION_ARCHIVE_V1'
    assert pack['mathematical_acceptance_claimed'] is False and pack['recorded_paths_rewritten'] is False
    assert {path.name for path in directory.iterdir()} == {'PACK.json'} | {row['name'] for row in pack['chunks']}
    combined = hashlib.sha256()
    total = 0
    for i, row in enumerate(pack['chunks']):
        assert row['name'] == f'captures.tar.gz.part{i:04d}'
        path = directory / row['name']
        assert path.stat().st_size == row['bytes'] and digest(path, combined) == row['sha256']
        total += row['bytes']
    assert total == pack['archive']['bytes'] and combined.hexdigest() == pack['archive']['sha256']
    packs.append(dict(id=name, pack_sha256=expected, chunks=pack['chunks'], archive=pack['archive'],
        files=pack['files'], logical_bytes=pack['logical_bytes'],
        ordered_complete_compressed_identity_verified=True))

files = {}
unfrozen = []
for path in sorted(PUB.rglob('*')):
    mode = path.lstat().st_mode
    assert not stat.S_ISLNK(mode), path
    if stat.S_ISDIR(mode):
        continue
    assert stat.S_ISREG(mode) and path.stat().st_size < 100000000, path
    relative = path.relative_to(PUB).as_posix()
    if path.name in UNFROZEN_DOCS:
        unfrozen.append(relative)
    else:
        files[relative] = dict(bytes=path.stat().st_size, sha256=digest(path))
result = dict(status='PASS_ACTUAL_PUBLICATION_ASSET_BYTE_AUDIT',
    publication_root=PUB.relative_to(BASE).as_posix(), source_assets_sha256=digest(source_path),
    source_assets_match_frozen_release=True, four_source_assets=assets, nine_tool_pins=tools,
    framework_inventory_sha256=digest(inventory), framework_files=4700,
    framework_manifest_and_inventory_maps_identical=True,
    reproduction_index_sha256=digest(index), index_nodes=114, evidence_packs=packs,
    ordinary_frozen_files=files, all_observed_files_strictly_under_100000000_bytes=True,
    no_symlinks=True, unfrozen_docs_not_hashed=unfrozen,
    documentation_pins_claimed=False, external_COUNT_download_attempted=False,
    archive_restoration_performed=False, native_calculations_performed=False,
    mathematical_acceptance_claimed=False, checker_sha256=digest(Path(__file__)))
with (HERE / 'RESULT.json').open('x') as stream:
    json.dump(result, stream, indent=2, sort_keys=True)
    stream.write('\n')
print(json.dumps(dict(status=result['status'], source_assets=4, tools=9, framework_files=4700,
    index_nodes=114, evidence_packs=3, frozen_files=len(files), restored_or_executed=False)), flush=True)

"""Bounded source-location search; no archived program is imported or run."""
from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZipFile

pins = json.loads(Path('mathematics/global-contract.json').read_text())['source_pins']
names = (
    'current_tail49_mathematical_assembly.py',
    'current_tail49_constant_bounds.py',
    'current61_mathematical_assembly.py',
    'newglobal-v2/completed_static.py',
)
results = []
for filename in ('BE_cutoff49_20260930.zip', 'backend.zip'):
    path = Path('verification/finite-tail/sources') / filename
    with ZipFile(path) as archive:
        matches = {name: [] for name in names}
        for entry in archive.infolist():
            if entry.is_dir():
                continue
            digest = sha256(archive.read(entry)).hexdigest()
            for name in names:
                if digest == pins[name]:
                    matches[name].append(entry.filename)
        results.append(dict(archive=str(path), members=len(archive.infolist()),
                            pinned_provider_body_matches=matches))
print(json.dumps(dict(
    scope='Direct members of two archives only; other packages and nested archives unsearched.',
    source_programs_executed=0, results=results), indent=2, sort_keys=True))

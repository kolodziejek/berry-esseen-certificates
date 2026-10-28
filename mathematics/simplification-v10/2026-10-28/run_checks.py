"""Reproduce only the bounded v10 arithmetic checks; no discovery imports."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys
import time

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions must remain enabled')
root = Path(__file__).resolve().parents[3]
source = Path(__file__).resolve().parent
if (source/'small-noise.tex').read_bytes() != (source/'small-noise-proof/proof.tex').read_bytes():
    raise RuntimeError('The standalone project copy differs from the canonical proof')
if len(sys.argv) != 2 or not sys.argv[1].isalnum():
    raise SystemExit('Supply a new alphanumeric run identifier')
out = root/'runs/simplification-v10-20261028'/sys.argv[1]
out.mkdir(parents=True, exist_ok=False)
names = [
    'primitives_check.py', 'counts_check.py',
    'geometry-check.py', 'geometry-panels.py', 'geometry-laws.py',
    'geometry-independent.py', 'small_noise_check.py',
    'small_noise_review_check.py',
    'moderate_noise_check.py', 'moderate_noise_independent.py',
]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def check(name):
    path = source/name
    before = sha(path)
    cmd = [sys.executable, '-I', '-B', str(path)]
    if name == 'moderate_noise_independent.py':
        cmd.append(str(root))
    start = time.monotonic()
    result = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
    (out/(name+'.stdout.json')).write_text(result.stdout)
    (out/(name+'.stderr.txt')).write_text(result.stderr)
    record = {'command': cmd, 'returncode': result.returncode,
              'elapsed_seconds': time.monotonic()-start,
              'source_sha256': before, 'source_unchanged': sha(path)==before}
    if result.returncode == 0:
        data = json.loads(result.stdout)
        record['status'] = data.get('status')
    return name, record

with ThreadPoolExecutor(max_workers=4) as pool:
    records = dict(pool.map(check, names))
success = all(r['returncode']==0 and r['source_unchanged'] and
              str(r.get('status', '')).startswith('PASS')
              for r in records.values())
receipt = {'status': 'PASS_BOUNDED_V10_COMPONENT_CHECKS' if success else 'FAILED',
           'checks': records, 'python': sys.version,
           'time_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'script_sha256': sha(Path(__file__)),
           'proof_pins': {p.name: sha(p) for p in source.glob('*.tex')},
           'scope': 'Bounded component arithmetic, not a full theorem or ancestor replay'}
(out/'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps({'status': receipt['status'],
                  'checks': {k: v.get('status', v['returncode']) for k,v in records.items()},
                  'receipt': str(out/'receipt.json')}, indent=2))
if not success:
    raise SystemExit(1)

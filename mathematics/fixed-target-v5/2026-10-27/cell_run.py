#!/usr/bin/env python3
"""Record one bounded scalar run; refuses to overwrite an evidence directory."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]
BASE=Path('mathematics/fixed-target-v5/2026-10-27')
if len(sys.argv)!=2 or not sys.argv[1].isalnum():raise SystemExit('one alphanumeric run id')
out=ROOT/'runs/fixed-target-v5-20261027'/sys.argv[1]
out.mkdir(parents=True,exist_ok=False)
inputs=[BASE/'cell_check.py',BASE/'cell-input.json',*sorted((ROOT/BASE/'cell-sources').glob('*.py'))]
inputs=[p if not p.is_absolute() else p.relative_to(ROOT) for p in inputs]
hashes={str(p):sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}
argv=[sys.executable,str(BASE/'cell_check.py'),str(BASE/'cell-input.json')]
start=datetime.now(timezone.utc).isoformat()
result=subprocess.run(argv,cwd=ROOT,capture_output=True)
end=datetime.now(timezone.utc).isoformat()
(out/'check.stdout.json').write_bytes(result.stdout)
(out/'check.stderr.txt').write_bytes(result.stderr)
receipt=dict(argv=argv,cwd=str(ROOT),python_version=sys.version,optimization=sys.flags.optimize,
 started_utc=start,ended_utc=end,returncode=result.returncode,inputs_sha256=hashes,
 stdout_sha256=sha256(result.stdout).hexdigest(),stderr_sha256=sha256(result.stderr).hexdigest(),
 scope='24 new uncharged coarse rho cells; no dense signed stage, native acceptor or local LOW campaign.')
(out/'check-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
if not result.returncode:
 obj=json.loads(result.stdout)
 for key in ('normalized_raw_upper','old_source_normalized_upper','minimum_license_margin_lower','rejected_controls'):
  print(key,obj[key])
raise SystemExit(result.returncode)

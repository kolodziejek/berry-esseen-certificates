#!/usr/bin/env python3
"""Save one bounded moment calculation; refuse an existing output directory."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[3]
BASE=Path('mathematics/fixed-target-v6/2026-10-27')
OLD=Path('mathematics/fixed-target-v5/2026-10-27')
if len(sys.argv)!=2 or not sys.argv[1].isalnum():raise SystemExit('one alphanumeric run id')
out=ROOT/'runs/fixed-target-v6-20261027'/sys.argv[1];out.mkdir(parents=True,exist_ok=False)
inputs=[BASE/'moment_check.py',BASE/'moment_run.py',OLD/'cell_check.py',OLD/'cell-input.json',*sorted((ROOT/OLD/'cell-sources').glob('*.py'))]
inputs=[p if not p.is_absolute() else p.relative_to(ROOT) for p in inputs]
argv=[sys.executable,str(BASE/'moment_check.py')]
start=datetime.now(timezone.utc).isoformat();r=subprocess.run(argv,cwd=ROOT,capture_output=True);end=datetime.now(timezone.utc).isoformat()
(out/'moment.stdout.json').write_bytes(r.stdout);(out/'moment.stderr.txt').write_bytes(r.stderr)
receipt=dict(argv=argv,cwd=str(ROOT),python_version=sys.version,optimization=sys.flags.optimize,started_utc=start,ended_utc=end,returncode=r.returncode,
 inputs_sha256={str(p):sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},stdout_sha256=sha256(r.stdout).hexdigest(),stderr_sha256=sha256(r.stderr).hexdigest())
(out/'moment-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('returncode',r.returncode)
if r.returncode:print(r.stderr.decode())
else:
 from fractions import Fraction as F
 o=json.loads(r.stdout)
 for row in o['summaries']:print({k:float(F(v)) if isinstance(v,str) else v for k,v in row.items()})
 print('controls',o['controls'])
raise SystemExit(r.returncode)

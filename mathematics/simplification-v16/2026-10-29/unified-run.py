"""Source-bound fresh replay; never overwrites an earlier receipt."""
from pathlib import Path
import datetime
import hashlib
import json
import platform
import subprocess
import sys
import time

if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
if len(sys.argv)!=2 or not sys.argv[1].isalnum():raise SystemExit('usage: unified-run.py DISTINCT_ALPHANUMERIC_RUN_ID')
here=Path(__file__).resolve().parent
root=here.parents[2]
out=root/'runs'/'unified-v16-20261029'/sys.argv[1]
out.mkdir(parents=True,exist_ok=False)
sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(here.glob('unified-*')) if p.suffix in ('.py','.tex')}
receipt={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),
         'sources':sources,'commands':[],'scope':'Bounded scalar acceptance and exact actual-law controls; no historical driver run'}
for script in ('unified-check.py','unified-actual.py'):
    start=time.monotonic();command=[sys.executable,str(here/script)]
    result=subprocess.run(command,cwd=root,text=True,capture_output=True)
    (out/(script+'.stdout.json')).write_text(result.stdout)
    (out/(script+'.stderr.txt')).write_text(result.stderr)
    receipt['commands'].append({'command':command,'returncode':result.returncode,'elapsed_seconds':time.monotonic()-start})
    (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    if result.returncode:raise SystemExit(result.returncode)
receipt['status']='PASS_UNIFIED_CHECKS'
(out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':receipt['status'],'receipt':str(out/'receipt.json'),'commands':receipt['commands']},indent=2))

#!/usr/bin/env python3
"""Fresh source-bound exact replay; never overwrites an earlier run."""
from pathlib import Path
import datetime,hashlib,json,platform,subprocess,sys,time
here=Path(__file__).resolve().parent;root=here.parents[2]
name=sys.argv[1] if len(sys.argv)>1 else 'check01'
run=root/'runs/loss-v14-20261028'/name;run.mkdir(parents=True,exist_ok=False)
cmd=[sys.executable,'-I','-B',str(here/'loss-check.py')]
tick=time.monotonic();start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
(run/'stdout.json').write_text(p.stdout);(run/'stderr.txt').write_text(p.stderr)
inputs=[here/'loss-closure.tex',here/'loss-common.tex',here/'loss-check.py',Path(__file__).resolve()]
receipt={'command':cmd,'cwd':str(root),'started_utc':start,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'returncode':p.returncode,'python':sys.version,'platform':platform.platform(),'input_sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in inputs}}
(run/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
if p.returncode:print(p.stdout);print(p.stderr,file=sys.stderr)
else:
    result=json.loads(p.stdout);print(json.dumps({k:v for k,v in result.items() if k!='phase_cases'},indent=2))
raise SystemExit(p.returncode)

#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,platform,subprocess,sys,time
here=Path(__file__).resolve().parent;root=here.parents[2]
p=argparse.ArgumentParser();p.add_argument('run_id');a=p.parse_args()
run=root/'runs/loss-v15-20261028'/a.run_id;run.mkdir(parents=True,exist_ok=False)
cmd=[sys.executable,'-I','-B',str(here/'loss-direct-check.py')]
start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
r=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
(run/'stdout.json').write_text(r.stdout);(run/'stderr.txt').write_text(r.stderr)
receipt={'command':cmd,'cwd':str(root),'started_utc':start,
 'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'elapsed_seconds':time.monotonic()-tick,'returncode':r.returncode,
 'python':sys.version,'platform':platform.platform(),
 'hashes':{f:hashlib.sha256((here/f).read_bytes()).hexdigest()
           for f in ['loss-direct.tex','loss-direct-check.py','loss-direct-run.py']}}
(run/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2));print(r.stdout);print(r.stderr,file=sys.stderr)
raise SystemExit(r.returncode)

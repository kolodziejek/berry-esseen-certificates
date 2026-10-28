#!/usr/bin/env python3
"""Fresh independent crossing review receipt. No constructor code imported."""
import argparse, datetime, hashlib, json, platform, subprocess, sys, time
from pathlib import Path
here=Path(__file__).resolve().parent; root=here.parents[2]
p=argparse.ArgumentParser();p.add_argument('run_id');p.add_argument('--source',type=Path,default=here/'crossing.tex');a=p.parse_args()
source=a.source.resolve(); assert source.is_file(),source
run=root/'runs/finite-v13-20261028'/a.run_id;run.mkdir(parents=True,exist_ok=False)
cmd=[sys.executable,'-I','-B',str(here/'crossing-independent-review.py'),str(source)]
start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic();proc=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
(run/'stdout.json').write_text(proc.stdout);(run/'stderr.txt').write_text(proc.stderr)
receipt={'command':cmd,'cwd':str(root),'started_utc':start,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'returncode':proc.returncode,'python':sys.version,'platform':platform.platform(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256((here/'crossing-independent-review.py').read_bytes()).hexdigest()}
(run/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2));print(proc.stdout);print(proc.stderr,file=sys.stderr);raise SystemExit(proc.returncode)

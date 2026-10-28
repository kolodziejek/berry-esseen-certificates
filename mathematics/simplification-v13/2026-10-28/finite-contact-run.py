#!/usr/bin/env python3
"""Record a fresh bounded finite-contact check without replacing any run."""
from pathlib import Path
import datetime, hashlib, json, platform, subprocess, sys, time
here=Path(__file__).resolve().parent
root=here.parents[2]
name=sys.argv[1] if len(sys.argv)>1 else 'check01'
run=root/'runs/finite-v13-20261028'/name
run.mkdir(parents=True,exist_ok=False)
cmd=[sys.executable,'-I','-B',str(here/'finite-contact-check.py')]
start=datetime.datetime.now(datetime.timezone.utc).isoformat(); tick=time.monotonic()
proc=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
(run/'stdout.txt').write_text(proc.stdout); (run/'stderr.txt').write_text(proc.stderr)
inputs=[here/'finite-contact.tex',here/'finite-contact-check.py',Path(__file__).resolve()]
receipt={'command':cmd,'cwd':str(root),'started_utc':start,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'returncode':proc.returncode,'python':sys.version,'platform':platform.platform(),'input_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}}
(run/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2)); print(proc.stdout); print(proc.stderr,file=sys.stderr)
raise SystemExit(proc.returncode)

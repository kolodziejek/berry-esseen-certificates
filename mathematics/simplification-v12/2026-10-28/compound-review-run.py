"""Record an isolated independent component check in a fresh run directory."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
root=Path(__file__).resolve().parents[3]
if len(sys.argv)!=2 or not sys.argv[1].replace('-','').replace('_','').isalnum():
    raise SystemExit('usage: compound-review-run.py NEW_RUN_ID')
run=root/'runs/compound-review-v12-20261028'/sys.argv[1]
run.mkdir(parents=True,exist_ok=False)
proof=Path(__file__).with_name('compound-review.tex')
checker=Path(__file__).with_name('compound-review-check.py')
started=datetime.now(timezone.utc).isoformat()
cmd=[sys.executable,'-I','-B',str(checker),str(root)]
r=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
(run/'stdout.json').write_text(r.stdout);(run/'stderr.txt').write_text(r.stderr)
receipt={'command':cmd,'python':sys.version,'started':started,'finished':datetime.now(timezone.utc).isoformat(),'returncode':r.returncode,
'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [checker,proof,Path(__file__)]},
'git_head':subprocess.run(['git','rev-parse','HEAD'],cwd=root,capture_output=True,text=True).stdout.strip()}
(run/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2));sys.exit(r.returncode)

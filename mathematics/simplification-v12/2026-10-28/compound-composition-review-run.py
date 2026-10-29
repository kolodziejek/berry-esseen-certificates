from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
if len(sys.argv)!=3 or not sys.argv[1].replace('-','').replace('_','').isalnum():
    raise SystemExit('usage: compound-composition-review-run.py NEW_ID CONSTRUCTOR_REPO_ROOT')
root=Path(__file__).resolve().parents[3];target=Path(sys.argv[2]).resolve()
run=root/'runs/compound-composition-review-v12-20261028'/sys.argv[1];run.mkdir(parents=True,exist_ok=False)
source=Path(__file__).with_name('compound-composition-review-check.py');cmd=[sys.executable,'-I','-B',str(source),str(target)]
start=datetime.now(timezone.utc).isoformat()
with (run/'stdout.json').open('w') as out,(run/'stderr.txt').open('w') as err:
 r=subprocess.run(cmd,cwd=root,stdout=out,stderr=err,text=True)
receipt={'command':cmd,'started':start,'finished':datetime.now(timezone.utc).isoformat(),'returncode':r.returncode,'python':sys.version,'checker_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'git_head':subprocess.run(['git','rev-parse','HEAD'],cwd=root,text=True,capture_output=True).stdout.strip()}
(run/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2));sys.exit(r.returncode)

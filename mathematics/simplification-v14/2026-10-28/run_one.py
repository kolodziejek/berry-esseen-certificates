"""Record one bounded local research command with immutable run directory."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys,time
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
here=Path(__file__).resolve().parent;root=here.parents[2]
if len(sys.argv)<3:raise SystemExit('run_one.py NEW_RUN_ID SCRIPT [args...]')
runid=sys.argv[1]
assert runid.isalnum()
script=here/sys.argv[2];assert script.is_file()and script.parent==here
out=root/'runs/simplification-v14-20261028'/runid;out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inputs={str(p.relative_to(root)):sha(p)for p in here.glob('*')if p.is_file()and p.suffix in ['.py','.json','.tex','.md']}
helper=root/'mathematics/simplification-v10/2026-10-28/actual_law_checks.py'
inputs[str(helper.relative_to(root))]=sha(helper)
cmd=[sys.executable,'-I','-B',str(script),*sys.argv[3:]];start=time.monotonic()
r=subprocess.run(cmd,cwd=root,capture_output=True)
(out/'stdout.json').write_bytes(r.stdout);(out/'stderr.txt').write_bytes(r.stderr)
record={'command':cmd,'returncode':r.returncode,'elapsed_seconds':time.monotonic()-start,
        'inputs_sha256':inputs,'inputs_unchanged':all(sha(root/p)==h for p,h in inputs.items()),
        'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest(),
        'python':sys.version,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
if r.returncode==0:record['result_status']=json.loads(r.stdout)['status']
(out/'receipt.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'receipt':str(out/'receipt.json'),**{k:record[k]for k in ['returncode','elapsed_seconds','inputs_unchanged']}}))
if r.returncode:print(r.stderr.decode()[-4000:])
assert r.returncode==0 and record['inputs_unchanged']

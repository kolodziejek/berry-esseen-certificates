"""Capture bounded all-panel checks in a new run directory."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
here=Path(__file__).resolve().parent;root=here.parents[2]
run=root/'runs/simplification-v11-20261028'/sys.argv[1];run.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
records=[]
for name in ['allpanel_check.py','allpanel_actual.py']:
 source=here/name;command=[sys.executable,'-I','-B',str(source)]
 before=sha(source);start=time.monotonic()
 p=subprocess.run(command,cwd=root,capture_output=True)
 (run/(name+'.stdout.json')).write_bytes(p.stdout);(run/(name+'.stderr.txt')).write_bytes(p.stderr)
 assert sha(source)==before
 record={'source':str(source.relative_to(root)),'source_sha256':before,'command':command,
 'elapsed_seconds':time.monotonic()-start,'returncode':p.returncode,
 'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()}
 if p.returncode==0:record['status']=json.loads(p.stdout)['status']
 records.append(record)
receipt={'python':sys.version,'driver_sha256':sha(Path(__file__)),'proof_sha256':sha(here/'allpanel.tex'),
 'checks':records,'status':'PASS'if all(r['returncode']==0 for r in records)else'FAILED'}
(run/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
assert receipt['status']=='PASS'

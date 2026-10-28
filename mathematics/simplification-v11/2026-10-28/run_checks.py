"""Reproduce bounded v11 checks with source binding and preservation checks.

No discovery program or certificate generator is imported or executed.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import datetime,hashlib,json,subprocess,sys,time
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
here=Path(__file__).resolve().parent;root=here.parents[2]
if len(sys.argv)!=2 or not sys.argv[1].isalnum():raise SystemExit('Use a new alphanumeric run ID')
out=root/'runs/simplification-v11-20261028'/sys.argv[1];out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert (here/'allpanel.tex').read_bytes()==(here/'allpanel-proof/proof.tex').read_bytes()
for name in ['allpanel.tex','allpanel_check.py']:
 assert (here/name).read_bytes()==(root/'runs/allpanel-review-v11-20261028/source01'/name).read_bytes()
review=json.loads((root/'runs/counts-v11-independent-20261028/check02/stdout.json').read_text())
for name,pin in review['source_sha256'].items():
 p=(root/'mathematics/simplification-v10/2026-10-28'/name)if name=='moderate_noise_check.py'else here/name
 assert sha(p)==pin,'Reviewed source changed: '+name
names=['leftpanels-check.py','allpanel_check.py','allpanel_actual.py',
 'allpanel-review-check.py','owncount_check.py','counts-v11-check.py',
 'counts-v11-actual.py','counts_v11_independent.py','extended_actual.py','preservation.py']
def run(name):
 source=here/name;pin=sha(source)
 cmd=[sys.executable,'-I','-B',str(source)]
 if name=='counts_v11_independent.py':cmd.append(str(root))
 start=time.monotonic();p=subprocess.run(cmd,cwd=root,capture_output=True)
 (out/(name+'.stdout.json')).write_bytes(p.stdout);(out/(name+'.stderr.txt')).write_bytes(p.stderr)
 r={'command':cmd,'returncode':p.returncode,'elapsed_seconds':time.monotonic()-start,
 'source_sha256':pin,'source_unchanged':sha(source)==pin,
 'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()}
 if not p.returncode:r['status']=json.loads(p.stdout)['status']
 return name,r
with ThreadPoolExecutor(max_workers=4)as pool:records=dict(pool.map(run,names))
passed=all(r['returncode']==0 and r['source_unchanged']and r.get('status','').startswith('PASS')for r in records.values())
receipt={'status':'PASS_BOUNDED_V11_CHECKS'if passed else'FAILED','checks':records,
 'proof_source_sha256':{p.name:sha(p)for p in here.glob('*.tex')},
 'python':sys.version,'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'driver_sha256':sha(Path(__file__)),'scope':'Bounded new component checks and integrity; no complete conjecture acceptance or ancestor replay'}
(out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':receipt['status'],'checks':{k:r.get('status',r['returncode'])for k,r in records.items()},'receipt':str(out/'receipt.json')},indent=2))
assert passed

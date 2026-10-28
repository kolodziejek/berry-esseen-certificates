"""Bounded v12 reproduction. No discovery or inherited generator is run."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime,hashlib,json,subprocess,sys,time
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
here=Path(__file__).resolve().parent;root=here.parents[2]
if len(sys.argv)!=2 or not sys.argv[1].isalnum():raise SystemExit('Supply a new alphanumeric run ID')
out=root/'runs/simplification-v12-20261028'/sys.argv[1];out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pins={
 'outer.tex':'72ff7ae27bdbecfa0a535dd62e52417de9bab370b7004af8b86e9e99f491facc',
 'outer-check.py':'2ab32c0bd1c07e4b6ac64ed7dceb8fd1ed999c0309fb580f28c3a4b79f8dcafb',
 'leftcount.tex':'f038aa62e039bfe48482fe69c1438553e90f7c246bf0fa74322115c33ea76ea9',
 'leftcount-check.py':'2e5190c9b035e54cd9e89a164fc335dc7cc7a535cc77d4931d616f397f0cb6d6',
 'compound-proof.tex':'5b9d8428b6aa10bc3fff44114cd26c482b88692f76dd624b841c79d5b4a753fa',
 'compound-accept.py':'f98de164169fae176644737b8b68b72044837db2a19dbba26602cea279c3d611',
 'compound-evaluator.py':'f23d657e0bc10b1d3334feeb65ccd43dd2d8b415e4a26fb0e6f7c3ddc853e582',
 'compound-certificate.json':'e3baf63f96f5f7fd6e7f9c6dae1e75448f9f588524e164fdf8c0b2e770ea6a0c',
 'comparison-union.tex':'31645628932501a0265959123b5d452b09116b77792fc2401c6a18eacdbb754a'}
for name,pin in pins.items():assert sha(here/name)==pin,'Reviewed source changed: '+name
jobs=[(here/name,[])for name in ['outer-check.py','outer-actual.py','negative-actual.py',
 'leftcount-check.py','leftcount-actual.py','left-independent.py',
 'compound-evaluator-check.py','compound-accept.py','preservation.py']]
jobs.extend((here/name,[str(root)])for name in ['outer-review-check.py','compound-review-check.py','compound-composition-review-check.py'])
jobs.append((here/'compound-cover-review-check.py',[str(here)]))
old=root/'mathematics/simplification-v11/2026-10-28/counts-v11-check.py'
assert sha(old)=='dfeba7bc10dcdcd41bdfde30c415239f5776434acf36415a919339db0a928225'
jobs.append((old,[]))
for p,args in jobs:assert p.exists(),str(p)
def run(job):
    p,args=job;name=p.name;pin=sha(p);cmd=[sys.executable,'-I','-B',str(p),*args]
    start=time.monotonic();result=subprocess.run(cmd,cwd=root,capture_output=True)
    (out/(name+'.stdout.json')).write_bytes(result.stdout);(out/(name+'.stderr.txt')).write_bytes(result.stderr)
    r={'command':cmd,'returncode':result.returncode,'elapsed_seconds':time.monotonic()-start,'source_sha256':pin,'source_unchanged':sha(p)==pin,
       'stdout_sha256':hashlib.sha256(result.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(result.stderr).hexdigest()}
    if not result.returncode:r['status']=json.loads(result.stdout)['status']
    print(json.dumps({'completed':name,'status':r.get('status','FAILED')}),flush=True)
    return name,r
with ThreadPoolExecutor(max_workers=4)as pool:records=dict(pool.map(run,jobs))
ok=all(r['returncode']==0 and r['source_unchanged']and r.get('status','').startswith('PASS')for r in records.values())
assert all(sha(here/n)==p for n,p in pins.items())
receipt={'status':'PASS_BOUNDED_V12_INTEGRATION'if ok else'FAILED','checks':records,'reviewed_source_sha256':pins,
 'python':sys.version,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'driver_sha256':sha(Path(__file__)),
 'scope':'Reviewed local count implications and integrity only; no full-conjecture, acquisition-chain or finite-base acceptance'}
(out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'checks':len(records),'receipt':str(out/'receipt.json')}));assert ok

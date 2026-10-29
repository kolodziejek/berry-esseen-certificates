"""Bounded reproduction of reviewed v14 claims; no discovery or generation."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime,hashlib,json,subprocess,sys,time
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
here=Path(__file__).resolve().parent;root=here.parents[2]
if len(sys.argv)!=2 or not sys.argv[1].isalnum():raise SystemExit('Supply a fresh alphanumeric run ID')
out=root/'runs/simplification-v14-20261028'/sys.argv[1];out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=here/'reviewed-sources.json';pins=json.loads(manifest.read_text())
for name,pin in pins.items():assert sha(here/name)==pin,'Reviewed source changed: '+name
jobs=[(name,[])for name in ['large-index-check.py','counts-check.py','loss-check.py',
                          'geometry-slack-check.py','geometry-slack-actual.py','preservation.py']]
jobs.extend([('large-index-review-check.py',[str(root)]),
             ('counts-window-review-check.py',['--source',str(here/'large-index.tex')]),
             ('geometry-slack-review.py',[str(here/'geometry-slack.tex')])])
def run(job):
    name,args=job;p=here/name;pin=sha(p);cmd=[sys.executable,'-I','-B',str(p),*args]
    start=time.monotonic();r=subprocess.run(cmd,cwd=root,capture_output=True)
    (out/(name+'.stdout.json')).write_bytes(r.stdout);(out/(name+'.stderr.txt')).write_bytes(r.stderr)
    record={'command':cmd,'returncode':r.returncode,'elapsed_seconds':time.monotonic()-start,'source_sha256':pin,
            'source_unchanged':sha(p)==pin,'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest()}
    if not r.returncode:
        obj=json.loads(r.stdout);record['status']=obj.get('status',obj.get('result','MISSING_STATUS'))
    print(json.dumps({'completed':name,'status':record.get('status','FAILED')}),flush=True)
    return name,record
with ThreadPoolExecutor(max_workers=3)as pool:records=dict(pool.map(run,jobs))
ok=all(r['returncode']==0 and r['source_unchanged']and r.get('status','').startswith('PASS')for r in records.values())
assert all(sha(here/n)==h for n,h in pins.items())
receipt={'status':'PASS_BOUNDED_V14_INTEGRATION'if ok else'FAILED','checks':records,'reviewed_sources_sha256':pins,
         'manifest_sha256':sha(manifest),'driver_sha256':sha(Path(__file__)),'python':sys.version,
         'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'scope':'Scoped all-law right comparison n>=6000, independent-noise subclass, left geometric region, central asymmetric families and integrity; no global conjecture, finite base or coarse-Fourier acceptance'}
(out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':receipt['status'],'checks':len(records),'receipt':str(out/'receipt.json')}));assert ok

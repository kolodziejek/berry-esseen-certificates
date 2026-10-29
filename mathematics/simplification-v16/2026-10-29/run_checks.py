"""Bounded reproduction of the reviewed v16 route; no discovery or generation."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime,hashlib,json,subprocess,sys,time

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions required')
here=Path(__file__).resolve().parent
root=here.parents[2]
if len(sys.argv)!=2 or not sys.argv[1].isalnum():
    raise SystemExit('Supply a fresh alphanumeric run ID')
out=root/'runs/simplification-v16-20261029'/sys.argv[1]
out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=here/'reviewed-sources.json'
pins=json.loads(manifest.read_text())
for name,pin in pins.items():
    assert sha(root/name)==pin,'Reviewed source changed: '+name
jobs=[(name,[])for name in ['acquisition-check.py','unified-check.py',
    'unified-actual.py','small-check.py','small-review-actual.py',
    'counts-check.py','preservation.py']]
jobs.extend([
    ('small-review-check.py',['--proof',str(here/'small-common.tex')]),
    ('unified-review-check.py',[str(root)]),
    ('acquisition-review.py',['--source-root',str(root)]),
])

def run(job):
    name,args=job
    p=here/name
    pin=sha(p)
    cmd=[sys.executable,'-I','-B',str(p),*args]
    start=time.monotonic()
    r=subprocess.run(cmd,cwd=root,capture_output=True)
    (out/(name+'.stdout.json')).write_bytes(r.stdout)
    (out/(name+'.stderr.txt')).write_bytes(r.stderr)
    record={'command':cmd,'returncode':r.returncode,
        'elapsed_seconds':time.monotonic()-start,'source_sha256':pin,
        'source_unchanged':sha(p)==pin,
        'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),
        'stderr_sha256':hashlib.sha256(r.stderr).hexdigest()}
    if r.returncode==0:
        obj=json.loads(r.stdout)
        record['status']=obj.get('status',obj.get('result','MISSING_STATUS'))
    print(json.dumps({'completed':name,'status':record.get('status','FAILED')}),flush=True)
    return name,record

with ThreadPoolExecutor(max_workers=3)as pool:
    records=dict(pool.map(run,jobs))
ok=all(r['returncode']==0 and r['source_unchanged'] and
       r.get('status','').startswith('PASS')for r in records.values())
assert all(sha(root/n)==h for n,h in pins.items())
receipt={'status':'PASS_BOUNDED_V16_INTEGRATION'if ok else'FAILED',
    'checks':records,'reviewed_sources_sha256':pins,
    'manifest_sha256':sha(manifest),'driver_sha256':sha(Path(__file__)),
    'python':sys.version,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope':'Direct post-entry geometry, conditional contact strip, elementary small noise, unified five-count local comparisons, exact conditional joins, adversarial controls and preservation. No full Fourier replay, finite-base acceptance, unconditional cutoff or full conjecture.'}
(out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':receipt['status'],'checks':len(records),'receipt':str(out/'receipt.json')}))
assert ok

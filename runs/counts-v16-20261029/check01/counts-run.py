"""Bounded source-recording runner; refuses to overwrite a receipt directory."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
here=Path(__file__).resolve().parent;base=here.parents[2]
if len(sys.argv)!=2 or not sys.argv[1].isalnum():raise SystemExit('Use one fresh alphanumeric run id')
out=base/'runs/counts-v16-20261029'/sys.argv[1];out.mkdir(parents=True,exist_ok=False)
inputs={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in here.glob('counts-*') if p.suffix in ('.py','.tex','.md')}
results=[]
for name in ['counts-check.py','counts-actual.py']:
    command=[sys.executable,'-I','-B',str(here/name)];start=time.monotonic()
    result=subprocess.run(command,cwd=base,capture_output=True)
    (out/(name+'.stdout.json')).write_bytes(result.stdout);(out/(name+'.stderr.txt')).write_bytes(result.stderr)
    row={'command':command,'returncode':result.returncode,'elapsed_seconds':time.monotonic()-start}
    results.append(row);(out/'receipt.json').write_text(json.dumps({'status':'RUNNING','inputs':inputs,'results':results,'python':sys.version},indent=2))
    if result.returncode:raise SystemExit(result.returncode)
for p in here.glob('counts-*'):
    if p.suffix in ('.py','.tex','.md'):(out/p.name).write_bytes(p.read_bytes())
(out/'receipt.json').write_text(json.dumps({'status':'PASS_COUNTS_V16_BOUNDED_REPLAY','inputs':inputs,'results':results,'python':sys.version},indent=2))
print(json.dumps({'status':'PASS_COUNTS_V16_BOUNDED_REPLAY','receipt':str(out/'receipt.json'),'results':results},indent=2))

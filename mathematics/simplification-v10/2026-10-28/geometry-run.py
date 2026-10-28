"""Record bounded independent-geometry checks and source bindings."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
run=ROOT/'runs/geometry-v10-20261028'/sys.argv[1];run.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'python':sys.version,'optimization':sys.flags.optimize,'driver_sha256':sha(Path(__file__)),'proof_sha256':sha(HERE/'geometry.tex'),'checks':[]}
for name in ['geometry-check.py','geometry-panels.py','geometry-laws.py']:
 p=HERE/name;cmd=[sys.executable,'-I','-B',str(p)];t=time.monotonic();c=subprocess.run(cmd,cwd=ROOT,capture_output=True)
 out=run/(name+'.stdout.json');err=run/(name+'.stderr.txt');out.write_bytes(c.stdout);err.write_bytes(c.stderr)
 r['checks'].append(dict(script=name,command=cmd,returncode=c.returncode,elapsed_seconds=time.monotonic()-t,source_sha256=sha(p),stdout_sha256=sha(out),stderr_sha256=sha(err)))
 (run/'receipt.json').write_text(json.dumps(r,indent=2)+'\n')
 if c.returncode:raise RuntimeError(name+' failed; saved output retained')
 z=json.loads(c.stdout);print(name+': '+z['status'],flush=True)
r['status']='PASS_BOUNDED_DIRECT_GEOMETRY_CHECKS';r['mathematical_scope']='Proved direct geometry plus finite gates and one-pass panel/strip consequences; not global confinement/count/finite base.'
(run/'receipt.json').write_text(json.dumps(r,indent=2)+'\n')

#!/usr/bin/env python3
"""Adversarial repaired-phase acceptance test, using disposable copies."""
import ast,hashlib,json,marshal,os,shutil,struct,subprocess,sys,time
from importlib.util import cache_from_source,MAGIC_NUMBER
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
SOURCE=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT
RUN=ROOT/'runs/fixed-target-v8-20261028/phase-accept-review03'
REL=Path('mathematics/fixed-target-v8/2026-10-28')
ACCEPT_SHA='416ab9b7bf957c57062e929743dad200f9ac002f879cb2516eeb9c6a2ac2e6b7'
def need(x,s):
 if not x:raise ValueError(s)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(RUN/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
def main():
 need(__debug__ and not sys.flags.optimize,'ordinary Python');RUN.mkdir(parents=True,exist_ok=True);box=RUN/'sandbox';box.mkdir()
 accept=SOURCE/REL/'accept_phase.py';need(digest(accept)==ACCEPT_SHA,'frozen repaired acceptor')
 tree=ast.parse(accept.read_text());pins=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='PINS'for t in n.targets)))
 for p,h in pins.items():need(digest(SOURCE/p)==h,'repaired pin '+p)
 for p in [*pins,str(REL/'accept_phase.py')]:
  target=box/p;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(SOURCE/p,target)
 source_proof=SOURCE/'runs/fixed-target-v8-20261028/phase01/stdout.json';shutil.copyfile(source_proof,box/'candidate.json')
 badproof=ROOT/'runs/fixed-target-v8-20261028/phase-accept-review02/cached-producer.stdout.json';shutil.copyfile(badproof,box/'altered-candidate.json')
 core=box/REL/'phase_core.py';st=core.stat();add="\nraise RuntimeError('unreviewed bytecode cache executed')\n"
 old=sys.pycache_prefix;sys.pycache_prefix=str(box/'cache');pyc=Path(cache_from_source(str(core)));sys.pycache_prefix=old
 pyc.parent.mkdir(parents=True);pyc.write_bytes(MAGIC_NUMBER+struct.pack('<III',0,int(st.st_mtime),st.st_size)+marshal.dumps(compile(core.read_text()+add,str(core),'exec')))
 shadow=box/'mathematics/fixed-target-v7/2026-10-27/phase_core.py';shadow.write_text("raise RuntimeError('unreviewed v7 shadow module executed')\n")
 need(all(digest(box/p)==h for p,h in pins.items()),'all repaired source pins unchanged')
 receipts=[]
 def run(name,proof,flags=()):
  cmd=[sys.executable,*flags,'-B',str(REL/'accept_phase.py'),proof];t=time.monotonic()
  p=subprocess.run(cmd,cwd=box,capture_output=True,timeout=120,env={**os.environ,'PYTHONPYCACHEPREFIX':str(box/'cache')})
  (RUN/(name+'.stdout.json')).write_bytes(p.stdout);(RUN/(name+'.stderr.txt')).write_bytes(p.stderr)
  receipt={'name':name,'command':['python3',*flags,'-B',str(REL/'accept_phase.py'),proof],'returncode':p.returncode,'elapsed_seconds':time.monotonic()-t,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()};save(name+'.receipt.json',receipt);receipts.append(receipt)
  return p
 good=run('valid-with-poisoned-cache-and-shadow','candidate.json');need(good.returncode==0,'repaired source-only replay')
 g=json.loads(good.stdout);need(g['proof_sha256']==g['replay_stdout_sha256']==digest(source_proof),'unchanged deterministic original export')
 bad=run('reject-prior-cache-altered-export','altered-candidate.json');need(bad.returncode!=0 and b'complete deterministic phase export'in bad.stderr,'prior attack rejected for output mismatch')
 optimized=run('reject-optimized-interpreter','candidate.json',('-O',));need(optimized.returncode!=0 and b'unoptimized interpreter'in optimized.stderr,'optimized rejection')
 original=core.read_bytes();core.write_bytes(original+b'\n# review mutation\n')
 corrupt=run('reject-mutated-pinned-core','candidate.json');need(corrupt.returncode!=0 and b'pinned source before execution'in corrupt.stderr,'source pin rejection');core.write_bytes(original)
 (box/'duplicate.json').write_text('{"x":{"y":1,"y":2}}')
 dup=run('reject-nested-duplicate-key','duplicate.json');need(dup.returncode!=0 and b'duplicate JSON key'in dup.stderr,'CLI duplicate rejection')
 need(all(digest(box/p)==h for p,h in pins.items()),'review restores original disposable pins')
 (RUN/'sources').mkdir()
 for name in ('accept_phase.py','phase_probe.py'):shutil.copyfile(box/REL/name,RUN/'sources'/name)
 save('summary.json',{'status':'PASS_REPAIRED_PHASE_ACCEPTOR_AUTHENTICITY','acceptor_sha256':ACCEPT_SHA,'source_pins':pins,'candidate_sha256':digest(source_proof),'replay_stdout_sha256':g['replay_stdout_sha256'],'active_cells':g['active_cells'],'total_cells':g['total_cells'],'attacks_present_during_success':['timestamp-valid unreviewed phase_core cache in inherited prefix','v7 phase_core.py shadow module'],'controls':['prior unreviewed-cache export rejected','optimized Python rejected','pinned core mutation rejected','nested JSON duplicate rejected'],'python':sys.version,'scope':'Executable source binding and deterministic export authenticity; does not replay v7 stages1-3 or establish analytic premises.'})
 print(json.dumps({'status':'PASS_REPAIRED_PHASE_ACCEPTOR_AUTHENTICITY','full_replays':2,'early_reject_controls':3}))
if __name__=='__main__':main()

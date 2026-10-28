#!/usr/bin/env python3
"""Independent bounded phase-export authenticity review. Disposable copies only."""
import ast, hashlib, json, marshal, os, shutil, struct, subprocess, sys, time
from fractions import Fraction as F
from importlib.util import cache_from_source, MAGIC_NUMBER
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
RUN=ROOT/'runs/fixed-target-v8-20261028/phase-accept-review01'
SOURCE=ROOT.parent/'phase-entry-v8'
REL=Path('mathematics/fixed-target-v8/2026-10-28')
def need(x,s):
    if not x: raise ValueError(s)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def literals(path,name):
    tree=ast.parse(path.read_text())
    return ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name)and t.id==name for t in n.targets)))
def unique(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,'duplicate key');d[k]=v
    return d
def save(name,x): (RUN/name).write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
def child(name,args,sandbox):
    t=time.monotonic();p=subprocess.run([sys.executable,'-B',*map(str,args)],cwd=sandbox,capture_output=True,timeout=120)
    (RUN/(name+'.stdout.json')).write_bytes(p.stdout);(RUN/(name+'.stderr.txt')).write_bytes(p.stderr)
    save(name+'.receipt.json',{'command':['python3','-B',*map(str,args)],'returncode':p.returncode,'elapsed_seconds':time.monotonic()-t,'python':sys.version,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()})
    return p

def main():
    need(__debug__ and not sys.flags.optimize,'ordinary Python')
    RUN.mkdir(parents=True,exist_ok=True);box=RUN/'sandbox';box.mkdir()
    accept=SOURCE/REL/'accept_phase.py';pins=literals(accept,'PINS')
    for rel,h in pins.items():need(digest(SOURCE/rel)==h,'source pin '+rel)
    for rel in [*pins,str(REL/'accept_phase.py')]:
        target=box/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(SOURCE/rel,target)
    proof=SOURCE/'runs/fixed-target-v8-20261028/phase01/stdout.json'
    shutil.copy2(proof,box/'candidate.json')
    obj=json.loads(proof.read_text(),object_pairs_hook=unique)
    clean=child('clean',[REL/'accept_phase.py','candidate.json'],box);need(clean.returncode==0,'clean acceptance')
    # Independent shape/type, parent-row, coefficient and cell census checks.
    parent=json.loads((box/'mathematics/fixed-target-v7/2026-10-27/entry-proof.json').read_text())
    target=[(i,r)for i,r in enumerate(parent['steps'][3])if not r.get('prior_excluded')]
    need(len(target)*128==obj['total_cells']==2048,'full inherited scheduled cover')
    need(sum(r['active']for i,r in target)==len(obj['phase_cells'])==682,'all active cells')
    need([i for i,r in target]==[r['index']for r in obj['rows']],'ordered inherited rows')
    for (i,r),row in zip(target,obj['rows']):
        need(row['active']==r['active']and row['excluded']==r['excluded'],'row census')
    reconstructed=0
    for x in obj['phase_cells']:
        f=lambda k:F(x[k]);K=list(map(F,x['K1']));W=list(map(F,x['W']));density=list(map(F,x['density']))
        need(0<f('pl')<=f('pu')<1 and len(x['quadratics'])==2,'closed phase-cell endpoints')
        need([F(q['c'])for q in x['quadratics']]==[F('.4097321837023'),F('.4097321837025')],'both c endpoints')
        for q in x['quadratics']:
            c=F(q['c']);terms=[c*k+p*w for k in K for p in density for w in W]
            need(F(q['plus'])==max(terms)+f('slope')and F(q['minus'])==-min(terms)+f('slope'),'signed coefficient')
            need(F(q['B'])==f('Fourier')+c*f('A'),'constant coefficient')
            need(F(q['Q'])==c*F(x['rho'][0])+min(p*F(x['gamma'][0])/2 for p in density)+f('eta')>0,'curvature coefficient')
            need(max(F(q['plus']),F(q['minus']))<=F(q['absolute']),'absolute ancestor domination');reconstructed+=1
    build=SOURCE/REL/'build_phase_core.py';patches=literals(build,'patches')
    ancestor=(SOURCE/'mathematics/fixed-target-v7/2026-10-27/signed_core.py').read_text();expected=ancestor
    for a,b in patches:need(expected.count(a)==1,'unique export patch');expected=expected.replace(a,b)
    need(expected==(SOURCE/REL/'phase_core.py').read_text(),'exact add-only core derivation')
    # Test schema comparison separately, without repeating the expensive stage.
    sys.path.insert(0,str(box/REL));import accept_phase as tested
    controls=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,TypeError):controls.append(name)
        else:raise ValueError('invalid comparison accepted '+name)
    import copy
    for name,change in [
       ('nested boolean integer',lambda z:z['rows'][0].update(index=True)),
       ('nested float integer',lambda z:z['rows'][0].update(index=float(z['rows'][0]['index']))),
       ('noncanonical rational',lambda z:z['phase_cells'][0].update(raw='0'+z['phase_cells'][0]['raw'])),
       ('rational numeric instead of string',lambda z:z['phase_cells'][0].update(pl=float(F(z['phase_cells'][0]['pl'])))),
       ('lost signed endpoint',lambda z:z['phase_cells'][0]['quadratics'].pop()),
       ('changed curvature',lambda z:z['phase_cells'][0]['quadratics'][1].update(Q='0')),
       ('unknown nested field',lambda z:z['phase_cells'][0].update(unknown=True)),
       ('NaN field',lambda z:z['probe'].update(H=float('nan'))),
       ('changed parent source',lambda z:z.update(source_proof_sha256='f'*64))]:
        bad=copy.deepcopy(obj);change(bad);reject(name,lambda:tested.match(bad,obj))
    reject('nested duplicate JSON key',lambda:json.loads('{"a":{"b":1,"b":2}}',object_pairs_hook=tested.unique))
    # Bytecode cache negative test: exact source hashes remain unchanged.
    core=box/REL/'phase_core.py';st=core.stat()
    addition='''\n_original_stage=stage\ndef stage(*args,**kwargs):\n    out=_original_stage(*args,**kwargs)\n    for cell in out['phase_cells']: cell['unreviewed_cache_field']=True\n    return out\n'''
    code=compile(core.read_text()+addition,str(core),'exec')
    pyc=Path(cache_from_source(str(core)));pyc.parent.mkdir(exist_ok=True)
    pyc.write_bytes(MAGIC_NUMBER+struct.pack('<III',0,int(st.st_mtime),st.st_size)+marshal.dumps(code))
    need(all(digest(box/p)==h for p,h in pins.items()),'all source hashes unchanged before cache test')
    poison=child('cached-producer',[REL/'phase_probe.py'],box);need(poison.returncode==0,'cached producer')
    altered=json.loads(poison.stdout,object_pairs_hook=unique)
    need(all(x.get('unreviewed_cache_field')is True for x in altered['phase_cells']),'unpinned cache executed')
    (box/'altered-candidate.json').write_bytes(poison.stdout)
    poisoned=child('cached-acceptor',[REL/'accept_phase.py','altered-candidate.json'],box)
    need(poisoned.returncode==0,'source pins did not reject unreviewed cache')
    need(all(digest(box/p)==h for p,h in pins.items()),'all source hashes unchanged after cache test')
    save('summary.json',{'status':'REVIEW_FOUND_BYTECODE_AUTHENTICITY_GAP','acceptor_sha256':digest(accept),'pins':pins,'candidate_sha256':digest(proof),'clean_replay_pass':True,'independent_scheduled_cells':2048,'independent_active_cells':682,'reconstructed_endpoint_quadratics':reconstructed,'rejected_comparison_controls':controls,'cache_gap':{'all_source_pins_unchanged':True,'unreviewed_field_cells':682,'altered_candidate_accepted':True,'cached_bytecode_sha256':digest(pyc)},'limits':'No independent reconstruction of inherited numerical kernel inequalities; accepted v7 ancestry remains a premise.'})
    print(json.dumps({'status':'REVIEW_FOUND_BYTECODE_AUTHENTICITY_GAP','active_cells':682,'comparison_controls_rejected':len(controls)}))
if __name__=='__main__':main()

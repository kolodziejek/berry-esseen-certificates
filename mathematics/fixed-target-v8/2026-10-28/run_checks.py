#!/usr/bin/env python3
"""Bounded v8 checks and evidence binding, not global theorem acceptance."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,os,platform,subprocess,sys,time
from datetime import datetime,timezone

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def need(x,s):
    if not x:raise ValueError(s)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('run_id');args=ap.parse_args()
    need(args.run_id.replace('-','').replace('_','').isalnum(),'simple distinct run id')
    need(__debug__ and not sys.flags.optimize,'assertions enabled')
    here=Path(__file__).resolve().parent;root=here.parents[2]
    out=root/'runs/fixed-target-v8-20261028'/args.run_id;out.mkdir(exist_ok=False)
    receipt={'started_utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),
       'optimization':sys.flags.optimize,'driver_sha256':sha(Path(__file__)),'checks':[],
       'scope':'Eleven bounded checks, complete one-panel confinement join, isolated ancestor binding and baseline preservation; not global confinement/count/BASE41.'}
    jobs=[('root4','root4-check.py',[]),('moments','moment-entry-v8.py',[]),
       ('independent-phase','phase-review-check.py',[str(root)]),
       ('independent-high-noise','high-noise-review.py',['--source-root',str(root)]),
       ('phase-regions','phase_region.py',[]),('independent-small-noise','small-noise-check.py',[]),
       ('direct-heat','phase-confinement-heat.py',[]),
       ('continuous-low-noise','low-noise-continuous.py',[]),
       ('independent-continuous-low-noise','reviews/low-noise-continuous-independent.py',[]),
       ('probability-limit','probability-probe.py',[]),
       ('complete-panel','phase-confinement.py',['--evidence',str(out/'panel-replay'),'--partition','equal','--compose-heat'])]
    outputs={}
    for name,file,extra in jobs:
        script=here/file;cmd=[sys.executable,'-I','-B',str(script),*extra];start=time.monotonic()
        r=subprocess.run(cmd,cwd=root,capture_output=True,text=True,timeout=120)
        stdout,stderr=out/(name+'.stdout.json'),out/(name+'.stderr.txt');stdout.write_text(r.stdout);stderr.write_text(r.stderr)
        receipt['checks'].append(dict(name=name,command=cmd,returncode=r.returncode,elapsed_seconds=time.monotonic()-start,
           source_sha256=sha(script),stdout_sha256=sha(stdout),stderr_sha256=sha(stderr)))
        (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
        need(r.returncode==0,name+' execution failed; saved evidence retained');outputs[name]=json.loads(r.stdout)
        print(name+': completed',flush=True)
    # Reconstruct the complete closed rectangle index separately from its producer.
    z=outputs['complete-panel'];need(z['status']=='PASS_CONDITIONAL_PANEL_HALF_AMPLITUDE_BY_HEAT_AND_PHASE','scoped panel outcome')
    reviewed=json.loads((root/'runs/fixed-target-v8-20261028/phase-confinement05/stdout.json').read_text())
    need(z['diagnostic']==reviewed['diagnostic'] and z['composition']==reviewed['composition'],'fresh scalar outputs match independently reconstructed saved data')
    records=z['diagnostic']['records'];cover=z['composition']['coverage']
    def key(row):return (row['sign'],*(F(x)for x in row['phase']),*(F(x)for x in row['noise']))
    expected={(s,F(907*j,4000),F(907*(j+1),4000),F(3*k,40),F(3*(k+1),40))for s in (-1,1)for j in range(8)for k in range(8)}
    need(len(records)==len(cover)==128 and set(map(key,records))==set(map(key,cover))==expected,'all closed rectangles exactly once')
    lookup={key(row):row for row in records};counts={};margins=[]
    for row in cover:
        k=key(row);original=lookup[k];method=row['method'];counts[method]=counts.get(method,0)+1
        if k[-1]<=F(3,40):need(method=='direct all-threshold heat lemma','whole lowest closed band')
        elif original['resource_excluded']:need(method=='resource exclusion','same exclusion')
        else:
            need(method=='two strict confinement rays' and len(original['sides'])==2,'both strict rays')
            need({a['side']for a in original['sides']}=={'lower','upper'},'both oriented rays')
            for a in original['sides']:
                margin=F(a['lhs'])-F(a['error']);need(margin==F(a['margin'])>0 and a['passed']is True,'exact positive difference')
                margins.append(margin)
    need(counts=={'direct all-threshold heat lemma':16,'resource exclusion':84,'two strict confinement rays':28},'complete composition counts')
    need(len(margins)==56 and min(margins)>F('0.00892011917'),'strict surviving margins')
    receipt['panel_cover_binding']=dict(counts=counts,remaining_strict_rays=56,smallest_margin=str(min(margins)),
        scope='Separate cover/accounting check; formulas independently reviewed elsewhere.')
    # The new low-noise argument has no extra probability grid. Its incoming
    # .6 strip is bound to the freshly reproduced elementary moment result.
    incoming=[row for row in outputs['moments']['panels']if row['index']in range(40,53)]
    need([row['index']for row in incoming]==list(range(40,53)),'all incoming strip panels')
    for row in incoming:
        need(not row['excluded'] and F(row['d'])<F('.072'),'incoming actual gap')
        for side in ('negative','positive'):
            gate=row['strip_'+side]
            need(gate['passed']is True and F(gate['boundary'])<0 and all(F(x)<0 for x in gate['rays']),'incoming whole-ray strip')
    uniform=outputs['continuous-low-noise'];independent=outputs['independent-continuous-low-noise']
    need(uniform['status']=='PASS_CONDITIONAL_CONTINUOUS_LOW_NOISE_ENDPOINT_GATES' and uniform['grid_cells']==0 and uniform['endpoint_gate_count']==28,'continuous selected contract')
    need(independent['status']=='PASS_CONTINUOUS_FOLDED_LOW_NOISE_CONCAVE_DERIVATIVE','independent continuous contract')
    need(uniform['polynomials']['P']==independent['quintic'] and uniform['interval']==independent['u_interval'] and uniform['beta_family']==independent['beta_affine'],'same independently expanded boundary polynomial')
    value=F(0)
    for coefficient in reversed(independent['quintic']):value=value*F(independent['u_interval'][1])+F(coefficient)
    need(value==F(uniform['heat_upper'])<F('-.1779'),'continuous negative endpoint')
    receipt['continuous_low_noise_join']=dict(incoming_panels=13,applied_probability_interval=['2/5','53/100'],noise_interval=['0','3/40'],new_grid_cells=0,endpoint_gates=28,heat_upper=str(value),scope='Conditional on incoming strip, contact/predecessor and heat inequalities; no larger-noise confinement.')
    # Bind the actual isolated full ancestor replay, not an old success label.
    a=root/'runs/fixed-target-v8-20261028/isolated-entry-review01'
    ar=json.loads((a/'receipt.json').read_text());az=json.loads((a/'summary.json').read_text())
    need(ar['returncode']==0 and ar['optimization']==0 and ar['copied_file_count']==13 and ar['empty_cache_after_replay']is True,'isolated ancestor execution')
    need(sha(a/'stdout.json')==ar['stdout_sha256'] and sha(a/'stderr.txt')==ar['stderr_sha256'],'ancestor stream binding')
    for rel,h in ar['source_pins'].items():need(sha(root/rel)==h,'unchanged isolated ancestor source '+rel)
    need(sha(here/'isolated_entry_replay.py')==ar['wrapper_sha256'],'reviewed isolated wrapper')
    need(az['status']=='PASS_ISOLATED_REPRODUCTION_FIXED_ENTRY_V7' and az['signed_cells']==11264 and len(az['wrapper_rejected_controls'])==5,'full selected ancestor')
    need((a/'stdout.json').read_bytes()==(root/'runs/fixed-target-v7-20261027/accept02/stdout.json').read_bytes(),'independent observation of unchanged ancestor output')
    receipt['isolated_entry_binding']=dict(receipt_sha256=sha(a/'receipt.json'),stdout_sha256=ar['stdout_sha256'],summary=az)
    pr=root/'runs/fixed-target-v8-20261028/phase-accept-review03/summary.json';pz=json.loads(pr.read_text())
    need(pz['status']=='PASS_REPAIRED_PHASE_ACCEPTOR_AUTHENTICITY' and pz['candidate_sha256']==pz['replay_stdout_sha256'],'repaired adversarial replay')
    need(sha(here/'accept_phase.py')==pz['acceptor_sha256'],'repaired acceptor binding')
    for rel,h in pz['source_pins'].items():need(sha(root/rel)==h,'repaired phase source '+rel)
    need(sha(root/'runs/fixed-target-v8-20261028/phase01/stdout.json')==pz['candidate_sha256'],'phase export binding')
    receipt['repaired_phase_binding']=dict(summary_sha256=sha(pr),status=pz['status'],export_sha256=pz['candidate_sha256'])
    baseline='6346fc1b4432bc5982822aa696eb566ed9e1e1ee'
    entries=subprocess.check_output(['git','ls-tree','-rz',baseline],cwd=root).split(b'\0')
    head={x.split(b'\t',1)[1]:x.split(b'\t',1)[0] for x in
          subprocess.check_output(['git','ls-tree','-rz','HEAD'],cwd=root).split(b'\0') if x}
    index={x.split(b'\t',1)[1]:x.split(b'\t',1)[0] for x in
           subprocess.check_output(['git','ls-files','--stage','-z'],cwd=root).split(b'\0') if x}
    tags={x[2:]:x[:1] for x in
          subprocess.check_output(['git','ls-files','-t','-z'],cwd=root).split(b'\0') if x}
    checked=materialized=sparse=0
    for line in entries:
        if not line:continue
        header,path=line.split(b'\t',1)
        mode,kind,oid=header.split()
        if kind!=b'blob':raise RuntimeError('unexpected baseline entry kind')
        if head.get(path)!=header:raise RuntimeError('committed baseline changed: '+path.decode())
        if index.get(path)!=mode+b' '+oid+b' 0':raise RuntimeError('indexed baseline changed: '+path.decode())
        target=root/path.decode()
        if not target.exists() and not target.is_symlink() and tags.get(path)==b'S':
            sparse+=1  # Original blob is preserved in HEAD and index, outside sparse checkout.
        elif mode==b'120000':
            if not target.is_symlink():raise RuntimeError('missing baseline link '+str(target))
            actual=os.readlink(target).encode()
            materialized+=1
        else:
            if not target.is_file():raise RuntimeError('missing baseline file '+str(target))
            actual=target.read_bytes()
            materialized+=1
        if target.exists() or target.is_symlink():
            blob=hashlib.sha1(b'blob '+str(len(actual)).encode()+b'\0'+actual).hexdigest().encode()
            if blob!=oid:raise RuntimeError('working baseline changed: '+str(target))
        checked+=1
    receipt.update(status='PASS_BOUNDED_V8_INTEGRATION',baseline=baseline,
        unchanged_baseline_entries=checked,materialized_baseline_files_checked=materialized,
        sparse_baseline_blobs_checked=sparse,completed_utc=datetime.now(timezone.utc).isoformat())
    (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(str(checked)+' original baseline entries unchanged')

if __name__=='__main__':main()

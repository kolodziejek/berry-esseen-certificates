#!/usr/bin/env python3
"""Record bounded integration checks; no native certificate campaign."""
from pathlib import Path
import argparse, hashlib, json, os, platform, subprocess, sys, time
from datetime import datetime, timezone

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('run_id')
    args=ap.parse_args()
    if not args.run_id.replace('-','').replace('_','').isalnum():
        ap.error('run id must contain letters, numbers, hyphens or underscores')
    if not __debug__ or sys.flags.optimize:
        raise RuntimeError('assertions must be enabled')
    here=Path(__file__).resolve().parent
    root=here.parents[2]
    out=root/'runs/fixed-target-v7-20261027'/args.run_id
    out.mkdir(exist_ok=False)
    receipt={'started_utc':datetime.now(timezone.utc).isoformat(),
       'python':platform.python_version(),'optimization':sys.flags.optimize,
       'driver_sha256':sha(Path(__file__)),'checks':[],
       'source_sha256':{str(p.relative_to(root)):sha(p)
                       for p in sorted(here.rglob('*'))
                       if p.is_file() and p.suffix in ('.tex','.py','.json')},
       'scope':'Six bounded independent checks, binding of the fresh exact entry replay, and baseline preservation; not LOCAL42 or BASE41.'}
    jobs=[(name,here/file) for name,file in [
       ('fourier','fourier-check.py'),('exclusion','exclusion_check.py'),
       ('base','base_check.py'),('signed-accounting','signed_review_structure.py'),
       ('entry-schema-pooling','entry_acceptor_review.py'),
       ('conservation','../../fixed-target-v8/2026-10-28/conservation-check.py')]]
    for name,script in jobs:
        cmd=[sys.executable,'-B',str(script)]
        if name in ('signed-accounting','entry-schema-pooling'):cmd.extend(['--source-root',str(root)])
        start=time.monotonic()
        result=subprocess.run(cmd,cwd=root,capture_output=True,text=True,timeout=120)
        stdout,stderr=out/(name+'.stdout.txt'),out/(name+'.stderr.txt')
        stdout.write_text(result.stdout);stderr.write_text(result.stderr)
        receipt['checks'].append({'name':name,'command':cmd,'returncode':result.returncode,
            'elapsed_seconds':time.monotonic()-start,'script_sha256':sha(script),
            'stdout_sha256':sha(stdout),'stderr_sha256':sha(stderr)})
        (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
        if result.returncode:
            raise RuntimeError(name+' failed; saved streams retained')
        print(name+': PASS',flush=True)
    accepted=root/'runs/fixed-target-v7-20261027/accept02'
    ar=json.loads((accepted/'receipt.json').read_text())
    if ar['returncode']!=0 or ar['optimization']!=0:raise RuntimeError('fresh acceptance did not pass')
    for rel,h in ar['source_sha256'].items():
        if sha(root/rel)!=h:raise RuntimeError('accepted input changed: '+rel)
    ao=json.loads((accepted/'stdout.json').read_text())
    if ao['status']!='PASS_INITIAL42_FIXED_TARGET_COARSE_V7' or len(ao['rejected_controls'])!=19:
        raise RuntimeError('wrong acceptance contract')
    receipt['entry_acceptance_binding']={'receipt_sha256':sha(accepted/'receipt.json'),
        'stdout_sha256':sha(accepted/'stdout.json'),'proof_sha256':ao['proof_sha256'],
        'summary':ao['summary'],'scope':'Binds the recorded fresh replay; does not rerun all signed cells.'}
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
    receipt.update(status='PASS_BOUNDED_INTEGRATION',baseline=baseline,
        unchanged_baseline_entries=checked,materialized_baseline_files_checked=materialized,
        sparse_baseline_blobs_checked=sparse,completed_utc=datetime.now(timezone.utc).isoformat())
    (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(str(checked)+' original baseline entries unchanged')

if __name__=='__main__':main()

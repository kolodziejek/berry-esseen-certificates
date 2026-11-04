"""Create-only actual process captures for this bounded construction."""
from pathlib import Path
import datetime,hashlib,json,platform,subprocess,sys,time
HERE=Path(__file__).resolve().parent

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def dump(p,x):
    with p.open('x')as f:json.dump(x,f,indent=2,sort_keys=True);f.write('\n')

def main():
    if sys.flags.optimize:raise ValueError('assertions required')
    out=Path(sys.argv[1]).resolve();out.mkdir()
    watched=sorted(p for p in HERE.rglob('*')if p.is_file()and p.suffix in ('.py','.json'))
    before={str(p.relative_to(HERE)):digest(p)for p in watched}
    dump(out/'INPUTS.json',{'source_root':str(HERE),'source_sha256':before,'python':sys.version,
                          'executable':sys.executable,'executable_sha256':digest(Path(sys.executable)),'platform':platform.platform()})
    jobs=[('acceptance',[str(HERE/'accept.py'),str(HERE/'proof_objects.json')]),
          ('controls',[str(HERE/'controls.py'),str(out/'controls_data')])]
    results=[]
    for name,args in jobs:
        run=out/name;run.mkdir();argv=[sys.executable,'-I','-B']+args
        dump(run/'STARTED.json',{'argv':argv,'cwd':str(HERE),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
        t=time.monotonic()
        with (run/'stdout.txt').open('xb')as stdout,(run/'stderr.txt').open('xb')as stderr:
            p=subprocess.run(argv,cwd=HERE,stdout=stdout,stderr=stderr)
        process={'argv':argv,'returncode':p.returncode,'elapsed_seconds':time.monotonic()-t,
                 'stdout_sha256':digest(run/'stdout.txt'),'stderr_sha256':digest(run/'stderr.txt')}
        dump(run/'PROCESS.json',process)
        if p.returncode:raise RuntimeError('failed actual child '+name)
        result=json.loads((run/'stdout.txt').read_text());results.append({'job':name,**result})
    after={str(p.relative_to(HERE)):digest(p)for p in watched}
    if after!=before:raise RuntimeError('source changed during checks')
    dump(out/'RESULT.json',{'status':'PASS_BOUNDED_JOINT_COUNT_TWO_PANEL_PILOT','source_hashes_unchanged':True,'jobs':results,
                           'mathematical_status':'locally derived continuous-domain implication under inherited acquired same-law premises',
                           'execution_status':'fresh exact normalization, proof objects and controls','no_acquisition_or_Fourier_rerun':True})
    print(json.dumps({'status':'PASS_BOUNDED_JOINT_COUNT_TWO_PANEL_PILOT','jobs':len(results),'source_hashes_unchanged':True}))

if __name__=='__main__':main()

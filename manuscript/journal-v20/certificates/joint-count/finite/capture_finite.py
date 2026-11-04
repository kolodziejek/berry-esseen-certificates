"""Create-only complete267finite acceptance and bounded controls."""
from pathlib import Path
import datetime,json,platform,subprocess,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parent))
from capture import digest,dump
HERE=Path(__file__).resolve().parent

def main():
    if sys.flags.optimize:raise ValueError('assertions required')
    out=Path(sys.argv[1]).resolve();out.mkdir()
    watched=sorted(p for p in HERE.rglob('*')if p.is_file()and p.suffix in('.py','.json')and not any(x.startswith('portable')for x in p.relative_to(HERE).parts))
    before={str(p.relative_to(HERE)):digest(p)for p in watched}
    dump(out/'INPUTS.json',{'source_root':str(HERE),'source_sha256':before,'python':sys.version,
                          'executable':sys.executable,'executable_sha256':digest(Path(sys.executable)),'platform':platform.platform()})
    results=[]
    for name,args in [('acceptance',[str(HERE/'accept_finite.py'),str(HERE/'finite_proof_objects.json')]),
                      ('controls',[str(HERE/'controls_finite.py'),str(out/'controls_data')])]:
        run=out/name;run.mkdir();argv=[sys.executable,'-I','-B']+args
        dump(run/'STARTED.json',{'argv':argv,'cwd':str(HERE),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
        t=time.monotonic()
        with(run/'stdout.txt').open('xb')as stdout,(run/'stderr.txt').open('xb')as stderr:
            p=subprocess.run(argv,cwd=HERE,stdout=stdout,stderr=stderr)
        dump(run/'PROCESS.json',{'argv':argv,'returncode':p.returncode,'elapsed_seconds':time.monotonic()-t,
                               'stdout_sha256':digest(run/'stdout.txt'),'stderr_sha256':digest(run/'stderr.txt')})
        if p.returncode:raise RuntimeError('failed finite child '+name)
        result=json.loads((run/'stdout.txt').read_text());dump(run/'RESULT.json',result);results.append({'job':name,'status':result['status'],'returncode':p.returncode})
    after={str(p.relative_to(HERE)):digest(p)for p in watched}
    if after!=before:raise RuntimeError('finite source changed during checks')
    result={'status':'PASS_COMPLETE267_FINITE_TINY_JOINT_COUNT','source_hashes_unchanged':True,'jobs':results,
            'mathematical_scope':'local comparison implications under all inherited finite same-law acquisition, positive-excess and binomial-gap premises',
            'execution_scope':'fresh original normalization,267row coefficient acceptance and controls; no acquisition/binomial/integral campaign'}
    dump(out/'RESULT.json',result);print(json.dumps(result,sort_keys=True))

if __name__=='__main__':main()

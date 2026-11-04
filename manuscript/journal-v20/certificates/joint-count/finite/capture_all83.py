"""Portable exact full input-cover proof and mutation-control capture."""
from pathlib import Path
import datetime,json,platform,subprocess,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parent))
from capture import digest,dump
HERE=Path(__file__).resolve().parent

def main():
    if sys.flags.optimize:raise ValueError('assertions required')
    out=Path(sys.argv[1]).resolve();out.mkdir()
    watched=sorted(p for p in HERE.rglob('*')if p.is_file()and p.suffix in('.py','.json'))
    before={str(p.relative_to(HERE)):digest(p)for p in watched}
    dump(out/'INPUTS.json',{'source_root':str(HERE),'source_sha256':before,'python':sys.version,
                          'executable':sys.executable,'executable_sha256':digest(Path(sys.executable)),'platform':platform.platform()})
    results=[]
    for name,args in [('full_cover',[str(HERE/'audit_full_inputs.py')]),
                      ('object_controls',[str(HERE/'controls.py'),str(out/'object_controls_data')]),
                      ('input_controls',[str(HERE/'full_input_controls.py'),str(out/'input_controls_data')])]:
        run=out/name;run.mkdir();argv=[sys.executable,'-I','-B']+args
        dump(run/'STARTED.json',{'argv':argv,'cwd':str(HERE),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
        t=time.monotonic()
        with(run/'stdout.txt').open('xb')as stdout,(run/'stderr.txt').open('xb')as stderr:
            p=subprocess.run(argv,cwd=HERE,stdout=stdout,stderr=stderr)
        dump(run/'PROCESS.json',{'argv':argv,'returncode':p.returncode,'elapsed_seconds':time.monotonic()-t,
                               'stdout_sha256':digest(run/'stdout.txt'),'stderr_sha256':digest(run/'stderr.txt')})
        if p.returncode:raise RuntimeError('failed actual child '+name)
        result=json.loads((run/'stdout.txt').read_text());dump(run/'RESULT.json',result)
        results.append({'job':name,'status':result['status'],'returncode':p.returncode})
    after={str(p.relative_to(HERE)):digest(p)for p in watched}
    if after!=before:raise RuntimeError('source changed during checks')
    result={'status':'PASS_PORTABLE_ALL83_TINY_JOINT_COUNT','source_hashes_unchanged':True,'jobs':results,
            'mathematical_scope':'all83 inherited acquired uniform47 TINY input rows; C>=.4 and actual same-law support/centering remain premises',
            'execution_scope':'complete fixed polynomial/normalization/input census plus corruptions, no integral or acquisition replay'}
    dump(out/'RESULT.json',result);print(json.dumps(result,sort_keys=True))

if __name__=='__main__':main()

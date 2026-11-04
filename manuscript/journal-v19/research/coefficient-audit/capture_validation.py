"""Create-only capture of the bounded algebra pilot; no native integration."""
import hashlib,json,platform,subprocess,sys,time
from pathlib import Path

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write(path,o):
    with Path(path).open('x') as f:json.dump(o,f,indent=2,sort_keys=True);f.write('\n')
def main():
    if len(sys.argv)!=2 or not __debug__ or sys.flags.optimize:raise ValueError('one new run root, no optimization')
    out=Path(sys.argv[1]).resolve();out.mkdir(parents=True,exist_ok=False)
    source=Path(__file__).resolve().parent;python=Path(sys.executable).resolve()
    paths=sorted(source.glob('*.py'))+[source/'proof_objects.json']
    pins={str(p):{'sha256':sha(p),'bytes':p.stat().st_size}for p in paths}
    write(out/'INPUTS.json',{'sources':pins,'python':str(python),'python_sha256':sha(python),
                           'version':sys.version,'platform':platform.platform(),'optimized':sys.flags.optimize})
    jobs=[('acceptance',[str(source/'accept_objects.py'),str(source/'proof_objects.json')]),
          ('controls',[str(source/'controls.py'),str(out/'controls_data')]),
          ('actual_comparison',[str(source/'compare_actual.py'),str(out/'actual_data')])]
    results=[]
    for name,args in jobs:
        capture=out/(name+'_process');capture.mkdir()
        command=[str(python),'-I','-B',*args];start=time.time()
        write(capture/'STARTED.json',{'argv':command,'cwd':str(source),'started_unix':start,'source_pins':pins})
        with (capture/'stdout.txt').open('xb')as stdout,(capture/'stderr.txt').open('xb')as stderr:
            done=subprocess.run(command,cwd=source,stdout=stdout,stderr=stderr,check=False,timeout=120)
        record={'argv':command,'returncode':done.returncode,'elapsed_seconds':time.time()-start,
                'stdout_sha256':sha(capture/'stdout.txt'),'stderr_sha256':sha(capture/'stderr.txt')}
        write(capture/'PROCESS.json',record)
        if done.returncode:raise ValueError('failed bounded job: '+name)
        result=json.loads((capture/'stdout.txt').read_text());write(capture/'RESULT.json',result)
        results.append({'job':name,'returncode':done.returncode,'status':result['status']})
    if pins!={str(p):{'sha256':sha(p),'bytes':p.stat().st_size}for p in paths}:raise ValueError('source changed')
    final={'status':'PASS_BOUNDED_ALGEBRA_PILOT','jobs':results,'all_source_hashes_unchanged':True,
           'native_numeric_exports_accepted':False,'new_manuscript_proof_ancestor':False,'fourier_calls':0}
    write(out/'RESULT.json',final);print(json.dumps(final,sort_keys=True))
if __name__=='__main__':main()

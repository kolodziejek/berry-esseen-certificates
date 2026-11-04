"""Corrupt full acquired tables in disposable flat package copies."""
from pathlib import Path
import copy,json,shutil,subprocess,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parent))
from model import need,sha
HERE=Path(__file__).resolve().parent

def main():
    out=Path(sys.argv[1]).resolve();out.mkdir();records=[]
    mutations=[('missing_last_central','conditional_input47.json',lambda x:x['panels'].pop()),
               ('duplicated_last_central','conditional_input47.json',lambda x:x['panels'].append(copy.deepcopy(x['panels'][-1]))),
               ('reordered_left','left270_input47_table.json',lambda x:x['panels'].reverse()),
               ('gap_in_unselected_row','conditional_input47.json',lambda x:x['panels'][44].update(p=['469/1000','47/100'])),
               ('zero_noise_ceiling','left270_input47_table.json',lambda x:x['panels'][0].update(lambda_max='0'))]
    for name,file,mutation in mutations:
        trial=out/name;trial.mkdir()
        for source in ('model.py','polynomials.py','accept.py','audit_full_inputs.py','SELECTED_INPUTS.json','proof_objects.json'):
            shutil.copy2(HERE/source,trial/source)
        shutil.copytree(HERE/'native',trial/'native')
        path=trial/'native'/file;obj=json.loads(path.read_text());mutation(obj);path.write_text(json.dumps(obj)+'\n')
        argv=[sys.executable,'-I','-B',str(trial/'audit_full_inputs.py')];started=time.monotonic()
        with(trial/'stdout.txt').open('xb')as stdout,(trial/'stderr.txt').open('xb')as stderr:
            process=subprocess.run(argv,cwd=trial,stdout=stdout,stderr=stderr)
        text=(trial/'stderr.txt').read_text()
        need(process.returncode!=0 and 'fixed native source identity' in text,'full input mutation rejected by fixed complete source pin')
        record={'case':name,'argv':argv,'returncode':process.returncode,'elapsed_seconds':time.monotonic()-started,
                'mutated_input_sha256':sha(path),'stdout_sha256':sha(trial/'stdout.txt'),'stderr_sha256':sha(trial/'stderr.txt')}
        (trial/'PROCESS.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n');records.append(record)
    result={'status':'PASS_ALL83_INPUT_CORRUPTION_CONTROLS','rejected':len(records),'cases':records,
            'scope':'externally fixed full input identity; no source pin is relaxed to accept a malformed cover'}
    (out/'RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'rejected':len(records)}))

if __name__=='__main__':main()

"""Exact correspondence of re-derived moment contractions on captured cells.

No Fourier, numerical export or feedback state is accepted by this test.
"""
from pathlib import Path
from fractions import Fraction
import gzip, hashlib, json, sys, time

ALGEBRA=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ALGEBRA))
import coefficient_map as c


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def fractions(v):
    return [fractions(x) for x in v] if type(v)is list else Fraction(v)


def main():
    c.need(__debug__ and not sys.flags.optimize,'unoptimized Python')
    c.need(len(sys.argv)==3,'capture directory and new comparison run directory')
    CAPTURE=Path(sys.argv[1]).resolve()
    run=Path(sys.argv[2]).resolve();run.mkdir(parents=True,exist_ok=False)
    names=('coefficient_map.py','accept_objects.py','fixed_targets.py','poly.py','proof_objects.json')
    pins={name:sha(ALGEBRA/name) for name in names}
    capture_result=json.loads((CAPTURE/'RESULT.json').read_text())
    c.need(sha(CAPTURE/'cells.jsonl.gz')==capture_result['cells_sha256'],'exact captured row stream')
    started={'scope':'EXACT_PSD_CORRESPONDENCE_ONLY','sources':pins,'input_sha256':capture_result['cells_sha256'],'driver_sha256':sha(Path(__file__)),'runtime':{'executable':sys.executable,'sha256':sha(Path(sys.executable).resolve()),'version':sys.version,'optimized':sys.flags.optimize}}
    (run/'STARTED.json').write_text(json.dumps(started,indent=2)+'\n')
    c.verify(c.load(ALGEBRA/'proof_objects.json'))
    stages={};cases=0;t0=time.monotonic()
    with gzip.open(CAPTURE/'cells.jsonl.gz','rt') as stream:
        for line in stream:
            item=json.loads(line);row=item['cell'];actual=c.native_psd_prefix(row)
            for key in ('c4u','Mc','etac','corrections'):
                c.need(actual[key]==fractions(row[key]),f"mismatch stage{item['stage']} cell{tuple(row[k] for k in ('ir','ib','ig','im'))} {key}")
            stages[item['stage']]=stages.get(item['stage'],0)+1;cases+=1
    c.need(cases==capture_result['rows'],'all captured rows compared')
    c.need(pins=={name:sha(ALGEBRA/name)for name in names},'all algebra sources unchanged')
    result={'status':'PASS_ALL_CAPTURED_PSD_RECTANGLES','rows':cases,'stages':stages,'fields_per_row':['c4u','Mc','etac','corrections'],'seconds':time.monotonic()-t0,'all_source_hashes_unchanged':True,'fourier_evaluations':0,'native_numeric_exports_accepted':False,'feedback_states_reaccepted':False,'mathematical_scope':'coefficient equality under separately proved same-law moment and support premises'}
    (run/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,sort_keys=True),flush=True)


if __name__=='__main__':main()

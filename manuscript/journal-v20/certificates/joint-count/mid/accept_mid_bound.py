"""Bind the MID majorants to the exact new normalizer and full native input census."""
from pathlib import Path
from fractions import Fraction as F
from importlib.util import spec_from_file_location,module_from_spec
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from accept_mid import accept,need,unique
from mid_math import A,C,R0,LF,HF,TL,TU,ETA
if not __debug__ or sys.flags.optimize:raise RuntimeError('optimized Python forbidden')

def bound(tiny,proof):
    source=tiny/'native/tiny47wide_normalization.py'
    need(hashlib.sha256(source.read_bytes()).hexdigest()=='f1e2606359e321d17db11c7240467a597f00094d1747d40ed4f69ceae18d4b71','fixed native normalization source')
    spec=spec_from_file_location('mid47_native_normalization',source)
    native=module_from_spec(spec);spec.loader.exec_module(native)
    # New named .08 scope. Original gate formulas remain byte-for-byte intact.
    new={'derivative_hi':'113121/100000','derivative_lo':'86879/100000',
      'ef':'100000/88401','lmax':'2/25','logcap':'11599/100000',
      'normal_c':'592161/100000','normal_v':'306097/100000',
      'repair':'59549/25000','repair_multiplier':'159233/50000'}
    native.CFG.update({k:F(v)for k,v in new.items()})
    c=native.CFG;gates=native.check()
    need(all(F(v)>0 for v in gates.values()),'all normalization gates')
    need((c['amplitude'],1-c['d0'],c['ratio'],c['derivative_lo'],c['derivative_hi'])==(A,C,R0,LF,HF),'semantic coefficient binding')
    need(TL==c['ownlo']/20 and TU==c['ownhi']*c['lmax'],'actual variance enclosure')
    need(c['mass']*ETA*c['ownlo']-c['repair']/c['N']-F('1/1000')>0,'strict unchanged target')
    # This pinned sibling checker establishes the entire fixed acquired-input
    # cover and the global geometry; its TINY numerical success is additional.
    reader=tiny/'audit_full_inputs.py'
    need(hashlib.sha256(reader.read_bytes()).hexdigest()=='f3ccf04e0d7c4a5dbb5138a985a40a6211a2a7f6ee894c03f4282b9962f78301','fixed entire-row applicability reader')
    p=subprocess.run([sys.executable,'-I','-B',str(reader)],capture_output=True,text=True)
    need(p.returncode==0,'native full census actual child failed: '+p.stderr)
    census=json.loads(p.stdout,object_pairs_hook=unique)
    need(census['status']=='PASS_ALL83_UNIFORM47_TINY_INPUT_APPLICABILITY' and len(census['rows'])==83,'fixed entire census result')
    rows=[]
    for r in census['rows']:
        # Recover the actual acquired ceiling, not the TINY-truncated output.
        name='left270_input47_table.json'if r['side']=='left'else'conditional_input47.json'
        table=json.loads((tiny/'native'/name).read_text(),object_pairs_hook=unique)
        native_row=table['panels'][r['native_index']]
        need(native_row['p']==r['p'],'same row joins')
        upper=min(F(native_row['lambda_max']),c['lmax'])
        rows.append({'side':r['side'],'native_index':r['native_index'],'p':r['p'],
          'noise_interval':['1/20',str(upper)]if upper>=F('1/20')else None,
          'reason_if_empty':'acquired ceiling below1/20'if upper<F('1/20')else None})
    accepted=accept(json.loads(proof.read_text(),object_pairs_hook=unique))
    return {'status':'PASS_SOURCE_BOUND_ALL83_MID47','majorants':accepted,
      'CFG':{k:str(v)for k,v in c.items()},'normalization_gates':gates,'input_rows':rows,
      'nonempty_rows':sum(r['noise_interval']is not None for r in rows),
      'geometry_inherited_from':'complete83-row source-pinned sibling census',
      'mathematical_premises':['actual same iid conditional laws','conditional centering',
        'C>=2/5','acquired supports, signed thresholds and variance bounds',
        'manuscript analytic normalization and joint-count soundness proofs'],
      'no_acquisition_or_integral_replay':True,
      'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest()}

def main():
    print(json.dumps(bound(Path(sys.argv[1]).resolve(),Path(sys.argv[2]).resolve()),indent=2))
if __name__=='__main__':main()

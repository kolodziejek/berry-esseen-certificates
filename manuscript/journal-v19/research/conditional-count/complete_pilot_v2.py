#!/usr/bin/env python3
"""Add exact full CDFs and explicit finite-law specifications to frozen pilot01."""
from fractions import Fraction as F
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
from math import comb
import hashlib,json,sys

if not __debug__ or sys.flags.optimize:raise RuntimeError('optimized Python forbidden')
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('pilot',HERE/'own_count_obstruction.py')
pilot=module_from_spec(spec);spec.loader.exec_module(pilot)
out=Path(sys.argv[1]);out.mkdir(exist_ok=False)
saved=json.loads((HERE/'pilot01/checked/RESULT.json').read_text())
details=[]
for c in saved['cases']:
    p=F(c['p']);q=1-p;n=c['n'];k=c['k'];a=F(c['a']);v=p*q
    s=q*F(c['same_s0'])+p*F(c['same_s1']);m,b=c['own_count_V_W_factors']
    own_atom=pilot.integer_tail(m,b,0)-pilot.integer_tail(m,b,1)
    own_out=(1-own_atom)/2
    mass=[F(comb(n,j))*p**j*q**(n-j)for j in range(n+1)]
    base=sum(mass[:k+1],F(0))-mass[k]*own_out
    full={tag:base-mass[k-1]*F(c['tail_probabilities'][tag+'_out'])
                   +mass[k+1]*F(c['tail_probabilities'][tag+'_in']) for tag in ['A','B']}
    assert all(0<x<1 for x in full.values())
    assert full['A']-full['B']==F(c['CDF_A_minus_CDF_B'])
    # Classify the additional score hypothesis; the intended pilot does not assume it.
    beta=F(c['same_raw_absolute_third'])
    score_above={tag: x>F(1,2) and n*(v+s)**3*(x-F(1,2))**2>F(4,25)*beta**2
                 for tag,x in full.items()}
    m0=c['m0'];m1=c['m1']
    intervals={
      'A_U0':[-m0*a,m0*a],'A_U1':[-2*m1*a,2*m1*a],
      'B_U0':[-2*m0*a,2*m0*a],'B_U1':[-m1*a,m1*a]}
    assert intervals['A_U0'][1]<p and intervals['B_U0'][1]<p
    assert intervals['A_U1'][0]>-q and intervals['B_U1'][0]>-q
    details.append({
      'p':str(p),'n':n,'threshold_k':k,'normalized_threshold_H':'0',
      'm0':m0,'m1':m1,'a':str(a),
      'V_law':[[str(-a),'1/2'],[str(a),'1/2']],
      'W_law':[[str(-2*a),'1/8'],['0','3/4'],[str(2*a),'1/8']],
      'law_A':'B~Bernoulli(p); Y|B=0 is sum of m0 independent V; Y|B=1 is 1+sum of m1 independent W.',
      'law_B':'B~Bernoulli(p); Y|B=0 is sum of m0 independent W; Y|B=1 is 1+sum of m1 independent V.',
      'all_copies_independent':True,'iid_sum':'n independent copies of the selected entire mixture Y',
      'support_intervals_raw_U':{name:list(map(str,value))for name,value in intervals.items()},
      'normalization':{'X':'(Y-p)/sqrt(v+s)','v_plus_s':str(v+s),
        'support':'For B=0 subtract p from the displayed U0 interval; for B=1 add q to U1; divide both by sqrt(v+s).',
        'mean':'0','variance':'1','absolute_third':'same_raw_absolute_third/(v+s)^(3/2)'},
      'same_own_count_distribution':{'V_factors':m,'W_factors':b,
        'characteristic_function':'cos(a*t)^V_factors * ((3+cos(2*a*t))/4)^W_factors'},
      'own_count_atom_at_zero':str(own_atom),
      'CDF_A_at_k':str(full['A']),'CDF_B_at_k':str(full['B']),
      'CDF_A_minus_CDF_B':str(full['A']-full['B']),
      'signed_score_above_2_over_5':score_above,
      'scope':'These remain normalization-domain examples, not established attained/contact laws or accepted acquired rows.'})
result={'schema':'OWN_COUNT_INSUFFICIENCY_FULL_LAWS_V2','cases':details,
        'pilot_result_sha256':hashlib.sha256((HERE/'pilot01/checked/RESULT.json').read_bytes()).hexdigest()}
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'cases':len(details),'exact_full_cdfs_verified':True}))

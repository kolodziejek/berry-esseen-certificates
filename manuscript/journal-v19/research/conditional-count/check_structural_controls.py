#!/usr/bin/env python3
"""Bounded exact controls for the own-count pilot and scalar majorants.

These are finite diagnostics, not a proof of the all-parameter lemmas.
The latter are proved in STRUCTURAL_RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction as F
from importlib.util import spec_from_file_location, module_from_spec
from math import comb
from pathlib import Path
import hashlib,json,sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('optimized Python forbidden')
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('own_count_pilot',HERE/'own_count_obstruction.py')
pilot=module_from_spec(spec);spec.loader.exec_module(pilot)

def convolution(a,b):
    out=defaultdict(F)
    for x,p in a.items():
        for y,q in b.items():out[x+y]+=p*q
    return dict(out)

def binomial(n,p):
    return [F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(n+1)]

def choose(h,j):
    return comb(h,j) if h>=j else 0

def main():
    out=Path(sys.argv[1]);out.mkdir(exist_ok=False)
    checks=0
    V={-1:F(1,2),1:F(1,2)};W={-2:F(1,8),0:F(3,4),2:F(1,8)}
    # Independent small-support convolution, rather than the coefficient/suffix algorithm.
    for m in range(5):
        for b in range(5):
            law={0:F(1)}
            for _ in range(m):law=convolution(law,V)
            for _ in range(b):law=convolution(law,W)
            assert sum(law.values())==1
            for threshold in range(-m-2*b-1,m+2*b+3):
                expected=sum((p for x,p in law.items() if x>=threshold),F(0))
                assert pilot.integer_tail(m,b,threshold)==expected
                checks+=1
    identity_checks=near_checks=whole_checks=0
    invalid_chi=None;missing_cubic=None
    for n in range(2,16):
        for p in [F(1,5),F(9,25),F(2,5),F(1,2)]:
            mass=binomial(n,p);next_mass=binomial(n+1,p);q=1-p;v=p*q
            def pi(j):return mass[j] if 0<=j<=n else F(0)
            def cdf(j):return sum(mass[:max(0,min(n+1,j+1))],F(0))
            for j in range(-2,n+4):
                nextj=next_mass[j] if 0<=j<=n+1 else F(0)
                assert nextj==q*pi(j)+p*pi(j-1)
                assert pi(j)-pi(j-1)==F((n+1)*p-j,(n+1)*v)*nextj
                identity_checks+=1
            for k in range(1,n):
                chi=(n+1)*p-k;curv=max(mass)/((n+1)*v*mass[k])
                for r in range(-n-3,n+4):
                    G=(cdf(k+r)-cdf(k))/mass[k]
                    near=-int(r<=-1)+sum((mass[k+i]/mass[k] for i in range(1,n-k+1) if r>=i),F(0))
                    assert G<=near;near_checks+=1
                    positive=max(r,0);negative=max(-r,0)
                    whole=r+curv*(max(chi-1,0)*positive+max(chi,0)*choose(negative,2)+choose(negative,3))
                    if chi<2:
                        assert G<=whole;whole_checks+=1
                        without_cubic=whole-curv*choose(negative,3)
                        if G>without_cubic and missing_cubic is None:
                            missing_cubic={'n':n,'p':str(p),'k':k,'r':r}
                    elif G>whole and invalid_chi is None:
                        invalid_chi={'n':n,'p':str(p),'k':k,'r':r,'chi':str(chi)}
    assert missing_cubic is not None and invalid_chi is not None
    # Exact atoms reject replacement of the strict outgoing event by a closed event.
    assert pilot.tail(0,1,F(1,2),False)==F(1,8)
    assert pilot.tail(0,1,F(1,2),True)==0
    # A negative coefficient requires the lower multiplier endpoint, not the upper.
    assert max(F(1)*F(-1),F(2)*F(-1))==F(-1)>F(-2)
    # Frozen pilot readback: preserve its distinction between arithmetic and theorem scope.
    saved=json.loads((HERE/'pilot01/checked/RESULT.json').read_text())
    cases=[pilot.case(F(2,5),150,2,3,F(9,4000)),pilot.case(F(9,25),150,9,16,F(1,2500))]
    # JSON normalizes tuples to lists.
    assert json.loads(json.dumps(cases))==saved['cases']
    result={'schema':'STRUCTURAL_BOUNDED_CONTROLS_V1','status':'PASS',
      'independent_small_convolution_tail_checks':checks,
      'binomial_degree_elevation_difference_identity_checks':identity_checks,
      'nearest_pointwise_majorant_checks':near_checks,
      'whole_pointwise_majorant_checks':whole_checks,
      'rejected_false_variants':{'omit_cubic_term':missing_cubic,'omit_chi_lt_2_gate':invalid_chi,
        'close_strict_outgoing_event':True,'use_wrong_endpoint_for_negative_coefficient':True},
      'full_pilot_result_reproduced_exactly':True,
      'scope':'Finite exact controls; not a replacement for the symbolic proof or any native certificate campaign.',
      'pilot_source_sha256':hashlib.sha256((HERE/'own_count_obstruction.py').read_bytes()).hexdigest()}
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()

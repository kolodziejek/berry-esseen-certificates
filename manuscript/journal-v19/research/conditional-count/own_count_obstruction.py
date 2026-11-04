#!/usr/bin/env python3
"""Exact bounded examples: the own-count law does not determine the full CDF."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
from decimal import Decimal,localcontext
import json,sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('optimized Python forbidden')

@lru_cache(None)
def w_coefficients(b):
    # W/a has weights (1,6,1)/8 at (-2,0,2).
    coefficients=[1]
    for _ in range(b):
        new=[0]*(len(coefficients)+2)
        for j,c in enumerate(coefficients):
            new[j]+=c;new[j+1]+=6*c;new[j+2]+=c
        coefficients=new
    assert sum(coefficients)==8**b
    return tuple(coefficients)

def integer_tail(m,b,threshold):
    # Sum of m independent V/a=(+-1) and b independent W/a.
    coefficients=w_coefficients(b)
    suffix=[0]*(len(coefficients)+1)
    for j in range(len(coefficients)-1,-1,-1):suffix[j]=suffix[j+1]+coefficients[j]
    count=0
    for i in range(m+1):
        lo=(threshold-(2*i-m)+2*b+1)//2
        count+=comb(m,i)*suffix[max(0,min(len(coefficients),lo))]
    return F(count,2**m*8**b)

def tail(m,b,a,strict):
    threshold=F(1,a)
    cut=(threshold.numerator//threshold.denominator+1 if strict else
         -((-threshold.numerator)//threshold.denominator))
    return integer_tail(m,b,cut)

def case(p,n,m0,m1,a):
    q=1-p;k=n*p
    assert k.denominator==1;k=int(k)
    assert q*m0==p*m1
    own_a=(m0*(n-k),m1*k)
    own_b=(m1*k,m0*(n-k))
    assert own_a==own_b
    s0=m0*a*a;s1=m1*a*a;s=q*s0+p*s1;v=p*q
    lam=n*s;theta=s/(v+s)
    d_a=(m0+2*m1)*a;d_b=(2*m0+m1)*a
    amplitude=max(2*m0,2*m1)*a
    assert F(304,1000)<=p<=F(47,100) and n>=47
    assert max(d_a,d_b)<F(181,10000) and amplitude<F(425,1000)
    assert 0<lam<F(5,100) and theta<F(154,10000)
    # Ordinary moments and absolute third moment of Y-p agree.
    fourth_a=q*(p**4+6*p*p*s0+(3*m0*m0-2*m0)*a**4)+p*(q**4+6*q*q*s1+(3*m1*m1+m1)*a**4)
    fourth_b=q*(p**4+6*p*p*s0+(3*m0*m0+m0)*a**4)+p*(q**4+6*q*q*s1+(3*m1*m1-2*m1)*a**4)
    assert fourth_a==fourth_b
    absolute_third=v*(1-2*v)+3*v*(s0+s1)
    # Away from k+-1, the conditional event is identically true or false.
    for j in range(n+1):
        max_a=(m0*(n-j)+2*m1*j)*a
        max_b=(2*m0*(n-j)+m1*j)*a
        if j<=k-2:assert max(max_a,max_b)<k-j
        if j>=k+2:assert max(max_a,max_b)<j-k
    counts={
       'A_out':(m0*(n-k+1),m1*(k-1)),
       'B_out':(m1*(k-1),m0*(n-k+1)),
       'A_in':(m0*(n-k-1),m1*(k+1)),
       'B_in':(m1*(k+1),m0*(n-k-1)),
    }
    tails={name:tail(m,b,a,strict=name.endswith('out')) for name,(m,b)in counts.items()}
    pi_minus=F(comb(n,k-1))*p**(k-1)*q**(n-k+1)
    pi_plus=F(comb(n,k+1))*p**(k+1)*q**(n-k-1)
    difference=pi_plus*(tails['A_in']-tails['B_in'])-pi_minus*(tails['A_out']-tails['B_out'])
    assert difference!=0
    atoms={name:tail(m,b,a,False)-tail(m,b,a,True) for name,(m,b)in counts.items()}
    with localcontext() as ctx:
        ctx.prec=18;approx=str(Decimal(difference.numerator)/Decimal(difference.denominator))
    return {'p':str(p),'n':n,'k':k,'u':'0','H':'0','m0':m0,'m1':m1,'a':str(a),
      'own_count_V_W_factors':own_a,'same_s0':str(s0),'same_s1':str(s1),
      'same_lambda':str(lam),'same_theta':str(theta),'same_raw_absolute_third':str(absolute_third),
      'same_raw_fourth':str(fourth_a),'max_inward_A':str(d_a),'max_inward_B':str(d_b),
      'common_amplitude':str(amplitude),'conditional_factor_counts':counts,
      'tail_probabilities':{key:str(value) for key,value in tails.items()},
      'atoms_at_positive_one':{key:str(value) for key,value in atoms.items()},
      'CDF_A_minus_CDF_B':str(difference),'diagnostic_decimal_difference':approx,
      'strict_outgoing_closed_incoming':True,
      'scope':'Shared normalization-domain example, not an attaining/contact law or an accepted acquired resource row; not a counterexample to the theorem.'}

def main():
    out=Path(sys.argv[1]);out.mkdir(exist_ok=False)
    result={'schema':'OWN_COUNT_INSUFFICIENCY_EXACT_V1',
      'cases':[case(F(2,5),150,2,3,F(9,4000)),case(F(9,25),150,9,16,F(1,2500))],
      'claim':'Same own-count distribution, p,n,H, conditional variances, first four ordinary moments and absolute third moment do not determine the full conditional-count CDF.',
      'arithmetic':'stdlib exact integers and Fraction; decimals are diagnostic only'}
    assert any(F(v)>0 for v in result['cases'][1]['atoms_at_positive_one'].values())
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([{'p':c['p'],'lambda':c['same_lambda'],'CDF_difference':c['diagnostic_decimal_difference']}for c in result['cases']],indent=2))

if __name__=='__main__':main()

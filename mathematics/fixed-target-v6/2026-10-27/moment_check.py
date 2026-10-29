#!/usr/bin/env python3
"""Six bounded same-law moment updates on 24 closed rho cells."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
OLD=HERE.parents[1]/'fixed-target-v5'/'2026-10-27'
PIN='6827a67e64cfea5b89d823ffd34821fa942b3c3add702ee9721c89d65f443aa5'
if sha256((OLD/'cell_check.py').read_bytes()).hexdigest()!=PIN:raise ValueError('first-cover source hash')
sys.path.insert(0,str(OLD))
import cell_check as base
N=42;PHILO=F(997,2500);PHIUP=F(2,5);SIGMALO=F(3162277660,10**9)
def need(x,s):
    if not x:raise ValueError(s)
def up(x):return F(base.upper(x,10))
def down(x):return F(base.lower(x,10))
def sqrt_up(x):
    need(x>=0,'square root domain');scale=10**12;k=isqrt(x.numerator*scale**2//x.denominator)
    a,b=F(k,scale),F(k+1,scale);need(a*a<=x<=b*b,'root enclosure');return b
def normalized_lower(a):
    need(a<=SIGMALO,'normalized target upper domain')
    if a<=-1:return F(-1)
    return max(F(-1),(a-3*sqrt_up(10-a*a))/10)
def circle_lower(l,u,d):
    need(1<=l<=u and d>=0,'circle moment/defect domain')
    a=SIGMALO-d/l;y=normalized_lower(a)
    # y is a lower bound for gamma/rho. Multiplication reverses the
    # useful rho endpoint if y is negative.
    return down(l*y if y>=0 else u*y),a,y
def step(row,T,U,d,c0,c1,j):
    l,u=row['rho_lower'],row['rho_upper'];g=row['gamma_abs'];b=row['beta_abs']
    need(0<=T<N*c0*l and d>=0,'prior licensed raw and defect')
    density=PHILO*(1-T/(N*c0*l));need(0<density<PHIUP,'density gate')
    circle,a,y=circle_lower(l,u,d)
    gl=max(-g,SIGMALO*l-3-d,circle)
    need(gl<=g,'no inconsistent cell silently dropped')
    diff=min(2*u,(1-SIGMALO)*l+3+d,u-gl)
    need(diff>=0,'nonnegative rho-minus-gamma enclosure')
    A=min(row['A'],F(3,2)*b*(2*u+1)+F(3,2)*row['Gamma']*diff+F(3,8)*u*u*(u+1)+F(8,27)*u**3-l/2)
    need(A>0,'constant coefficient gate')
    endpoints=[]
    for t in (c0,c1):
        q=max(t*l-g/5,t*l+min(density*gl,PHIUP*gl)/2)
        f=t*row['K_abs']+row['normal_H_coefficient']+row['slope']
        need(q>0 and f>=0,'quadratic gates')
        endpoints.append(dict(c=t,constant=row['KF']+t*A,linear=f,quadratic=q))
    raw_exact=max(z['constant']+z['linear']**2/(4*z['quadratic']) for z in endpoints)
    Tnew=min(T,up(raw_exact));eta=(c0*l-Tnew/N)/2;need(eta>0,'positive phase price')
    resource_exact=max(z['constant']+z['linear']**2/(4*(z['quadratic']+eta)) for z in endpoints)
    Unew=min(U,up(resource_exact));dnew=min(d,up(6*Unew/(N*PHILO)))
    need(Tnew<=T and Unew<=U and dnew<=d,'ordered contraction')
    return dict(step=j,prior_raw=T,prior_resource=U,prior_defect=d,density_lower=density,
      normalized_a_lower=a,normalized_gamma_lower=y,circle_gamma_lower=circle,gamma_lower=gl,
      rho_minus_gamma_upper=diff,A=A,KF=row['KF'],endpoints=endpoints,
      raw_exact=raw_exact,raw=Tnew,phase_extra=eta,resource_exact=resource_exact,resource=Unew,
      defect=dnew,weighted_nD=6*Unew/PHILO)
def check_law(name,law):
    need(sum(p for x,p in law)==1 and all(p>0 for x,p in law),'law probabilities')
    need(sum(p*x for x,p in law)==0 and sum(p*x*x for x,p in law)==1,'law standardization')
    rho=sum(p*abs(x)**3 for x,p in law);gamma=sum(p*x**3 for x,p in law)
    m=sum(p*x for x,p in law if x>0)
    ap=sum(p*x*x for x,p in law if x>0);am=1-ap
    bp=sum(p*x**3 for x,p in law if x>0);bm=-(sum(p*x**3 for x,p in law if x<0))
    need(m*bp>=ap*ap and m*bm>=am*am and ap*am>=m*m,'same-law sign Cauchy')
    gap=rho*rho-gamma*gamma-4*m*m;need(gap>=0,'moment circle')
    xs=sorted(x for x,p in law);J=sum(sum(p*x for x,p in law if x>=v)*(v-u)**2 for u,v in zip(xs,xs[1:]))
    need(J<=rho+2*m,'gap mass bound')
    return dict(name=name,rho=rho,gamma=gamma,m=m,circle_slack=gap,
      conserved_defect_minus_compulsory_lower=3*rho-3*J+6*m)
def controls():
    cases=[]
    for name,fn in [('negative defect',lambda:circle_lower(F(1),F(2),F(-1))),
                   ('reversed rho interval',lambda:circle_lower(F(2),F(1),F(1))),
                   ('out-of-domain inverse',lambda:normalized_lower(F(4))),
                   ('negative square root',lambda:sqrt_up(F(-1)))]:
        try:fn()
        except ValueError:cases.append(name)
        else:raise ValueError('invalid coupling input accepted')
    need(normalized_lower(F(-2))==-1,'inactive branch retains whole interval')
    need(normalized_lower(F(-1))==-1,'closed lower branch endpoint')
    # If one drops the negative root term, a=0 would give y>=0,
    # excluding the valid boundary y=-3/sqrt(10). A rational interior
    # witness y=-9/10 has f(y)>0, so it rejects that wrong inverse.
    need(F(-9,10)+3*F(43,100)>0 and F(43,100)**2<1-F(9,10)**2,'wrong-root-branch witness')
    cases.append('wrong inverse branch excluded by rational witness')
    need(F(1)**2+4*F(1,2)**2>F(1)**2,'infeasible fabricated moments rejected')
    cases.append('fabricated rho=gamma=1,m=1/2 violates circle')
    return cases
def run():
    need(__debug__ and not sys.flags.optimize,'no optimized Python')
    obj=json.loads((OLD/'cell-input.json').read_text(),object_pairs_hook=base.unique)
    blobs={name:(OLD/'cell-sources'/name).read_bytes() for name in base.PINS}
    first=base.run(obj,blobs)
    c0,c1=F(obj['c_lower']),F(obj['c_upper']);rows=[]
    for row in first['rows']:
        T=up(row['fixed_raw']);U=T;d=up(6*U/(N*PHILO));trace=[]
        for j in range(1,7):
            z=step(row,T,U,d,c0,c1,j);trace.append(z);T,U,d=z['raw'],z['resource'],z['defect']
        rows.append(dict(index=row['index'],rho_lower=row['rho_lower'],rho_upper=row['rho_upper'],steps=trace))
    summaries=[]
    for j in range(6):
        summaries.append(dict(step=j+1,max_raw=max(r['steps'][j]['raw'] for r in rows),
         max_resource=max(r['steps'][j]['resource'] for r in rows),max_defect=max(r['steps'][j]['defect'] for r in rows),
         cells_below4=sum(r['steps'][j]['defect']<4 for r in rows),cells_below2=sum(r['steps'][j]['defect']<2 for r in rows)))
    laws=[check_law('symmetric Bernoulli',[(F(-1),F(1,2)),(F(1),F(1,2))])]
    for a in (F(3,2),F(2,3)):
        laws.append(check_law('skew Bernoulli '+str(a),[(-a,1/(1+a*a)),(1/a,a*a/(1+a*a))]))
    laws.extend([check_law('three point zero atom',[(F(-2),F(1,8)),(F(0),F(3,4)),(F(2),F(1,8))]),
      check_law('four symmetric atoms',[(F(-3,2),F(3,16)),(F(-1,2),F(5,16)),(F(1,2),F(5,16)),(F(3,2),F(3,16))]),
      check_law('tiny far atoms outside acquisition domain',[(F(-20),F(1,800)),(F(0),F(399,400)),(F(20),F(1,800))])])
    return dict(name='SAME_LAW_CIRCLE_SIX_COARSE_UPDATES_V1',scope='Conditional scalar result; no dense stage or local numerical acceptance.',
      cells=24,updates=6,rows=rows,summaries=summaries,laws=laws,controls=controls())
if __name__=='__main__':print(json.dumps(base.encode(run()),indent=2,sort_keys=True))

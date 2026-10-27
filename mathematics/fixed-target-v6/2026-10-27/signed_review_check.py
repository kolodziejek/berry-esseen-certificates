#!/usr/bin/env python3
"""Independent exact review of C's fixed signed table; never imports its code."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
import json,sys
PINS={
 'mathematics/fixed-target-v6/2026-10-27/signed-proof/signed.tex':'43dc933883f313b26a6b4a0a99b57369f98a3ec2093707818e63dda5a1f9ef56',
 'mathematics/fixed-target-v6/2026-10-27/signed-check.py':'c827917d18b241d7e6255b3c15184ca719044cc3b7ffb8c7474ea5482dd7a847',
 'runs/fixed-target-v6-20261027/signed02/stdout.json':'3376557f83874f571ed1c7cfad10b82930e736427ba597b5c8ed76b3c46b1944',
 'runs/fixed-target-v5-20261027/cell02/check.stdout.json':'7525713bd06a30b9c13693d01949d4f186890128eed3432771953ef9eafef082'}
R=F(96,25)
def need(x,message):
    if not x:raise ValueError(message)
def verify(rows,prior):
    need(len(rows)==len(prior)==24,'complete 24-cell count');results=[]
    for i,z in enumerate(rows):
        l,u=1+F(3361*i,96000),1+F(3361*(i+1),96000)
        need(z['index']==i and F(z['rho_lower'])==l and F(z['rho_upper'])==u,'fixed ordered closed cells')
        b=F(z['beta_abs']);h=1+b
        need(0<=b<1 and (1+b*b)**2>=u*u*(1-b*b),'independent beta polynomial test')
        al,au=(3*l-R)/2,(3*u-R)/2
        # Bernstein coefficients of the h-derivative on [0,h*].
        bern=[F(3),3+al*h,3+2*al*h-F(3,2)*h*h]
        gates=[h-au,bern[-1],R-3*u+F(3,2)*h*h]
        strong=all(x>=0 for x in gates)
        need(z['strong_gate_passed'] is strong,'strong gate truth value')
        need([F(z[k]) for k in ('h_above_a_gate','h_derivative_gate','rho_derivative_gate')]==gates,'exact gate margins')
        p0=3*b+h*R*R/8;p1=R-3*h*R/4;p2=-F(3,2)+9*h/8
        Q=lambda r:p0+p1*r+p2*r*r
        candidates=[Q(l),Q(u)]
        if p2<0 and l<=-p1/(2*p2)<=u:candidates.append(Q(-p1/(2*p2)))
        easy=max(candidates)
        need(F(z['unconstrained_cap'])==easy,'quadratic endpoint/vertex bound')
        if strong:
            need(min(bern)>=0,'independent full-h derivative Bernstein certificate')
            # Evaluate the original signed expression at delta=h².
            cap=R*u-F(3,2)*u*u-3+3*h+au*h*h-(h*h)**2/(2*h)
            need(F(z['constrained_cap'])==cap,'constrained maximum from original expression')
            new=min(easy,cap)
        else:
            need(z['constrained_cap'] is None,'failed gates are not extrapolated');new=easy
        need(F(z['new_K_abs'])==new,'new absolute cap')
        effective=min(new,F(z['retained_K_abs']))
        need(F(z['effective_K_abs'])==effective<=F(z['safe_K_decimal']),'effective outward K bound')
        old=prior[i];need(old['index']==i and F(old['beta_abs'])==b,'prior beta binding')
        M=min(F(111,10),R*u,1+(R+1)**2/(R+F(1,2))*(u-1))
        Gamma=F(old['Gamma']);need(Gamma>=0,'conditional gap coefficient sign')
        other=3*b*(2*u+1)/2+2*u*M-l/2
        shared=3*b*(2*u+1)/2+3*Gamma*u+3*u*u*(u+1)/8-l/2
        newA=min(shared+u**3/4,other);oldA=min(shared+8*u**3/27,other)
        need(F(z['retained_A'])==oldA and F(z['new_A'])==newA,'independent quarter-constant reconstruction')
        need(newA<=oldA and newA<=F(z['safe_A_decimal']),'outward improved constant')
        results.append(dict(index=i,strong=strong,bernstein=[str(x) for x in bern],K=str(new),effective=str(effective)))
    return results
def law_check(name,law,radius):
    E=lambda fn:sum(p*fn(x) for x,p in law)
    need(sum(p for x,p in law)==1 and all(p>=0 and abs(x)<=radius for x,p in law),'actual probabilities and support')
    need(E(lambda x:x)==0 and E(lambda x:x*x)==1,'standardization')
    rho=E(lambda x:abs(x)**3);beta=E(lambda x:x*abs(x));gamma=E(lambda x:x**3)
    K=E(lambda x:x*abs(x)**3)-3*beta-F(3,2)*rho*gamma
    need(E(lambda x:abs(x)**3*(abs(x)-rho)**2)==E(lambda x:abs(x)**5)-2*rho*E(lambda x:x**4)+rho**3,'fifth square identity')
    for eps in (1,-1):
        h=1-eps*beta;d=rho-eps*gamma
        need(h>0 and d>=h*h,'signwise constraint')
        bound=radius*rho-F(3,2)*rho*rho-3+3*h+(F(3,2)*rho-radius/2)*d-d*d/(2*h)
        need(eps*K<=bound,'direct signed envelope both reflections')
    return dict(name=name,rho=str(rho),K=str(K),radius=str(radius))
def main():
    need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'fixed unoptimized invocation')
    root=Path(sys.argv[1]);blobs={p:(root/p).read_bytes() for p in PINS}
    for p,sha in PINS.items():need(sha256(blobs[p]).hexdigest()==sha,'review source hash '+p)
    data=json.loads(blobs['runs/fixed-target-v6-20261027/signed02/stdout.json'])
    prior=json.loads(blobs['runs/fixed-target-v5-20261027/cell02/check.stdout.json'])['rows']
    rows=data['rows'];review=verify(rows,prior);controls=[]
    for name,mutate in [
      ('missing cell',lambda x:x.pop()),('reordered cells',lambda x:x.reverse()),
      ('duplicate cell',lambda x:x.__setitem__(1,deepcopy(x[0]))),
      ('understated constrained cap',lambda x:x[-1].update(constrained_cap='99/25')),
      ('forced failed gate',lambda x:x[1].update(strong_gate_passed=True)),
      ('invalid beta cap',lambda x:x[-1].update(beta_abs='1/10'))]:
        changed=deepcopy(rows);mutate(changed)
        try:verify(changed,prior)
        except ValueError:controls.append(name)
        else:raise ValueError('mutation accepted '+name)
    laws=[]
    for i,z in enumerate(data['actual_laws']):
        laws.append(law_check('constructor literal law '+str(i),list(zip(map(F,z['xs']),map(F,z['ps']))),R))
    laws.append(law_check('four-point law',[(F(-3,2),F(3,16)),(F(-1,2),F(5,16)),(F(1,2),F(5,16)),(F(3,2),F(3,16))],F(3,2)))
    laws.append(law_check('tiny far atoms, universal inequality only',[(F(-20),F(1,800)),(F(0),F(399,400)),(F(20),F(1,800))],F(20)))
    print(json.dumps(dict(name='INDEPENDENT_SIGNED_COEFFICIENT_REVIEW_V1',source_pins=PINS,
      rows=review,laws=laws,rejected_controls=controls,no_constructor_or_fourier_execution=True),indent=2))
if __name__=='__main__':main()

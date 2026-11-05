"""Bounded floating exploration only; no numerical proof claims."""
from fractions import Fraction as F
from itertools import product
from math import factorial,sqrt,erf
from pathlib import Path
import json,random,sys
N=5;A0=F(82453,125000);A1=F(703209,1000000);CAP=.30748
CE=(3+sqrt(10))/(6*sqrt(2*3.141592653589793))
counts=[]
for a in range(6):
 for b in range(6-a):
  for c in range(6-a-b):
   d=5-a-b-c;ns=(a,b,c,d);mult=factorial(5)
   for z in ns:mult//=factorial(z)
   counts.append((ns,mult))
def test(p,A,b,a,B):
    pp=float(p);qq=1-pp;v=pp*qq
    A,b,a,B=map(float,(A,b,a,B))
    if not A*b*a*B:return None
    atoms=(-A,b,1-a,1+B)
    probs=(qq*b/(A+b),qq*A/(A+b),pp*B/(a+B),pp*a/(a+B))
    x=qq*A*b;y=pp*a*B;w=v+x+y;lam=5*(x+y)
    beta=(v*(1-2*pp)-x+y)/w
    rho=sum(r*abs(z-pp)**3 for z,r in zip(atoms,probs))/w**1.5
    if lam>CAP or not (-.030586<=beta<=.307221 and 1.1<=rho<=1.15):return None
    arr=[]
    for ns,mult in counts:
        mass=float(mult);z=0.
        for j,c in enumerate(ns):mass*=probs[j]**c;z+=atoms[j]*c
        arr.append((z,mass))
    arr.sort();cum=0.;best=None
    for i,(z,mass) in enumerate(arr):
        cum+=mass
        if i+1<len(arr) and abs(arr[i+1][0]-z)<1e-12:continue
        h=(z-5*pp)/sqrt(w)
        if abs(h)>2.051019:continue
        gap=cum-(1+erf(h/sqrt(10)))/2
        margin=gap-CE*1.1/sqrt(5)
        if best is None or margin>best['floor_margin']:
            best=dict(floor_margin=margin,threshold=z,raw_H=h,discrepancy=gap,
              actual_score=sqrt(5)*gap/rho,rho=rho,beta=beta,noise=lam,
              meanabs=sum(r*abs(z-pp) for z,r in zip(atoms,probs))/sqrt(w))
    return best
def main(out):
    rng=random.Random(20261105);best=None;admitted=0;total=18000
    fractions=[F(1,10**k) for k in range(1,7)]+[F(i,20) for i in range(1,21)]
    for _ in range(total):
        p=rng.choice((F(19,50),F(77,200),F(39,100)));q=1-p
        A=A0*rng.choice(fractions);B=A1*rng.choice(fractions)
        b=p*rng.choice(fractions);a=q*rng.choice(fractions)
        if a+b>F(471533,500000):continue
        result=test(p,A,b,a,B)
        if result is None:continue
        admitted+=1
        if best is None or result['floor_margin']>best['floor_margin']:
            best=dict(result,law=dict(p=str(p),outward0=str(A),inward0=str(b),inward1=str(a),outward1=str(B)))
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    result=dict(status='FLOATING_EXPLORATION_ONLY',tested=total,admitted_noise_beta_rho=admitted,best=best,
      scope='Actual two-point conditional pairs. No contact or full acquired-row membership claim. Any positive margin requires fresh exact verification.')
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main(sys.argv[1])

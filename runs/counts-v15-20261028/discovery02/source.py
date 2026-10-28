"""Bounded floating discovery for actual three-point marginals; not acceptance."""
from fractions import Fraction as F
from math import comb,sqrt,erf,floor
from bisect import bisect_right
import itertools,json,time
A=F(3,5)
def phi(x):return .5*(1+erf(x/sqrt(2)))
def law(n,p,lam,kind):
 q=1-p;eps=lam/(n*(q if kind==0 else p)*A);theta=eps/(A+eps)
 pi=[float(F(comb(n,j))*p**j*q**(n-j)) for j in range(n+1)]
 raw={}
 for j in range(n+1):
  m=n-j if kind==0 else j
  for r in range(m+1):
   x=j+(n-j)*eps-r*(A+eps) if kind==0 else j*(1-eps)+r*(A+eps)
   w=pi[j]*comb(m,r)*float(theta)**r*float(1-theta)**(m-r)
   raw[x]=raw.get(x,0.)+w
 values=sorted(raw);cdf=[];total=0.
 for x in values:total+=raw[x];cdf.append(total)
 B=[];total=0.
 for w in pi:total+=w;B.append(total)
 v=p*q;s=lam/n
 v0=A*eps if kind==0 else F(0);v1=A*eps if kind==1 else F(0)
 mu0=v0*(eps-A);mu1=v1*(A-eps)
 M3=v*(1-2*v)+3*v*(v0+v1)-q*mu0+p*mu1
 rho=float(M3)/float(v+s)**1.5;rhoB=float(1-2*v)/sqrt(float(v))
 return eps,values,cdf,B,rho,rhoB
records=[];start=time.perf_counter()
for n,p,lam,kind in itertools.product([42,80],[F(2,5),F(1,2),F(53,100)],[F(9,250000),F(3,40),F(18,125),F(9,25)],[0,1]):
 eps,xs,Fs,B,rho,rhoB=law(n,p,lam,kind);v=p*(1-p);V=v+lam/n
 lower=float(n*p)-1.84*sqrt(float(V));upper=float(n*p)+1.84*sqrt(float(V))
 candidates=[x for x in xs if lower<=float(x)<=upper]
 for j in range(floor(lower)-1,floor(upper)+2):
  candidates.extend([F(j),F(j)-F(34,125)])
 candidates=[x for x in candidates if lower<=float(x)<=upper]
 for anchor in ['floor','shifted']:
  worst=None
  for t in candidates:
   k=t.__floor__() if anchor=='floor' else (t+F(34,125)).__floor__()
   actual=Fs[bisect_right(xs,t)-1] if bisect_right(xs,t)>0 else 0
   delta=sqrt(n)*(actual-B[k]-phi(float(t-n*p)/sqrt(n*float(V)))+phi(float(k-n*p)/sqrt(n*float(v))))+.4*(rhoB-rho)
   if worst is None or delta>worst['delta']:worst={'delta':delta,'t':str(t),'k':k,'phase':str(t-k)}
  records.append({'n':n,'p':str(p),'lambda':str(lam),'kind':kind,'epsilon':str(eps),'anchor':anchor,'candidates':len(candidates),'worst':worst})
print(json.dumps({'status':'DISCOVERY_ONLY','elapsed_seconds':time.perf_counter()-start,'cases':len(records),'evaluations':sum(r['candidates'] for r in records),'positive_records':[r for r in records if r['worst']['delta']>0],'worst_moderate':sorted([r for r in records if F(r['lambda'])>=F(3,40)],key=lambda r:r['worst']['delta'],reverse=True)[:12],'records':records},indent=2))

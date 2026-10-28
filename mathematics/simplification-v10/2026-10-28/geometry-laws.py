"""Exact actual-law adversarial checks for the direct budget, in Q(sqrt(10))."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
SL,SU=F('3.162277660'),F('3.162277661')
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def scale(a,b):return(a[0]*b,a[1]*b)
def sign(a):
 x,y=a
 if x==0:return (y>0)-(y<0)
 if y==0:return (x>0)-(x<0)
 if x>0 and y>0:return 1
 if x<0 and y<0:return -1
 z=x*x-10*y*y
 return ((z>0)-(z<0)) if x>0 else ((z<0)-(z>0))
def enclosure(a):
 x,y=a
 return sorted([x+y*SL,x+y*SU])
def law(values):
 merged={}
 for x,w in values:
  if w<=0:raise ValueError('positive masses')
  merged[x]=merged.get(x,F(0))+w
 xs=sorted(merged.items())
 if sum(w for x,w in xs)!=1:raise ValueError('unit mass')
 mu=sum(x*w for x,w in xs);xs=[(x-mu,w)for x,w in xs]
 if any(x==0 for x,w in xs):raise ValueError('central gap excludes zero atom')
 V=sum(x*x*w for x,w in xs)
 if V<=0:raise ValueError('positive variance')
 p=sum(w for x,w in xs if x>0);q=1-p
 if not 0<p<1:raise ValueError('both signs')
 m=sum(x*w for x,w in xs if x>0);ell=m/(p*q);theta=1-m*m/(p*q*V);w=1-theta
 A=min(-x for x,t in xs if x<0);B=min(x for x,t in xs if x>0)
 a0=(m/q-A)/ell;a1=(m/p-B)/ell;d=1-(A+B)/ell
 assert 0<=theta<1 and a0>=0 and a1>=0 and a0+a1==d
 rho=sum(abs(x)**3*t for x,t in xs);gamma=sum(x**3*t for x,t in xs)
 J=sum(sum(x*t for x,t in xs if x>=v)*(v-u)**2 for (u,wu),(v,wv)in zip(xs,xs[1:]))
 D=(3*rho-gamma-3*J,rho)
 Q=(6*p*p-4*p-1,2*p*p-2*p+1)
 Kp=(3*q-5*d,3*q-d);Km=(9*p-7*d,3*p-d)
 K=Kp if sign(add(Kp,scale(Km,-1)))<=0 else Km
 def rhs(k):return scale(add(add(scale(Q,w),(6*w*d*(1-d),F(0))),scale(k,theta)),ell*V)
 reserve=add(D,scale(rhs(K),-1));assert sign(reserve)>=0
 E0=6*m*((A+B)*(m/q-A+m/p-B)+(m/q-A)*(m/p-B))
 assert E0==6*ell*V*w*(d*(1-d)+a0*a1)
 # This deliberately false stronger formula assigns the dearer sign cost
 # to all noise. The control must reject it for at least one genuine law.
 Kbad=Km if K==Kp else Kp
 badreserve=add(D,scale(rhs(Kbad),-1))
 return dict(p=p,theta=theta,d=d,reserve=reserve,bad_reserve=badreserve,centered_law=xs)
controls=[]
for p in [F(1,4),F(2,5),F(1,2),F(3,5),F(3,4)]:
 controls.append(('Bernoulli '+str(p),[(-p,1-p),(1-p,p)]))
 for jump in [F(1,10),F(1,2),F(1),F(2),F(10)]:
  for eps in [F(1,10),F(1,100),F(1,10**6)]:
   U=[(-jump,eps),(eps*jump/(1-eps),1-eps)]
   controls.append((f'negative rare jump p={p} jump={jump} eps={eps}',[(-p+x,(1-p)*z)for x,z in U]+[(1-p,p)]))
   controls.append((f'positive rare jump p={p} jump={jump} eps={eps}',[(-p,1-p)]+[(1-p-x,p*z)for x,z in U]))
 for t in [F(1,1000),F(1,20),F(1,10)]:
  controls.append((f'four points p={p} t={t}',[(-p-t,(1-p)/2),(-p+t,(1-p)/2),(1-p-t,p/2),(1-p+t,p/2)]))
accepted=[];outside=[];bad=[]
for name,x in controls:
 try:r=law(x)
 except ValueError as e:outside.append({'name':name,'reason':str(e)});continue
 accepted.append(name)
 if sign(r['bad_reserve'])<0 and len(bad)<1:
  bad.append({'name':name,**r,'bad_reserve_enclosure':enclosure(r['bad_reserve'])})
assert len(accepted)>=160 and bad
try:law([(-F(1),F(1,4)),(F(0),F(1,2)),(F(1),F(1,4))])
except ValueError as e:zero_rejection=str(e)
else:raise AssertionError('zero-atom control failed')
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(tuple,list)):return[enc(a)for a in x]
 if isinstance(x,dict):return{k:enc(v)for k,v in x.items()}
 return x
print(json.dumps(enc({'status':'PASS_DIRECT_BUDGET_ACTUAL_LAW_CONTROLS','exact_field':'Q(sqrt(10)); variance normalization canceled algebraically','tested_laws':len(accepted),'cases':accepted,'outside_hypotheses':outside,'false_maximum_sign_cost_rejected':bad,'zero_atom_rejected':zero_rejection,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python':sys.version,'scope':'Adversarial identity/inequality controls, not a proof from sampling or a contact/first-failure claim.'}),indent=2))

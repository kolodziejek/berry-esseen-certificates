"""Exact acceptance for the anchor counterexample and first-moment curvature.
No normal-CDF numerical routine and no constructor imports are used.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,itertools,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
ROOT=Path(__file__).resolve().parents[3]
PINS={
'mathematics/simplification-v12/2026-10-28/comparison-union.tex':'31645628932501a0265959123b5d452b09116b77792fc2401c6a18eacdbb754a',
'mathematics/simplification-v11/2026-10-28/counts-v11.tex':'209f173c19a73c4fecf5aaf9aa2732c30b72266ff3f1673ddd52fa4a4e6c4641',
'mathematics/simplification-v14/2026-10-28/large-index.tex':'ad48f1eae57817b955016c6a12114e3929852a3e636afcfbb91646697b4c6509',
'mathematics/simplification-v13/2026-10-28/counts-tools.tex':'7e4defcb35a1711fc4104dec49aa03f91e04ef1529418398b1b3f1c1b957bb9b'}
for name,pin in PINS.items():
 if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=pin:raise RuntimeError('Audited source changed: '+name)
A=F(3,5);eps=F(1,350000);n=42;p=F(1,2);v=p*(1-p);theta=eps/(A+eps);h=21*eps;t=21-h
s=p*A*eps;V=v+s;lam=n*s
assert theta==F(1,210001) and lam==F(9,250000) and h==F(3,50000)
assert eps<F(9,125) and h*h/V<F(46,25)**2
assert t.__floor__()==20 and (t+F(34,125)).__floor__()==21
assert -F(34,125)<=t-21<=F(91,125)
assert F(162,25)**2<42<F(649,100)**2
# Machin plus alternating arctangent bounds implies pi>25/8, hence phi(0)<2/5.
assert 16*(F(1,5)-F(1,375))-F(4,239)>F(25,8)
assert 1-F(1,63)+F(1,4410)==F(1447,1470)
pi21=F(comb(n,21),2**n);w=A*eps;M3=F(1,8)+F(3,4)*w+F(1,2)*w*(A-eps)
assert 8*M3-1>0
counter=F(162,25)*pi21-F(649,100)*21*theta-F(4,5)*F(1447,1470)-(8*M3-1)
assert counter==F(185046727061827375519549,37666554485145600000000000)>F(1,250)
shifted_margin=F(162,25)*pi21/F(10001)-F(4,5)*h
assert shifted_margin>0
# Actual iid product probabilities, independently reconstructed from B and rare jumps.
actual=F(0);bernoulli=sum(F(comb(n,j),2**n) for j in range(22));collision=F(0)
for j in range(n+1):
 pi=F(comb(n,j),2**n)
 for r in range(j+1):
  x=j*(1-eps)+r*(A+eps)
  prob=pi*comb(j,r)*theta**r*(1-theta)**(j-r)
  if x<=t:actual+=prob
  if x==t:collision+=prob
assert collision>=pi21*(1-theta)**21>0
assert actual>=bernoulli-21*theta
assert actual<=bernoulli-pi21*(1-(1-theta)**21)
assert 1-(1-theta)**21>=F(1,10001)
# Genuine wrong-anchor control: both certified signs concern this same actual law.
assert counter>0 and shifted_margin>0

def conv(a,b):
 out={}
 for x,p in a.items():
  for y,q in b.items():out[x+y]=out.get(x+y,F(0))+p*q
 assert sum(out.values())==1
 return out
def powers(a,n):
 out=[{F(0):F(1)}]
 for _ in range(n):out.append(conv(out[-1],a))
 return out
def centered(a,b):
 if not a or not b:return {F(0):F(1)}
 return {-a:b/(a+b),b:a/(a+b)}
def E(law,f):return sum(pr*f(x) for x,pr in law.items())
zero={F(0):F(1)};e=F(3,125)
laws=[(centered(A,e),zero),(zero,centered(e,A)),(centered(A,e),centered(e,A)),(zero,zero),(zero,centered(F(1,350000),A))]
records=[];checks=0
for n,p,(U0,U1) in itertools.product([4,7,42],[F(2,5),F(1,2),F(53,100)],laws):
 q=1-p;v=p*q;v0=E(U0,lambda x:x*x);v1=E(U1,lambda x:x*x);s=q*v0+p*v1
 e0=E(U0,lambda x:max(x,0));e1=E(U1,lambda x:max(x,0));ell=q*e0+p*e1
 assert e0==E(U0,lambda x:max(-x,0)) and e1==E(U1,lambda x:max(-x,0))
 if U0==zero and len(U1)==2:
  inward=-min(U1);assert ell==s/(A+inward)
 if U1==zero and len(U0)==2:
  inward=max(U0);assert ell==s/(A+inward)
 p0,p1=powers(U0,n),powers(U1,n)
 Ws=[conv(p1[j],p0[n-j]) for j in range(n+1)]
 pi=[F(comb(n,j))*p**j*q**(n-j) for j in range(n+1)]
 pit=[F(comb(n+1,r))*p**r*q**(n+1-r) for r in range(n+2)]
 for off in [F(-2),F(-47,50),F(-1,2),F(0),F(1,2),F(47,50)]:
  t=n*p+off;c=max(F(0),n*p-q-t);Bs=[]
  for j in range(n+1):
   Bj=E(Ws[j],lambda x:max(t-j-x,0))-max(t-j,0)
   assert 0<=Bj<=E(Ws[j],lambda x:max(x,0))<=(n-j)*e0+j*e1
   assert max(t-j,0)*Bj<=((n-j)*v0+j*v1)/4
   Bs.append(Bj)
  correction=sum((pi[j+1]-pi[j])*Bs[j] for j in range(1,n))
  bound=s/(4*v)+c*ell/v
  assert correction<=bound
  assert sum(pit[j+1]*((n-j)*e0+j*e1) for j in range(1,n))<=(n+1)*ell
  checks+=1
 records.append({'n':n,'p':str(p),'lambda':str(n*s),'both_noisy':len(U0)>1 and len(U1)>1})
print(json.dumps({'status':'PASS_EXACT_ANCHOR_OBSTRUCTION_AND_CURVATURE','counterexample_delta_lower_for_all_C_in_0_1':str(counter),'shifted_anchor_negative_margin_for_all_C_ge_0':str(shifted_margin),'actual_counterexample_cdf':str(actual),'closed_collision_mass':str(collision),'lambda':str(lam),'floor_anchor':20,'retained_shifted_anchor':21,'audited_source_pins':PINS,'actual_curvature_laws':len(records),'actual_curvature_checks':checks,'records':records,'scope':'The floor-anchor extension is refuted, while all retained anchor domains remain consistent. The first-moment curvature lemma is analytically proved; finite actual-law tests are controls only.','python':sys.version},indent=2))

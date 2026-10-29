"""Exact algebra and actual-law controls for the paired reserve.

No constructor imports, floating acceptance, numerical search, or new grid.
The displayed universal algebra is separate from the finite actual-law controls.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,itertools,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
ROOT=Path(__file__).resolve().parents[3]
PINS={
 'mathematics/simplification-v13/2026-10-28/crossing.tex':'0dda285adb9aaa24277fdc1d74843c20bc6100b2a64a0cd5ae34bb696a68a6ec',
 'mathematics/simplification-v13/2026-10-28/counts-tools.tex':'7e4defcb35a1711fc4104dec49aa03f91e04ef1529418398b1b3f1c1b957bb9b'}
for path,expected in PINS.items():
 actual=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
 if actual!=expected:raise RuntimeError(f'Dependency bytes changed: {path}')
def conv(a,b):
 z={}
 for x,p in a.items():
  for y,q in b.items():z[x+y]=z.get(x+y,F(0))+p*q
 assert sum(z.values())==1
 return z
def powers(a,n):
 z=[{F(0):F(1)}]
 for _ in range(n):z.append(conv(z[-1],a))
 return z
def centered(a,b):
 if not a or not b:return {F(0):F(1)}
 return {-a:b/(a+b),b:a/(a+b)}
def expectation(law,fun):return sum(w*fun(x) for x,w in law.items())
def check_pair(laws,t,k):
 n=len(laws)-1;u=t-k
 L=[expectation(laws[j],lambda x:max(t-j-x,0)) for j in range(n+1)]
 C=[expectation(laws[j],lambda x:F(j+x<=t)) for j in range(n+1)]
 g=[L[j-1]-L[j]-C[j] for j in range(1,n+1)]
 assert all(x>=0 for x in g)
 own=expectation(laws[k],lambda x:F(x>u))
 outgoing=expectation(laws[k-1],lambda x:max(x-u-1,0))
 incoming=expectation(laws[k+1],lambda x:(u-x)*F(x<=u-1))
 assert g[k-1]+g[k]==u+own+outgoing-incoming
 return g,own,incoming,outgoing,C
# Universal rational gates corresponding to the printed proof.
gates={
 'k_integer_min':F(42)*F(2,5)>16,
 'm_integer_min':F(42)*F(47,100)>19,
 'density_cap_half_mass':F(289,81)>F(127,42),
 'support_eps':F(3,5)/17<F(9,125),
 'v_lower':min(F(2,5)*F(3,5),F(53,100)*F(47,100))==F(6,25),
 'cubic_sign':F(87,250)-F(13,16)*F(9,25)/42>0,
 'first_regime_reserve':1-F(2,5)-F(3,5)*F(2,5)**2==F(63,125)>F(2,15),
 'second_regime_two_jumps':F(3,5)*(2-F(2,5)*(1-F(3,20)))==F(249,250)<1,
 'factorial_derivative':6-3-F(1,20)==F(59,20)>0,
 'factorial_endpoint_polynomial':3+5*F(1,20)-4*F(1,20)**2>0,
 'positive_no_incoming':F(3,5)*(1+F(1,17))==F(54,85)<1,
 'negative_final':F(1,15)-F(1,16)==F(1,240)>0,
 'positive_final':1/(4*F(3,5)**2)-1/(4*F(6,25)*6)==F(25,48)>0,
}
assert all(gates.values())
# Check the symbolic endpoint factor and derivative polynomials at coefficient level.
# (1+h)^2-(1+2h)(1-h)(1-2h) = h(3+5h-4h^2),
# and 3+5h-4h^2>=3 for 0<=h<=1/20.
assert 5-4*F(1,20)>0
assert 1-F(4,20)>0
# Strict e<3 follows from j!>=2^(j-1), strict already at j=3.
assert 6>2**2
A=F(3,5);records=[];pair_checks=0;hinge_checks=0;collision_checks=0
for n,p,mu,kind in itertools.product([42,50], [F(1,2)], [F(1,10000),F(1,4),F(2,5),F(1)], [0,1]):
 k=int(n*p);m=n-k;eps=A*mu/(m if kind==0 else k)
 U0=centered(A,eps) if kind==0 else {F(0):F(1)}
 U1={F(0):F(1)} if kind==0 else centered(eps,A)
 p0,p1=powers(U0,n),powers(U1,n)
 laws=[conv(p1[j],p0[n-j]) for j in range(n+1)]
 pi=[F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(n+1)]
 v=p*(1-p);s=(1-p)*expectation(U0,lambda x:x*x)+p*expectation(U1,lambda x:x*x)
 lam=n*s;assert lam==A*A*mu
 assert min(pi[k],pi[k+1])**2*n>F(1,4)
 for u in [F(-1,5),F(0),F(2,5)]:
  t=k+u;g,own,Q,outgoing,C=check_pair(laws,t,k);pair_checks+=1
  assert sum(pi[i+1]*g[i] for i in range(n))>=min(pi[k],pi[k+1])*(u+own-Q)
  d=max(U0)-min(U1);zeta=1-d
  same=u+expectation(laws[k],lambda x:F(x>u)-(u-x+d)*F(x<=u-zeta))
  assert g[k-1]+g[k]>=same
  for y in [F(0),F(1,5)]:
   b=1-u
   if y>=b:continue
   for z in [-x for x in laws[k+1]]:
    assert (u+z)*F(z>=b)<=max(z-y,0)**2/(b-y)**2;hinge_checks+=1
  if u:continue
  reserve=own-Q
  assert reserve>F(2,15) if kind==0 else reserve>=mu/2
  actual=sum(pi[j]*C[j] for j in range(n+1));bernoulli=sum(pi[:k+1]);diff=actual-bernoulli
  assert diff<0
  goal=F(1,240) if kind==0 else F(25,48)*lam
  assert n*diff**2>goal**2
  marginal={}
  for x,w in U0.items():marginal[x-p]=marginal.get(x-p,F(0))+(1-p)*w
  for x,w in U1.items():marginal[1+x-p]=marginal.get(1+x-p,F(0))+p*w
  M3=expectation(marginal,lambda x:abs(x)**3)
  assert M3*M3*v>(1-2*v)**2*(v+s)**3
  records.append({'n':n,'p':str(p),'mu':str(mu),'lambda':str(lam),'kind':kind,'reserve':str(reserve),'cdf_difference':str(diff)})
# Additional skew cases at exact central integer anchors.
for n,p in [(42,F(3,7)),(50,F(2,5)),(100,F(53,100))]:
 for mu,kind in itertools.product([F(1,4),F(1)],[0,1]):
  k=int(n*p);m=n-k;eps=A*mu/(m if kind==0 else k)
  U0=centered(A,eps) if kind==0 else {F(0):F(1)}
  U1={F(0):F(1)} if kind==0 else centered(eps,A)
  p0,p1=powers(U0,n),powers(U1,n);laws=[conv(p1[j],p0[n-j]) for j in range(n+1)]
  pi=[F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(n+1)]
  g,own,Q,outgoing,C=check_pair(laws,F(k),k);pair_checks+=1
  reserve=own-Q;assert reserve>F(2,15) if kind==0 else reserve>=mu/2
  diff=sum(pi[j]*C[j] for j in range(n+1))-sum(pi[:k+1]);assert diff<0
  lam=A*A*mu;goal=F(1,240) if kind==0 else F(25,48)*lam
  assert n*diff**2>goal**2
  records.append({'n':n,'p':str(p),'mu':str(mu),'lambda':str(lam),'kind':kind,'reserve':str(reserve),'cdf_difference':str(diff)})
# General paired identity with both noisy conditionals and noiseless Bernoulli.
for U0,U1 in [(centered(A,F(1,50)),centered(F(3,100),A)),({F(0):F(1)},{F(0):F(1)})]:
 n=4;k=2;p0,p1=powers(U0,n),powers(U1,n)
 laws=[conv(p1[j],p0[n-j]) for j in range(n+1)]
 for u in [F(-1,4),F(0),F(3,125),F(1,2)]:
  g,own,Q,outgoing,C=check_pair(laws,k+u,k);pair_checks+=1
# Closed collision: excluding the incoming equality overstates the exact pair.
U0=centered(A,F(1,20));U1={F(0):F(1)};n=3;k=1;u=F(2,5);t=k+u
p0,p1=powers(U0,n),powers(U1,n);laws=[conv(p1[j],p0[n-j]) for j in range(n+1)]
g,own,Q,outgoing,C=check_pair(laws,t,k)
wrongQ=expectation(laws[k+1],lambda x:(u-x)*F(x<u-1))
assert Q-wrongQ==F(1,13)
assert u+own+outgoing-wrongQ>g[k-1]+g[k];collision_checks+=1
# An inadmissible negative physical hinge gives a false pointwise bound.
u=F(0);y=F(-2);z=F(2);b=1-u
assert (u+z)*F(z>=b)>max(z-y,0)**2/(b-y)**2
# An ordinary-tail probability cap is not a weighted-tail cap.
Z={F(-3):F(1,2),F(3):F(1,2)}
assert expectation(Z,lambda z:z*F(z>=1))==F(3,2)>1
# Full product checks of selected biases and half-open residual supports.
bias_checks=0;nonzero_bias=0
for n in [3,4]:
 U0=centered(A,F(3,125));U1=centered(F(3,125),A);a0=max(U0);a1=-min(U1);zeta=1-a0-a1
 for t in [F(n,2),F(n,2)+F(3,125),F(n,2)+F(1,4)]:
  EKnoise=F(0);Enextnoise=F(0)
  for sample in itertools.product(list(U0.items()),list(U1.items()),repeat=n):
   z0=[sample[2*i][0] for i in range(n)];z1=[sample[2*i+1][0] for i in range(n)]
   prob=F(1)
   for x,w in sample:prob*=w
   W=[sum(z1[:j])+sum(z0[j:]) for j in range(n+1)];T=[j+W[j] for j in range(n+1)]
   K=max(j for j in range(n) if T[j]<=t)
   assert T[K]<=t<T[K+1]
   R=[t-i-sum(z1[:i])-sum(z0[i+1:]) for i in range(n)]
   assert all(R[i]-R[i+1]>=zeta for i in range(n-1))
   assert sum(-A<=r<a0 for r in R)<=1
   assert sum(1-a1<=r<1+A for r in R)<=1
   EKnoise+=prob*W[K];Enextnoise+=prob*W[K+1]
  assert 0<=Enextnoise<=expectation(U0,lambda x:max(x,0))<=a0
  assert 0<=-EKnoise<=expectation(U1,lambda x:max(-x,0))<=a1
  bias_checks+=1;nonzero_bias+=int(EKnoise!=0 or Enextnoise!=0)
print(json.dumps({'status':'PASS_PAIRED_ANALYTIC_CONTROLS','universal_gates':len(gates)+3,'actual_family_cases':len(records),'pair_identity_checks':pair_checks,'hinge_point_checks':hinge_checks,'closed_collision_checks':collision_checks,'full_product_bias_checks':bias_checks,'nonzero_bias_checks':nonzero_bias,'dependency_pins':PINS,'negative_controls':{'open_incoming_event_overstates_pair_by':'1/13','inadmissible_hinge':'2 > 16/9','weighted_tail_clipping':'3/2 > 1'},'scope':'The uniform theorem is established by the displayed analytic proof and rational gates. Actual-law controls are finite adversarial checks, not a general parameter cover.','records':records,'python':sys.version},indent=2))

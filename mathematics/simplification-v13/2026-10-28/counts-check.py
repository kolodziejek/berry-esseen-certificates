"""Exact controls for the structural count tools; no constructor imports."""
from fractions import Fraction as F
from math import comb
import json,itertools,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
def conv(a,b):
 out={}
 for x,p in a.items():
  for y,q in b.items():out[x+y]=out.get(x+y,F(0))+p*q
 assert sum(out.values())==1
 return out
def centered(a,b):
 if not a or not b:return {F(0):F(1)}
 return {-a:b/(a+b),b:a/(a+b)}
def powers(law,n):
 z=[{F(0):F(1)}]
 for j in range(n):z.append(conv(z[-1],law))
 return z
def maximum_window(law,width):
 items=sorted(law.items());j=0;total=F(0);best=F(0)
 for i,(x,p) in enumerate(items):
  while j<len(items) and items[j][0]<=x+width:total+=items[j][1];j+=1
  best=max(best,total);total-=p
 return best
A=F(3,5);a=F(3,125)
u0=centered(A,a);u1=centered(a,A)
laws=[(u0,u1),(centered(A,F(1,25)),{F(0):F(1)}),({F(0):F(1)},centered(F(1,25),A)),({F(0):F(1)},{F(0):F(1)})]
records=[];curvature_checks=0;concentration_checks=0;symmetry_checks=0
for n,li,p in itertools.product([2,4,7,42],range(4),[F(2,5),F(1,2)]):
 U0,U1=laws[li];p0,p1=powers(U0,n),powers(U1,n)
 a0=max(U0);a1=-min(U1);zeta=1-a0-a1
 v0=sum(x*x*w for x,w in U0.items());v1=sum(x*x*w for x,w in U1.items());s=(1-p)*v0+p*v1;v=p*(1-p)
 pi=[F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(n+1)]
 pin=[F(comb(n+1,j))*p**j*(1-p)**(n+1-j) for j in range(n+2)]
 conditional=[{j+x:w for x,w in conv(p1[j],p0[n-j]).items()} for j in range(n+1)]
 actual={}
 for j,law in enumerate(conditional):
  for x,w in law.items():actual[x]=actual.get(x,F(0))+pi[j]*w
 assert sum(actual.values())==1
 for m,width in [(1,F(0)),(1,zeta/2),(2,3*zeta/2)]:
  bound=max(sum(pi[j:j+m]) for j in range(n+2-m))
  maximum=maximum_window(actual,width)
  assert maximum<=bound;concentration_checks+=1
 for off in [F(-9,10),F(-1,10),F(0),F(3,10),F(9,10)]:
  t=n*p+off;c=max(F(0),n*p-(1-p)-t)
  bend=[]
  for j in range(n+1):
   B=sum(max(t-x,0)*w for x,w in conditional[j].items())-max(t-j,0)
   assert B>=0;bend.append(B)
   tj=(n-j)*v0+j*v1
   assert 4*B*B<=tj
   if t>j:assert 4*(t-j)*B<=tj
  correction=sum((pi[j+1]-pi[j])*bend[j] for j in range(1,n))
  for j in range(n):assert pi[j+1]-pi[j]==((n+1)*p-j-1)*pin[j+1]/((n+1)*v)
  V=sum(pin[j+1]*((n-j)*v0+j*v1) for j in range(1,n))
  assert V<=(n+1)*s
  residual=correction-s/(4*v)
  if residual>0:assert (2*v*residual)**2<=c*c*s/(n+1)
  curvature_checks+=1
 if p==F(1,2) and li==0 and n%2==0:
  assert all(actual.get(n-x,F(0))==w for x,w in actual.items())
  atom=actual.get(F(n,2),F(0));assert atom<=pi[n//2]
  marginal={}
  for x,w in U0.items():marginal[x-p]=marginal.get(x-p,F(0))+w/2
  for x,w in U1.items():marginal[1+x-p]=marginal.get(1+x-p,F(0))+w/2
  V=sum(x*x*w for x,w in marginal.items());M3=sum(abs(x)**3*w for x,w in marginal.items())
  assert M3*M3>V**3;symmetry_checks+=1
 records.append({'n':n,'law':li,'p':str(p),'lambda':str(n*s)})
# A four-moment relaxation cannot prove a positive selected stop-loss reserve.
Z={F(-6,5):F(25,144),F(0):F(47,72),F(6,5):F(25,144)}
assert sum(Z.values())==1
mom={j:sum(x**j*w for x,w in Z.items()) for j in range(1,5)}
assert mom[1]==mom[3]==0 and mom[2]==F(1,2) and mom[4]==F(18,25)
assert mom[4]<=A*A*mom[2]+3*mom[2]**2
stoploss=sum((F(x>0)-max(x,0))*w for x,w in Z.items())
assert stoploss==F(-5,144)
# At the boundary length=zeta, closed windows can contain two mesh points.
bin2={F(j):F(comb(2,j),4) for j in range(3)}
assert maximum_window(bin2,F(1))==F(3,4)>max(bin2.values())
# A comonotone coupling does not make the initial noise independent of increments.
pairs=[(-A,-a,F(1,26)),(a,-a,F(12,13)),(a,A,F(1,26))]
assert sum(w*x for x,y,w in pairs)==sum(w*y for x,y,w in pairs)==0
cov=sum(w*x*(1+y-x) for x,y,w in pairs)
assert cov==F(-216,15625)
assert 42*A*a==F(378,625)<F(77,125)
print(json.dumps({'status':'PASS_STRUCTURAL_COUNT_CONTROLS','actual_law_cases':len(records),'curvature_checks':curvature_checks,'concentration_checks':concentration_checks,'symmetric_center_checks':symmetry_checks,'four_moment_obstruction':str(stoploss),'correlated_initial_increment_covariance':str(cov),'closed_window_boundary_counterexample':'3/4 > 1/2','records':records,'scope':'Exact finite controls of proved structural lemmas, not full larger-noise Berry-Esseen acceptance. The four-moment obstruction is not claimed to be an iid sum.','python':sys.version},indent=2))

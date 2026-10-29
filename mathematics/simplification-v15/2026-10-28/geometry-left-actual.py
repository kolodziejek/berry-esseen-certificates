"""Bounded actual-law controls for the left signed comparison.

No search or acceptance grid. Four named three-atom iid laws, three exact
threshold events per law, and small product controls for the smooth-kernel
replacement. These checks supplement, and do not replace, the analytic proof.
"""
from fractions import Fraction as F
from math import comb,factorial,gcd,lcm
from functools import lru_cache
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
here=Path(__file__).resolve();repo=here.parents[3]
helper=repo/'mathematics/simplification-v10/2026-10-28/actual_law_checks.py'
HELPER_SHA='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
assert hashlib.sha256(helper.read_bytes()).hexdigest()==HELPER_SHA
# Only the displayed rational normal/interval helpers are reused; no main or
# discovery function is run. This is disclosed, not called independent code.
namespace={'__name__':'pinned_interval_helper'}
exec(compile(helper.read_text(),str(helper),'exec'),namespace)
I,add,sub,mul,div,root,Phi,CE,PI=[namespace[x] for x in ['I','add','sub','mul','div','root','Phi_interval','CE','PI']]

def centered(neg,pos):
 neg,pos=F(neg),F(pos)
 assert neg>0 and pos>0
 return [(-neg,pos/(neg+pos)),(pos,neg/(neg+pos))]
ZERO=[(F(0),F(1))]
def moment(law,r):return sum((w*x**r for x,w in law),F(0))
def convolution(a,b):
 out={}
 for x,wx in a:
  for y,wy in b:out[x+y]=out.get(x+y,F(0))+wx*wy
 return sorted(out.items())
def power(a,n):
 out=ZERO
 for _ in range(n):out=convolution(out,a)
 return out

def h(x,U0,U1):
 return (sum((w*max(x-z,0) for z,w in U0),F(0))
         -sum((w*max(x-1-z,0) for z,w in U1),F(0))
         -sum((w for z,w in U1 if 1+z<=x),F(0)))
@lru_cache(maxsize=None)
def bump(x):
 if x<=0 or x>=1:return I(0)
 r=min(x,1-x);z=2*PI[0]*r
 # Taylor polynomial degree48; next nonzero term bounds the remainder,
 # plus a Lipschitz enclosure for replacing pi by its lower bound.
 c=sum(((-1)**j*z**(2*j)/factorial(2*j) for j in range(25)),F(0))
 error=z**50/factorial(50)+2*r*(PI[1]-PI[0])
 return max(F(0),(1-c-error)/2),min(F(1),(1-c+error)/2)
def EB(u,j,law):
 out=I(0)
 for x,w in law:out=add(out,mul(I(w),bump(u-j-x)))
 return out

def kernel_controls():
 eps=F(1,10**12);A=F(7,10);d=F(17,250)
 designs=[('left_inward_endpoint',centered(A,d),ZERO),
  ('right_inward_endpoint',ZERO,centered(d,A)),
  ('split_inward',centered(A,d/2),centered(d/2,A)),
  ('tiny_symmetric',centered(eps,eps),centered(eps,eps))]
 rows=[];swap_rows=[];collision=0
 for name,U0,U1 in designs:
  a1=max(-x for x,w in U1)
  xs=set([F(0),F(1,4),F(2,5),F(1,2),1-a1,1-a1-eps,1-a1+eps,F(1),1-eps,1+eps])
  for x in sorted(xs):
   hv=h(x,U0,U1);bi=bump(x)
   assert hv>=F(2,5)*bi[1],(name,x,hv,bi)
   if any(1+y==x for y,w in U1):collision+=1
   rows.append({'design':name,'x':str(x),'margin_lower':str(hv-F(2,5)*bi[1])})
  n=7;k=3;s0=moment(U0,2);s1=moment(U1,2)
  laws={j:convolution(power(U1,k+j),power(U0,n-k-j-1)) for j in range(-2,3)}
  for u in [F(0),F(1,2),1-eps]:
   actual=I(0);frozen=I(0)
   for j in range(-2,3):
    actual=add(actual,EB(u,j,laws[j]));frozen=add(frozen,EB(u,j,laws[0]))
   cost=4*PI[1]**2*(s0+s1)
   assert actual[0]-frozen[1]+cost>=0,(name,u)
   swap_rows.append({'design':name,'n':n,'k':k,'u':str(u),
       'centered_replacement_margin_lower':str(actual[0]-frozen[1]+cost)})
 return rows,swap_rows,collision

# Streaming exact trinomial CDF: each row is one binomial allocation.
# All operations below are integer operations after a common-denominator
# conversion; no event mass is rounded or replaced by a count relaxation.
def stream_cdf(atoms,n,t):
 assert len(atoms)==3
 atoms=sorted(atoms);C=lcm(*(x.denominator for x,w in atoms),t.denominator)
 D=lcm(*(w.denominator for x,w in atoms))
 z=[int(x*C) for x,w in atoms];w=[int(a*D) for x,a in atoms]
 assert sum(w)==D and min(w)>0 and z[0]<z[1]<z[2]
 target=int(t*C);gap=z[1]-z[0]
 powers=[[a**r for r in range(n+1)] for a in w]
 cdf=jump=0;rows=0
 for j in range(n+1):
  m=n-j;base=j*z[2]+m*z[1];diff=base-target
  hmin=-((-diff)//gap)
  if hmin<=0:tail=(w[0]+w[1])**m
  elif hmin>m:tail=0
  else:
   tail=0;term=powers[1][m]
   for h0 in range(m+1):
    if h0>=hmin:tail+=term
    if h0<m:
     num=term*(m-h0)*w[0];den=(h0+1)*w[1]
     term,rem=divmod(num,den);assert rem==0
  factor=comb(n,j)*powers[2][j];cdf+=factor*tail
  if diff%gap==0:
   h0=diff//gap
   if 0<=h0<=m:
    jump+=factor*comb(m,h0)*powers[0][h0]*powers[1][m-h0]
  rows+=1
 assert 0<=jump<=cdf<=D**n
 return F(cdf,D**n),F(jump,D**n),C,rows

def direct_cdf(atoms,n,t):
 dist=power(atoms,n)
 return (sum((w for x,w in dist if x<=t),F(0)),
         sum((w for x,w in dist if x==t),F(0)))

def full_event_controls():
 n=700;A=F(7,10);rows=[];event_total=0;stream_rows=0
 # Test independent streaming code on every atom and inter-atom location of
 # a tiny actual trinomial convolution before the four n700 controls.
 smoke_atoms=[(F(-2,5),F(1,7)),(F(1,11),F(3,7)),(F(6,5),F(3,7))]
 smoke=0
 for nn in [1,2,3]:
  dist=power(smoke_atoms,nn);xs=[x for x,w in dist]
  for t in xs+[(a+b)/2 for a,b in zip(xs,xs[1:])]:
   assert stream_cdf(smoke_atoms,nn,t)[:2]==direct_cdf(smoke_atoms,nn,t)
   smoke+=1
 for p,lam,side in [(F(1,3),F(1,100),0),(F(2,5),F(1,100),1),
                    (F(1,3),F(8,25),1),(F(2,5),F(8,25),0)]:
  q=1-p;v=p*q;s=lam/n;conditional_var=s/(q if side==0 else p)
  inward=conditional_var/A;assert inward<=F(17,250)
  noises=[ZERO,ZERO];noises[side]=centered(A,inward) if side==0 else centered(inward,A)
  atoms=[(u,q*w) for u,w in noises[0]]+[(1+u,p*w) for u,w in noises[1]]
  assert sum(w for x,w in atoms)==1 and moment(atoms,1)==p
  V=sum((w*(x-p)**2 for x,w in atoms),F(0));M=sum((w*abs(x-p)**3 for x,w in atoms),F(0))
  assert V==v+s and M*M*v>=(1-2*v)**2*V**3
  k=(n*p+F(1,2)).numerator//(n*p+F(1,2)).denominator
  common=[max(noise,key=lambda a:a[1])[0] for noise in noises]
  t=k+(n-k)*common[0]+k*common[1]
  eps=F(1,10**20)
  assert (abs(t-n*p)+eps)**2<=F(46,25)**2*V
  cdf,jump,C,count=stream_cdf(atoms,n,t);stream_rows+=count
  assert jump>0 and eps*C<1
  # Every sum lies in (1/C)Z: there are no additional atoms between these
  # exact neighbors. At t itself the event includes its jump.
  rho=div(I(M),mul(I(V),root(V)));events=[]
  for offset,c in [(-eps,cdf-jump),(F(0),cdf),(eps,cdf)]:
   tt=t+offset
   normal=Phi(div(I(tt-n*p),root(n*V)))
   excess=sub(mul(root(F(n)),sub(I(c),normal)),mul(CE,rho))
   assert excess[1]<-lam/100,(p,lam,side,offset,float(excess[1]))
   events.append({'offset':str(offset),'excess_interval':[str(z) for z in excess],
     'margin_lower':str(-lam/100-excess[1])})
   event_total+=1
  # Large exact numerators stay reproducible in the code; a hash and size
  # bind them without inflating this finite-control log by several MB.
  def fingerprint(x):
   raw=str(x).encode()
   return {'sha256':hashlib.sha256(raw).hexdigest(),'numerator_bits':x.numerator.bit_length(),
           'denominator_bits':x.denominator.bit_length()}
  rows.append({'n':n,'p':str(p),'lambda':str(lam),'noise_side':side,
    'inward':str(inward),'raw_threshold':str(t),'raw_H_squared':str((t-n*p)**2/V),
    'exact_cdf':fingerprint(cdf),'positive_atom_jump':fingerprint(jump),
    'event_checks':events})
 return rows,event_total,smoke,stream_rows

def negative_curvature_control():
 n=42;p=F(7,20);v=p*(1-p);t=F(14);eps=F(1,10**6)
 law=centered(eps,eps);W=power(law,n)
 bend=sum((w*abs(x)/2 for x,w in W),F(0))
 def mass(j):return F(comb(n,j))*p**j*(1-p)**(n-j)
 # All other bends vanish: every |W_j|<=n*eps<1 and every other t-j
 # is a nonzero integer. Thus this is the full signed curvature exactly.
 curvature=(mass(15)-mass(14))*bend
 lam=n*eps*eps;T=F(5,3)*lam;M=F(49,100)*T+3*T*T;c=n*p-(1-p)-t
 assert c>0 and curvature>0
 false_bound=F(41,100)/(n*F(13,125))*(T/4+F(27,256)*M*(F(5,3)+F(5,4)*c))
 assert root(F(n))[0]*curvature>false_bound
 return {'n':n,'p':str(p),'lambda':str(lam),'c':str(c),
  'false_omission':'delete the c*sqrt(T) term from the curvature bound',
  'contradiction_margin_lower':str(root(F(n))[0]*curvature-false_bound),
  'scope':'Internal curvature lemma; n42 is outside the n700 theorem.'}

kernel,swaps,collisions=kernel_controls()
actual,event_total,smoke,stream_rows=full_event_controls()
negative=negative_curvature_control()
proof=here.with_name('geometry-left.tex')
print(json.dumps({'status':'PASS_SELECTED_ACTUAL_LEFT_LAWS','kernel_checks':len(kernel),
 'kernel_atom_collisions':collisions,'four_swap_product_checks':len(swaps),
 'independent_trinomial_smoke_checks':smoke,'full_iid_laws':len(actual),
 'full_signed_event_checks':event_total,'streamed_outer_rows':stream_rows,
 'kernel_rows':kernel,'swap_rows':swaps,'actual_laws':actual,
 'negative_control':negative,'normal_helper_sha256':HELPER_SHA,
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),'python':sys.version,
 'scope':'Selected exact actual-law controls, not a proof of the continuum. Main scalar proof separately establishes all-p/all-phase/all-noise coverage. Normal interval helpers are reused with disclosed source pin.'},indent=2))

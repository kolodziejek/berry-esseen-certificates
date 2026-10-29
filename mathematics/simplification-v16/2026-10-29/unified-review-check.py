"""Independent scalar reconstruction and product checks; no constructor import."""
from fractions import Fraction as F
from math import isqrt,comb
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
ROOT=Path(__file__).resolve().parents[3]
CONSTRUCTOR=ROOT.parent/'unified-v16'
if len(sys.argv)>1:CONSTRUCTOR=Path(sys.argv[1]).resolve()
SOURCE=CONSTRUCTOR/'mathematics/simplification-v16/2026-10-29'
PIN='2be0dc58973a281accb66cf3c8dffd7209592e68278ef4c0c46805708e374938'
assert hashlib.sha256((SOURCE/'unified-comparison.tex').read_bytes()).hexdigest()==PIN
checks={}
def ck(name,truth):
 assert name not in checks and truth,name;checks[name]=True
# Different reconstruction: evaluate the displayed functions at integers,
# solve their exact interpolation systems, then inspect derivatives.
def interpolate(values):
 n=len(values);a=[[F(i)**j for j in range(n)]+[v]for i,v in enumerate(values)]
 for j in range(n):
  z=next(i for i in range(j,n)if a[i][j]);a[j],a[z]=a[z],a[j]
  t=a[j][j];a[j]=[x/t for x in a[j]]
  for i in range(n):
   if i!=j:
    t=a[i][j];a[i]=[x-t*y for x,y in zip(a[i],a[j])]
 return [a[i][-1]for i in range(n)]
def ev(a,x):return sum((v*x**i for i,v in enumerate(a)),F(0))
def derivative(a):return [i*a[i]for i in range(1,len(a))]
# Parameters copied from the mathematical statement, not from its checker.
rows=[('compact',700,F(3,8),F(93,200),F(3,5),F(1,250),F(1,100),F(7,20),F(3),F(93,100),F(6),F(23,100),F(3,4),F(113,1000),F(79,200),F(1,5),F(5,2)),
 ('right',200,F(2,5),F(53,100),F(3,5),F(9,125),F(3,100),F(9,25),F(3),F(231,250),F(5),F(23,100),F(13,20),F(117,1000),F(23,50),F(9,40),F(5,2)),
 ('left',700,F(1,3),F(2,5),F(7,10),F(17,250),F(1,100),F(8,25),F(7,5),F(23,25),F(6),F(11,50),F(3,4),F(13,125),F(8,25),F(13,200),F(250,39))]
records={};pi=F(22,7);phi=F(2,5);beta=F(41,100)
for name,N,l,h,A,d,low,high,kap,xi,cm,zeta,mass,V,c,j0,j1 in rows:
 def gate(label,t):ck(name+':'+label,t)
 r=min(l,1-h);q=1-h;v0=min(l*(1-l),h*(1-h));v1=F(1,4)if l<=F(1,2)<=h else max(l*(1-l),h*(1-h))
 gate('legal_probability_noise',F(1,3)<=l<=h<=F(2,3)and 0<low<=high)
 gate('separation',0<=d<=A and d<r and A+d<1)
 gate('high_kernel',F(2,5)*pi*pi*d<=(1-A-d)/(A+d))
 gate('phase',F(46,25)**2*(v1+high/N)<xi*xi and 0<xi<1)
 gate('mesh',N*(r-d)>xi and N*r>4)
 gate('frozen_variance',cm*r>=1+xi and 0<cm<N)
 gate('window',0<zeta<min(t*(1-t)for t in [l-F(4,N),h+F(4,N)]))
 gate('five_weights',0<mass<2*F(199,500)*(1-(8+F(1,12))/(N*zeta)))
 gate('variance_power',0<V*V<v0**3)
 gate('curvature_offset',max(0,xi-q)<=c<1)
 gate('sqrt_tangent',j0>0 and j1>0 and 4*j0*j1>=1/q)
 gate('cubic',3*r-d-F(3,2)*(1-2*v0)-3*(1-2*v0)*high/(8*v0*N)>0)
 diameter=A+d
 if kap==3:
  gate('cosine_seed',F(17,20)**2<F(3,4))
  gate('cosine_chord',2*(F(17,20)/F(2,3))**2>kap)
  if diameter>F(2,3):gate('cosine_end',2*(F(17,20)-pi*(diameter-F(2,3)))**2>kap*diameter**2)
 else:
  gate('cosine_seed',F(7,10)**2<F(1,2));gate('cosine_chord',2*F(14,15)**2>kap)
  gate('cosine_end',2*(F(7,10)-pi*(diameter-F(3,4)))**2>kap*diameter**2)
 alpha=1-cm/N;b=1+F(3,N);z=kap*alpha
 def W(x):
  t=z*x
  return F(2,5)*mass*((t-t*t/2+t**3/6-t**4/24)/2-(A*A*b*x+3*b*b*x*x)/16-4*pi*pi*x/(N*r))
 def error(x,cc,positive):
  T=x/q;M=A*A*T+3*T*T
  S=T/4+cc*(j0+j1*x)+F(27,256)*M*(F(5,3)+F(5,4)*cc)
  normal=F(2,27)+(xi*x/2 if positive else xi/8)
  return (beta*S+phi*normal)/V
 wc=interpolate([W(F(i))for i in range(5)])
 ec=[interpolate([error(F(i),cc,pos)for i in range(3)])for cc,pos in [(c,False),(F(0),True)]]
 # Both sides are quadratic polynomials, so three distinct exact equalities
 # prove their identity after interpolation, not sampled positivity.
 wd=derivative(derivative(wc))
 for x in [F(-1),F(0),F(1)]:gate('completed_square_at_'+str(x),ev(wd,x)==-F(2,5)*mass*(z*z*((z*x-1)**2+1)/4+3*b*b/8))
 endpoints=[];polys=[]
 for j,e in enumerate(ec):
  gate('convex_nonnegative_error_'+str(j),all(x>=0 for x in e)and e[2]>0)
  P=interpolate([W(F(i))-error(F(i),c if j==0 else F(0),j==1)/N-F(i,100)for i in range(5)])
  for x in [low,high]:
   gate('endpoint_'+str(j)+'_'+str(x),ev(P,x)>0);endpoints.append(str(ev(P,x)))
  polys.append([str(x)for x in P])
 records[name]={'interpolated_W':[str(x)for x in wc],'interpolated_errors':[[str(x)for x in e]for e in ec],'interpolated_comparison_polynomials':polys,'exact_endpoints':endpoints}
ck('quartic_stoploss_identity', [256,-256,0,0,27]==[256,(-24)*16+16*8,9*16-24*8+16*3,9*8-24*3,9*3])
ck('full_square_tail',sum(F(1,i*i)for i in range(1,6))+F(1,5)<F(5,3))
ck('full_cube_tail_integral',1+F(1,8)+F(1,8)==F(5,4))
ck('mode_ratio',1-F(1,43)-F(2,43**2)>F(39,40))
ck('mode_constant',F(2,5)**2*F(40,39)*F(516,515)**2<F(41,100)**2)
# Whole acquired open domain lies in the common closed row; noise zero and
# positive noise <=.01 remain a separate theorem, not accepted by this proof.
ck('acquisition_p_join',F(3,8)==rows[0][2]and F(93,200)==rows[0][3])
ck('acquisition_support_noise_join',rows[0][4:8]==(F(3,5),F(1,250),F(1,100),F(7,20)))
ck('acquisition_rawH_join',F('1.83605680')<F(46,25))

# Independent small exact product-law implementation of the full weighted
# identity, with conditional convolution and actual iid mixture computed twice.
def conv(x,y):
 out={}
 for a,wa in x:
  for b,wb in y:out[a+b]=out.get(a+b,F(0))+wa*wb
 return sorted(out.items())
def power(x,n):
 out=[(F(0),F(1))]
 for _ in range(n):out=conv(out,x)
 return out
def noise(a,b):return [(-a,b/(a+b)),(b,a/(a+b))]
def stop(law,t):return sum((w*max(t-x,0)for x,w in law),F(0))
def cdf(law,t):return sum((w for x,w in law if x<=t),F(0))
def root(x):
 S=10**30;k=isqrt(x.numerator*S*S//x.denominator);return F(k,S),F(k+1,S)
zero=[(F(0),F(1))];eps=F(1,10**12)
designs=[(zero,noise(F(1,250),F(3,5))),(noise(F(3,5),F(1,250)),zero),
 (noise(F(1,1000),F(1,1000)),noise(F(1,1000),F(1,1000))),
 (noise(F(3,5),F(1,1000)),noise(F(3,1000),F(3,5)))]
identities=0;curvatures=0;collisions=0;strict_wrong_found=False
for n in [3,5]:
 for p in [F(3,8),F(93,200)]:
  q=1-p;v=p*q;pii=[F(comb(n,j))*p**j*q**(n-j)for j in range(n+1)]
  for U0,U1 in designs:
   atoms=[(u,q*w)for u,w in U0]+[(1+u,p*w)for u,w in U1]
   full=power(atoms,n)
   W=[conv(power(U1,j),power(U0,n-j))for j in range(n+1)]
   VV=[conv(power(U1,i-1),power(U0,n-i))for i in range(1,n+1)]
   atom=min((x for x,w in full),key=lambda x:abs(x-n*p))
   for t in [atom-eps,atom,atom+eps,n*p-F(4,5)]:
    a0=max(x for x,w in U0);a1=max(-x for x,w in U1)
    assert n*a0<=t<n*(1-a1)
    k=t.numerator//t.denominator;u=t-k
    g=[]
    for i,VV_i in enumerate(VV,1):
     value=F(0)
     for z,wz in VV_i:
      x=t-i+1-z
      value+=wz*(stop(U0,x)-stop([(1+y,w)for y,w in U1],x)-cdf([(1+y,w)for y,w in U1],x))
     assert value>=0
     direct=stop(W[i-1],t-i+1)-stop(W[i],t-i)-cdf(W[i],t-i)
     assert value==direct;g.append(value)
    bends=[stop(W[j],t-j)-max(t-j,0)for j in range(n+1)]
    curvature=sum((pii[j+1]-pii[j])*bends[j]for j in range(1,n))
    rhs=(1-u)*sum(pii[:k+1])+u*sum(pii[:k+2])+curvature-sum(pii[i]*g[i-1]for i in range(1,n+1))
    actual=cdf(full,t);mixture=sum(pii[j]*cdf(W[j],t-j)for j in range(n+1))
    assert rhs==actual==mixture;identities+=1
    jump=sum((w for x,w in full if x==t),F(0))
    collisions+=jump>0
    if jump>0:strict_wrong_found=actual-jump!=rhs
    increasing=[j for j in range(1,n)if pii[j+1]>pii[j]]
    T=max([sum(w*x*x for x,w in W[j])for j in increasing]+[F(0)])
    M=max([sum(w*x**4 for x,w in W[j])for j in increasing]+[F(0)])
    c=max(n*p-q-t,0);assert c<1
    # beta=2 is a valid crude mode coefficient at these tiny indices.
    assert (n+1)*v<4
    bound=F(2,n)/(v*root(v)[1])*(T/4+c*root(T)[0]+F(27,256)*M*(F(5,3)+F(5,4)*c))
    assert root(F(n))[1]*max(curvature,0)<=bound
    curvatures+=1
ck('closed_event_negative_control',strict_wrong_found)
# Removing q from the increasing-side variance budget is false at j=0.
ck('variance_denominator_negative_control',F(1,100)/(1-F(3,8))>F(1,100))
# A left-of-domain law refutes an unrestricted favorable cubic assertion.
p=F(13,50);v=p*(1-p);s=(1-p)*F(1,1000)**2
M=v*(1-2*v)+3*p*s
ck('cubic_domain_negative_control',M*M*v<(1-2*v)**2*(v+s)**3)
ck('frozen_count_negative_control',4*F(1,1000)**2!=5*F(1,1000)**2)
print(json.dumps({'status':'PASS_INDEPENDENT_UNIFIED_REVIEW','checks':len(checks),'rows':records,
 'full_weighted_identity_controls':identities,'full_curvature_controls':curvatures,
 'exact_atom_cases':collisions,'reviewed_proof_sha256':PIN,
 'constructor_bytes':{f:hashlib.sha256((SOURCE/f).read_bytes()).hexdigest()for f in ['unified-comparison.tex','unified-check.py','unified-actual.py']},
 'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python':sys.version,
 'scope':'Independent analytic/scalar review of generic local criterion and Compact acquisition join. No small-noise proof, acquisition theorem re-review, or unconditional cutoff accepted here.'},indent=2))

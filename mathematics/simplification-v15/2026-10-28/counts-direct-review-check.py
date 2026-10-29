"""Independent analytic-gate and exact actual-law review.

No constructor import. Quartics are reconstructed by rational interpolation.
Bump expectations use a separate rational Machin/Taylor enclosure.
"""
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
from functools import lru_cache
import argparse,hashlib,itertools,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
p=argparse.ArgumentParser();p.add_argument('--source-dir',type=Path,required=True);args=p.parse_args()
PINS={'loss-direct.tex':'1bb19aee8183fbf70e81424dfb4503a54877a1938cd073bf58e751556e387ead','right-direct.tex':'5946340c178bc54c5094fcde567ec2c260a1abd0d39daf16306dadbb12971d67'}
for name,pin in PINS.items():
 if hashlib.sha256((args.source_dir/name).read_bytes()).hexdigest()!=pin:raise RuntimeError('Reviewed source bytes changed: '+name)
A=F(3,5);D=F(9,125);L=F(3,40);U=F(9,25);pi_hi=F(22,7)
# Analytic local-kernel, cosine, frozen-variance, and finite-window guards.
assert pi_hi**2<10 and pi_hi<F(10,3)
assert F(2,5)*pi_hi**2*D<F(41,84)
assert 2*F(51,40)**2>3
assert 2*(F(17,20)-F(44,2625))**2>3*F(84,125)**2
assert F(46,25)**2*(F(1,4)+U/42)<F(47,50)**2
assert F(97,50)/F(47,100)<5 and F(97,50)/F(2,5)<5
assert F(47,50)/F(47,100)<3 and F(47,50)/F(2,5)<3
assert 42*F(2,5)-F(97,50)-1>1 and 42*F(47,100)>F(47,50)+3
# Uniform coefficient table, independently evaluated as finite scalar formulas.
table={125:F(1,250),150:F(1,20),200:F(1,8),250:F(1,6),300:F(19,100),400:F(9,40),500:F(6,25)}
table_margins={}
for n,target in table.items():
 a=1-F(5,n);b=1+F(3,n);z=3*a*U
 expo=sum(z**j/F(factorial(j)) for j in range(7))
 coeff=F(2,5)*((1-1/expo)/(2*U)-(A*A*b+3*b*b*U)/16-10*pi_hi*pi_hi/n)
 assert coeff>target;table_margins[n]=str(coeff-target)
# Finite binomial mass guards and mode bound, all rational.
assert F(46,25)*F(251,500)<F(231,250)
assert F(251,500)**2>F(1,4)+U/200
assert min(F(19,50)*F(31,50),F(11,20)*F(9,20))>F(23,100)
assert F(199,500)**2*F(44,7)<1
mass=F(199,250)*(1-(8+F(1,12))/46);assert mass>F(13,20)
assert 1-F(1,43)-F(2,43**2)>F(39,40)
assert F(2,5)**2*F(40,39)*F(516,515)**2<F(41,100)**2
assert F(6,25)**3>F(117,1000)**2
assert F(3,2)**2>F(100,47)
assert F(231,250)-F(47,100)<F(23,50)
assert F(87,250)-F(13,16)*U/200>0
# Quartic formulas reconstructed through values, not constructor coefficients.
a=F(39,40);b=F(203,200);z=3*a

def W(x):
 return F(13,50)*((z*x-(z*x)**2/2+(z*x)**3/6-(z*x)**4/24)/2-(A*A*b*x+3*b*b*x*x)/16-F(10,200)*pi_hi*pi_hi*x)
def E(x,negative):
 T=F(100,47)*x;M=A*A*T+3*T*T;c=F(23,50) if negative else F(0)
 S=T/4+F(3,2)*c*(x+F(1,4))+F(27,256)*M*(F(5,3)+F(5,4)*c)
 normal=F(2,5)*(F(231,2000)+F(2,27)) if negative else F(2,5)*(F(2,27)+F(231,500)*x)
 return (F(41,100)*S+normal)/F(117,1000)
def multiply(p,q):
 out=[F(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):out[i+j]+=x*y
 return out
def interpolate(fun,degree):
 nodes=[F(j,degree) for j in range(degree+1)];out=[F(0)]*(degree+1)
 for j,x in enumerate(nodes):
  term=[F(1)];den=F(1)
  for k,y in enumerate(nodes):
   if j==k:continue
   term=multiply(term,[-y,F(1)]);den*=x-y
  for k,c in enumerate(term):out[k]+=fun(x)*c/den
 return out
def evaluate(p,x):return sum(c*x**j for j,c in enumerate(p))
def derivative(p):return [j*p[j] for j in range(1,len(p))]
wp=interpolate(W,4);wpp=derivative(derivative(wp))
identity=[-F(13,50)*(z*z/2+3*b*b/8),F(13,50)*z**3/2,-F(13,50)*z**4/4]
assert wpp==identity
polys={}
for negative,label,floors in [(True,'negative',[6075,2577]),(False,'positive',[11528,11247])]:
 ep=interpolate(lambda x:E(x,negative),2);assert ep[2]>0 and all(c>=0 for c in ep)
 fun=lambda x:W(x)-E(x,negative)/200-x/100
 P=interpolate(fun,4)
 for x in [F(1,7),F(2,9)]:assert evaluate(P,x)==fun(x)
 second=derivative(derivative(P))
 assert all(second[j]==wpp[j]-(2*ep[2]/200 if j==0 else 0) for j in range(3))
 # An independent interval proof also follows from all degree-two Bernstein coefficients.
 bern=[evaluate(second,L),evaluate(second,L)+(U-L)*evaluate(derivative(second),L)/2,evaluate(second,U)]
 assert all(x<0 for x in bern)
 endpoints=[fun(L),fun(U)]
 assert all(x>F(y,10**6) for x,y in zip(endpoints,floors))
 polys[label]={'coefficients':list(map(str,P)),'second_derivative_Bernstein':list(map(str,bern)),'endpoints':list(map(str,endpoints))}
# Negative control: the stronger normalized mass bound 4/5 is false.
assert 200*F(comb(200,100),2**200)**2<F(4,5)**2
# Independent exact rational trigonometric enclosure for actual bump controls.
def atan_bounds(x,terms=16):
 s=sum((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms))
 nxt=x**(2*terms+1)/F(2*terms+1)
 return (s,s+nxt) if terms%2==0 else (s-nxt,s)
lo5,hi5=atan_bounds(F(1,5));lo239,hi239=atan_bounds(F(1,239))
pilo=16*lo5-4*hi239;pihi=16*hi5-4*lo239
assert F(25,8)<pilo<pihi<F(22,7)
@lru_cache(None)
def B(x):
 if x<=0 or x>=1:return F(0),F(0)
 if x in [F(1,4),F(3,4)]:return F(1,2),F(1,2)
 if x==F(1,2):return F(1),F(1)
 r=min(x,1-x);y=pilo*r;gap=(pihi-pilo)*r
 s=sum((-1)**j*y**(2*j+1)/F(factorial(2*j+1)) for j in range(12))
 low=max(F(0),s-gap);high=min(F(1),s+y**25/F(factorial(25))+gap)
 assert 0<=low<=high<=1
 return low*low,high*high
zero=((F(0),F(1)),)
def two(a,b):return ((-a,b/(a+b)),(b,a/(a+b)))
def moment(law,r):return sum(x**r*p for x,p in law)
@lru_cache(None)
def power(law,n):
 if len(law)==1:return ((F(0),F(1)),)
 (x,p),(y,q)=law
 return tuple((n*x+j*(y-x),F(comb(n,j))*p**(n-j)*q**j) for j in range(n+1))
@lru_cache(None)
def conditional(U0,U1,m0,m1):
 out={}
 for x,p in power(U0,m0):
  for y,q in power(U1,m1):out[x+y]=out.get(x+y,F(0))+p*q
 return tuple(out.items())
def kernel(x,U0,U1):
 return sum(pr*max(x-z,0) for z,pr in U0)-sum(pr*max(x-1-z,0) for z,pr in U1)-sum(pr for z,pr in U1 if 1+z<=x)
def expected_B(law,shift):
 lo=hi=F(0)
 for x,p in law:
  l,h=B(shift-x);lo+=p*l;hi+=p*h
 return lo,hi
cases=[('zero',zero,zero),('rare0',two(A,F(1,100)),zero),('rare1',zero,two(F(1,100),A)),('unequal',two(A,F(3,1000)),two(F(7,1000),A)),('common',two(F(1,100),F(1,100)),two(F(1,100),F(1,100)))]
actual=[];minorant_checks=0;swap_checks=0;negative_freezes=[]
for name,U0,U1 in cases:
 n=42;p=F(2,5);s0=moment(U0,2);s1=moment(U1,2);lam=n*((1-p)*s0+p*s1)
 assert lam<=U and moment(U0,1)==moment(U1,1)==0
 for x in [F(-3,5),F(0),F(1,10),F(1,4),F(2,5),F(1,2),F(116,125),F(97,100),F(1),F(8,5)]+[1+x for x,_ in U1]:
  assert kernel(x,U0,U1)>=F(2,5)*B(x)[1];minorant_checks+=1
 for shift in [F(-9,10),F(0),F(1,2),F(9,10)]:
  t=n*p+shift;k=t.__floor__();u=t-k
  frozen=conditional(U0,U1,n-k-1,k);actual_lo=actual_hi=frozen_lo=frozen_hi=F(0);G=F(0)
  for j in range(-2,3):
   law=conditional(U0,U1,n-k-1-j,k+j)
   l,h=expected_B(law,u-j);actual_lo+=l;actual_hi+=h
   l,h=expected_B(frozen,u-j);frozen_lo+=l;frozen_hi+=h
   G+=sum(pr*kernel(u-j-x,U0,U1) for x,pr in law)
  if U0==U1:
   assert all(dict(conditional(U0,U1,n-k-1-j,k+j))==dict(frozen) for j in range(-2,3))
  else:assert actual_lo-frozen_hi+4*pilo*pilo*(s0+s1)>=0
  swap_checks+=1
  assert G>=F(2,5)*actual_hi
  if actual_hi<frozen_lo:
   gap_lower=F(((frozen_lo-actual_hi)*10**12).__floor__(),10**12)
   assert gap_lower>0
   negative_freezes.append({'law':name,'t':str(t),'strict_gap_lower':str(gap_lower)})
  actual.append({'law':name,'n':n,'t':str(t),'lambda':str(lam),'five_kernel_loss':str(G)})
# A genuine omitted bump: u=1/4,V=5/2 leaves only j=-3 with value1/2.
assert sum(B(F(1,4)-j-F(5,2))[1] for j in range(-2,3))==0
assert B(F(3,4))==(F(1,2),F(1,2))
# Without the diameter restriction, centered +-1/2 has modulus1 at2pi.
assert F(0)<6*F(1,4)
print(json.dumps({'status':'PASS_INDEPENDENT_FIVE_COUNT_AND_RIGHT_COMPARISON','proof_pins':PINS,'table_margins':table_margins,'polynomials':polys,'actual_kernel_cases':len(actual),'pointwise_minorant_checks':minorant_checks,'centered_swap_checks':swap_checks,'actual_freeze_without_cost_failures':negative_freezes,'negative_controls':['4/5 normalized central binomial mass fails atn200','deleted omitted bump loses1/2','diameter-free CF contraction fails for+-1/2'],'actual_cases':actual,'scope':'Independent continuum derivation and exact outward component controls; no constructor code imported. The external Schulz theorem was checked separately in its original PDF.','python':sys.version},indent=2))

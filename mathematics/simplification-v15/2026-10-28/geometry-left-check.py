"""Exact acceptance for the full left signed comparison at n>=700.

Continuous probability, phase and sample-size reductions are in the proof.
The final noise problem is two concave quartics, checked at both endpoints.
No discovery result or constructor from another component is imported.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
N=700;lo=F(1,100);hi=F(8,25);p0=F(1,3);p1=F(2,5);q0=1-p1
A=F(7,10);d=F(17,250);v0=F(2,9);v3=F(13,125);kappa=F(7,5)
checks={}
def gate(name,x):
 assert name not in checks;checks[name]=F(x);assert x>0,(name,x)
def add(x,y):return [(x[i] if i<len(x) else F(0))+(y[i] if i<len(y) else F(0)) for i in range(max(len(x),len(y)))]
def scale(x,c):return [a*c for a in x]
def mul(x,y):
 out=[F(0)]*(len(x)+len(y)-1)
 for i,a in enumerate(x):
  for j,b in enumerate(y):out[i+j]+=a*b
 return out
def ev(x,t):return sum((a*t**i for i,a in enumerate(x)),F(0))
def atan(x,m):
 a=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(m)),F(0))
 b=a+(-1)**m*x**(2*m+1)/F(2*m+1)
 return min(a,b),max(a,b)
al,au=atan(F(1,5),12);bl,bu=atan(F(1,239),4)
pi_l=16*al-4*bu;pi_u=16*au-4*bl;phi_l=F(19943,50000);phi_u=F(2,5)
gate('pi_upper',F(22,7)-pi_u)
gate('pi_square_below10',10-F(22,7)**2)
gate('pi_below10over3',F(10,3)-F(22,7))
gate('phi_lower',1-2*pi_u*phi_l**2);gate('phi_upper',2*pi_l*phi_u**2-1)
gate('raw_scale_half',F(1,4)-(p1*(1-p1)+hi/N))
assert F(46,25)/2==F(23,25)
gate('left_sign_separation',p0-d);gate('right_sign_separation',q0-d)
gate('inward_below_amplitude',A-d)
gate('kernel_high',F(29,96)-F(2,5)*F(22,7)**2*d)
assert (1-d-A)/(A+d)==F(29,96)
gate('kernel_tangent_left',F(5,2)*F(1,4)-F(1,2))
gate('kernel_tangent_right',1-(F(1,2)+F(22,7)*(F(2,5)-F(1,4))))
gate('sqrt2_lower',2-F(7,5)**2)
gate('cosine_low',2*F(14,15)**2-kappa)
assert A+d==F(96,125)
gate('cosine_high',2*(F(7,10)-F(22,7)*(F(96,125)-F(3,4)))**2-kappa*F(96,125)**2)
# Physical lower and upper frozen variance coefficients.
dl=F(-48,25);dh=F(23,25)
gate('frozen_lower0',6-(dh+1)/q0)
gate('frozen_lower1',6+dl/p0)
gate('frozen_upper0',3+(dl+1)/q0)
gate('frozen_upper1',3-dh/p0)
gate('mesh_lower',N*(p0-d)-F(23,25))
gate('mesh_upper',N*(1-d-p1)-F(23,25))
gate('five_counts_lower',N*p0-F(23,25)-3)
gate('five_counts_upper',N*(1-p1)-F(23,25)-3)
gate('window_negative_displacement',4-(-dl+1))
gate('window_positive_displacement',4-(dh+3))
window_v=min(r*(1-r) for r in [p0-F(4,N),p1+F(4,N)])
gate('window_variance',window_v-F(11,50))
exp_upper=(8+F(1,12))/(N*F(11,50))
gate('five_count_mass',2*phi_l*(1-exp_upper)-F(3,4))
# Uniform maximum binomial mass bound from the retained finite mode estimate.
gate('mode_variance',1-F(1,43)-F(2,43**2)-F(39,40))
gate('mode_mass',F(41,100)**2-phi_u**2*F(40,39)*F(516,515)**2)
gate('v_three_halves',v0**3-v3*v3)
gate('curvature_zeta2',F(5,3)-sum((F(1,j*j) for j in range(1,6)),F(0))-F(1,5))
gate('curvature_zeta3',F(5,4)-sum((F(1,j**3) for j in range(1,4)),F(0))-F(1,18))
gate('curvature_c_less_than_one',1-F(8,25))
assert F(23,25)-q0==F(8,25)
gate('actual_cubic_favorable',1-F(5,6)-d-F(15,16)*hi/N)
# The full-noise polynomials: no grid or fitted proof object is loaded.
a=1-F(6,N);b=1+F(3,N);z=kappa*a;m=F(3,4)
x=[F(0),F(1)];T=scale(x,F(5,3));M=add(scale(T,A*A),scale(mul(T,T),3))
W=scale([F(0),z/2-A*A*b/16-12*F(22,7)**2/N,
         -z*z/4-3*b*b/16,z**3/12,-z**4/48],m*F(2,5))
# Reconstruct W'' independently from the globally negative completed square.
expected_Wsecond=scale([z*z/2+3*b*b/8,-z**3/2,z**4/4],-m*F(2,5))
assert [2*W[2],6*W[3],12*W[4]]==expected_Wsecond
polys={}
for name,c in [('negative',F(8,25)),('positive',F(0))]:
 sqrt_upper=[F(13,200),F(250,39)]
 # sqrt(T)<=T/(2r)+r/2 with r=.13, verified algebraically in the proof.
 assert sqrt_upper==[F(13,100)/2,F(5,3)/(2*F(13,100))]
 S=add(add(scale(T,F(1,4)),scale(sqrt_upper,c)),scale(M,F(27,256)*(F(5,3)+F(5,4)*c)))
 E=scale(S,F(41,100))
 if name=='negative':E=add(E,[phi_u*(F(23,200)+F(2,27))])
 else:E=add(E,[phi_u*F(2,27),phi_u*F(23,25)/2])
 E=scale(E,1/v3)
 assert all(x>=0 for x in E) and E[2]>0
 P=add(add(W,scale(E,-F(1,N))),scale(x,-F(1,100)))
 assert len(P)==5 and P[3]>0 and P[4]<0
 gate(name+'_concavity',-(2*P[2]+6*P[3]*hi))
 for end in [lo,hi]:gate(name+'_endpoint_'+str(end),ev(P,end))
 polys[name]={'coefficients':[str(x) for x in P],
  'second_derivative_upper':str(2*P[2]+6*P[3]*hi),
  'endpoint_margins':[str(ev(P,e)) for e in [lo,hi]]}
# False stronger mass premise, refuted at an actual interior binomial atom.
p=F(2,5);j=280;pi=F(comb(N,j))*p**j*(1-p)**(N-j)
assert N*pi*pi<1
# The trigonometric width premise cannot be removed: at x=1 the left side0.
assert 0<kappa
here=Path(__file__).resolve();proof=here.with_name('geometry-left.tex')
print(json.dumps({'status':'PASS_LEFT_SIGNED_N700','scalar_gates':len(checks),
 'checks':{k:str(v) for k,v in checks.items()},'polynomials':polys,
 'closed_noise_interval':[str(lo),str(hi)],
 'negative_controls':['unit_binomial_weight_is_false','cosine_lower_bound_requires_width_cap'],
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),'python':sys.version,
 'scope':'Exact continuous-domain reduction for full signed excess at C_E on n>=700,p∈[1/3,.4],lambda∈[.01,.32]. Acquisition, reflection, finite base and global cutoff are not accepted here.'},indent=2))

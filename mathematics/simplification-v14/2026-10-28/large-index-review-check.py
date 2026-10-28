"""Independent review arithmetic and exact small product-space controls.

No constructor code is imported or executed. Source hashes bind this review,
not mathematical correctness. The product probes test internal lemmas only.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
from math import factorial
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
canonical=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path('../simplification-v14').resolve()
source=canonical/'mathematics/simplification-v14/2026-10-28/large-index.tex'
expected='ad48f1eae57817b955016c6a12114e3929852a3e636afcfbb91646697b4c6509'
assert hashlib.sha256(source.read_bytes()).hexdigest()==expected
checks={}
def positive(name,x):
    assert name not in checks;checks[name]=F(x);assert x>0,(name,x)
# Independently reconstruct constants from the domain endpoints.
n0=6000;p0=F(2,5);p1=F(53,100);q0=1-p1;v0=p0*(1-p0)
lam0=F(3,40);lam1=F(9,25);d0=F(9,125);A=F(3,5)
scale=F(501,1000);positive('raw_scale',scale**2-F(1,4)-lam1/n0)
raw=F(46,25)*scale
positive('raw_phase_94',F(47,50)-raw)
positive('curvature_c46',F(23,50)-(raw-q0))
positive('threshold_lower',n0*p0-raw-3)
positive('threshold_upper',n0-3-n0*p1-raw)
# Different full-tail proof of transport, using zeta2 and distances >=.7r.
zeta2=F(5,3)
positive('zeta2_proof',zeta2-sum((F(1,k*k) for k in range(1,6)),F(0))-F(1,5))
transport=2*(3+F(9,10)*(zeta2/(1-d0)**2+(zeta2-1)/(1-A/2)**2))
positive('independent_transport_below12',12-transport)
positive('transport_license13',13-transport)
# CF interpolation is certified in two closed x intervals.
positive('sqrt3_lower',3-F(17,10)**2)
positive('sine_chord_square',2*F(51,40)**2-3)
positive('sine_second_square',2*(F(17,20)-F(22,7)*(F(84,125)-F(2,3)))**2-3*F(84,125)**2)
positive('clipped_age_coefficient',F(41,125)-F(3,10))
positive('transport_CF_lipschitz',1-F(3,10)*F(22,7))
var_ratio=1-F(2)/(n0*min(p0,q0))
positive('fixed_variance_ratio',var_ratio-F(37,42))
cf_per_noise=F(3,20)*3*F(37,42)/(1+3*F(37,42)*lam1)
positive('CF_gain',cf_per_noise-F(1,5))
# Fourth moments and the entire tail, independently integrated.
M4_per_lambda=A*A/F(2,5)+3*lam1/F(2,5)**2
assert M4_per_lambda==F(153,20)
right=F(11)-F(13,5);left=F(11)-A
full_tail=M4_per_lambda*(right**-4+right**-3/3+left**-4+left**-3/3)
positive('discarded_window_tail',F(1,100)-full_tail)
# Machin formula with finite alternating remainders: independently bound phi(0).
def atan(x,m):
    a=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(m)),F(0))
    b=a+(-1)**m*x**(2*m+1)/F(2*m+1)
    return min(a,b),max(a,b)
al,ah=atan(F(1,5),12);bl,bh=atan(F(1,239),4)
pi_l=16*al-4*bh;pi_h=16*ah-4*bl
positive('pi_upper22over7',F(22,7)-pi_h)
positive('density_lower',1-2*pi_h*F(199,500)**2)
positive('density_upper',2*pi_l*F(2,5)**2-1)
vrange=[(p0-F(12,n0))*(1-p0+F(12,n0)),(p1+F(12,n0))*(1-p1-F(12,n0))]
positive('window_variance',min(vrange)-F(23,100))
exponent=(F(12)**2/2+F(1,12))/(n0*F(23,100))
positive('window_exponent',F(53,1000)-exponent)
positive('window_mass',2*F(199,500)*(1-exponent)-F(3,4))
positive('window_loss_positive',F(19,100)*lam0-F(39,n0))
# Phase estimate: reconstruct the integrated polynomial in u.
zmin=min(z*(1-z) for z in [F(399,1000),F(531,1000)])
nummax=max(abs(1-2*z) for z in [F(399,1000),F(531,1000)])
positive('log_prefactor_derivative',1-nummax/zmin)
positive('entropy_third_derivative',4-nummax/zmin**2)
positive('Stirling_upper_error',F(11,10)-(1+F(1,12)+F(4,6)*8/n0))
a=F(47,50)
# Integral of (1-x)(2u+2a-x-1), reconstructed by integration of x powers:
poly=[F(0),2*a-1,2-a,F(-2,3)]
assert sum(poly)==a+F(1,3)
# Its derivative is concave, hence the minimum is at u=0 or1.
derivative_min=min(poly[1],poly[1]+2*poly[2]+3*poly[3])
positive('integrated_phase_monotonicity',derivative_min)
positive('log_ratio_below8',8-(F(37,20)+(1+2*a)/(2*v0)))
positive('normal_density_bound',F(41,50)**2*v0-F(2,5)**2)
phase_first=F(41,50)/(1-F(8,n0))*(F(37,20)+(a+F(1,3))/(2*v0))
positive('phase_first',F(15,4)-phase_first)
positive('phase_variance',v0**3-(F(2,5)*a*lam1/2)**2)
positive('complete_phase',5-(F(15,4)+1))
# Actual absolute-third-moment repair and all-n final comparison.
raw_gain=3*min(p0,q0)-d0
normal_linear=F(3,2)*(1-2*v0)
normal_quadratic=F(3,8)*(1-2*v0)/v0
assert raw_gain-normal_linear==F(87,250) and normal_quadratic==F(13,16)
positive('cubic_repair',raw_gain-normal_linear-normal_quadratic*lam1/n0)
positive('sqrt_n',n0-77**2);positive('sqrt_lambda',lam0-F(27,100)**2)
margin=F(57,400)-F(137,4*n0)/lam0-F(25,24*77)-F(23,24*77)/F(27,100)-F(1,200)
positive('final_relative_margin',margin)
positive('gap_noise_price0',18*p0-11*d0)
positive('gap_noise_price1',12*q0-9*d0)
ratio=scale*(1+lam1/(n0*v0))
positive('geometric_variance_ratio',F(251,500)-ratio)
positive('geometric_nd_below3',3-F(129,4)*ratio/(6*(1-d0)))

# Exact actual product-space probes, deliberately at small n only.
def rare(A,a,side):
    return [(-A,a/(A+a)),(a,A/(A+a))] if side==0 else [(-a,A/(A+a)),(A,a/(A+a))]
zero=[(F(0),F(1))]
symmetric=[(-F(1,10**6),F(1,2)),(F(1,10**6),F(1,2))]
cases=[('both',rare(A,F(1,50),0),rare(A,F(1,100),1)),
       ('negative_only',rare(A,F(1,1000),0),zero),
       ('positive_only',zero,rare(A,F(1,50),1)),
       ('tiny_symmetric',symmetric,symmetric),
       ('zero',zero,zero)]
records=[];positive_CF=0;nonzero_bias=0;atom_count=0
for n in [2,3,4]:
 for label,z0,z1 in cases:
  a0=max(x for x,_ in z0);a1=max(-x for x,_ in z1);d=a0+a1
  assert d<=d0
  v0a=sum(x*x*m for x,m in z0);v1a=sum(x*x*m for x,m in z1)
  pairs=[(x,y,m*l) for x,m in z0 for y,l in z1]
  kk=n//2;c0=max(z0,key=lambda x:x[1])[0];c1=max(z1,key=lambda x:x[1])[0]
  atom=kk+(n-kk)*c0+kk*c1
  for t in [atom-F(1,10**20),atom,atom+F(1,10**20),F(kk),F(kk)+F(1,2)]:
   assert n*a0<=t<n*(1-a1)
   k=t.numerator//t.denominator
   EK=EWK=distance=age=F(0);collision=False
   for seq in product(pairs,repeat=n):
    mass=F(1)
    for x,y,m in seq:mass*=m
    mesh=[F(j)+sum(seq[i][1] if i<j else seq[i][0] for i in range(n)) for j in range(n+1)]
    assert all(mesh[i]<mesh[i+1] for i in range(n))
    K=max(j for j in range(n+1) if mesh[j]<=t);assert K<n
    WK=mesh[K]-K;Wk=mesh[k]-k
    EK+=mass*K;EWK+=mass*WK;distance+=mass*abs(WK-Wk)
    age+=mass*min(t-mesh[K],F(41,125))
    collision=collision or t in mesh
   g=t-EK
   assert g>=age>=0 and EWK<=0 and distance<=13*d
   tk=(n-k)*v0a+k*v1a
   CFbound=F(3,20)*3*tk/(1+3*tk)-distance
   assert g>=CFbound
   positive_CF+=CFbound>0;nonzero_bias+=EWK!=0;atom_count+=collision
   for p in [F(2,5),F(53,100)]:
    lam=n*((1-p)*v0a+p*v1a)
    assert g>=lam/5-13*d
    records.append({'n':n,'law':label,'p':str(p),'t':str(t),'atom':collision,
     'lambda':str(lam),'inward_sum':str(d),'selected_transport':str(distance),
     'g':str(g),'clipped_age':str(age),'selected_mean':str(EWK),
     'actual_variance_CF_transport_lower':str(CFbound),
     'main_variance_factor_holds_here':tk>=F(37,42)*lam})
assert nonzero_bias>0 and atom_count>0 and positive_CF>0
# Explicit rejected claims; they are not counterexamples to Berry--Esseen.
assert any(F(z['selected_mean'])<0 for z in records)
assert any(F(z['selected_transport'])>0 for z in records)
assert margin<F(1,200) # Doubling the final target is not licensed by these bounds.
assert hashlib.sha256(source.read_bytes()).hexdigest()==expected
here=Path(__file__).resolve()
print(json.dumps({'status':'PASS_INDEPENDENT_LARGE_INDEX_REVIEW','scalar_gates':len(checks),
 'checks':{k:str(x) for k,x in checks.items()},'independent_transport_coefficient':str(transport),
 'phase_polynomial_coefficients':[str(x) for x in poly],'final_margin_after_target':str(margin),
 'product_controls':len(records),'distinct_mesh_threshold_controls':len(records)//2,
 'positive_CF_lower_controls':positive_CF,'nonzero_selected_mean_controls':nonzero_bias,
 'threshold_atom_controls':atom_count,'records':records,
 'negative_controls':['selected_mean_cannot_be_set_to_zero','transport_cannot_be_discarded',
                      'doubling_the_final_margin_is_not_licensed'],
 'proof_sha256':expected,'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),
 'python':sys.version,
 'scope':'Independent analytic review plus scalar reconstruction and small product-space probes. No constructor code imported, no n6000 convolution, no acquisition or global-conjecture acceptance.'},indent=2))

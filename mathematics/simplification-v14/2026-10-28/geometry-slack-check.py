"""Exact arithmetic for the full signed exclusion n Q(p)/sqrt(pq)>=24.

All constants are constructed from the displayed analytic inequalities.
There is no parameter grid or inherited acceptance-program execution.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
gates={}
def gate(k,x):
    assert k not in gates;gates[k]=F(x)
S=F('3.162277660');Su=F('3.162277661');d=F(17,250)
pmin=F(1,3);pmax=F(2,5);vmin=F(2,9);N=F(42)
oldU=F(8,25);U=F(9,100);B=F(129,4);target=F(24)
gate('sqrt10_lower',10-S*S);gate('sqrt10_upper',Su*Su-10)
# Squared denominators at their analytically proved maxima.
for name,bound,square in [('sqrt_p_q3',F(63,200),F(8,81)),
                         ('p_sqrt_q3',F(93,500),F(108,3125)),
                         ('sqrt_p3_q',F(49,250),F(24,625)),
                         ('sqrt_p3_q2',F(19,125),F(72,3125))]:
    gate('denominator_'+name,bound*bound-square)
gate('v_three_halves_lower',vmin**3-F(13,125)**2)
gate('noise_root0',6*(1-d)*(S+1)-F(24,5)**2)
gate('noise_root1',6*(1-d)*(S-1)-F(69,20)**2)
Y0=3*(S+3)/F(63,200)+2*F(24,5)/F(93,500)-(Su+7)*d/F(13,125)
Y1=3*(S+1)/F(49,250)+2*F(69,20)/F(19,125)-(Su+5)*d/F(13,125)
gate('variance_price0_above100',Y0-100);gate('variance_price1_above100',Y1-100)
xmax=oldU/(N*vmin);assert xmax==F(6,175)
gate('power_slope',F(31,20)-(F(3,2)+3*xmax/8))
price=100-B*F(31,20)/(N*vmin)
gate('geometry_noise_price_positive',price)
gate('geometry_forces_lambda_below09',U*price-(B-target))
# Normal constants, independently obtained from Machin's formula.
def arctan(x,terms):
    val=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    nxt=(-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(val,val+nxt),max(val,val+nxt)
a,b=arctan(F(1,5),12);c,e=arctan(F(1,239),4)
pi_lo=16*a-4*e;pi_hi=16*b-4*c
phi_lo=F(19943,50000);phi_hi=F(2,5)
gate('normal_density_lower',1-phi_lo**2*2*pi_hi)
gate('normal_density_upper',phi_hi**2*2*pi_lo-1)
# Finite binomial mode bound, N=n+1>=43.
gate('mode_variance_guard',1-F(1,43)-F(2,43**2)-F(39,40))
beta=F(41,100)
gate('mode_mass_upper_squared',beta**2-phi_hi**2*F(40,39)*F(516,515)**2)
# Infinite sums are bounded by exact finite sums plus integral remainders.
gate('zeta2',F(5,3)-sum((F(1,j*j) for j in range(1,6)),F(0))-F(1,5))
gate('zeta3',F(5,4)-sum((F(1,j**3) for j in range(1,4)),F(0))-F(1,18))
gate('closed_crossing_left',N*(pmin-d)-F(23,25))
gate('closed_crossing_right',N*(1-d-pmax)-F(23,25))
gate('raw_scale_half',F(1,4)-(pmax*(1-pmax)+U/N))
cmax=F(8,25);assert F(23,25)-(1-pmax)==cmax
gate('c_less_than_one',1-cmax)
T=F(3,20);M=F(141,1000);rootT=F(97,250)
assert U/(1-pmax)==T
assert F(7,10)**2*T+3*T*T==M
gate('sqrtT_upper',rootT*rootT-T)
rho_bracket=3*pmin-F(3,2)*(1-2*vmin)-d-F(3,8)*(1-2*vmin)*(U/N)/vmin
gate('rho_correction_favorable',rho_bracket)
def curv(c):return T/4+c*rootT+F(27,256)*M*(F(5,3)+F(5,4)*c)
Em=(beta*curv(cmax)+phi_hi*(F(23,200)+F(2,27)))/F(13,125)
Ep=(beta*curv(0)+phi_hi*F(2,27)+phi_hi*F(23,25)*U/2)/F(13,125)
gate('negative_threshold_margin',4*phi_lo-Em-F(1,10))
gate('positive_threshold_margin',4*phi_lo-Ep-F(1,10))
assert all(x>0 for x in gates.values()),{k:str(x) for k,x in gates.items() if x<=0}
# Coefficient mutations relevant to analytic scaling.
assert 4*phi_lo-Em*N-F(1,10)<0 # dropping the curvature/interpolation 1/n is fatal.
assert 3*F(13,50)-F(3,2)*(1-2*F(13,50)*F(37,50))-d<0
# Sample-size cutoffs follow only on the source-supported p>=1/3 range.
index_rows=[]
for p,cutoff in [(F(1,3),126),(F(7,20),196),(F(3,8),491),(F(39,100),1141),(F(2,5),2682)]:
    q=1-p;v=p*q;Q=(S+1)*p*p+(S-1)*q*q-6*v
    assert Q>0 and cutoff*cutoff*Q*Q>target*target*v
    index_rows.append({'p':str(p),'all_n_at_least_excluded':cutoff,
                       'positive_squared_margin':str(cutoff*cutoff*Q*Q-target*target*v)})
here=Path(__file__).resolve();proof=here.with_suffix('.tex').with_name('geometry-slack.tex')
print(json.dumps({'status':'PASS_GEOMETRY_BERNOULLI_REGION','gate_count':len(gates),
 'gates':{k:str(x) for k,x in gates.items()},'negative_error_upper':str(Em),
 'positive_error_upper':str(Ep),'pi_enclosure':[str(pi_lo),str(pi_hi)],
 'consequent_index_rows':index_rows,
 'negative_controls':['normalization_1_over_n_cannot_be_omitted',
                      'favorable_cubic_sign_not_extended_below_one_third'],
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),'python':sys.version,
 'scope':'All phases and acquired noise on 1/3<=p<=.4 with n Q(p)/sqrt(pq)>=24; '
 'conditional on the stated support/budget inputs and external Bernoulli theorem.'},indent=2))

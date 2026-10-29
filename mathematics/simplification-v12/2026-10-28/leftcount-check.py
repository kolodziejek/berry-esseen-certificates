"""Exact closed scalar checks for the LEFT-01 theorem; no floating acceptance.

The continuous reductions are proved in leftcount.tex.  This program checks
their finite rational endpoints and sign/denominator hypotheses.  It does not
claim to establish those analytic reductions by a PASS.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions are proof obligations; optimization forbidden')

A=F(7,10); d=F(17,250); U=F(1,100); N=F(42); v=F(3,16)
lo=-F(109,500); hi=F(391,500); b=F(1,20); D=F(17,10)
near=F(1,10); Dnear=F(101,100); xi=F(46,25)*F(491,1000)
alpha=F(27,50); M=5*alpha**4; T=F(23,21)*U; z0=F(3,2)
cl=F(819,2000); cu=F(41,100); ml=F(18,25); mg=F(57,100)
fl=F(47,50); fu=F(213,200); Ri=F(53,50); Rg=F(9,5)
checks={}
def gate(name,margin):
    assert name not in checks
    checks[name]=F(margin)
def atan(x,n):
    a=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    c=a+(-1)**n*x**(2*n+1)/F(2*n+1)
    return min(a,c),max(a,c)
a=atan(F(1,5),34); c=atan(F(1,239),10)
pil=16*a[0]-4*c[1]; piu=16*a[1]-4*c[0]
gate('pi_lower',pil-F(3141592653589793,10**15))
gate('pi_upper',F(3141592653589794,10**15)-piu)
gate('phi_lower',1-2*piu*F(19943,50000)**2)
gate('phi_upper',2*pil*F(2,5)**2-1)
sqrt10lo=F(3162277660,10**9); sqrt10hi=F(3162277661,10**9)
gate('sqrt10_lower',10-sqrt10lo**2);gate('sqrt10_upper',sqrt10hi**2-10)
gate('CE_lower',(3+sqrt10lo)**2-36*cl**2*2*piu)
gate('CE_upper',36*cu**2*2*pil-(3+sqrt10hi)**2)

assert hi-lo==1 and lo==(A-1-2*d)/2 and hi==(A+1-2*d)/2
gate('sqrt_variance',F(491,1000)**2-F(6,25)-U/N)
gate('sqrt_v',F(49,100)**2-F(6,25))
gate('global_displacement',D-xi-hi)
gate('inner_displacement',1-xi-b)
gate('near_displacement',Dnear-xi-near)
gate('global_segment_left',F(1,4)-D/N-F(1,5))
gate('global_segment_right',F(9,20)-F(2,5)-D/N)
gate('near_segment_left',F(1,4)-Dnear/N-F(9,40))
gate('near_segment_right',F(17,40)-F(2,5)-Dnear/N)
vg=F(4,25); vn=F(279,1600)
for lab,vv,hh,e3,ld,sr in [
    ('global',vg,F(3,5),F(24),F(4),F(53,100)),
    ('near',vn,F(11,20),F(19),F(16,5),F(12,25))]:
    gate(lab+'_entropy3',e3-hh/vv**2)
    gate(lab+'_log_derivative',ld-hh/vv)
    gate(lab+'_factorial_remainder',sr-1/(12*vv))
Zg=lambda x:2*x+F(53,100)+4*x**3/N
Zn=lambda x:F(8,5)*x+F(12,25)+F(19,6)*x**3/N
gate('normal_noise_coefficient',4-1/(2*v)-D**2/(2*N*v**2))
for lab,dd,bb,Z,lower,upper in [
    ('global',D,hi,Zg,F(2,3),F(3,2)),
    ('inner',F(1),b,Zn,fl,fu),
    ('near',Dnear,near,Zn,F(93,100),F(11,10))]:
    eta=(4*U+(2*dd*bb+bb**2)/(2*v)+Z(dd))/N
    gate(lab+'_log_denominator',1-eta)
    gate(lab+'_slope_lower',1-eta-lower)
    gate(lab+'_slope_upper',upper*(1-eta)-1)
mass=lambda x,Z:F(19943,50000)/F(49,100)*(1-(x*x/(2*v)+Z(x))/N)
gate('inner_mass',mass(F(1),Zn)-ml)
gate('global_mass',mass(D,Zg)-mg)
gate('mode_log_denominator',1-Zn(F(1))/N)
gate('mode_mass',v*(1-Zn(F(1))/N)**2-F(2,5)**2)
gate('global_ratio',Rg*mg-1)
gate('inner_ratio',Ri-1-F(2,5)/(N*v))
gate('later_inner_ratios',2-F(2,5)-1)
gate('own_global_variance',F(7,6)-1-4*D/N)
gate('incoming_global_variance',F(4,3)-1-4*(D+1)/N)
gate('incoming_inner_variance',F(6,5)-1-8/N)
assert 1-4/N==F(19,21) and 1+4/N==F(23,21)

# Repairs remain valid even when the actual marginal rho is below rho_B.
Bbad=F(3,2)*(1-2*v)+d-F(3,4)+3*(1-2*v)*U/(8*N*v)
gate('adverse_cubic_repair',F(4,3)**2*v**3-(cu*Bbad)**2)
gate('normal_variance_repair',F(5,2)**2*v**3-F(1,5)**2)
gate('inner_separate_repair',4-F(5,2)-F(4,3))
gate('global_separate_repair',6-F(5,2)*D-F(4,3))

# Joint moment pricing: all inequalities are uniform, not fitted to a law.
gate('ell_cubed_cap',F(25,2)**2*v**3-1)
gate('count0_reciprocal',F(1,38)-1/(N-F(5,3)))
assert 1/(N-4)==F(1,38)
Gamma=cu*F(25,2)*M/(ml*38)
gate('joint_endpoint_branch',A-d-4*b-Gamma)
Bjoint=A+F(3,4)-F(3,2)*(1-2*v)-3*(1-2*v)*U/(8*N*v)
gate('joint_positive_bracket',Bjoint)
gate('joint_gain',cl*Bjoint-F(7,4)*F(491,1000)**3)

def quartic(sig,slope,z,t):
    return ((3*alpha**2-A*A-3*t)/M+
        (2*sig/(5*alpha)+slope-4*A*t/M)*z+
        (3*alpha**2*t-6*t*t)*z*z/M-t**3*z**4/M)
gate('negative_quartic_decreasing',fu-2/(5*alpha)-6*alpha**2*T*z0/M)
for ti,label in [(F(0),'zero'),(T,'max')]:
    gate('negative_quartic_'+label,quartic(1,-fu,z0,ti)-F(1,4))
gate('positive_quadratic_coefficient',3*alpha**2-6*T)
gate('positive_quartic_increasing',fl-2/(5*alpha)-4*A*T/M-4*T**3*z0**3/M)
gate('positive_quartic',quartic(-1,fl,F(0),T)-F(4,5))
gate('inner_switch_inside',b-z0*T)
gate('negative_switch_value',z0*z0/(1+z0*z0*T)-fu*z0-F(1,2))
gate('negative_switch_derivative',2*z0/(1+z0*z0*T)**2-fu)
gate('negative_inner_endpoint',b*b/(T+b*b)-fu*b-T/2)
gate('positive_linear_extension',fl*z0-F(4,5))

def Q(mu,h):
    aa=(1-h)/A-1
    assert aa>0
    return mu**2*(F(1,2)+mu/6)/(aa+mu)**2
def J(mu,h,start):
    bb=1/A-1-h/(start*A)
    assert start in [2,3] and bb>0 and 0<=3*mu<1
    return (mu**3/3 if start==2 else F(3,8)*mu**4)/((bb+mu)**2*(1-3*mu))
muI=F(6,5)*U/A**2; muG=F(4,3)*U/A**2
for name,mu,hh,start in [('inner',muI,b,2),('negative',muG,F(0),2),
                       ('near',muG,near,3),('far',muG,hi,3)]:
    gate(name+'_hinge_domain',1/A-1-hh/(start*A))
    gate(name+'_tail_ratio',1-3*mu)
gate('inner_Q_over_lambda_monotone',(1-b)/A-1-muI)
gate('global_Q_over_lambda_monotone',1/A-1-muG)
negTail=Q(muI,F(0))+J(muI,F(0),2)
posTail=Q(muI,b)+J(muI,b,2)
for name,own,tail,repair in [
    ('inner_joint',F(1,4),negTail,F(3,4)),
    ('inner_negative_cantelli',F(1,2),negTail,F(4)),
    ('inner_positive',F(4,5),posTail,F(4))]:
    bracket=own*F(19,21)-Ri*tail/U
    gate(name+'_bracket',bracket)
    gate(name+'_final',ml*bracket-repair/N-F(1,100))
Tg=F(7,6)*U
gate('negative_outer_initial_derivative',2*b*Tg/(Tg+b*b)**2-F(3,2))
own=min(r*r/(Tg+r*r)-F(3,2)*r for r in [b,-lo])
br=own-Rg*(Q(muG,F(0))+J(muG,F(0),2))
gate('negative_outer_bracket',br)
gate('negative_outer_final',mg*br-6*U/N-U/100)
tg=F(4,3)*U
def two_cantelli(u):
    return tg/(tg+(1-u)**2)+2*tg/(2*tg+(2-u)**2)
br=F(93,100)*b-Rg*(two_cantelli(near)+J(muG,near,3))
gate('positive_near_bracket',br)
gate('positive_near_final',mg*br-6*U/N-U/100)
gate('positive_far_concavity1',3*(1-hi)**2-tg)
gate('positive_far_concavity2',3*(2-hi)**2-2*tg)
br=min(F(2,3)*u-Rg*two_cantelli(u) for u in [near,hi])-Rg*J(muG,hi,3)
gate('positive_far_bracket',br)
gate('positive_far_final',mg*br-6*U/N-U/100)

def closed_cover(intervals):
    target=[(lo,-b),(-b,b),(b,near),(near,hi)]
    return intervals==target and all(a<c for a,c in intervals) and all(
        intervals[i][1]==intervals[i+1][0] for i in range(len(intervals)-1))
cover=[(lo,-b),(-b,b),(b,near),(near,hi)]
assert closed_cover(cover)
mutations=[cover[:-1],cover+[cover[-1]],list(reversed(cover)),
           [(lo,-b),(-b,b),(b+F(1,10**6),near),(near,hi)]]
assert all(not closed_cover(x) for x in mutations)

# Actual counterexamples to shortcuts, not to the theorem.
pb=F(13,50);vb=pb*(1-pb);sb=(1-pb)/10**6
raw=vb*(1-2*vb)+3*pb*sb
assert raw**2*vb<(1-2*vb)**2*(vb+sb)**3
kap=F(-1); eps=F(1,1000); inward=d
moment_ratio=eps**2-eps*inward+inward**2-kap*(inward-eps)
assert moment_ratio>A*A+kap*A  # Wrong outer endpoint after deleting guard.
assert (2-hi)/A+2*muG-2<0     # Invalid j=2 hinge at the largest phase.
assert ml*(F(1,4)*F(19,21)-Ri*negTail/U)-F(4,42)-F(1,100)<0
negative_controls=['adverse_rho_is_real','unguarded_endpoint_price_rejected',
                   'second_hinge_at_far_phase_rejected',
                   'discarding_joint_reserve_fails_this_01_proof',
                   'cover_missing','cover_duplicate','cover_reordered','cover_gap']
failed={k:str(x) for k,x in checks.items() if x<=0}
proof=Path(__file__).with_name('leftcount.tex')
print(json.dumps({'status':'PASS_LEFT_01_SCALAR_GATES' if not failed else 'FAILED',
    'gate_count':len(checks),'negative_controls':negative_controls,
    'failed':failed,'margins':{k:str(x) for k,x in checks.items() if k.endswith('_final')},
    'checks':{k:str(x) for k,x in checks.items()},
    'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest() if proof.exists() else None,
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'python':sys.version,'scope':'Exact scalar gates and explicit negative controls. '
    'The universal probability conclusion requires the analytic reductions and review.'},indent=2))
assert not failed

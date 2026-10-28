"""Exact scalar gates for the new small-noise comparison, not a global cover."""
from fractions import Fraction as F
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Optimization disables proof obligations')

def evaluate(U=F(1,500)):
    checks={}
    def positive(name,x):
        checks[name]=x
        return x>0
    A=F(3,5); d=F(9,125); N=F(42); v=F(6,25)
    lower,upper=-F(34,125),F(91,125)
    inner=F(1,20); D=F(33,20); cv=F(5,2)
    Z=lambda t:F(5,8)*t+F(3,8)+t**3/N
    B0=F(8,3)
    P=lambda D,a:(2*D*a+a*a)/(2*v)+Z(D)
    positive('global_threshold_delta',D-(F(46,25)*F(501,1000)+upper))
    positive('sqrt_variance_upper',F(501,1000)**2-(F(1,4)+U/N))
    positive('inner_delta',1-(F(46,25)*F(501,1000)+inner))
    positive('count_fraction_lower',F(2,5)-D/N-F(9,25))
    positive('count_fraction_upper',F(23,40)-(F(53,100)+D/N))
    positive('interior_lower',N*F(2,5)-D-1)
    positive('interior_upper',N*F(47,100)-D-1)
    positive('stirling_variance',F(9,25)*F(16,25)-F(23,100))
    positive('stirling_E',6-F(7,25)/F(23,100)**2)
    positive('stirling_L',F(5,4)-F(7,25)/F(23,100))
    positive('stirling_R',F(3,8)-1/(12*F(23,100)))
    positive('log_variance_B0',B0-(1/(2*v)+D*D/(2*N*v*v)))
    eps=(B0*U+P(D,upper))/N
    eps_inner=(B0*U+P(F(1),inner))/N
    positive('global_lower_derivative',1-eps-F(4,5))
    positive('global_upper_derivative',F(5,4)*(1-eps)-1)
    positive('inner_lower_derivative',1-eps_inner-F(19,20))
    positive('inner_upper_derivative',F(21,20)*(1-eps_inner)-1)
    mass=lambda D:2*F(19943,50000)*(1-(D*D/(2*v)+Z(D))/N)
    positive('global_mass',mass(D)-F(13,20))
    positive('inner_mass',mass(F(1))-F(73,100))
    positive('mode_mass_squared',F(17,20)**2*v*(1-Z(1)/N)**2-F(2,5)**2)
    positive('mode_own_ratio',F(3,2)*F(13,20)-F(17,20))
    positive('inner_ratio',F(53,50)-1-F(53,100)/(N*v))
    positive('inner_second_ratio',2-F(53,100)-1)
    positive('inner_count_variance',F(9,8)-(1+cv*2/N))
    positive('global_count_variance',F(7,6)-(1+cv*(D+1)/N))
    positive('global_own_variance',F(11,10)-(1+cv*D/N))
    positive('cubic_repair_nonnegative',F(6,5)-F(3,2)*(1-2*v)-d-F(3,8)*(1-2*v)*U/(N*v))
    positive('normal_repair_squared',F(7,4)**2*v**3-F(1,5)**2)
    positive('global_repair',3-F(7,4)*D)
    positive('inner_repair',2-F(7,4))
    positive('zeta3',F(49,40)-(1+F(1,8)+F(1,27)+F(1,18)))
    positive('zeta2',F(17,10)-(1+F(1,4)+F(1,9)+F(1,3)))
    # K0=5 exceeds (9+6 sqrt(3))/4 because 11^2>108.
    positive('quartic_majorant',F(121-108))
    a=F(9,20); K0=F(5); den=K0*a**4
    om_lo=F(79,84);om_hi=F(89,84);tstar=om_hi*U
    def quadratic_min(c0,c1,c2,zmax):
        candidates=[c0,c0+c1*zmax+c2*zmax*zmax]
        if c2>0 and 0<-c1/(2*c2)<zmax:
            candidates.append(c0-c1*c1/(4*c2))
        return min(candidates)
    def scaled_min(sig,b,zmax):
        mins=[]
        for t in (F(0),tstar):
            c0=(3*a*a-A*A-3*t)/den
            c1=2*sig/(K0*a)+b-4*A*t/den
            c2=(3*a*a*t-6*t*t-t**3*zmax*zmax)/den
            mins.append(quadratic_min(c0,c1,c2,zmax))
        return min(mins)
    zminus=F(2); zplus=F(3,2);cm=F(4,5);cp=F(1)
    positive('negative_scaled_quartic',scaled_min(1,-F(21,20),zminus)-cm)
    positive('positive_scaled_quartic',scaled_min(-1,F(19,20),zplus)-cp)
    positive('negative_cantelli_start',zminus*zminus/(1+zminus*zminus*tstar)-F(21,20)*zminus-cm)
    positive('negative_cantelli_slope',2*zminus/(1+zminus*zminus*tstar)**2-F(21,20))
    positive('negative_cantelli_endpoint',inner*inner/(tstar+inner*inner)-F(21,20)*inner-cm*tstar)
    positive('negative_split',inner-zminus*tstar)
    positive('positive_linear',F(19,20)*zplus-cp)
    positive('positive_split',inner-zplus*tstar)
    tail=lambda V:A*A*V*F(49,40)+3*V*V*U*F(17,10)
    Ki=tail(F(9,8))/(1-inner)**4
    positive('inner_final_margin',F(73,100)*(cm*om_lo-F(53,50)*Ki)-F(2,42)-F(1,100))
    Tg=F(11,10)*U
    positive('outer_negative_concavity',3*inner*inner-Tg)
    ownneg=min(x*x/(Tg+x*x)-F(5,4)*x for x in [inner,-lower])
    positive('outer_negative_bracket',ownneg-F(3,2)*tail(F(7,6))*U)
    positive('outer_negative_final',F(13,20)*(ownneg-F(3,2)*tail(F(7,6))*U)-F(3,42)*U-U/100)
    # u(1-u)^4 rises then falls on [0,1], so its minimum is at an endpoint.
    G=min(x*(1-x)**4 for x in [inner,upper])
    positive('outer_positive_bracket',F(4,5)*G-F(3,2)*tail(F(7,6))*U)
    positive('outer_positive_final',F(13,20)*(F(4,5)*G-F(3,2)*tail(F(7,6))*U)-F(3,42)*U-U/100)
    return checks

checks=evaluate()
assert all(x>0 for x in checks.values()),[k for k,x in checks.items() if x<=0]
bad=evaluate(F(1,20))
assert any(x<=0 for x in bad.values())
print(json.dumps({'status':'PASS_UNIFORM_SMALL_NOISE_SCALAR_GATES',
    'scope':'Full scalar proof of the stated conditional n>=42, p in [.4,.53], lambda in (0,.002], .6-strip comparison; not the remaining noise/probability domain.',
    'gate_count':len(checks),'gates':{k:str(v) for k,v in checks.items()},
    'diagnostic_final_inner_margin_above_epsilon':float(checks['inner_final_margin']),
    'negative_control':'The same sufficient constants reject the unproved expansion to lambda<=.05',
    'negative_control_failed_gates':[k for k,x in bad.items() if x<=0],
    'python':sys.version},indent=2))

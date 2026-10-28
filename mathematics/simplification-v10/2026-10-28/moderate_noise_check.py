"""Exact rational gates for the direct comparison on 0 < lambda <= 1/50.

This checks the scalar inequalities in moderate-noise.tex. It does not discover
them, prove the probability reduction, or certify any other parameter region.
"""
from fractions import Fraction as F
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Optimization disables proof obligations')


def evaluate(U=F(1, 50)):
    checks = {}
    def gate(name, value):
        checks[name] = value
    A=F(3,5); d=F(9,125); N=F(42); v=F(6,25)
    lower=-F(34,125); upper=F(91,125); inner=F(1,20)
    near=F(1,10); D=F(33,20); cv=F(5,2); xi=F(46,25)*F(501,1000)
    Z=lambda t:F(5,8)*t+F(3,8)+t**3/N
    B0=F(8,3)
    P=lambda z,b:(2*z*b+b*b)/(2*v)+Z(z)
    gate('global_threshold_delta',D-xi-upper)
    gate('sqrt_variance_upper',F(501,1000)**2-F(1,4)-U/N)
    gate('inner_delta',1-xi-inner)
    gate('count_fraction_lower',F(2,5)-D/N-F(9,25))
    gate('count_fraction_upper',F(23,40)-F(53,100)-D/N)
    gate('interior_lower',N*F(2,5)-D-1)
    gate('interior_upper',N*F(47,100)-D-1)
    gate('stirling_variance',F(9,25)*F(16,25)-F(23,100))
    gate('stirling_E',6-F(7,25)/F(23,100)**2)
    gate('stirling_L',F(5,4)-F(7,25)/F(23,100))
    gate('stirling_R',F(3,8)-1/(12*F(23,100)))
    gate('log_variance_B0',B0-1/(2*v)-D*D/(2*N*v*v))
    eps=(B0*U+P(D,upper))/N
    eps_inner=(B0*U+P(F(1),inner))/N
    gate('global_lower_derivative',1-eps-F(4,5))
    gate('global_upper_derivative',F(5,4)*(1-eps)-1)
    gate('inner_lower_derivative',1-eps_inner-F(19,20))
    gate('inner_upper_derivative',F(21,20)*(1-eps_inner)-1)
    Dnear=F(21,20)
    gate('near_delta',Dnear-xi-near)
    gate('near_lower_derivative',1-(B0*U+P(Dnear,near))/N-F(19,20))
    G=2*xi*upper-upper**2
    gate('positive_G_monotone',xi-upper)
    gate('positive_lower_derivative',1-((U+G)/(2*v)+Z(D))/N-F(9,10))
    mass=lambda z:2*F(19943,50000)*(1-(z*z/(2*v)+Z(z))/N)
    gate('global_mass',mass(D)-F(13,20))
    gate('inner_mass',mass(F(1))-F(73,100))
    gate('mode_mass_squared',F(17,20)**2*v*(1-Z(1)/N)**2-F(2,5)**2)
    gate('mode_own_ratio',F(3,2)*F(13,20)-F(17,20))
    gate('inner_ratio',F(53,50)-1-F(53,100)/(N*v))
    gate('inner_second_ratio',2-F(53,100)-1)
    gate('inner_count_variance',F(9,8)-1-cv*2/N)
    gate('global_count_variance',F(7,6)-1-cv*(D+1)/N)
    gate('global_own_variance',F(11,10)-1-cv*D/N)
    gate('cubic_repair_nonnegative',F(6,5)-F(3,2)*(1-2*v)-d-F(3,8)*(1-2*v)*U/(N*v))
    gate('normal_repair_squared',F(7,4)**2*v**3-F(1,5)**2)
    gate('global_repair',3-F(7,4)*D)
    gate('inner_repair',2-F(7,4))
    gate('quartic_majorant',F(121-108))

    alpha=F(1,2); den=5*alpha**4
    om_lo=F(79,84); om_hi=F(89,84); tstar=om_hi*U
    def quadratic_min(c0,c1,c2,zmax):
        values=[c0,c0+c1*zmax+c2*zmax*zmax]
        if c2>0 and 0 < -c1/(2*c2) < zmax:
            values.append(c0-c1*c1/(4*c2))
        return min(values)
    def scaled_min(sigma,b,zmax):
        values=[]
        for t in (F(0),tstar):
            c0=(3*alpha*alpha-A*A-3*t)/den
            c1=2*sigma/(5*alpha)+b-4*A*t/den
            c2=(3*alpha*alpha*t-6*t*t-t**3*zmax*zmax)/den
            values.append(quadratic_min(c0,c1,c2,zmax))
        return min(values)
    zminus=F(2); zplus=F(3,2); cm=F(3,8); cp=F(1)
    gate('negative_scaled_quartic',scaled_min(1,-F(21,20),zminus)-cm)
    gate('positive_scaled_quartic',scaled_min(-1,F(19,20),zplus)-cp)
    gate('negative_cantelli_start',zminus*zminus/(1+zminus*zminus*tstar)-F(21,20)*zminus-cm)
    gate('negative_cantelli_slope',2*zminus/(1+zminus*zminus*tstar)**2-F(21,20))
    gate('negative_cantelli_endpoint',inner*inner/(tstar+inner*inner)-F(21,20)*inner-cm*tstar)
    gate('negative_split',inner-zminus*tstar)
    gate('positive_linear',F(19,20)*zplus-cp)
    gate('positive_split',inner-zplus*tstar)

    def tail_rest(mu,h):
        b=1/A-1-h/(2*A)
        return mu**3/(3*(b+mu)**2*(1-3*mu))
    def tail_all(mu,h):
        a=(1-h)/A-1
        return mu**2*(F(1,2)+mu/6)/(a+mu)**2+tail_rest(mu,h)
    mui=F(9,8)*U/A**2; mug=F(7,6)*U/A**2
    for label,mu,h in [('inner',mui,inner),('negative',mug,F(0)),('near',mug,near),('far',mug,upper)]:
        gate(label+'_geometric_ratio',1-3*mu)
        gate(label+'_tail_denominator',1/A-1-h/(2*A))
    gate('inner_first_ratio_monotonicity',(1-inner)/A-1-mui)
    gate('negative_first_ratio_monotonicity',1/A-1-mug)
    Ti=tail_all(mui,inner)
    inner_bracket=cm*om_lo-F(53,50)*Ti/U
    gate('inner_positive_bracket',inner_bracket)
    gate('inner_final_margin',F(73,100)*inner_bracket-F(2,42)-F(1,100))

    Tg=F(11,10)*U
    ownneg=min(x*x/(Tg+x*x)-F(5,4)*x for x in [inner,-lower])
    gate('negative_outer_initial_slope',2*inner*Tg/(Tg+inner**2)**2-F(5,4))
    neg_bracket=ownneg-F(3,2)*tail_all(mug,F(0))
    gate('negative_outer_bracket',neg_bracket)
    gate('negative_outer_final',F(13,20)*neg_bracket-F(3,42)*U-U/100)

    tin=F(7,6)*U
    near_bracket=F(19,20)*inner-F(3,2)*(tin/(tin+(1-near)**2)+tail_rest(mug,near))
    gate('near_positive_bracket',near_bracket)
    gate('near_positive_final',F(13,20)*near_bracket-F(3,42)*U-U/100)
    gate('far_cantelli_convexity',3*(1-upper)**2-tin)
    far_base=min(F(9,10)*x-F(3,2)*tin/(tin+(1-x)**2) for x in [near,upper])
    far_bracket=far_base-F(3,2)*tail_rest(mug,upper)
    gate('far_positive_bracket',far_bracket)
    gate('far_positive_final',F(13,20)*far_bracket-F(3,42)*U-U/100)
    return checks


if __name__ == '__main__':
    values=evaluate()
    assert all(x>0 for x in values.values()),[k for k,x in values.items() if x<=0]
    negative={str(U):[k for k,x in evaluate(U).items() if x<=0] for U in [F(1,20),F(3,40)]}
    assert all(negative.values())
    # Genuine failure of this sufficient quartic bound at an admissible point,
    # not a counterexample to the probability theorem. Here t=lambda=r=1/20,
    # z=r/t=1, alpha=1/2, and the negative normal coefficient is 21/20.
    t=F(1,20); alpha=F(1,2); A=F(3,5); den=5*alpha**4
    point=(3*alpha**2-A**2-3*t)/den+2/(5*alpha)-F(21,20)-4*A*t/den
    point+=(3*alpha**2*t-6*t*t-t**3)/den
    assert point==F(257,1250) and point<F(3,8)
    # n=42,p=1/2, conditional U=+-1/sqrt(840) realizes t=lambda=1/20.
    assert F(4,840)<F(9,125)**2
    print(json.dumps({'status':'PASS_UNIFORM_MODERATE_NOISE_SCALAR_GATES',
        'mathematical_scope':'Conditional comparison n>=42, p in [2/5,53/100], .6 strip, d<=9/125, |H|<=46/25, 0<lambda<=1/50. Proof and external P2 lemma remain analytic obligations.',
        'gate_count':len(values),'gates':{k:str(v) for k,v in values.items()},
        'final_margins_above_epsilon':{k:float(v) for k,v in values.items() if 'final' in k},
        'negative_controls':negative,
        'point_negative_control':{'t_lambda_r':'1/20','quartic_scaled_lower_bound':str(point),
          'target':'3/8','shortfall':str(F(3,8)-point),
          'meaning':'The same sufficient quartic estimate cannot be extended unchanged to lambda=.05. No counterexample to the probabilistic comparison.'},
        'python':sys.version},indent=2))

#!/usr/bin/env python3
"""Independent fixed rational gates; no inherited imports or cell subdivision."""
from fractions import Fraction as F
import json


def gate(u,b,r=F(1093,1000)):
    c,S=F(819,2000),F(81,80)
    A=(u**3-3*u)/6;H4=u**4-6*u*u+3
    E=u**5/4100+3*u/820+17*(3*u*u-2)/78720
    Q=-u**3+F(3,2)*r*u*u+3*b*u+F(8,875)*r
    Q1=-3*u*u+3*r*u+3*b;Q2=-6*u+3*r
    heat=F(2,5)*S**3*(A+abs(H4)/72)+S**3*E+c*Q
    signs=[Q,Q1,Q2,F(2,5)*(u*u/2+F(1,2)+F(8,875))+c*Q1,
           F(2,5)*u+c*Q2,F(2,5)-6*c]
    assert u*u>3 and A>0 and all(x<0 for x in signs) and heat<0
    return {'u':str(u),'beta_direction':str(b),'heat_upper':str(heat),
            'ray_signs':[str(x) for x in signs]}


def bernoulli(a):
    return [(-a,1/(1+a*a)),(1/a,a*a/(1+a*a))]


def main():
    l,h=F(41,100),F(42,100);vl,vh=l*(1-l),h*(1-h)
    lam=F(3,40);theta=lam/(42*vl+lam);th=F(733,100000)
    assert theta<th
    ell=F(1009,500);r=F(1093,1000);bl,bu=F(151,1000),F(187,1000)
    assert ell*ell*vh<1-th
    assert F(21,20)**2*vl>(1-2*vl)**2
    assert 24**2*vl**3>(3*(1-l)+F(3,5))**2
    assert F(21,20)+24*lam/42<r
    assert 1-2*h-2*(1-h)*th>bl and 1-2*l+2*l*th<bu
    un,up=F(459,250),F(2179,1000)
    assert un<ell*(l+F(1,2)) and up<ell*(F(3,2)-h)
    # Independent all-index Gaussian/scalar constants.
    pi_lower=16*(F(1,5)-F(1,375))-F(4,239)
    assert pi_lower>F(160,51) and pi_lower>F(25,8)
    s=F(101213,100000)
    assert s*s>F(42,41) and s*s/(s+1)-F(1,2)<F(8,875)
    assert F(81,80)**2>F(42,41) and 6**2<41
    sigma=F(3162277660,10**9);phi=F(997,2500)
    assert sigma*sigma<10 and phi*phi*F(44,7)<1
    assert (3+sigma)*phi/6>F(819,2000)
    # Actual standardized finite-law controls for the conditional cubic identity.
    laws=[('zero_noise',bernoulli(F(21,25)))]
    for delta in (F(1,1000),F(1,100),F(1,50)):
        laws.append((f'nearby_four_point_{delta}',[(x,p/2) for a in (F(21,25)-delta,F(21,25)+delta) for x,p in bernoulli(a)]))
    records=[]
    for name,law in laws:
        E=lambda f:sum(w*f(x) for x,w in law)
        assert E(lambda x:1)==1 and E(lambda x:x)==0 and E(lambda x:x*x)==1
        p=E(lambda x:int(x>0));q=1-p;v=p*q;m=E(lambda x:max(x,0));e=m/v
        U=lambda x:x/e+p-int(x>0)
        assert E(U)==0 and E(lambda x:U(x)*int(x>0))==0
        noise=E(lambda x:U(x)**2);radius=max(abs(U(x)) for x,w in law if w)
        rho=E(lambda x:abs(x)**3)
        cubic=v*(1-2*v)+3*E(lambda x:abs(int(x>0)-p)*U(x)**2)+E(lambda x:(1 if x>0 else -1)*U(x)**3)
        assert rho==e**3*cubic
        assert rho<=e**3*(v*(1-2*v)+(3*max(p,q)+radius)*noise)
        assert l<p<h and 42*noise<lam and radius<F(3,5)
        assert 1-m*m/v==noise/(v+noise)
        records.append({'name':name,'p':str(p),'lambda_at_42':str(42*noise),'amplitude':str(radius)})
    return {'status':'PASS_INDEPENDENT_LOW_NOISE_HALF_AMPLITUDE_GATES',
            'noise_ceiling':str(lam),'theta_exact_upper':str(theta),
            'simple_caps':{'theta':str(th),'ell_lower':str(ell),'rho_upper':str(r),'beta':[str(bl),str(bu)]},
            'boundaries':[gate(un,-bl),gate(up,bu)],'actual_law_controls':records,
            'new_cells_added':0,'inherited_code_imported':False,
            'scope':'Conditional on fixed-target contact, true sharp predecessor, and already acquired .6 strip/inner gap. No global theorem or new full confinement replay.'}


if __name__=='__main__':print(json.dumps(main(),indent=2))

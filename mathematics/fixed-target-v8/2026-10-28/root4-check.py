#!/usr/bin/env python3
"""Bounded independent exact original-law controls; imports no inherited kernel."""
from fractions import Fraction as F
from collections import defaultdict
import json


def expct(law, f):
    return sum((p * f(x) for x, p in law), F(0))


def geometry(law):
    assert expct(law, lambda x: 1) == 1
    assert expct(law, lambda x: x) == 0
    assert expct(law, lambda x: x*x) == 1
    u = expct(law, lambda x: max(x, 0))
    vp = expct(law, lambda x: max(x, 0)**2)
    a, b = (1-vp)/u, vp/u
    w = u/a + u/b
    reference = [(-a, u/a), (F(0), 1-w), (b, u/b)]
    rho = expct(law, lambda x: abs(x)**3)
    r = expct(reference, lambda x: abs(x)**3)
    return u, a, b, w, rho, r, reference


def convolution(law, n=4):
    # Keep count of nonnegative coordinates alongside the raw sum.
    out = {(F(0), 0): F(1)}
    for _ in range(n):
        nxt = defaultdict(F)
        for (s, j), p in out.items():
            for x, q in law:
                nxt[s+x, j+int(x >= 0)] += p*q
        out = nxt
    return out


def cdf(conv, H):
    return sum((p for (s, _), p in conv.items() if s <= H), F(0))


def controls():
    laws = [
        ('symmetric', [(F(-1), F(1,2)), (F(1), F(1,2))]),
        ('zero_contact', [(F(-5,4), F(8,25)), (F(0), F(9,25)), (F(5,4), F(8,25))]),
        ('four_point', [(F(-3,2), F(3,16)), (F(-1,2), F(5,16)),
                        (F(1,2), F(5,16)), (F(3,2), F(3,16))]),
    ]
    for t in (F(1,40), F(1,12), F(1,6)):
        law = [(F(-1), F(1,2)-t), (F(0), 3*t), (F(1), F(1,2)-3*t), (F(2), t)]
        laws.extend([(f'skew_{t}', law), (f'reflected_{t}', [(-x,p) for x,p in law])])
    counts = defaultdict(int)
    q_counterexample = None
    for name, law in laws:
        u, a, b, w, rho, r, reference = geometry(law)
        eta = rho-r
        assert eta >= 0 and rho < F(46,25) and max(abs(x) for x,_ in law) <= F(17,4)
        W = lambda x: abs(x)*(abs(x)-(b if x>0 else a))**2
        assert expct(law, W) == eta
        assert expct(law, lambda x:x**3) == b-a+expct(law, lambda x: (1 if x>0 else -1)*W(x))
        assert expct(law, lambda x:x**4) == a*a-a*b+b*b+expct(law, lambda x:(abs(x)+2*(b if x>0 else a))*W(x))
        pzero = expct(law, lambda x: int(x==0))
        pplus = expct(law, lambda x: int(x>=0))
        preflect = expct(law, lambda x: int(x<=0))
        assert preflect == 1-pplus+pzero
        if pzero:
            assert preflect != 1-pplus
            counts['reject_complementary_reflection_mass'] += 1
        assert u/b <= pplus <= 1-u/a
        if eta:
            nu = [(1 if x>0 else -1, abs(x), p*W(x)/eta)
                  for x,p in law if W(x)]
            assert sum(p for _,_,p in nu) == 1
            k0 = sum(p/((b if sig>0 else a)**2*y) for sig,y,p in nu)
            assert eta*k0 == 1-w-pzero
            for sig,c in ((1,b),(-1,a)):
                k2 = sum(p/(y-c)**2 for s,y,p in nu if s==sig)
                k1 = sum(p/(y-c) for s,y,p in nu if s==sig)
                atom = expct(law, lambda x: int(x==sig*c))
                assert eta*k2 == u-c*atom and k1 == 0
            # Polynomial coefficient version of Hermite's exact response.
            for degree in range(13):
                def response(sig,y):
                    c = b if sig>0 else a
                    f0 = F(int(degree==0))
                    fc = (sig*c)**degree
                    fp = F(0) if degree==0 else degree*sig**degree*c**(degree-1)
                    L = fc+fp*(y-c)+(f0-fc+c*fp)*(y-c)**2/c**2
                    return ((sig*y)**degree-L)/(y*(y-c)**2)
                rhs = eta*sum(p*response(sig,y) for sig,y,p in nu)
                assert rhs == expct(law, lambda x:x**degree)-expct(reference, lambda x:x**degree)
                counts['polynomial_common_measure_identities'] += 1
        else:
            assert all(not p or x in (-a,F(0),b) for x,p in law)
            counts['zero_excess_contact_cases'] += 1
        conv = convolution(law)
        rconv = convolution(reference)
        reflected = convolution([(-x,p) for x,p in law])
        thresholds = sorted(set(s for s,_ in conv) | {F(-4),F(25,8),F(0)})
        thresholds += [(x+y)/2 for x,y in zip(thresholds, thresholds[1:])]
        masses = [sum(p for (s,k),p in conv.items() if k==j) for j in range(5)]
        from math import comb
        assert masses == [comb(4,j)*pplus**j*(1-pplus)**(4-j) for j in range(5)]
        for j,mass in enumerate(masses):
            assert mass > 0
            mu = sum(p*s/2 for (s,k),p in conv.items() if k==j)/mass
            var = sum(p*(s/2-mu)**2 for (s,k),p in conv.items() if k==j)/mass
            vp, vm = u*b, u*a
            formula_mu = u*(j-4*pplus)/(2*pplus*(1-pplus))
            formula_var = (j*(vp/pplus-u*u/pplus**2)+(4-j)*(vm/(1-pplus)-u*u/(1-pplus)**2))/4
            assert mu==formula_mu and var==formula_var and var >= 0
            counts['conditional_moment_pairs'] += 1
            for H in thresholds:
                actual = sum(p for (s,k),p in conv.items() if k==j and s<=H)/mass
                bound = F(1) if H/2>=mu else var/(var+(mu-H/2)**2)
                assert actual <= bound
                counts['conditional_cantelli_events'] += 1
        for H in thresholds:
            atom = sum(p for (s,_),p in conv.items() if s==H)
            assert cdf(reflected,-H) == 1-cdf(conv,H)+atom
            if atom:
                counts['closed_threshold_collisions'] += 1
            if name=='four_point' and F(-4)<=H<=F(25,8) and cdf(conv,H)>cdf(rconv,H) and q_counterexample is None:
                q_counterexample = {'raw_H':str(H),'actual_CDF':str(cdf(conv,H)),
                    'reference_CDF':str(cdf(rconv,H)), 'rho':str(rho),'eta':str(eta)}
        counts['actual_laws'] += 1
    assert q_counterexample is not None
    # The same canonical point is not an iid convolution specification for a dependent vector.
    iid = cdf(convolution(laws[0][1]), F(-2))
    assert iid==F(5,16) and F(1,2)>iid
    # Exact midpoint error and raw-factor mutation.
    N=256
    midpoint = sum(F(2*j+1,2*N)**2 for j in range(N))/N
    assert F(1,3)-midpoint == F(1,12*N*N)
    assert 2*(F(1,3)-midpoint) == F(2,12*N*N)
    assert 2*(F(1,3)-midpoint) > F(2,24*N*N)
    # Sharp chord error for curvature M=(B+1/4)/2.
    h,B=F(1,8),F(6)
    M=(B+F(1,4))/2
    bump=M*(h/2)*(h-h/2)/2
    assert bump==h*h*(B+F(1,4))/16 and bump>h*h*(B+F(1,4))/32
    for n in (1,2,7,256):
        ordinary=first=intersection=F(0)
        def po(x):return x**3/3-x**4/4+x*x/6
        def pf(x):return x*x/4+x**3/6-x**4/4
        for j in range(n):
            l,r0=F(j,n),F(j+1,n)
            d,e=po(r0)-po(l),pf(r0)-pf(l)
            assert d>0 and e>0
            ordinary+=d;first+=e;intersection+=min(d,e)
        assert ordinary==F(1,4) and first==F(1,6) and intersection<=F(1,6)
    # Reference Gaussian tail: pi<22/7 -> phi(0)>997/2500.
    philow=F(997,2500)
    assert philow**2*F(44,7)<1
    x=F(25,16)
    tail=F(1,2)+philow*(x-x**3/6+x**5/40-x**7/336)
    assert tail>F(4,5)
    assert 42*F(9,4)+108*5+24*F(33,2)==F(2061,2)
    assert F(2061,2)/12==F(687,8)
    # Wrong normalization of a negative numerator changes the bound direction.
    assert -F(1)/F(3,2)>-F(1)/F(1)
    return {'status':'PASS_BOUNDED_EXACT_ROOT4_PHYSICAL_CONTROLS',
        'counts':dict(counts),'Q_only_replacement_counterexample':q_counterexample,
        'iid_required_control':{'dependent_all_equal_CDF':'1/2','iid_CDF':str(iid),'raw_H':'-2'},
        'tail_Phi_lower':str(tail),
        'negative_controls':['Q-only CDF replacement','complementary reflected sign mass',
            'dependent vector with iid binomial weights','half-sized raw midpoint reserve',
            'half-sized H chord reserve','lower-only denominator for negative numerator'],
        'source_imports':False,'native_ROOT4_executed':False,'complete_C4_claim':False}


if __name__=='__main__':
    print(json.dumps(controls(),indent=2,sort_keys=True))

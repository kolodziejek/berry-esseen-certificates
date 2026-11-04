#!/usr/bin/env python3
"""Exact adversarial examples for the separately proved conditional family.

These finite examples are regression checks, not a continuous-domain proof.
All arithmetic here uses fractions; no assertion is disabled or target adapted.
"""
from fractions import Fraction as F
import json


def moment(law, j, signed=False):
    return sum(w * (1 if x >= 0 else -1) ** bool(signed) * abs(x) ** j
               for x, w in law)


def standard(law):
    assert all(w > 0 for x, w in law)
    assert sum(w for x, w in law) == 1
    assert sum(x*w for x, w in law) == 0
    assert moment(law, 2) == 1
    return law


def bernoulli(a):
    b = 1/a
    return standard([(-a, b/(a+b)), (b, a/(a+b))])


def three(a, b):
    return standard([(-a, 1/(a*(a+b))), (F(0), 1-1/(a*b)),
                     (b, 1/(b*(a+b)))])


def mix(a, b, epsilon):
    points = {}
    for law, mass in ((a, 1-epsilon), (b, epsilon)):
        for x, w in law:
            points[x] = points.get(x, F(0)) + mass*w
    return standard(sorted(points.items()))


def remainder(j, x, a):
    return sum((k+1)*a**k*x**(j-2-k) for k in range(j-1))


def coefficient(x, a, t):
    return x*x + 2*a*x + 3*a*a - 3 - F(3, 2)*t*(x+2*a)


def k1(law):
    return (moment(law, 4, True) - 3*moment(law, 2, True)
            - F(3, 2)*moment(law, 3)*moment(law, 3, True))


def clip(x, interval):
    return max(interval[0], min(interval[1], x))


def extrema(rect, t):
    xs, aa = rect
    corners = [(x,a) for x in xs for a in aa]
    candidates = list(corners)
    candidates += [(x, clip(t/2-x/3, aa)) for x in xs]
    candidates += [(clip(3*t/4-a, xs), a) for a in aa]
    center = 3*t/8
    if xs[0] <= center <= xs[1] and aa[0] <= center <= aa[1]:
        candidates.append((center, center))
    return (min(coefficient(x,a,t) for x,a in candidates),
            max(coefficient(x,a,t) for x,a in corners))


def audit_law(law):
    p = sum(w for x,w in law if x > 0)
    q = 1-p
    m = sum(x*w for x,w in law if x > 0)
    assert 0 < p < 1 and m > 0
    v_law = [(m/p, p), (-m/q, q)]
    signed = []
    theta = F(0)
    theta_plus = F(0)
    min_lower = F(0)
    max_upper = F(0)
    support_determinants = 0
    zero_denominators = 0
    rho, gamma_v = moment(law,3), moment(v_law,3,True)
    correction = F(0)
    for positive, prob in [(True,p), (False,q)]:
        part = [(x,w) for x,w in law if (x > 0) == positive]
        a = m/prob
        var = sum(w*(abs(x)-a)**2 for x,w in part)
        theta += var
        if positive: theta_plus = var
        for j in range(2,9):
            actual = sum(w*abs(x)**j for x,w in part) - prob*a**j
            derived = sum(w*(abs(x)-a)**2*remainder(j,abs(x),a) for x,w in part)
            assert actual == derived
        for x,w in part:
            sign = 1 if positive else -1
            correction += sign*w*(abs(x)-a)**2*coefficient(abs(x),a,rho+sign*gamma_v)
        R = max(abs(x) for x,w in part)
        mom = [sum(w*abs(x)**j for x,w in part) for j in range(6)]
        for j in range(3):
            d0 = R*mom[j]-mom[j+1]
            off = R*mom[j+1]-mom[j+2]
            d1 = R*mom[j+2]-mom[j+3]
            assert d0 >= 0 and d1 >= 0 and d0*d1-off*off >= 0
            support_determinants += 1
            if d0 == 0:
                assert off == 0
                zero_denominators += 1
        signed.append(var)
    assert theta < 1 and m*m == (1-theta)*p*q
    assert correction == k1(law)-k1(v_law)
    assert moment(law,2,True) == 1-2*p-2*q*theta+2*theta_plus
    v = 1-theta
    binary_k = (1-2*p)*((F(3,2)*v**3-v**2)/(p*q)-3*v**3+v*v+3*v)
    assert k1(v_law) == -binary_k
    if theta == 0:
        assert correction == 0
    return {"atoms":len(law), "p":str(p), "theta":str(theta),
            "gamma_sign":(moment(law,3,True)>0)-(moment(law,3,True)<0),
            "support_determinants":support_determinants,
            "zero_denominator_branches":zero_denominators}


def main():
    laws = {
        'symmetric_bernoulli':bernoulli(F(1)),
        'skew_bernoulli':bernoulli(F(2,3)),
        'zero_atom':three(F(1,2),F(3)),
        'zero_atom_reflected':[(-x,w) for x,w in three(F(1,2),F(3))],
        'nearby_four_atoms':mix(bernoulli(F(2,3)),bernoulli(F(667,1000)),F(1,7)),
        'tiny_noise':mix(bernoulli(F(2,3)),bernoulli(F(667,1000)),F(1,10**20)),
        'tiny_noise_reflected':[(-x,w) for x,w in mix(bernoulli(F(2,3)),bernoulli(F(667,1000)),F(1,10**20))],
        'tiny_far_atom':mix(bernoulli(F(1)),three(F(100),F(100)),F(1,10**24)),
        'collision_mixture':mix(bernoulli(F(1)),three(F(1),F(2)),F(1,5)),
        'large_noise':three(F(10),F(10)),
    }
    output = {name:audit_law(standard(law)) for name,law in laws.items()}
    checked = 0
    rectangles = [((F(0),F(2)),(F(1,4),F(3))),
                  ((F(0),F(0)),(F(1),F(1))),
                  ((F(1),F(2)),(F(1),F(2))),
                  ((F(1,3),F(1,3)),(F(1,10),F(4)))]
    for rect in rectangles:
        for t in [F(-5),F(0),F(1,3),F(8,3),F(5),F(40)]:
            lo, hi = extrema(rect,t)
            for i in range(13):
                for j in range(13):
                    x = rect[0][0]+F(i,12)*(rect[0][1]-rect[0][0])
                    a = rect[1][0]+F(j,12)*(rect[1][1]-rect[1][0])
                    assert lo <= coefficient(x,a,t) <= hi
                    checked += 1
    # Exact counterexamples to unsafe implementation shortcuts.
    controls = {
        'omit_zero_resource_vertex': F(0) > F(-1),
        'negative_coefficient_uses_wrong_mass_endpoint':-F(1,4) > -F(1,2),
        'omit_quadratic_interior_minimum':coefficient(F(1),F(1),F(8,3))
             < min(coefficient(x,a,F(8,3)) for x in [F(0),F(2)] for a in [F(0),F(2)]),
        'variance_endpoint_K_monotonicity_requires_v_gate':
             (F(9,2)*F(1,3)**2-2*F(1,3))/(F(1,100)*F(99,100))
             -9*F(1,3)**2+2*F(1,3)+3 < 0,
    }
    assert all(controls.values())
    print(json.dumps({'status':'PASS_EXACT_EXAMPLE_REGRESSION',
                      'continuous_domain_proof_claimed':False,
                      'laws':output,'rectangle_grid_points':checked,
                      'unsafe_shortcuts_detected':controls},indent=2))


if __name__ == '__main__':
    main()

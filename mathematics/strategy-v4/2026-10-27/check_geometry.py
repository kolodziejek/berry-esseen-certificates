"""Bounded independent algebra and finite-law controls; not an all-law proof."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import platform
from math import comb
from itertools import product


def finite_law(xs, ps):
    assert sum(ps) == 1 and all(p > 0 for p in ps)
    mean = sum(x*p for x, p in zip(xs, ps))
    ys = [x-mean for x in xs]
    var = sum(p*y*y for y, p in zip(ys, ps))
    assert var > 0
    m = sum(p*max(y, 0) for y, p in zip(ys, ps))
    rho = sum(p*abs(y)**3 for y, p in zip(ys, ps))
    gamma = sum(p*y**3 for y, p in zip(ys, ps))
    points = sorted(set(ys))
    gap = sum(sum(p*y for y,p in zip(ys,ps) if y >= b)*(b-a)**2
              for a,b in zip(points, points[1:]))
    circle = rho*rho-gamma*gamma-4*m*m*var*var
    gap_residual = rho+2*m*var-gap
    assert circle >= 0 and gap_residual >= 0
    return dict(circle=str(circle), gap_residual=str(gap_residual),
                zero_circle=circle == 0, zero_gap=gap_residual == 0,
                rejects_J_le_rho=gap > rho)


def main():
    laws = [([F(-1), F(1)], [F(1,2), F(1,2)]),
            ([F(-2), F(1)], [F(1,3), F(2,3)]),
            ([F(-1), F(0), F(1)], [F(1,20), F(9,10), F(1,20)]),
            ([F(-1), F(1,1000), F(1)], [F(1,20), F(9,10), F(1,20)]),
            ([F(-20), F(0), F(20)], [F(1,800), F(399,400), F(1,800)]),
            ([F(-1), F(1), F(10**6)], [F(1,2), F(1,2)-F(1,10**20), F(1,10**20)]),
            ([F(-3), F(-1), F(2), F(5)], [F(1,8), F(3,8), F(3,8), F(1,8)])]
    law_results = [finite_law(*law) for law in laws]
    assert all(x['zero_circle'] and x['zero_gap'] for x in law_results[:2])
    assert all(not x['zero_circle'] for x in law_results[2:])
    assert law_results[0]['rejects_J_le_rho']
    # Exact polynomial identity tests. Degree bounds are separately stated:
    # evaluating degree <= j in each variable on j+1 distinct values is unisolvent.
    for j in range(2, 8):
        for x, a in product(map(F, range(j+1)), repeat=2):
            response = sum((k+1)*a**k*x**(j-2-k) for k in range(j-1))
            assert x**j-a**j-j*a**(j-1)*(x-a)-(x-a)**2*response == 0
        for a in map(F, range(j+1)):
            diagonal = sum((k+1)*a**(j-2) for k in range(j-1))
            assert diagonal == F(j*(j-1),2)*a**(j-2)
    # Weighted-budget identity: degree <=2 in each of a,b,A,B and <=1 in sigma.
    # The common factor m is cancelled on both sides.
    for a,b,A,B,sigma in product(range(3),range(3),range(3),range(3),range(2)):
        old = (sigma-1)*b*b+(sigma+1)*a*a-6*A*B+6*B*(b-B)+6*A*(a-A)
        new = ((sigma-1)*b*b+(sigma+1)*a*a-6*a*b
               +6*((A+B)*(a-A+b-B)+(a-A)*(b-B)))
        assert old == new
    # Arithmetic in Q[sqrt(10)] retains the exact irrational coefficients.
    def add(a,b): return (a[0]+b[0],a[1]+b[1])
    def mul(a,b): return (a[0]*b[0]+10*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    def scale(a,b): return (a[0]*b,a[1]*b)
    sigma=(F(0),F(1)); pstar=(F(2),F(-1,2))
    # Degree <=2 in p; three rational values verify each reduced coefficient.
    for p in map(F,range(3)):
        square=mul(add((p,F(0)),scale(pstar,-1)),add((p,F(0)),scale(pstar,-1)))
        lhs=add(scale(add(sigma,(F(1),F(0))),p*p),
                add(scale(add(sigma,(F(-1),F(0))),(1-p)**2),(-6*p*(1-p),F(0))))
        assert lhs == mul((F(6),F(2)),square)
        lhs_margin=add(scale((F(3),F(1)),p*p+(1-p)**2),(-4+2*p,F(0)))
        assert lhs_margin == mul((F(6),F(2)),square)
    # Polynomial coefficients in g,d of the integral power remainder.
    for n in range(2, 101):
        for k in range(n-1):
            assert F(n*(n-1)*comb(n-2,k),(k+1)*(k+2)) == comb(n,k+2)
    # A linearized convolution is not an identity: retain the quadratic term.
    assert (F(1,2)+F(1,10))**2-F(1,2)**2-2*F(1,2)*F(1,10) == F(1,100)
    here = Path(__file__).resolve()
    print(json.dumps(dict(status='PASS_BOUNDED_GEOMETRY_CONTROLS',
       mathematical_scope='Algebraic identities and seven finite laws; continuous proofs are in geometry.tex and the manuscript.',
       python=platform.python_version(), arithmetic='fractions.Fraction; unisolvent polynomial grids and coefficient identities',
       source_sha256=sha256(here.read_bytes()).hexdigest(), finite_laws=law_results,
       powers_checked=list(range(2,101)), taylor_degrees=list(range(2,8)),
       negative_controls=['J <= rho rejected on symmetric Bernoulli',
                          'no quadratic convolution remainder rejected']), indent=2))


if __name__ == '__main__':
    main()

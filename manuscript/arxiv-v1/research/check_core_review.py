#!/usr/bin/env python3
"""Bounded exact diagnostics for core manuscript identities; not a proof engine.

Only standard-library rational arithmetic. No inherited executable is imported.
The continuum arguments and limits are reviewed separately in core-review.md.
"""
from fractions import Fraction as F
from math import comb
from collections import defaultdict
from itertools import product
import json


def need(ok, message):
    if not ok:
        raise AssertionError(message)


def merge(items):
    out = defaultdict(F)
    for x, w in items:
        out[x] += w
    return dict(sorted((x, w) for x, w in out.items() if w))


def two(a):
    return {-a: 1/(1+a*a), 1/a: a*a/(1+a*a)}


def mix(a, b, w):
    return merge([(x, w*p) for x, p in two(a).items()]
                 + [(x, (1-w)*p) for x, p in two(b).items()])


def moment(law, j):
    return sum(w*x**j for x, w in law.items())


def conv(a, b):
    return merge((x+y, p*q) for x, p in a.items() for y, q in b.items())


def power(a, n):
    out = {F(0): F(1)}
    for _ in range(n):
        out = conv(out, a)
    return out


def cdf(a, t):
    return sum(p for x, p in a.items() if x <= t)


def surd_ge_zero(a, b):
    """Exact sign of a + b sqrt(10), without numerical square roots."""
    if a >= 0 and b >= 0:
        return True
    if a <= 0 and b <= 0:
        return a == b == 0
    return a*a >= 10*b*b if a >= 0 else 10*b*b >= a*a


laws = {
    'symmetric': two(F(1)),
    'skew': two(F(2)),
    'nearby_four': mix(F(1), F(101, 100), F(2, 5)),
    'nearby_skew_four': mix(F(4, 3), F(27, 20), F(3, 7)),
    'remote_tiny': mix(F(1), F(1000), 1-F(1, 10**6)),
    'remote_reflected': mix(F(1), F(1, 1000), 1-F(1, 10**6)),
    'three_with_zero': {F(-2): F(1, 6), F(0): F(1, 2), F(1): F(1, 3)},
    'four_wide': mix(F(1, 3), F(3), F(1, 2)),
}
counts = defaultdict(int)
for name, law in laws.items():
    need(sum(law.values()) == 1 and moment(law, 1) == 0
         and moment(law, 2) == 1, name + ': standardization')
    p = sum(w for x, w in law.items() if x > 0)
    q, v = 1-p, p*(1-p)
    m = sum(w*x for x, w in law.items() if x > 0)
    ell = m/v
    u0 = merge(((x/ell+p), w/q) for x, w in law.items() if x <= 0)
    u1 = merge(((x/ell-(1-p)), w/p) for x, w in law.items() if x > 0)
    w0, w1 = moment(u0, 2), moment(u1, 2)
    mu0, mu1 = moment(u0, 3), moment(u1, 3)
    s = q*w0+p*w1
    rho = sum(w*abs(x)**3 for x, w in law.items())
    gamma = moment(law, 3)
    beta = sum(w*x*abs(x) for x, w in law.items())
    need(rho/ell**3 == v*(1-2*v)+3*v*(w0+w1)-q*mu0+p*mu1,
         name + ': rho conditional expansion')
    need(gamma/ell**3 == v*(q-p)+3*v*(w1-w0)+q*mu0+p*mu1,
         name + ': gamma conditional expansion')
    need(beta/ell**2 == v*(q-p)+p*w1-q*w0, name + ': beta expansion')
    J = F(0)
    xs = list(law)
    for a, b in zip(xs, xs[1:]):
        tau = sum(w*x for x, w in law.items() if x >= b)
        J += tau*(b-a)**2
    Da, Db = 3*rho-gamma-3*J, rho
    need(surd_ge_zero(Da, Db), name + ': nonnegative defect')
    if 0 in law:
        need(surd_ge_zero(Da+rho, Db-rho), 'zero in support defect floor')
    else:
        A = -max(x for x in law if x < 0)
        B = min(x for x in law if x > 0)
        pos3 = sum(w*x**3 for x, w in law.items() if x > 0)
        neg3 = sum(w*(-x)**3 for x, w in law.items() if x < 0)
        Tp, Tm = pos3-m*B*B, neg3-m*A*A
        Jo = J-m*(A+B)**2
        decomp_a = m*(A*A-B*B-6*A*B)-Tp+Tm+3*(Tp+Tm-Jo)
        decomp_b = m*(A*A+B*B)+Tp+Tm
        need((Da, Db) == (decomp_a, decomp_b), name + ': defect identity')
        ba, bb = m/q, m/p
        da, db = ba-A, bb-B
        theta_p = sum(w*(x-bb)**2 for x, w in law.items() if x > 0)
        theta_m = sum(w*(x+ba)**2 for x, w in law.items() if x < 0)
        rhs_a = m*(-bb*bb+ba*ba-6*ba*bb)+6*m*((A+B)*(da+db)+da*db)
        rhs_a += 3*B*theta_p+9*A*theta_m
        rhs_b = m*(bb*bb+ba*ba)+3*B*theta_p+3*A*theta_m
        need(surd_ge_zero(Da-rhs_a, Db-rhs_b), name + ': simultaneous budget')
    counts['marginal_laws'] += 1

    # Closed collisions and midpoint thresholds, with the exact actual marginal.
    for n in [2, 3, 4]:
        actual = power(law, n)
        for k in range(n+1):
            W = conv(power(u1, k), power(u0, n-k))
            need(moment(W, 2) == n*s+(k-n*p)*(w1-w0), 'own-count variance')
            for u in [F(-1, 2), F(0), F(1, 2)]:
                H = ell*(k+u-n*p)
                count_value = F(0)
                outgoing = incoming = F(0)
                for j in range(n+1):
                    mass = F(comb(n,j))*p**j*q**(n-j)
                    Z = conv(power(u1,j), power(u0,n-j))
                    val = cdf(Z,k+u-j)
                    count_value += mass*val
                    if j <= k:
                        outgoing -= mass*(1-val)
                    else:
                        incoming += mass*val
                need(count_value == cdf(actual,H), 'count identity at closed event')
                FB = sum(F(comb(n,j))*p**j*q**(n-j) for j in range(k+1))
                need(count_value-FB == outgoing+incoming, 'signed count identity')
                counts['count_collision_cases'] += 1

    # Full independent coupling, only when the acquired-gap hypothesis holds.
    a0, a1 = max(u0), -min(u1)
    c = 1-a0-a1
    if not F(1,2) < c <= 1:
        continue
    n = 3
    au = max(abs(x) for x in list(u0)+list(u1))
    for k in range(n+1):
        t = (n-k)*w0+k*w1
        for u in [F(-1,2), F(0), F(1,2)]:
            ep = e2 = e3 = cutoff_cdf = F(0)
            for atoms in product(list(u0.items()), repeat=n):
                for atoms1 in product(list(u1.items()), repeat=n):
                    weight = F(1)
                    for _, w in atoms+atoms1:
                        weight *= w
                    ws = [sum(x for x,_ in atoms1[:j])+sum(x for x,_ in atoms[j:])
                          for j in range(n+1)]
                    cutoff = None
                    for j in range(-20,n+21):
                        wj = ws[min(n,max(0,j))]
                        if j+wj <= k+u:
                            cutoff = j
                    need(cutoff is not None and cutoff < n+20, 'bounded enumeration covers cutoff')
                    R = cutoff-k
                    ep += weight*max(R,0)
                    h = max(-R,0)
                    e2 += weight*(comb(h,2) if h >= 2 else 0)
                    e3 += weight*(comb(h,3) if h >= 3 else 0)
                    cutoff_cdf += weight*sum(F(comb(n,j))*p**j*q**(n-j)
                        for j in range(n+1) if j <= cutoff)
            need(ep <= t/(c-u)**2, 'positive crossing bound')
            need(e2 <= t/(c+min(u,c/3))**2, 'second crossing bound')
            need((e3*(2*c-F(1,2))**3)**2 <= t*t*(au*au+3*t), 'third crossing bound')
            need(cutoff_cdf == cdf(power(law,n),ell*(k+u-n*p)), 'whole-count coupling')
            counts['whole_count_cases'] += 1

for n in range(1,9):
    for p in [F(1,10),F(1,3),F(1,2),F(2,3),F(9,10)]:
        q=1-p
        masses=[F(comb(n,j))*p**j*q**(n-j) for j in range(n+1)]
        def FB(k):
            return sum(masses[:max(0,min(n+1,k+1))])
        for k in range(n+1):
            chi=(n+1)*p-k
            if chi >= 2:
                continue
            for r in range(-n-4,n+5):
                h=max(-r,0)
                rhs=max(chi-1,0)*max(r,0)+max(chi,0)*(comb(h,2) if h>=2 else 0)
                rhs += comb(h,3) if h>=3 else 0
                need(FB(k+r)-FB(k)-r*masses[k] <= max(masses)*rhs/((n+1)*p*q),
                     'discrete binomial curvature')
                counts['discrete_curvature_cases'] += 1

# Atom convention negative control: replacing the strict outgoing event by
# a closed event is detectably false at a Bernoulli count plane.
need(cdf({F(0):F(1)},F(0)) == 1, 'collision fixture')
need(-F(1,2)*cdf({F(0):F(1)},F(0)) != 0, 'wrong closed outgoing event rejected')
counts['negative_controls'] += 1
need(F(3003,10250) < F(3,10) and F(73,175) < F(2113,5000), 'entry reserves')
need(F(3,10)-F(3003,10250) == F(36,5125), 'first exact reserve')
need(F(2113,5000)-F(73,175) == F(191,35000), 'second exact reserve')
print(json.dumps({'result':'PASS','counts':dict(counts),
 'scope':'Finite exact diagnostics only; analytic continuum and compactness arguments are reviewed in prose.'},indent=2))

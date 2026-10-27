"""Bounded rational checks for the retained-support exposition.

This checks displayed algebra/constants and selected false-rule controls.
It does not execute a native certificate or validate any support-row cover.
"""
from fractions import Fraction as F
from math import comb, factorial
import json


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(a, c):
    return {k: v*c for k, v in a.items() if v*c}


def h_minus_t(m):
    return {(m-i, i): F(comb(m, i)*(-1)**i) for i in range(m+1)}


def rising(x, m):
    y = F(1)
    for i in range(m):
        y *= x+i
    return y


def coefficient(j):
    """Extract z^(j+1) from the four analytic terms of S(z)."""
    degree = j+1
    ans = {}
    for k in range(degree+1):
        c = F((-1)**k, 2**k*factorial(k)*(2*k+1))
        q = c*rising(F(2*k+1, 2), degree-k)/factorial(degree-k)
        ans = add(ans, scale(h_minus_t(2*k+1), q))
    c = F((-1)**degree, 2**degree*factorial(degree)*(2*degree+1))
    ans = add(ans, {(2*degree+1, 0): -c})
    ans = add(ans, {(2*degree, 1): F((-1)**degree, 2**degree*factorial(degree))})
    q = F((-1)**(degree-1), 2**degree*factorial(degree-1))
    ans = add(ans, {(2*degree-1, 2): q, (2*degree-1, 0): -q})
    return ans


def expect_failure(predicate):
    if predicate:
        raise AssertionError("false-rule control was accepted")


def main():
    c = F(48, 125)
    def bracket(x):
        return 2*c-F(3,4)-(c+F(1,4))*x+(c*c-c)*x*x-c*c*x*x*x
    assert bracket(F(1,36)) == F(823,4050000)
    assert bracket(F(1,36)) > 0
    expect_failure(bracket(F(1,35)) > 0)

    pi_upper = 16*(F(1,5)-F(1,3*5**3)+F(1,5*5**5))-4*(F(1,239)-F(1,3*239**3))
    assert pi_upper < F(22,7)
    assert F(997,2500)**2 < F(7,44)
    assert sum((F(1, factorial(k)) for k in range(4)), F(0)) == F(8,3) > F(64,25)
    assert sum((F(3,2)**k/factorial(k) for k in range(5)), F(0)) > F(21,5)
    assert F(3) < F(7,4)**2
    assert F(25,128) < F(1,4)  # [5/(8 sqrt(2))]^2 < (1/2)^2
    e_upper = sum((F(1,factorial(k)) for k in range(7)), F(0)) + F(1,factorial(7))*F(8,7)
    assert e_upper < F(193,71)

    p0 = {(0,3): F(1,6), (0,1): F(-1,2)}
    p1 = {(2,1): F(3,4), (2,3): F(-1,4),
          (1,4): F(1,8), (1,2): F(-3,4), (1,0): F(3,8),
          (0,5): F(-1,40), (0,3): F(1,4), (0,1): F(-3,8)}
    assert coefficient(0) == p0
    assert coefficient(1) == p1
    expect_failure(coefficient(0) == scale(p0, -1))
    # Derivative coefficients after independent spatial/variance collection.
    f4 = {4: F(1,24), 0: F(-1,8)+F(1,4), 2: F(-1,4)}
    f5 = {5: F(-1,120), 1: F(1,8)}
    assert f4 == {4: F(1,24), 2: F(-6,24), 0: F(3,24)}
    assert f5 == {5: F(-1,120), 1: F(15,120)}
    expect_failure(f5 == {5: F(-1,120)})

    n=27
    upper_s=F(1019049330731,10**12)
    upper_e=F(14331929737,10**12)
    score=F(8171,18000)
    rho=F(6413121,5478500)
    beta=F(326352124353,10**12)
    assert upper_s**2 > F(n,n-1)
    assert upper_e == n*(upper_s-1)-F(1,2)
    assert score == F(819,2000)+F(2,45)
    rho_from_caps=min(F(3031,10000)*F(646,1000)/(score-F(3031,10000)),
                      F(3322,10000)*F(429,1000)/(score-F(3322,10000)))
    assert rho >= rho_from_caps
    assert (1+beta**2)**2 > rho**2*(1-beta**2)

    # The favorable fifth-order term must use the UPPER index endpoint.
    u=F(3)
    d36=(u**5-15*u)/(120*35)
    d48=(u**5-15*u)/(120*47)
    assert d36>d48>0
    expect_failure(-3*d48 <= -3*d36)
    ell=F(-6)
    assert ell**2<=41
    expect_failure(ell>0 and 1/ell>0)
    print(json.dumps({
        "status":"PASS_BOUNDED_RETAINED_SUPPORT_IDENTITIES",
        "scope":"rational algebra/constants only; no support-row or native certificate acceptance",
        "series_nonzero_coefficients":[len(coefficient(j)) for j in range(6)],
        "negative_controls": ["wrong floor35", "reversed leading series sign", "missing fifth-term correction", "favorable term frozen at lower index", "negative square-root surrogate"],
        "index27_scale_and_moment_constants":"checked",
        "scale36_margin":str(bracket(F(1,36)))
    },indent=2))


if __name__ == "__main__":
    main()

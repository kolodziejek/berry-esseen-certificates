#!/usr/bin/env python3
"""Bounded exact review checks; no manuscript/native certificate code imported.

The continuous-domain maximum argument is in revision3-independent-review.md.
This script checks its polynomial derivative identities and elementary rational
constant comparisons, not analytic coverage of the local-exclusion package.
"""

from fractions import Fraction as F


# Sparse polynomials in (b,c,u), independently differentiated below.
def poly(value):
    return {(0, 0, 0): F(value)} if value else {}


def add(*terms):
    out = {}
    for term in terms:
        for e, a in term.items():
            out[e] = out.get(e, F(0)) + a
    return {e: a for e, a in out.items() if a}


def scale(a, p):
    return {e: F(a) * v for e, v in p.items() if a * v}


def mul(p, q):
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            key = tuple(x + y for x, y in zip(e, f))
            out[key] = out.get(key, F(0)) + a * b
    return {e: a for e, a in out.items() if a}


def du(p):
    return {(e[0], e[1], e[2] - 1): a * e[2]
            for e, a in p.items() if e[2]}


def evaluate(p, values):
    return sum(a * values[0] ** e[0] * values[1] ** e[1]
               * values[2] ** e[2] for e, a in p.items())


def rational_derivative(numerator, denominator, power):
    # d(N / D**power) = (N' D - power N D') / D**(power+1).
    return add(mul(du(numerator), denominator),
               scale(-power, mul(numerator, du(denominator))))


b = {(1, 0, 0): F(1)}
c = {(0, 1, 0): F(1)}
u = {(0, 0, 1): F(1)}
one = poly(1)
p = add(b, u, scale(-1, one))
d = add(c, scale(-1, u))
r1 = rational_derivative(p, d, 2)
r2 = rational_derivative(r1, d, 3)
assert r1 == add(scale(2, b), u, c, poly(-2))
correct_r2 = scale(2, add(scale(3, b), poly(-3), u, scale(2, c)))
old_r2 = scale(2, add(scale(3, b), poly(-3), scale(2, u), c))
assert r2 == correct_r2
assert add(r2, scale(-1, old_r2)) == scale(2, d)
assert correct_r2 == scale(2, add(scale(3, p), scale(2, d)))
point = (F(1), F(3, 4), F(1, 4))
assert evaluate(p, point) > 0
correct_value = evaluate(r2, point) / evaluate(d, point) ** 4
old_value = evaluate(old_r2, point) / evaluate(d, point) ** 4
assert (correct_value, old_value) == (56, 40)
print("PASS r' and corrected r'' by exact polynomial differentiation")
print("NEGATIVE CONTROL old r'' at b=1,c=3/4,u=1/4: old=40, actual=56")

q = add(b, u)
e = add(c, u)
g1 = rational_derivative(q, e, 2)
g2 = rational_derivative(g1, e, 3)
assert g1 == add(c, scale(-2, b), scale(-1, u))
assert g2 == scale(2, add(scale(3, b), u, scale(-2, c)))
print("PASS g' and g'' by exact polynomial differentiation")

# At u=c/3, the derivative jump has denominator (4c/3)^3.
jump_numerator = add(scale(F(4, 3), c),
                     scale(-1, add(scale(F(2, 3), c), scale(-2, b))))
assert jump_numerator == scale(2, add(b, scale(F(1, 3), c)))
print("PASS cap derivative-jump numerator = 2(b+c/3)")


def atan_interval(x, even_terms):
    assert 0 < x < 1 and even_terms > 0 and even_terms % 2 == 0
    low = sum((-1) ** j * x ** (2*j + 1) / (2*j + 1)
              for j in range(even_terms))
    return low, low + x ** (2*even_terms + 1) / (2*even_terms + 1)


# Alternating integrated geometric series and Machin's identity give this
# rational interval for pi; their analytic proof is recorded in the review.
al, ah = atan_interval(F(1, 5), 32)
bl, bh = atan_interval(F(1, 239), 12)
pi_l, pi_h = 16*al - 4*bh, 16*ah - 4*bl
assert F("3.141592653589793") < pi_l < pi_h < F("3.141592653589794")
assert pi_l > F(333, 106) > F(160, 51)
assert pi_h < F(22, 7)
rl, rh = F("3.162277660"), F("3.162277661")
assert rl**2 < 10 < rh**2
ce2_l, ce2_h = (19 + 6*rl)/(72*pi_h), (19 + 6*rh)/(72*pi_l)
assert F(819, 2000)**2 < ce2_l < ce2_h < F(20487, 50000)**2
assert F("0.39886")**2 < 1/(2*pi_h) < 1/(2*pi_l) < F(2, 5)**2
assert 1/(4*pi_l) < F(2, 25)
assert 8/pi_l < F(51, 20)
print("PASS directed pi interval at 15 decimal places (32/12-term Machin bounds)")
print("PASS sqrt(10), CE, phi(0), 1/(4pi), and fifth-derivative coefficient bounds")
print("SCOPE exact algebra/constants only; no local certificate predicates executed")

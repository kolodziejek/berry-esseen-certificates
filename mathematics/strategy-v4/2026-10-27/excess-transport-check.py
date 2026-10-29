"""Exact scalar transport controls, independent of native certificate code."""
from fractions import Fraction as F
from itertools import product

# The master identity is algebraic in the three Gaussian CDF values.
# Use independent rational values, rather than approximating those functions.
count = 0
for root_n, rho, rho_b, prob, binprob, phi_h, phi_b, phi_base, c in product(
        [F(2), F(3)], [F(1), F(3,2)], [F(1), F(5,4)],
        [F(1,4), F(4,5)], [F(1,3), F(2,3)],
        [F(1,5), F(3,4)], [F(1,6), F(5,6)],
        [F(1,7), F(6,7)], [F(4095,10000),F(40974,100000)]):
    mass = F(1,11)
    a = root_n*(prob-phi_h)-c*rho
    cb = root_n*(binprob-phi_b)/rho_b
    phase = (phi_h-phi_base)/mass
    repair = root_n*(phi_b-phi_base)+c*(rho_b-rho)
    rhs = root_n*mass*((prob-binprob)/mass-phase)+repair
    assert a+rho_b*(c-cb) == rhs
    count += 1

# Low-interval corner dominance needs no upper bound on the actual score.
# Rational points sample a proof identity: the chord gap of x^2 is
# (x-lo)(hi-x); arbitrary affine terms cancel exactly.
lo, chi = F(4095,10000), F(40974,100000)
for j in range(101):
    x = lo+(chi-lo)*F(j,100)
    chord = ((chi-x)*lo*lo+(x-lo)*chi*chi)/(chi-lo)
    assert chord-x*x == (x-lo)*(chi-x) >= 0
    assert max(F(0), x-chi) == 0

# Choosing the upper coefficient for a negative gain remains essential,
# even though the multiplier is now fixed.
gain, lower, fixed, upper = F(-1,7), F(2,5), F(40973,100000), F(2113,5000)
assert lower < fixed < upper
assert upper*gain <= fixed*gain < lower*gain

print('EXACT PASS: fixed-target count master identity in', count, 'independent rational cases.')
print('EXACT PASS: low-interval chord-gap identity at 101 rational points; charge is zero.')
print('NEGATIVE CONTROL: a negative cubic gain rejects the lower multiplier as a lower bound.')
print('Scope: scalar identity/sign checks only. Finite samples do not establish general convexity or cover; those are proved in the note.')

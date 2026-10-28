"""Independent exact checks for the enlarged actual-law comparison.

Does not import or execute the constructor. Uses the original bivariate
quartics in tensor Bernstein form, independently derived interval envelopes,
and exact convolution versus conditional-count identities at atom collisions.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError("Assertions must remain enabled")
ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "runs/allpanel-review-v11-20261028/source01"
PINS = {
    "allpanel.tex": "bd9d32de7000391edbc6a94547316b7c88234cc9aaf6d2c4f4c2d2de183dbf15",
    "allpanel_check.py": "75c8e09509354ecfad9d1172b4a4f41f7b06e62195ced817b240f5471ad3d844",
}
for name, pin in PINS.items():
    assert hashlib.sha256((SOURCE/name).read_bytes()).hexdigest() == pin

A, alpha = Q(7, 10), Q(3, 5)
V, N, U = Q(3, 16), Q(42), Q(1, 500)
T = Q(23, 10500)
den = 5*alpha**4
bernstein = []
for sign, slope, width, claim in [(1, -Q(27, 25), Q(3, 2), Q(1, 4)),
                                  (-1, Q(9, 10), Q(1), Q(4, 5))]:
    # Coefficients of den*(F-claim), before any quadratic truncation.
    power = {(0, 0): 3*alpha**2-A**2-claim*den,
             (0, 1): -3, (1, 0): 2*sign*alpha**3+slope*den,
             (1, 1): -4*A, (2, 1): 3*alpha**2,
             (2, 2): -6, (4, 3): -1}
    coeff = []
    for k in range(5):
        for j in range(4):
            x = sum(c*width**i*T**t*Q(comb(k, i), comb(4, i))
                    * Q(comb(j, t), comb(3, t))
                    for (i, t), c in power.items() if i <= k and t <= j)/den
            assert x > 0
            coeff.append(x)
    bernstein.append({"sign": sign, "coefficients": coeff, "minimum": min(coeff)})
assert bernstein[0]["minimum"] == Q(10788447499, 444528000000)
assert bernstein[1]["minimum"] == Q(569, 5670)

# Independent interval envelopes with positive square-root domains exposed.
phase_low, phase_high, cut = -Q(109, 500), Q(391, 500), Q(1, 20)
D = Q(171, 100)
assert phase_high-phase_low == 1
assert Q(1, 4)+U/N < Q(501, 1000)**2
raw_scale_upper = Q(46, 25)*Q(501, 1000)
assert raw_scale_upper+phase_high < D
assert raw_scale_upper+cut < 1
assert Q(1, 4)-D/N > Q(1, 5)
assert Q(53, 100)+D/N < Q(29, 50)
assert Q(3, 5)/Q(4, 25)**2 < 24
assert Q(3, 5)/Q(4, 25) < 4
assert 1/(12*Q(4, 25)) < Q(53, 100)
assert 1/(2*V)+D**2/(2*N*V**2) < 4

def error_bound(delta):
    return 2*delta+Q(53, 100)+4*delta**3/N

normalization = []
for delta, width, mass, derivative_low, derivative_high in [
        (Q(1), cut, Q(69, 100), Q(9, 10), Q(27, 25)),
        (D, phase_high, Q(14, 25), Q(2, 3), Q(3, 2))]:
    exponent_abs = (4*U+(2*delta*width+width**2)/(2*V)+error_bound(delta))/N
    assert 0 < exponent_abs < 1
    lower_mass = 2*Q(19943, 50000)*(1-(delta**2/(2*V)+error_bound(delta))/N)
    assert lower_mass > mass
    assert 1-exponent_abs > derivative_low
    assert 1/(1-exponent_abs) < derivative_high
    normalization.append({"delta": delta, "mass_lower": lower_mass,
                          "derivative_lower": 1-exponent_abs,
                          "derivative_upper": 1/(1-exponent_abs)})
mode_factor = 1-error_bound(Q(1))/N
assert mode_factor > 0 and V*mode_factor**2 > Q(2, 5)**2
assert Q(25, 14) < Q(9, 5)
assert 1+Q(53, 100)/(N*V) < Q(107, 100)
assert 1+Q(53, 100) < 2

# Adverse moment repair and normal variance repair, without discarding either.
d = Q(17, 250)
B = Q(3, 2)*(1-2*V)+d-Q(3, 4)+3*(1-2*V)*U/(8*N*V)
assert B > 0
assert (Q(41, 100)*B)**2 < Q(4, 3)**2*V**3
assert Q(1, 5)**2 < Q(5, 2)**2*V**3
assert Q(5, 2)+Q(4, 3) < 4
assert Q(5, 2)*D+Q(4, 3) < 6
assert 1-4/N == Q(19, 21) and 1+4/N == Q(23, 21)
assert 1+4*D/N < Q(7, 6)
assert 1+8/N < Q(6, 5)
assert 1+4*(D+1)/N < Q(4, 3)

# Cantelli switch checks independently use the unscaled probability function.
z = Q(3, 2)
switch_value = (z*T)**2/(T+(z*T)**2)-Q(27, 25)*z*T
assert switch_value > T/4
assert 2*z/(1+z*z*T)**2 > Q(27, 25)
assert cut**2/(T+cut**2)-Q(27, 25)*cut > T/4
assert z*T < cut and T < cut and Q(9, 10) > Q(4, 5)

# Tail coefficients and three full phase intervals. The infinite coefficient
# ratio is proved in the report, not inferred from these finite controls.
def first(mu, h):
    a = (1-h)/A-1
    assert a > 0
    return mu**2*(Q(1, 2)+mu/6)/(a+mu)**2

def remaining(mu, h, m):
    gap = 1/A-1-h/(m*A)
    assert gap > 0 and 0 <= 3*mu < 1
    coefficient = Q(m**(m-1), __import__('math').factorial(m+1))
    return coefficient*mu**(m+1)/((gap+mu)**2*(1-3*mu))

mu_inner, mu_global = Q(6, 5)*U/A**2, Q(4, 3)*U/A**2
assert mu_inner < (1-cut)/A-1
inner_incoming = first(mu_inner, cut)+remaining(mu_inner, cut, 2)
inner_bracket = Q(19, 84)-Q(107, 100)*inner_incoming/U
assert inner_bracket > 0
inner_margin = Q(69, 100)*inner_bracket-Q(4, 42)-Q(1, 100)

total_variance = Q(7, 6)*U
assert 3*cut**2 > total_variance
negative_own = min(x*x/(total_variance+x*x)-Q(3, 2)*x
                   for x in [cut, -phase_low])
negative_bracket = negative_own-Q(9, 5)*(first(mu_global, 0)+remaining(mu_global, 0, 2))
assert negative_bracket > 0
negative_margin = Q(14, 25)*negative_bracket-6*U/N-U/100

t = Q(4, 3)*U
assert 3*(1-phase_high)**2 > t
assert 3*(2-phase_high)**2 > 2*t
positive_own_minus_first_two = min(Q(2, 3)*u-Q(9, 5)*sum(
    i*t/(i*t+(i-u)**2) for i in [1, 2]) for u in [cut, phase_high])
assert 1/A-1-phase_high/(3*A) == Q(59, 1050)
positive_bracket = positive_own_minus_first_two-Q(9, 5)*remaining(mu_global, phase_high, 3)
assert positive_bracket > 0
positive_margin = Q(14, 25)*positive_bracket-6*U/N-U/100
assert inner_margin == Q(17926467866165398367, 1060536251855551002000) > 0
assert negative_margin == Q(303207159039, 1226220050000) > 0
assert positive_margin == Q(1429750577643511489, 102275398586900550000) > 0

for i in range(2, 13):
    for P in range(81):
        assert max(P-i, 0)**2 <= (comb(P, i+1) if P >= i+1 else 0)
assert (3-1)**2 > comb(3, 2)  # The factorial hinge shortcut fails for i=1.
assert (2-phase_high)/A+2*mu_global-2 < 0  # Second outer hinge is illegal.

# Actual iid laws: direct polynomial convolution and a separately enumerated
# conditional binomial identity. Integer lattice nodes prevent rounding merges.
actual_controls = []
for p in [Q(13, 50), Q(1, 3)]:
    q = 1-p
    law = [(-1, q/2), (1, q/2), (1000, p)]
    dist = {0: Q(1)}
    for _ in range(42):
        new = {}
        for node, mass in dist.items():
            for step, weight in law:
                new[node+step] = new.get(node+step, Q(0))+mass*weight
        dist = new
    assert sum(dist.values()) == 1
    variance = p*q+q/Q(10**6)
    for phase in [phase_low, -cut, Q(0), cut, phase_high]:
        k = 14 if p == Q(1, 3) else (10 if phase == phase_high else 11)
        delta = k-42*p
        assert (delta+phase)**2 <= Q(46, 25)**2*variance
        actual_cdf = sum(m for x, m in dist.items() if x <= 1000*(k+phase))
        binomial_cdf = sum(Q(comb(42, j))*p**j*q**(42-j) for j in range(k+1))
        correction = Q(0)
        collision = Q(0)
        for j in range(43):
            pi = Q(comb(42, j))*p**j*q**(42-j)
            # Positive signs have noise zero; negative signs have +/- .001.
            M = 42-j
            conditional_cdf = sum(Q(comb(M, r), 2**M) for r in range(M+1)
                                  if Q(2*r-M, 1000) <= phase+k-j)
            correction += pi*(conditional_cdf-(1 if j <= k else 0))
            if j == k:
                collision = pi*sum(Q(comb(M, r), 2**M) for r in range(M+1)
                                   if Q(2*r-M, 1000) == phase)
        assert actual_cdf-binomial_cdf == correction
        if p == Q(1, 3) and phase == 0:
            assert collision > 0
        actual_controls.append({"p": p, "phase": phase, "k": k,
                                "own_atom_collision_mass": collision})

def encode(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x

print(json.dumps(encode({"status": "PASS_INDEPENDENT_ALLPANEL_REVIEW_CHECKS",
    "source_pins": PINS, "constructor_imported_or_executed": False,
    "bernstein": bernstein, "normalization": normalization,
    "final_margins": {"inner": inner_margin, "negative": negative_margin,
                      "positive": positive_margin},
    "actual_law_controls": actual_controls,
    "negative_controls": ["factorial_hinge_fails_at_i1", "second_outer_hinge_illegal",
                          "strict_outgoing_atom_cannot_be_closed"],
    "scope": "Exact arithmetic and actual-law controls; full analytic derivation reviewed separately"
}), indent=2))

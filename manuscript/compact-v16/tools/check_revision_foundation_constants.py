"""Exact scalar and polynomial audit of the 2026-10-29 revisions.

This program does not prove the analytical reductions, coverage of the entry
certificate, or the finite base. All computations below use Python integers
and Fraction. The formulas are derived from the displayed moment and
quadratic-form expressions, not from decimal evaluation or sampled grids.
"""
from fractions import Fraction as F
import json
import sys

if not __debug__:
    raise RuntimeError("Assertions are required; do not use -O or -OO")

checks = []
controls = []


def require(name, predicate):
    if not predicate:
        raise AssertionError(name)
    checks.append(name)


def reject(name, predicate):
    if predicate:
        raise AssertionError("Invalid control accepted: " + name)
    controls.append(name)


# Polynomials in one variable, stored in increasing powers.
def add(a, b):
    return tuple((a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b))))


def scale(a, c):
    return tuple(c*x for x in a)


def mul(a, b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return tuple(c)


def value(a, x):
    y = F(0)
    for c in reversed(a):
        y = y*x+c
    return y


def deriv(a):
    return tuple(i*a[i] for i in range(1, len(a)))


def equal(a, b):
    return all(c == 0 for c in add(a, scale(b, -1)))


def atan_sum(k, x):
    return sum(((-1)**j*x**(2*j+1)/F(2*j+1)
                for j in range(k)), F(0))


pi_lo = 16*atan_sum(10, F(1, 5))-4*atan_sum(5, F(1, 239))
pi_hi = 16*atan_sum(9, F(1, 5))-4*atan_sum(4, F(1, 239))
root_lo = F(3162277660168379, 10**15)
root_hi = F(3162277660168380, 10**15)
ce_lo = F(4097321837023, 10**13)
ce_hi = F(4097321837025, 10**13)
require("positive ordered pi endpoints", 0 < pi_lo < pi_hi)
require("sqrt10 directed squares", root_lo**2 < 10 < root_hi**2)
ce2_lo = (19+6*root_lo)/(72*pi_hi)
ce2_hi = (19+6*root_hi)/(72*pi_lo)
require("narrow CE lower bound", ce_lo**2 < ce2_lo)
require("narrow CE upper bound", ce2_hi < ce_hi**2)
reject("lower CE endpoint raised beyond upper bound", ce_hi**2 < ce2_lo)
reject("upper CE endpoint lowered beyond lower bound", ce2_hi < ce_lo**2)

# Compute det G and the adjugate quadratic form independently from entries.
g00, g01, g11 = (1, 1), (2, 1), (6, 2)
det = add(mul(g00, g11), scale(mul(g01, g01), -1))
adj_numerator = add(add(g11, g00), scale(g01, -2))
require("positive Fourier determinant coefficients", all(c > 0 for c in det))
require("Fourier adjugate numerator", equal(adj_numerator, (3, 1)))
require("Fourier L numerator from 1-xJ", equal(
    add(det, scale(mul((0, 1), adj_numerator), -1)), (2, 1)))
reject("altered Fourier numerator identity", equal(
    add(det, scale(mul((0, 1), adj_numerator), -1)), (3, 1)))

# The global minorant is established by factorization and its exact maximum.
h = (F(0), F(4, 5), F(12, 5), F(0), F(-16, 5))
h_factored = scale(mul(mul((0, 1), (1, -1)), mul((1, 2), (1, 2))), F(4, 5))
require("minorant global factorization", equal(h, h_factored))
require("minorant derivative factorization", equal(
    deriv(h), scale(mul((1, 2), (-1, -4, 8)), F(-4, 5))))
require("minorant maximum below one via sqrt3<11/6", 3 < F(11, 6)**2)
require("minorant vanishes at threshold", value(h, F(0)) == 0)

# For the t-endpoint lower quadratics, derive coefficients from alpha=1/2.
alpha, denom, A, tmax = F(1, 2), F(5, 16), F(3, 5), F(101, 10000)
minima = {}
for phase, eps, corr in [("negative", 1, F(-101, 100)),
                         ("positive", -1, F(99, 100))]:
    for t in (F(0), tmax):
        c0 = (3*alpha**2-A**2-3*t)/denom
        c1 = 2*eps/(5*alpha)+corr-4*A*t/denom
        c2 = (3*alpha**2*t-6*t*t-F(9, 4)*t**3)/denom
        quadratic = (c0, c1, c2)
        require(f"{phase} {t}: nonnegative quadratic coefficient", c2 >= 0)
        if phase == "negative":
            require(f"{phase} {t}: decreasing quadratic", c1+3*c2 < 0)
            lower = value(quadratic, F(3, 2))
        else:
            require(f"{phase} {t}: increasing quadratic", c1 > 0)
            lower = value(quadratic, F(0))
        require(f"{phase} {t}: minimum greater than 3/5", lower > F(3, 5))
        minima[f"{phase};t={t}"] = str(lower)
reject("overstated 4/5 small-noise minimum", F(minima[f"negative;t={tmax}"]) > F(4, 5))

# Reconstruct both original error polynomials; then compare coefficients.
N, qmin, beta, cbar = F(700), F(107, 200), F(41, 100), F(79, 200)
phi, xi, Vstar = F(2, 5), F(93, 100), F(113, 1000)
T = (0, 1/qmin)
M4 = add(scale(T, A*A), scale(mul(T, T), 3))
J = (F(1, 5), F(5, 2))


def S(c):
    return add(add(scale(T, F(1, 4)), scale(J, c)),
               scale(M4, F(27, 256)*(F(5, 3)+5*c/4)))


eminus = scale(add(scale(S(cbar), beta), (phi*(xi/8+F(2, 27)),)), 1/Vstar)
eplus = scale(add(scale(S(F(0)), beta), (phi*F(2, 27), phi*xi/2)), 1/Vstar)
ediff = scale(add(eminus, scale(eplus, -1)), Vstar)
identified = add((F(7889, 100000), F(1751, 8000)),
                 scale(M4, beta*F(27, 256)*5*cbar/4))
require("exact error-envelope difference identity", equal(ediff, identified))
require("error-envelope difference positive on nonnegative ray", all(c > 0 for c in ediff))
require("Eminus nonnegative and convex", all(c >= 0 for c in eminus) and eminus[2] > 0)
eta, mass, kappa, piup, r = F(2, 5), F(3, 4), F(3), F(22, 7), F(3, 8)
z, b = kappa*(1-6/N), 1+3/N
W = scale((0,
           z/2-A*A*b/16-4*piup*piup/(N*r),
           -z*z/4-3*b*b/16,
           z**3/12, -z**4/48), eta*mass)
second_formula = scale(add(scale(add(mul((-1, z), (-1, z)), (1,)), z*z/4),
                           (3*b*b/8,)), -eta*mass)
require("W second derivative negative square identity", equal(deriv(deriv(W)), second_formula))
P = add(add(W, scale(eminus, -1/N)), (0, F(-1, 100)))
quartic_values = {}
for endpoint, floor in [(F(1, 100), F(2314, 10**6)),
                         (F(7, 20), F(61304, 10**6))]:
    result = value(P, endpoint)
    require(f"P({endpoint}) strict lower bound", result > floor)
    quartic_values[str(endpoint)] = str(result)
reject("overstated lower-noise quartic margin", value(P, F(1, 100)) > F(3, 1000))

# Six radial comparisons, without differentiating the absolute-value h.
c0, radius, eta_ray = F(819, 2000), F(9, 8), F(8, 875)
ray_values = {}
for name, t, moment, hfloor, lfloor, dlfloor in [
        ("negative", F(499, 250)*(F(3, 8)+F(3, 5)), F(-16537, 250000),
         F(-2, 5), F(-1), F(-13, 5)),
        ("positive", F(499, 250)*(F(107, 200)+F(3, 5)), F(2527, 10000),
         F(-13, 100), F(-8, 5), F(-16, 5))]:
    Q = (eta_ray*radius, 3*moment, F(3, 2)*radius, F(-1))
    g = (F(2, 5)*(F(1, 2)+eta_ray), F(0), F(1, 5))
    L = add(g, scale(deriv(Q), c0))
    hvalue = F(81, 80)**3*(F(2, 5)*((t**3-3*t)/6+abs(t**4-6*t*t+3)/72)
                             +t**5/4100+3*t/820+17*(3*t*t-2)/78720)
    boundary = hvalue+c0*value(Q, t)
    require(f"{name}: t squared exceeds 3", t*t > 3)
    require(f"{name}: h nonnegative", hvalue >= 0)
    require(f"{name}: boundary upper bound", boundary < hfloor)
    require(f"{name}: L upper bound", value(L, t) < lfloor)
    require(f"{name}: L prime upper bound", value(deriv(L), t) < dlfloor)
    require(f"{name}: L second derivative constant negative", deriv(deriv(L)) == (F(-2057, 1000),))
    ray_values[name] = {"boundary": str(boundary), "L": str(value(L, t)),
                        "Lprime": str(value(deriv(L), t))}

sig_lo = F(3162277660, 10**9)
p = F(3, 8)
q = 1-p
q_endpoint = (sig_lo+1)*p*p+(sig_lo-1)*q*q-6*p*q
require("probability endpoint bound", q_endpoint > F(47, 2000))
require("pstar between 3/8 and 21/50 by directed squares",
        F(79, 25)**2 < 10 < F(13, 4)**2)
reject("incorrect common probability endpoint margin", q_endpoint > F(24, 1000))

# Test the joint-budget identity directly on rational atomic laws.  All its
# terms are homogeneous of degree three, so raw centered coordinates suffice:
# standardization divides both sides by the same positive variance^(3/2).
# Pairs (a,b) represent a+b*sqrt(10); the sqrt coefficient cancels exactly.
actual_laws = []


def joint_budget_case(name, atoms):
    require(name + ": mass one", sum(p for _, p in atoms) == 1)
    mean = sum(x*p for x, p in atoms)
    merged = {}
    for x, p in atoms:
        if p:
            merged[x-mean] = merged.get(x-mean, F(0))+p
    law = sorted(merged.items())
    require(name + ": no zero atom and both signs", law[0][0] < 0 < law[-1][0] and all(x for x, _ in law))
    p = sum(prob for x, prob in law if x > 0)
    q, v = 1-p, p*(1-p)
    m = sum(x*prob for x, prob in law if x > 0)
    ell, A0, B0 = m/v, -max(x for x, _ in law if x < 0), min(x for x, _ in law if x > 0)
    a0, a1 = p-A0/ell, q-B0/ell
    d, w = a0+a1, v*ell*ell
    require(name + ": inward displacements", a0 >= 0 and a1 >= 0 and 0 <= d < 1)
    rho = sum(abs(x)**3*prob for x, prob in law)
    gamma = sum(x**3*prob for x, prob in law)
    Jgap = F(0)
    for (left, _), (right, _) in zip(law, law[1:]):
        tau = sum(x*prob for x, prob in law if x >= right)
        Jgap += tau*(right-left)**2
    Dpair = (3*rho-gamma-3*Jgap, rho)
    Qpair = (p*p-q*q-6*v, p*p+q*q)
    Gpair = [ell*w*Qpair[0]+6*ell*w*(d*(1-d)+a0*a1), ell*w*Qpair[1]]
    for x, prob in law:
        conditional_mean = ell*q if x > 0 else -ell*p
        residual_square = (x-conditional_mean)**2
        magnitude_sum = x+2*ell*q if x > 0 else -x+2*ell*p
        constant = -magnitude_sum+6*B0 if x > 0 else magnitude_sum+6*A0
        Gpair[0] += prob*constant*residual_square
        Gpair[1] += prob*magnitude_sum*residual_square
    remainder = (Dpair[0]-Gpair[0], Dpair[1]-Gpair[1])
    require(name + ": exact radical cancellation", remainder[1] == 0)
    require(name + ": nonnegative budget surplus", remainder[0] >= 0)
    actual_laws.append({"name": name, "atoms_after_collision_merge": len(law),
                        "budget_surplus": str(remainder[0])})


joint_budget_case("symmetric Bernoulli", [(F(-1), F(1, 2)), (F(1), F(1, 2))])
joint_budget_case("skew Bernoulli", [(F(-1), F(2, 3)), (F(2), F(1, 3))])
joint_budget_case("nearby three atoms", [(F(-1), F(1, 2)), (F(1), F(1, 4)), (F(10001, 10000), F(1, 4))])
joint_budget_case("nearby four atoms", [(F(-10001, 10000), F(1, 4)), (F(-1), F(1, 4)),
                                        (F(1), F(1, 4)), (F(10001, 10000), F(1, 4))])
joint_budget_case("tiny far atom", [(F(-1), F(1, 2)), (F(1), F(1, 2)-F(1, 10**12)),
                                    (F(10**6), F(1, 10**12))])
joint_budget_case("exact support collision", [(F(-1), F(1, 4)), (F(-1), F(1, 4)),
                                              (F(1), F(1, 2))])
joint_budget_case("five atoms with noncentral outer gap", [(F(x), F(1, 5)) for x in (-2, -1, 1, 2, 3)])
require("noncentral outer gap has positive surplus", F(actual_laws[-1]["budget_surplus"]) > 0)

print(json.dumps({
    "status": "PASS_REVISION_FOUNDATION_CONSTANTS",
    "python": sys.version,
    "scope": "Exact scalar/polynomial checks; analytical implications separately proved in text and review. No entry replay or finite-base theorem.",
    "checks": checks, "negative_controls_rejected": controls,
    "small_noise_minima": minima, "quartic_values": quartic_values,
    "radial_values": ray_values, "actual_law_diagnostics": actual_laws,
}, indent=2))

"""Exact scalar and polynomial checks for the compact manuscript.

Only standard-library integer/rational arithmetic is used. This checks the
finite identities in the two canonical appendices, not the analytical
Fourier theorem, entry certificate semantics, finite base, or full conjecture.
Run: python -I -B tools/canonical-check.py
"""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import re
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError("Run with assertions enabled")

root = Path(__file__).resolve().parents[1]
constants = root / "appendices/normalization.tex"
fourier = root / "appendices/fixed-fourier.tex"
text = constants.read_text(encoding="utf-8")


def capture(pattern):
    match = re.search(pattern, text)
    if match is None:
        raise ValueError("Canonical constant recipe missing: " + pattern)
    return match.groups()


# Extract the actual printed recipes, rather than accepting a separately
# hard-coded numerical approximation to pi, sqrt(10), or the target.
kl, jl = map(int, capture(r"\\pi_-:=16s_\{(\d+)\}\(1/5\)-4s_(\d+)\(1/239\)"))
ku, ju = map(int, capture(r"<16s_\{(\d+)\}\(1/5\)-4s_(\d+)\(1/239\)=:\\pi_\+"))
rl_num, rl_power = map(int, capture(r"r_-=(\d+)/10\^\{(\d+)\}"))
ru_num, ru_power = map(int, capture(r"r_\+=(\d+)/10\^\{(\d+)\}"))
cl_text, = capture(r"c_-=([.\d]+),")
cu_text, = capture(r"c_\+=([.\d]+)\.")
assert kl % 2 == 0 and jl % 2 == 1
assert ku % 2 == 1 and ju % 2 == 0


def arctan_sum(x, count):
    return sum(((-1) ** j * x ** (2 * j + 1) / F(2 * j + 1)
                for j in range(count)), F())


pi_lo = 16 * arctan_sum(F(1, 5), kl) - 4 * arctan_sum(F(1, 239), jl)
pi_hi = 16 * arctan_sum(F(1, 5), ku) - 4 * arctan_sum(F(1, 239), ju)
r_lo, r_hi = F(rl_num, 10 ** rl_power), F(ru_num, 10 ** ru_power)
c_lo, c_hi = F(cl_text), F(cu_text)
ce_sq_lo = (19 + 6 * r_lo) / (72 * pi_hi)
ce_sq_hi = (19 + 6 * r_hi) / (72 * pi_lo)

checks = {
    "Machin_alternating_directions": kl % 2 == 0 and jl % 2 == 1
        and ku % 2 == 1 and ju % 2 == 0,
    "positive_branch": 0 < 4 * (F(1, 5) - F(1, 3 * 5 ** 3)) - F(1, 239),
    "pi_coarse_chain": F(25, 8) < F(333, 106) < pi_lo < pi_hi < F(22, 7),
    "sqrt_pi_lower": F(4431, 2500) ** 2 < pi_lo,
    "sqrt_pi_over_two_upper": pi_hi / 2 < F(251, 200) ** 2,
    "sqrt10": r_lo ** 2 < 10 < r_hi ** 2,
    "fine_target_squared_chain": c_lo ** 2 < ce_sq_lo < ce_sq_hi < c_hi ** 2,
    "coarse_target_chain": F(819, 2000) < c_lo < c_hi
        < F(20487, 50000) < F(41, 100),
    "phi_zero_lower": F(39886, 100000) ** 2 < 1 / (2 * pi_hi),
    "phi_zero_lower_consequences": F(199, 500) < F(997, 2500)
        == F(3988, 10000) < F(39886, 100000),
    "phi_zero_upper": 1 / (2 * pi_lo) < F(2, 5) ** 2,
    "inverse_four_pi_upper": 1 / (4 * pi_lo) < F(2, 25),
    "phi_second_derivative_exterior_gate": 1 + F(3, 2) > 2,
    "Gaussian_absolute_moments_3_and_5":
        (2 ** 2 * factorial(1), 2 ** 3 * factorial(2)) == (4, 16),
}
assert all(checks.values()), checks

# Bivariate polynomials: (power of x, power of u) -> exact coefficient.
# This verifies coefficients, not values on a sampled grid.
def clean(p):
    return {key: value for key, value in p.items() if value}


def add(*polys):
    result = {}
    for poly in polys:
        for key, value in poly.items():
            result[key] = result.get(key, F()) + value
    return clean(result)


def scale(poly, factor):
    return clean({key: factor * value for key, value in poly.items()})


def mul(a, b):
    result = {}
    for (i, j), av in a.items():
        for (k, l), bv in b.items():
            key = (i + k, j + l)
            result[key] = result.get(key, F()) + av * bv
    return clean(result)


def const(value):
    return {(0, 0): F(value)}


def integral_u(poly):
    result = {}
    for (i, j), value in poly.items():
        key = (i, 0)
        result[key] = result.get(key, F()) + value * factorial(j)
    return clean(result)


x, u = {(1, 0): F(1)}, {(0, 1): F(1)}
x2, u2 = mul(x, x), mul(u, u)
P = add(u2, scale(u, -4), const(2))
D = add(x2, scale(x, 4), const(2))
A = add(scale(mul(u2, u), -1), mul(add(x, const(8)), u2),
        scale(mul(add(x2, scale(x, 8), const(20)), u), -1),
        mul(x2, x), scale(x2, 8), scale(x, 20), const(16))
checks.update({
    "Mills_division_coefficients": add(mul(D, D), scale(mul(add(x, u), A), -1))
        == mul(P, P),
    "Mills_factorial_integral": integral_u(A) == mul(add(x, const(3)), D),
    "Mills_orthogonality_0": integral_u(P) == {},
    "Mills_orthogonality_1": integral_u(mul(u, P)) == {},
    "Mills_denominator_positive_on_x_positive": all(v > 0 for v in D.values()),
})
assert all(checks.values()), checks
ftext = fourier.read_text(encoding="utf-8")
assert "P(u)=u^2-4u+2" in ftext and "D_x=P(-x)=x^2+4x+2" in ftext

result = {
    "status": "PASS_CANONICAL_CONSTANTS_AND_MILLS_IDENTITIES",
    "checks": checks,
    "exact": {
        "pi_lower": str(pi_lo), "pi_upper": str(pi_hi),
        "sqrt10_lower": str(r_lo), "sqrt10_upper": str(r_hi),
        "target_lower": str(c_lo), "target_upper": str(c_hi),
        "target_squared_lower_margin": str(ce_sq_lo - c_lo ** 2),
        "target_squared_upper_margin": str(c_hi ** 2 - ce_sq_hi),
        "Mills_P_coefficients_in_u": ["2", "-4", "1"],
        "Mills_D_coefficients_in_x": ["2", "4", "1"],
    },
    "source_sha256": {str(p.relative_to(root)).replace("\\", "/"):
                      sha256(p.read_bytes()).hexdigest() for p in (constants, fourier)},
    "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Exact finite scalar gates and polynomial/factorial identities only; "
             "not the full analytical Fourier theorem, entry semantics, finite base, "
             "or full conjecture acceptance.",
}
print(json.dumps(result, separators=(",", ":")))
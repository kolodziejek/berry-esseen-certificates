#!/usr/bin/env python3
"""Bounded exact checks for the Argon proposal audit; no archive execution.

The universal statements are proved in argon-audit.md. This program checks
their algebra and rational examples, not acquisition or certificate coverage.
"""
from fractions import Fraction as F
from math import isqrt
import hashlib
import json
from pathlib import Path
import platform
import sys


ROOT = Path(__file__).resolve().parents[3]
INPUTS = [
    "manuscript/arxiv-v1/sections/03-smoothing.tex",
    "manuscript/arxiv-v1/appendices/finite-support.tex",
    "manuscript/arxiv-v1/appendices/finite-analysis.tex",
    "manuscript/arxiv-v1/appendices/fourier-analysis.tex",
    "manuscript/arxiv-v1/appendices/uniform-bridge.tex",
]


def sqrtenclose(x, denominator=10**12):
    """Exact enclosing rationals, proved by squaring (no floating point)."""
    k = isqrt(x.numerator * denominator**2 // x.denominator)
    lo, hi = F(k, denominator), F(k + 1, denominator)
    assert lo**2 <= x < hi**2
    return lo, hi


def excess_interval(n):
    assert isinstance(n, int) and n >= 2
    ratio = F(n, n - 1)
    sl, su = sqrtenclose(ratio)
    ll, lu = sqrtenclose(F(n - 1))
    # c in (819/2000,41/100); denominators enclosed in opposite direction.
    lower = ratio * (F(819, 2000) / (su + 1) + sl / 15 + 2 * sl / (25 * lu))
    upper = ratio * (F(41, 100) / (sl + 1) + su / 15 + 2 * su / (25 * ll))
    assert lower < upper
    return lower, upper


def show(name, value):
    print(f"{name}: {value}")


def main():
    print("scope: exact algebra, scalar entry bounds and rejected substitutions only")
    print("python: " + platform.python_version())
    assert sys.flags.optimize == 0
    print("optimization: 0")
    for path in INPUTS + [str(Path(__file__).resolve().relative_to(ROOT))]:
        show("sha256 " + path, hashlib.sha256((ROOT / path).read_bytes()).hexdigest())

    # Independently expand the numerator of the alleged scale comparison.
    # N^2(N-2) -(N-1)^3 = N^2-3N+1.
    lhs_coefficients = [0, 0, -2, 1]
    rhs_coefficients = [-1, 3, -3, 1]
    assert [a - b for a, b in zip(lhs_coefficients, rhs_coefficients)] == [1, -3, 1, 0]
    for n in (3, 4, 20, 25, 40, 42, 47, 1000):
        diff = F(n, n - 1)**3 - F(n, n - 2)
        identity = F(n * (n*n - 3*n + 1), (n - 1)**3 * (n - 2))
        assert diff == identity > 0
        show(f"deletion difference N={n}", diff)
    for n, fd in ((3, F(9, 5)), (42, F(103, 100))):
        assert F(n, n - 2) < fd**2 < F(n, n - 1)**3
        show(f"REJECT weaker deletion gate N={n}, Fd={fd}", "proposed gate passes, required gate fails")

    # Polynomial multiplication without relying on the manuscript expansion.
    def multiply(a, b):
        out = [F(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] += x*y
        return out
    for a in (F(1), F(3, 7)):
        for c in (F(2), F(3, 2), F(7, 3)):
            assert multiply([0, c*a, -1], [a*a, 2*a, 1]) == [0, c*a**3, (2*c-1)*a*a, (c-2)*a, -1]
    assert multiply([0, 2, -1], [1, 2, 1]) == [0, 2, 3, 0, -1]
    assert F(1)**2 < 3 < F(2)**2
    show("REJECT c=1+sqrt(3) shifted-quartic identity", "cubic coefficient sqrt(3)-1 is positive; c=2 is exact")

    # The retained n=4 endpoint certificate has only this much margin.
    radius = F(101, 25)
    p = -F(643, 1875)*radius**3 + F(17664, 15625)*radius**2 + F(77257, 78125)*radius + F(7541, 46875)
    assert p == -F(51557, 9765625)
    coarse = p + F(1, 2) - F(1, 15)
    assert coarse > 0
    show("n4 retained endpoint", p)
    show("REJECT replacement of n4 1/15 remainder by universal 1/2", coarse)

    cap42 = F(42, 41)*(F(41, 200) + F(27, 400) + F(27, 2000))
    assert 41*81**2 - 42*80**2 == 201
    assert cap42 == F(3003, 10250) < F(3, 10)
    assert F(41, 100) + F(3, 10)/42 == F(73, 175) < F(2113, 5000)
    cap40 = F(40, 39)*(F(41, 200) + F(40, 39)/15 + 2*F(40, 39)/(25*6))
    assert F(40, 39)**2 > F(40, 39) and 6**2 < 39
    assert cap40 < F(61, 200)
    show("coarse excess cap at N=40", cap40)
    for n in (2, 3, 4, 5, 20, 25, 40, 42, 47):
        lo, hi = excess_interval(n)
        show(f"epsilon enclosure n={n}", f"({lo}, {hi})")
    assert excess_interval(42)[1] < cap42
    assert excess_interval(40)[1] < F(61, 200)
    try:
        excess_interval(1)
    except AssertionError:
        show("REJECT n=1 smoothing substitution", "n-1 would vanish")
    else:
        raise AssertionError("invalid smoothing index accepted")

    # Logical countermodels are abstract sequences, not Berry--Esseen laws.
    c = F(41, 100)
    scores = [c - F(1, 100), c, c - F(1, 100)]
    assert not any(x > c for x in scores) and not all(x < c for x in scores)
    show("REJECT strict conclusion from absence of > failures", "abstract equality countermodel")
    assert 5*max(c + F(1, 100) - c, 0) == F(1, 20)
    show("REJECT zero loss with predecessor premise erased", "abstract predecessor c+1/100 gives loss 1/20")
    assert F(1000, 4553) > F(5, 23)
    show("harmonic coefficient comparison", F(1000, 4553) - F(5, 23))
    print("PASS: bounded scalar checks; no analytic/certificate coverage acceptance")


if __name__ == "__main__":
    main()

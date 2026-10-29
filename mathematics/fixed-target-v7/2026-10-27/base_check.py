#!/usr/bin/env python3
"""Bounded rational checks for base-audit.md; no inherited module is imported.

This checks the displayed localization polynomial and scalar obstructions.
It does not check ROOT4, BASE41, any Fourier inequality or any native certificate.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
T, RHO, BETA, RADIUS = F(4097, 10000), F(979013, 533000), F(641, 1000), F(504, 125)


def derivatives(a, x):
    return [sum(a[j] * F(factorial(j), factorial(j-k)) * x**(j-k)
                for j in range(k, len(a))) for k in range(len(a))]


def gates(rho=RHO, beta=BETA, radius=RADIUS):
    # Q(y) is the coefficient of the actual maximizing score C.
    q = [-F(9, 2)*rho, 3*beta, F(3, 2)*rho, -F(1)]
    # P dominates the contact at C >= T, after Q < 0 has been proved.
    p = [F(1, 15)+(F(236, 125)-F(9, 2)*T)*rho,
         F(1, 5)+3*T*beta, F(3, 2)*T*rho, F(1, 15)-T]
    result = {
        "rho_encloses_shevtsova": rho >= F(3031, 10000)*F(323, 500)/(T-F(3031, 10000)),
        "beta_excluded_boundary": (1+beta*beta)**2 > rho*rho*(1-beta*beta),
        "negative_Q_ray_from_4": all(x < 0 for x in derivatives(q, F(4))),
        "rho_coefficient_positive": F(3, 2)*T*16+F(236, 125)-F(9, 2)*T > 0,
        "radius_at_least_4": radius >= 4,
        "negative_P_ray": all(x < 0 for x in derivatives(p, radius)),
    }
    return result, p, derivatives(p, radius)


def main():
    checks, p, values = gates()
    assert all(checks.values()), checks
    assert T*T - F(3)*F(59, 250)**2 > 0
    # The leading predecessor term already admits the false scalar value .41.
    assert F(59, 125) > F(41, 100)
    # At 40/41 the recurrence also permits c + 1/(100*n), for every c > .4:
    # sqrt(n/(n-1))-1 > 1/(2*n); after squaring this is an exact check.
    for n in (40, 41):
        assert F(n, n-1) > (1+F(1, 2*n))**2
        assert F(2, 5)*F(1, 2*n) > F(1, 100*n)
    controls = {
        "radius4_rejected": not all(gates(radius=F(4))[0].values()),
        "understated_rho_1.8_rejected": not all(gates(rho=F(9, 5))[0].values()),
        "understated_beta_.640_rejected": not all(gates(beta=F(16, 25))[0].values()),
        "LOCAL42_at41_rejected": not (41 >= 42),
        "reversed_signed_endpoint_rejected": not (F(1, 41) <= F(1, 42)),
    }
    assert all(controls.values()), controls
    sources = ["paper/analytic-supplement.txt", "paper/main.tex", "mathematics/global-contract.json",
               "source/original/proof/obligations.json",
               "mathematics/simplification/2026-10-27/base-closure.md",
               "mathematics/audit/ARITHMETIC-FOUNDATIONS-G2-G3-ROOT4-v4.md"]
    print(json.dumps({
        "schema": "be.bounded-base-audit/1",
        "mathematical_scope": "Conditional n4 localization only; scalar countermodels are not iid laws.",
        "native_execution": "not run", "BASE41_verified": False,
        "constants": {"target": str(T), "rho": str(RHO), "beta": str(BETA), "radius": str(RADIUS)},
        "polynomial_coefficients_ascending": list(map(str, p)),
        "derivatives_at_radius": list(map(str, values)),
        "beta_boundary_reserve": str((1+BETA*BETA)**2-RHO*RHO*(1-BETA*BETA)),
        "checks": checks, "negative_controls": controls,
        "source_sha256": {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

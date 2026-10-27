#!/usr/bin/env python3
"""Exact finite algebra supporting scalar-review.md; not an analytic prover.

Uses only Python integers/Fraction. The infinite-n reduction, Gaussian Taylor
argument and Machin identity proof are written in the accompanying review.
No certificate generation, source mutation, network or third-party dependency.
"""

from fractions import Fraction as Q
import json


class Rejected(ValueError):
    pass


def require(condition, obligation):
    if not condition:
        raise Rejected(obligation)


PARAMETERS = {
    "n0": 47,
    "sqrt_bound": Q(1011, 1000),
    "sqrt_v_lower": Q(6),
    "sqrt10_upper": Q(19, 6),
    "c_upper": Q(41, 100),
    "taylor": Q(1, 15),
    "heat": Q(2, 25),
    "excess": Q(3, 10),
    "own_cap": Q(4247, 10000),
    "deleted_cap": Q(4253, 10000),
}


def check(p):
    require(set(p) == set(PARAMETERS), "exact parameter keys")
    require(isinstance(p["n0"], int) and p["n0"] >= 2, "n0 >= 2")
    require(all(v > 0 for v in p.values()), "positive constants")

    # tan(4 arctan(1/5) - arctan(1/239)) = 1.
    a, b = Q(1, 5), Q(1, 239)
    tan2 = 2*a/(1-a*a)
    tan4 = 2*tan2/(1-tan2*tan2)
    require((tan4-b)/(1+tan4*b) == 1, "Machin tangent identity")
    angle_lower = 4*(a-a**3/3)-b
    require(0 < angle_lower < 4*a < 1, "Machin angle branch")
    pi_lower = 4*angle_lower
    require(pi_lower == Q(281476, 89625), "pi lower identity")
    require(pi_lower > Q(157, 50) > Q(25, 8), "pi comparison")

    r = p["sqrt10_upper"]
    require(r*r > 10, "sqrt(10) upper bound")
    require((19+6*r)/(72*pi_lower) < p["c_upper"]**2,
            "Esseen constant upper bound")
    require((6*p["taylor"])**2 * 2*pi_lower > 1,
            "Gaussian spatial Taylor constant")
    require(1/(4*pi_lower) < p["heat"], "Gaussian heat constant")

    n0 = p["n0"]
    ratio = Q(n0, n0-1)
    require(p["sqrt_bound"] > 1 and p["sqrt_bound"]**2 > ratio,
            "uniform square root upper bound")
    require(n0-1 > p["sqrt_v_lower"]**2,
            "uniform sqrt(n-1) lower bound")
    bound = ratio*(p["c_upper"]/2
                   + p["sqrt_bound"]*p["taylor"]
                   + p["heat"]*p["sqrt_bound"]/p["sqrt_v_lower"])
    require(bound < p["excess"], "excess bound")
    require(p["excess"] <= Q(7, 10), "local excess gate")
    own = p["c_upper"] + p["excess"]/n0
    require(own < p["own_cap"], "own-index cap")
    require(p["c_upper"] < p["deleted_cap"], "deleted-index cap")
    # Strict violation, or a >= violation after a weak prefix, supplies this
    # sign analytically; no law or supremum is represented by the checker.
    require(0 <= Q(19, 100), "zero predecessor-loss gate")
    return {"pi_lower": str(pi_lower), "excess_upper": str(bound),
            "excess_margin": str(p["excess"]-bound),
            "own_cap_margin": str(p["own_cap"]-own)}


def main():
    accepted = check(PARAMETERS)
    require(accepted["excess_upper"] == "335909/1150000", "reported bound")
    mutations = [
        ("endpoint_46", {"n0": 46}),
        ("singular_index_1", {"n0": 1}),
        ("sqrt_upper_too_small", {"sqrt_bound": Q(101, 100)}),
        ("sqrt_v_lower_too_large", {"sqrt_v_lower": Q(7)}),
        ("sqrt10_upper_too_small", {"sqrt10_upper": Q(79, 25)}),
        ("c_upper_too_small", {"c_upper": Q(409, 1000)}),
        ("taylor_constant_too_small", {"taylor": Q(1, 16)}),
        ("heat_constant_too_small", {"heat": Q(79, 1000)}),
        ("excess_target_029", {"excess": Q(29, 100)}),
        ("own_cap_too_small", {"own_cap": Q(4163, 10000)}),
        ("deleted_cap_too_small", {"deleted_cap": Q(409, 1000)}),
        ("unexpected_field", {"unproved_input": Q(1)}),
    ]
    rejected = {}
    for name, changes in mutations:
        try:
            check(PARAMETERS | changes)
        except Rejected as exc:
            rejected[name] = str(exc)
        else:
            raise Rejected("negative control accepted: " + name)
    missing = dict(PARAMETERS)
    del missing["heat"]
    try:
        check(missing)
    except Rejected as exc:
        rejected["missing_heat"] = str(exc)
    else:
        raise Rejected("missing-field control accepted")
    print(json.dumps({"status": "PASS_SCALAR_ALGEBRA",
                      "scope": "finite rational obligations only",
                      "accepted": accepted, "negative_controls": rejected},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

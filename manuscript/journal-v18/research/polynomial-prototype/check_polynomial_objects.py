#!/usr/bin/env python3
"""Five fixed polynomial identities only; not a manuscript proof ancestor.

Acceptance uses Python integers/Fraction and a sparse bivariate ring Q[x,a].
There is no symbolic algebra dependency, numerical search, or evaluation grid.
"""
from fractions import Fraction
import json
from pathlib import Path
import sys


class Reject(ValueError):
    pass


def need(value, message):
    if not value:
        raise Reject(message)


def fields(obj, keys):
    need(type(obj) is dict and set(obj) == set(keys), "exact object fields")


def unique(pairs):
    out = {}
    for key, value in pairs:
        need(key not in out, "duplicate JSON key")
        out[key] = value
    return out


def clean(p):
    return {e: c for e, c in p.items() if c}


def add(p, q):
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, Fraction(0)) + c
    return clean(out)


def scale(p, c):
    return clean({e: c * v for e, v in p.items()})


def mul(p, q):
    out = {}
    for (i, j), c in p.items():
        for (k, l), d in q.items():
            e = i + k, j + l
            out[e] = out.get(e, Fraction(0)) + c * d
    return clean(out)


def power(p, n):
    out = {(0, 0): Fraction(1)}
    for _ in range(n):
        out = mul(out, p)
    return out


def dx(p):
    return clean({(i - 1, j): i * c for (i, j), c in p.items() if i})


def polynomial(rows):
    need(type(rows) is list and 1 <= len(rows) <= 20, "finite nonempty polynomial")
    out = {}
    previous = None
    for row in rows:
        need(type(row) is list and len(row) == 3, "monomial shape")
        i, j, value = row
        need(type(i) is int and type(j) is int and 0 <= i <= 8 and 0 <= j <= 8,
             "nonnegative bounded integer exponents")
        exponent = i, j
        need(previous is None or previous < exponent, "ordered unique monomials")
        need(type(value) is str and len(value) < 40, "rational string")
        try:
            coefficient = Fraction(value)
        except (ValueError, ZeroDivisionError):
            raise Reject("invalid rational") from None
        need(str(coefficient) == value and coefficient != 0, "canonical nonzero rational")
        out[exponent] = coefficient
        previous = exponent
    return out


X = {(1, 0): Fraction(1)}
A = {(0, 1): Fraction(1)}
ONE = {(0, 0): Fraction(1)}
IDS = ["conditional3", "conditional4", "conditional5", "radial4", "radial5"]


def verify(obj):
    need(__debug__ and not sys.flags.optimize, "optimized Python forbidden")
    fields(obj, ("format", "scope", "variables", "cases"))
    need(obj["format"] == "FIVE_POLYNOMIAL_OBJECTS_V1", "format")
    need(obj["scope"] == "demonstration_only_not_current_proof_ancestor", "fixed scope")
    need(obj["variables"] == ["x", "a"], "fixed variables")
    cases = obj["cases"]
    need(type(cases) is list and len(cases) == 5, "all five cases required")
    need(all(type(case) is dict for case in cases), "case objects")
    need([case.get("id") for case in cases] == IDS, "exact ordered five-case cover")
    rows = []
    for case in cases:
        identity = case["id"]
        if identity.startswith("conditional"):
            fields(case, ("id", "quotient"))
            j = int(identity[-1])
            q = polynomial(case["quotient"])
            delta = add(X, scale(A, -1))
            target = add(add(power(X, j), scale(power(A, j), -1)),
                         scale(mul(power(A, j - 1), delta), -j))
            need(mul(power(delta, 2), q) == target, "conditional coefficient identity")
            need(all(c > 0 for c in q.values()), "conditional positive coefficients")
            rows.append({"id": identity, "identity": True,
                         "nonnegative_on_x_a_nonnegative": True,
                         "coordinatewise_nondecreasing": True})
        else:
            fields(case, ("id", "numerator", "derivative_numerator", "moment_difference"))
            j = int(identity[-1])
            numerator = polynomial(case["numerator"])
            derivative = polynomial(case["derivative_numerator"])
            moment = polynomial(case["moment_difference"])
            # The finite theorem, rather than the submitted data, fixes N_j.
            expected = (power(add(X, ONE), 2) if j == 4 else
                        add(add(power(X, 3), scale(power(X, 2), 2)),
                            add(scale(X, 3), scale(ONE, Fraction(3, 2)))))
            need(numerator == expected, "fixed radial numerator")
            denominator = add(X, scale(ONE, Fraction(1, 2)))
            target = add(mul(dx(numerator), denominator), scale(numerator, -1))
            need(derivative == target, "radial derivative coefficient identity")
            need(all(k == 0 and c > 0 for (i, k), c in derivative.items()),
                 "radial derivative nonnegative on x>=0")
            need(moment == mul(power(add(X, scale(ONE, -1)), 2), numerator),
                 "radial factor identity")
            fixed_moment = add(power(X, j), add(scale(power(X, 2), -Fraction(j, 2)),
                                               scale(ONE, Fraction(j, 2) - 1)))
            need(moment == fixed_moment, "radial moment coefficient identity")
            rows.append({"id": identity, "identity": True,
                         "denominator_positive_on_x_nonnegative": True,
                         "quotient_nondecreasing_on_x_nonnegative": True})
    return {"status": "PASS_FIVE_POLYNOMIAL_IDENTITIES_ONLY", "cases": rows,
            "current_manuscript_ancestor": False, "native_integrations": 0}


def load(path):
    data = Path(path).read_bytes()
    need(len(data) < 20000, "bounded object size")
    try:
        return json.loads(data, object_pairs_hook=unique)
    except (ValueError, UnicodeError) as exc:
        raise Reject("JSON parse: " + str(exc)) from None


if __name__ == "__main__":
    need(len(sys.argv) == 2, "one proof-object path")
    print(json.dumps(verify(load(sys.argv[1])), sort_keys=True))

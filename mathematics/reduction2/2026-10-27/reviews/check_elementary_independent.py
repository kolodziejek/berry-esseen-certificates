#!/usr/bin/env python3
"""Independent bounded rational checks of the fourth-order support proof.

No constructor or archived module is imported. The family polynomial is
reconstructed from scalar evaluations using a rational Vandermonde solve,
not the constructor's polynomial multiplication/shift implementation.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile
import ast
import json
import sys

ROOT = Path(__file__).resolve().parents[4]
ARCHIVE = ROOT / "verification/finite-tail/sources/backend.zip"
ARCHIVE_SHA = "43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52"
PINS = {
    "proof": "419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393",
    "route": "df1631620cf1135a5bb6fb9cd28f6c514f6a0451f7c1699ad55054fa1b23dcd0",
    "initial_caller": "343046eaf0a3e6b2e140644cee19b7764d76b4171b844eaac27fb1a288b12d2e",
    "left_caller": "a565247f6587f3bb07dd67ef2100d08f70aebbe7543937f1ab98f8d09cf31eb6",
}
C, S, EMAX = F(819, 2000), F(81, 80), F(8, 875)
RMIN, RMAX = F(5, 2), F(111, 40)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def unique(pairs):
    d = {}
    for key, val in pairs:
        need(key not in d, "duplicate JSON key")
        d[key] = val
    return d


def A(u):
    return (u**3-3*u)/6


def H4(u):
    return u**4-6*u*u+3


def remainder(u):
    # Derived from phi4<6/5 and phi5<51/20 before simplifying fractions.
    return (F(6, 5)*(u**5/120+u/8))/41 + F(51, 20)*(F(1, 48)+(u*u-1)/16)/(41*6)


def Q(u, r, b):
    return -u**3+F(3, 2)*r*u*u+3*b*u+r*EMAX


def reserve(u, r, b, sharp=False):
    g = A(u)+H4(u)/72
    if sharp:
        # 9B^2/(4A), with B^2 <= H4^2/(24^2*41).
        g = A(u)+F(9, 4)*H4(u)**2/(24**2*41*A(u))
    return -(S**3*(F(2, 5)*g+remainder(u))+C*Q(u, r, b))


def ray_values(u, r, b):
    dq = -3*u*u+3*r*u+3*b
    ddq = -6*u+3*r
    return [Q(u, r, b), dq, ddq,
            F(2, 5)*(u*u/2+F(1, 2)+EMAX)+C*dq,
            F(2, 5)*u+C*ddq, F(2, 5)-6*C]


def family(R):
    return reserve(R, F(7, 20)*R+F(1, 3), F(3, 8)*R-F(3, 5))


def interpolate(xs, ys):
    """Rational linear solve for coefficients, with independent residuals."""
    n = len(xs)
    rows = [[x**j for j in range(n)]+[y] for x, y in zip(xs, ys)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        rows[col] = [v/scale for v in rows[col]]
        for i in range(n):
            if i != col:
                k = rows[i][col]
                rows[i] = [a-k*b for a, b in zip(rows[i], rows[col])]
    ans = [row[-1] for row in rows]
    need(all(sum(a*x**j for j, a in enumerate(ans)) == y for x, y in zip(xs, ys)), "interpolation residual")
    return ans


def literal(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, str):
        return F(node.value)
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "F" and len(node.args) == 1:
        return literal(node.args[0])
    if isinstance(node, ast.Name):
        return node.id
    raise ValueError("unexpected target argument syntax")


def target_calls(raw, owner):
    found = []
    for node in ast.walk(ast.parse(raw)):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "target" and isinstance(node.func.value, ast.Name) and node.func.value.id == owner:
            # The only target with five positional arguments is the actual call;
            # initial negative controls use the unpacked *args form.
            if len(node.args) == 5:
                found.append(tuple(literal(a) for a in node.args))
    return found


def bind(proof, route):
    need((proof["N"], proof["L"], F(proof["cap"])) == (42, 48, F(2113, 5000)), "original proof domain")
    need(proof["route_sha256"] == PINS["route"], "route dependency")
    need((route["N"], route["L"], F(route["cap"]), F(route["first_radius"])) == (42, 48, F(2113, 5000), F(121, 40)), "route domain")
    need(len(proof["coarse"]) == 15 and len(proof["fine"]) == len(route["rows"]) == 55, "complete selected rows")
    for j, cell in enumerate(proof["coarse"]):
        need(list(map(F, cell["input_p"])) == [F(23+j, 100), F(24+j, 100)], "coarse closed partition")
    active = [cell for cell in proof["coarse"] if not cell.get("excluded")]
    first = proof["first_bridge"]
    need(F(first["rho_upper"]) == max(F(cell["rho"]) for cell in active), "common rho maximum")
    need(F(first["beta_absolute_upper"]) == max(F(cell["beta"]) for cell in active), "common beta maximum")
    need(F(first["radius"]) == F(121, 40), "common radius")
    later = []
    for i, (cell, planned) in enumerate(zip(proof["fine"], route["rows"])):
        interval = [F(135+i, 500), F(136+i, 500)]
        need(list(map(F, cell["p"])) == list(map(F, planned["p"])) == interval, "same ordered fine interval")
        trace = cell["trace"]
        need(trace and trace[0]["contraction"] is None, "common bridge first")
        need([F(step["radius"]) for step in trace] == list(map(F, planned["radii"])), "complete planned support path")
        need(F(trace[0]["radius"]) == F(121, 40), "common fine starting radius")
        for prev, step in zip(trace, trace[1:]):
            q = step["contraction"]
            need(q is not None, "required support edge")
            R, r, b = map(F, (q["radius"], q["rho_upper"], q["beta_absolute_upper"]))
            need(R == F(step["radius"]) < F(prev["radius"]), "contracting radius")
            need((r, b) == (F(prev["resource"]["rho"]), F(prev["resource"]["beta"])), "preceding same-law resource")
            need(RMIN <= R <= RMAX, "later radius domain")
            need(r <= F(7, 20)*R+F(1, 3) and b <= F(3, 8)*R-F(3, 5), "affine ceilings")
            later.append(q)
    need(len(later) == 63, "all later support edges")
    for edge in [first]+later:
        need(edge["n_band"] == [42, 48] and F(edge["barrier"]) == 0 and F(edge["slow"]) == F(19, 100) and F(edge["current_score_lower"]) == C, "unchanged historical call parameters")
    return first, later


def main():
    need(not sys.flags.optimize and __debug__ and len(sys.argv) == 1, "fixed unoptimized check")
    need(sha256(ARCHIVE.read_bytes()).hexdigest() == ARCHIVE_SHA, "archive pin")
    data = {}
    with ZipFile(ARCHIVE) as z:
        for label, pin in PINS.items():
            raw = z.read("finite61/blobs/"+pin)
            need(sha256(raw).hexdigest() == pin, "source pin")
            data[label] = raw
    need(target_calls(data["initial_caller"], "heat") == [(F(42), F(48), F(0), F(96, 25), F(19, 100))], "initial literal invocation")
    need(target_calls(data["left_caller"], "fifth") == [(F(42), F(48), F(0), "R", F(19, 100))], "LEFT literal invocation")
    proof = json.loads(data["proof"], object_pairs_hook=unique)
    route = json.loads(data["route"], object_pairs_hook=unique)
    first, later = bind(proof, route)

    # Rational pi bounds from independently evaluated alternating atan terms.
    pil = 16*(F(1, 5)-F(1, 375))-F(4, 239)
    piu = 16*(F(1, 5)-F(1, 375)+F(1, 15625))-4*(F(1, 239)-F(1, 3*239**3))
    need((F(120, 119)-F(1, 239))/(1+F(120, 119*239)) == 1, "Machin tangent identity")
    need(pil > F(160, 51) > F(25, 8) and piu < F(22, 7), "Gaussian constants")
    need(F(79, 25)**2 < 10 and (F(79, 25)+3)**2/(36*2*piu) > C*C, "Esseen constant exceeds rational c")
    need(sum(F(3, 2)**j/F((1, 1, 2, 6)[j]) for j in range(4)) > 4, "negative branch exponential bound")
    need(S*S > F(42, 41) and 6**2 < 41, "outward scale")
    x, a = F(1, 42), F(48, 125)
    scale = ((1-x)*(1+x/2+a*x*x)**2-1)/(x*x)
    need(scale > 0, "scale squared endpoint")
    # Check spatial/variance cancellation at distinct t, independently of z.
    for t in map(F, (-4, -3, -2, -1, 0, 1, 2, 3, 4)):
        coeff = [F(1), -t, t*t/2, -t**3/6, t**4/24]
        for k, v in ((0, -1), (2, -F(1, 2)), (4, -F(1, 8)), (1, t), (3, t/2), (2, -(t*t-1)/2), (4, -(t*t-1)/4)):
            coeff[k] += v
        need(coeff == [0, 0, 0, -(t**3-3*t)/6, (t**4-6*t*t+3)/24], "heat cancellation")

    xs = [F(j, 20) for j in range(6)]
    coeffs = interpolate(xs, [family(RMIN+w) for w in xs])
    for w in (F(1, 80), F(3, 80), F(11, 40), F(1, 3)):
        need(sum(a*w**j for j, a in enumerate(coeffs)) == family(RMIN+w), "independent polynomial holdout")
    need(coeffs[1] < 0 < coeffs[2] and coeffs[3] > 0 > coeffs[4] and coeffs[5] < 0, "derivative signs")
    h = RMAX-RMIN
    derivative_upper = coeffs[1]+2*coeffs[2]*h+3*coeffs[3]*h*h
    need(derivative_upper < 0 and family(RMAX) > F(1, 50), "continuous family margin")
    rstar, bstar = F(131, 100), F(441, 1000)
    need(F(7, 20)*RMAX+F(1, 3) < rstar and F(3, 8)*RMAX-F(3, 5) < bstar, "fixed ray rectangle")
    need(all(g < 0 for g in ray_values(RMIN, rstar, bstar)), "whole family ray gate")

    initial_r = min(F(3031, 10000)*F(646, 1000)/(C-F(3031, 10000)), F(3322, 10000)*F(429, 1000)/(C-F(3322, 10000)))
    r0, b0, R0 = F(1841, 1000), F(321, 500), F(96, 25)
    need(initial_r < r0 and 0 < b0 < 1 and (1+b0*b0)**2 > r0*r0*(1-b0*b0), "initial moment ceiling")
    need(0 < H4(R0)/144 < A(R0)/4, "initial sharp envelope coupling")
    initial = reserve(R0, r0, b0, sharp=True)
    common = reserve(F(121, 40), F(143, 100), F(93, 200))
    need(initial*A(R0) > F(1, 5) and common > F(1, 100), "two endpoint reserves")
    need(F(first["rho_upper"]) < F(143, 100) and F(first["beta_absolute_upper"]) < F(93, 200), "common outward moments")
    all_calls = [(R0, r0, b0, True), (F(121, 40), F(143, 100), F(93, 200), False)]
    all_calls += [(F(q["radius"]), F(q["rho_upper"]), F(q["beta_absolute_upper"]), False) for q in later]
    for R, r, b, sharp in all_calls:
        need(reserve(R, r, b, sharp) > 0, "all65 endpoint values")
        need(all(g < 0 for g in ray_values(R, r, b)), "all65 fixed-parameter ray gates")
    for q in later:
        R, r, b = map(F, (q["radius"], q["rho_upper"], q["beta_absolute_upper"]))
        need(reserve(R, r, b) >= family(R), "actual bound no worse than affine envelope")
    need(reserve(R0, r0, b0) < 0 and family(F(39, 10)) < 0, "coarser-bound obstructions")

    controls = []
    def rejected(name, fn):
        try:
            fn()
        except (ValueError, KeyError, TypeError):
            controls.append(name)
        else:
            raise ValueError("negative control accepted: "+name)
    changed = json.loads(data["proof"])
    changed["fine"][10]["trace"][1]["contraction"]["rho_upper"] = "1"
    rejected("different preceding moment", lambda: bind(changed, route))
    changed2 = json.loads(data["route"])
    changed2["rows"][10]["radii"].pop()
    rejected("missing planned support edge", lambda: bind(proof, changed2))
    changed3 = json.loads(data["proof"])
    changed3["fine"].reverse()
    rejected("reordered fine cells", lambda: bind(changed3, route))
    rejected("duplicate JSON key", lambda: json.loads('{"N":42,"N":43}', object_pairs_hook=unique))
    print(json.dumps({
        "status": "PASS_INDEPENDENT_ELEMENTARY_SUPPORT_ARITHMETIC",
        "scope": "conditional support component; no acquisition, attainment, base or global proof",
        "source_pins": PINS,
        "method": "direct rational scalar envelopes and Vandermonde reconstruction; no constructor imports",
        "heat_cancellation_points": 9,
        "radius_polynomial_coefficients_at_5_2": list(map(str, coeffs)),
        "polynomial_holdouts": 4,
        "radius_derivative_upper": str(derivative_upper),
        "radius_endpoint_reserve": str(family(RMAX)),
        "initial_reserve_times_A": str(initial*A(R0)),
        "common_reserve": str(common),
        "scale_margin": str(scale),
        "source_bound_support_calls": len(all_calls),
        "individually_checked_ray_gates": 6*len(all_calls),
        "negative_controls": controls,
        "refuted_coarse_shortcuts": 2,
        "native_programs_executed": 0,
    }, indent=2))


if __name__ == "__main__":
    main()

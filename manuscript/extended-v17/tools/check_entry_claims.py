#!/usr/bin/env python3
"""Independent exact diagnostics for the signed entry; imports no retained code.

This does not replay the cover or establish its analytic ancestors. Run the
source-isolated entry replay as well. This checks
the exported target constants and selected delicate semantics independently.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import sys


def require(value, message):
    if not value:
        raise ValueError(message)


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def rational(value):
    require(type(value) is str, "rational must be text")
    result = F(value)
    require(str(result) == value, "noncanonical rational")
    return result


def exported_targets(path):
    blob = path.read_bytes()
    require(sha256(blob).hexdigest() ==
            "61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae",
            "unexpected fixed proof bytes")
    obj = json.loads(blob, object_pairs_hook=no_duplicate_keys)
    require(obj["name"] == "INITIAL42_FIXED_TARGET_COARSE_V7", "wrong theorem")
    require(len(obj["steps"]) == 4, "four passes")
    excluded = set()
    previous = {}
    census = []
    nominal_boxes = 0
    for stage, rows in enumerate(obj["steps"]):
        require(len(rows) == 24, "all original rho identities")
        processed = 0
        for index, row in enumerate(rows):
            require(type(row["index"]) is int and row["index"] == index,
                    "ordered integer rho identity")
            if index in excluded:
                require(set(row) == {"index", "prior_excluded"}
                        and row["prior_excluded"] is True, "excluded identity persists")
                continue
            processed += 1
            for key in ("active", "excluded"):
                require(type(row[key]) is int and row[key] >= 0, "integer count")
            require(row["active"] + row["excluded"] == 128, "closed cover count")
            radius = rational(row["radius"])
            raw, defect = rational(row["raw"]), rational(row["defect"])
            require(F(5, 2) <= radius <= F(96, 25), "licensed support range")
            if not row["active"]:
                require(raw == defect == -1, "empty row sentinel")
                excluded.add(index)
                continue
            require(raw > 0 and defect > 0, "positive live ceiling")
            if index in previous:
                require(raw <= previous[index][0] and defect <= previous[index][1],
                        "ordered scalar ceilings")
            # The ancestor establishes this gate; subsequent ceilings preserve it.
            if stage:
                lower_rho = 1 + F(3361 * index, 96000)
                require(defect < (F(3162277660168, 10**12) - 1) * lower_rho,
                        "actual-gap license in stored output")
            previous[index] = raw, defect
        nominal_boxes += 128 * processed
        census.append({"processed": processed, "live": 24 - len(excluded)})

    final = [row for row in obj["steps"][-1] if row.get("active", 0)]
    raw = max(rational(row["raw"]) for row in final)
    defect = max(rational(row["defect"]) for row in final)
    radius = max(rational(row["radius"]) for row in final)
    rho = max(1 + F(3361 * (row["index"] + 1), 96000) for row in final)
    require(raw <= F("2.1995174"), "printed raw target")
    require(defect <= F("0.76682509"), "printed D target")
    require(42 * defect <= F("32.20665378"), "printed weighted nD target")
    require(rho <= F(71527, 48000), "printed exact rho target from closed cell endpoints")
    require(radius <= F(157, 50), "printed final radius")
    require(len(final) == 14 and nominal_boxes == 11264, "printed signed census")

    panels = obj["panels"]
    require(len(panels) == 100, "100 probability panels")
    keys = ("raw", "D", "rho", "beta", "H", "theta")
    maxima = {key: F(-1) for key in keys}
    nonempty = 0
    incidence = 0
    for index, panel in enumerate(panels):
        require(rational(panel["pl"]) == F(index, 100)
                and rational(panel["pu"]) == F(index + 1, 100), "exact closed panel endpoints")
        require(type(panel["cells"]) is int and panel["cells"] >= 0, "integer incidence")
        incidence += panel["cells"]
        values = {key: rational(panel[key]) for key in keys}
        if not panel["cells"]:
            require([values[key] for key in keys] == [-1, -1, 1, 0, 0, 0], "empty panel")
            continue
        nonempty += 1
        require(values["raw"] <= F("2.1995174") and values["D"] <= F("0.76682509"),
                "every nonempty panel's printed resources")
        require(values["beta"] <= F("0.50549963") and values["H"] <= F("1.83605680"),
                "every nonempty panel's printed beta and phase")
        require(0 <= values["theta"] < 1, "theta domain")
        for key in keys:
            maxima[key] = max(maxima[key], values[key])
    require(nonempty == 30, "printed nonempty census")
    # The export rounds rho up to 1e-8. The sharper rational theorem bound
    # follows instead from the exact identities of surviving original rows.
    require(maxima["rho"] >= rho and maxima["rho"] - rho < F(1, 10**8),
            "panel rho rounding distinguished from exact theorem endpoint")
    return {
        "input_sha256": sha256(blob).hexdigest(), "stages": census,
        "nominal_boxes": nominal_boxes, "nonempty_panels": nonempty,
        "panel_incidence": incidence,
        "final_row_maxima": {"raw": str(raw), "D": str(defect),
                             "weighted_nD": str(42 * defect), "rho": str(rho),
                             "radius": str(radius)},
        "panel_maxima": {key: str(value) for key, value in maxima.items()},
    }


def p1(a, b):
    return b**3 / 3 + a * b**2 / 2 - a**3 / 6


def delicate_sign_and_endpoint_diagnostics():
    # Independent exhaustive rational samples supplement the derivative proof
    # in the audit. They are not a continuous-domain certificate.
    checked = 0
    for a0, a1 in [(F(1, 3), F(5, 3)), (F(3, 2), F(2))]:
        for b0, b1 in [(F(1, 4), F(2, 3)), (F(2), F(3))]:
            ml, mu = F(1, 5), F(2, 5)
            poly_lo = min(p1(a0, b0), p1(a1, b0))
            poly_hi = p1(max(a0, min(a1, b1)), b1)
            product_lo = poly_lo * (ml if poly_lo >= 0 else mu)
            product_hi = poly_hi * (mu if poly_hi >= 0 else ml)
            for ia in range(9):
                a = a0 + (a1 - a0) * F(ia, 8)
                for ib in range(9):
                    b = b0 + (b1 - b0) * F(ib, 8)
                    for im in range(9):
                        m = ml + (mu - ml) * F(im, 8)
                        require(product_lo <= m * p1(a, b) <= product_hi,
                                "sign-aware central product")
                        checked += 1
    negative = p1(F(3, 2), F(2, 3))
    require(negative < 0, "negative central polynomial witness")
    require(F(1, 5) * negative > F(2, 5) * negative,
            "negative control: upper m gives false upper bound")

    # A necessary interval reduced to a boundary point belongs to both
    # incident closed panels; replacing <= by < would miss both incidences.
    point = F(1, 2)
    closed = [j for j in range(100) if max(point, F(j, 100)) <= min(point, F(j + 1, 100))]
    strict = [j for j in range(100) if max(point, F(j, 100)) < min(point, F(j + 1, 100))]
    require(closed == [49, 50] and strict == [], "shared endpoint negative control")

    # A 2x2 PSD condition u*v >= w^2 permits u=w=0; u=0,w>0
    # contradicts it for every finite v. Dropping 0/0 is harmless, whereas
    # dividing it or assigning a positive correction would be unjustified.
    require(0 * F(7) >= 0**2 and not 0 * F(7) >= F(1, 10)**2,
            "zero denominator PSD semantics")
    return {"rational_product_points": checked, "negative_P1": str(negative),
            "closed_boundary_panels": closed, "strict_boundary_panels": strict,
            "negative_controls": ["incorrect negative-product multiplier",
                                  "strict shared-endpoint intersection",
                                  "zero PSD denominator with nonzero numerator"]}


def exact_law_diagnostics():
    # All masses and atoms are rational and have exactly mean 0, variance 1.
    laws = {
        "symmetric_binary": {F(-1): F(1, 2), F(1): F(1, 2)},
        "skew_binary": {F(-1, 2): F(4, 5), F(2): F(1, 5)},
        "binary_negative_P1": {F(-3, 2): F(4, 13), F(2, 3): F(9, 13)},
        "zero_atom": {F(-2): F(1, 6), F(0): F(1, 2), F(1): F(1, 3)},
        "small_zero_atom": {F(-6, 5): F(25, 66), F(0): F(1, 6), F(1): F(5, 11)},
    }
    checked = []
    zero_denominators = 0
    for name, law in laws.items():
        ex = lambda f: sum(weight * f(atom) for atom, weight in law.items())
        require(sum(law.values()) == 1 and ex(lambda x: x) == 0
                and ex(lambda x: x*x) == 1, "standardized actual law")
        R = max(abs(x) for x in law)
        rho = ex(lambda x: abs(x)**3)
        gamma = ex(lambda x: x**3)
        beta = ex(lambda x: x*abs(x))
        m = ex(lambda x: max(x, 0))
        m4 = ex(lambda x: x**4)
        m5 = ex(lambda x: abs(x)**5)
        delta = gamma - rho * beta
        require(m4 >= rho*rho + delta*delta/(1-beta*beta), "projection")
        require(4*m*m + beta*beta <= 1, "common first moment")
        first_correction = fourth_correction = fifth_correction = F(0)
        for sign in (-1, 1):
            moment = lambda power: ex(lambda x: max(sign*x, 0)**power)
            a, b, c, f = [moment(power) for power in (2, 3, 4, 5)]
            deficit = R*a-b
            low_deficit = R*m-a
            require(a*a <= m*b, "semimoment Cauchy")
            if deficit:
                first_correction += low_deficit**2/deficit
                fifth_correction += (R*b-c)**2/deficit
                require(f <= R*c-(R*b-c)**2/deficit, "fifth localizing matrix")
            else:
                zero_denominators += 1
                require(low_deficit == 0 and R*b-c == 0, "zero numerator compatibility")
            if low_deficit:
                fourth_correction += deficit**2/low_deficit
            else:
                require(deficit == 0, "zero fourth denominator compatibility")
        require(2*m + first_correction <= R, "first localizing matrices")
        require(m4 <= R*rho - fourth_correction, "fourth localizing matrices")
        require(m5 <= R*m4-fifth_correction, "summed fifth localizing matrices")
        loss1 = delta**4/(4*rho*(1-beta*beta)**2)
        loss2 = ((rho+gamma)*max(delta, 0)**2/(8*(1+beta)**2)
                 + (rho-gamma)*max(-delta, 0)**2/(8*(1-beta)**2))
        loss3 = delta*delta/(8*m)
        require(rho*m4/2-m5/4 <= rho**3/4-max(loss1, loss2, loss3), "maximum of independent losses")
        p = sum(weight for atom, weight in law.items() if atom > 0)
        q = sum(weight for atom, weight in law.items() if atom < 0)
        probability = sum(px*py for x, px in law.items() for y, py in law.items() if x*y < 0)
        numerator = sum(px*py*(x-y)**2 for x, px in law.items() for y, py in law.items() if x*y < 0)
        require(probability == 2*p*q, "actual opposite-sign event probability")
        if F(0) not in law:
            expression = (1+4*m*m+beta)/(2*p) + (1+4*m*m-beta)/(2*q)
            require(p+q == 1 and p*q >= m*m and numerator/probability == expression,
                    "conditional second moment identity and variance bound")
        else:
            require(p+q < 1, "zero atom must be excluded before q=1-p")
        checked.append(name)
    return {"actual_laws": checked, "zero_localizing_denominators": zero_denominators,
            "scope": "Exact finite diagnostic laws; continuous implications are proved in signed-audit.md."}


if __name__ == "__main__":
    require(__debug__ and not sys.flags.optimize, "unoptimized Python")
    require(len(sys.argv) == 2, "usage: check_entry_claims.py path/to/entry-proof.json")
    path = Path(sys.argv[1])
    result = {"status": "PASS_FIXED_ENTRY_PRINTED_CLAIMS",
              "proof_targets": exported_targets(path),
              "delicate_semantics": delicate_sign_and_endpoint_diagnostics(),
              "actual_laws": exact_law_diagnostics()}
    print(json.dumps(result, indent=2))

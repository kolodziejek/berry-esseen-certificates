#!/usr/bin/env python3
"""Bounded, independent Fraction calculation; never imports archive programs.

This checks a new conditional resource consequence, not acquisition or LOCAL42.
The companion note supplies the analytic score-chord and weighted-resource proof.
"""
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[3]
ARCHIVE = "verification/finite-tail/sources/backend.zip"
ARCHIVE_SHA = "43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52"
MANIFEST_SHA = "c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf"
PREFIX = "work/toward40_20261007/audit43/capsule/work/below49_20261006/"
PINS = {
    "package_audit/left42_confinement/post_sperner42_exact.json": "d0a1f547aa4c181d4ad64e9db403ae566760137d1fe75caedc4f317c8aec2ace",
    "package_audit/left42_confinement/confinement42_proof.json": "b75c5bf10dfcc47b33d4e273a8591f0332feb6351251fb65bc21928cb597bd40",
    "package_audit/left42_confinement/profiles42_proof.json": "2f275bf59e018bac8f53327e1649a71b1c13e30d7e70171a6c8664c4f7bddcdd",
    "package_audit/left42_confinement/contracted_kernel.py": "b216161eec801c96a77df81fb77771e86e6ab55f0fc1b14cd2428508191a3dfc",
    "package_audit/left42_confinement/coupled_panel_core.py": "adb21a5ee493fc9c257aa3ba67cdf1a162a841d40798d3e423bd2bc93a16aa3e",
    "package_audit/left42_confinement/corrected_phase_callback_extended.py": "036d32989f9c522e9d6151cf8898338e13ed2c9790a5d2c003bff095df270a63",
    "package_audit/left42_confinement/confinement_core.py": "c42762298dbb32dacf8c10e777c26c24dc38616f46c702679257aeb2a3d289af",
    "package_audit/left42_confinement/profile_core.py": "6ade623c27a16a79640978e5739270d748c45b006e6e82dbe4d592f5336924e5",
    "package_audit/left42_confinement/accept_profiles.py": "2ca74e873b36f305549f2bcaa46a0792c6fca1ee229343feceb209facd8ca9ef",
    "local/left42_final/actual_float_targets.json": "9244aee2e0eef320915fb41d1ac3fccaaf1300c25ca686f361602a251d8ec563",
    "local/left42_final/central42_contract.py": "10868c085cf69e6a0b1db01b6bcf638e2a13863db088bc966754ae44c22e2167",
    "local/left42_final/mid42_contract.py": "e3ff07f66e35a24028a4d7136cb4b36149646da1046efbd48541da918cdd4956",
    "local/left42_final/bind_low42.py": "b21670bda62bcc2a97dad1f58a4e89eaf4e3e0907ba1b5de192f4c2f1617ec3c",
    "acquisition/central42_confinement_candidate.json": "2f95d0271996eb9868c2fffcdfb0fa2646a99c2cf588e70d063178e27d07246d",
    "acquisition/central42_profiles_candidate.json": "5667786996a88f241225d53d99ec28a797c9f37a874a74d4f51e5c28f86a7336",
    "acquisition/central42_acquisition_core.py": "edd75b67061e484ba62e0266101c9fe3f98af8d15ac26218a259c630261b37ce",
    "acquisition/central42_confinement_core.py": "6c70e17dd81811d16f4bcc267db2a5a3aaac39f95552c065e93411ef79a79c8c",
    "acquisition/central42_profile_core.py": "b015459decb4dc7d17423ee4361fe8f105706fafa9b08568bd3f3953dafeecb3",
    "acquisition/coupled_panel_core.py": "f3ff3321f3b47486d58248c245ec83e376d517e88ff2508aa814a724870d78fc",
    "acquisition/corrected_phase_callback_v2.py": "65b91b83fd888aea1b01bfe6f16040fc1b51b9ced1520a866aa82778bfd4a2d6",
    "acquisition/kernel.py": "d71f58b7527c3cf6d2146d816e5d124f6f331d1b153e5aaedee5182707647f12",
    "acquisition/contracted_kernel.py": "0367aae733dfe2d6467188d941d6fc8ccd7bb6f4bf3aa4c98dca3c4781534d22",
}
N, C0, CHI = 42, F(".4095"), F(".40974")
SL, SU = F("3.162277660"), F("3.162277661")
THRESHOLDS = tuple(map(F, (".05", ".08", ".10", ".12")))
FIELDS = ("A", "Fplus", "Fminus", "Qbudget")


def need(condition, message):
    if not condition:
        raise ValueError(message)


def roots(x):
    need(x >= 0, "nonnegative radicand")
    scale = 10**8
    k = isqrt(x.numerator * scale**2 // x.denominator)
    low, high = F(k, scale), F(k + 1, scale)
    need(low**2 <= x < high**2, "outward root enclosure")
    return low, high


def upper_decimal(x, digits=9):
    scale = 10**digits
    q = -((-x.numerator * scale) // x.denominator)
    return f"{q // scale}.{q % scale:0{digits}d}"


def budget(quads):
    need(bool(quads), "nonempty quadratic list")
    values = []
    for q in quads:
        need(q["Qbudget"] > 0, "positive curvature")
        f = max(F(0), q["Fplus"], q["Fminus"])
        values.append(q["A"] + f**2 / (4 * q["Qbudget"]))
    return max(values)


def interpolate(quads, score):
    c0, c1 = quads[0]["C"], quads[2]["C"]
    need(c0 <= score <= c1, "score interpolation domain")
    alpha = (score - c0) / (c1 - c0)
    return [{k: (1-alpha)*quads[j][k] + alpha*quads[j+2][k]
             for k in FIELDS} for j in range(2)]


def geometry(row):
    l, u, t, a, b = (F(row[k]) for k in ("pl", "pu", "theta", "A", "B"))
    need(0 < l < u < F(1, 2) and 0 <= t < 1 and min(a, b) > 0,
         "same-law geometry domain")
    v = max(l*(1-l), u*(1-u))
    distance = max(F(0), (4-SU)/2-u, l-(4-SL)/2)
    binary = (6+2*SL)*roots((1-t)**3)[0]/roots(v)[1]*distance**2
    price = min(3*(SL+1)*b, 3*(SL+3)*a)
    need(price > 0, "positive variance price")
    return t, a+b, v, binary, price


def consequence(row, bound):
    t, gap, v, binary, price = geometry(row)
    d = min(F(row["D"]), F(15000, 997*N)*bound)
    residual = d-binary
    out = {"budget": bound, "D_new": d, "binary": binary,
           "residual": residual, "old_lambda": F(row["lambda_max"])}
    if residual < 0:
        out.update(excluded=True, new_lambda=None, new_inward=None, crossings=[])
    else:
        need(residual > 0, "zero residual needs separate Bernoulli assembly")
        lam = N*v*residual/(price*(1-t))
        inward = residual/(6*(1-t)*gap)
        need(lam <= F(row["lambda_max"]) and inward <= F(row["inward_d_max"]),
             "both coherent intercepts tighten")
        out.update(excluded=False, new_lambda=lam, new_inward=inward,
                   lambda_upper_decimal=upper_decimal(lam),
                   crossings=[x for x in THRESHOLDS if F(row["lambda_max"]) >= x > lam])
    return out


def validate_left(obj):
    need(type(obj["N"]) is int and obj["N"] == 42 and obj["L"] == 48,
         "original finite metadata")
    need(len(obj["rows"]) == 45, "complete left table")
    for i, row in enumerate(obj["rows"]):
        need([F(row[k]) for k in ("pl", "pu")] == [F(145+i,500), F(146+i,500)],
             "ordered complete probability panels")
        q = [{k: F(v) for k, v in x.items()} for x in row["quadratics"]]
        need(len(q) == 4, "all four corners")
        need([x["C"] for x in q] == [C0, C0, F(".4226"), F(".4226")],
             "same score endpoints")
        need(q[0]["rho"] == q[2]["rho"] <= q[1]["rho"] == q[3]["rho"],
             "paired coherent moment corners")
        need(q[0]["rho"] >= 1, "positive actual moment floor")
        need(CHI+F(row["raw"])/N >= F(".4226"), "actual high score cap saturated")
        for j in range(2):
            for key in ("Qraw", "Qbudget"):
                need(q[j+2][key]-q[j][key] == (F(".4226")-C0)*q[j]["rho"],
                     "affine curvature identity")
            extra = (1-F(5,2)*F(row["raw"])/N)*(C0*q[j]["rho"]-F(row["D"])/15)/2
            need(q[j]["Qbudget"]-q[j]["Qraw"] == extra > 0,
                 "single conserved curvature charge")
        t, gap, v, binary, price = geometry(row)
        residual = F(row["D"])-binary
        need(N*v*residual/(price*(1-t)) == F(row["lambda_max"]),
             "exact original joint noise reconstruction")
        need(residual/(6*(1-t)*gap) == F(row["inward_d_max"]),
             "exact original joint inward reconstruction")


def left_result(row):
    q = [{k: F(v) for k, v in x.items()} for x in row["quadratics"]]
    middle = budget(interpolate(q, CHI))
    low = budget(q[:2])
    high = budget(q[2:])-N*(q[2]["C"]-CHI)  # universal actual rho >= 1 suffices
    need(middle >= max(low, high), "middle endpoint dominates charged endpoints")
    out = consequence(row, middle)
    out.update(low_endpoint=low, charged_high_endpoint=high)
    return out


def central_result(row):
    # bounded() rounds raw up by less than 2e-6 and A,F up / Q down.
    # Do not treat a rounded raw value as the exact high score endpoint.
    raw = F(row["raw"])
    c1low = min(F(".4247"), CHI+(raw-F(2,10**6))/N)
    c1high = min(F(".4247"), CHI+raw/N)
    need(C0 < CHI < c1low <= c1high, "central score endpoint interval")
    alphas = ((CHI-C0)/(c1high-C0), (CHI-C0)/(c1low-C0))
    q = [{k: F(v) for k, v in x.items()} for x in row["quadratics"]]
    need(len(q) == 4, "central four outward corners")
    mid = []
    for j in range(2):
        values = {k: [(1-a)*q[j][k]+a*q[j+2][k] for a in alphas] for k in FIELDS}
        mid.append({k: (min(v) if k == "Qbudget" else max(v)) for k,v in values.items()})
    middle = budget(mid)
    low = budget(q[:2])
    high = budget(q[2:])-N*(c1low-CHI)  # actual rho >= 1
    need(middle >= max(low, high), "central middle dominates charged endpoints")
    out = consequence(row, middle)
    out.update(score_endpoint_low=c1low, score_endpoint_high=c1high,
               low_endpoint=low, charged_high_endpoint=high)
    return out


def encode(obj):
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, dict):
        return {k: encode(v) for k,v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [encode(v) for v in obj]
    return obj


def main():
    need(not sys.flags.optimize and __debug__ and len(sys.argv) == 1, "fixed unoptimized invocation")
    blob = (ROOT/ARCHIVE).read_bytes()
    need(sha256(blob).hexdigest() == ARCHIVE_SHA, "archive SHA256")
    with zipfile.ZipFile(ROOT/ARCHIVE) as archive:
        mb = archive.read("finite61/MANIFEST.json")
        need(sha256(mb).hexdigest() == MANIFEST_SHA, "manifest SHA256")
        files = json.loads(mb)["files"]
        data = {}
        for path, digest in PINS.items():
            need(files[PREFIX+path]["sha256"] == digest, "manifest path binding")
            b = archive.read("finite61/blobs/"+digest)
            need(sha256(b).hexdigest() == digest, "blob SHA256")
            if path.endswith(".json"):
                data[path] = json.loads(b)
    left = data["package_audit/left42_confinement/post_sperner42_exact.json"]
    parent = data["package_audit/left42_confinement/confinement42_proof.json"]
    profiles = data["package_audit/left42_confinement/profiles42_proof.json"]
    need(left["rows"] == [x["final"] for x in parent["rows"]], "post table equals confinement outputs")
    need(profiles["source_sha256"] == PINS["package_audit/left42_confinement/post_sperner42_exact.json"], "left profile parent binding")
    validate_left(left)
    need(SL**2 < 10 < SU**2, "sqrt10 enclosure")
    def atan_sum(x, terms):
        return sum(((-1)**i*x**(2*i+1)/F(2*i+1) for i in range(terms)), F(0))
    pi_low = 16*atan_sum(F(1,5),6)-4*atan_sum(F(1,239),1)
    pi_high = 16*atan_sum(F(1,5),5)-4*atan_sum(F(1,239),2)
    need(pi_low > F("3.14159"), "Machin lower bound")
    need((19+6*SL)/(72*pi_high) > C0**2, "Esseen constant lower bound")
    need((19+6*SU)/(72*pi_low) < CHI**2, "Esseen constant upper bound")
    lr = [dict(index=i, p=[row["pl"],row["pu"]], **left_result(row))
          for i,row in enumerate(left["rows"])]
    central = data["acquisition/central42_confinement_candidate.json"]
    cp = data["acquisition/central42_profiles_candidate.json"]
    need(cp["source_sha256"] == PINS["acquisition/central42_confinement_candidate.json"], "central profile parent binding")
    need(central["N"] == 42 and len(central["rows"]) == 47, "central table floor and size")
    cr = []
    for i,row in enumerate(central["rows"]):
        need(type(row["index"]) is int and row["index"] == i and
             [F(row[k]) for k in ("pl","pu")] == [F(190+i,500),F(191+i,500)], "central complete ordered panels")
        cr.append(dict(index=i, p=[row["pl"],row["pu"]], **central_result(row)))
    need([r["index"] for r in lr if r["excluded"]] == [0], "only row0 excluded")
    need([(r["index"],r["crossings"]) for r in lr if r["crossings"]] ==
         [(5,[F(".05")]),(8,[F(".08")]),(10,[F(".10")]),(13,[F(".12")])], "all left named crossings")
    need([(r["index"],r["crossings"]) for r in cr if r["crossings"]] == [(28,[F(".10")])], "all central named crossings")
    profile_drops = []
    for i,row in enumerate(profiles["rows"]):
        if lr[i]["excluded"]:
            continue
        for band in row["profiles"]:
            lo = F(band["requested_noise"][0])
            if lr[i]["new_lambda"] < lo and band["source"] == "joint_resource_profile":
                need(len(band["signs"]) == 2, "two signed profile calls")
                profile_drops.append(dict(index=i, lower=lo, signed_calls=2))
    need(profile_drops == [dict(index=10,lower=F(".1"),signed_calls=2),
                           dict(index=13,lower=F(".12"),signed_calls=2)], "exact profile arithmetic candidates")
    controls = []
    def rejected(name, action):
        try:
            action()
        except (ValueError, KeyError, IndexError, ZeroDivisionError):
            controls.append(name)
        else:
            raise ValueError("negative control accepted: "+name)
    def mutation(name, change):
        obj = deepcopy(left)
        change(obj)
        rejected(name, lambda: validate_left(obj))
    mutation("missing_panel", lambda o:o["rows"].pop())
    mutation("reordered_panels", lambda o:o["rows"].reverse())
    mutation("wrong_score_endpoint", lambda o:o["rows"][0]["quadratics"][2].update(C=".42"))
    mutation("mismatched_moment_corner", lambda o:o["rows"][0]["quadratics"][2].update(rho="1"))
    mutation("corrupt_curvature", lambda o:o["rows"][0]["quadratics"][2].update(Qbudget="100"))
    mutation("false_noise_intercept", lambda o:o["rows"][0].update(lambda_max="1/100"))
    qs = [{k:F(v) for k,v in x.items()} for x in left["rows"][0]["quadratics"]]
    rejected("extrapolation_instead_of_interpolation", lambda: interpolate(qs,F(".43")))
    rejected("delete_next_MID_row", lambda:need(lr[6]["new_lambda"]<F(".05"),"row6 survives"))
    rejected("delete_next_LOW_row", lambda:need(lr[9]["new_lambda"]<F(".08"),"row9 survives"))
    rejected("delete_central_LOW_boundary", lambda:need(cr[38]["new_lambda"]<F(".05"),"central38 survives"))
    rejected("negative_residual_is_positive_noise_domain", lambda:need(lr[0]["residual"]>=0,"row0 excluded"))
    rejected("positive_excess_charge_at_equality", lambda:need(F(0)>0,"equality permits e=0"))
    output = dict(status="PASS_BOUNDED_CONDITIONAL_RESOURCE_ARITHMETIC",
                  mathematical_status="conditional on original same-law acquisition, phase resource and uniform-scope bridge",
                  execution_scope="new Fraction algebra only; no archived program imported or executed",
                  archive_sha256=ARCHIVE_SHA,manifest_sha256=MANIFEST_SHA,
                  source_pins={PREFIX+k:v for k,v in PINS.items()},
                  pi_lower=pi_low,pi_upper=pi_high,score_lower=C0,score_upper=CHI,
                  left=lr,central=cr,profile_arithmetic_candidates=profile_drops,
                  rejected_controls=controls)
    print(json.dumps(encode(output),indent=2,sort_keys=True))


if __name__ == "__main__":
    main()

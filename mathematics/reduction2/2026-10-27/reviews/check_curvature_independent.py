#!/usr/bin/env python3
"""Independent bounded review of the new helper, never archive execution.

The oracle partitions at every kink and optimizes each smooth piece. This
differs from the helper's reduced endpoint/stationary-candidate implementation.
The review note gives the continuous proof and the conditional transport scope.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from types import ModuleType
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[4]
TARGET = "mathematics/reduction2/2026-10-27/check_local_curvature.py"
TARGET_SHA = "3e3a35c30af20201fc5b3143f40f1439c235b7bfd4dd702f4fa8348356ff70dc"
ARCHIVE = "verification/finite-tail/sources/backend.zip"
ARCHIVE_SHA = "43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52"
MANIFEST_SHA = "c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf"
PREFIX = "work/toward40_20261007/audit43/capsule/work/below49_20261006/"
TABLES = {
    "central42_v2": ("local/central42_v2/new_central42_targets.json", "c281ad46d97c0c5054609a88727c079e509fa1e07837bb856d470d7e2171f1c0"),
    "left42_final": ("local/left42_final/actual_float_targets.json", "9244aee2e0eef320915fb41d1ac3fccaaf1300c25ca686f361602a251d8ec563"),
}


def need(ok, text):
    if not ok:
        raise ValueError(text)


def fun(b, c, u):
    first = F(0) if b+u <= 1 else (b+u-1)/(c-u)**2
    if b+u <= 0:
        second = F(0)
    elif u <= c/3:
        second = (b+u)/(c+u)**2
    else:
        second = 9*(b+u)/(16*c*c)
    return first+second


def piecewise_oracle(b, c, low, high):
    cuts = sorted(set([low, high]+[u for u in (-b, 1-b, c/3) if low <= u <= high]))
    choices = [(u, fun(b,c,u)) for u in cuts]
    for left, right in zip(cuts, cuts[1:]):
        middle = (left+right)/2
        if 0 < b+middle < 1 and middle < c/3:
            root = c-2*b
            if left < root < right:
                choices.append((root,fun(b,c,root)))
        # Otherwise the summand is zero/linear, or the active first summand
        # lies in the convex regime established in the review proof.
    return max(value for _,value in choices)


def module_from_text(source):
    mod = ModuleType("curvature_review_target")
    exec(compile(source, TARGET, "exec"), mod.__dict__)
    return mod


def main():
    need(not sys.flags.optimize and __debug__, "unoptimized Python")
    source = (ROOT/TARGET).read_text()
    need(sha256(source.encode()).hexdigest() == TARGET_SHA, "reviewed helper source")
    target = module_from_text(source)
    # 7*27*45 = 8,505 exact tests, including all singleton intervals.
    cs = [F(500001,10**6),F(51,100),F(3,5),F(3,4),F(9,10),F(999999,10**6),F(1)]
    bs = [F(j,5) for j in range(-10,17)]
    points = [F(j,8) for j in range(-4,5)]
    tests = 0
    for b in bs:
        for c in cs:
            for i,low in enumerate(points):
                for high in points[i:]:
                    wanted = piecewise_oracle(b,c,low,high)
                    actual, candidates = target.curvature_supremum(b,c,low,high)
                    need(actual == wanted, "helper differs from piecewise oracle")
                    need(all(low <= u <= high and fun(b,c,u) == value for u,value in candidates), "candidate membership and attained value")
                    tests += 1
    # Mutate copies of the new helper in memory. Never touch either source.
    controls = []
    def must_disagree(label, mutated, case):
        module = module_from_text(mutated)
        need(module.curvature_supremum(*case)[0] != piecewise_oracle(*case), label)
        controls.append(label)
    case = (F(2,5),F(9,10),F(0),F(1,5))
    old = "if c > b and lo <= stationary <= hi and stationary <= min(c/3, 1-b):"
    need(source.count(old) == 1, "stationary mutation anchor")
    must_disagree("omitted_stationary_candidate",source.replace(old,"if False:"),case)
    old = "1/(4*(c-b))"
    need(source.count(old) == 1, "value mutation anchor")
    must_disagree("wrong_stationary_value",source.replace(old,"1/(3*(c-b))"),case)
    old = "(c+min(u, c/3))**2"
    need(source.count(old) == 1, "truncation mutation anchor")
    must_disagree("omitted_denominator_truncation",source.replace(old,"(c+u)**2"),
                  (F(2,5),F(3,5),F(1,2),F(1,2)))
    # The floor and mass controls are counterexamples to invalid replacements.
    N, n = 42, 84
    need(F(-1,n) > F(-1,N), "negative correction cannot use floor unclamped")
    controls.append("unclamped_negative_correction")
    need(F(9,10) > F(7,10), "positive bracket invalidates lower mass replacement")
    controls.append("mass_lower_bound_with_positive_event")
    need(-F(7,10) > -F(9,10), "upper mass gives wrong direction for negative event")
    controls.append("mass_upper_bound_with_negative_event")
    need(fun(F(2,5),F(4,5),F(0)) > fun(F(2,5),F(9,10),F(0)), "decreasing-c cache reuse fails")
    controls.append("cache_used_in_reverse_c_order")
    # Rational Jensen checks supplement, but do not replace, the convexity proof.
    jensen = 0
    for a0 in (F(-2),F(-1,1000),F(0),F(2)):
        for a1 in (F(0),F(1,100),F(2)):
            for low,high in ((F(1,100),F(1,10)),(F(1,10),F(1)),(F(1),F(4))):
                def score(lam):
                    bracket=F(-20)+F(3)/(F(2)*lam+F(1,7))+F(1,9)*lam
                    return F(3,4)*bracket+max(F(0),a0+a1/lam)/42
                for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
                    need(score((1-t)*low+t*high) <= (1-t)*score(low)+t*score(high), "clamped score convexity diagnostic")
                    jensen += 1
    raw = (ROOT/ARCHIVE).read_bytes()
    need(sha256(raw).hexdigest() == ARCHIVE_SHA,"archive pin")
    with zipfile.ZipFile(ROOT/ARCHIVE) as archive:
        rawmanifest = archive.read("finite61/MANIFEST.json")
        need(sha256(rawmanifest).hexdigest() == MANIFEST_SHA,"manifest pin")
        manifest = json.loads(rawmanifest)
        tables = {}
        for family,(path,digest) in TABLES.items():
            need(manifest["files"][PREFIX+path]["sha256"] == digest,"table logical binding")
            rawtable=archive.read("finite61/blobs/"+digest)
            need(sha256(rawtable).hexdigest() == digest,"table bytes")
            tables[family] = json.loads(rawtable)["rows"]
    jobs = manifest["low_rows"]
    expected = {(family,i,s) for family,indices in (("central42_v2",range(39)),("left42_final",range(8,45))) for i in indices for s in (-1,1)}
    labels=[(x["family"],x["index"],x["sign"]) for x in jobs]
    need(len(labels)==152 and set(labels)==expected,"all producer labels exactly once")
    counts={"central42_v2":0,"left42_final":0}
    for job in jobs:
        family,index,sign=job["family"],job["index"],job["sign"]
        hc,oc=job["H_cells"],job["outer_phase_cells"]
        wanted=(32,16) if (family,index,sign)==("central42_v2",0,-1) else ((16,8) if family=="central42_v2" else (8,4))
        need((hc,oc)==wanted,"literal grid dispatch")
        row=tables[family][index]
        lower=F(".05") if family=="central42_v2" else F(".08")
        ceiling=F(row["lambda_max"])
        cuts=sorted({lower,ceiling}|{F(j,400) for j in range(20,75) if lower<F(j,400)<ceiling})
        need(cuts[0] < cuts[-1] and cuts[-1] < F(75,400),"bounded exact noise cuts")
        if family=="left42_final":
            multiplicity=len(cuts)-1
        else:
            def phase(x):
                return next(radius for upper,radius in [(F(".06"),F(".09")),(F(".08"),F(".14")),(F(".10"),F(".19")),(F(".12"),F(".29")),(F(1),F(".5"))] if x<upper)
            multiplicity=len({phase(x) for x in cuts[:-1]})
        counts[family]+=hc*oc*multiplicity
    need(counts=={"central42_v2":43136,"left42_final":77952},"potential key counts")
    print(json.dumps(dict(status="PASS_INDEPENDENT_BOUNDED_REVIEW",target_sha256=TARGET_SHA,
                         archive_sha256=ARCHIVE_SHA,manifest_sha256=MANIFEST_SHA,
                         piecewise_exact_cases=tests,mutations_and_false_rules_rejected=controls,
                         clamp_Jensen_diagnostics=jensen,producer_labels=152,
                         potential_keys_before_pruning=counts,
                         old_candidates_upper=64*sum(counts.values()),
                         new_candidates_upper=3*sum(counts.values()),
                         scope="new helper and algebra only; no archived module, LOW gate or native certificate execution"),indent=2))


if __name__ == "__main__":
    main()

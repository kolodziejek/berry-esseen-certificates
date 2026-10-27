#!/usr/bin/env python3
"""Bounded exact diagnostics for a proved LOW curvature supremum.

This does not import/execute archived programs or evaluate a LOW score gate.
The proof is in local-kernel.md. All numeric decisions use Fraction.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import argparse
import json
import sys
import zipfile

if not __debug__ or sys.flags.optimize:
    raise RuntimeError("unoptimized Python required")

PREFIX = "work/toward40_20261007/audit43/capsule/work/below49_20261006/"
PINS = {
    "local/central42_v2/central42_kernel.py": "9dc0754fe2dd4f2f7057247d3d62f3b71472c65a49d46f67d35fb0d66e3f8673",
    "local/left42_final/central42_kernel.py": "d025529aa2690c3cfc0f1c34a6af385d6fa69db8e069543057f29475cbb133c3",
    "local/central42_v2/central42_contract.py": "de30acd375d9d53d6a7068cd4b5397da6c775c21be29aca2e5c6b5da5f65a39f",
    "local/left42_final/central42_contract.py": "10868c085cf69e6a0b1db01b6bcf638e2a13863db088bc966754ae44c22e2167",
    "local/central42_v2/tiny42_normalization.py": "3650f39f618def7615d8be20ce8b9efd28e16202102fb8fa76dd8687deff4a6c",
    "local/central42_v2/new_central42_targets.json": "c281ad46d97c0c5054609a88727c079e509fa1e07837bb856d470d7e2171f1c0",
    "local/left42_final/actual_float_targets.json": "9244aee2e0eef320915fb41d1ac3fccaaf1300c25ca686f361602a251d8ec563",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def value(b, c, u):
    return max(F(0), b + u - 1)/(c-u)**2 + max(F(0), b+u)/(c+min(u, c/3))**2


def curvature_supremum(b, c, lo, hi):
    """Exact supremum, including the three kink collisions and endpoints."""
    require(all(type(x) is F for x in (b, c, lo, hi)), "exact Fraction input")
    require(F(1, 2) < c <= 1, "c in (1/2,1]")
    require(-F(1, 2) <= lo <= hi <= F(1, 2), "closed nearest-phase interval")
    candidates = [(lo, value(b, c, lo)), (hi, value(b, c, hi))]
    stationary = c - 2*b
    if c > b and lo <= stationary <= hi and stationary <= min(c/3, 1-b):
        candidates.append((stationary, 1/(4*(c-b))))
    return max(v for _, v in candidates), candidates


def old_envelope(b, c, lo, hi):
    """Literal outward formula at kernel159--167; no archived imports."""
    values = []
    for j in range(64):
        a = lo + (hi-lo)*F(j, 64)
        d = lo + (hi-lo)*F(j+1, 64)
        values.append(max(F(0), b+d-1)/(c-d)**2 + max(F(0), b+d)/(c+min(a, c/3))**2)
    return max(values)


def rational_mesh_checks(b, c, lo, hi, result):
    # A diagnostic only. The proof, not this mesh, covers the continuum.
    pts = [lo + (hi-lo)*F(i, 16) for i in range(17)]
    pts += [u for u in (-b, 1-b, c/3, c-2*b) if lo <= u <= hi]
    for u in pts:
        require(value(b, c, u) <= result, "sample escaped exact supremum")
    return len(pts)


def rootlo(q):
    return F(isqrt(q.numerator*10**16//q.denominator), 10**8)


def bands(row, kind):
    lm = F(row["lambda_max"])
    start = F(".05") if kind == "central" else F(".08")
    pts = sorted(set([start, lm] + [F(j, 400) for j in range(int(start*400)+1, int(lm*400)+1)]))
    ans = []
    for lo, hi in zip(pts, pts[1:]):
        if kind == "central":
            phase = F(".09") if lo < F(".06") else F(".14") if lo < F(".08") else F(".19") if lo < F(".10") else F(".29") if lo < F(".12") else F(".5")
        else:
            phase = F(".19") if lo < F(".10") else F(".27") if lo < F(".12") else F(".5")
        ans.append((lo, hi, phase))
    return ans


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", type=Path, required=True)
    args = ap.parse_args()
    rawzip = args.archive.read_bytes()
    require(sha256(rawzip).hexdigest() == "43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52", "archive pin")
    sources = {}
    with zipfile.ZipFile(args.archive) as z:
        manifest_raw = z.read("finite61/MANIFEST.json")
        require(sha256(manifest_raw).hexdigest() == "c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf", "manifest pin")
        manifest = json.loads(manifest_raw)
        for name, pin in PINS.items():
            require(manifest["files"][PREFIX+name]["sha256"] == pin, "manifest source pin")
            raw = z.read("finite61/blobs/"+pin)
            require(sha256(raw).hexdigest() == pin, "source byte pin")
            sources[name] = raw
    configs = 0
    checked = 0
    sample_points = 0
    stationary_cases = 0
    strict_improvements = 0
    potential_keys = {"central": 0, "left": 0}
    jobs = {}
    grid_counts = {}
    for job in manifest["low_rows"]:
        key = (job["family"], job["index"], job["sign"])
        require(key not in jobs, "unique manifest LOW row")
        require(type(job["H_cells"]) is int and job["H_cells"] > 0, "manifest H grid")
        require(type(job["outer_phase_cells"]) is int and job["outer_phase_cells"] > 0, "manifest phase grid")
        jobs[key] = job
        grid = str((job["H_cells"], job["outer_phase_cells"]))
        grid_counts[grid] = grid_counts.get(grid, 0) + 1
    seen_jobs = set()
    min_ratio = F(1)
    largest_absolute_improvement = F(0)
    selected = {}
    for kind, source in (("central", "local/central42_v2/new_central42_targets.json"), ("left", "local/left42_final/actual_float_targets.json")):
        rows = json.loads(sources[source])["rows"]
        cutoff = F(".05") if kind == "central" else F(".08")
        rows = [r for r in rows if F(r["lambda_max"]) > cutoff]
        selected[kind] = [r["index"] for r in rows]
        for row in rows:
            bs = bands(row, kind)
            p, q = map(F, row["p"])
            ell = rootlo((1-F(row["theta"]))/ (q*(1-q)))
            eh = rootlo(1/(p*(1-p))) + F(1, 10**8)
            require(ell > 0 and eh**2*p*(1-p) > 1, "span enclosures")
            for sign in (-1, 1):
                family = "central42_v2" if kind == "central" else "left42_final"
                key = (family, row["index"], sign)
                require(key in jobs, "manifest job for selected row/sign")
                seen_jobs.add(key)
                job = jobs[key]
                hc, oc = job["H_cells"], job["outer_phase_cells"]
                # Actual producer grid from the pinned manifest, not contract defaults.
                potential_keys[kind] += hc*oc*(len(set(x[2] for x in bs)) if kind == "central" else len(bs))
                configs += 1
                H = F(row["H_minus" if sign < 0 else "H_plus"])
                # Bounded selection: both edge noise bands, H first/middle/last,
                # and phase edge/zero-adjacent cells. No native score evaluation.
                for bi in sorted({0, len(bs)-1}):
                    low, high, phase = bs[bi]
                    c = 1-F(row["d0"])*(1-low/F(row["lambda_max"]))
                    for hj in sorted({0, (hc-1)//2, hc-1}):
                        hl, hh = H*F(hj, hc), H*F(hj+1, hc)
                        hs = (hl, hh) if sign > 0 else (-hh, -hl)
                        hqs = [h/e for h in hs for e in (ell, eh)]
                        b = q - min(hqs)
                        for oi in sorted({0, (oc-1)//2, oc//2, oc-1}):
                            lo = -phase+2*phase*F(oi, oc)
                            hi = -phase+2*phase*F(oi+1, oc)
                            exact, candidates = curvature_supremum(b, c, lo, hi)
                            old = old_envelope(b, c, lo, hi)
                            require(exact <= old, "new bound exceeds old grid")
                            require(any(v == exact and value(b, c, u) == exact for u, v in candidates), "supremum is attained")
                            sample_points += rational_mesh_checks(b, c, lo, hi, exact)
                            checked += 1
                            stationary_cases += len(candidates) == 3
                            strict_improvements += exact < old
                            if old:
                                min_ratio = min(min_ratio, exact/old)
                            largest_absolute_improvement = max(largest_absolute_improvement, old-exact)
    require(selected == {"central": list(range(39)), "left": list(range(8, 45))}, "all152 selected configurations")
    require(seen_jobs == set(jobs), "exact manifest producer label coverage")
    require(grid_counts == {"(32, 16)": 1, "(16, 8)": 77, "(8, 4)": 74}, "literal selected grid inventory")
    # Endpoint-only shortcut is false: the permitted interior maximum matters.
    b, c, lo, hi = F(2, 5), F(9, 10), F(0), F(1, 5)
    exact, _ = curvature_supremum(b, c, lo, hi)
    require(exact == F(1, 2) > max(value(b, c, lo), value(b, c, hi)), "endpoint-only negative control")
    require(value(b, c, F(1, 5)) != value(b, c, -F(1, 5)), "phase symmetry negative control")
    # Kinks, zero-length intervals, c=1 endpoint, negative b and large b.
    adversarial = [(F(0), F(1), -F(1, 2), F(1, 2)), (F(1, 3), F(1), F(1, 3), F(1, 3)), (F(-2), F(3, 4), -F(1, 2), F(1, 2)), (F(2), F(3, 4), -F(1, 2), F(1, 2)), (F(3, 5), F(9, 10), -F(1, 2), F(1, 2)), (F(2, 5), F(3, 5), -F(1, 2), F(1, 2))]
    for data in adversarial:
        exact, _ = curvature_supremum(*data)
        require(exact <= old_envelope(*data), "adversarial grid domination")
        sample_points += rational_mesh_checks(*data, exact)
    rejected = 0
    for data in [(b, F(1, 2), lo, hi), (b, F(11, 10), lo, hi), (b, c, hi, lo), (b, c, -F(3, 5), hi), (b, c, lo, F(3, 5)), (0.4, c, lo, hi)]:
        try:
            curvature_supremum(*data)
        except ValueError:
            rejected += 1
        else:
            raise ValueError("invalid domain accepted")
    # Exact algebraic checks of the floor clamp and endpoint convexity examples.
    for old_i, new_i in [(F(1, 100000), F(-1)), (F(3), F(2)), (F(1), F(0))]:
        require(new_i <= old_i and max(F(0), new_i) <= old_i, "floor clamp")
    print(json.dumps({
        "status": "PASS bounded exact diagnostics; analytic proof supplies continuous coverage",
        "selected_LOW_configurations": configs,
        "manifest_grid_configuration_counts": grid_counts,
        "manifest_low_rows_canonical_sha256": sha256(json.dumps(manifest["low_rows"], sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        "sampled_curvature_calls": checked,
        "rational_point_diagnostics": sample_points,
        "sampled_calls_with_stationary_candidate": stationary_cases,
        "sampled_calls_strictly_improved": strict_improvements,
        "minimum_new_over_old_ratio": str(min_ratio),
        "largest_absolute_improvement": str(largest_absolute_improvement),
        "potential_cache_keys_before_empty_pruning": potential_keys,
        "adversarial_cases": len(adversarial),
        "false_shortcuts_refuted": 2,
        "malformed_domains_rejected": rejected,
        "source_pins": PINS,
        "scope": "curvature supremum only; no LOW score gates, no native execution, no certificate replacement",
    }, indent=2))


if __name__ == "__main__":
    main()

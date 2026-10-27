#!/usr/bin/env python3
"""Bounded exact scalar arithmetic and read-only finite61 source inventory.

This does not import or run archived code or certify LOCAL42/LOCAL47.
Run from any directory with unoptimized Python 3; no arguments are accepted.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import sys
import zipfile

if sys.flags.optimize or not __debug__:
    raise RuntimeError("Unoptimized Python required")
if len(sys.argv) != 1:
    raise ValueError("No overrides")

def need(ok, why):
    if not ok:
        raise ValueError(why)

ROOT = Path(__file__).resolve().parents[3]
ARCHIVE = ROOT / "verification/finite-tail/sources/backend.zip"
MANIFEST_SHA = "c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf"
PINS = {
    "/proofs/cutoff44.tex": "41af93935e4ebe64e38670bab222b1f8447b5dd7d95b3dc205ffc97236114f2b",
    "/acquisition/check_local42_support.py": "343046eaf0a3e6b2e140644cee19b7764d76b4171b844eaac27fb1a288b12d2e",
    "/acquisition/heat_support50.py": "650d7f3617775102fe92977605dfda5fb68a11e0ad738eb799aab77bc4a79e18",
    "/acquisition/fifth_heat50.py": "09a6e27ef42847cef0ac258504546eaef3a3035e83171143f1c2fd848736ac6c",
    "/acquisition/accept_initial42.py": "aa759c74fbd9ad39618264ef51b961f13c7833faa77a7f7b33309c27a7cee032",
    "/acquisition/local_signed_core.py": "f0c2df790b794413e7fd08c4f3fc20f79c15c27a6456c8eae5013b96eb093c11",
    "/acquisition/central42_acquisition_core.py": "edd75b67061e484ba62e0266101c9fe3f98af8d15ac26218a259c630261b37ce",
    "/acquisition/panel_exterior.py": "98894be48c3523c6f2e8d9f25d45d008ef1bc361f6ca9c00355c16939c86f0b7",
    "/acquisition/central42_confinement_core.py": "6c70e17dd81811d16f4bcc267db2a5a3aaac39f95552c065e93411ef79a79c8c",
    "/acquisition/central42_profile_core.py": "b015459decb4dc7d17423ee4361fe8f105706fafa9b08568bd3f3953dafeecb3",
    "/package_audit/left42_exact/accept_acquisition.py": "a565247f6587f3bb07dd67ef2100d08f70aebbe7543937f1ab98f8d09cf31eb6",
    "/package_audit/left42_exact/panel_exterior42.py": "98dbde39a9eb1464293eba2949d74f010313b7ea6abe5bdaef96174a988c6942",
    "/package_audit/left42_confinement/confinement_core.py": "c42762298dbb32dacf8c10e777c26c24dc38616f46c702679257aeb2a3d289af",
    "/local/central42_v2/central42_contract.py": "de30acd375d9d53d6a7068cd4b5397da6c775c21be29aca2e5c6b5da5f65a39f",
    "/local/left42_final/central42_contract.py": "10868c085cf69e6a0b1db01b6bcf638e2a13863db088bc966754ae44c22e2167",
    "/entry/check_support42_48.py": "a51a70f459a4f3cd1fb5d2cbd561baa2cd6fdfadd30aa132222dbd04dbc4ca7d",
}

# Endpoint inequalities: monotonicity in n>=43 is proved in finite-entry.md.
N, s = 43, F(253, 250)
square_surplus = (N - 1) * 253**2 - N * 250**2
need(square_surplus == 878 and s*s > F(N, N-1), "sqrt endpoint")
need(N-1 > 6**2, "heat denominator")
B = F(N, N-1) * (F(41, 200) + s/F(15) + 2*s/F(150))
need(B == F(102469, 350000) < F(3, 10), "scalar excess")
need(F(3, 10) - B == F(2531, 350000), "scalar strict reserve")
own = F(41, 100) + F(3, 10*N)
need(own == F(1793, 4300) < F(".4226") < F(".4247"), "own score")
need(F(".4226") - own == F(1209, 215000), "own strict reserve")
need(F(41, 100) < F(".4253"), "both deleted scores")
need(F(3, 10) < F(".54") < F(".7"), "excess inclusion")
need(F(0) <= F(".19"), "zero decrement")
# A different rational envelope also reaches42; do not extrapolate253/250.
s42 = F(81, 80)
need(41*81**2 - 42*80**2 == 201 and s42*s42 > F(42,41), "sqrt endpoint42")
need(41 > 6**2, "heat denominator42")
B42 = F(42,41)*(F(41,200)+s42/F(15)+2*s42/F(150))
need(B42 == F(3003,10250) < F(3,10), "scalar excess42")
need(F(3,10)-B42 == F(36,5125), "scalar reserve42")
own42 = F(41,100)+F(3,420)
need(own42 == F(73,175) < F(".4226"), "own score42")
negative_controls = []
for label, false_claim in [
    ("same sqrt bound at42", F(42, 41) < s*s),
    ("old1.011 sqrt bound at43", F(43, 42) < F(1011, 1000)**2),
    ("this coarse bound proves .29", B < F(29, 100)),
    ("support window extends49", 42 <= 49 <= 48),
]:
    try:
        need(false_claim, label)
    except ValueError:
        negative_controls.append(label)
    else:
        raise ValueError("False control accepted: " + label)

with zipfile.ZipFile(ARCHIVE) as z:
    raw = z.read("finite61/MANIFEST.json")
    need(sha256(raw).hexdigest() == MANIFEST_SHA, "manifest pin")
    m = json.loads(raw)
    sources = []
    for suffix, expected in PINS.items():
        matches = [p for p in m["files"] if p.endswith(suffix)]
        need(len(matches) == 1, "unique source " + suffix)
        path = matches[0]
        actual = m["files"][path]["sha256"]
        need(actual == expected, "source map pin " + suffix)
        content = z.read("finite61/blobs/" + actual)
        need(sha256(content).hexdigest() == expected, "source bytes " + suffix)
        sources.append(dict(path=path, sha256=expected, lines=len(content.splitlines())))
    actions = m["actions"]
    need(len(actions) == 31, "complete native inventory")
    ids = [a["id"] for a in actions]
    need(len(set(ids)) == 31, "unique native labels")
    bypass = ids[:6] + ids[25:]
    retained = ids[6:25]
    need(all(x.startswith("44.entry/") for x in ids[:6]), "ceiling prefix")
    need(all(x.startswith("43.") for x in ids[25:]), "special43 suffix")
    need(ids[6] == "44.acquisition/local42_initial_support01", "retain initial support")
    need(ids[24] == "44.package_audit/left42_profiles_accept01", "retain profiles")
    need(len(retained) == 19 and len(bypass) == 12, "new composition inventory partition")
    low = m["low_rows"]
    expected = {(family, i, sign)
                for family, indices in [("central42_v2", range(39)), ("left42_final", range(8,45))]
                for i in indices for sign in (-1, 1)}
    observed = [(x["family"], x["index"], x["sign"]) for x in low]
    need(len(observed) == len(set(observed)) == 152 and set(observed) == expected,
         "all retained LOW row labels")
    for family, count in [("central42_v2", 78), ("left42_final", 74)]:
        need(sum(x["family"] == family for x in low) == count, "LOW family count")

print(json.dumps(dict(
    status="PASS_BOUNDED_FINITE_ENTRY_SCALAR_AND_INVENTORY",
    mathematical_scope="Exact scalar arithmetic and static source identity only; conditional theorem proved in prose; native/local predicates not executed or certified.",
    scalar=dict(n_floor=N,sqrt_upper=str(s),square_surplus=square_surplus,
                excess_upper=str(B),excess_margin=str(F(3,10)-B),own_upper=str(own)),
    scalar42=dict(n_floor=42,sqrt_upper=str(s42),square_surplus=201,
                  excess_upper=str(B42),excess_margin=str(F(3,10)-B42),own_upper=str(own42)),
    negative_controls=negative_controls,
    source_manifest_sha256=MANIFEST_SHA,sources=sources,
    retained_native=retained,bypassed_native_in_new_composition=bypass,
    retained_low=dict(central42_v2=78,left42_final=74,total=152),
    native_programs_executed=0,
), indent=2))

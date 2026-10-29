"""Exact acceptance of the wider left-panel strip; no Fourier generation.

The input is the source-bound v10 direct one-pass geometry export. Its
analytic entry/contact/predecessor hypotheses are retained, not checked by
this arithmetic program. All decimals below are exact rational numbers.
"""
from fractions import Fraction as F
from pathlib import Path
import copy
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError("Assertions must remain enabled")
ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT / "runs/geometry-v10-20261028/final05/geometry-panels.py.stdout.json"
PIN = "2980009e801c9bc7bb1ab15edca2edd6782241e5151986ed269a961fefb8dcd4"
assert hashlib.sha256(INPUT.read_bytes()).hexdigest() == PIN
data = json.loads(INPUT.read_text())
assert data["status"] == "PASS_DIRECT_ONE_PASS_PANEL_CALCULATIONS"
rows = [r for r in data["panels"] if 25 <= r["index"] <= 39]


def coverage(table):
    assert [r["index"] for r in table] == list(range(25, 40))
    for r in table:
        i = r["index"]
        assert not r["excluded"]
        assert F(r["pl"]) == F(i, 100)
        assert F(r["pu"]) == F(i+1, 100)
        assert 0 <= F(r["d"]) <= F(17, 250)
        assert F(r["ell_l"]) > F(49, 25)
        assert F(r["rho"]) > 0
        assert F(r["beta_l"]) <= F(r["beta_u"])


coverage(rows)
mutations = []
for name, changed in [
    ("missing panel", rows[:-1]),
    ("duplicate panel", rows+[rows[-1]]),
    ("reordered panels", rows[1:]+rows[:1]),
]:
    try:
        coverage(changed)
    except AssertionError:
        mutations.append(name)
    else:
        raise AssertionError("Malformed cover accepted: "+name)
changed = copy.deepcopy(rows)
changed[0]["pu"] = "259/1000"
try:
    coverage(changed)
except AssertionError:
    mutations.append("corrupted closed endpoint")
else:
    raise AssertionError("Corrupted endpoint accepted")

S, c, error = F(81, 80), F(819, 2000), F(8, 875)
calls = 0


def margins(t, rho, beta):
    global calls
    calls += 1
    Q = -t*t*t + rho*(F(3, 2)*t*t+error) + 3*beta*t
    Qp = -3*t*t + 3*rho*t + 3*beta
    Qpp = -6*t + 3*rho
    H = S**3 * (
        F(2, 5)*((t*t*t-3*t)/6 + abs(t**4-6*t*t+3)/72)
        + t**5/4100 + 3*t/820 + F(17, 78720)*(3*t*t-2))
    L = F(2, 5)*(t*t/2+F(1, 2)+error)+c*Qp
    Lp = F(2, 5)*t+c*Qpp
    return {"t_squared_minus_three": t*t-3,
            "negative_boundary": -(H+c*Q),
            "negative_Q": -Q, "negative_Q_prime": -Qp,
            "negative_Q_second": -Qpp, "negative_L": -L,
            "negative_L_prime": -Lp, "negative_L_second": 6*c-F(2, 5)}


certificate = []
for r in rows:
    ell, rho = F(r["ell_l"]), F(r["rho"])
    negative_t = ell*(F(r["pl"])+F(3, 5))
    positive_t = ell*(1-F(r["pu"])+F(7, 10))
    negative = margins(negative_t, rho, -F(r["beta_l"]))
    positive = margins(positive_t, rho, F(r["beta_u"]))
    assert all(x > 0 for x in negative.values())
    assert all(x > 0 for x in positive.values())
    certificate.append({"index": r["index"], "pl": F(r["pl"]),
                        "pu": F(r["pu"]), "negative_t": negative_t,
                        "positive_t": positive_t,
                        "negative_ray_margins": negative,
                        "positive_ray_margins": positive})

assert min(x["positive_ray_margins"]["negative_boundary"]
           for x in certificate) > F(27, 100)
assert min(x["negative_ray_margins"]["negative_boundary"]
           for x in certificate) > F(3, 10)

# First obstruction for the smaller exploratory candidate: a failure of
# this sufficient bound, not a counterexample to the strip itself.
r = rows[4]
assert r["index"] == 29
bad = margins(F(r["ell_l"])*(1-F(r["pu"])+F(13, 20)),
              F(r["rho"]), F(r["beta_u"]))
assert F(10460, 10**6) < -bad["negative_boundary"] < F(10461, 10**6)
assert all(x > 0 for name, x in bad.items() if name != "negative_boundary")

# All constants needed for shifted-anchor feasibility, not a count bound.
A, d = F(7, 10), F(17, 250)
l = (A-1-2*d)/2
h = l+1
epsilon = (1-A-2*d)/2
zeta = 1-d
assert A+2*d == F(209, 250) < 1
assert l == -F(109, 500) and h == F(391, 500)
assert epsilon == F(41, 500) > 0
assert -zeta < l < h < zeta
assert F("1.83605680") < F(49, 25)
assert 42*F(1, 4)-1-h > 0
assert 42*F(3, 5)-1+l > 0

# Schulz's sharper gap is used only on [1/3,2/3]. On [1/3,.4],
# both (p*-p)^2 and 1/sqrt(p(1-p)) decrease, so the minimum is at .4.
sl, su = F("3.162277660"), F("3.162277661")
assert sl*sl < 10 < su*su
pstar_lower = (4-su)/2
assert pstar_lower > F(2, 5)
assert F(49, 100)**2 > F(6, 25)
gap_lower = 2*c*(pstar_lower-F(2, 5))**2/F(49, 100)
assert gap_lower > F(59, 100000)

# Actual-law negative control: favorable rho repair does not extend to
# all left panels. U_1=0; U_0 takes +/-epsilon equiprobably.
p, q, jump = F(13, 50), F(37, 50), F(1, 1000)
v = p*q
noise = q*jump*jump
V = v+noise
M3 = v*(1-2*v)+3*p*noise
rho_squared = M3*M3/V**3
rhoB_squared = (1-2*v)**2/v
assert 0 < rho_squared < rhoB_squared
theta, ell_squared = noise/V, 1/V
assert theta/ell_squared == noise
assert 42*noise < F(1, 500)
assert jump < d and jump < p
nodes = [(-p-jump, q/2), (-p+jump, q/2), (q, p)]
assert sum(m for x, m in nodes) == 1
assert sum(x*m for x, m in nodes) == 0
assert sum(x*x*m for x, m in nodes) == V
assert sum(abs(x)**3*m for x, m in nodes) == M3
assert calls == 31


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


print(json.dumps(encode({
    "status": "PASS_LEFT_PANELS_POINT_SEVEN_STRIP",
    "input_sha256": PIN, "python": sys.version,
    "ray_evaluations": calls, "closed_panel_indices": list(range(25, 40)),
    "certificate": certificate,
    "minimum_positive_ray_margins": {
        k: min(x["positive_ray_margins"][k] for x in certificate)
        for k in certificate[0]["positive_ray_margins"]},
    "minimum_negative_ray_margins": {
        k: min(x["negative_ray_margins"][k] for x in certificate)
        for k in certificate[0]["negative_ray_margins"]},
    "shifted_anchor": {"A": A, "d": d, "phase_lower": l,
                       "phase_upper": h, "epsilon": epsilon, "zeta": zeta},
    "gap_on_one_third_to_point_four": {"lower": gap_lower,
        "simple_strict_lower": F(59, 100000),
        "outside_scope": "No use of the sharper Schulz formula below 1/3"},
    "point_six_five_obstruction": {"index": 29, "margins": bad,
        "meaning": "Failure of sufficient boundary estimate only"},
    "adverse_rho_control": {"raw_centered_nodes_and_masses": nodes,
        "standardizing_variance": V, "rho_squared": rho_squared,
        "rhoB_squared": rhoB_squared, "lambda_at_n42": 42*noise,
        "meaning": "Refutes rho>=rhoB on the whole new domain, not the count theorem"},
    "rejected_cover_mutations": mutations,
    "mathematical_scope": "Conditional on the proved v10 geometry export and retained contact/heat/ray/sharp-predecessor hypotheses; no new count theorem or finite base"
}), indent=2))

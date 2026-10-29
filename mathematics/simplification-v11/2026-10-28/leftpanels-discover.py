"""Bounded exact exploration of five candidate left-panel amplitudes.

This records discovery, not acceptance of a mathematical reduction. The
negative ray is already excluded at amplitude 3/5 by the retained v10 theorem.
Only the positive ray needs exploration. Stop at the first common amplitude.
"""
from fractions import Fraction as F
from pathlib import Path
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
rows = [r for r in data["panels"] if 25 <= r["index"] <= 39]
assert [r["index"] for r in rows] == list(range(25, 40))


def ray(t, rho, beta):
    S, c, e = F(81, 80), F(819, 2000), F(8, 875)
    q = -t**3 + F(3, 2)*rho*t*t + 3*beta*t + e*rho
    q1 = -3*t*t + 3*rho*t + 3*beta
    q2 = -6*t + 3*rho
    h = F(2, 5)*S**3*((t**3-3*t)/6 + abs(t**4-6*t*t+3)/72)
    h += S**3*(t**5/4100 + 3*t/820 + 17*(3*t*t-2)/78720)
    gates = [t*t-3, -(h+c*q), -q, -q1, -q2,
             -(F(2, 5)*(t*t/2+F(1, 2)+e)+c*q1),
             -(F(2, 5)*t+c*q2), -(F(2, 5)-6*c)]
    return gates


results = []
calls = 0
selected = None
for amplitude in map(F, [".65", ".7", ".75", ".8", ".85"]):
    run = []
    for row in rows:
        t = F(row["ell_l"])*(1-F(row["pu"])+amplitude)
        gates = ray(t, F(row["rho"]), F(row["beta_u"]))
        calls += 1
        run.append({"index": row["index"], "gates": [str(g) for g in gates],
                    "passed": all(g > 0 for g in gates)})
    results.append({"amplitude": str(amplitude), "panels": run})
    if all(r["passed"] for r in run):
        selected = str(amplitude)
        break
assert calls <= 75
print(json.dumps({"status": "BOUNDED_EXACT_EXPLORATION", "input_sha256": PIN,
                  "calls": calls, "selected_first_common_amplitude": selected,
                  "results": results}, indent=2))

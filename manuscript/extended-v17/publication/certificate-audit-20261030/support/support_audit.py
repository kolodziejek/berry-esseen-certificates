"""Independent exact support gates; imports no retained numerical kernel."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

assert __debug__
repo = Path(sys.argv[1]).resolve()
proof = repo / 'mathematics/fixed-target-v7/2026-10-27/entry-proof.json'
assert hashlib.sha256(proof.read_bytes()).hexdigest() == '61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae'


def gates(R, r, b):
    S, c, e = F(81, 80), F(819, 2000), F(8, 875)
    A = (R**3 - 3*R)/6
    H4 = R**4 - 6*R**2 + 3
    E = R**5/4100 + 3*R/820 + F(17, 78720)*(3*R**2-2)
    Q = -R**3 + F(3, 2)*r*R**2 + 3*b*R + e*r
    Q1 = -3*R**2 + 3*r*R + 3*b
    Q2 = -6*R + 3*r
    L = F(2, 5)*(R**2/2 + F(1, 2) + e) + c*Q1
    L1, L2 = F(2, 5)*R+c*Q2, F(2, 5)-6*c
    P = F(2, 5)*S**3*(A**2+H4**2/(256*41)) + S**3*E*A+c*Q*A
    return {'A': A, 'H4': H4, '36A-H4': 36*A-H4,
            'Q': Q, 'Q1': Q1, 'Q2': Q2, 'L': L, 'L1': L1, 'L2': L2, 'P': P}


def good(g):
    return (all(g[k] > 0 for k in ['A', 'H4', '36A-H4'])
            and all(g[k] < 0 for k in ['Q', 'Q1', 'Q2', 'L', 'L1', 'L2', 'P']))


initial = gates(F(96, 25), F(1841, 1000), F(321, 500))
assert good(initial)
assert -initial['P'] == F(2214258283536204102723, 10250000000000000000000)
assert F(793881, 2073680) < F(48, 125)
assert F(48, 125)/42 == F(8, 875)
assert F(42, 41) < F(81, 80)**2

# Recover beta ceilings by rational bisection of the monotone exact relation,
# independently of signed_support's nested square-root formula.
data = json.loads(proof.read_text())
rows = []
for cell in data['steps'][0]:
    if 'radius' not in cell:
        continue
    i = cell['index']
    r = 1 + F(3361*(i+1), 96000)
    lo, hi = F(0), F(1)
    for _ in range(80):
        mid = (lo+hi)/2
        if (1+mid**2)**2 < r**2*(1-mid**2):
            lo = mid
        else:
            hi = mid
    assert (1+hi**2)**2 >= r**2*(1-hi**2)
    g = gates(F(cell['radius']), r, hi)
    assert good(g), i
    rows.append({'index': i, 'radius': cell['radius'], 'rho_upper': str(r),
                 'beta_upper': str(hi), 'gates': {k: str(v) for k,v in g.items()}})
assert len(rows) == 24
assert not good(gates(F(5, 2), F(1841, 1000), F(321, 500)))
assert not good({**initial, 'P': -initial['P']})
print(json.dumps({'status': 'PASS_INDEPENDENT_SUPPORT_GATES',
                  'python': sys.version, 'optimize': sys.flags.optimize,
                  'scope': 'Initial radius and 24 stored radii; continuous heat/ray argument is in Appendix D.',
                  'initial': {k:str(v) for k,v in initial.items()}, 'cells': rows,
                  'rejection_controls': ['unlicensed small initial radius', 'wrong boundary sign']}, indent=2))

#!/usr/bin/env python3
"""Fixed, bounded algebra diagnostics for an independent uniform42 review.

This is not a native predicate checker, a general proof acceptance interface,
or a proof of the retained analytic premises. No archived code is imported.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[4]
A = 'work/toward40_20261007/audit43/capsule/'
B = A + 'work/below49_20261006/'
PINS = {
    A + 'proofs/cutoff44.tex': '41af93935e4ebe64e38670bab222b1f8447b5dd7d95b3dc205ffc97236114f2b',
    A + 'proofs/joint_resource.tex': 'afda69759618eba2a0671e66bac0afc27046e9dd596e8bff5c9e24c29f3fcc44',
    A + 'proofs/local42_signed_gaussian_v2.tex': '894495dd297f25ea9e68741dfefdbf7ba0fcaa217047db301f3bbdea6cdc4143',
    A + 'proofs/signed_cubic_repair.tex': 'ad8360b6af1abe479b84a1070b4ac91a277c514051d78d7a71b5a3455e9e2696',
    B + 'acquisition/sperner_kernel.py': '21249fe117c6756a7a84af481dea2c5a490f9c66013c331cc998ab6828e1bb08',
    B + 'acquisition/high_window_core.py': '53e181be63852e21abc3f44191cce7237c46d9e9d7868d3b6b94fccb606c7232',
    B + 'package_audit/left42_exact/paired_extended.py': '9fbfdee44f42fe29caa3ee049d8b60d84670c8b4f5d53c147b6fbe280ccb5998',
    B + 'package_audit/left42_exact/accept_acquisition.py': 'a565247f6587f3bb07dd67ef2100d08f70aebbe7543937f1ab98f8d09cf31eb6',
    B + 'local/left42_final/central42_kernel.py': 'd025529aa2690c3cfc0f1c34a6af385d6fa69db8e069543057f29475cbb133c3',
    B + 'local/left42_tiny_final/normalization_piecewise42_v2.py': 'acc4055234a2629298cb665b12474ba5a9f35ed979dd3d238fffe9afd4aa5708',
}


def need(ok, message):
    if not ok:
        raise ValueError(message)


# Polynomials in one indeterminate, ascending exact coefficients.
def add(p, q):
    return [
        (p[i] if i < len(p) else F(0)) + (q[i] if i < len(q) else F(0))
        for i in range(max(len(p), len(q)))]


def scale(p, c):
    return [c * v for v in p]


def mul(p, q):
    result = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i + j] += x * y
    return result


def derivative(p):
    return [i * p[i] for i in range(1, len(p))]


def value(p, x):
    result = F(0)
    for c in reversed(p):
        result = result * x + c
    return result


# Sparse polynomials in the independent symbols (a,x,t).
def madd(p, q, sign=1):
    result = dict(p)
    for key, coefficient in q.items():
        result[key] = result.get(key, 0) + sign * coefficient
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def mmul(p, q):
    result = {}
    for kp, cp in p.items():
        for kq, cq in q.items():
            key = tuple(x + y for x, y in zip(kp, kq))
            result[key] = result.get(key, 0) + cp * cq
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def main():
    need(__debug__ and not sys.flags.optimize, 'unoptimized Python required')
    bindings = []
    archive = ROOT / 'verification/finite-tail/sources/backend.zip'
    with ZipFile(archive) as z:
        manifest = json.loads(z.read('finite61/MANIFEST.json'))['files']
        for logical, expected in PINS.items():
            record = manifest[logical]
            need(record['sha256'] == expected, 'manifest pin mismatch: ' + logical)
            data = z.read('finite61/blobs/' + expected)
            need(sha256(data).hexdigest() == expected, 'blob hash mismatch: ' + logical)
            bindings.append(dict(path=logical, sha256=expected, lines=len(data.splitlines())))

    # Sign numerator of d/dx [sqrt(x) exp(-x) (x+2)/(x^2+4x+2)].
    p, q = [F(2), F(1)], [F(2), F(4), F(1)]
    numerator = add(mul([F(1), F(-2)], mul(p, q)),
                    mul([F(0), F(2)], add(mul(derivative(p), q),
                                             scale(mul(p, derivative(q)), F(-1)))))
    need(numerator == list(map(F, [4, -10, -22, -13, -2])), 'high-window derivative identity')
    need(value(numerator, F(1, 4)) == F(-11, 128), 'high-window endpoint')
    need(all(c < 0 for c in derivative(numerator)), 'derivative numerator strictly decreases for positive x')
    # The elementary rational factor itself decreases for x >= 0.
    rational_derivative = add(mul(derivative(p), q), scale(mul(p, derivative(q)), F(-1)))
    need(rational_derivative == list(map(F, [-6, -4, -1])), 'rational-factor monotonicity')

    # Exact coefficient identity for the tangent numerator.
    # For arbitrary positive a and nonnegative t, expansion gives
    # (a*x+t^2)*(a+x)-x*(a+t)^2 = a*x^2-2*a*t*x+a*t^2.
    a, x, t = {(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1}
    tangent_left = madd(mmul(madd(mmul(a, x), mmul(t, t)), madd(a, x)),
                        mmul(x, mmul(madd(a, t), madd(a, t))), -1)
    tangent_right = mmul(a, mmul(madd(x, t, -1), madd(x, t, -1)))
    need(tangent_left == tangent_right == {(1, 0, 2): 1, (1, 2, 0): 1, (1, 1, 1): -2},
         'tangent identity')

    excess = F(42, 41) * (F(41, 200) + F(27, 400) + F(27, 2000))
    need(41 * 81**2 - 42 * 80**2 == 201, 'floor42 square endpoint')
    need(excess == F(3003, 10250) and excess < F(3, 10), 'floor42 excess')
    own = F(41, 100) + F(3, 10) / 42
    need(own == F(73, 175) and F('0.4226') - own == F(191, 35000), 'floor42 own score')

    # These are deliberate countermodels to dropped hypotheses, not iid
    # counterexamples to LOCAL42 or the Berry--Esseen conjecture.
    controls = []
    need(F(-1, 84) > F(-1, 42), 'negative inverse-index coefficient control')
    controls.append('dropping inverse-index positivity reverses the floor bound')
    need(F(2) * F(1) > F(1) * F(1), 'positive event bracket control')
    controls.append('positive event bracket cannot use a mass lower bound for an upper estimate')
    raw = 6 * F(29, 100) - 3 * F(29, 100)**2 - F(3, 2)
    need(raw == F(-123, 10000) and 2 * raw < raw, 'negative cubic multiplier control')
    controls.append('negative cubic bracket requires the upper score multiplier')
    atoms = {F(0): F(1, 2), F(1): F(1, 2)}
    interval_mass = sum(mass for point, mass in atoms.items() if 0 <= point <= 1)
    need(interval_mass == 1 and interval_mass > max(atoms.values()),
         'closed width-equals-step atom control')
    controls.append('Bernoulli interval [0,1] has mass1, exceeding max atom1/2 at width equal to step')
    # N=42,n=84,pq=1/4,theta=Theta=1/2,K=1,b=d=0,D=d_D=1/2.
    # These satisfy the weakened unweighted premises, but not nD<=N*d_D.
    lam = 84 * F(1, 4) * F(1, 2) / (1 - F(1, 2))
    false_ceiling = 42 * F(1, 4) * F(1, 2) / (1 - F(1, 2))
    need(lam == 21 and false_ceiling == F(21, 2) and lam > false_ceiling,
         'unweighted resource control')
    controls.append('unweighted defect alone does not yield the claimed uniform noise ceiling')
    print(json.dumps(dict(
        status='PASS_BOUNDED_INDEPENDENT_UNIFORM42_DIAGNOSTICS',
        mathematical_status='Exact identities and countermodels to omitted hypotheses; conditional analytic review is separate.',
        execution_status='Fresh stdlib-only diagnostic; no archived code imported or executed.',
        source_bindings=bindings,
        high_window_derivative_coefficients=list(map(str, numerator)),
        high_window_endpoint=str(value(numerator, F(1, 4))),
        tangent_identity={str(key): coefficient for key, coefficient in tangent_left.items()},
        scalar42=dict(excess=str(excess), own_score=str(own), own_reserve=str(F('0.4226') - own)),
        negative_controls=controls,
        limitations=['No native gate replay', 'No analytic premise acceptance',
                     'No generic parameter acceptance API', 'No full BASE41 proof']), indent=2))


if __name__ == '__main__':
    main()

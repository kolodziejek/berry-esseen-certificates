#!/usr/bin/env python3
"""Exact algebra/input bindings for a NEW zero-loss support lifting lemma.

Does not run, accept, alter, or weaken an inherited numerical certificate.
Old finite-band polynomial positivity and resource acquisition remain inputs.
Run from the repository root with unoptimized Python 3.9+.
"""
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import sys
from zipfile import ZipFile

ARCHIVE = Path('verification/finite-tail/sources/backend.zip')
ARCHIVE_SHA = '43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52'
LEFT_SHA = '419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393'
FIFTH_SHA = '09a6e27ef42847cef0ac258504546eaef3a3035e83171143f1c2fd848736ac6c'
HEAT_SHA = '650d7f3617775102fe92977605dfda5fb68a11e0ad738eb799aab77bc4a79e18'
N, LAST = 42, 48
C, EC, QOLD = F(819, 2000), F(48, 125), F(19, 100)
S_UPPER = F(81, 80)


class Rejected(ValueError):
    pass


def need(condition, message):
    if not condition:
        raise Rejected(message)


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def roots(x):
    need(x >= 0, 'nonnegative square root')
    scale = 10**12
    k = isqrt(x.numerator * scale * scale // x.denominator)
    lo, hi = F(k, scale), F(k + 1, scale)
    need(lo * lo <= x < hi * hi, 'outward square-root enclosure')
    return lo, hi


def trim(a):
    a = list(map(F, a))
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(*polys):
    out = [F(0)] * max(map(len, polys))
    for p in polys:
        for k, value in enumerate(p):
            out[k] += value
    return trim(out)


def times(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def scale(p, c):
    return trim([c * x for x in p])


ELL, _ = roots(F(N - 1))
_, S = roots(F(N, N - 1))
A = [0, F(-1, 2), 0, F(1, 6)]
J = [0, -15, 0, 0, 0, 1]
H4 = [3, 0, -6, 0, 1]
DU = scale(J, F(1, 120 * (N - 1)))
DL = scale(J, F(1, 120 * (LAST - 1)))
W = add(A, scale(DU, F(-15, 2)))
E = add(scale([0, 0, 0, 0, 0, 0, 1], F(51, 14400 * (N - 1)) / ELL),
        scale([-2, 0, 3], F(51, 960 * (N - 1)) / ELL),
        [0, F(1, 8 * (N - 1)**2)])
B2 = scale(times(H4, H4), F(1, 256 * (N - 1)))


def contact_polynomial(r, b, lower_D, loss):
    q = [r * EC / N, 3 * b, F(3, 2) * r, -1]
    numerator = add(times(add(A, scale(lower_D, -3)), W), B2)
    return add(scale(numerator, F(2, 5) * S**3),
               scale(times(E, W), S**3), times(scale(q, C), W),
               scale(W, r * S * loss))


def domination_polynomial(lower_D):
    inner = add(scale(A, F(1, 2)), scale(lower_D, -3), scale(DU, -3),
                scale(H4, F(-1, 12) / ELL))
    return add(times(inner, W), B2)


def check_identity(r, b):
    actual = add(contact_polynomial(r, b, [F(0)], F(0)),
                 scale(contact_polynomial(r, b, DL, QOLD), -1))
    expected = scale(times(W, add(scale(J, S**2 / 4700), [-QOLD * r])), S)
    need(actual == expected, 'contact difference identity')
    difference = add(domination_polynomial([F(0)]),
                     scale(domination_polynomial(DL), -1))
    need(difference == scale(times(DL, W), 3), 'outer domination improves')


def bridge_gates(cut, rlo, rhi, bhi, new_loss=F(0)):
    need(new_loss == 0, 'this theorem assumes zero predecessor loss')
    need(F(5, 2) <= cut < F(9, 2), 'splice inside old certified radial range')
    need(1 <= rlo <= rhi and 0 <= bhi < 1, 'moment parameter bounds')
    need(S < S_UPPER, 'inherited rational scale is below the comparison bound')
    j = cut**5 - 15 * cut
    margin = QOLD * rlo - S_UPPER**2 * j / 4700
    need(margin > 0, 'finite-to-infinite contact domination')
    # J and its derivative are positive/increasing for u >= 5/2.
    need(F(5, 2)**4 > 15 and 5 * F(5, 2)**4 > 15, 'radial J monotonicity')
    e = EC / N
    q = -cut**3 + F(3, 2) * rhi * cut**2 + 3 * bhi * cut + rhi * e
    qp = -3 * cut**2 + 3 * rhi * cut + 3 * bhi
    qpp = -6 * cut + 3 * rhi
    ell = F(2, 5) * (cut**2 / 2 + F(1, 2) + e) + C * qp
    ellp = F(2, 5) * cut + C * qpp
    gates = dict(Q=q, Q_prime=qp, Q_second=qpp, L=ell,
                 L_prime=ellp, L_second=F(2, 5) - 6 * C)
    need(all(value < 0 for value in gates.values()), 'whole-ray derivative gates')
    return dict(splice=str(cut), domination_margin=str(margin),
                ray_gates={k: str(v) for k, v in gates.items()})


def bind_left_rows(proof):
    need(proof['N'] == N and proof['L'] == LAST and F(proof['cap']) == F(2113, 5000),
         'unchanged finite acquisition scope')
    need(len(proof['coarse']) == 15 and len(proof['fine']) == 55, 'complete acquisition rows')
    active = [r for r in proof['coarse'] if not r.get('excluded')]
    first = proof['first_bridge']
    need(F(first['rho_upper']) == max(F(r['rho']) for r in active), 'first bridge rho source')
    need(F(first['beta_absolute_upper']) == max(F(r['beta']) for r in active), 'first bridge beta source')
    need(F(first['radius']) == F(121, 40), 'first bridge radius')
    rows = [first]
    for index, cell in enumerate(proof['fine']):
        need(list(map(F, cell['p'])) == [F(135 + index, 500), F(136 + index, 500)],
             'ordered complete fine probability cover')
        need(bool(cell['trace']) and cell['trace'][0]['contraction'] is None,
             'first fine step uses the common preceding bridge')
        for previous, step in zip(cell['trace'], cell['trace'][1:]):
            bridge = step['contraction']
            need(bridge is not None, 'every later support bridge is present')
            need(F(bridge['rho_upper']) == F(previous['resource']['rho']), 'same preceding rho')
            need(F(bridge['beta_absolute_upper']) == F(previous['resource']['beta']), 'same preceding beta')
            need(F(bridge['radius']) == F(step['radius']), 'same contracted radius')
            rows.append(bridge)
    need(len(rows) == 64, 'all 64 left support invocations')
    for r in rows:
        need(r['n_band'] == [N, LAST] and F(r['barrier']) == 0 and
             F(r['slow']) == QOLD and F(r['current_score_lower']) == C,
             'unchanged zero-barrier finite support input')
        need(1 <= F(r['rho_upper']) <= F(3, 2) and
             0 <= F(r['beta_absolute_upper']) <= F(1, 2), 'uniform left moment ceilings')
        need(F(5, 2) <= F(r['radius']) <= F(121, 40) < F(39, 10), 'left radius before splice')
    return rows


def read_member(archive, digest):
    data = archive.read('finite61/blobs/' + digest)
    need(sha256(data).hexdigest() == digest, 'exact member identity')
    return data


def main():
    need(not sys.flags.optimize, 'unoptimized Python required')
    need(len(sys.argv) == 1, 'fixed proof bridge; no target overrides')
    need(sha256(ARCHIVE.read_bytes()).hexdigest() == ARCHIVE_SHA, 'baseline archive identity')
    with ZipFile(ARCHIVE) as archive:
        for digest in (FIFTH_SHA, HEAT_SHA):
            read_member(archive, digest)
        proof = json.loads(read_member(archive, LEFT_SHA), object_pairs_hook=unique)
    rows = bind_left_rows(proof)
    r = min(F(3031, 10000) * F(646, 1000) / (C - F(3031, 10000)),
            F(3322, 10000) * F(429, 1000) / (C - F(3322, 10000)))
    _, disc = roots((2 + r*r)**2 - 4 * (1 - r*r))
    _, b = roots((disc - 2 - r*r) / 2)
    need(F(46, 25) <= r <= F(37, 20) and 0 <= b <= F(2, 3), 'initial moment parameter bounds')
    initial = bridge_gates(F(21, 5), F(46, 25), F(37, 20), F(2, 3))
    left = bridge_gates(F(39, 10), F(1), F(3, 2), F(1, 2))
    check_identity(r, b)
    for row in rows:
        check_identity(F(row['rho_upper']), F(row['beta_absolute_upper']))
    # e_n < EC/n for all n >= 42: after clearing x^2, positive constant
    # minus nonnegative multiples of x, x^2, x^3; check its minimum at 1/42.
    x = F(1, N)
    scale_margin = ((2*EC - F(3, 4)) - (EC + F(1, 4))*x
                    + (EC*EC - EC)*x*x - EC*EC*x*x*x)
    need(scale_margin > 0, 'uniform scale correction')
    rejected = {}
    def reject(label, fn):
        try:
            fn()
        except (Rejected, KeyError, TypeError):
            rejected[label] = True
        else:
            raise Rejected('negative control accepted: ' + label)
    reject('nonzero_predecessor_loss', lambda: bridge_gates(F(39, 10), F(1), F(3, 2), F(1, 2), F(1, 100)))
    reject('blind_left_splice_45', lambda: bridge_gates(F(449, 100), F(1), F(3, 2), F(1, 2)))
    reject('false_ray_moment_cap', lambda: bridge_gates(F(39, 10), F(1), F(4), F(1, 2)))
    reject('missing_first_bridge', lambda: bind_left_rows({k:v for k,v in proof.items() if k != 'first_bridge'}))
    p = deepcopy(proof); p['fine'].pop()
    reject('missing_probability_cell', lambda: bind_left_rows(p))
    p = deepcopy(proof); p['fine'][12] = deepcopy(p['fine'][11])
    reject('duplicated_probability_cell', lambda: bind_left_rows(p))
    p = deepcopy(proof); p['fine'].reverse()
    reject('reordered_probability_cells', lambda: bind_left_rows(p))
    p = deepcopy(proof); p['fine'][10]['trace'][1]['contraction']['rho_upper'] = '1'
    reject('changed_preceding_moment', lambda: bind_left_rows(p))
    p = deepcopy(proof); p['fine'][10]['trace'][1]['contraction'] = None
    reject('missing_refinement_bridge', lambda: bind_left_rows(p))
    reject('duplicate_json_key', lambda: json.loads('{"N":42,"N":43}', object_pairs_hook=unique))
    print(json.dumps(dict(status='PASS_SUPPORT_LIFT_ALGEBRA_AND_BINDINGS',
        mathematical_scope='New conditional zero-loss support lift, all n>=42; inherited finite polynomial positivity, same-law resources and analytic contact/heat inputs are NOT accepted by this script.',
        native_certificate_programs_executed=0, historical_support_invocations_bound=65,
        initial_r=str(r), initial_b=str(b), inherited_S=str(S),
        initial=initial, left=left, scale_margin=str(scale_margin),
        polynomial_identities_checked=130, negative_controls=rejected), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()

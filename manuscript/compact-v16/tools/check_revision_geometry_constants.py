"""Exact finite checks for the revised geometry and two contact rays.

Only rational scalar comparisons and diagnostic finite-law identities are
checked here. Whole-domain coverage follows from the monotonicity and moment
arguments in sections/05-geometry-counts.tex and 07-direct-acquisition.tex.
No historical checker or numerical result is imported.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions are mathematical obligations; optimization is forbidden.')

checks = {}

def positive(name, value):
    value = F(value)
    if name in checks or value <= 0:
        raise AssertionError((name, str(value)))
    checks[name] = str(value)

SL, SU = F('3.162277660'), F('3.162277661')
positive('sqrt10_lower', 10-SL*SL)
positive('sqrt10_upper', SU*SU-10)
left, right = F(3, 8), F(93, 200)
positive('pstar_above_left', (4-SU)/2-left)
positive('midpoint_above_pstar', (left+right)/2-(4-SL)/2)
assert (left+right)/2 == F(21, 50)

def Q(p, sigma):
    q = 1-p
    return (sigma+1)*p*p+(sigma-1)*q*q-6*p*q

qleft = Q(left, SL)
assert qleft == F(37936011, 1600000000)
positive('single_probability_endpoint_surplus', qleft-F(47, 2000))
assert qleft-F(47, 2000) == F(336011, 1600000000)

c0, r, eta = F(819, 2000), F(9, 8), F(8, 875)
ray_values = []
for name, t, b, bounds in [
    ('negative', F('1.996')*(left+F(3, 5)), -F('.066148'),
     (F(-2, 5), F(-1), F(-13, 5))),
    ('positive', F('1.996')*(1-right+F(3, 5)), F('.2527'),
     (F(-13, 100), F(-8, 5), F(-16, 5))),
]:
    qb = -t**3+F(3, 2)*r*t*t+3*b*t+eta*r
    qprime = -3*t*t+3*r*t+3*b
    qsecond = -6*t+3*r
    h = F(81, 80)**3*(F(2, 5)*((t**3-3*t)/6+abs(t**4-6*t*t+3)/72)
                           +t**5/4100+3*t/820+17*(3*t*t-2)/78720)
    g = F(2, 5)*(t*t/2+F(1, 2)+eta)
    L = g+c0*qprime
    Lprime = F(2, 5)*t+c0*qsecond
    values = (h+c0*qb, L, Lprime)
    positive(name+'_radius_squared_gt_3', t*t-3)
    for quantity, bound, value in zip(('boundary', 'L', 'Lprime'), bounds, values):
        positive(name+'_'+quantity+'_surplus', bound-value)
    ray_values.append({'ray': name, 'boundary': str(t),
                       'h_plus_c0_Q': str(values[0]), 'L': str(L),
                       'Lprime': str(Lprime)})
Lsecond = F(2, 5)-6*c0
assert Lsecond == F(-2057, 1000)
positive('negative_constant_second_derivative', -Lsecond)

# Actual finite marginals: compute the support-gap sum directly from atoms.
# Center first; divide every cubic quantity by variance^(3/2) to recover
# the standardized statement. Thus the comparison itself is rational.
def law_budget(name, input_atoms, gap_error=F(0)):
    merged = {}
    for x, mass in input_atoms:
        x, mass = F(x), F(mass)
        if mass < 0:
            raise AssertionError('negative probability')
        merged[x] = merged.get(x, F(0))+mass
    if sum(merged.values(), F(0)) != 1:
        raise AssertionError('probabilities must sum to one')
    mean = sum(x*mass for x, mass in merged.items())
    atoms = sorted((x-mean, mass) for x, mass in merged.items() if mass)
    if any(x == 0 for x, mass in atoms):
        raise AssertionError('central gap required')
    p = sum(mass for x, mass in atoms if x > 0)
    q = 1-p
    if not 0 < p < 1:
        raise AssertionError('both signs required')
    m = sum(x*mass for x, mass in atoms if x > 0)
    ell = m/(p*q)
    w = p*q*ell*ell
    A = -max(x for x, mass in atoms if x < 0)
    B = min(x for x, mass in atoms if x > 0)
    a0, a1 = p-A/ell, q-B/ell
    d = a0+a1
    assert a0 >= 0 and a1 >= 0 and d < 1
    rho = sum(abs(x)**3*mass for x, mass in atoms)
    gamma = sum(x**3*mass for x, mass in atoms)
    variance = sum(x*x*mass for x, mass in atoms)
    J = sum((b-a)**2*sum(x*mass for x, mass in atoms if x >= b)
            for (a, _), (b, _) in zip(atoms, atoms[1:]))+gap_error
    # Separate coefficients of 1 and sqrt(10) in both sides of (G).
    rhs_constant = ell*w*(p*p-q*q-6*p*q)+6*ell*w*(d*(1-d)+a0*a1)
    rhs_sqrt10 = ell*w*(p*p+q*q)
    for x, mass in atoms:
        conditional_mean = ell*q if x > 0 else -ell*p
        W = x-conditional_mean
        magnitude, mean_magnitude, endpoint = (x, ell*q, B) if x > 0 else (-x, ell*p, A)
        kernel_common = magnitude+2*mean_magnitude
        rhs_sqrt10 += mass*W*W*kernel_common
        rhs_constant += mass*W*W*((-1 if x > 0 else 1)*kernel_common+6*endpoint)
    assert rhs_sqrt10 == rho
    slack = 3*rho-gamma-3*J-rhs_constant
    if slack < 0:
        raise AssertionError(('joint budget', name, str(slack)))
    return {'name': name, 'atoms_after_merging': len(atoms),
            'variance': str(variance), 'homogeneous_cubic_slack': str(slack)}

examples = []
for label, p in [('symmetric', F(1, 2)), ('skew', F(1, 5)),
                 ('near_extremal', F(41886117, 100000000)),
                 ('left_probability_boundary', left), ('right_probability_boundary', right)]:
    examples.append(law_budget(label, [(-p, 1-p), (1-p, p)]))
examples.extend([
    law_budget('three_point', [(-2, F(1, 4)), (1, F(1, 2)), (3, F(1, 4))]),
    law_budget('four_point', [(-3, F(1, 4)), (-1, F(1, 4)), (1, F(1, 4)), (3, F(1, 4))]),
    law_budget('several_outer_gaps', [(x, F(1, 6)) for x in (-3, -2, -1, 1, 2, 3)]),
    law_budget('tiny_remote_atom', [(-1, F(1, 2)), (1, F(1, 2)-F(1, 10**10)),
                                  (100, F(1, 10**10))]),
    law_budget('exact_collision', [(-1, F(1, 2)), (1, F(1, 5)), (1, F(3, 10))]),
    law_budget('nearby_four_point', [(-1, F(1, 4)), (-1+F(1, 10**9), F(1, 4)),
                                     (1, F(1, 4)), (1+F(1, 10**9), F(1, 4))]),
])

# These are rejection tests of the predicates, not extra theorem evidence.
negative_controls = []
def must_reject(name, operation):
    try:
        operation()
    except AssertionError:
        negative_controls.append(name)
    else:
        raise AssertionError('negative control was accepted: '+name)

must_reject('wrong_probability_target', lambda: positive('bad_probability', qleft-F(3, 100)))
must_reject('reversed_ray_curvature', lambda: positive('bad_curvature', Lsecond))
must_reject('inflated_gap_sum', lambda: law_budget('bad_gap', [(-1, F(1, 2)), (1, F(1, 2))], F(1, 1000)))
must_reject('missing_probability_mass', lambda: law_budget('bad_mass', [(-1, F(1, 3)), (1, F(1, 2))]))
must_reject('zero_atom_outside_central_gap_domain', lambda: law_budget('zero_atom', [(-1, F(1, 4)), (0, F(1, 2)), (1, F(1, 4))]))

here = Path(__file__).resolve().parents[1]
paths = [here/'sections/05-geometry-counts.tex', here/'sections/07-direct-acquisition.tex', Path(__file__).resolve()]
print(json.dumps({'status': 'PASS_REVISION_GEOMETRY_CONSTANTS',
                  'mathematical_scope': 'Finite rational comparisons for revised probability and ray arguments; diagnostic finite-law evaluations of the joint budget. The manuscript supplies the analytic proof.',
                  'rational_checks': checks, 'rays': ray_values,
                  'finite_law_diagnostics': examples, 'negative_controls': negative_controls,
                  'source_sha256': {str(p.relative_to(here)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}, indent=2))

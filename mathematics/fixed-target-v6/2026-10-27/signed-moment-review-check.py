#!/usr/bin/env python3
"""Independent rational audit of recorded inverse bounds; no kernel imports."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import argparse
import json
import sys


def need(x, text):
    if not x:
        raise ValueError(text)


def lower_inverse_certificate(a, y):
    need(-1 <= y <= 1, "normalized moment domain")
    if a <= -1:
        need(y == -1, "inactive branch retains whole interval")
        return
    # Certify f(y)<=a on f's increasing branch without evaluating a root.
    need(a*a < 10 and (y <= 0 or 10*y*y <= 1), "increasing inverse branch")
    need(a-y >= 0, "sign before squaring")
    need((a-y)**2 >= 9*(1-y*y), "lower inverse certificate")


def main():
    need(__debug__ and not sys.flags.optimize, "unoptimized Python")
    p = argparse.ArgumentParser()
    p.add_argument("--source-root", type=Path, default=Path(__file__).resolve().parents[3])
    src = p.parse_args().source_root
    names = ["mathematics/fixed-target-v6/2026-10-27/moment.tex",
             "mathematics/fixed-target-v6/2026-10-27/moment_check.py",
             "runs/fixed-target-v6-20261027/moment01/moment.stdout.json"]
    blobs = {name: (src/name).read_bytes() for name in names}
    need(sha256(blobs[names[1]]).hexdigest() == "c44f789c35198eabb2d6d07a3843437c4fa29e9b85ebf79505a3bb696987513f", "reviewed constructor bytes")
    need(sha256(blobs[names[2]]).hexdigest() == "301a768e1622f0b79161ef2c56225f5035e4d72d683e911f3b152e95ac694a93", "reviewed output bytes")
    obj = json.loads(blobs[names[2]])
    need(obj['cells'] == 24 and obj['updates'] == 6 and len(obj['rows']) == 24, "complete recorded cover")
    sigma = F(3162277660, 10**9)
    need(0 < sigma and sigma*sigma < 10, "strict square-root lower constant")
    count = negative = positive = 0
    previous_upper = F(1)
    for index, row in enumerate(obj['rows']):
        l, u = F(row['rho_lower']), F(row['rho_upper'])
        need(row['index'] == index and l == previous_upper and l < u, "ordered shared endpoints")
        need(l == 1+F(3361*index,96000) and u == 1+F(3361*(index+1),96000), "literal rho cover")
        previous_upper = u
        need(len(row['steps']) == 6, "all six updates retained")
        for j, step in enumerate(row['steps'], 1):
            need(step['step'] == j, "ordered update index")
            a, y, d = (F(step[k]) for k in ('normalized_a_lower','normalized_gamma_lower','prior_defect'))
            need(d >= 0 and a == sigma-d/l, "prior-defect normalization")
            lower_inverse_certificate(a, y)
            gamma = F(step['circle_gamma_lower'])
            need(gamma <= min(l*y, u*y), "correct rho endpoint and lower rounding")
            need(F(step['gamma_lower']) >= gamma, "new bound retained in intersection")
            count += 1
            negative += y < 0
            positive += y >= 0
    need(previous_upper == F(7361,4000), "last rho endpoint")
    rejected = []
    for name, a, y in [('wrong root branch', F(0), F(9,10)),
                        ('upward lower-bound rounding', F(31,13), -F(5,13)+F(1,10**9))]:
        try:
            lower_inverse_certificate(a, y)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError('invalid inverse accepted: '+name)
    print(json.dumps(dict(status='PASS_INDEPENDENT_INVERSE_CERTIFICATES',
        recorded_updates_checked=count, negative_normalized_bounds=negative,
        nonnegative_normalized_bounds=positive, rejected_controls=rejected,
        scope='Rational audit of all recorded inverse lower bounds and coverage; no Fourier or acquisition replay',
        input_sha256={name:sha256(data).hexdigest() for name,data in blobs.items()}), indent=2))


if __name__ == '__main__':
    main()

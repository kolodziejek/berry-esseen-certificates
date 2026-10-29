#!/usr/bin/env python3
"""Two simple quadratic passes, with one gap-free circle update.

Fresh first-cover Fourier primitives remain explicit analytic inputs. No
degree-six phase routine, dense acquisition stage or native acceptor is used.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import argparse
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
N, PHILO, SIGMALO = 42, F(997,2500), F(3162277660,10**9)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def load(name, path, expected=None):
    blob = path.read_bytes()
    if expected:
        need(sha256(blob).hexdigest() == expected, "reviewed module bytes")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, sha256(blob).hexdigest()


def ceiling(x):
    scale = 10**10
    return F(-((-x.numerator*scale)//x.denominator), scale)


def cover(rows):
    need(len(rows) == 24, "complete 24-cell cover")
    for i, row in enumerate(rows):
        need(row['index'] == i and row['rho_lower'] == 1+F(3361*i,96000)
             and row['rho_upper'] == 1+F(3361*(i+1),96000), "closed ordered endpoints")


def constant(row, difference):
    l,u,b,G = (row[k] for k in ('rho_lower','rho_upper','beta_abs','Gamma'))
    need(0 <= difference <= 2*u and G >= 0, "signed gap charge domain")
    first = 3*b*(2*u+1)/2+3*G*difference/2+3*u*u*(u+1)/8+u**3/4-l/2
    second = 3*b*(2*u+1)/2+2*u*row['M4']-l/2
    A = min(first, second)
    need(A > 0, "constant coefficient gate")
    return A


def one_pass(row, c0, c1, signed, circle, previous=None):
    l,u,g = (row[k] for k in ('rho_lower','rho_upper','gamma_abs'))
    K = min(row['K_abs'], signed.signed_cap(l,u,row['beta_abs'])['new_K_abs'])
    gamma, density, difference = -g, F(0), 2*u
    A = constant(row, difference)
    if previous is not None:
        oldT, oldD = previous['raw'], previous['defect']
        need(0 <= oldT < N*c0*l and oldD >= 0, "previous raw and defect license")
        density = PHILO*(1-oldT/(N*c0*l))
        need(0 < density < F(2,5), "density interval")
        circle_gamma, _, _ = circle.circle_lower(l,u,oldD)
        gamma = max(-g,SIGMALO*l-3-oldD,circle_gamma)
        need(gamma <= g, "inconsistent cell is not discarded")
        difference = min(2*u,(1-SIGMALO)*l+3+oldD,u-gamma)
        A = min(A,constant(row,difference))
    endpoints = []
    for c in (c0,c1):
        q = c*l-g/5
        if previous is not None:
            q = max(q,c*l+min(density*gamma,F(2,5)*gamma)/2)
        f = c*K+row['normal_H_coefficient']+row['slope']
        B = row['KF']+c*A
        need(q > 0 and f >= 0, "quadratic completion gates")
        endpoints.append(dict(c=c,constant=B,linear=f,quadratic=q))
    raw_exact = max(z['constant']+z['linear']**2/(4*z['quadratic']) for z in endpoints)
    raw = min(ceiling(raw_exact),ceiling(row['fixed_raw']))
    if previous is not None:
        raw = min(raw,previous['raw'])
    need(0 <= raw < N*c0*l, "new raw Gaussian license")
    eta = (c0*l-raw/N)/2
    need(eta > 0, "positive simple phase price")
    resource_exact = max(z['constant']+z['linear']**2/(4*(z['quadratic']+eta)) for z in endpoints)
    resource = min(raw,ceiling(resource_exact))
    if previous is not None:
        resource = min(resource,previous['resource'])
    defect = ceiling(6*resource/(N*PHILO))
    if previous is not None:
        defect = min(defect,previous['defect'])
        need(raw <= previous['raw'] and resource <= previous['resource']
             and defect <= previous['defect'], "ordered contraction")
    return dict(raw=raw,resource=resource,defect=defect,
                weighted_nD=ceiling(6*resource/PHILO), K_abs=K,A=A,
                gamma_lower=gamma,density_lower=density,rho_minus_gamma_upper=difference,
                endpoints=endpoints,raw_exact=raw_exact,phase_extra=eta,
                resource_exact=resource_exact,
                actual_gap_margin=(SIGMALO-1)*l-defect)


def run(moment_path):
    need(__debug__ and not sys.flags.optimize, "unoptimized interpreter")
    moment, mh = load('two_pass_circle',moment_path,
        'c44f789c35198eabb2d6d07a3843437c4fa29e9b85ebf79505a3bb696987513f')
    signed, sh = load('two_pass_signed',HERE/'signed-check.py',
        'c827917d18b241d7e6255b3c15184ca719044cc3b7ffb8c7474ea5482dd7a847')
    base = moment.base
    obj = json.loads((base.HERE/'cell-input.json').read_text(),object_pairs_hook=base.unique)
    inputs = {name:(base.HERE/'cell-sources'/name).read_bytes() for name in base.PINS}
    first = base.run(obj,inputs)
    cover(first['rows'])
    need(SIGMALO > 1 and SIGMALO*SIGMALO < 10, "strict sigma lower constant")
    c0,c1 = F(obj['c_lower']),F(obj['c_upper'])
    rows = []
    for row in first['rows']:
        initial = one_pass(row,c0,c1,signed,moment)
        second = one_pass(row,c0,c1,signed,moment,initial)
        rows.append(dict(index=row['index'],rho_lower=row['rho_lower'],rho_upper=row['rho_upper'],passes=[initial,second]))
    summaries = []
    for j in range(2):
        states = [r['passes'][j] for r in rows]
        summaries.append(dict(pass_number=j+1,max_raw=max(r['raw'] for r in states),
          max_resource=max(r['resource'] for r in states),max_defect=max(r['defect'] for r in states),
          max_weighted_nD=max(r['weighted_nD'] for r in states),
          cells_D_below4=sum(r['defect']<4 for r in states),
          cells_D_below2=sum(r['defect']<2 for r in states),
          cells_actual_gap=sum(r['actual_gap_margin']>0 for r in states),
          min_actual_gap_margin=min(r['actual_gap_margin'] for r in states)))
    need(summaries[1]['max_defect'] < 4, "second pass uniformly below four")
    need(summaries[1]['cells_actual_gap'] == 24, "second pass licenses every actual central gap")
    from copy import deepcopy
    rejected = []
    def reject(name, action):
        try:
            action()
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError('negative control accepted: '+name)
    for name, mutate in [
        ('missing cell',lambda x:x.pop()),
        ('duplicated cell',lambda x:x.__setitem__(1,x[0])),
        ('reordered cells',lambda x:x.reverse()),
        ('broken shared endpoint',lambda x:x[1].__setitem__('rho_lower',x[1]['rho_lower']+F(1,1000)))]:
        changed = deepcopy(first['rows'])
        mutate(changed)
        reject(name,lambda:cover(changed))
    invalid = deepcopy(rows[-1]['passes'][0])
    invalid['raw'] = N*c0*first['rows'][-1]['rho_lower']
    reject('unlicensed prior raw',lambda:one_pass(first['rows'][-1],c0,c1,signed,moment,invalid))
    reject('first pass incorrectly claims all actual gaps',lambda:need(summaries[0]['cells_actual_gap']==24,'actual gap coverage'))
    reject('understated final defect target',lambda:need(summaries[1]['max_defect']<F(7,2),'defect target'))
    return dict(name='FIXED_TARGET_TWO_SIMPLE_PASSES_V1',status='PASS_CONDITIONAL_TWO_QUADRATIC_PASSES',
      scope='Conditional on initial support/contact and retained full Fourier bounds. No full initial/local acceptance.',
      cells=24,passes=2,rows=rows,summaries=summaries,rejected_controls=rejected,
      source_sha256={'signed-check.py':sh,'moment_check.py':mh,
        'cell_check.py':sha256((base.HERE/'cell_check.py').read_bytes()).hexdigest(),
        'signed-two-pass-check.py':sha256(Path(__file__).read_bytes()).hexdigest(),
        **{name:sha256(blob).hexdigest() for name,blob in inputs.items()}})


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--moment-source',type=Path,default=HERE/'moment_check.py')
    obj = run(p.parse_args().moment_source)
    def enc(x):
        if isinstance(x,F): return str(x)
        if isinstance(x,dict): return {k:enc(v) for k,v in x.items()}
        if isinstance(x,list): return [enc(v) for v in x]
        return x
    print(json.dumps(enc(obj),indent=2))

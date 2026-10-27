#!/usr/bin/env python3
"""Exact bounded checks for disjoint crossing costs and fourth-moment pricing.

The continuum/integer conclusions are proved in count-cost.tex. This program
does not execute a native LOW kernel or accept the acquired row hypotheses.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import zipfile

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions must be enabled')


def need(ok, message):
    if not ok:
        raise ValueError(message)


def separated_value(b, c, u):
    return max(max(F(0), b+u-1)/(c-u)**2,
               max(F(0), b+u)/(c+min(u, c/3))**2)


def separated_supremum(b, c, lo, hi):
    need(all(type(x) is F for x in (b, c, lo, hi)), 'rational input required')
    need(F(1, 2) < c <= 1, 'c domain')
    need(-F(1, 2) <= lo <= hi <= F(1, 2), 'phase domain')
    candidates = [(lo, separated_value(b, c, lo)), (hi, separated_value(b, c, hi))]
    u = c-2*b
    if c > b and lo <= u <= hi and u <= c/3:
        need(b+u < 1, 'stationary point belongs to negative-crossing branch only')
        candidates.append((u, 1/(4*(c-b))))
    return max(value for _, value in candidates), candidates


def coupled_checks():
    counts = {'tuples': 0, 'law_phase_cases': 0, 'nonzero_curvature_tuples': 0}
    # U0 is mostly small positive noise; U1 is its reflection. Both are centered.
    for n, large, small in [(2, F(3,4), F(1,10)), (4, F(3,4), F(1,10)),
                            (3, F(3), F(1,20)), (4, F(1,4), F(1,20))]:
        p, q = F(2,5), F(3,5)
        k = round(n*p)
        c = 1-2*small
        var = large*small
        t = n*var
        upper_fourth = t*(large**2+3*t)
        mass = [F(comb(n,j))*p**j*q**(n-j) for j in range(n+1)]
        cdf = [sum(mass[:j+1]) for j in range(n+1)]
        chi = (n+1)*p-k
        factor = max(mass)/((n+1)*p*q)
        for u in [-F(1,2), F(0), F(1,2)]:
            ev4 = edelta = F(0)
            for bits in product((0,1), repeat=2*n):
                probability = F(1)
                u0, u1 = [], []
                for i, bit in enumerate(bits):
                    probability *= (small if bit else large)/(large+small)
                    value = -large if bit else small
                    (u0 if i < n else u1).append(value if i < n else -value)
                vs = [sum(u1[:j])+sum(u0[j:]) for j in range(n+1)]
                # Outside legal counts, the extension is constant. These exact
                # endpoints contain every possible crossing for this tuple.
                left = min(-2, int(k+u-vs[0])-2)
                right = max(n+2, int(k+u-vs[-1])+2)
                eligible = [j for j in range(left, right+1)
                            if j+vs[min(n,max(0,j))] <= k+u]
                K = max(eligible)
                need(K < right, 'right endpoint contains crossing')
                r = K-k
                v = vs[k]
                rp, rm = max(0,r), max(0,-r)
                choose2, choose3 = comb(rm,2) if rm>=2 else 0, comb(rm,3) if rm>=3 else 0
                first2 = max(F(0),chi-1)*rp+max(F(0),chi)*choose2
                coeff = separated_value(chi-u,c,u)
                need(first2 <= coeff*v*v, 'shared quadratic cost')
                d = 2*c-F(1,2)
                need(choose3 <= max(F(0),v)**4/d**4, 'fourth crossing bound')
                fnew = F(0) if K < 0 else F(1) if K > n else cdf[K]
                delta = fnew-cdf[k]-r*mass[k]
                need(delta <= factor*(first2+choose3), 'discrete curvature identity')
                need(delta <= factor*(coeff*v*v+max(F(0),v)**4/d**4), 'combined pointwise bound')
                ev4 += probability*v**4
                edelta += probability*delta
                counts['tuples'] += 1
                counts['nonzero_curvature_tuples'] += delta != 0
            need(ev4 <= upper_fourth, 'independent fourth-moment upper bound')
            need(edelta <= factor*t*(coeff+(large**2+3*t)/d**4), 'expected bound')
            counts['law_phase_cases'] += 1
    return counts


def main():
    root = Path(__file__).resolve().parents[3]
    previous = root/'mathematics/reduction2/2026-10-27/check_local_curvature.py'
    # The previous reader and comparison formula were read before this import.
    # Its guarded main is not executed. No archived program is imported.
    spec = importlib.util.spec_from_file_location('prior_curvature', previous)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    archive = root/'verification/finite-tail/sources/backend.zip'
    need(hashlib.sha256(archive.read_bytes()).hexdigest() == '43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52', 'archive hash')
    with zipfile.ZipFile(archive) as z:
        raw = z.read('finite61/MANIFEST.json')
        need(hashlib.sha256(raw).hexdigest() == 'c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf', 'manifest hash')
        manifest = json.loads(raw)
        src = {}
        for name,pin in old.PINS.items():
            need(manifest['files'][old.PREFIX+name]['sha256'] == pin, 'source pin')
            blob = z.read('finite61/blobs/'+pin)
            need(hashlib.sha256(blob).hexdigest() == pin, 'blob pin')
            src[name] = blob
    jobs = {(j['family'],j['index'],j['sign']):j for j in manifest['low_rows']}
    seen = set(); checked = disjoint_gains = fourth_gains = 0
    best_ratio = F(1); worst_ratio = F(0); largest_gain = F(0); examples = []
    for kind, family, filename in [('central','central42_v2','new_central42_targets.json'),
                                    ('left','left42_final','actual_float_targets.json')]:
        for row in json.loads(src[f'local/{family}/{filename}'])['rows']:
            if F(row['lambda_max']) <= (F('.05') if kind=='central' else F('.08')):
                continue
            bs = old.bands(row,kind)
            if not bs:
                continue
            pl,pu = map(F,row['p']); lm = F(row['lambda_max'])
            ell = old.rootlo((1-F(row['theta']))/(pu*(1-pu)))
            eh = old.rootlo(1/(pl*(1-pl)))+F(1,10**8)
            for sign in (-1,1):
                key=(family,row['index'],sign); job=jobs[key]; seen.add(key)
                hc,oc=job['H_cells'],job['outer_phase_cells']
                H=F(row['H_minus' if sign<0 else 'H_plus'])
                for bi in sorted({0,len(bs)-1}):
                    low,high,phase=bs[bi]
                    c=1-F(row['d0'])*(1-low/lm)
                    profile = (F('.375') if low<F('.08') else F('.325') if low<F('.10') else F('.275') if low<F('.12') else F('.25')) if kind=='central' else (F('.4') if low<F('.08') else F('.35') if low<F('.10') else F('.3') if low<F('.12') else F('.275'))
                    amp=min(F(row['amplitude']),profile)
                    for hj in sorted({0,(hc-1)//2,hc-1}):
                        hl,hh=H*F(hj,hc),H*F(hj+1,hc)
                        hs=(hl,hh) if sign>0 else (-hh,-hl)
                        hqs=[h/e for h in hs for e in (ell,eh)]
                        b=pu-min(hqs)
                        for oi in sorted({0,(oc-1)//2,oc//2,oc-1}):
                            lo=-phase+2*phase*F(oi,oc);hi=-phase+2*phase*F(oi+1,oc)
                            dd=max(abs(h-u) for h in hqs for u in (lo,hi))
                            ownhi=1+dd/(42*pl)
                            S=amp*amp+3*ownhi*high;d=2*c-F(1,2)
                            third=old.rootlo(S)+F(1,10**8)
                            need(third*third>S,'strict outward root')
                            phase_old,_=old.curvature_supremum(b,c,lo,hi)
                            phase_new,candidates=separated_supremum(b,c,lo,hi)
                            cubic_old=third/d**3; cubic_new=min(cubic_old,S/d**4)
                            before=phase_old+cubic_old;after=phase_new+cubic_new
                            need(after<=before,'new cost dominated by previous exact bound')
                            need(any(separated_value(b,c,u)==v==phase_new for u,v in candidates),'attained candidate')
                            for j in range(9):
                                u=lo+(hi-lo)*F(j,8)
                                need(separated_value(b,c,u)<=phase_new,'phase diagnostic')
                            checked+=1;disjoint_gains+=phase_new<phase_old;fourth_gains+=cubic_new<cubic_old
                            if before:
                                ratio=after/before;best_ratio=min(best_ratio,ratio);worst_ratio=max(worst_ratio,ratio)
                            largest_gain=max(largest_gain,before-after)
                            if len(examples)<3 or (row['index']==19 and hj==0 and oi==0):
                                examples.append({'family':family,'row':row['index'],'sign':sign,'band':bi,'H_cell':hj,'phase_cell':oi,'before':str(before),'after':str(after),'S':str(S),'d':str(d),'fourth_active':S/d**4<cubic_old})
    need(seen==set(jobs),'all152 signed row configurations represented')
    # The reciprocal-square-only envelope is useful as an independent bound,
    # but cannot replace the small-noise moment estimate uniformly in n.
    rare_t=F(1,100)
    need(rare_t>3*rare_t**2,'dropping individual fourth moments fails')
    b,c,u=F(9,10),F(9,10),F(2,5)
    rising=(b+u-1)/(c-u)**2;falling=(b+u)/(c+c/3)**2
    need(min(rising,falling)*(c-u)**2<b+u-1,'minimum of disjoint costs is invalid')
    rejected=0
    for data in [(b,F(1,2),F(0),F(1,4)),(b,F(11,10),F(0),F(1,4)),(b,c,F(1,4),F(0)),(b,c,F(-3,5),F(0)),(0.9,c,F(0),F(1,4))]:
        try: separated_supremum(*data)
        except ValueError: rejected+=1
        else: raise ValueError('invalid domain accepted')
    print(json.dumps({'status':'PASS_BOUNDED_COUNT_COST','comparison_source_sha256':hashlib.sha256(previous.read_bytes()).hexdigest(),'source_pins':old.PINS,'signed_row_configurations':len(seen),'sampled_cells':checked,'disjoint_strict_improvements':disjoint_gains,'fourth_strict_improvements':fourth_gains,'new_over_previous_exact_min':str(best_ratio),'new_over_previous_exact_max':str(worst_ratio),'largest_coefficient_gain':str(largest_gain),'examples':examples,'actual_coupling_checks':coupled_checks(),'malformed_domains_rejected':rejected,'scope':'Proved component domination; bounded real-law and source-parameter checks. No native LOW acceptance or acquisition acceptance.'},indent=2))


if __name__=='__main__':
    main()

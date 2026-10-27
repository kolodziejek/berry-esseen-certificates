#!/usr/bin/env python3
"""Independent conservative resource arithmetic, no constructor/native imports.

Uses the linear tangent 1-3*theta/2 instead of the constructor's square-root
lower bound, and independently enclosed dyadic square roots. It certifies
only conditional consequences of the pinned acquired rows, not acquisition.
"""
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import sys
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[4]
PREFIX = 'work/toward40_20261007/audit43/capsule/work/below49_20261006/'
PINS = {
    'package_audit/left42_confinement/post_sperner42_exact.json': 'd0a1f547aa4c181d4ad64e9db403ae566760137d1fe75caedc4f317c8aec2ace',
    'package_audit/left42_confinement/confinement42_proof.json': 'b75c5bf10dfcc47b33d4e273a8591f0332feb6351251fb65bc21928cb597bd40',
    'package_audit/left42_confinement/profiles42_proof.json': '2f275bf59e018bac8f53327e1649a71b1c13e30d7e70171a6c8664c4f7bddcdd',
    'acquisition/central42_confinement_candidate.json': '2f95d0271996eb9868c2fffcdfb0fa2646a99c2cf588e70d063178e27d07246d',
    'acquisition/central42_profiles_candidate.json': '5667786996a88f241225d53d99ec28a797c9f37a874a74d4f51e5c28f86a7336',
    'package_audit/left42_confinement/contracted_kernel.py': 'b216161eec801c96a77df81fb77771e86e6ab55f0fc1b14cd2428508191a3dfc',
    'package_audit/left42_confinement/coupled_panel_core.py': 'adb21a5ee493fc9c257aa3ba67cdf1a162a841d40798d3e423bd2bc93a16aa3e',
    'package_audit/left42_confinement/corrected_phase_callback_extended.py': '036d32989f9c522e9d6151cf8898338e13ed2c9790a5d2c003bff095df270a63',
    'acquisition/central42_acquisition_core.py': 'edd75b67061e484ba62e0266101c9fe3f98af8d15ac26218a259c630261b37ce',
}
N, C0, CHI = 42, Q('.4095'), Q('.40974')
SL, SU = Q('3.162277660'), Q('3.162277661')
SEAMS = tuple(map(Q, ('.05', '.08', '.10', '.12')))


def need(value, message):
    if not value:
        raise ValueError(message)


def panels(rows, first, count):
    need(len(rows) == count, 'complete panel count')
    for i, row in enumerate(rows):
        need((Q(row['pl']), Q(row['pu'])) == (Q(first+i, 500), Q(first+i+1, 500)),
             'ordered closed probability panel')


def parabola_sup(corner):
    a, denominator = corner['A'], 4*corner['Qbudget']
    need(denominator > 0, 'positive phase curvature')
    return max(a + max(Q(0), corner[sign])**2/denominator for sign in ('Fminus', 'Fplus'))


def score_budget(row, family):
    corners = [{key: Q(value) for key, value in corner.items()} for corner in row['quadratics']]
    need(len(corners) == 4, 'all four coherent corners')
    if family == 'left':
        need([c['C'] for c in corners] == [C0, C0, Q('.4226'), Q('.4226')], 'fixed left score endpoints')
        need(corners[0]['rho'] == corners[2]['rho'] and corners[1]['rho'] == corners[3]['rho'], 'paired moment corners')
        cmin = cmax = Q('.4226')
        need(CHI + Q(row['raw'])/N >= cmax, 'saturated exact left score cap')
    else:
        r = Q(row['raw'])
        cmin = min(Q('.4247'), CHI+(r-Q(1, 500000))/N)
        cmax = min(Q('.4247'), CHI+r/N)
    need(C0 < CHI < cmin <= cmax, 'score interpolation endpoints')
    # True chord weight lies between these two numbers. Coefficientwise
    # interval bounds give an upper parabola at CHI, including central rounding.
    weights = [(CHI-C0)/(score-C0) for score in (cmin, cmax)]
    interpolants = []
    for j in (0, 1):
        interpolants.append({key: (min if key == 'Qbudget' else max)(
            corners[j][key] + w*(corners[j+2][key]-corners[j][key]) for w in weights)
            for key in ('A', 'Fminus', 'Fplus', 'Qbudget')})
    middle = max(map(parabola_sup, interpolants))
    uncharged_low = max(map(parabola_sup, corners[:2]))
    charged_high = max(map(parabola_sup, corners[2:]))-N*(cmin-CHI)
    need(middle >= uncharged_low and middle >= charged_high,
         'middle dominates with universal rho >= 1')
    return middle


def dyadic_root_upper(value):
    need(value > 0, 'positive variance')
    scale = 1 << 40
    root = Q(isqrt(value.numerator*scale*scale//value.denominator)+1, scale)
    need(root*root > value, 'dyadic outward square root')
    return root


def conservative_result(row, family, index):
    budget = score_budget(row, family)
    l, u, theta, a, b = (Q(row[key]) for key in ('pl', 'pu', 'theta', 'A', 'B'))
    need(0 < l < u < Q(1, 2) and 0 <= theta < Q(2, 3) and a > 0 and b > 0,
         'actual geometry and positive linear tangent')
    variance = u*(1-u)
    distance = max(Q(0), (4-SU)/2-u, l-(4-SL)/2)
    binary = (6+2*SL)*(1-3*theta/2)*distance**2/dyadic_root_upper(variance)
    price = min(3*(SL+1)*b, 3*(SL+3)*a)
    defect = min(Q(row['D']), budget*15000/(997*N))
    residual = defect-binary
    if residual < 0:
        return dict(index=index, excluded=True, residual=residual, crossed=[])
    need(residual > 0, 'zero residual needs explicit zero-noise handling')
    noise = N*variance*residual/(price*(1-theta))
    inward = residual/(6*(1-theta)*(a+b))
    need(noise <= Q(row['lambda_max']) and inward <= Q(row['inward_d_max']),
         'both new conservative intercepts no larger than old')
    crossed = [x for x in SEAMS if noise < x <= Q(row['lambda_max'])]
    return dict(index=index, excluded=False, noise=noise, inward=inward,
                crossed=crossed, noise_upper_1e9=Q(-((-noise.numerator*10**9)//noise.denominator), 10**9))


def main():
    need(__debug__ and not sys.flags.optimize, 'unoptimized exact check')
    archive = ROOT/'verification/finite-tail/sources/backend.zip'
    need(sha256(archive.read_bytes()).hexdigest() == '43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52', 'archive binding')
    data, bindings = {}, []
    with ZipFile(archive) as z:
        raw = z.read('finite61/MANIFEST.json')
        need(sha256(raw).hexdigest() == 'c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf', 'manifest binding')
        files = json.loads(raw)['files']
        for relative, pin in PINS.items():
            need(files[PREFIX+relative]['sha256'] == pin, 'source path binding')
            source = z.read('finite61/blobs/'+pin)
            need(sha256(source).hexdigest() == pin, 'source bytes')
            bindings.append(dict(path=PREFIX+relative, sha256=pin, lines=len(source.splitlines())))
            if relative.endswith('.json'):
                data[relative] = json.loads(source)
    left = data['package_audit/left42_confinement/post_sperner42_exact.json']
    parent = data['package_audit/left42_confinement/confinement42_proof.json']
    central = data['acquisition/central42_confinement_candidate.json']
    lp = data['package_audit/left42_confinement/profiles42_proof.json']
    cp = data['acquisition/central42_profiles_candidate.json']
    need(left['N'] == 42 and left['L'] == 48 and central['N'] == 42, 'retained source scope')
    need(left['rows'] == [p['final'] for p in parent['rows']], 'exact final acquired parent rows')
    need(lp['source_sha256'] == PINS['package_audit/left42_confinement/post_sperner42_exact.json']
         and cp['source_sha256'] == PINS['acquisition/central42_confinement_candidate.json'], 'profile parent bindings')
    panels(left['rows'], 145, 45)
    panels(central['rows'], 190, 47)
    need(SL**2 < 10 < SU**2, 'sqrt10 rational bounds')
    # Independent tighter Machin truncation and an explicit tangent identity.
    def atan_series(x, count):
        return sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(count)), Q(0))
    lo = 16*atan_series(Q(1,5), 8)-4*atan_series(Q(1,239), 1)
    hi = 16*atan_series(Q(1,5), 7)-4*atan_series(Q(1,239), 2)
    need((Q(120,119)-Q(1,239))/(1+Q(120,119)/239) == 1, 'Machin tangent identity')
    need(4*(Q(1,5)-Q(1,375))-Q(1,239) > 0 and Q(4,5) < 1, 'Machin positive short branch')
    need((19+6*SL)/(72*hi) > C0**2 and (19+6*SU)/(72*lo) < CHI**2, 'Esseen constant bracket')
    results = {name: [conservative_result(row, name, i) for i,row in enumerate(obj['rows'])]
               for name,obj in [('left',left), ('central',central)]}
    need([r['index'] for r in results['left'] if r['excluded']] == [0], 'only left0 excluded')
    need(not any(r['excluded'] for r in results['central']), 'all central survive')
    want = {'left': [(5,[Q('.05')]),(8,[Q('.08')]),(10,[Q('.10')]),(13,[Q('.12')])],
            'central': [(28,[Q('.10')])]}
    for family in results:
        need([(r['index'],r['crossed']) for r in results[family] if r['crossed']] == want[family], 'all named threshold crossings')
    drops = []
    for i,p in enumerate(lp['rows']):
        if results['left'][i]['excluded']:
            continue
        for band in p['profiles']:
            if results['left'][i]['noise'] < Q(band['requested_noise'][0]) and band['source'] == 'joint_resource_profile':
                need(len(band['signs']) == 2, 'both signed profile calls')
                drops.append(dict(index=i, lower=band['requested_noise'][0],
                                  recorded_gates=[s['gates']['count'] for s in band['signs']]))
    need(drops == [dict(index=10,lower='1/10',recorded_gates=[1795,295]),
                   dict(index=13,lower='3/25',recorded_gates=[2265,295])], 'exact profile consumers')
    central_dropped = [r for r in cp['rows'] if r['index'] == 28 and r['band'] == 2]
    need(len(central_dropped) == 2 and all(r['proof'].get('inherited') is True for r in central_dropped), 'central28 no native profile arithmetic')
    controls = []
    def reject(name, fn):
        try:
            fn()
        except ValueError:
            controls.append(name)
        else:
            raise ValueError('invalid control accepted: '+name)
    reject('missing_panel', lambda: panels(left['rows'][:-1], 145, 45))
    reject('reordered_panels', lambda: panels(list(reversed(left['rows'])), 145, 45))
    bad = deepcopy(left['rows'][0]);bad['quadratics'][2]['C'] = '.43'
    reject('changed_score_endpoint', lambda: score_budget(bad, 'left'))
    reject('nonpositive_phase_curvature', lambda: parabola_sup(dict(A=Q(1),Fminus=Q(0),Fplus=Q(1),Qbudget=Q(0))))
    for family,index,seam in [('left',6,'.05'),('left',9,'.08'),('central',38,'.05')]:
        reject('unsupported_'+family+str(index)+'_deletion', lambda f=family,i=index,s=seam:
               need(results[f][i]['noise'] < Q(s), 'this computed cap does not delete the row'))
    # Necessity witnesses for two tempting invalid relaxations.
    need(N*(CHI-Q('.40973')) > 0, 'positive charge would be false at C=c=.40973')
    need(84*Q(1,4) > 42*Q(1,4), 'unweighted D does not yield a uniform noise ceiling')
    def compact(r):
        return {k: str(v) if isinstance(v,Q) else [str(x) for x in v] if isinstance(v,list) else v
                for k,v in r.items() if k not in ('noise','inward')}
    print(json.dumps(dict(status='PASS_INDEPENDENT_CONSERVATIVE_RESOURCE_CHECK',
                         mathematical_status='Conditional consequences of pinned acquired resources; full analytic/native acceptance not established.',
                         execution_status='Fresh exact Fraction/dyadic calculation; no constructor or archived program imported.',
                         source_bindings=bindings, constant_bounds=dict(pi_lower=str(lo),pi_upper=str(hi)),
                         rows={f:list(map(compact,rs)) for f,rs in results.items()},
                         profile_calls=drops, recorded_profile_gate_sum=sum(sum(d['recorded_gates']) for d in drops),
                         central28_profile_arithmetic_saved=0, rejected_controls=controls,
                         invalid_relaxations_demonstrated=['positive excess charge at equality','unweighted resource'],
                         full_proof_pass=False), indent=2))


if __name__ == '__main__':
    main()

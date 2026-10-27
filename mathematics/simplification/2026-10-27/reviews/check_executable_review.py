#!/usr/bin/env python3
"""Independent bounded review. Executes only the two NEW checkers and copies.

Archive members are data, never executed/imported. Mutants are temporary copies.
This is not a local-certificate acceptance or a review of uniform42.md.
"""
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / 'runs/simplification-20261027/executable-review01'
DIR = ROOT / 'mathematics/simplification/2026-10-27'
ARCHIVE = ROOT / 'verification/finite-tail/sources/backend.zip'
BASELINE = '6346fc1b4432bc5982822aa696eb566ed9e1e1ee'
PREFIX = 'work/toward40_20261007/audit43/capsule/work/below49_20261006/'


def need(v, message):
    if not v:
        raise ValueError(message)


def root_pair(x):
    # Independently audit the endpoints, including the adjacent lower/upper grid.
    k = isqrt(x.numerator * 10**24 // x.denominator)
    a, b = F(k, 10**12), F(k + 1, 10**12)
    need(a*a <= x < b*b and b-a == F(1, 10**12), 'exact root grid')
    return a, b


def poly_add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def poly_product(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i+j] = out.get(i+j, F(0)) + x*y
    return {k: v for k, v in out.items() if v}


def main():
    need(__debug__ and not sys.flags.optimize, 'unoptimized Python')
    OUT.mkdir(parents=True, exist_ok=True)
    runs = []
    outputs = {}
    inputs = {}
    for name in ('check_support_lift.py', 'check_finite_entry.py'):
        path = DIR / name
        inputs[str(path.relative_to(ROOT))] = sha256(path.read_bytes()).hexdigest()
        cmd = ['python3', str(path.relative_to(ROOT))]
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True)
        (OUT / (name + '.stdout.json')).write_bytes(result.stdout)
        (OUT / (name + '.stderr.txt')).write_bytes(result.stderr)
        need(result.returncode == 0, 'fresh original checker failed: ' + name)
        outputs[name] = json.loads(result.stdout)
        runs.append(dict(command=cmd, cwd='.', returncode=result.returncode,
                         stdout_sha256=sha256(result.stdout).hexdigest(),
                         stderr_sha256=sha256(result.stderr).hexdigest()))
    sup = outputs['check_support_lift.py']; ent = outputs['check_finite_entry.py']
    need(len(sup['negative_controls']) == 10 and all(sup['negative_controls'].values()), 'all ten controls')
    need(len(ent['negative_controls']) == 4, 'four entry controls')

    # Independent scalar calculations, not values imported from either checker.
    scalar = []
    for n, s in ((42, F(81, 80)), (43, F(253, 250))):
        need(s*s*(n-1)>n and n-1>36, 'scalar endpoint')
        bound = F(n,n-1)*(F(41,200)+F(2,25)*s)
        own = F(41,100)+F(3,10*n)
        need(bound<F(3,10) and own<F(2113,5000), 'scalar inclusion')
        scalar.append(dict(n=n, bound=str(bound), reserve=str(F(3,10)-bound),
                           own=str(own), own_reserve=str(F(2113,5000)-own)))
    need(scalar[0]['bound']==ent['scalar42']['excess_upper'] and
         scalar[1]['bound']==ent['scalar']['excess_upper'], 'reported scalar values')

    ell, _ = root_pair(F(41)); _, s = root_pair(F(42,41))
    r = min(F(3031*646,10**7)/F(1064,10000), F(3322*429,10**7)/F(773,10000))
    _, disc = root_pair((2+r*r)**2-4*(1-r*r))
    _, b = root_pair((disc-2-r*r)/2)
    need(ell*ell < 41 and s*s > F(42,41) and s<F(81,80), 'scale orientations')
    need((1+b*b)**2>r*r*(1-b*b) and 0<b<F(2,3), 'beta inequality')
    need(str(s)==sup['inherited_S'] and str(r)==sup['initial_r'] and str(b)==sup['initial_b'], 'original initial constants')
    for name,u,rl,rh,bh in [('initial',F(21,5),F(46,25),F(37,20),F(2,3)),
                          ('left',F(39,10),F(1),F(3,2),F(1,2))]:
        q={0:F(48,125)*rh/42,1:3*bh,2:F(3,2)*rh,3:F(-1)}
        qp={k-1:k*v for k,v in q.items()if k};qpp={k-1:k*v for k,v in qp.items()if k}
        val=lambda p:sum(v*u**k for k,v in p.items())
        L=poly_add({0:F(2,5)*(F(1,2)+F(48,125)/42),2:F(1,5)},
                   {k:F(819,2000)*v for k,v in qp.items()})
        Lp={k-1:k*v for k,v in L.items()if k};Lpp={k-1:k*v for k,v in Lp.items()if k}
        values={k:val(p)for k,p in [('Q',q),('Q_prime',qp),('Q_second',qpp),('L',L),('L_prime',Lp),('L_second',Lpp)]}
        need(all(v<0 for v in values.values()),'independent ray polynomial signs')
        need({k:str(v)for k,v in values.items()}==sup[name]['ray_gates'],'reported ray values')
        gap=F(19,100)*rl-F(81,80)**2*(u**5-15*u)/4700
        need(gap>0 and str(gap)==sup[name]['domination_margin'],'independent splice domination')

    # Expand the scale square independently in coefficient dictionaries.
    c = F(48,125)
    square = poly_product({0:F(1),1:F(-1)},
                          poly_product({0:F(1),1:F(1,2),2:c}, {0:F(1),1:F(1,2),2:c}))
    actual = poly_add(square, {0:F(-1)})
    expected = {2:2*c-F(3,4),3:-c-F(1,4),4:c*c-c,5:-c*c}
    need(actual==expected, 'scale polynomial coefficient identity')
    margin = sum(v*F(1,42)**(k-2) for k,v in expected.items())
    need(margin>0 and str(margin)==sup['scale_margin'], 'scale endpoint')

    # The contact difference has only 6/5 S^3 D_- W - q r S W left.
    # Compare all coefficients using a sparse representation independent of the
    # checker's list arithmetic; adverse remainder and Q cancel algebraically.
    a={1:F(-1,2),3:F(1,6)}; j={1:F(-15),5:F(1)}
    w=poly_add(a,{k:-F(1,656)*v for k,v in j.items()})
    left=poly_product(w,poly_add({k:F(6,5)*s**3*v/F(5640) for k,v in j.items()}, {0:-F(19,100)*r*s}))
    right=poly_product({k:s*v for k,v in w.items()},poly_add({k:s*s*v/F(4700) for k,v in j.items()},{0:-F(19,100)*r}))
    need(left==right, 'independent contact coefficient identity')

    archive_bytes=ARCHIVE.read_bytes()
    baseline=subprocess.run(['git','show',BASELINE+':verification/finite-tail/sources/backend.zip'],cwd=ROOT,capture_output=True)
    need(baseline.returncode==0 and baseline.stdout==archive_bytes,'preserved baseline archive')
    inputs['verification/finite-tail/sources/backend.zip']=sha256(archive_bytes).hexdigest()
    bindings=[]
    with ZipFile(ARCHIVE) as z:
        raw=z.read('finite61/MANIFEST.json'); m=json.loads(raw)
        def read(path):
            record=m['files'][path]; data=z.read('finite61/blobs/'+record['sha256'])
            need(len(data)==record['bytes'] and sha256(data).hexdigest()==record['sha256'],'source identity '+path)
            bindings.append(dict(path=path,sha256=record['sha256']))
            return data
        proof=json.loads(read(PREFIX+'package_audit/left42_exact/acquisition42_proof.json'))
        route_bytes=read(PREFIX+'package_audit/left42_exact/fixed_route.json'); route=json.loads(route_bytes)
        initial_bytes=read(PREFIX+'package_audit/left42_exact/initial42_candidate.json')
        need(proof['source_sha256']==sha256(initial_bytes).hexdigest() and proof['route_sha256']==sha256(route_bytes).hexdigest(),'left parent file bindings')
        for tail in ('acquisition/check_local42_support.py','acquisition/heat_support50.py','acquisition/fifth_heat50.py','package_audit/left42_exact/heat_support50.py','package_audit/left42_exact/fifth_heat50.py','package_audit/left42_exact/accept_acquisition.py'):
            read(PREFIX+tail)
        need(m['files'][PREFIX+'acquisition/heat_support50.py']['sha256']==m['files'][PREFIX+'package_audit/left42_exact/heat_support50.py']['sha256'],'same heat implementation')
        need(m['files'][PREFIX+'acquisition/fifth_heat50.py']['sha256']==m['files'][PREFIX+'package_audit/left42_exact/fifth_heat50.py']['sha256'],'same fifth implementation')
        active=[]
        for index, row in enumerate(proof['coarse']):
            need(list(map(F,row['input_p']))==[F(23+index,100),F(24+index,100)],'coarse ordered coverage')
            if not row.get('excluded'):active.append(row)
        need(len(active)==11,'active parent count')
        calls=[proof['first_bridge']]
        for index,(cell, rr) in enumerate(zip(proof['fine'],route['rows'])):
            parent=active[index//5]; child=index%5
            need(list(map(F,cell['p']))==[F(parent['pl'])+F(child,500),F(parent['pl'])+F(child+1,500)],'coarse to fine ancestry')
            radii=list(map(F,rr['radii']))
            need(len(radii)==len(cell['trace']) and radii[0]==F(121,40) and all(y<x for x,y in zip(radii,radii[1:])),'fixed decreasing radius route')
            need(cell['final']==cell['trace'][-1]['resource'] and bool(cell['final'].get('excluded'))==(index<10),'final same-law and exclusion pattern')
            for step_i, step in enumerate(cell['trace']):
                need(F(step['radius'])==radii[step_i],'same radius in route')
                if step_i==0:need(step['contraction'] is None,'initial common bridge')
                else:
                    previous=cell['trace'][step_i-1]['resource']; q=step['contraction']
                    need(F(q['rho_upper'])==F(previous['rho']) and F(q['beta_absolute_upper'])==F(previous['beta']),'same preceding moment bounds')
                    calls.append(q)
        need(len(calls)==64,'left call total')
        for row in calls:
            cells=[tuple(map(F,c))for c in row['closed_cells']]
            need(cells[0][0]==F(row['radius']) and cells[-1][1]==F(9,2) and all(x<y for x,y in cells) and all(x[1]==y[0] for x,y in zip(cells,cells[1:])),'radial closed coverage')
        initial=m['actions'][6]['stdout_rule']['expected']['row']
        need(initial['n_band']==[42,48] and F(initial['radius'])==F(96,25) and F(initial['slow'])==F(19,100) and F(initial['rho_upper'])==r and F(initial['beta_absolute_upper'])==b,'initial source parameter identity')
        need(len(initial['closed_cells'])==14,'initial fourteen cells')
        # Confirm task selection against actual noise thresholds in target data.
        observed=[]
        for family,target,threshold in [('central42_v2','new_central42_targets.json',F(1,20)),('left42_final','actual_float_targets.json',F(2,25))]:
            data=json.loads(read(PREFIX+'local/'+family+'/'+target))
            for row in data['rows']:
                if F(row['lambda_max'])>threshold:
                    observed.extend((family,row['index'],sign)for sign in(-1,1))
        labels=[(v['family'],v['index'],v['sign'])for v in m['low_rows']]
        need(labels==observed and len(observed)==152,'actual target-derived LOW inventory')
        mapping=[dict(id=a['id'],script=a['script'],arguments=a['arguments'],retained=a['id'] in ent['retained_native'])for a in m['actions']]
        need(len(mapping)==31 and sum(a['retained']for a in mapping)==19,'native partition')

    # Copy-only mutations: expected passes expose limits, not hidden failures.
    source=(DIR/'check_support_lift.py').read_text()
    cases=[
        ('wrong_identity_divisor','S**2 / 4700','S**2 / 4701',False),
        ('wrong_favorable_upper_endpoint','LAST = 42, 48','LAST = 42, 49',False),
        ('inward_scale_rounding','_, S = roots(F(N, N - 1))','S, _ = roots(F(N, N - 1))',True),
        ('shared_H4_transcription','H4 = [3, 0, -6, 0, 1]','H4 = [3, 0, -5, 0, 1]',True),
        ('shared_remainder_transcription','F(51, 14400 * (N - 1))','F(52, 14400 * (N - 1))',True),
        ('corrupt_archive_pin',"ARCHIVE_SHA = '43b606", "ARCHIVE_SHA = '03b606",False),
        ('omitted_old_radial_cell',"rows = bind_left_rows(proof)","proof['first_bridge']['closed_cells'].pop(1)\n    rows = bind_left_rows(proof)",True),
    ]
    mutations=[]
    with TemporaryDirectory(prefix='be-executable-review-') as temp:
        for name,old,new,expected_pass in cases:
            need(source.count(old)==1,'unique mutation site '+name)
            changed=source.replace(old,new); p=Path(temp)/(name+'.py');p.write_text(changed)
            result=subprocess.run(['python3',str(p)],cwd=ROOT,capture_output=True)
            passed=result.returncode==0
            need(passed==expected_pass,'unexpected mutation outcome '+name)
            stderr=result.stderr.decode().replace(str(p),'<disposable-new-checker-copy>')
            (OUT/(name+'.stdout.txt')).write_bytes(result.stdout)
            (OUT/(name+'.stderr.txt')).write_text(stderr)
            mutations.append(dict(name=name,replacement=[old,new],source_sha256=sha256(changed.encode()).hexdigest(),returncode=result.returncode,expected_pass=expected_pass,stdout_sha256=sha256(result.stdout).hexdigest()))
    report=dict(status='PASS_BOUNDED_INDEPENDENT_EXECUTABLE_REVIEW',
                reviewed_commit='341c1e3f77806a4aaa178051f6f8c80c13bd63ac',
                baseline_archive_unchanged=True, native_archived_programs_executed=0,
                original_runs=runs,source_bindings=bindings,scalar=scalar,
                exact_constants=dict(ell=str(ell),S=str(s),r=str(r),b=str(b)),
                support_calls=65,left_parent_chains=55,low_rows=152,
                native_mapping=mapping,mutations=mutations)
    (OUT/'independent.json').write_text(json.dumps(report,indent=2)+'\n')
    inputs[str(Path(__file__).relative_to(ROOT))]=sha256(Path(__file__).read_bytes()).hexdigest()
    (OUT/'run.json').write_text(json.dumps(dict(command=['python3',str(Path(__file__).relative_to(ROOT))],cwd='.',python_version=sys.version.splitlines()[0],returncode=0,input_sha256=inputs),indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in ['source_bindings','native_mapping','mutations']},indent=2))


if __name__=='__main__':
    main()

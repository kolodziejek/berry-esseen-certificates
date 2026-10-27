#!/usr/bin/env python3
"""Independent bounded exact review; no submitted/native module is imported.

Uses scalar evaluations at12 distinct rational points to establish equality
of polynomials of degree<=11, not to certify positivity on an interval.
Old support/resource sign predicates remain conditional inputs.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
import json
import sys
import zipfile

if sys.flags.optimize or not __debug__ or len(sys.argv) != 1:
    raise RuntimeError('Unoptimized Python, fixed inputs')
ROOT = Path(__file__).resolve().parents[3]
ARCHIVE = ROOT / 'verification/finite-tail/sources/backend.zip'
LEFT = '419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393'
PREFIX = 'work/toward40_20261007/audit43/capsule/work/below49_20261006/package_audit/left42_exact/'
C, E0, S, ELL = F(819,2000), F(48,125*42), F(1012121654695,10**12), F(6403124237432,10**12)

def require(condition, message):
    if not condition:
        raise ValueError(message)

require(ELL**2 < 41 < (ELL+F(1,10**12))**2, 'ell enclosure')
require((S-F(1,10**12))**2 < F(42,41) < S**2 < F(81,80)**2, 'S enclosure')

def ancestry(p, route):
    require(len(p['coarse'])==15 and len(p['fine'])==len(route['rows'])==55, 'complete rows')
    for i,row in enumerate(p['coarse']):
        require(list(map(F,row['input_p']))==[F(23+i,100),F(24+i,100)], 'coarse closed cover')
    active=[r for r in p['coarse'] if not r.get('excluded')]
    require(len(active)==11, '11 surviving coarse parents')
    first=p['first_bridge']
    require(F(first['rho_upper'])==max(F(r['rho']) for r in active), 'first rho maximum')
    require(F(first['beta_absolute_upper'])==max(F(r['beta']) for r in active), 'first beta maximum')
    require(F(first['radius'])==F(121,40), 'common first radius')
    calls=[('common',first)]
    for i,(row,plan) in enumerate(zip(p['fine'],route['rows'])):
        parent=active[i//5]; j=i%5
        pp=[F(parent['pl'])+F(j,500),F(parent['pl'])+F(j+1,500)]
        require(list(map(F,row['p']))==list(map(F,plan['p']))==pp==[F(135+i,500),F(136+i,500)], 'five child ancestry')
        trace=row['trace']; radii=list(map(F,plan['radii']))
        require(len(trace)==len(radii)>0 and radii[0]==F(121,40), 'all scheduled stages')
        require(all(b<a for a,b in zip(radii,radii[1:])), 'strict contraction order')
        require(trace[0]['contraction'] is None, 'common bridge used first')
        require(row['final']==trace[-1]['resource'] and F(row['radius'])==radii[-1], 'final resource ancestry')
        require(bool(row['final'].get('excluded'))==plan['excluded']==(i<10), 'exclusion disposition')
        for k,step in enumerate(trace):
            require(F(step['radius'])==radii[k], 'actual route radius')
            if not k:
                continue
            before=trace[k-1]['resource']; bridge=step['contraction']
            require(not before.get('excluded') and bridge is not None, 'no excluded continuation or missing bridge')
            require(F(bridge['radius'])==radii[k], 'bridge radius')
            require(F(bridge['rho_upper'])==F(before['rho']), 'prior rho')
            require(F(bridge['beta_absolute_upper'])==F(before['beta']), 'prior beta')
            calls.append((f'fine{i}:stage{k}',bridge))
    require(len(calls)==64, 'all64 support calls')
    for label,r in calls:
        require(r['n_band']==[42,48] and F(r['barrier'])==0 and F(r['slow'])==F(19,100), 'old theorem scope')
        require(F(r['current_score_lower'])==C and F(r['scale_coefficient'])==F(48,125), 'old constants')
        require(F(5,2)<=F(r['radius'])<=F(121,40), 'radius domain')
        require(1<=F(r['rho_upper'])<=F(3,2) and 0<=F(r['beta_absolute_upper'])<=F(1,2), 'parameter rectangle')
        cells=list(map(lambda row:list(map(F,row)),r['closed_cells']))
        require(cells[0][0]==F(r['radius']) and cells[-1][1]==F(9,2), 'old cover endpoints')
        require(all(a<b and b-a<=F(1,20) for a,b in cells), 'old closed cells')
        require(all(a[1]==b[0] for a,b in zip(cells,cells[1:])), 'old cover seams')
    return calls

def evaluate(u,r,b,dl,q):
    a=(u**3-3*u)/6; j=u**5-15*u; h=u**4-6*u*u+3
    du=j/F(4920); w=a-F(15,2)*du; b2=h*h/F(10496)
    e=F(51,590400)*u**6/ELL+F(51,39360)*(3*u*u-2)/ELL+u/F(13448)
    cubic=-u**3+F(3,2)*r*u*u+3*b*u+r*E0
    contact=F(2,5)*S**3*((a-3*dl)*w+b2)+S**3*e*w+(C*cubic+r*S*q)*w
    dom=(a/2-3*dl-3*du-h/(12*ELL))*w+b2
    return contact,dom,w,j

def splice(u,rmin,rmax,bmax,remaining_loss=F(0)):
    margin=(F(19,100)-remaining_loss)*rmin-F(81,80)**2*(u**5-15*u)/4700
    q=-u**3+F(3,2)*rmax*u*u+3*bmax*u+rmax*E0
    d1=-3*u*u+3*rmax*u+3*bmax;d2=-6*u+3*rmax
    gates=[q,d1,d2,F(2,5)*(u*u/2+F(1,2)+E0)+C*d1,F(2,5)*u+C*d2,F(2,5)-6*C]
    require(margin>0 and all(x<0 for x in gates), 'strict bridge/ray rectangle')
    return margin,gates

with zipfile.ZipFile(ARCHIVE) as z:
    require(sha256(ARCHIVE.read_bytes()).hexdigest()=='43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52', 'archive')
    manifest=json.loads(z.read('finite61/MANIFEST.json'))
    def read(d):
        raw=z.read('finite61/blobs/'+d);require(sha256(raw).hexdigest()==d,'blob identity');return json.loads(raw)
    proof=read(LEFT)
    route_sha=manifest['files'][PREFIX+'fixed_route.json']['sha256']
    initial_sha=manifest['files'][PREFIX+'initial42_candidate.json']['sha256']
    require(proof['route_sha256']==route_sha and proof['source_sha256']==initial_sha,'route and INITIAL source identity')
    route=read(route_sha);read(initial_sha)
calls=ancestry(proof,route)
params=[(F(7361,4000),F(641562334877,10**12))]+[(F(r['rho_upper']),F(r['beta_absolute_upper']))for _,r in calls]
require(params[0][0]==min(F('0.3031')*F('0.646')/(C-F('0.3031')),F('0.3322')*F('0.429')/(C-F('0.3322'))),'initial rho parameter')
require((1+params[0][1]**2)**2>params[0][0]**2*(1-params[0][1]**2),'initial signed-moment bound')
identity_evaluations=0
for r,b in params:
    for i in range(12):
        u=F(i,2);dl=(u**5-15*u)/5640
        old,oldg,w,j=evaluate(u,r,b,dl,F(19,100));new,newg,_,_=evaluate(u,r,b,F(0),F(0))
        require(new-old==S*w*(S*S*j/4700-F(19,100)*r), 'contact polynomial identity')
        require(newg-oldg==3*dl*w, 'domination polynomial identity')
        identity_evaluations+=2
initial=splice(F(21,5),F(46,25),F(37,20),F(2,3));left=splice(F(39,10),F(1),F(3,2),F(1,2))
require(initial[0]==F(3679155107,47000000000) and left[0]==F(17940880361,3008000000000),'reported margins')
x=F(1,42);a=F(48,125)
scale=(2*a-F(3,4))-(a+F(1,4))*x+(a*a-a)*x*x-a*a*x*x*x
require(scale==F(118707,42875000)>0,'uniform scale gate')
controls=[]
def reject(label,fn):
    try:fn()
    except (ValueError,TypeError,KeyError):controls.append(label)
    else:raise ValueError('false input accepted '+label)
reject('retain_full_old_loss',lambda:splice(F(39,10),F(1),F(3,2),F(1,2),F(19,100)))
reject('positive_loss01_in_broad_left_rectangle',lambda:splice(F(39,10),F(1),F(3,2),F(1,2),F(1,100)))
reject('blind_left_splice45',lambda:splice(F(9,2),F(1),F(3,2),F(1,2)))
reject('ray_r_cap4',lambda:splice(F(39,10),F(1),F(4),F(1,2)))
p=deepcopy(proof);p['coarse'][4]['input_p'][0]='0'
reject('broken_coarse_ancestry',lambda:ancestry(p,route))
p=deepcopy(proof);p['fine'][10]['trace'][1]['contraction']=None
reject('missing_support_edge',lambda:ancestry(p,route))
p=deepcopy(proof);p['fine'][10]['trace'][1]['contraction']['rho_upper']='1'
reject('changed_parent_moment',lambda:ancestry(p,route))
ro=deepcopy(route);ro['rows'][10]['radii'].reverse()
reject('reversed_radius_schedule',lambda:ancestry(proof,ro))
print(json.dumps(dict(status='PASS_INDEPENDENT_SUPPORT_LIFT_ALGEBRA_AND_ANCESTRY',
    native_programs_executed=0,old_polynomial_signs_checked=False,
    polynomial_degree_bound=11,distinct_points_per_identity=12,identities=130,
    exact_identity_evaluations=identity_evaluations,left_support_calls=len(calls),
    route_sha256=route_sha,initial_sha256=initial_sha,
    initial_margin=str(initial[0]),left_margin=str(left[0]),
    initial_ray_gates=list(map(str,initial[1])),left_ray_gates=list(map(str,left[1])),
    scale_margin=str(scale),negative_controls=controls,
    r_min=str(min(F(r['rho_upper'])for _,r in calls)),r_max=str(max(F(r['rho_upper'])for _,r in calls)),
    b_max=str(max(F(r['beta_absolute_upper'])for _,r in calls)),
    conclusion='Conditional implication review only; no numerical LOCAL42 or global proof acceptance.'),indent=2))

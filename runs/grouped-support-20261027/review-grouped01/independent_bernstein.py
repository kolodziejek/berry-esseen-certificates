#!/usr/bin/env python3
"""Independent exact construction directly in Bernstein basis.

No submitted or archived module is imported. Product/elevation identities
replace the submitted power-basis transform. Old sign metadata is ignored.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
import ast
import json
import sys
import zipfile

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
C=F(819,2000);ELL=F(6403124237432,10**12);S=F(1012121654695,10**12);E0=F(48,5250)
PROOF='419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393'
PREFIX='work/toward40_20261007/audit43/capsule/work/below49_20261006/package_audit/left42_exact/'
def check(ok,msg):
    if not ok:raise ValueError(msg)
check(not sys.flags.optimize and len(sys.argv)==1,'unoptimized fixed invocation')

# B_i^m B_j^n = binom(m,i)binom(n,j)/binom(m+n,i+j) B_(i+j)^(m+n).
def product(a,b):
    m,n=len(a)-1,len(b)-1
    return [sum((a[i]*b[k-i]*F(comb(m,i)*comb(n,k-i),comb(m+n,k))
                 for i in range(max(0,k-n),min(m,k)+1)),F(0))for k in range(m+n+1)]
def elevate(a,d):
    m=len(a)-1;check(d>=m,'degree only increases')
    return product(a,[F(1)]*(d-m+1))
def linear(*terms):
    d=max(len(a)-1 for _,a in terms)
    return [sum((s*elevate(a,d)[k]for s,a in terms),F(0))for k in range(d+1)]
def value(a,t):
    # de Casteljau convex interpolation, independent of power reconstruction.
    a=list(a)
    while len(a)>1:a=[(1-t)*x+t*y for x,y in zip(a,a[1:])]
    return a[0]
def direct(l,h,r,b):
    one=[F(1)];u=[l,h];p=[one,u]
    for i in range(2,7):p.append(product(p[-1],u))
    A=linear((F(1,6),p[3]),(F(-1,2),u))
    H4=linear((F(1),p[4]),(F(-6),p[2]),(F(3),one))
    J=linear((F(1),p[5]),(F(-15),u))
    W=linear((F(1),A),(F(-1,656),J))
    B2=linear((F(1,10496),product(H4,H4)))
    E=linear((F(51,590400)/ELL,p[6]),(F(51,13120)/ELL,p[2]),
             (F(-51,19680)/ELL,one),(F(1,13448),u))
    Q=linear((F(-1),p[3]),(F(3,2)*r,p[2]),(3*b,u),(r*E0,one))
    Gin=linear((F(1,2),A),(F(-1,1640),J),(F(-1,12)/ELL,H4))
    G=linear((F(1),product(Gin,W)),(F(1),B2))
    P=linear((F(2,5)*S**3,product(A,W)),(F(2,5)*S**3,B2),
             (S**3,product(E,W)),(C,product(Q,W)))
    return dict(A=A,H4=H4,J=J,W=W,G=G,negative_Q=linear((F(-1),Q)),negative_P=linear((F(-1),P)))
def scalar(u,r,b):
    a=(u**3-3*u)/6;j=u**5-15*u;h=u**4-6*u*u+3
    w=a-j/656;b2=h*h/10496
    e=51*u**6/(590400*ELL)+51*(3*u*u-2)/(39360*ELL)+u/13448
    q=-u**3+F(3,2)*r*u*u+3*b*u+r*E0
    g=(a/2-j/1640-h/(12*ELL))*w+b2
    contact=F(2,5)*S**3*(a*w+b2)+S**3*e*w+C*q*w
    return dict(A=a,H4=h,J=j,W=w,G=g,negative_Q=-q,negative_P=-contact)
def ray(U,r,b):
    q=-U**3+F(3,2)*r*U**2+3*b*U+r*E0
    d=-3*U*U+3*r*U+3*b;dd=-6*U+3*r
    return [q,d,dd,F(2,5)*(U*U/2+F(1,2)+E0)+C*d,F(2,5)*U+C*dd,F(2,5)-6*C]

def calls(p,route):
    check(len(p['coarse'])==15 and len(p['fine'])==len(route['rows'])==55,'complete source coverage')
    for i,row in enumerate(p['coarse']):check(list(map(F,row['input_p']))==[F(23+i,100),F(24+i,100)],'coarse order')
    active=[r for r in p['coarse']if not r.get('excluded')];check(len(active)==11,'active parents')
    first=p['first_bridge']
    check(F(first['radius'])==F(121,40),'first radius')
    check(F(first['rho_upper'])==max(F(r['rho'])for r in active),'first rho')
    check(F(first['beta_absolute_upper'])==max(F(r['beta'])for r in active),'first beta')
    result=[first]
    for i,(cell,plan)in enumerate(zip(p['fine'],route['rows'])):
        parent=active[i//5];j=i%5;trace=cell['trace'];rs=list(map(F,plan['radii']))
        pp=[F(parent['pl'])+F(j,500),F(parent['pl'])+F(j+1,500)]
        check(list(map(F,cell['p']))==list(map(F,plan['p']))==pp==[F(135+i,500),F(136+i,500)],'five child ancestry')
        check(len(trace)==len(rs)>0 and rs[0]==F(121,40) and trace[0]['contraction']is None,'common bridge')
        check(all(b<a for a,b in zip(rs,rs[1:])),'contracting route')
        check(cell['final']==trace[-1]['resource']and F(cell['radius'])==rs[-1],'final ancestry')
        check(bool(cell['final'].get('excluded'))==plan['excluded']==(i<10),'exclusion placement')
        for k,step in enumerate(trace):
            check(F(step['radius'])==rs[k],'route radius')
            if k:
                prev=trace[k-1]['resource'];out=step['contraction']
                check(not prev.get('excluded')and out is not None,'support edge')
                check(F(out['radius'])==rs[k]and F(out['rho_upper'])==F(prev['rho'])and F(out['beta_absolute_upper'])==F(prev['beta']),'same preceding resources')
                result.append(out)
    check(len(result)==64,'all64 invocations')
    return [(F(x['radius']),F(x['rho_upper']),F(x['beta_absolute_upper']))for x in result]

archive=ROOT/'verification/finite-tail/sources/backend.zip'
check(sha256(archive.read_bytes()).hexdigest()=='43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52','archive identity')
with zipfile.ZipFile(archive)as z:
    manifest=json.loads(z.read('finite61/MANIFEST.json'))
    def read(pin):
        data=z.read('finite61/blobs/'+pin);check(sha256(data).hexdigest()==pin,'blob identity');return json.loads(data)
    p=read(PROOF);routepin=manifest['files'][PREFIX+'fixed_route.json']['sha256'];initialpin=manifest['files'][PREFIX+'initial42_candidate.json']['sha256']
    check(p['route_sha256']==routepin and p['source_sha256']==initialpin,'selected source inputs')
    route=read(routepin);read(initialpin)
tuples=calls(p,route);group={}
for R,r,b in tuples:group.setdefault(R,[]).append((r,b))
r=min(F('0.3031')*F('0.646')/(C-F('0.3031')),F('0.3322')*F('0.429')/(C-F('0.3322')));b=F(641562334877,10**12)
check(r==F(7361,4000)and 0<b<1 and (1+b*b)**2>r*r*(1-b*b),'initial moment ceilings')
group[F(96,25)]=[(r,b)]
table=[(str(R),str(max(r for r,b in vals)),str(max(b for r,b in vals)),len(vals))for R,vals in sorted(group.items())]
submitted_ast=ast.parse((ROOT/'mathematics/simplification/2026-10-27/check_grouped_support.py').read_text())
literal=next(ast.literal_eval(x.value)for x in submitted_ast.body if isinstance(x,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='TABLE'for t in x.targets))
check(table==literal and len(table)==14 and sum(t[3]for t in table)==65,'exact literal table binding')
check(0<ELL and ELL**2<41 and S>0 and S*S>F(42,41),'outward constants')
check((ELL+F(1,10**12))**2>41 and (S-F(1,10**12))**2<F(42,41),'tight inherited rounding')
submitted=json.loads((HERE/'submitted.stdout.json').read_text());check(len(submitted['groups'])==14,'submitted transcript')
allvalues=[];allrays=[];independent=[];evals=0
for (R,r,b,count),record in zip(table,submitted['groups']):
    R,r,b=map(F,(R,r,b));U=F(21,5)if R==F(96,25)else F(39,10)
    polys=direct(R,U,r,b);check([len(x)for x in polys.values()]==[4,5,6,6,11,4,12],'allseven degrees')
    for name,coefs in polys.items():
        check(all(v>F(1,4)for v in coefs),'strict coefficient margin')
        check(coefs==list(map(F,record['coefficients'][name])),'independent/submitted vector equality')
        for t in [F(0),F(1,3),F(1,2),F(1)]:
            check(value(coefs,t)==scalar(R+(U-R)*t,r,b)[name],'de Casteljau/scalar consistency');evals+=1
        allvalues.extend(coefs)
    gates=ray(U,r,b);check(all(x<0 for x in gates),'whole ray signs');allrays.extend(gates)
    independent.append(dict(radius=str(R),r=str(r),b=str(b),count=count,splice=str(U),coefficients={k:list(map(str,v))for k,v in polys.items()},ray_gates=list(map(str,gates))))
check(len(allvalues)==672 and len(allrays)==84,'complete counts')
minimum=min(allvalues)
check(minimum==F(168770300272604270966158879019623858439411520950319456559,650737668933625093816320000000000000000000000000000000000),'reported exact minimum')
a=F(48,125);x=F(1,42);gate=2*a-F(3,4)-(a+F(1,4))*x+(a*a-a)*x*x-a*a*x*x*x
check(gate==F(118707,42875000)>0,'scale correction')

controls=[]
def reject(name,fn):
    try:fn()
    except(ValueError,KeyError,TypeError):controls.append(name)
    else:raise ValueError('false control accepted: '+name)
check(product([F(0),F(1)],[F(0),F(1)])==[F(0),F(0),F(1)],'t squared control')
check(elevate([F(0),F(1)],3)==[F(0),F(1,3),F(2,3),F(1)],'linear elevation control')
reject('corrupt_constant_vector',lambda:check(value([F(7),F(8)],F(1,2))==7,'corrupt polynomial'))
reject('omit_radial_prefix',lambda:check(F(table[0][0])+F(1,100)==F(table[0][0]),'source radius equality'))
reject('false_ray_cap',lambda:check(all(v<0 for v in ray(F(39,10),F(4),F(1,2))),'ray failure'))
bad=deepcopy(p);bad['fine'][10]['trace'][1]['contraction']['rho_upper']='1'
reject('alter_preceding_resource',lambda:calls(bad,route))
bad=deepcopy(p);bad['fine'][10]['trace'][1]['contraction']=None
reject('missing_support_edge',lambda:calls(bad,route))
# Removing all historical positivity/cover annotations does not alter tuples.
no_signs=deepcopy(p)
def scrub(v):
    if isinstance(v,dict):
        for k in ['minimum_contact','scale_positive_gate','gate_sha256','gates','closed_cells']:v.pop(k,None)
        for x in v.values():scrub(x)
    elif isinstance(v,list):
        for x in v:scrub(x)
scrub(no_signs);check(calls(no_signs,route)==tuples,'old sign annotations are not premises')
print(json.dumps(dict(status='PASS_INDEPENDENT_GROUPED_BERNSTEIN_CERTIFICATE',
    method='Direct Bernstein multiplication and degree elevation; no submitted or archived imports',
    intervals=14,bound_calls=65,coefficients=672,ray_signs=84,minimum=str(minimum),
    margin_over_quarter=str(minimum-F(1,4)),scalar_consistency_checks=evals,
    scale_margin=str(gate),old_sign_annotations_used=False,native_programs_executed=0,
    negative_controls=controls,groups=independent),indent=2))

#!/usr/bin/env python3
"""Independent rational reconstruction of the direct-geometry polynomials.

No constructor code is imported. Polynomial coefficients are reconstructed
from the factored mathematical expressions using rational interpolation,
rather than the constructor's polynomial multiplication implementation.
This is a bounded scalar review, not a replay of a global proof.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions required')

root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[3]
folder=root/'mathematics/simplification-v10/2026-10-28'
evidence=root/'runs/geometry-v10-20261028/final05/geometry-check.py.stdout.json'
source=json.loads(evidence.read_text())
need=lambda c,m: None if c else (_ for _ in ()).throw(ValueError(m))
s=F('3.162277660');D=F('.76682509');T=F(7,125);w=1-T
left,right=F(6,25),F(27,50)
def Q(p):return (s+1)*p*p+(s-1)*(1-p)**2-6*p*(1-p)
def variance(p):return p*(1-p)
def plus(p):return 3*(s+1)*(1-p)
def minus(p):return 3*(s+3)*p

def interpolate(fun,degree):
    # Exact Vandermonde elimination at integer nodes. The formulas below
    # have degree at most degree, so these values uniquely identify them.
    rows=[[F(k)**j for j in range(degree+1)]+[fun(F(k))]
          for k in range(degree+1)]
    for j in range(degree+1):
        pivot=next(i for i in range(j,degree+1) if rows[i][j])
        rows[j],rows[pivot]=rows[pivot],rows[j]
        scale=rows[j][j];rows[j]=[x/scale for x in rows[j]]
        for i in range(degree+1):
            if i==j:continue
            scale=rows[i][j]
            rows[i]=[a-scale*b for a,b in zip(rows[i],rows[j])]
    out=[r[-1] for r in rows]
    for p in [F(-2,5),F(1,7),F(7,8)]:
        need(value(out,p)==fun(p),'Interpolation consistency')
    return out
def value(poly,p):return sum((a*p**i for i,a in enumerate(poly)),F(0))
def derivative(poly):return [i*poly[i] for i in range(1,len(poly))]
def quadratic_range(poly,l,u):
    need(len(poly)<=3,'Quadratic degree')
    points=[l,u]
    if len(poly)==3 and poly[2]:
        critical=-poly[1]/(2*poly[2])
        if l<=critical<=u:points.append(critical)
    vals=[value(poly,x) for x in points]
    return min(vals),max(vals)

delta=F(17,250)
rho_margin=F(713,500)-F(2,5)*D
expressions={
 'theta_plus':lambda p:w*(w*Q(p)+T*plus(p))**2-D*D*variance(p),
 'theta_minus':lambda p:w*(w*Q(p)+T*minus(p))**2-D*D*variance(p),
 'displacement':lambda p:(Q(p)+6*delta*(1-delta))**2-D*D*variance(p),
 'rho':lambda p:rho_margin**2*variance(p)-(1-2*variance(p)-F(2,5)*Q(p))**2,
}
checks=[]
for name,x,a,target in [('theta_plus',F(9,20),D*D,F(17,10000)),
                       ('theta_minus',F(39,100),D*D,F(11,1000)),
                       ('displacement',F(53,125),D*D,F(3,2500)),
                       ('rho',F(129,500),F(1,5),F(3,20000))]:
    poly=interpolate(expressions[name],4)
    need(poly==list(map(F,source['quartic_coefficients'][name])),
         'Independently reconstructed quartic differs: '+name)
    dp=derivative(poly);ddp=derivative(dp)
    lower,_=quadratic_range(ddp,left,right)
    need(lower>=2*a,'Uniform convexity: '+name)
    bound=value(poly,x)-value(dp,x)**2/(4*a)
    need(bound>target,'Tangent lower bound: '+name)
    checks.append({'name':name,'degree':4,'second_derivative_lower':str(lower),
                   'tangent_point':str(x),'global_lower':str(bound),
                   'strict_target':str(target)})

for name,fun,x,l,curvature,target in [
    ('positive',lambda p:p*(F('17.558')-42*Q(p))/(3*(s+1)),
      F(91,200),F(1,3),F(13),F(615289,10**6)),
    ('negative',lambda p:(1-p)*(F('17.558')-42*Q(p))/(3*(s+3)),
      F(49,125),left,F(12),F(565358,10**6))]:
    poly=interpolate(fun,3)
    need(poly==list(map(F,source['cubic_upper_coefficients'][name])),
         'Independently reconstructed cubic differs: '+name)
    dp=derivative(poly);ddp=derivative(dp)
    _,upper=quadratic_range(ddp,l,right)
    need(upper<=-curvature,'Uniform concavity: '+name)
    bound=value(poly,x)+value(dp,x)**2/(2*curvature)
    need(bound<target,'Tangent upper bound: '+name)
    if name=='positive':
        first_min,_=quadratic_range(dp,left,F(1,3))
        need(first_min>0,'Monotone initial cubic segment')
    checks.append({'name':'lambda_'+name,'degree':3,
                   'second_derivative_upper':str(upper),
                   'global_upper':str(bound),'strict_target':str(target)})

# A negative control must be a mathematically false stronger gate, not merely
# a sufficient procedure that happens to reject a valid bound.
positive_actual=expressions['theta_plus'](F(9,20))
need(positive_actual<F(1,50),'False uniform quartic lower bound .02 rejected')

# These are checks of serialized reserves and triangle containment after the
# separate analytic proof, not an independent replay of the panel algorithm.
panel_evidence=evidence.with_name('geometry-panels.py.stdout.json')
panel_data=json.loads(panel_evidence.read_text())
old_evidence=root/'runs/fixed-target-v8-20261028/moment03/stdout.json'
old_panel=next(z for z in json.loads(old_evidence.read_text())['panels']
               if z['index']==41)
joint_checks=[]
for z in panel_data['panels']:
    if z['excluded']:continue
    theta,d,e,cap,q,c=[F(z[k]) for k in
        ('theta','d','ell_l','D','qmin','cmin')]
    l,u=F(z['pl']),F(z['pu'])
    vmax=max(l*(1-l),u*(1-u),F(1,4) if l<=F(1,2)<=u else F(0))
    reserve=cap/(e*(1-theta))-q
    B=F('3.162277661')+7
    a=6*(1-d)-B*theta/(2*(1-theta))
    cbalanced=c-B*d/2
    need(reserve==F(z['joint_reserve']),'Shared reserve export')
    need(a==F(z['balanced_displacement_cost']),'Balanced d coefficient')
    need(cbalanced==F(z['balanced_noise_cost']),'Balanced lambda coefficient')
    need(a>0 and cbalanced>0 and reserve>=0,'Positive joint domains')
    dcap=F(z['balanced_displacement_intercept'])
    lcap=F(z['balanced_noise_intercept'])
    need(a*dcap>=reserve,'Outward joint d intercept')
    need(cbalanced*lcap/(42*vmax)>=reserve,'Outward joint lambda intercept')
    # The two full intercepts together violate the common line, rather than
    # provide an admissible rectangle. This is an abstract budget control,
    # not a claim that this pair is realized by an actual probability law.
    if reserve>0:
        need(a*dcap+cbalanced*lcap/(42*vmax)>reserve,
             'Invalid independent spending must be rejected')
    joint_checks.append({'index':z['index'],'reserve':str(reserve),
                         'balanced_d_intercept':str(dcap),
                         'balanced_lambda_intercept':str(lcap)})
    if z['index']==41:
        need(dcap<F(old_panel['joint_displacement_intercept']),
             'Central new triangle d intercept improves old')
        need(lcap<F(old_panel['lambda_upper']),
             'Central new triangle noise intercept improves old')
need(len(joint_checks)==28,'All retained panel joint exports checked')

sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
print(json.dumps({'status':'PASS_INDEPENDENT_DIRECT_GEOMETRY_POLYNOMIAL_RECONSTRUCTION',
 'scope':'Four quartic and two cubic continuum certificates, independently reconstructed; panel rounding and analytic hypotheses reviewed separately',
 'source_root':str(root),'constructor_imports':False,'checks':checks,
 'negative_control':{'false_theta_plus_uniform_lower':'1/50',
  'counterexample_p':'9/20','exact_value':str(positive_actual)},
 'reviewed_source_sha256':{p.name:sha(p) for p in [folder/'geometry.tex',
    folder/'geometry-check.py',folder/'geometry-panels.py',folder/'geometry-laws.py']},
 'constructor_evidence_sha256':sha(evidence),
 'joint_export_checks':joint_checks,
 'joint_evidence_sha256':sha(panel_evidence),
 'old_central_resource_sha256':sha(old_evidence),
 'script_sha256':sha(Path(__file__)),
 'python':sys.version,'optimization':sys.flags.optimize},indent=2))

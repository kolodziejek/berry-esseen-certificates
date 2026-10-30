from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json, hashlib, sys
root=Path('/Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/manuscript_revision_20261029/manuscript/compact-v16')
# Both sides are polynomials with degree at most two in p,a0,a1 and
# at most one in sigma. Equality on this tensor grid therefore verifies
# the coefficient identity exactly by univariate interpolation in turn.
checks=0
for p,a0,a1,sigma in product((F(0),F(1,3),F(1)),repeat=4):
 q=1-p;Aminus=p-a0;Aplus=q-a1;d=a0+a1
 lhs=(sigma+1)*p*p+(sigma-1)*q*q+6*Aminus*p+6*Aplus*q-6*(Aminus*Aminus+Aminus*Aplus+Aplus*Aplus)
 Q=(sigma+1)*p*p+(sigma-1)*q*q-6*p*q
 rhs=Q+6*(d*(1-d)+a0*a1)
 assert lhs==rhs;checks+=1
# Exact finite-law checks before standardizing. J/h is invariant under
# scaling; each zero-bias gap mass equals tail*gap/variance.
cases=[('two_point',[(-1,F(1,2)),(1,F(1,2))],F(2)),('atom_zero',[(-1,F(1,4)),(0,F(1,2)),(1,F(1,4))],F(1)),('missing_site',[(0,F(1,3)),(1,F(1,3)),(3,F(1,3))],F(1))]
rows=[]
for name,raw,span in cases:
 mean=sum(F(x)*p for x,p in raw);law=[(F(x)-mean,p) for x,p in raw]
 variance=sum(x*x*p for x,p in law)
 def gapdata(points):
  weights=[];ratio=F(0)
  for (left,_),(right,_) in zip(points,points[1:]):
   tail=sum(x*p for x,p in points if x>=right);gap=right-left
   assert gap/span>=1 and (gap/span).denominator==1
   mass=tail*gap/variance;weights.append(mass);ratio+=mass*gap/span
  return weights,ratio
 weights,ratio=gapdata(law)
 assert sum(weights)==1 and ratio>=1
 reflected=sorted([(-x,p) for x,p in law]);rw,rr=gapdata(reflected)
 assert rr==ratio and sum(rw)==1
 rows.append(dict(law=name,zero_bias_weights=list(map(str,weights)),J_over_h=str(ratio),reflection_preserves_J=True))
# Newly explained coupled d correction is positive on the stated domain.
sigma_hi=F(3162277661,10**9)
margin=6*F(994,1000)*(1-F(4,1000))-F(6,1000)*(sigma_hi+7)
assert margin>0
# Uniform-threshold bound is an analytic implication recorded in review.
result=dict(status='PASS_INDEPENDENT_GEOMETRY_LOCAL_CHECKS',mathematical_scope='Polynomial budget identity and finite lattice diagnostics; full lattice/unbounded and conservation proofs are in independent review.',execution_scope='Exact fractions; tensor interpolation verifies the polynomial identity, while finite-law examples are diagnostics only.',polynomial_grid_checks=checks,lattice_cases=rows,coupled_displacement_margin=str(margin),python=sys.version,source_hashes={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ('sections/03-conservation.tex','sections/05-geometry-counts.tex','sections/07-direct-acquisition.tex')})
print(json.dumps(result,indent=2))

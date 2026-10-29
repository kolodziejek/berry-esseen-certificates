#!/usr/bin/env python3
"""Independent tensor-polynomial and final-margin check; no producer imports."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions must remain enabled')
root = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[3]
source = root/'mathematics/simplification-v10/2026-10-28'
A, alpha, U, N = F(3,5), F(9,20), F(1,500), F(42)
den=5*alpha**4; tmax=F(89,84)*U

def polynomial(sign, b, target):
    # Expand the shifted fourth-moment bound divided by t, after r=z*t.
    # Keys are powers of (z,t). This is the original quartic, not the
    # producer's lower quadratic with z^4 replaced by zmax^2*z^2.
    return {(0,0):(3*alpha**2-A**2)/den-target,
            (0,1):-3/den,(1,0):2*sign/(5*alpha)+b,
            (1,1):-4*A/den,(2,1):3*alpha**2/den,
            (2,2):-6/den,(4,3):-1/den}

def tensor_coefficients(poly,zmax):
    result=[]
    for k in range(5):
        for l in range(4):
            result.append(sum((c*zmax**i*tmax**j*F(comb(k,i),comb(4,i))*F(comb(l,j),comb(3,j))
                               for (i,j),c in poly.items() if i<=k and j<=l),F(0)))
    return result

rectangles=[]
for sign,b,c,zmax in [(1,F(-21,20),F(4,5),F(2)),(-1,F(19,20),F(1),F(3,2))]:
    coeff=tensor_coefficients(polynomial(sign,b,c),zmax)
    assert min(coeff)>0
    rectangles.append({'sigma':sign,'b':str(b),'target':str(c),'zmax':str(zmax),
                       'coefficient_count':len(coeff),'minimum':str(min(coeff))})

# Independently grouped scalar proof of the tail and final comparisons.
z3=1+F(1,8)+F(1,27)+F(1,18)
z2=1+F(1,4)+F(1,9)+F(1,3)
assert z3<F(49,40) and z2<F(17,10)
def tail(V): return A*A*V*F(49,40)+3*V*V*U*F(17,10)
inner=F(1,20)
inner_bracket=F(4,5)*F(79,84)-F(53,50)*tail(F(9,8))/(1-inner)**4
inner_margin=F(73,100)*inner_bracket-F(2,42)-F(1,100)
assert inner_bracket>0 and inner_margin>0

Tglobal=F(11,10)*U
negative_own=min(x*x/(Tglobal+x*x)-F(5,4)*x for x in [inner,F(34,125)])
assert 3*inner*inner>Tglobal and negative_own>F(469,1000)
negative_bracket=negative_own-F(3,2)*tail(F(7,6))*U
negative_margin=F(13,20)*negative_bracket-(F(3,42)+F(1,100))*U
assert negative_bracket>0 and negative_margin>0

G=min(x*(1-x)**4 for x in [inner,F(91,125)])
positive_bracket=F(4,5)*G-F(3,2)*tail(F(7,6))*U
positive_margin=F(13,20)*positive_bracket-(F(3,42)+F(1,100))*U
assert positive_bracket>0 and positive_margin>0

# The remaining negative-inner portion: only endpoints can minimize after
# the switch because the derivative is first increasing, then decreasing.
z=F(2); hf=F(21,20); c=F(4,5)
switch=z*z/(1+z*z*tmax)-hf*z-c
slope=2*z/(1+z*z*tmax)**2-hf
end=inner*inner/(tmax+inner*inner)-hf*inner-c*tmax
assert min(switch,slope,end,inner-z*tmax)>0
assert F(19,20)*F(3,2)>1 and F(3,2)*tmax<inner

# Two genuine false-bound controls, independently of the sufficient format.
bad=polynomial(1,F(-21,20),F(11,10))
false_endpoint=sum((c*2**i*tmax**j for (i,j),c in bad.items()),F(0))
assert false_endpoint<0
y=F(4,3)
assert (-y**4+3*y*y+2*y)/4>1

sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
print(json.dumps({
  'status':'PASS_INDEPENDENT_SMALL_NOISE_POLYNOMIAL_AND_MARGIN_REVIEW',
  'scope':'Independent 40-coefficient tensor proof of the two quartic rectangles, exact final margins and switch gates; analytic normalization/tail review separately documented',
  'constructor_imports':False,'quartic_rectangles':rectangles,
  'inner_margin_above_1_over_100':str(inner_margin),
  'outer_negative_margin_at_upper_noise':str(negative_margin),
  'outer_positive_margin_at_upper_noise':str(positive_margin),
  'negative_controls':['The stronger own-count constant11/10 is false at the negative rectangle endpoint','The quartic denominator4 is not an indicator minorant at x/alpha=4/3'],
  'reviewed_source_pins':{name:sha(source/name) for name in ['small-noise.tex','small_noise_check.py']},
  'reviewer_script_sha256':sha(Path(__file__)),'python':sys.version,
},indent=2))

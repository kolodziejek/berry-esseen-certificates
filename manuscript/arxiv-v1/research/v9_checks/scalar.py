"""Independent rational checks for the manuscript's two cosine majorants.

No constructor imports and no transcendental numerical oracle. The proof that
these coefficients imply the displayed continuous bounds is in the manuscript.
"""
from fractions import Fraction as F
from math import comb, factorial
import json, sys
if not __debug__:
    raise RuntimeError("Optimized Python is not an acceptance configuration")

PI_L=F('3.141592653589793')
PI_U=F('3.141592653589794')

def atan_bounds(x,terms):
    value=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    next_value=value+(-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(value,next_value),max(value,next_value)
a0,a1=atan_bounds(F(1,5),32)
b0,b1=atan_bounds(F(1,239),12)
assert PI_L<16*a0-4*b1 and 16*a1-4*b0<PI_U

def bernstein_cosine(K,terms,cells):
    degree=2*terms-1
    power=[F(0)]*(degree+1)
    power[0]=K
    for j in range(1,terms+1):
        direction=PI_U if j%2 else PI_L
        power[2*j-1]=-(-1)**(j+1)*(2*direction)**(2*j)/factorial(2*j)
    width=(2/K)/cells
    coeffs=[]
    for panel in range(cells):
        left=panel*width
        local=[width**i*sum((power[h]*comb(h,i)*left**(h-i)
                              for h in range(i,degree+1)),F(0))
               for i in range(degree+1)]
        coeffs.extend(sum((local[i]*F(comb(k,i),comb(degree,i))
                           for i in range(k+1)),F(0))
                      for k in range(degree+1))
    assert all(x>0 for x in coeffs)
    if K==F(23,5): assert min(coeffs)>F(4492,100000)
    if K==F(4553,1000): assert min(coeffs)>F(123,10**6)
    # Taylor-tail magnitudes decrease from the first retained positive term.
    assert (2*PI_U*(2/K))**2 < 12
    return {'K':str(K),'terms':terms,'closed_cells':cells,
            'positive_coefficients':len(coeffs),'minimum':str(min(coeffs)),
            'minimum_decimal_diagnostic':float(min(coeffs))}

report={'mathematical_scope':'Finite coefficients for the stated alternating-Taylor/Bernstein majorants only',
        'cases':[bernstein_cosine(F(23,5),5,8),
                 bernstein_cosine(F(4553,1000),7,64)]}
try:
    bernstein_cosine(F(9,2),5,8)
except AssertionError:
    report['negative_control']='Rejected the false K=4.5 majorant'
else:
    raise RuntimeError('False majorant was accepted')
report['python']=sys.version
report['passed']=True
print(json.dumps(report,indent=2))

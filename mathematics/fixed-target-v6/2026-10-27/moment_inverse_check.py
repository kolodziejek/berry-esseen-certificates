#!/usr/bin/env python3
"""Exact inverse-branch boundary controls; no Fourier function is called."""
from fractions import Fraction as F
from math import isqrt
import json
import moment_check as m
m.need(m.SIGMALO*m.SIGMALO<10,'strict sigma lower bound')
rows=[]
for t in (F(0),F(1,10),F(1,3),F(3,4),F(1),F(3,2),F(2),F(3),F(10),F(100)):
    y=(1-t*t)/(1+t*t);z=2*t/(1+t*t);a=y+3*z
    m.need(y*y+z*z==1 and z>=0 and -1<=a<=m.SIGMALO,'rational circle parameter')
    lo=m.normalized_lower(a)
    m.need(lo<=y,'inverse lower bound preserves exact circle point')
    rows.append(dict(t=str(t),y=str(y),a=str(a),inverse_lower=str(lo)))
# Exact increasing-branch point y=-5/13,z=12/13,a=31/13 has
# sqrt(10-a²)=27/13. A lower-rounded root makes the claimed gamma
# lower bound too large, excluding this valid boundary point.
a=F(31,13);x=10-a*a;scale=10**12;k=isqrt(x.numerator*scale**2//x.denominator)
wrong=(a-3*F(k,scale))/10;correct=m.normalized_lower(a)
m.need(correct<F(-5,13)<wrong,'reversed root-rounding control')
print(json.dumps(dict(name='MOMENT_INVERSE_EXACT_BOUNDARY_CONTROLS_V1',points=rows,
 rounding_control=dict(valid_y=str(F(-5,13)),correct_lower=str(correct),wrong_lower=str(wrong)),
 no_fourier_calls=True),indent=2))

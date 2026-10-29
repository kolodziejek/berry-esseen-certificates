#!/usr/bin/env python3
"""Per-cell support from all explicit contact/heat and whole-ray gates.
The v5 proof establishes the implication; no numerical Fourier premise.
"""
from fractions import Fraction as F
from math import isqrt
import json,sys
if not __debug__ or sys.flags.optimize:raise ValueError('no optimized Python')
def sqrt_up(x):
    scale=10**8;k=isqrt(x.numerator*scale**2//x.denominator)
    a,b=F(k,scale),F(k+1,scale)
    if not a*a<=x<=b*b:raise ValueError('root enclosure')
    return b
def support(R,r,b):
    S,c,e=F(81,80),F(819,2000),F(8,875)
    A=(R**3-3*R)/6;h4=R**4-6*R**2+3
    E=R**5/4100+3*R/820+17*(3*R**2-2)/78720
    Q=-R**3+3*r*R**2/2+3*b*R+e*r
    Q1=-3*R**2+3*r*R+3*b;Q2=-6*R+3*r
    L=F(2,5)*(R**2/2+F(1,2)+e)+c*Q1
    L1=F(2,5)*R+c*Q2;L2=F(2,5)-6*c
    P=F(2,5)*S**3*(A*A+h4*h4/(256*41))+S**3*E*A+c*Q*A
    out=dict(A=A,h4=h4,Q=Q,Q1=Q1,Q2=Q2,L=L,L1=L1,L2=L2,P=P)
    good=R>=F(5,2) and A>0 and 0<h4<36*A and all(out[k]<0 for k in ('Q','Q1','Q2','L','L1','L2','P'))
    return good,out

def cell_radius(rho_upper):
    b=sqrt_up((rho_upper*sqrt_up(rho_upper*rho_upper+8)-rho_upper*rho_upper-2)/2)
    for j in range(250,385):
        R=F(j,100);ok,gates=support(R,rho_upper,b)
        if ok:return R,b,gates
    raise ValueError('no licensed cell support radius')

#!/usr/bin/env python3
"""175 tiny rational support-envelope probes, no Fourier or native imports."""
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
rows=[]
for i in range(19,24):
    l=1+F(3361*i,96000);u=1+F(3361*(i+1),96000)
    beta=sqrt_up((u*sqrt_up(u*u+8)-u*u-2)/2)
    candidates=[]
    for j in range(350,385):
        R=F(j,100);good,values=support(R,u,beta)
        candidates.append((R,good,values))
    chosen=next((x for x in candidates if x[1]),None)
    if chosen is None:raise ValueError('no tested radius passed')
    rows.append(dict(index=i,rho_lower=str(l),rho_upper=str(u),beta_upper=str(beta),
      tested=35,radius=str(chosen[0]),gates={k:str(v) for k,v in chosen[2].items()},
      first_failed=[str(x[0]) for x in candidates if not x[1]],
      caveat='First passing centigrid point in [3.50,3.84], not a globally minimal support radius.'))
good,values=support(F(3),F(7361,4000),rows and F(rows[-1]['beta_upper']))
if good or values['P']<=0:raise ValueError('too-small radius rejection failed')
print(json.dumps(dict(name='FIVE_HIGH_RHO_SUPPORT_ENVELOPE_PROBES_V1',
 scope='Conditional support-radius potential from fixed-target contact and fourth-order heat bound; no new Fourier or acquisition cover.',
 source_formula='Companion entry.tex:128-155; reproduced rational algebra without importing its code.',
 rows=rows,rejected_radius3_P=str(values['P'])),indent=2))

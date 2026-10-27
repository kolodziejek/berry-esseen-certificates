#!/usr/bin/env python3
"""Bounded, independent rational checks for entry.tex; no inherited imports.

The analytic Taylor/heat/contact claims are not proved by this program.
It checks their stated rational reductions and exact finite-law identities.
"""
from fractions import Fraction as F
import json


def arctan_sum(x, terms):
    return sum(((-1)**j * x**(2*j+1) / (2*j+1)
                for j in range(terms)), F(0))


def support(u, r=F(1841,1000), b=F(321,500)):
    S, c, e = F(81,80), F(819,2000), F(8,875)
    A = (u**3-3*u)/6
    h4 = u**4-6*u**2+3
    E = u**5/4100+3*u/820+17*(3*u**2-2)/78720
    q = -u**3+3*r*u**2/2+3*b*u+e*r
    q1 = -3*u**2+3*r*u+3*b
    q2 = -6*u+3*r
    L = F(2,5)*(u**2/2+F(1,2)+e)+c*q1
    L1 = F(2,5)*u+c*q2
    L2 = F(2,5)-6*c
    P = F(2,5)*S**3*(A**2+h4**2/(256*41))+S**3*E*A+c*q*A
    return dict(A=A,h4=h4,Q=q,Q1=q1,Q2=q2,L=L,L1=L1,L2=L2,P=P)


def check_law(name, atoms):
    moment = lambda power: sum(p*x**power for x,p in atoms)
    absolute = lambda power: sum(p*abs(x)**power for x,p in atoms)
    assert sum(p for x,p in atoms)==1 and moment(1)==0 and moment(2)==1
    rho,beta,gamma = absolute(3),sum(p*x*abs(x) for x,p in atoms),moment(3)
    assert (1+beta**2)**2 <= rho**2*(1-beta**2)
    weights=[(abs(x),p*(abs(x)-1)**2*(abs(x)+F(1,2))) for x,p in atoms]
    assert sum(p for x,p in weights)==rho-1
    assert sum(p*(x+1)**2/(x+F(1,2)) for x,p in weights)==moment(4)-1
    assert sum(p*(x**3+2*x**2+3*x+F(3,2))/(x+F(1,2))
               for x,p in weights)==absolute(5)-1
    R=max(abs(x) for x,p in atoms)
    k4=(R+1)**2/(R+F(1,2))
    k5=(R**3+2*R**2+3*R+F(3,2))/(R+F(1,2))
    assert moment(4)<=min(R*rho,1+k4*(rho-1))
    assert absolute(5)<=min(R*moment(4),1+k5*(rho-1))
    assert moment(6)<=R*absolute(5)
    assert gamma**2<=moment(4)-1
    return dict(name=name,rho=str(rho),beta=str(beta),gamma=str(gamma),
                initial_moment_domain=(rho<F(7361,4000)))


def main():
    pi_low=16*arctan_sum(F(1,5),6)-4*arctan_sum(F(1,239),1)
    pi_high=16*arctan_sum(F(1,5),5)-4*arctan_sum(F(1,239),2)
    sr_low,sr_high=F(3162277660,10**9),F(3162277661,10**9)
    assert sr_low**2<10<sr_high**2
    assert F(819,2000)**2<(19+6*sr_low)/(72*pi_high)
    assert (19+6*sr_high)/(72*pi_low)<F(20487,50000)**2
    assert pi_low>F(160,51) and pi_low>F(25,8) and pi_high<F(22,7)
    assert F(997,2500)**2<F(7,44)
    bound3031=F(3031,10000)*F(323,500)/(F(819,2000)-F(3031,10000))
    bound3322=F(1661,5000)*F(429,1000)/(F(819,2000)-F(1661,5000))
    assert bound3031==F(7361,4000)<F(1841,1000)<bound3322
    r,b=F(1841,1000),F(321,500)
    assert (1+b*b)**2-r*r*(1-b*b)==F(93288849,50000000000)>0
    S=F(81,80)
    assert F(42,41)<S*S
    assert S*S*(2*S+1)/(2*(S+1)**2)==F(793881,2073680)<F(48,125)
    values=support(F(96,25))
    assert values['A']>0 and 0<values['h4']<36*values['A']
    assert all(values[k]<0 for k in ['Q','Q1','Q2','L','L1','L2'])
    assert -values['P']==F(2214258283536204102723,10250000000000000000000)>F(1,5)
    # A too-small radius is rejected by this same envelope, not accepted by fiat.
    assert support(F(3))['P']>0
    # The rho-sensitive license is algebraically stronger than the old floor.
    l,N,c,T=F(9,5),42,F(819,2000),F(18)
    assert T>F(2,5)*N and T<N*c*l
    density=1-T/(N*c*l)
    assert density==F(7199,17199)>F(209,500)
    assert F(60)/(42*F(997,2500))==F(25000,6979)
    laws=[]
    laws.append(check_law('symmetric Bernoulli',[(F(-1),F(1,2)),(F(1),F(1,2))]))
    for a in [F(3,2),F(2,3)]:
        laws.append(check_law('skew Bernoulli '+str(a),[
            (-a,1/(1+a*a)),(1/a,a*a/(1+a*a))]))
    laws.append(check_law('three-point zero atom',[
        (F(-2),F(1,8)),(F(0),F(3,4)),(F(2),F(1,8))]))
    laws.append(check_law('tiny distant atoms (outside entry moment domain)',[
        (F(-20),F(1,800)),(F(0),F(399,400)),(F(20),F(1,800))]))
    print(json.dumps(dict(status='PASS_BOUNDED_ENTRY_RATIONAL_CHECKS',
        structural_bounds={'3031':str(bound3031),'3322':str(bound3322)},
        support={k:str(v) for k,v in values.items()},
        rejected_radius3_P=str(support(F(3))['P']),
        illustrative_license_density=str(density),laws=laws,
        limitations=['No certificate/backend imports or native runs.',
                     'No claim of a raw numerical cover or local exclusion.',
                     'Exact arithmetic does not prove analytic premises.']),indent=2))


if __name__=='__main__':
    main()

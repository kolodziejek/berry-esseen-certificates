#!/usr/bin/env python3
"""Independent rational diagnostics for the full-phase lemma; no source imports."""
from fractions import Fraction as Q
import json


def poly(A,F,q,b,N):
    return [A,F,-q+(A-N*b)/(2*N),F/(2*N),
            -q/(2*N)+(A-N*b)/(8*N*N),F/(8*N*N),-q/(8*N*N)]


def value(p,h):
    return sum(a*h**j for j,a in enumerate(p))


def derivative(p):
    return [j*a for j,a in enumerate(p)][1:]


def main():
    checked=0
    for N in [Q(1),Q(2),Q(42),Q(100)]:
        for q in [Q(1,10),Q(1),Q(3)]:
            for F in [Q(0),Q(1,5),Q(1),Q(3)]:
                A=Q(1)
                b=(A+F*F/(4*q)+Q(1))/N  # strict raw gate holds globally
                z=F*F/(8*q*q*N)
                if z+z*z>=1: continue
                p=poly(A,F,q,b,N);p1=derivative(p);p2=derivative(p1)
                assert value(p1,0)==F
                for j in range(81):
                    h=Q(j,10)
                    r=A+F*h-q*h*h
                    v=h*h/(2*N)+h**4/(8*N*N)
                    vp=h/N+h**3/(2*N*N);vpp=1/N+3*h*h/(2*N*N)
                    assert value(p,h)==r+(r-N*b)*v
                    assert value(p2,h)==-2*q*(1+v)+2*(F-2*q*h)*vp+(r-N*b)*vpp
                    assert value(p2,h)<0
                    checked+=1
    # No global concavity conclusion without a condition: raw gate alone fails.
    A,F,q,b,N=Q(0),Q(20),Q(1),Q(101),Q(1)
    assert A+F*F/(4*q)<N*b
    assert value(derivative(derivative(poly(A,F,q,b,N))),Q(5))==Q(663,4)>0
    # The F=0 maximum is attained at h=0; its VALUE need not be zero.
    p=poly(Q(1),Q(0),Q(1),Q(2),Q(1))
    assert value(p,0)==1
    # Discarding the infinite endpoint without positive part is false on
    # negative values. For h=2,N=2,r=0,b=1 and y=exp(1/2)>1,
    # f(1/4)-f(1/2)=2(y-1)^2>0, verified as an exact polynomial identity.
    for y in [Q(3,2),Q(2),Q(5)]:
        assert (4-4*y)-(2-2*y*y)==2*(y-1)**2>0
    print(json.dumps({'status':'PASS_INDEPENDENT_PHASE_POLYNOMIAL_CHECKS',
        'rational_parameter_threshold_cases':checked,'negative_controls':3,
        'scope':'Only polynomial identities and bounded diagnostics. Integral derivative argument, continuum concavity proof and numerical24cell acceptance are separate.'},indent=2))


if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Independent bounded diagnostics; imports neither constructor nor backend.

Continuum and unbounded-integer arguments are in independent-review.md.
"""
from fractions import Fraction as Q
from math import comb
import json


def positive(x):
    return max(Q(0),x)


def prices(chi,c,u):
    return positive(chi-1)/(c-u)**2,positive(chi)/(c+min(u,c/3))**2


def phase(b,c,u):
    return max(prices(b+u,c,u))


def bound(b,c,l,h):
    # Derive the two branch suprema separately (constructor takes g candidates).
    first=positive(b+h-1)/(c-h)**2
    second=max(positive(b+l)/(c+min(l,c/3))**2,
               positive(b+h)/(c+min(h,c/3))**2)
    critical=c-2*b
    if c>b and l<=critical<=min(h,c/3):
        second=max(second,1/(4*(c-b)))
    return max(first,second)


def main():
    integer_count=0
    for c in [Q(51,100),Q(3,5),Q(3,4),Q(1)]:
        for u in sorted({Q(-1,2),Q(-49,100),Q(0),c/3,Q(1,2)}):
            d=2*c-Q(1,2)
            for chi in [Q(-2),Q(0),Q(1,5),Q(99,100),Q(1),Q(3,2),Q(199,100)]:
                m=max(prices(chi,c,u))
                for r in range(1,17):
                    V=-(c*r-u)
                    assert positive(chi-1)*r<=m*V*V
                    assert (c*r-u)**2-r*(c-u)**2==(r-1)*(c*c*r-u*u)
                    integer_count+=1
                for h in range(2,17):
                    V=c*(h-1)+u+Q(1,10000)  # strict closed-CDF crossing
                    assert positive(chi)*comb(h,2)<=m*V*V
                    if h>=3:
                        assert V>d
                        assert comb(h,3)<=V**3/d**3<=V**4/d**4
                    integer_count+=1
    discrete_count=0
    for n in range(1,11):
        for pn in range(1,10):
            p=Q(pn,10);q=1-p;v=p*q
            mass=[Q(comb(n,j))*p**j*q**(n-j) for j in range(n+1)]
            cdf=[sum(mass[:j+1]) for j in range(n+1)]
            F=lambda j:Q(0) if j<0 else Q(1) if j>n else cdf[j]
            for k in range(n+1):
                chi=(n+1)*p-k
                if chi>=2:
                    continue
                for r in range(-16,17):
                    rp,rm=max(r,0),max(-r,0)
                    b2=comb(rm,2) if rm>=2 else 0
                    b3=comb(rm,3) if rm>=3 else 0
                    rhs=max(mass)/((n+1)*v)*(positive(chi-1)*rp+positive(chi)*b2+b3)
                    assert F(k+r)-F(k)-r*mass[k]<=rhs
                    discrete_count+=1
    phase_count=0
    points=[Q(-1,2),Q(-1,10),Q(0),Q(1,5),Q(1,2)]
    for c in [Q(51,100),Q(3,5),Q(3,4),Q(1)]:
        for b in [Q(-2),Q(-1,10),Q(0),Q(3,10),Q(4,5),Q(1),Q(3,2),Q(2)]:
            for l in points:
                for h in [z for z in points if z>=l]:
                    B=bound(b,c,l,h)
                    critical=c-2*b
                    candidates=[l,h]+([critical] if c>b and l<=critical<=min(h,c/3) else [])
                    assert any(phase(b,c,x)==B for x in candidates)
                    for j in range(81):
                        assert phase(b,c,l+(h-l)*Q(j,80))<=B
                        phase_count+=1
    # Negative controls: replacing maximum by minimum is unsound.
    chi,c,u,V=Q(6,5),Q(3,4),Q(1,10),Q(9,10)
    assert V>c+u
    assert min(prices(chi,c,u))*V*V<chi<=max(prices(chi,c,u))*V*V
    # Independent centered rare-atom variable needs its individual fourth moment.
    t=Q(1,100);fourth=Q(1,100)
    assert fourth>3*t*t
    # Inverse-index upper substitution must clamp a possibly negative constant.
    h0,N,n=Q(-1),42,43
    assert h0/n>h0/N and h0/n<=max(h0,0)/N
    print(json.dumps({'status':'PASS_INDEPENDENT_BOUNDED_COUNT_CHECKS',
        'integer_crossing_cases':integer_count,'discrete_binomial_cases':discrete_count,
        'phase_grid_diagnostics':phase_count,'negative_controls':3,
        'scope':'Exact bounded diagnostics, independent of constructor implementation. Continuous and all-integer results require the written derivation; no LOW acceptance.'},indent=2))


if __name__=='__main__':
    main()

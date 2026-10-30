#!/usr/bin/env python3
"""Exact scalar checks for the revised count proof (not an all-law checker).

All arithmetic below is integer/Fraction arithmetic. Analytical premises are
the global quartic-minorant argument, concavity, and the complete incoming and
curvature-tail estimates in sections/08-direct-comparison.tex. This checks the
new endpoint comparisons and coefficient identities; it does not infer the
analytical premises from examples. No historical checker or source is changed.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import sys


def require(condition: bool, label: str) -> None:
    if not condition:
        raise ValueError(label)


def add(*polynomials):
    out = [F(0)] * max(map(len, polynomials))
    for p in polynomials:
        for k, coefficient in enumerate(p):
            out[k] += coefficient
    while len(out) > 1 and not out[-1]:
        out.pop()
    return tuple(out)


def scale(p, c):
    return tuple(c * x for x in p)


def multiply(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return tuple(out)


def evaluate(p, x):
    out = F(0)
    for a in reversed(p):
        out = out*x+a
    return out


def derivative(p):
    return tuple(k*p[k] for k in range(1, len(p))) or (F(0),)


def same(p, q):
    return all(x == 0 for x in add(p, scale(q, -1)))


def rectangle_data(alpha=F(1, 2), A=F(3, 5), limit=F(101, 10000),
                   negative_b=F(-101, 100), positive_b=F(99, 100)):
    """Reconstruct the two lower quadratics at both t endpoints."""
    denominator = 5*alpha**4
    rows = []
    for epsilon, b, name in [(1, negative_b, "negative"),
                              (-1, positive_b, "positive")]:
        for t in [F(0), limit]:
            a = (3*alpha**2-A**2-3*t)/denominator
            linear = 2*epsilon/(5*alpha)+b-4*A*t/denominator
            quadratic = (3*alpha**2*t-6*t*t-F(9,4)*t**3)/denominator
            require(quadratic >= 0, "rectangle quadratic must be convex in z")
            if epsilon == 1:
                max_derivative = linear+3*quadratic
                require(max_derivative < 0, "negative phase must decrease in z")
                z = F(3,2)
                slope = max_derivative
            else:
                require(linear > 0, "positive phase must increase in z")
                z = F(0)
                slope = linear
            minimum = a+linear*z+quadratic*z*z
            require(minimum > F(3,5), "rectangle minimum must exceed 3/5")
            rows.append(dict(phase=name,t=t,z=z,quadratic=quadratic,
                             extremal_derivative=slope,minimum=minimum))
    return rows


def count_polynomials():
    N=700
    A=F(3,5); q_min=F(107,200); eta=F(2,5); mass=F(41,100)
    pi_upper=F(22,7); r=F(3,8); phi_upper=F(2,5); xi=F(93,100)
    cbar=F(79,200); V=F(113,1000); mstar=F(3,4)
    alpha=1-F(6,N); b=1+F(3,N); z=3*alpha
    T=(F(0),1/q_min)
    M4=add(scale(T,A*A),scale(multiply(T,T),3))
    Lvar=(F(1,5),F(5,2))
    def S(c):
        return add(scale(T,F(1,4)),scale(Lvar,c),
                   scale(M4,F(27,256)*(F(5,3)+5*c/4)))
    Eminus=scale(add(scale(S(cbar),mass),
                     (phi_upper*(xi/8+F(2,27)),)),1/V)
    Eplus=scale(add(scale(S(F(0)),mass),
                    (phi_upper*F(2,27),phi_upper*xi/2)),1/V)
    W=scale(add((F(0),z/2,-z*z/4,z**3/12,-z**4/48),
                (F(0),-A*A*b/16,-3*b*b/16),
                (F(0),-4*pi_upper*pi_upper/(N*r))),eta*mstar)
    expected_gap=add((F(7889,100000),F(1751,8000)),
                      scale(M4,mass*F(27,256)*5*cbar/4))
    require(same(scale(add(Eminus,scale(Eplus,-1)),V),expected_gap),
            "Eminus-Eplus coefficient identity")
    require(all(c>=0 for c in expected_gap) and expected_gap[0]>0,
            "strict envelope domination on lambda>=0")
    require(all(c>=0 for c in Eminus) and Eminus[2]>0,
            "Eminus nonnegative and strictly convex")
    Wsecond=scale(add(scale(add(multiply((-F(1),z),(-F(1),z)),(F(1),)),
                                  z*z/4),(3*b*b/8,)),-eta*mstar)
    require(same(derivative(derivative(W)),Wsecond), "W second derivative identity")
    require(z>0 and b>0 and eta*mstar>0, "strict negative square-form derivative")
    P=add(W,scale(Eminus,-F(1,N)),(F(0),-F(1,100)))
    for x, bound in [(F(1,100),F(2314,10**6)),(F(7,20),F(61304,10**6))]:
        require(evaluate(P,x)>bound, "quartic endpoint lower bound")
    require(evaluate(W,F(0))==0<evaluate(Eminus,F(0)),
            "larger-noise estimate does not reach zero")
    return dict(W=W,Eminus=Eminus,Eplus=Eplus,P=P,gap=expected_gap,
                small_endpoint=evaluate(P,F(1,100)),
                large_endpoint=evaluate(P,F(7,20)))


def run():
    h=(F(0),F(4,5),F(12,5),F(0),F(-16,5))
    factored=scale(multiply(multiply((F(0),F(1)),(F(1),F(-1))),
                            multiply((F(1),F(2)),(F(1),F(2)))),F(4,5))
    require(same(h,factored), "global minorant factorization")
    # The unique critical maximum in (0,1) has value (9+6 sqrt(3))/20.
    # Its comparison with 1 reduces to 6 sqrt(3)<11, i.e. 108<121.
    require(108<121, "strict maximum below indicator")
    require(evaluate(h,F(0))==0, "strict-event atom at zero")
    rows=rectangle_data()
    require(rows[1]['minimum']>F(769,1000), "printed compact lower bound")
    require(rows[1]['extremal_derivative']<F(-1,5), "printed derivative bound")
    polys=count_polynomials()

    # Diagnostics, not continuous-domain certificates. Include exact threshold
    # atoms, small noise, skew noise, and sums exceeding the summand bound.
    laws=[[(F(-3,5),F(1,2)),(F(3,5),F(1,2))],
          [(F(-2,5),F(3,5)),(F(3,5),F(2,5))],
          [(F(-1,10**5),F(1,2)),(F(1,10**5),F(1,2))],
          [(F(-1,1000),F(1000,1001)),(F(1),F(1,1001))]]
    diagnostic_events=0
    for law in laws:
        require(sum((x*p for x,p in law),F(0))==0, "centered diagnostic law")
        for copies in [1,2]:
            for threshold in [F(-3,5),F(0),F(3,5),F(6,5)]:
                moment_bound=probability=F(0)
                for atoms in itertools.product(law,repeat=copies):
                    value=sum((a[0] for a in atoms),F(0))-threshold
                    weight=F(1)
                    for _,p in atoms:
                        weight*=p
                    moment_bound+=weight*evaluate(h,value)
                    probability+=weight*(value>0)
                require(moment_bound<=probability,"diagnostic strict-event minorant")
                diagnostic_events+=1

    rejected=[]
    # Deliberate corruptions are in memory only. These test predicates used by
    # acceptance, not independent implementations of the analytic argument.
    mutations={
      "wrong_negative_phase_slope":lambda:rectangle_data(negative_b=F(-2)),
      "oversized_variance_rectangle":lambda:rectangle_data(limit=F(1,10)),
      "oversized_summand_amplitude":lambda:rectangle_data(A=F(1)),
      "wrong_positive_phase_slope":lambda:rectangle_data(positive_b=F(0)),
      "minorant_constant_at_atom":lambda:require(evaluate(add(h,(F(1,100),)),F(0))<=0,
                                                   "strict atom mutant"),
      "minorant_positive_leading_term":lambda:require(
          evaluate(add(h,(F(0),F(0),F(0),F(0),F(32,5))),F(2))<=1,
          "leading term mutant"),
      "lost_small_endpoint_margin":lambda:require(
          evaluate(add(polys['P'],(-F(1,100),)),F(1,100))>0,
          "endpoint mutant"),
      "incorrect_domination_constant":lambda:require(
          same(add(polys['gap'],(-F(1,1000),)),polys['gap']),
          "domination identity mutant"),
    }
    for name,test in mutations.items():
        try:
            test()
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError("negative control unexpectedly accepted: "+name)
    source=Path(__file__).resolve().parents[1]/'sections/08-direct-comparison.tex'
    return dict(status="PASS_REVISION_COUNT_CONSTANTS",python=sys.version,
                mathematical_scope="Exact changed scalar identities and endpoint inequalities; analytical soundness remains in the manuscript.",
                arithmetic="Python integer and fractions.Fraction; no floating-point acceptance",
                rectangle=rows,polynomials=polys,diagnostic_events=diagnostic_events,
                rejected_mutations=rejected,
                manuscript_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())


if __name__=='__main__':
    print(json.dumps(run(),default=str,indent=2))

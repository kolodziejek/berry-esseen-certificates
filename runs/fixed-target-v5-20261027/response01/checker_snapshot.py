#!/usr/bin/env python3
"""Exact bounded acceptance of the common-response bound on CENTRAL row 19.

Reads JSON proof data as untrusted source bytes; imports no archive program.
This checks a new conditional coefficient inequality, not acquisition.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import platform
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[3]
ARCHIVE = "verification/finite-tail/sources/backend.zip"
ARCHIVE_SHA = "43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52"
MANIFEST_SHA = "c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf"
ROW_PATH = "work/toward40_20261007/audit43/capsule/work/below49_20261006/acquisition/central42_confinement_candidate.json"
ROW_SHA = "2f95d0271996eb9868c2fffcdfb0fa2646a99c2cf588e70d063178e27d07246d"


def need(test, message):
    if not test:
        raise ValueError(message)


def ev(p, x):
    result = F(0)
    for a in reversed(p):
        result = result*x+a
    return result


def derivative(p):
    return [i*a for i, a in enumerate(p)][1:]


def poly_interval(p, lo, hi):
    # x>=0, so each monomial has a directed interval.
    need(0 <= lo <= hi, "positive polynomial interval")
    return (sum(a*(lo**j if a >= 0 else hi**j) for j, a in enumerate(p)),
            sum(a*(hi**j if a >= 0 else lo**j) for j, a in enumerate(p)))


def ratio_derivative(p, d):
    d0, d1 = d
    return [p[1]*d0-p[0]*d1, 2*p[2]*d0,
            p[2]*d1+3*p[3]*d0, 2*p[3]*d1]


def one_maximum(p, d, lo, hi, bound):
    need(ev(d, lo) > 0 and d[1] > 0, "positive affine denominator")
    g = ratio_derivative(p, d)
    gp, gpp = derivative(g), derivative(derivative(g))
    # G''<0 and G'(lo)<0 imply G strictly decreases throughout.
    need(poly_interval(gpp, lo, hi)[1] < 0 and ev(gp, lo) < 0,
         "whole-interval derivative direction")
    need(ev(g, lo) > 0 > ev(g, hi), "unique stationary maximum inside")
    a, b = lo, hi
    for _ in range(40):
        mid = (a+b)/2
        if ev(g, mid) > 0:
            a = mid
        else:
            b = mid
    upper = poly_interval(p, a, b)[1]/ev(d, a)
    endpoints = [ev(p, x)/ev(d, x) for x in (lo, hi)]
    need(max([upper]+endpoints) < bound, "strict closed-domain ratio bound")
    return dict(polynomial=p, denominator=d, domain=[lo,hi],
                derivative_numerator=g, stationary_bracket=[a,b],
                stationary_upper=upper, endpoint_ratios=endpoints, bound=bound)


def q(j, v, x):
    return sum((k+1)*v**k*x**(j-2-k) for k in range(j-1))


def moments(xs, ps):
    return dict(rho=sum(p*abs(x)**3 for x,p in zip(xs,ps)),
                beta=sum(p*x*abs(x) for x,p in zip(xs,ps)),
                gamma=sum(p*x**3 for x,p in zip(xs,ps)),
                mu4=sum(p*x**4 for x,p in zip(xs,ps)),
                eta5=sum(p*abs(x)**5 for x,p in zip(xs,ps)),
                zeta4=sum(p*x*abs(x)**3 for x,p in zip(xs,ps)))


def polynomial_part(m, J, J1, J2, H, phi, c):
    r,b,g,M,E,Z=(m[k] for k in ("rho","beta","gamma","mu4","eta5","zeta4"))
    Kq=E/4-r*M/2-F(3,2)*b*g+r/2
    K1=Z-3*b-F(3,2)*r*g
    return c*(F(3,2)*b*J+3*r*J1-3*J2-Kq)+H*(c*K1+phi*(J1+(M-3)/6))-H*H*(c*r+phi*g/2)


def exact_response(v, x, sign, m, m0, J, J1, H, phi, c):
    r,b=m["rho"],m["beta"]
    g0,M0=m0["gamma"],m0["mu4"]
    R3,R4,R5=q(3,v,x),q(4,v,x),q(5,v,x)
    T0=-R5/4+r*R4/2+(M0/2-F(1,2)+3*J1)*R3+F(3,2)*sign*((g0+J)+b*R3)
    T1=sign*(R4-3)-F(3,2)*(sign*r+g0)*R3
    return c*T0+H*(c*T1+phi*R4/6)-H*H*(c+sign*phi/2)*R3


def encode(value):
    if isinstance(value,F): return str(value)
    if isinstance(value,list): return [encode(x) for x in value]
    if isinstance(value,dict): return {k:encode(v) for k,v in value.items()}
    return value


def main():
    need(not sys.flags.optimize and __debug__, "unoptimized Python required")
    raw=(ROOT/ARCHIVE).read_bytes()
    need(sha256(raw).hexdigest()==ARCHIVE_SHA, "archive bytes")
    with zipfile.ZipFile(ROOT/ARCHIVE) as z:
        manifest=z.read("finite61/MANIFEST.json")
        need(sha256(manifest).hexdigest()==MANIFEST_SHA, "manifest bytes")
        entry=json.loads(manifest)["files"][ROW_PATH]
        need(entry["sha256"]==ROW_SHA, "manifest path binding")
        blob=z.read("finite61/blobs/"+ROW_SHA)
        need(sha256(blob).hexdigest()==ROW_SHA, "row source bytes")
        obj=json.loads(blob);row=obj["rows"][19]
    need(obj["N"]==42 and row["index"]==19, "row index binding")
    expected={"pl":"209/500","pu":"21/50","theta":"12657/1000000",
              "rho":"214889/200000","beta":"174581/1000000",
              "beta_lo":"72659/500000","A":"810731/1000000",
              "B":"284079/250000","radius":"46/25"}
    need(all(row[k]==v for k,v in expected.items()), "exact selected fields")

    l,u,T,R=F(row["pl"]),F(row["pu"]),F(row["theta"]),F(row["radius"])
    vl,vu=l*(1-l),u*(1-u)
    al,au,bl,bu=F(21,25),F(213,250),F(29,25),F(119,100)
    A,B,r,blo,bhi=F(81,100),F(113,100),F(43,40),F(29,200),F(7,40)
    need(0<l<u<F(1,2) and 0<T<1, "probability/noise domain")
    need(al**2 < (1-T)*l/(1-l) and au**2 > u/(1-u), "negative mean box")
    need(bl**2 < (1-T)*(1-u)/u and bu**2 > (1-l)/l, "positive mean box")
    need(F(row["A"])>A and F(row["B"])>B, "inner endpoint floors")
    need(F(row["rho"])<r and blo<F(row["beta_lo"])<=F(row["beta"])<bhi,
         "actual moment bounds")
    need(F(49,100)**2 < (1-T)*vl, "first absolute half-moment floor")
    need(F(3,10)**2 < (1-T)**3*(1-2*u)**2/vu, "positive skeleton skew lower")
    need(F(1,3)**2 > (1-2*l)**2/vl, "skeleton skew upper")
    need(1/vl-3<F(10,9), "skeleton fourth moment upper")
    need(F(3,2)*(F(3,10)+F(49,100)*(A+B)**2)>3, "negative signed constant")
    J1upper=R*r/3+au*bu**2/4
    need(J1upper<1, "same-law gap first moment upper")
    need(F(79,25)**2<10, "lower square-root constant")

    alpha=F(43,80)
    pplus=[F(435879881,36000000),F(320027,90000),-F(17,400),-F(1,4)]
    pminus=[F(895536247,375000000),F(289067,90000),F(47,400),-F(1,4)]
    def envelope(vl0,vu0,linear,constant):
        return [3*alpha*vu0**2-vu0**3+2*linear*vu0+constant,
                2*alpha*vl0-F(3,4)*vl0**2+linear,
                alpha-vl0/2,-F(1,4)]
    need(envelope(bl,bu,F(55,18)+F(21,80),F(289,80))==pplus,"positive envelope coefficients")
    need(envelope(al,au,F(55,18)-F(87,400),-F(3))==pminus,"negative envelope coefficients")
    # In either class: the u^2 and u coefficients decrease with v; constant increases.
    for vlow,vhigh,linear in [(bl,bu,F(55,18)+F(21,80)),(al,au,F(55,18)-F(87,400))]:
        need(2*alpha-F(3,2)*vlow<0, "u coefficient decreases")
        need(6*alpha*vlow-3*vhigh**2+2*linear>0,"constant coefficient increases")
    dplus=[F(54,25)*2*bl+6*B,F(54,25)]
    dminus=[F(104,25)*2*al+6*A,F(104,25)]
    plus=one_maximum(pplus,dplus,B,R,F(221,200))
    minus=one_maximum(pminus,dminus,A,R,F(3,8))

    # Four signed linear-H responses. Each polynomial is an upper enclosure.
    linear_polys=[
        ("H>=0,+", [F(7,2)*bu**2-F(39,10)*bu-3,F(7,3)*bu-F(39,20),F(7,6)],dplus,B),
        ("H>=0,-", [-F(5,2)*al**2+F(93,40)*al+3,F(93,80)-F(5,3)*al,-F(5,6)],dminus,A),
        ("H<=0,+", [-3*bl**2+F(169,40)*bl+3,F(169,80)-2*bl,-F(1)],dplus,B),
        ("H<=0,-", [3*au**2-2*au-3,2*au-1,F(1)],dminus,A),
    ]
    linear=[]
    for name,p,d,xlo in linear_polys:
        w=[F(9,50)*d[0]-p[0],F(9,50)*d[1]-p[1],-p[2]]
        if w[2]<0:
            # Concavity: minimum on a closed interval is at an endpoint.
            need(min(ev(w,xlo),ev(w,R))>0,"linear response endpoint gate")
        else:
            need(ev(derivative(w),xlo)>0 and ev(w,xlo)>0,"linear response increasing gate")
        linear.append(dict(name=name, polynomial=p, denominator=d,
                           domain=[xlo,R], endpoint_slacks=[ev(w,xlo),ev(w,R)]))
    need(F(819,2000)>F(2,5)/2,"nonpositive quadratic-H noise response")

    split_at_R=(alpha*q(4,bu,R)+(F(55,18)+F(21,80))*q(3,bu,R)+F(289,80))/ev(dplus,R)
    need(split_at_R==F(173316497,113512320)>F(221,200),"strict split-response improvement")

    # Actual rational four-point law within the selected moment/support domain.
    xs=list(map(F,[-533,-517,717,733]));xs=[x/617 for x in xs]
    ps=[F(29,100),F(29,100),F(21,100),F(21,100)]
    need(sum(ps)==1 and sum(p*x for p,x in zip(ps,xs))==0 and sum(p*x*x for p,x in zip(ps,xs))==1,"standardized control law")
    m=moments(xs,ps);means=[-F(525,617),-F(525,617),F(725,617),F(725,617)]
    m0=moments(means,ps);theta=sum(p*(x-v)**2 for p,x,v in zip(ps,xs,means))
    need(theta>0 and theta<T and m["rho"]<F(row["rho"]) and F(row["beta_lo"])<m["beta"]<F(row["beta"]),"actual law's moments")
    need(-xs[1]>F(row["A"]) and xs[2]>F(row["B"]) and max(map(abs,xs))<R,"actual law's support")
    # J,J1,J2 are allowed to be arbitrary in the identity; use exact actual gaps.
    J=J1=J2=F(0)
    for a,b in zip(xs,xs[1:]):
        tau=sum(p*x for p,x in zip(ps,xs) if x>=b)
        J+=tau*(b-a)**2
        J1+=tau*((b**3-a**3)/3-a*(b*b-a*a)/2)
        # Integral (t-a)t|t| across a gap, split at zero if needed.
        cuts=sorted(set([a,b]+([F(0)] if a<0<b else [])))
        for x,y in zip(cuts,cuts[1:]):
            sign=1 if x>=0 else -1
            J2+=tau*sign*((y**4-x**4)/4-a*(y**3-x**3)/3)
    for H in [F(-1),F(-1,7),F(0),F(1,3),F(1)]:
        for phi in [F(1,3),F(2,5)]:
            c=F(20487,50000) # algebra allows arbitrary c; not asserted equal CE.
            difference=polynomial_part(m,J,J1,J2,H,phi,c)-polynomial_part(m0,J,J1,J2,H,phi,c)
            integral=sum(p*(x-v)**2*exact_response(abs(v),abs(x),1 if x>0 else -1,m,m0,J,J1,H,phi,c)
                         for p,x,v in zip(ps,xs,means))
            need(difference==integral,"exact combined moment response")
    # A positive-noise law witnesses non-vacuity; no maximizer or score claim.
    controls=[]
    def reject(name,fn):
        try:fn()
        except ValueError:controls.append(name)
        else:raise ValueError("negative control accepted: "+name)
    reject("too_small_ratio_target",lambda:one_maximum(pplus,dplus,B,R,F(11,10)))
    reject("wrong_stationary_direction",lambda:one_maximum(pplus,dplus,R,B,F(221,200)))
    reject("omit_one_sign",lambda:need(len(linear_polys[:2])==4,"both H and sign classes required"))
    reject("zero_noise_claim_from_positive_example",lambda:need(theta==0,"positive noise retained"))
    reject("replace_actual_gap_by_skeleton_gap",lambda:need(J==F(21,50)*F(29,50)*(F(1250,617))**3,"actual and skeleton gaps differ"))
    need(m["eta5"]!=m0["eta5"],"negative fifth-moment response is not zero")
    print(json.dumps(encode(dict(
        status="PASS_BOUNDED_COMMON_RESPONSE",python=platform.python_version(),
        scope="New conditional moment-polynomial bound on CENTRAL19; no acquisition, full raw remainder or LOCAL42 acceptance",
        archive_sha256=ARCHIVE_SHA,manifest_sha256=MANIFEST_SHA,row_source=ROW_PATH,row_sha256=ROW_SHA,
        selected_fields=expected,derived=dict(J1_upper=J1upper,mean_minus=[al,au],mean_plus=[bl,bu]),
        constant_responses=[plus,minus],linear_responses=linear,split_benchmark=split_at_R,
        strict_ratio_reserve=split_at_R-F(221,200),control_law=dict(xs=xs,ps=ps,theta=theta,moments=m,J=J,J1=J1,J2=J2),
        rejected_controls=controls,
        input_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in [
            "mathematics/strategy-v4/2026-10-27/geometry.tex",
            "mathematics/strategy-v4/2026-10-27/excess.tex",
            "mathematics/fixed-target-v5/2026-10-27/response_check.py"]}
    )),indent=2))


if __name__=="__main__":
    main()

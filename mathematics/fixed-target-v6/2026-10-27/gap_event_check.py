#!/usr/bin/env python3
"""Exact finite-law controls for the central-gap event; no kernel imports."""
from fractions import Fraction as Q
import json

SL,SU=Q(3162277660,10**9),Q(3162277661,10**9)


def law_check(name,atoms,d):
    atoms=sorted(atoms)
    E=lambda f:sum(p*f(x) for x,p in atoms)
    assert E(lambda x:Q(1))==1 and E(lambda x:x)==0 and E(lambda x:x*x)==1
    rho=E(lambda x:abs(x)**3);gamma=E(lambda x:x**3)
    m=E(lambda x:max(x,0));p=E(lambda x:Q(x>0));q=1-p
    J=Q(0)
    for (x,px),(y,py) in zip(atoms,atoms[1:]):
        mid=(x+y)/2;tau=E(lambda z:z*Q(z>=mid))
        J+=tau*(y-x)**2
    dl,dh=(3+SL)*rho-gamma-3*J,(3+SU)*rho-gamma-3*J
    assert dh<=d
    gate=d<(SL-1)*rho
    result=dict(name=name,rho=str(rho),D_lower=str(dl),D_upper=str(dh),
                chosen_d=str(d),strict_gap_gate=gate)
    zero=any(x==0 and prob>0 for x,prob in atoms)
    if zero:
        assert not gate
        return result
    A=min(-x for x,prob in atoms if x<0);B=min(x for x,prob in atoms if x>0)
    Tplus=E(lambda x:max(x,0)**3)-m*B*B
    Tminus=E(lambda x:max(-x,0)**3)-m*A*A
    assert Tplus>=0 and Tminus>=0
    assert m*(A*A+B*B)==rho-Tplus-Tminus
    assert Q(1)/(2*rho)<=m<=Q(1,2) and m*m<=p*q
    prob=sum(px*py for x,px in atoms for y,py in atoms if x*y<0)
    second=sum(px*py*(x-y)**2 for x,px in atoms for y,py in atoms if x*y<0)/prob
    alpha=1/(2*rho*rho)
    assert prob==2*p*q>=alpha and second<=2/alpha
    if gate:
        P0=(SL-1)*rho-d;S=rho-d/(SL-1)
        basic=2*S;strong=2*S+2*P0/3
        assert S>0 and P0>0
        assert (A+B)**2>=strong>basic>0
        result.update(gap_squared_actual=str((A+B)**2),gap_squared_lower=str(strong),
                      event_probability=str(prob),probability_lower=str(alpha),
                      conditional_second=str(second),conditional_second_upper=str(2/alpha))
    return result


def main():
    assert SL*SL<10<SU*SU
    a=Q(8,5)
    skew=[(-a,1/(1+a*a)),(1/a,a*a/(1+a*a))]
    controls=[law_check('symmetric Bernoulli',[(Q(-1),Q(1,2)),(Q(1),Q(1,2))],Q(1,5)),
        law_check('skew Bernoulli with chosen d>2',skew,Q(5,2)),
        law_check('reflected skew Bernoulli',[(-x,p) for x,p in skew],Q(3,5)),
        law_check('gapped three-point law',[(Q(-11,10),Q(199,440)),(Q(9,10),Q(21,40)),(Q(11,10),Q(1,44))],Q(1,2)),
        law_check('gapped law whose sufficient gate fails',[(Q(-1),Q(7,15)),(Q(1,2),Q(1,3)),(Q(3,2),Q(1,5))],Q(3)),
        law_check('zero atom rejects the gap gate',[(Q(-5,4),Q(8,25)),(Q(0),Q(9,25)),(Q(5,4),Q(8,25))],Q(4))]
    assert controls[1]['strict_gap_gate'] and Q(controls[1]['chosen_d'])>2
    # A boundary-only gate provides no strictly positive distance for HIGH.
    l=Q(1);d=(SL-1)*l
    assert 2*(l-d/(SL-1))==0
    # All fixed windows' d0-independent HIGH gates at worst initial M and alpha.
    N=42;umax=Q(7361,4000);M=Q(96,25)*umax;alpha=1/(2*umax*umax)
    rate=(1-max(1-t*t+(M+3)*t**4/12 for t in [Q(1,2),Q(9,10)]))/2
    slope=(1-(M+3)*Q(53,600))/2;cquarter=Q(1,8)-(M+3)/384
    assert 1<=M<=Q(111,10) and 0<alpha<=1 and 2*umax<4
    assert slope>0 and 2*N*cquarter>1
    margins=[]
    for w in [Q(1,8),Q(4,25),Q(9,50),Q(1,5),Q(11,50),Q(1,4)]:
        h=Q(333,106)-Q(22,7)**3*w*w/6
        assert h>0
        ms=[2*N*x-1 for x in [rate,alpha*h*h*w*w,alpha*Q(23,48)**2,Q(1,8)]]
        assert min(ms)>0
        margins.append({'window':str(w),'smallest_monotonicity_margin':str(min(ms))})
    print(json.dumps({'status':'PASS_BOUNDED_CENTRAL_GAP_EVENT',
        'finite_laws':controls,'generic_HIGH_window_gates':margins,
        'scope':'No24cell acquisition or HIGH evaluation. Conditional event interface and bounded exact controls only.'},indent=2))


if __name__=='__main__':main()

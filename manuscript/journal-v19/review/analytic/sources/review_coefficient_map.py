#!/usr/bin/env python3
"""Independent actual-law regression for the fixed coefficient map.

Finite examples do not prove the continuous-domain analytic license.
"""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import json
import sys

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE/'algebra'))
from accept_objects import verify, load
from coefficient_map import Family, coherent_coefficients, sign_contraction
from check_conditional_family import bernoulli, three, mix, moment, k1


def primitive(law):
    pos=[(x,w)for x,w in law if x>0]
    neg=[(-x,w)for x,w in law if x<0]
    p=sum(w for x,w in pos);q=1-p;m=sum(x*w for x,w in pos)
    Rplus=max(x for x,w in pos);Rminus=max(x for x,w in neg)
    A=min(x for x,w in neg);B=min(x for x,w in pos)
    def raw(part,j):return sum(w*x**j for x,w in part)
    aplus,aminus=raw(pos,2),raw(neg,2)
    bplus,bminus=raw(pos,3),raw(neg,3)
    tp=bplus-m*B*B;tm=bminus-m*A*A
    point=lambda x:[x,x]
    cell={'radii':[Rplus,Rminus],'m':point(m),
          'a_plus':point(aplus),'a_minus':point(aminus),
          'b_plus':point(bplus),'b_minus':point(bminus),
          'rho':point(moment(law,3)),'beta':point(moment(law,2,True)),
          'gamma':point(moment(law,3,True)),'A':point(A),'B':point(B),
          'mu4_upper':moment(law,4),'eta5_upper':moment(law,5),
          # Exact rational valid budget. It is a premise here, not a claimed
          # rational replacement for sqrt(10) in the manuscript's defect.
          'outer':{'amount':2*tp+4*tm,'plus_price':F(2),'minus_price':F(4),
                   'plus_cap':tp,'minus_cap':tm}}
    return cell,(p,q,m,A,B,Rplus,Rminus)


def integral_poly(a,b,j):
    return (b**(j+2)-a**(j+2))/F(j+2)-a*(b**(j+1)-a**(j+1))/F(j+1)


def gap_integrals(law):
    points=sorted(x for x,w in law)
    j1=j2=F(0)
    for a,b in zip(points,points[1:]):
        tau=sum(x*w for x,w in law if x>=(a+b)/2)
        j1+=tau*integral_poly(a,b,1)
        # Primitive of (t-a)t|t|, split at zero with the same lower endpoint.
        def primitive(t):return t**4/F(4)-a*t**3/F(3)
        if b<=0: part=-(primitive(b)-primitive(a))
        elif a>=0: part=primitive(b)-primitive(a)
        else:part=primitive(b)+primitive(a)
        j2+=tau*part
    return j1,j2


def reject(call):
    try:call()
    except (ValueError,TypeError,KeyError,ZeroDivisionError):return True
    raise AssertionError('invalid object/domain accepted')


def main():
    path=BASE/'algebra/proof_objects.json';family=Family(path)
    laws={'symmetric':bernoulli(F(1)),
          'skew_positive':bernoulli(F(2,3)),
          'skew_negative_central':bernoulli(F(3,2)),
          'four_points':mix(bernoulli(F(2,3)),bernoulli(F(4,5)),F(1,4)),
          'tiny_noise':mix(bernoulli(F(2,3)),bernoulli(F(667,1000)),F(1,10**20)),
          'asymmetric_far_support':mix(bernoulli(F(2,3)),bernoulli(F(1,100)),F(1,10**24))}
    law_results={}
    for name,law in laws.items():
        cell,(p,q,m,A,B,rp,rm)=primitive(law);rho=moment(law,3)
        result=coherent_coefficients(family,cell,rho)
        j1,j2=gap_integrals(law);mu4=moment(law,4);eta5=moment(law,5)
        beta=moment(law,2,True);gamma=moment(law,3,True)
        negative_kq=rho*mu4/2-eta5/4+F(3,2)*beta*gamma-rho/2
        assert result['mu4'][0]<=mu4<=result['mu4'][1]
        assert eta5<=result['eta5_upper']
        assert result['signed_fourth'][0]<=moment(law,4,True)<=result['signed_fourth'][1]
        assert result['K1'][0]<=k1(law)<=result['K1'][1]
        actual_u=j1+(mu4-3)/6
        assert result['U'][0]<=actual_u<=result['U'][1]
        assert 3*(rho*j1-j2)<=result['three_G_upper']
        assert negative_kq<=result['negative_Kq_upper']
        theta=1-m*m/(p*q);vlaw=[(m/p,p),(-m/q,q)]
        kl,ku=family.conditional_k([B,rp],[A,rm],[m/p,m/p],[m/q,m/q],
                                   [rho,rho],[moment(vlaw,3,True)]*2,theta)
        assert kl<=k1(law)-k1(vlaw)<=ku
        # Wider intervals test sign-sensitive m and the full central rectangle.
        box=family.central([A/2,2*A],[B/2,2*B],[m/2,2*m],rho)
        actual_c1=m*(B**3/3+A*B*B/2-A**3/6)
        actual_c2=m*(B**4/4+A*B**3/3-A**4/12)
        assert box['J1_interval'][0]<=actual_c1<=box['J1_interval'][1]
        assert box['J2_interval'][0]<=actual_c2<=box['J2_interval'][1]
        assert rho*actual_c1-actual_c2<=box['G_upper']
        law_results[name]={'atoms':len(law),'theta':str(theta),'central_J1_sign':(actual_c1>0)-(actual_c1<0)}
    controls={}
    controls['zero_denominator_nonzero_cross']=reject(lambda:sign_contraction(1,[1,1],[1,1],[F(1,2)]*2))
    controls['negative_sign_radius']=reject(lambda:sign_contraction(-1,[1,1],[1,1],[1,1]))
    controls['theta_one']=reject(lambda:family.conditional_k([1,1],[1,1],[1,1],[1,1],[1,1],[0,0],1))
    obj=load(path)
    bad=deepcopy(obj);bad['polynomials'][0]['coefficients'][0][1]='123'
    controls['changed_polynomial']=reject(lambda:verify(bad))
    bad2=deepcopy(obj);bad2['moment_matrices'].pop()
    controls['missing_matrix']=reject(lambda:verify(bad2))
    bad3=deepcopy(obj);bad3['central_transform'].reverse()
    controls['reordered_bernstein_rows']=reject(lambda:verify(bad3))
    print(json.dumps({'status':'PASS_INDEPENDENT_EXACT_MAP_EXAMPLES','continuous_domain_acceptance_claimed':False,
                      'algebra_acceptance':family.acceptance,'laws':law_results,'negative_controls':controls},indent=2))


if __name__=='__main__':main()

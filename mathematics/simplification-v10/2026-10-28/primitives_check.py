#!/usr/bin/env python3
"""Exact bounded controls for elementary analytic reductions; no constructor imports.

The written analytic proofs handle the continuum and all laws. This script
checks scalar arithmetic, algebraic identities and fixed actual-law fixtures.
It is not a finite-base or global Berry--Esseen acceptor.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import factorial
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions must remain enabled')

def need(condition, message):
    if not condition:
        raise ValueError(message)

def expect(law, fun):
    return sum((p * fun(x) for x, p in law), F(0))

def normalize(law):
    d = defaultdict(F)
    for x, p in law:
        d[x] += p
    need(all(p >= 0 for p in d.values()), 'Negative probability')
    return sorted((x, p) for x, p in d.items() if p)

def bernoulli(a):
    return [(-a, 1 / (1 + a*a)), (1/a, a*a/(1 + a*a))]

def mix(left, right, weight):
    return normalize([(x, weight*p) for x,p in left] +
                     [(x, (1-weight)*p) for x,p in right])

def summary(law):
    need(expect(law, lambda x: F(1)) == 1, 'Mass')
    need(expect(law, lambda x: x) == 0, 'Mean')
    need(expect(law, lambda x: x*x) == 1, 'Variance')
    m = expect(law, lambda x: max(x,F(0)))
    rho = expect(law, lambda x: abs(x)**3)
    beta = expect(law, lambda x: x*abs(x))
    gamma = expect(law, lambda x: x**3)
    moment4 = expect(law, lambda x: x**4)
    moment5 = expect(law, lambda x: abs(x)**5)
    return m, rho, beta, gamma, moment4, moment5

def fifth(law):
    m, rho, beta, gamma, moment4, moment5 = summary(law)
    need(m > 0 and -1 < beta < 1, 'Strict sign domains')
    delta = gamma-rho*beta
    square = (moment5-2*rho*moment4+rho**3)/4
    signed = ((rho+gamma)*max(delta,F(0))**2/(8*(1+beta)**2) +
              (rho-gamma)*max(-delta,F(0))**2/(8*(1-beta)**2))
    weighted = delta**2/(8*m)
    quartic = delta**4/(4*rho*(1-beta**2)**2)
    combined = signed+weighted/2
    need(square >= combined, 'Combined fifth-moment inequality')
    need(combined >= max(signed, weighted, quartic), 'Domination')
    for sign in (-1,1):
        a = expect(law, lambda x: max(sign*x,F(0))**2)
        b = expect(law, lambda x: max(sign*x,F(0))**3)
        d = b-rho*a
        V = expect(law, lambda x: max(sign*x,F(0))**3 *
                   (max(sign*x,F(0))-rho)**2)
        need(V >= d*d/m, 'One-sign weighted loss')
        if d >= 0:
            need(V >= b*d*d/(a*a), 'One-sign stronger loss')
    return {'square':square,'signed':signed,'weighted':weighted,
            'combined':combined,'quartic':quartic}

def first(law):
    m,rho,*_ = summary(law)
    u = 2*m
    R = max(abs(x) for x,p in law)
    need(1 <= rho <= R and 1/R <= u <= 1, 'First-moment domains')
    det = (R-u)*(R-rho)-(R*u-1)**2
    polynomial = -R*R*u*u+(R+rho)*u+R*R-R*rho-1
    radicand = (R-rho)*(4*R**3-3*R-rho)
    need(det == polynomial >= 0, 'PSD determinant')
    need(radicand == (R+rho)**2+4*R*R*(R*R-R*rho-1) >= 0,
         'Discriminant identity')
    # Avoid approximating a square root: z <= sqrt(D) follows from z<=0
    # or z^2<=D. The determinant identity supplies this upper-root inequality.
    z = 2*R*R*u-(R+rho)
    need(z <= 0 or z*z <= radicand, 'Closed upper root')
    for a in [F(j,10) for j in range(2,13)]:
        bound = (R-rho+2*a+R*a*a)/(a*(2*R+a))
        need(u <= bound, 'Legacy auxiliary comparison')
        # Prove the exact root <= bound by squaring only a nonnegative side.
        s = 2*R*R*bound-(R+rho)
        need(s >= 0 and s*s >= radicand, 'Root dominates sampled auxiliary')
    return det

def transfer(law):
    m,rho,*_ = summary(law)
    mus = {sign: normalize([(sign*x,p*sign*x/m) for x,p in law if sign*x>0])
           for sign in (-1,1)}
    c = {sign:expect(mus[sign],lambda y:y) for sign in (-1,1)}
    for sign in (-1,1):
        need(expect(mus[sign],lambda y:F(1)) == 1, 'Size-biased mass')
        need(m/c[sign] <= expect(law,lambda x:F(int(sign*x>0))), 'Zero mass')
    Q = normalize([(-c[-1],m/c[-1]),(F(0),1-m/c[-1]-m/c[1]),
                   (c[1],m/c[1])])
    summary(Q)
    eta = rho-expect(Q,lambda x:abs(x)**3)
    variances = {s:expect(mus[s],lambda y:(y-c[s])**2) for s in (-1,1)}
    need(eta == m*sum(variances.values()) >= 0, 'Defect variance identity')
    if not eta:
        need(normalize(Q) == normalize(law), 'Zero-defect law equality')
    # Exact coefficient form of the common characteristic representation,
    # including both tags and all low moments. k=0 is equality of masses.
    for k in range(1,13):
        actual = expect(law,lambda x:x**k)-expect(Q,lambda x:x**k)
        response = m*sum(s**k*(expect(mus[s],lambda y:y**(k-1))-c[s]**(k-1))
                         for s in (-1,1))
        need(actual == response, 'Common response coefficient')
    return Q, eta, variances

def atan_interval(x, terms):
    s = sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    t = s+(-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(s,t),max(s,t)

def cosine():
    lo,hi = atan_interval(F(1,5),8)
    low,high = atan_interval(F(1,239),2)
    pi_lo,pi_hi = 16*lo-4*high,16*hi-4*low
    need(F(3) < pi_lo < pi_hi < F(355,113), 'Machin enclosure')
    y=F(23311,10000)
    lower=sum(((-1)**(j-1)*(2*j-1)*y**(2*j)/factorial(2*j)
               for j in range(1,7)),F(0))
    need(y*y < 11*14, 'Alternating tail decreases from j=6')
    need(lower > F(3,200000), 'Positive derivative before the true maximizer')
    margin=F(4553,1000)-4*F(355,113)*y/(1+y*y)
    need(margin > F(1,10000), 'Final cosine upper margin')
    # Genuine counterexample to K=9/2 at x=3/8, without evaluating sqrt2.
    need(F(11,8)**2 < 2 and (8+4*F(11,8))/3 == F(9,2),
         'False 9/2 negative control')
    return {'machin_terms':[8,2], 'stationary_point_lower':str(y),
            'six_term_derivative_lower':str(lower),
            'derivative_lower_decimal_diagnostic':float(lower),
            'final_margin':str(margin), 'margin_decimal_diagnostic':float(margin)}

def finite_base():
    lo,hi=atan_interval(F(1,5),8)
    low,high=atan_interval(F(1,239),2)
    pi_lo,pi_hi=16*lo-4*high,16*hi-4*low
    sig_lo,sig_hi=F('3.162277660'),F('3.162277661')
    need(sig_lo**2<10<sig_hi**2,'Sqrt10 enclosure')
    need((19+6*sig_lo)/(72*pi_hi)>F(819,2000)**2,'Target lower bound')
    need((19+6*sig_hi)/(72*pi_lo)<F(41,100)**2,'Target upper bound')
    need(F(3031,10000)*F(323,500)/(F(819,2000)-F(3031,10000))
         == F(7361,4000)<F(1841,1000),'Finite-base moment bound')
    need(pi_lo>F(25,8) and F(8,3)*pi_lo>8,'Density constants')
    need(F(13,2)**2>41,'Finite index square root')
    A=F(13,16)+F(3,2)*F(41,100)*F(1841,1000)
    B=41*F(2,5)+3*F(41,100)
    C=F(819,2000)
    need(A==F('1.944715') and B==F('17.63'),'Contact coefficients')
    y=F(13)
    values=[F(533,2)+A*y*y+B*y-C*y**3,2*A*y+B-3*C*y*y,
            2*A-6*C*y,-6*C]
    need(values[0]<-75 and values[1]<-139 and values[2]<-28 and values[3]<0,
         'Full exterior ray derivative signs')
    need(C-F(533,2)/26**2==F(397,26000)>0,'Threshold exclusion')
    return {'finite_n_domain':[1,41],'support_radius':13,'threshold_radius':26,
            'contact_polynomial_at13_and_derivatives':[str(x)for x in values],
            'threshold_margin':str(F(397,26000)),
            'scope':'Conditional on the stated universal affine structural inequality and fixed-target maximizing contact, not finite-base acceptance'}

def complex_product(z,w):
    return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cpow(z,n):
    out=(F(1),F(0))
    for _ in range(n):out=complex_product(out,z)
    return out
def cminus(z,w):return z[0]-w[0],z[1]-w[1]
def norm2(z):return z[0]**2+z[1]**2

def powers():
    points=[(F(0),F(0)),(F(1),F(0)),(F(-1),F(0)),(F(3,5),F(4,5)),
            (F(1,2),F(-1,3)),(F(999,1000),F(0))]
    total=0
    for psi,g,n in product(points,points,[1,2,3,4,8,41,42]):
        need(norm2(psi)<=1 and norm2(g)<=1,'Unit-disk fixture')
        delta=cminus(psi,g)
        lin=complex_product(cpow(g,n-1),delta)
        rem=cminus(cminus(cpow(psi,n),cpow(g,n)),(n*lin[0],n*lin[1]))
        cap=F(n*(n-1),2)*norm2(delta)
        need(norm2(rem)<=cap*cap,'Power remainder')
        total+=1
    # n=2, psi=1, g=0 attains the coefficient one exactly.
    need(norm2((F(1),F(0))) > F(1,2)**2,'Missing factor negative control')
    return total

def main():
    laws=[]
    for a in [F(1,20),F(1,4),F(1,2),F(3,4),F(1),F(3,2),F(2),F(20)]:
        laws.append(('bernoulli_'+str(a),bernoulli(a)))
    for R in [F(1),F(5,4),F(2),F(20)]:
        laws.append(('zero_'+str(R),normalize([(-R,1/(2*R*R)),
                     (F(0),1-1/(R*R)),(R,1/(2*R*R))])))
    for a,b,w in product([F(1,4),F(3,4),F(2)],
                         [F(1,2),F(1),F(3)],
                         [F(1,10**8),F(1,100),F(1,2),F(99,100)]):
        laws.append(('mixture_'+str((a,b,w)),mix(bernoulli(a),bernoulli(b),w)))
    for t in [F(1,10**8),F(1,40),F(1,12),F(1,6)]:
        law=normalize([(F(-1),F(1,2)-t),(F(0),3*t),
                       (F(1),F(1,2)-3*t),(F(2),t)])
        laws.append(('one_sign_defect_'+str(t),law))
        laws.append(('reflected_defect_'+str(t),[(-x,p) for x,p in law]))
    strict_improvements=zero_defects=0
    for name,law in laws:
        z=fifth(law);first(law);Q,eta,var=transfer(law)
        strict_improvements+=z['combined']>max(z['signed'],z['weighted'],z['quartic'])
        zero_defects+=eta==0
    wrong_law=mix(bernoulli(F(1,4)),bernoulli(F(1,2)),F(99,100))
    wrong=fifth(wrong_law)
    false_margin=wrong['signed']+wrong['weighted']-wrong['square']
    correct_margin=wrong['square']-wrong['combined']
    need(false_margin>F(267,10000) and correct_margin>F(201,10000),
         'Rejecting an overlapping full-weighted addition')
    one=normalize([(F(-1),F(19,40)),(F(0),F(3,40)),
                   (F(1),F(17,40)),(F(2),F(1,40))])
    Q,eta,var=transfer(one)
    gamma_diff=expect(one,lambda x:x**3)-expect(Q,lambda x:x**3)
    need(gamma_diff==eta>0 and var[-1]==0,'Sharp cubic coefficient fixture')
    fourth_sum=expect(one,lambda x:x**4)+expect(Q,lambda x:x**4)
    t=2*eta/(7*fourth_sum)
    lower=t**3*eta/6-t**4*fourth_sum/24
    need(lower>t**3*eta/7,'Reject false characteristic coefficient1/7')
    report={'status':'PASS_PRIMITIVE_EXACT_CHECKS','mathematical_scope':
      'Scalar arithmetic and fixed actual-law controls for the stated analytic proofs; no count cover or finite-base acceptance',
      'actual_laws':len(laws),'strict_improvement_fixtures':strict_improvements,
      'zero_defect_fixtures':zero_defects,'polynomial_response_coefficients':12*len(laws),
      'cosine':cosine(),'finite_base_localization':finite_base(),'complex_power_cases':powers(),
      'negative_controls':{
       'false_full_weighted_addition_margin':str(false_margin),
       'correct_combined_loss_margin':str(correct_margin),
       'false_cosine_K':'9/2','false_characteristic_coefficient':'1/7',
       'characteristic_counterexample_t':str(t),
       'false_power_coefficient':'1/2 of n(n-1)/2'},
      'python':sys.version,'optimization':sys.flags.optimize}
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()

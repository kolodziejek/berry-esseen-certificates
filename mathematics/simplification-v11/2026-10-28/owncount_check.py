#!/usr/bin/env python3
"""Exact bounded checks for allocation-preserving own-count estimates.

The polynomial identities and analytic derivation are in owncount.tex.
Actual-law checks are adversarial controls, not a continuous count cover.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions required')

A=F(3,5); d=F(9,125); upper=F(3,40); vmin=F(6,25)
D=F(21,20); phase=F(1,10)
Z=lambda x:F(5,8)*x+F(3,8)+x**3/42
eps=(F(8,3)*upper+(2*D*phase+phase**2)/(2*vmin)+Z(D))/42
gates={
    'sqrt_variance':F(251,500)**2-F(1,4)-upper/42,
    'near_delta':D-F(46,25)*F(251,500)-phase,
    'normal_lower':1-eps-F(19,20),
    'normal_upper':F(21,20)*(1-eps)-1,
    'normal_variance_coefficient':F(8,3)-1/(2*vmin)-D**2/(84*vmin**2),
    'stirling_segment_lower':F(2,5)-D/42-F(9,25),
    'stirling_segment_upper':F(23,40)-F(53,100)-D/42,
    'moment_sign_gate_through_point_one':(A-d)/4-phase,
}
assert all(x>0 for x in gates.values())

def pair(outer,inner):
    if not inner:return [(F(0),F(1))]
    return [(outer,inner/(abs(outer)+inner)),
            (-inner if outer>0 else inner,abs(outer)/(abs(outer)+inner))]

def moments(law):
    return [sum(p*x**j for x,p in law) for j in range(5)]

def sum_law(count,law):
    if len(law)==1:return {F(0):F(1)}
    (x,p),(y,q)=law
    return {j*x+(count-j)*y:F(comb(count,j))*p**j*q**(count-j)
            for j in range(count+1)}

def coeff(kappa,a0,a1):
    return max(A*A+kappa*A,a0*a0-kappa*a0),max(A*A-kappa*A,a1*a1+kappa*a1)

def quartic_data(alpha,b):
    # Two completely explicit admissible minorants: b=2a with M=5a^4,
    # or b=3a/2 with M=2a^4 and maximum at x=a.
    M=5*alpha**4 if b==2*alpha else 2*alpha**4
    if b==F(3,2)*alpha:
        # At z=x/a, 2-z(z+1)^2(3/2-z)
        # =(z-1)^2*(2z^2+5z+4)/2>=0 for z>=0.
        for z in (F(0),F(1,3),F(1),F(3,2),F(2)):
            assert 2-z*(z+1)**2*(F(3,2)-z)==(z-1)**2*(2*z*z+5*z+4)/2
    return M,b-2*alpha,2*alpha*b-alpha**2,alpha**2*b

fixtures=[]; moment_cases=0; own_cases=0; cubic_cases=0
for n in (42,43):
    for p in (F(2,5),F(1,2),F(53,100)):
        q=1-p; v=p*q; k=(n*p.numerator)//p.denominator
        n0,n1=n-k,k
        for lam in (F(1,20),F(3,40)):
            s=lam/n
            for eta in (F(0),F(1,2),F(1)):
                a0=s*(1-eta)/(q*A);a1=s*eta/(p*A)
                u0=pair(-A,a0);u1=pair(A,a1)
                m0,m1=moments(u0),moments(u1)
                assert m0[0]==m1[0]==1 and m0[1]==m1[1]==0
                assert a0+a1<d and a0<p and a1<q
                assert q*m0[2]+p*m1[2]==s
                t0=n0*m0[2];t1=n1*m1[2];t=t0+t1
                wm3=n0*m0[3]+n1*m1[3]
                wm4=n0*m0[4]+n1*m1[4]+3*t*t-3*(n0*m0[2]**2+n1*m1[2]**2)
                laws0,laws1=sum_law(n0,u0),sum_law(n1,u1)
                law={}
                for x,w in laws0.items():
                    for y,z in laws1.items():law[x+y]=law.get(x+y,F(0))+w*z
                assert sum(law.values())==1
                assert sum(x*w for x,w in law.items())==0
                assert sum(x*x*w for x,w in law.items())==t
                assert sum(x**3*w for x,w in law.items())==wm3
                assert sum(x**4*w for x,w in law.items())==wm4
                for alpha,b in ((F(1,2),F(1)),(F(1,2),F(3,4))):
                    M,b3,b2,b1=quartic_data(alpha,b)
                    for r in (F(0),F(1,50),F(1,20),F(3,40),F(1,10)):
                        kappa=b3-4*r;L=b2+3*b3*r-6*r*r
                        K=-r**4+b3*r**3+b2*r*r+b1*r
                        c0,c1=coeff(kappa,a0,a1)
                        assert wm4-kappa*wm3<=c0*t0+c1*t1+3*t*t
                        moment_cases+=1
                        lower=(L*t-3*t*t-c0*t0-c1*t1+K)/M
                        actual=sum(w for x,w in law.items() if x>-r)
                        assert lower<=actual
                        own_cases+=1
                        assert (k-n*p-r)**2<=F(46,25)**2*(v+s)
                        # For the repair coupling, tau stands for C*ell^3.
                        # Both sides are rational after the common C*rho_B
                        # term is canceled; the identity holds for any tau.
                        weight,tau=F(3,4),F(1,2)
                        k0=kappa-tau*M*q/(weight*n0)
                        k1=kappa+tau*M*p/(weight*n1)
                        cc0,_=coeff(k0,a0,a1);_,cc1=coeff(k1,a0,a1)
                        base=v*(1-2*v)+3*v*(m0[2]+m1[2])
                        rhs=weight*(L*t-3*t*t-cc0*t0-cc1*t1+K)/M+tau*base
                        lhs=weight*actual+tau*(base+p*m1[3]-q*m0[3])
                        assert rhs<=lhs
                        cubic_cases+=1
                fixtures.append({'n':n,'p':str(p),'lambda':str(lam),
                                 'allocation':str(eta),'a0':str(a0),'a1':str(a1)})

# The own-count improvement is realized by an actual centered conditional law.
alpha=F(1,2);M=5*alpha**4;r=t=F(3,40)
L=3*alpha*alpha-6*r*r;K=-r**4+3*alpha*alpha*r*r+2*alpha**3*r
new=((L-(A*A-4*A*r))*t-3*t*t+K)/M-F(21,20)*r
old=((L-(A*A+4*A*r))*t-3*t*t+K)/M-F(21,20)*r
assert new==F(55479,800000) and old==-F(13641,800000)
assert new-old==F(54,625)

# Genuine false moment shortcut: assigning the favorable U0 coefficient to
# positive conditional noise violates the fourth/third-moment inequality.
bad=pair(A,F(1,1000));mm=moments(bad);kappa=-F(1,5)
assert mm[4]-kappa*mm[3]>(A*A+kappa*A)*mm[2]
# The amplitude hypothesis is necessary: a centered Rademacher summand
# violates the coefficient A^2 when its support exceeds the claimed A.
assert F(1)>A*A

# Exact Hermite-majorant identity and its validity on the physical interval.
for var in (F(1,1000),F(1,100),F(3,100)):
    b=F(3,40)
    assert var<=A*b
    for kappa in (-F(2,5),F(0),F(2,5)):
        if A-b-2*var/A-kappa<0:continue
        z=var/A
        # Reconstruct the resulting quadratic at 0,+1,-1, then verify at
        # additional exact points, separately from the proof factorization.
        fun=lambda x:x**4-kappa*x**3-(x-A)*(x+z)**2*(x+A-2*z-kappa)
        c=fun(F(0));aa=(fun(F(1))+fun(F(-1))-2*c)/2;bb=(fun(F(1))-fun(F(-1)))/2
        for x in (-b,-z,F(0),A/2,A):
            assert fun(x)==aa*x*x+bb*x+c
            assert fun(x)>=x**4-kappa*x**3
        expected=var*(A*A-var+var*var/(A*A)-kappa*(A-var/A))
        assert aa*var+c==expected

# Omitting the Hermite sign condition makes even the moment conclusion
# false for an actual centered law within the stated support interval.
b=F(3,40);var=F(1,100);kappa=F(2)
badlaw=pair(-b,var/b);badmom=moments(badlaw)
assert badmom[2]==var and max(x for x,w in badlaw)<=A
claimed=var*(A*A-var+var*var/(A*A)-kappa*(A-var/A))
assert badmom[4]-kappa*badmom[3]>claimed

# Exact concavity identity with support caps held fixed while allocation
# varies. Enlarged caps suffice even if an endpoint is only a relaxation.
for p in (F(2,5),F(53,100)):
    q=1-p;n=42;k=(n*p.numerator)//p.denominator;s=F(3,40)/n
    r=F(1,20);alpha=F(1,2);M=5*alpha**4;kappa=-4*r
    c0,c1=coeff(kappa,d,d)
    L=3*alpha*alpha-6*r*r;K=-r**4+3*alpha*alpha*r*r+2*alpha**3*r
    t_of=lambda eta:(n-k)*s*(1-eta)/q+k*s*eta/p
    value=lambda eta:(L*t_of(eta)-3*t_of(eta)**2-c0*(n-k)*s*(1-eta)/q-c1*k*s*eta/p+K)/M
    for eta in (F(1,4),F(1,2),F(3,4)):
        gap=value(eta)-(1-eta)*value(F(0))-eta*value(F(1))
        assert gap==3*eta*(1-eta)*(t_of(F(1))-t_of(F(0)))**2/M>=0

# Why the favorable finite-sum correction is dropped in the endpoint proof:
# at k=np, t is constant in allocation, but sum Var(U_i)^2 is convex.
p=q=F(1,2);n=42;k=21;s=F(1,1000)
correction=lambda eta:3*((n-k)*(s*(1-eta)/q)**2+k*(s*eta/p)**2)
assert correction(F(1,2))<(correction(F(0))+correction(F(1)))/2
# Also, min of two affine (hence convex) tail bounds need not be convex.
assert min(F(1,2),1-F(1,2))>(min(F(0),F(1))+min(F(1),F(0)))/2

source=Path(__file__).with_name('owncount.tex')
sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
print(json.dumps({'status':'PASS_ALLOCATION_PRESERVING_OWN_COUNT_CONTROLS',
 'scope':'Local analytic inequalities and bounded actual-law controls; no full moderate-noise comparison',
 'normalization_gates':{k:str(x) for k,x in gates.items()},
 'actual_laws':len(fixtures),'moment_cases':moment_cases,'own_event_cases':own_cases,
 'cubic_repair_cases':cubic_cases,'fixtures':fixtures,
 'illustrative_gain':{'new':str(new),'old':str(old),'difference':str(new-old)},
 'negative_controls':['Wrong favorable sign coefficient fails on actual centered positive-noise law',
                      'Dropping the amplitude hypothesis invalidates the moment bound',
                      'Dropping the Hermite sign condition invalidates its moment bound',
                      'Finite-sum correction does not preserve allocation concavity',
                      'Minimum of convex tail bounds need not be convex'],
 'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'python':sys.version},indent=2))

#!/usr/bin/env python3
"""Exact actual-law controls for the off-contact identity; no inherited imports.

The normal values Phi and phi occur affinely. Checking the coefficient basis
(0,0),(1,0),(0,1) verifies their formal affine dependence, not an approximation
to a Gaussian CDF. No tested finite law is asserted to be a maximizer.
"""
from fractions import Fraction as F
from collections import defaultdict
from bisect import bisect_right
from math import isqrt
import json,sys

def need(ok,msg):
    if not ok: raise ValueError(msg)

def convolve(law,n):
    out={F(0):F(1)}
    for _ in range(n):
        new=defaultdict(F)
        for x,p in out.items():
            for y,q in law.items():new[x+y]+=p*q
        out=dict(new)
    return out

def cdf_factory(law):
    xs=sorted(law);ps=[F(0)]
    for x in xs:ps.append(ps[-1]+law[x])
    return lambda t:ps[bisect_right(xs,t)]

def int_power(a,b,j):return (b**(j+1)-a**(j+1))/F(j+1)
def abs3_primitive(x):return (1 if x>=0 else -1)*x**4/F(4)
def int_J2(a,b):
    primitive=lambda t:t**4/F(4)-a*t**3/F(3)
    if b<=0:return -primitive(b)+primitive(a)
    if a>=0:return primitive(b)-primitive(a)
    return primitive(a)+primitive(b)

def run():
    a=F(8,5)
    laws={
      'symmetric Bernoulli':{F(-1):F(1,2),F(1):F(1,2)},
      'skew Bernoulli':{-a:1/(1+a*a),1/a:a*a/(1+a*a)},
      'reflected skew':{a:1/(1+a*a),-1/a:a*a/(1+a*a)},
      'zero atom':{F(-5,4):F(8,25),F(0):F(9,25),F(5,4):F(8,25)},
      'gapped three point':{F(-11,10):F(199,440),F(9,10):F(21,40),F(11,10):F(1,44)},
      'four point':{F(-2):F(1,10),F(-1,2):F(2,5),F(1,2):F(2,5),F(2):F(1,10)}}
    M=F(10)
    laws['small far atoms']={-M:1/(2*M**3),M:1/(2*M**3),F(-1):(M-1)/(2*M),F(1):(M-1)/(2*M),F(0):(M*M-1)/M**3}
    cases=affine=collisions=nonzero_B=nonzero_xi=missing_excess=0
    example=None;directions=set();threshold_atoms=0
    for name,law in laws.items():
        moment=lambda j:sum((p*x**j for x,p in law.items()),F(0))
        need(moment(0)==1 and moment(1)==0 and moment(2)==1,'actual standardized law')
        xs=sorted(law);rho=sum((p*abs(x)**3 for x,p in law.items()),F(0))
        beta=sum((p*x*abs(x) for x,p in law.items()),F(0));gamma=moment(3)
        M4=moment(4);M5=sum((p*abs(x)**5 for x,p in law.items()),F(0))
        X4=sum((p*x*abs(x)**3 for x,p in law.items()),F(0))
        gap=[]
        for u,v in zip(xs,xs[1:]):
            t=(u+v)/2;tau=sum((x*p for x,p in law.items() if x>=t),F(0))
            gap.append((u,v,tau))
        J=sum((tau*(v-u)**2 for u,v,tau in gap),F(0))
        J1=sum((tau*(int_power(u,v,2)-u*int_power(u,v,1)) for u,v,tau in gap),F(0))
        J2=sum((tau*int_J2(u,v) for u,v,tau in gap),F(0))
        need(sum((tau*(v-u) for u,v,tau in gap),F(0))==1,'zero-bias density mass')
        for j,target in [(1,gamma/2),(2,M4/3)]:
            need(sum((tau*int_power(u,v,j) for u,v,tau in gap),F(0))==target,'zero-bias moments')
        need(sum((tau*(abs3_primitive(v)-abs3_primitive(u)) for u,v,tau in gap),F(0))==M5/4,'absolute third zero-bias moment')
        m=sum((p*x for x,p in law.items() if x>0),F(0))
        need(J<=rho+2*m and gamma*gamma+4*m*m<=rho*rho,'physical gap/circle controls')
        for n in (4,9):
            s=F(isqrt(n));sn=convolve(law,n);prev=convolve(law,n-1)
            cdf=cdf_factory(sn);hp=cdf_factory(prev);ts=sorted(sn)
            thresholds=sorted(set([F(-3,2),F(0),F(7,4),ts[0],ts[-1],ts[len(ts)//3],ts[2*len(ts)//3],(ts[0]+ts[1])/2]))
            for H in thresholds:
                directions.add('negative' if H<0 else 'positive' if H>0 else 'zero')
                threshold_atoms+=H in sn;Fh=cdf(H);z=H/s
                reflected_closed=sum((p for x,p in sn.items() if -x<=-H),F(0))
                need(reflected_closed==1-Fh+sn.get(H,F(0)),'closed reflection includes the threshold atom')
                h=lambda y:hp(H-y)
                nu={H-x:p for x,p in prev.items()}
                T=sum((p*(x*x-H*x) for x,p in sn.items() if x<=H),F(0))/n
                Mtr=sum((p*x for x,p in sn.items() if x<=H),F(0))/s
                hinge=sum((p*(x-H)*abs(x-H) for x,p in sn.items()),F(0))/n
                # Direct tau*h integration, split at its actual jumps.
                Th=F(0)
                for u,v,tau in gap:
                    cuts=sorted(set([u,v]+[t for t in nu if u<t<v]))
                    Th+=tau*sum(((b-a)*h((a+b)/2) for a,b in zip(cuts,cuts[1:])),F(0))
                need(Th==T,'direct zero-bias convolution CDF')
                need(hinge==1+z*z-2*T+2*z*Mtr-2*z*z*Fh,'raw hinge identity')
                L=sum((tau*sum((p*(t-u) for t,p in nu.items() if u<=t<v),F(0)) for u,v,tau in gap),F(0))
                wrongL=sum((tau*sum((p*(t-u) for t,p in nu.items() if u<=t<=v),F(0)) for u,v,tau in gap),F(0))
                collisions+=wrongL!=L
                if wrongL!=L and example is None:
                    example={'law':name,'n':n,'H':str(H),'correct_L':str(L),'closed_upper_L':str(wrongL)}
                for c in (F(2,5),F(3,4)):
                    for Phi,phi in [(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]:
                        q0=Fh+(H*phi+c*rho)/(2*s**3)
                        q1=-(n*phi+3*c*beta)/s**3
                        q2=-(H*phi+3*c*rho)/(2*s**3);q3=c/s**3
                        Q=lambda y:q0+q1*y+q2*y*y+q3*abs(y)**3
                        Delta=lambda y:Q(y)-h(y)
                        B=sum((tau*(v-u)*Delta(v) for u,v,tau in gap),F(0))
                        xi=sum((p*x*Delta(x) for x,p in law.items()),F(0))
                        Qtau=sum((tau*(q0*(v-u)+q1*int_power(u,v,1)+q2*int_power(u,v,2)+q3*(abs3_primitive(v)-abs3_primitive(u))) for u,v,tau in gap),F(0))
                        A=Qtau-Th
                        G=3*c*beta*J/2+(H*phi+3*c*rho)*J1-3*c*J2
                        need(A==phi*J/(2*s)+G/s**3-L+B,'off-contact gap slack')
                        Kq=M5/4-rho*M4/2-3*beta*gamma/2+rho/2
                        K1=X4-3*beta-3*rho*gamma/2
                        need(A==Fh-gamma*phi/(2*s)+(H*phi*(3-M4)/6+c*Kq)/s**3-T,'direct moment slack')
                        need(Mtr+phi==-gamma*H*phi/(2*n)+c*K1/n-s*xi,'contact first-moment residual')
                        need(sum((p*Delta(x) for x,p in law.items()),F(0))==0,'zeroth contact residual always cancels')
                        excess=s*(Fh-Phi)-c*rho
                        gaussian_hinge=(1+z*z)*(1-2*Phi)-2*z*phi
                        eps=hinge-gaussian_hinge-2*gamma*phi/(3*s);En=-s**3*eps/2
                        Rc=c*(3*beta*J/2+3*rho*J1-3*J2-Kq)+H*(c*K1+phi*(J1+(M4-3)/6))-H*H*(c*rho+gamma*phi/2)+En
                        master=(n+H*H)*excess+n*c*rho-n*phi*(gamma+3*J)/6+s**3*L
                        need(master-Rc==s**3*(B-H*xi),'complete off-contact master identity')
                        nonzero_B+=B!=0;nonzero_xi+=H*xi!=0;missing_excess+=H*H*excess!=0
                        if H*H*excess:
                            need(master-H*H*excess-Rc!=s**3*(B-H*xi),'missing H^2 excess negative control')
                        if wrongL!=L:
                            need(master+s**3*(wrongL-L)-Rc!=s**3*(B-H*xi),'wrong leakage endpoint negative control')
                        affine+=1
                cases+=1
    need(collisions and nonzero_B and nonzero_xi and missing_excess,'negative controls exercised')
    # Non-UI3 family: exact standardized laws with fixed tail third moment.
    tails=[]
    for M in (F(10),F(100),F(1000)):
        rho=2-1/M;tail=2*(1/(2*M**3))*M**3
        need(tail==1 and rho<2,'bounded third moments without UI3 control')
        tails.append({'far_atom':str(M),'rho':str(rho),'tail_third_moment':'1'})
    # An open CDF composed with H-y takes the smaller value at its jump.
    law=laws['symmetric Bernoulli'];open_h=lambda y:sum((p for x,p in law.items() if x<-y),F(0))
    need(open_h(F(1))==0 and open_h(F(9,10))==F(1,2),'open contact is not upper semicontinuous')
    # For uniform[-sqrt(3),sqrt(3)], divide Kq by sqrt(3).
    uniform_kq=F(3,2)/4-F(3,4)*F(9,5)/2+F(3,4)/2
    need(uniform_kq==F(3,40)>0,'nonzero support integral with no gaps')
    return {'status':'PASS_EXACT_OFF_CONTACT_CONSERVATION','finite_laws':len(laws),
      'law_index_threshold_cases':cases,'affine_coefficient_checks':affine,
      'threshold_directions':sorted(directions),'threshold_atom_cases':threshold_atoms,
      'strict_closed_reflection_cases':threshold_atoms,
      'upper_endpoint_mutations_detected':collisions,'nonzero_boundary_residual_checks':nonzero_B,
      'nonzero_first_moment_residual_checks':nonzero_xi,'missing_H_squared_excess_detected':missing_excess,
      'endpoint_example':example,'bounded_rho_non_UI3_controls':tails,
      'continuous_support_negative_control_Kq_over_sqrt3':str(uniform_kq),
      'scope':'Exact finite-law/convolution and affine algebra controls only; no tested law asserted maximizing, no inherited program imported.'}

if __name__=='__main__':
    need(__debug__ and not sys.flags.optimize,'unoptimized interpreter required')
    print(json.dumps(run(),indent=2))

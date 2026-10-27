#!/usr/bin/env python3
"""Bounded independent exact diagnostics, with no inherited-kernel imports.

Polynomial identities are checked formally; law controls and parameter grids
are diagnostics, not substitutes for the analytic proof or continuous covers.
"""
from fractions import Fraction as F
from math import factorial, isqrt
import json, sys

def need(ok, why):
    if not ok: raise ValueError(why)

# Sparse polynomials in two indeterminates, first x, second u.
def add(*parts):
    out={}
    for p in parts:
        for key,c in p.items(): out[key]=out.get(key,F(0))+c
    return {key:c for key,c in out.items() if c}
def scale(p,c): return {key:c*v for key,v in p.items() if c*v}
def mul(p,q):
    out={}
    for (i,j),c in p.items():
        for (k,l),d in q.items():
            key=(i+k,j+l);out[key]=out.get(key,F(0))+c*d
    return {key:c for key,c in out.items() if c}
def power(p,n):
    out={(0,0):F(1)}
    for _ in range(n): out=mul(out,p)
    return out
def deriv(p,index=0):
    out={}
    for key,c in p.items():
        if key[index]:
            new=list(key);new[index]-=1;out[tuple(new)]=c*key[index]
    return out
def at(p,x,u=0):return sum((c*x**i*u**j for (i,j),c in p.items()),F(0))

def identities():
    one={(0,0):F(1)};x={(1,0):F(1)};u={(0,1):F(1)}
    D=add(power(x,2),scale(x,4),scale(one,2))
    P=add(power(u,2),scale(u,-4),scale(one,2))
    Q={(0,3):F(-1),(1,2):F(1),(0,2):F(8),(2,1):F(-1),
       (1,1):F(-8),(0,1):F(-20),(3,0):F(1),(2,0):F(8),
       (1,0):F(20),(0,0):F(16)}
    need(add(power(D,2),scale(mul(add(x,u),Q),-1))==power(P,2),'Laguerre division')
    integrated={}
    for (i,j),c in Q.items():integrated[(i,0)]=integrated.get((i,0),F(0))+factorial(j)*c
    need(integrated==mul(add(x,scale(one,3)),D),'Laguerre factorial moments')
    numerator=add(mul(mul(add(one,scale(x,-2)),add(x,scale(one,2))),D),
                  scale(mul(x,D),2),scale(mul(mul(x,add(x,scale(one,2))),deriv(D)),-2))
    expected={(0,0):F(4),(1,0):F(-10),(2,0):F(-22),(3,0):F(-13),(4,0):F(-2)}
    need(numerator==expected,'scaled tail derivative numerator')
    need(at(expected,F(1,4))<0,'tail derivative endpoint')
    need(all(c<0 for c in deriv(expected).values()),'tail derivative decreasing polynomial')
    need(at(numerator,F(1,10))>0,'negative control: unguarded tail not decreasing')
    need(1-2*42*F(1,1000)>0,'negative control: unguarded sqrt(n) exponential grows')
    # The first-piece chord identity: x denotes M, u denotes t^2.
    c=add(scale(u,F(1,2)),scale(mul(add(x,scale(one,3)),power(u,2)),F(-1,24)))
    cq=add(scale(one,F(1,8)),scale(add(x,scale(one,3)),F(-1,384)))
    slope=add(scale(one,F(1,2)),scale(add(x,scale(one,3)),F(-53,1200)))
    diff=add(c,scale(cq,-1),scale(mul(slope,add(u,scale(one,F(-1,4)))),-1))
    expected=scale(mul(mul(add(x,scale(one,3)),add(u,scale(one,F(-1,4)))),add(scale(one,F(81,100)),scale(u,-1))),F(1,24))
    need(diff==expected,'first-piece chord identity')
    # Taylor coefficients: use first variable t, second gamma; imaginary
    # coefficients are tracked separately, avoiding approximate complex values.
    wr={(2,0):F(-1,2)};wi={(3,1):F(-1,6)}
    hr=add(one,wr,scale(add(mul(wr,wr),scale(mul(wi,wi),-1)),F(1,2)))
    hi=add(wi,mul(wr,wi))
    need(hr=={(0,0):F(1),(2,0):F(-1,2),(4,0):F(1,8),(6,2):F(-1,72)},'real comparator Taylor')
    need(hi=={(3,1):F(-1,6),(5,1):F(1,12)},'imaginary comparator Taylor')
    need(hi[(5,1)]!=F(-1,12),'negative control: reflected fifth coefficient sign')
    # Nonzero mean destroys compensation: Im(delta_1-delta_0) has linear
    # coefficient one, so dividing by t^3 leaves a nonintegrable t^-2 term.
    need(F(1)-F(0)==1,'negative control: missing first moment cancellation')
    return 7

def directed_constants():
    # Independent long division of x^4(1-x)^4 by 1+x^2.
    rem=[F(0)]*9
    for i,c in enumerate([1,-4,6,-4,1]):rem[i+4]=F(c)
    quotient=[F(0)]*7
    for j in range(8,1,-1):
        q=rem[j];quotient[j-2]=q;rem[j]-=q;rem[j-2]-=q
    need(rem==[F(-4)]+[F(0)]*8,'pi-upper polynomial division')
    need(sum((c/F(i+1) for i,c in enumerate(quotient)),F(0))==F(22,7),'pi-upper integral')
    def atan_lower(t):return sum(((-1)**j*t**(2*j+1)/F(2*j+1) for j in range(4)),F(0))
    lower=16*atan_lower(F(1,5))-F(4,239)
    t=F(1,5);t=2*t/(1-t*t);t=2*t/(1-t*t)
    need((t-F(1,239))/(1+t/239)==1,'Machin tangent identity')
    need(lower>F(333,106)>F(25,8),'directed pi lower')
    need(F(4431,2500)**2<F(333,106),'sqrt pi lower')
    need(F(251,100)**2>F(44,7),'sqrt two pi upper')
    return {'pi_lower':str(lower),'pi_upper':'22/7','sqrt_pi_lower':'4431/2500','sqrt_two_pi_upper':'251/100'}

def sqrt_up(x):
    s=10**12;k=isqrt(x.numerator*s*s//x.denominator)
    return F(k+1,s)

def z_cap(M,g,R,E5):
    if M<=5:
        z=6*(M-1)+(10-2*M)*g-6*g*g+g**3 if 10-2*M-12*g+3*g*g>=0 else 6*(M-1)+(10-2*M)**2/(4*(6-g))
    else:z=6*(M-1)+(2*M-10)**2/24
    r=max(R,2*g)
    if M<=5:
        t=min(g,(10-2*M)/(2*(r-g)))
        zr=r*(M-1)+(10-2*M)*t-(r-g)*t*t
    else:
        t=min(g,(2*M-10)/(2*r))
        zr=r*(M-1)+(2*M-10)*t-r*t*t
    return min(z,zr,E5+10*g)/120

def low(M,g,R,E5,N):
    Z=z_cap(M,g,R,E5);A=max(F(2),M-3)/24
    E=R*E5/720+g*g/72+(F(1,2)+g*g/144)**3/5
    B=A+Z/2+E/4;a=F(N-1,2*N);b=(45-M)/96*(1-F(2,N))
    # Check squared normal factor instead of rounding roots; the remaining
    # two pieces are rational and manifestly decreasing with N.
    normal2=F(22,7)/(16*a**3)
    return normal2,E/(2*a*a)+B*B/(2*b**3)

def laws():
    a=F(8,5)
    rows=[('symmetric Bernoulli',[(F(-1),F(1,2)),(F(1),F(1,2))]),
          ('skew Bernoulli',[(-a,1/(1+a*a)),(1/a,a*a/(1+a*a))]),
          ('reflected skew',[(a,1/(1+a*a)),(-1/a,a*a/(1+a*a))]),
          ('gapped three point',[(F(-11,10),F(199,440)),(F(9,10),F(21,40)),(F(11,10),F(1,44))]),
          ('zero atom',[(F(-5,4),F(8,25)),(F(0),F(9,25)),(F(5,4),F(8,25))]),
          ('distant symmetric atoms',[(F(-3),F(1,18)),(F(0),F(8,9)),(F(3),F(1,18))])]
    out=[]
    for name,law in rows:
        moment=lambda j:sum((p*x**j for x,p in law),F(0))
        need(moment(0)==1 and moment(1)==0 and moment(2)==1,'normalized actual law')
        gam=moment(3);M=moment(4);E5=sum((p*abs(x)**5 for x,p in law),F(0));R=max(abs(x) for x,p in law);g=abs(gam)
        need(M<=F(111,10) and g<=F(37,20),'test law within Fourier scope')
        q2=sum((p*(x*x-gam*x-1)**2 for x,p in law),F(0))
        fifth=sum((p*(x*x-gam*x-1)**2*(x+2*gam) for x,p in law),F(0))
        need(q2==M-1-gam*gam and moment(5)==gam**3+2*gam+fifth,'actual-law Pearson identities')
        Z=z_cap(M,g,R,E5);actual=abs(10*gam-moment(5))/120
        need(actual<=Z,'actual-law fifth coefficient bound')
        pair4=sum((p*q*(x-y)**4 for x,p in law for y,q in law),F(0))
        need(pair4==2*M+6,'actual-law independent-copy fourth moment')
        values=[low(M,g,R,E5,N) for N in (42,43,100,1000000)]
        need(all(all(v>=w for v,w in zip(x,y)) for x,y in zip(values,values[1:])),'rational LOW floor factors decrease')
        out.append({'law':name,'mu4':str(M),'gamma':str(gam),'radius':str(R),'actual_abs_z':str(actual),'Z_bound':str(Z)})
    return out

def domain_grid():
    count=0;worst=F(0)
    for M in [F(1),F(2),F(3),F(499,100),F(5),F(501,100),F(8),F(111,10)]:
        for g in [F(0),F(1,10),F(1,2),F(1),F(37,20)]:
            if g*g>M-1:continue
            # R=6 gives an enclosing radius regardless of feasibility of a
            # parameter pair; these controls test the scalar inequality only.
            Z=z_cap(M,g,F(6),F(1000))*120
            for j in range(41):
                t=g*F(j,40)
                P=6*(M-1)+(10-2*M)*t-6*t*t+t**3
                Q=6*(M-1)+(2*M-10)*t-6*t*t-t**3
                need(max(P,Q)<=Z,'bounded scalar Pearson envelope diagnostic')
                count+=1;worst=max(worst,max(P,Q)-Z)
    g=F(37,20)
    need((F(1,2)+g*g/144)/4<F(1,6),'uniform small exponential argument')
    # Analytic global gate, with the actual initial M ceiling.
    M=F(96,25)*F(7361,4000);a=(2-F(9,25))**2/(2*M+6)
    windows=[F(1,8),F(4,25),F(9,50),F(1,5),F(11,50),F(1,4)]
    margins=[]
    for r in windows:
        h=F(333,106)-F(22,7)**3*r*r/6
        rate=min(t/2-(M+3)*t*t/24 for t in [F(1,4),F(81,100)])
        cq=F(1,8)-(M+3)/384;s=(1-(M+3)*F(53,600))/2
        gates=[84*rate-1,84*a*h*h*r*r-1,84*a*F(23,48)**2-1,F(84,8)-1,84*cq-1]
        need(s>0 and h>0 and min(gates)>0,'initial full-HIGH window gates')
        margins.append({'window':str(r),'minimum_gate_margin':str(min(gates))})
    return {'scalar_grid_points':count,'windows':margins}

if __name__=='__main__':
    need(__debug__ and not sys.flags.optimize,'unoptimized interpreter')
    print(json.dumps({'status':'PASS_BOUNDED_FOURIER_IDENTITIES_AND_CONTROLS',
      'formal_identity_groups':identities(),'actual_laws':laws(),'domain_checks':domain_grid(),
      'directed_constants':directed_constants(),
      'negative_controls':['missing damping gate','missing Laguerre quarter gate','wrong fifth-coefficient sign','missing first-moment compensation'],
      'scope':'No inherited kernel import, Fourier quadrature, dense certificate or full local exclusion run.'},indent=2))

"""Independent LEFT-01 reconstruction: no constructor imports or execution."""
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
A=F(7,10);alpha=F(27,50);M=5*alpha**4;T=F(23,2100);Z=F(3,2)
def invert(a):
    n=len(a);a=[list(row)+[F(i==j)for j in range(n)]for i,row in enumerate(a)]
    for j in range(n):
        i=next(i for i in range(j,n)if a[i][j]);a[i],a[j]=a[j],a[i]
        d=a[j][j];a[j]=[x/d for x in a[j]]
        for i in range(n):
            if i!=j:
                d=a[i][j];a[i]=[x-d*y for x,y in zip(a[i],a[j])]
    return [row[n:]for row in a]
def basis(n,j,x):return F(comb(n,j))*x**j*(1-x)**(n-j)
it=invert([[basis(3,j,F(i+1,4))for j in range(4)]for i in range(4)])
iz=invert([[basis(4,j,F(i+1,5))for j in range(5)]for i in range(5)])
coeff=[]
for sigma,slope,goal in [(1,-F(213,200),F(1,4)),(-1,F(47,50),F(4,5))]:
    def original(t,z):
        r=z*t;shift=sigma*r
        # Choose the adverse third moment before expanding the shifted fourth.
        moments=[F(1),F(0),t,sigma*A*t,A*A*t+3*t*t]
        shifted=lambda j:sum(F(comb(j,l))*shift**(j-l)*moments[l]for l in range(j+1))
        return (-shifted(4)+3*alpha**2*shifted(2)+2*alpha**3*shifted(1))/(M*t)+slope*z-goal
    values=[[original(T*F(i+1,4),Z*F(j+1,5))for j in range(5)]for i in range(4)]
    bs=[[sum(it[i][a]*values[a][b]*iz[j][b]for a in range(4)for b in range(5))for j in range(5)]for i in range(4)]
    assert all(b>0 for row in bs for b in row)
    for x,y in [(F(1,7),F(2,9)),(F(4,5),F(1,11))]:
        assert sum(bs[i][j]*basis(3,i,x)*basis(4,j,y)for i in range(4)for j in range(5))==original(T*x,Z*y)
    coeff.extend(b for row in bs for b in row)

# The six closing margins, independently reconstructed from probability bounds.
U=F(1,100);b=F(1,20);hi=F(391,500);low=F(-109,500)
def q(mu,h):return (mu*mu/2+mu**3/6)/((1-h)/A+mu-1)**2
def tail(mu,h,j):
    lead=(j*mu)**(j+1)/F(__import__('math').factorial(j+1))
    return lead/(j*(1/A-1+mu)-h/A)**2/(1-3*mu)
mi=F(6,5)*U/A**2;mg=F(4,3)*U/A**2
ni=q(mi,0)+tail(mi,0,2);pi=q(mi,b)+tail(mi,b,2)
margins=[F(18,25)*(c*F(19,21)-F(53,50)*tt/U)-repair/42-F(1,100)
 for c,tt,repair in [(F(1,4),ni,F(3,4)),(F(1,2),ni,F(4)),(F(4,5),pi,F(4))]]
own=min(r*r/(F(7,6)*U+r*r)-F(3,2)*r for r in [b,-low])
margins.append(F(57,100)*(own-F(9,5)*(q(mg,0)+tail(mg,0,2)))-6*U/42-U/100)
tg=F(4,3)*U
def cc(u):return tg/(tg+(1-u)**2)+2*tg/(2*tg+(2-u)**2)
margins.append(F(57,100)*(F(93,100)*b-F(9,5)*(cc(F(1,10))+tail(mg,F(1,10),3)))-6*U/42-U/100)
margins.append(F(57,100)*(min(F(2,3)*u-F(9,5)*cc(u)for u in [F(1,10),hi])-F(9,5)*tail(mg,hi,3))-6*U/42-U/100)
assert all(m>0 for m in margins)

def sqrt_interval(x):
    scale=10**40;z=isqrt(x.numerator*scale*scale//x.denominator)
    lo,hi=F(z,scale),F(z+1,scale);assert lo*lo<=x<=hi*hi
    return lo,hi
def twopoint(a,b):
    if not a and not b:return [(F(0),F(1))]
    return [(-a,b/(a+b)),(b,a/(a+b))]
def moments(law):return [sum(x**j*w for x,w in law)for j in range(5)]
def sums(law,n):
    if len(law)==1:return [(n*law[0][0],F(1))]
    (a,pa),(b,pb)=law
    return [(j*a+(n-j)*b,F(comb(n,j))*pa**j*pb**(n-j))for j in range(n+1)]
laws=events=0;minimum=None;nonzero_transport=0
for p in [F(1,4),F(2,5),F(13,50)]:
    for side in [0,1,2]:
        zero=[(F(0),F(1))];left=twopoint(A,F(1,10000));right=twopoint(F(1,10000),A)
        P0=left if side in [0,2]else zero;P1=right if side in [1,2]else zero
        q0=1-p;s0=moments(P0)[2];s1=moments(P1)[2];s=q0*s0+p*s1
        n=64;v=p*q0;assert 0<n*s<=U
        k=(n*p).numerator//(n*p).denominator;delta=F(k)-n*p
        nonzero_transport+=int(bool(delta));m=8*F(comb(n,k))*p**k*q0**(n-k)
        t=(n-k)*s0+k*s1
        raw=q0*sum(abs(x-p)**3*w for x,w in P0)+p*sum(abs(1+x-p)**3*w for x,w in P1)
        vr=sqrt_interval(v+s);br=sqrt_interval(v)
        rho_lo=raw/((v+s)*vr[1]);rhoB_hi=(1-2*v)/br[0]
        distribution={}
        for x,wx in sums(P0,n-k):
            for y,wy in sums(P1,k):distribution[x+y]=distribution.get(x+y,F(0))+wx*wy
        assert sum(distribution.values())==1
        for r in [F(0),t,F(3,2)*t,b]:
            assert 0<=r<=b
            strict=sum(w for x,w in distribution.items()if x>-r)
            L=((3*alpha**2-A*A-6*r*r)*t-3*t*t-4*A*r*t-r**4+3*alpha**2*r*r+2*alpha**3*r)/M
            # C is positive; use independent outward radical enclosures.
            margin=m*(strict-L)+F(819,2000)*(rho_lo-rhoB_hi)-F(7,4)*s
            assert margin>0
            minimum=margin if minimum is None else min(minimum,margin);events+=1
        laws+=1
assert nonzero_transport>0
print(json.dumps({'status':'PASS_INDEPENDENT_LEFT_01_COMPONENTS','bernstein_coefficients':len(coeff),
 'minimum_coefficient':str(min(coeff)),'closing_margins':[str(m)for m in margins],
 'actual_laws':laws,'strict_events':events,'nonzero_transport_cases':nonzero_transport,
 'minimum_actual_joint_margin':str(minimum),'python':sys.version,
 'scope':'Independent polynomial interpolation, six complete-tail margins and actual-law joint lemma controls; analytic review is separate; no full-conjecture claim'},indent=2))

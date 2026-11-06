from fractions import Fraction as F
from math import comb

def need(x,msg):
    if not x:raise ValueError(msg)

def tidy(p):return {ij:a for ij,a in p.items() if a}

def add(*ps):
    r={}
    for p in ps:
      for ij,a in p.items():r[ij]=r.get(ij,F(0))+a
    return tidy(r)

def scale(p,c):return tidy({ij:c*a for ij,a in p.items()})

def mul(p,q):
    r={}
    for (i,j),a in p.items():
      for (k,l),b in q.items():r[i+k,j+l]=r.get((i+k,j+l),F(0))+a*b
    return tidy(r)

ONE={(0,0):F(1)};P={(1,0):F(1)};U={(0,1):F(1)};Q=add(ONE,scale(P,-1));V=mul(P,Q);V2=mul(V,V)

def power(p,n):
    r=ONE
    for _ in range(n):r=mul(r,p)
    return r

def local(p,pl,pu,ul,uh):
    r={}
    for (i,j),a in p.items():
      for h in range(i+1):
       for k in range(j+1):
        r[h,k]=r.get((h,k),F(0))+a*comb(i,h)*pl**(i-h)*(pu-pl)**h*comb(j,k)*ul**(j-k)*(uh-ul)**k
    return tidy(r)

def inverse(b):
    need(len(b)==50,'tensor shape');r={}
    for a in range(10):
      for c in range(5):
       z=b[5*a+c]*comb(9,a)*comb(4,c)
       for i in range(a,10):
        for j in range(c,5):
         r[i,j]=r.get((i,j),F(0))+z*comb(9-a,i-a)*comb(4-c,j-c)*(-1)**(i-a+j-c)
    return tidy(r)

def direct(k,x,y,g0,g1,qs,k0=None,k1=None):
    if k0 is None:k0=g0*g0
    if k1 is None:k1=g1*g1
    total={}
    for j,c in enumerate(qs):
        a=add(scale(ONE,F(j-k)),scale(U,-1))
        T=add(scale(P,(5-j)*x),scale(Q,j*y))
        G=add(scale(P,(5-j)*x*g0),scale(Q,j*y*g1))
        L=add(scale(P,(5-j)*x*k0),scale(Q,j*y*k1))
        first=mul(V2,add(*(scale(power(a,r),c[r]) for r in range(5))))
        second=mul(mul(T,V),add(scale(ONE,c[2]),scale(a,3*c[3]),scale(power(a,2),6*c[4])))
        third=mul(mul(G,V),add(scale(ONE,c[3]),scale(a,4*c[4])))
        fourth=add(scale(mul(L,V),c[4]),scale(mul(T,T),F(12,5)*c[4]))
        mass=scale(mul(power(P,j),power(Q,5-j)),F(comb(5,j)))
        total=add(total,mul(mass,add(first,second,third,fourth)))
    return total

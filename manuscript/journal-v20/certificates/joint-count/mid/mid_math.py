"""Exact univariate arithmetic for fixed quartic proof objects (stdlib only)."""
from fractions import Fraction as F
from math import comb

def trim(p):
    p=list(p)
    while len(p)>1 and not p[-1]:p.pop()
    return p or [F(0)]
def add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for i,v in enumerate(p):r[i]+=v
    for i,v in enumerate(q):r[i]+=v
    return trim(r)
def scale(p,c):return trim([c*x for x in p])
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return trim(r)
def power(p,n):
    r=[F(1)]
    for _ in range(n):r=mul(r,p)
    return r
def affine(p,a,b):
    r=[F(0)]
    for i,v in enumerate(p):r=add(r,scale(power([a,b],i),v))
    return r
def compact_ray(p):
    # (1-y)^4 p(y/(1-y)), with p in the nonnegative ray coordinate.
    assert len(p)<=5
    r=[F(0)]
    for i,v in enumerate(p):r=add(r,scale(mul([F(0)]*i+[F(1)],power([F(1),F(-1)],4-i)),v))
    return r
def evaluate(p,x):return sum((v*x**i for i,v in enumerate(p)),F(0))

C=F('9819/10000');A=F('17/40');R0=F('53421/50000')
LF=F('86879/100000');HF=F('113121/100000')
TL=F('18319/20000')/20;TU=F('21681/20000')*F('2/25')
ETA=F('1/10');M=9

def targets(q,b):
    right=compact_ray(add(affine(q,b,F(1)),[F(1)]))
    intervals=[add(affine(q,b-C*m,-C),[-R0*m]) for m in range(M)]
    left=compact_ray(add(affine(q,b-C*M,-C),[-R0*M,-R0]))
    return [right]+intervals+[left]

def loss_gates(q,a):
    flo=(LF if a>=0 else HF)*a
    lin=q[2]+A*abs(q[3])+A*A*q[4]+ETA
    return [-(q[0]-flo+lin*t+3*q[4]*t*t)for t in (TL,TU)]

def bernstein_forward(p,a,b):
    z=affine(p,a,b-a)
    return [sum((z[j]*F(comb(i,j),comb(4,j))for j in range(min(i,len(z)-1)+1)),F(0))for i in range(5)]

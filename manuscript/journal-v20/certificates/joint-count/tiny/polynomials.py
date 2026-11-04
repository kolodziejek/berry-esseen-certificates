"""Small exact two-variable polynomial operations and Bernstein conversion."""
from fractions import Fraction as F
from math import comb

def scalar(x):
    x=F(x)
    return {(0,0):x} if x else {}

X={(1,0):F(1)}
Y={(0,1):F(1)}

def add(*ps):
    r={}
    for p in ps:
        for k,v in p.items():r[k]=r.get(k,F(0))+v
    return {k:v for k,v in r.items() if v}

def scale(p,x):
    return {k:v*F(x) for k,v in p.items() if v*F(x)}

def mul(a,b):
    r={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():r[i+k,j+l]=r.get((i+k,j+l),F(0))+v*w
    return {k:v for k,v in r.items() if v}

def power(p,n):
    r=scalar(1)
    for _ in range(n):r=mul(r,p)
    return r

def sub(p,x,y):
    out={}
    for (i,j),v in p.items():out=add(out,scale(mul(power(x,i),power(y,j)),v))
    return out

def evaluate(p,x,y):
    return sum((v*F(x)**i*F(y)**j for (i,j),v in p.items()),F(0))

def bernstein(p,box):
    xl,xh,yl,yh=box
    q=sub(p,add(scalar(xl),scale(X,xh-xl)),add(scalar(yl),scale(Y,yh-yl)))
    nx=max((i for i,j in p),default=0);ny=max((j for i,j in p),default=0)
    return [[sum((q.get((i,j),F(0))*F(comb(k,i),comb(nx,i))*F(comb(l,j),comb(ny,j))
                  for i in range(k+1) for j in range(l+1)),F(0))
             for l in range(ny+1)] for k in range(nx+1)]

def split(box,axis):
    a=list(box);b=list(box);mid=(box[2*axis]+box[2*axis+1])/2
    a[2*axis+1]=mid;b[2*axis]=mid
    return tuple(a),tuple(b)

def encode(p):
    return [[i,j,str(v)] for (i,j),v in sorted(p.items())]

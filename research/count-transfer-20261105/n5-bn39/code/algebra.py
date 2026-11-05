"""Exact primitives copied from accepted V4, with three unchanged native modules."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
from functools import lru_cache
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('unoptimized exact Python required')
HERE=Path(__file__).resolve().parent
def need(x,msg):
    if not x:raise ValueError(msg)

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def unique(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,'duplicate JSON key');d[k]=v
    return d
PINS={'quartic_sturm.py':'1f815ccb23692f78be98691a76a5fe0605f8995abdab5d9a3964f1625a4c2617',
'quartic_global.py':'0760d772b6cf1858ed139a1fe179490cb1e523a5d685a37a25271a10b349aa35',
'finite_binomial_core.py':'939236711b080f9148ee3d3f7f6a0cd15b86cb24f3d2700f0e7127b2a345291f'}
for name,pin in PINS.items():need(sha(HERE/'native'/name)==pin,'fixed native source '+name)
sys.path.insert(0,str(HERE/'native'))
import quartic_sturm as sturm
import finite_binomial_core as normal
DEGP=9;DEGU=4
def rational(s):
    need(type(s)is str,'rational data must be strings');v=F(s)
    need(str(v)==s,'canonical rational string');return v

def add(a,b):
    return tuple((a[i]if i<len(a)else F(0))+(b[i]if i<len(b)else F(0))for i in range(max(len(a),len(b))))

def scale(a,c):return tuple(x*c for x in a)

def mul(a,b):
    r=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
      for j,y in enumerate(b):r[i+j]+=x*y
    return tuple(r)

def power(a,n):
    r=(F(1),)
    for _ in range(n):r=mul(r,a)
    return r

def evaluate(a,x):
    r=F(0)
    for c in reversed(a):r=r*x+c
    return r

@lru_cache(maxsize=2048)
def bernstein(a,l,h,d):
    need(len(a)<=d+1 and l<h,'degree and nondegenerate Bernstein interval')
    local=[sum(a[j]*comb(j,i)*l**(j-i)*(h-l)**i for j in range(i,len(a)))for i in range(d+1)]
    return tuple(sum(local[j]*F(comb(i,j),comb(d,j))for j in range(i+1))for i in range(d+1))

def compact_ray(q,sign,subtract):
    q=list(q);q[0]-=subtract;r=[F(0)]*5
    for j,a in enumerate(q):
      for h in range(5-j):r[j+h]+=a*sign**j*comb(4-j,h)*(-1)**h
    return tuple(r)

def normal_lower(num,den):
    lo,hi=normal.root(den)
    if num>=0:
        z=num/hi;idx=z.numerator*normal.Z//z.denominator
        need(0<=idx<=5*normal.Z,'normal range');return F(normal.positive_cdf(idx)[0],normal.S)
    z=-num/lo;idx=-((-z.numerator*normal.Z)//z.denominator)
    need(0<=idx<=5*normal.Z,'normal range');return 1-F(normal.positive_cdf(idx)[1],normal.S)
P=(F(0),F(1));Q=(F(1),-F(1));V=mul(P,Q);V2=mul(V,V)

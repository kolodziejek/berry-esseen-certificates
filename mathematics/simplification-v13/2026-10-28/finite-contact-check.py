#!/usr/bin/env python3
"""Bounded exact controls for the v13 finite contact/moment-path note.

No inherited checker is imported. Convolution coefficients and direct iid
products are evaluated by different loops. This is not a full C4 certificate.
"""
from fractions import Fraction as Q
from itertools import product, combinations_with_replacement
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
checks = []
rejections = []

def require(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def rejected(name, call):
    try:
        call()
    except (AssertionError, ValueError):
        rejections.append(name)
        return
    raise AssertionError('negative control was accepted: ' + name)

def polysum(a,b):
    out = [Q(0)] * max(len(a),len(b))
    for j,v in enumerate(a): out[j] += v
    for j,v in enumerate(b): out[j] += v
    return out

def polymul(a,b):
    out = [Q(0)] * (len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b): out[j+k] += x*y
    return out

def peval(a,t):
    ans = Q(0)
    for x in reversed(a): ans = ans*t+x
    return ans

def vector_rank(rows):
    a = [[Q(x) for x in row] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(rank,len(a)) if a[j][col]),None)
        if pivot is None: continue
        a[rank],a[pivot] = a[pivot],a[rank]
        p = a[rank][col]
        a[rank] = [x/p for x in a[rank]]
        for j in range(len(a)):
            if j != rank:
                p = a[j][col]
                a[j] = [x-p*y for x,y in zip(a[j],a[rank])]
        rank += 1
    return rank

z = tuple(map(Q,[-2,-1,0,1,2]))
p = (Q(1,20),Q(1,5),Q(1,2),Q(1,5),Q(1,20))
v = tuple(map(Q,[1,-2,0,2,-1]))
rows = [[Q(1) for x in z],list(z),[x*x for x in z],[abs(x)**3 for x in z]]
require('moment rank is four',vector_rank(rows)==4)
require('moment null vector',all(sum(a*b for a,b in zip(row,v))==0 for row in rows))
require('moment values', [sum(a*b for a,b in zip(row,p)) for row in rows]==[1,0,Q(4,5),Q(6,5)])
lo=max(-a/b for a,b in zip(p,v) if b>0)
hi=min(-a/b for a,b in zip(p,v) if b<0)
require('complete feasible segment',(lo,hi)==(Q(-1,20),Q(1,20)))
require('interior positive weights',all(a>0 for a in p))
require('endpoint zero atom and positive remainder',all(sum(a+t*b==0 for a,b in zip(p,v))==1 for t in [lo,hi]))
require('standardized rho squared ceiling',Q(45,16)<Q(46,25)**2)
require('standardized support ceiling',5<Q(504,125)**2)
require('standardized beta ceiling',Q(1,4)<Q(641,1000))
require('positive discrepancy elementary ceiling',5<Q(23,10)**2)
require('signed third is not preserved',sum(x**3*w for x,w in zip(z,v))==-12)

# Polynomial convolution of the common marginal: all four factors are equal.
dist={Q(0):[Q(1)]}
for _ in range(4):
    nxt={}
    for s,a in dist.items():
        for x,b,c in zip(z,p,v):
            nxt[s+x]=polysum(nxt.get(s+x,[]),polymul(a,[b,c]))
    dist=nxt
coeff=[Q(0)]*5
for s,a in dist.items():
    if s<=1: coeff=polysum(coeff,a)
expected=[Q(25719,32000),Q(-103,2000),Q(-483,200),Q(-123,5),Q(11)]
require('complete quartic coefficients',coeff==expected)
require('probability mass polynomial',sum((a[0] for a in dist.values()),Q(0))==1 and all(sum(a[j] for a in dist.values())==0 for j in range(1,5)))

def iid_event(points,weights,threshold,n=4,closed=True):
    ans=Q(0)
    for ids in product(range(len(points)),repeat=n):
        total=sum(points[i] for i in ids)
        if total<threshold or (closed and total==threshold):
            mass=Q(1)
            for i in ids: mass*=weights[i]
            ans+=mass
    return ans

def law_at(t): return tuple(a+t*b for a,b in zip(p,v))
for t in [lo,Q(-1,40),Q(-1,100),Q(0),Q(1,100),hi]:
    require('direct iid product equality at '+str(t),iid_event(z,law_at(t),Q(1))==peval(coeff,t))
require('left endpoint CDF',peval(coeff,lo)==Q(4017,5000))
require('right endpoint CDF',peval(coeff,hi)==Q(7921,10000))
require('left endpoint strict gap',coeff[0]-peval(coeff,lo)==Q(51,160000))
require('right endpoint strict gap',coeff[0]-peval(coeff,hi)==Q(1859,160000))
require('positive discrepancy lower bound',coeff[0]>Q(4,5))
derivative=[(j+1)*coeff[j+1] for j in range(4)]
require('cubic derivative factor',derivative==[x/Q(2000) for x in polymul([1,20],[-103,-7600,4400])])
require('quadratic derivative strictly negative',8800*hi-7600<0)
require('interior maximizer derivative bracket',peval(derivative,Q(-1,40))>0 and peval(derivative,Q(-1,100))<0)
require('radical root bracket',Q(190)+Q(220,100)<Q(386,2) and (Q(190)+Q(220,100))**2<37233<(Q(190)+Q(220,40))**2)
require('nonconvexity at origin',2*coeff[2]==Q(-483,100))

# Recover every multilinear coefficient independently, using signed product laws.
A=[]
for j in range(5):
    total=Q(0)
    for ids in product(range(5),repeat=4):
        if sum(z[i] for i in ids)<=1:
            value=Q(1)
            for k,i in enumerate(ids): value*=v[i] if k<j else p[i]
            total+=value
    A.append(total)
require('multilinear binomial expansion',all(comb(4,j)*A[j]==coeff[j] for j in range(5)))
K=[[iid_event(z,p,Q(1)-x-y,n=2) for y in z] for x in z]
quad=sum(v[i]*v[j]*K[i][j] for i in range(5) for j in range(5))
require('same-law Hessian identity',quad==A[2]==Q(-161,400))
require('first variation is nonzero at origin',A[1]==Q(-103,8000))

# Occupancy hypergraphs, independently compared with ordered actual iid sums.
def occupations(points,H):
    return [ids for ids in combinations_with_replacement(range(len(points)),4) if sum(points[i] for i in ids)==H]

def collision_vertices(points,H):
    sums3={sum(xs) for xs in product(points,repeat=3)}
    return {i for i,x in enumerate(points) if H-x in sums3}

def occupation_vertices(active): return {i for ids in active for i in ids}

families=[
    ('symmetric Bernoulli',(Q(-1),Q(1)),(Q(1,2),Q(1,2))),
    ('skew Bernoulli',(Q(-1),Q(2)),(Q(2,3),Q(1,3))),
    ('three points',(Q(-2),Q(0),Q(1)),(Q(1,4),Q(1,4),Q(1,2))),
    ('nearby four points',(Q(-2),Q(-199,100),Q(1),Q(199,200)),(Q(1,6),Q(1,6),Q(1,3),Q(1,3))),
    ('five point moment interior',z,p),
    ('tiny remote atom',(Q(-1),Q(0),Q(100)),(Q(1,2),Q(99,200),Q(1,200))),
]
collision_cases=0
for name,points,weights in families:
    require(name+' is an actual mean-zero law',sum(weights)==1 and all(w>0 for w in weights) and sum(x*w for x,w in zip(points,weights))==0)
    sums=sorted({sum(xs) for xs in product(points,repeat=4)})
    # All exact sum atoms and immediate rational midpoints: finite and bounded.
    thresholds=sums+[(a+b)/2 for a,b in zip(sums,sums[1:])]
    for H in thresholds:
        active=occupations(points,H)
        require(name+' collision incidence '+str(H),collision_vertices(points,H)==occupation_vertices(active))
        if active:
            require(name+' closed atom positive '+str(H),iid_event(points,weights,H)>iid_event(points,weights,H,closed=False))
        else:
            require(name+' empty collision unchanged '+str(H),iid_event(points,weights,H)==iid_event(points,weights,H,closed=False))
        collision_cases+=1

powers=tuple(Q(5)**j for j in range(7))
all_occ=list(combinations_with_replacement(range(7),4))
require('seven-point base-five support has distinct four-sums',len({sum(powers[i] for i in ids) for ids in all_occ})==len(all_occ))
active=occupations(powers,Q(4))
require('one active repeated-atom multiset',active==[(0,0,0,0)])
require('six nonresonant atoms without contact',len(powers)-len(collision_vertices(powers,Q(4)))==6)
# Centering preserves the entire occupancy incidence relation.
mean=sum(powers)/7
centered=tuple(x-mean for x in powers)
require('actual centered seven-point law',sum(centered)==0)
require('centered contact-omission control',occupations(centered,4-4*mean)==active)
require('actual threshold atom in omission control',iid_event(centered,(Q(1,7),)*7,4-4*mean)==Q(1,7**4))

# The potential lemma has a sharp two-minimum example, including the curvature boundary.
def cubic_potential(x): return abs(x)**3-x*x
require('two strict minima example equal values',cubic_potential(Q(-2,3))==cubic_potential(Q(2,3))==Q(-4,27))
require('curvature boundary cannot be counted as minimum',cubic_potential(Q(1,3)-Q(1,100))>cubic_potential(Q(1,3))>cubic_potential(Q(1,3)+Q(1,100)))

# Negative controls are mathematical errors rather than changes to accepted targets.
def assert_true(x): assert x
rejected('endpoint-only moment maximization',lambda:assert_true(coeff[0]<=max(peval(coeff,lo),peval(coeff,hi))))
rejected('convexity of iid objective on moment segment',lambda:assert_true(2*coeff[2]>=0))
rejected('dropping closed threshold atoms',lambda:assert_true(iid_event(z,p,Q(1),closed=False)==coeff[0]))
rejected('forgetting binomial factor in second variation',lambda:assert_true(A[2]==coeff[2]))
rejected('signed third moment claimed fixed',lambda:assert_true(sum(x**3*w for x,w in zip(z,v))==0))
rejected('contact omitted from nonresonance conclusion',lambda:assert_true(len(powers)-len(collision_vertices(powers,Q(4)))<=2))
rejected('at most one local minimum claimed',lambda:assert_true(cubic_potential(Q(-2,3))!=cubic_potential(Q(2,3))))
rejected('endpoint probabilities extended past feasible interval',lambda:assert_true(all(a>=0 for a in law_at(hi+Q(1,1000)))))

def validate_fixture(points,base,direction):
    assert tuple(points)==z and tuple(base)==p and tuple(direction)==v
rejected('missing fixture atom',lambda:validate_fixture(z[:-1],p[:-1],v[:-1]))
rejected('duplicate fixture atom',lambda:validate_fixture(z+(z[-1],),p+(p[-1],),v+(v[-1],)))
rejected('reordered fixture without co-permutation',lambda:validate_fixture(tuple(reversed(z)),p,v))
rejected('corrupt fixture mass',lambda:validate_fixture(z,(p[0]+Q(1,1000),)+p[1:],v))

files=[HERE/'finite-contact.tex',Path(__file__).resolve(),ROOT/'manuscript/arxiv-v1/sections/02-fixed-target.tex',ROOT/'mathematics/fixed-target-v7/2026-10-27/base-audit.md',ROOT/'mathematics/fixed-target-v8/2026-10-28/root4-bridge.tex']
print(json.dumps({'result':'PASS','scope':'finite moment path and conditional contact/collision lemmas only; not C4','exact_checks':len(checks),'collision_cases':collision_cases,'negative_controls':rejections,'quartic_coefficients':list(map(str,coeff)),'endpoint_gaps':['51/160000','1859/160000'],'source_sha256':{str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}},indent=2))

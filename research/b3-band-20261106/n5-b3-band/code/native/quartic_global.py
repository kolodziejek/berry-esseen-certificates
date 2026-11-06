"""Exact global quartic majorants of a closed conditional-count staircase.

Discovery constructs Bernstein leaves; acceptance independently expands their
Bernstein polynomials and compares exact power coefficients. No numerical
probability or unproved moment bound is included in this small checker.
"""
from fractions import Fraction as F
from math import comb
import json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('unoptimized Python required')
DEGREE=4

def need(v,s):
    if not v:raise ValueError(s)
def rational(x):
    need(type(x)in(int,str,F),'exact rational representation required')
    return F(x)
def add(a,b):return [(a[i]if i<len(a)else F(0))+(b[i]if i<len(b)else F(0))for i in range(max(len(a),len(b)))]
def mul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z
def power(a,n):
    z=[F(1)]
    for _ in range(n):z=mul(z,a)
    return z
def affine(a,l,w):
    z=[F(0)]*5
    for j,v in enumerate(a):
        for h in range(j+1):z[h]+=v*comb(j,h)*l**(j-h)*w**h
    return z
def compact_ray(a):
    # (1-t)^4 P(t/(1-t)), including its polynomial endpoint at t=1.
    z=[F(0)]*5
    for j,v in enumerate(a):
        for h in range(5-j):z[j+h]+=v*comb(4-j,h)*(-1)**h
    return z

def parameters(q,phase_upper,c,R0,J):
    need(type(q)in(list,tuple)and len(q)==5,'five ascending quartic coefficients')
    q=list(map(rational,q));u,c,R=map(rational,(phase_upper,c,R0))
    need(q[4]>=0,'globally convex second derivative q4>=0')
    need(c>0 and R>=0 and type(J)is int and J>=1,'staircase parameters')
    return q,u,c,R,J

def fixed_targets(q,u,c,R,J):
    targets=[]
    # Right open ray needs q>=-1; the finite j0 interval separately supplies
    # q(u)>=0. Imposing both at their shared closed endpoint is safe.
    right=affine(q,u,F(1));right[0]+=1
    targets.append(('right-ray',compact_ray(right)))
    for j in range(J):
        low=u-(j+1)*c;high=u-j*c
        p=affine(q,low,high-low);p[0]-=R*j
        targets.append(('step-'+str(j),p))
    left=affine(q,u-J*c,F(-1));left[0]-=R*J;left[1]-=R/c
    targets.append(('left-ray',compact_ray(left)))
    return targets

def bernstein(a):
    # Forward transform used by discovery only.
    return [sum((a[j]*F(comb(k,j),comb(4,j))for j in range(k+1)),F(0))for k in range(5)]
def split(b):
    levels=[list(b)]
    for _ in range(4):levels.append([(x+y)/2 for x,y in zip(levels[-1],levels[-1][1:])])
    return [r[0]for r in levels],[r[-1]for r in reversed(levels)]
def propose_tree(a,maxdepth,maxnodes):
    stack=[('',bernstein(a))];leaves=[];nodes=0
    while stack:
        path,b=stack.pop();nodes+=1
        need(nodes<=maxnodes,'discovery node budget exhausted')
        if min(b)>=0:leaves.append({'path':path,'bernstein':list(map(str,b))});continue
        need(len(path)<maxdepth,'unproved positivity at dyadic path '+path)
        l,r=split(b);stack.append((path+'1',r));stack.append((path+'0',l))
    return leaves

def metadata(q,u,c,R,J):
    return {'q':list(map(str,q)),'phase_upper':str(u),'c':str(c),'R0':str(R),'J':J}
def build(q,phase_upper,c,R0,J=8,maxdepth=22,maxnodes=200000):
    q,u,c,R,J=parameters(q,phase_upper,c,R0,J)
    need(type(maxdepth)is int and 0<=maxdepth<=30 and type(maxnodes)is int and maxnodes>=1,'finite discovery limits')
    return {'schema':'CLOSED_STAIRCASE_GLOBAL_QUARTIC_V1','parameters':metadata(q,u,c,R,J),
      'targets':[{'name':name,'leaves':propose_tree(p,maxdepth,maxnodes)}for name,p in fixed_targets(q,u,c,R,J)]}

def inverse_bernstein(b):
    # Independent expansion: sum b_j binom(4,j)t^j(1-t)^(4-j).
    out=[F(0)]*5
    for j,bj in enumerate(b):
        term=mul([F(0)]*j+[bj*comb(4,j)],power([F(1),F(-1)],4-j))
        out=add(out,term)
    return out

def accept_tree(leaves,target):
    need(type(leaves)is list and len(leaves)>0,'nonempty positivity forest')
    paths=[]
    for leaf in leaves:
        need(type(leaf)is dict and set(leaf)=={'path','bernstein'},'exact leaf fields')
        s=leaf['path'];need(type(s)is str and len(s)<=30 and set(s)<=set('01'),'dyadic path')
        need(type(leaf['bernstein'])is list and len(leaf['bernstein'])==5,'five Bernstein coefficients')
        b=list(map(rational,leaf['bernstein']));need(min(b)>=0,'nonnegative Bernstein coefficients')
        lo=F(int(s,2),2**len(s))if s else F(0);width=F(1,2**len(s))
        need(inverse_bernstein(b)==affine(target,lo,width),'independent exact polynomial reconstruction')
        paths.append(s)
    need(paths==sorted(paths)and len(set(paths))==len(paths),'ordered unique leaves')
    # Recursive consumption requires exactly both children at every split.
    position=0
    def visit(prefix):
        nonlocal position
        need(position<len(paths),'missing branch')
        if paths[position]==prefix:position+=1;return
        need(paths[position].startswith(prefix)and len(prefix)<30,'incomplete or overlapping dyadic cover')
        visit(prefix+'0');visit(prefix+'1')
    visit('');need(position==len(paths),'extra overlapping leaves')
    return len(paths)

def accept(obj,q,phase_upper,c,R0,J=8):
    q,u,c,R,J=parameters(q,phase_upper,c,R0,J)
    need(type(obj)is dict and set(obj)=={'schema','parameters','targets'},'fixed object fields')
    need(obj['schema']=='CLOSED_STAIRCASE_GLOBAL_QUARTIC_V1','fixed schema')
    need(json.dumps(obj['parameters'],sort_keys=True,separators=(',',':'))==json.dumps(metadata(q,u,c,R,J),sort_keys=True,separators=(',',':')),'exact externally supplied target parameters')
    targets=fixed_targets(q,u,c,R,J);need(type(obj['targets'])is list and len(obj['targets'])==len(targets),'all finite intervals and both rays')
    count=0
    for row,(name,p)in zip(obj['targets'],targets):
        need(type(row)is dict and set(row)=={'name','leaves'}and row['name']==name,'ordered fixed target names')
        count+=accept_tree(row['leaves'],p)
    return {'status':'PASS_EXACT_GLOBAL_QUARTIC_MAJORANT','targets':len(targets),'leaves':count,'coefficients':5*count,
      'scope':'q(w)>=-1{w>u}+R0*floor((u-w)/c)_+ for every real w and every phase u<=phase_upper; q second derivative globally convex',
      'probabilistic_claim':False}

#!/usr/bin/env python3
"""Instrument selected acceptance; independently reconstruct scalar Fourier maps.

This checks correspondence of formulas proved in fourier-audit.md and runtime
arguments. It is not an independent proof of support acquisition or acceptance.
Pinned files are read only; no source modification or optimized Python is used.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt, factorial
from functools import lru_cache
from hashlib import sha256
import importlib.util, json, platform, sys, time

assert __debug__ and not sys.flags.optimize
sys.dont_write_bytecode = True
ROOT=Path('/Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/manuscript_revision_20261029')
V5=ROOT/'mathematics/fixed-target-v5/2026-10-27'
V7=ROOT/'mathematics/fixed-target-v7/2026-10-27'
sys.path[:0]=[str(V7),str(V5/'cell-sources')]
import kernel, high_window_core, accept_entry

def floor(x,s): return F((x*s).__floor__(),s)
def ceil(x,s): return F((x*s).__ceil__(),s)
def sqrtbox(x):
    s=10**8
    r=isqrt((x*s*s).__floor__())
    lo,hi=F(r,s),F(r+1,s)
    assert lo*lo<=x<=hi*hi
    return lo,hi
@lru_cache(None)
def expupper(x):
    assert x>=0
    y=floor(min(x,F(64)),10**6)
    denominator=sum((y**j/factorial(j) for j in range(65)),F(0))
    assert denominator>0
    return ceil(1/denominator,10**14)

@lru_cache(None)
def low_exact(N,M,g,E5,R):
    assert 42<=N and 1<=M<=F(111,10) and 0<=g<=F(37,20)
    assert F(23,10)<=R<=6 and E5>0
    A=max(F(2),M-3)/24
    r=max(R,2*g)
    if M<=5:
        t=min(g,(10-2*M)/(2*(r-g)))
        radius_bound=r*(M-1)+(10-2*M)*t-(r-g)*t*t
        six_bound=(6*(M-1)+(10-2*M)*g-6*g*g+g**3
                   if 10-2*M-12*g+3*g*g>=0
                   else 6*(M-1)+(10-2*M)**2/(4*(6-g)))
    else:
        t=min(g,(2*M-10)/(2*r))
        radius_bound=r*(M-1)+(2*M-10)*t-r*t*t
        six_bound=6*(M-1)+(2*M-10)**2/24
    Z=min(radius_bound,six_bound,E5+10*g)/120
    E=R*E5/720+g*g/72+(F(1,2)+g*g/144)**3/5
    B=A+Z/2+E/4
    a=F(N-1,2*N);b=F(45-M,96)*(1-F(2,N))
    norm=sqrtbox(F(22,7)/(16*a**3))[1]
    return (norm*(Z+A*g/2)+F(251,17280)*g**3,
            norm*A+F(251,4800)*g*g,
            E/(2*a*a)+B*B/(2*b**3))

gate_min={}
def gate(name,x):
    assert x>0,(name,x)
    gate_min[name]=min(x,gate_min.get(name,x))

@lru_cache(None)
def high_exact(N,alpha,ME,d,M,r):
    assert N>=42 and 0<alpha<=1 and ME>0 and 0<d<=12
    assert 1<=M<=F(111,10) and 0<r<=F(1,4)
    p,ps=F(333,106),F(4431,2500)
    b=F(9,10); h=p-F(22,7)**3*r*r/6
    gate('h',h)
    c=lambda u:u/2-(M+3)*u*u/24
    rate=min(c(F(1,4)),c(b*b))
    kap=alpha*F(23,48)**2*d*d
    for name,q in [('first',rate),('wings',alpha*h*h*r*r),
                   ('zero_far',alpha*F(23,48)**2),('comparator',F(1,8))]:
        gate(name+'_positive',q);gate(name+'_monotonic',2*N*q-1)
    nl,nu=sqrtbox(F(N))
    first=2*nu*expupper(N*rate)
    slope=(1-(M+3)*F(53,600))/2
    if slope>0:
        cq=c(F(1,4));gate('chord_monotonic',2*N*cq-1)
        x=N*slope/4
        first=min(first,2*nu*expupper(N*cq)*(x+2)/(x*x+4*x+2))
    x=N*kap*b*b
    zero=expupper(x)/(2*b**4*kap*nl)
    if x>=F(1,4):
        zero=min(zero,nu*expupper(x)*(x+2)/(2*b*b*(x*x+4*x+2)))
    s3=sum((F(1,j**3) for j in range(1,21)),F(1,800))
    s5=sum(((F(j)-r)**-5 for j in range(1,21)),1/(4*(20-r)**4))
    xc=F(N,8)
    terms=(first,
           ME*(s3+3*s5/(N*alpha*h*h))/(4*p*ps*h*sqrtbox(alpha)[0]),
           ME*nu*expupper(N*alpha*h*h*r*r)/(2*p*p),
           zero,
           nu*expupper(N*alpha*F(23,48)**2)/(2*b*b),
           nu*expupper(xc)*(2*(xc+2)/(xc*xc+4*xc+2)+sqrtbox(M-1)[1]/3))
    assert len(terms)==6 and min(terms)>0
    return ceil(sum(terms),10**10),terms

counts={'LOW_calls':0,'HIGH_complete_calls':0,'HIGH_minimum_calls':0}
radii=set()
oldlow=kernel.sixth
def checked_low(N,M,g,E5):
    counts['LOW_calls']+=1;R=kernel.RADIUS;radii.add(R)
    answer=oldlow(N,M,g,E5)
    assert answer==low_exact(N,M,g,E5,R)
    return answer
kernel.sixth=checked_low
oldinstall=high_window_core.install
def checked_install(target=kernel):
    one,best=oldinstall(target)
    def checked_one(*args):
        counts['HIGH_complete_calls']+=1
        answer=one(*args)
        assert answer==high_exact(*args)
        return answer
    def checked_best(N,a,m,d,M,window):
        counts['HIGH_minimum_calls']+=1
        answer=best(N,a,m,d,M,window)
        alternatives=[high_exact(N,a,m,d,M,w) for w in
                      (window,F(1,8),F(4,25),F(9,50),F(1,5),F(11,50),F(1,4))]
        assert answer==min(alternatives,key=lambda z:z[0])
        return answer
    target.high=checked_best
    return checked_one,checked_best
high_window_core.install=checked_install

start=time.monotonic()
proof=(V7/'entry-proof.json').read_bytes()
out=accept_entry.verify(json.loads(proof,object_pairs_hook=accept_entry.unique))
inputs=[V7/'accept_entry.py',V7/'entry-proof.json',V7/'signed_core.py',
        V7/'signed_support.py',V5/'cell_check.py',V5/'cell-sources/kernel.py',
        V5/'cell-sources/high_window_core.py',
        ROOT/'manuscript/compact-v16/appendices/fixed-fourier.tex']
report={'status':'PASS_FOURIER_RUNTIME_FORMULA_MAPPING',
        'python':sys.version,'platform':platform.platform(),'optimized':sys.flags.optimize,
        'elapsed_seconds':time.monotonic()-start,'source_root':str(ROOT),
        'input_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in inputs},
        'counts':counts,'unique_LOW_inputs':low_exact.cache_info().currsize,
        'unique_HIGH_inputs':high_exact.cache_info().currsize,
        'radii':sorted(radii),'minimum_exact_gate_margins':gate_min,
        'acceptance_status':out['status'],'acceptance_summary':out['summary'],
        'scope':'Runtime correspondence with the separately derived scalar formulas, not an independent proof of the acquisition hypotheses.'}
print(json.dumps(accept_entry.encode(report),indent=2))

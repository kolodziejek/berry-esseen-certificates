"""Exact strict global quartic staircase acceptance with compact witnesses.

Only the five coefficients are proof data. The fixed degree<=4 positivity
problems are rebuilt, and rational Sturm sequences are recomputed exactly.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,importlib.util,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('unoptimized Python required')
HERE=Path(__file__).resolve().parent
TARGET_PIN='0760d772b6cf1858ed139a1fe179490cb1e523a5d685a37a25271a10b349aa35'
source=HERE/'quartic_global.py'
if hashlib.sha256(source.read_bytes()).hexdigest()!=TARGET_PIN:raise ValueError('fixed staircase target source hash')
spec=importlib.util.spec_from_file_location('fixed_quartic_staircase_targets',source)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
need=base.need

def trim(p):
    p=list(p)
    while p and p[-1]==0:p.pop()
    return p

def derivative(p):return trim([j*p[j]for j in range(1,len(p))])
def evaluate(p,x):
    v=F(0)
    for a in reversed(p):v=v*x+a
    return v

def remainder(a,b):
    a=trim(a);b=trim(b);need(b,'division by nonzero polynomial')
    while len(a)>=len(b):
        d=len(a)-len(b);ratio=a[-1]/b[-1]
        for i,c in enumerate(b):a[d+i]-=ratio*c
        a=trim(a)
    return a

def variation(seq,x):
    signs=[]
    for p in seq:
        v=evaluate(p,x)
        if v:signs.append(1 if v>0 else -1)
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def positive(p):
    p=trim(list(map(base.rational,p)));need(p and len(p)<=5,'nonzero degree at most four')
    p0=evaluate(p,F(0));p1=evaluate(p,F(1))
    need(p0>0 and p1>0,'strictly positive interval endpoints')
    d=derivative(p)
    if not d:return {'degree':0,'sequence_length':1,'variations':[0,0]}
    seq=[p,d]
    while True:
        r=remainder(seq[-2],seq[-1])
        if not r:break
        seq.append([-v for v in r])
        need(len(seq)<=6,'Sturm degree strictly decreases')
    # Sufficient, deliberately conservative. Strictly positive polynomials
    # with a repeated complex root may reject; no false positive is admitted.
    need(len(seq[-1])==1,'squarefree target required by this strict checker')
    v0=variation(seq,F(0));v1=variation(seq,F(1))
    need(v0>=v1,'ordered Sturm root count')
    need(v0==v1,'no real root on the full compact interval')
    return {'degree':len(p)-1,'sequence_length':len(seq),'variations':[v0,v1]}

def accept(q,phase_upper,c,R0,J=8):
    q,u,c,R,J=base.parameters(q,phase_upper,c,R0,J)
    results=[]
    for name,p in base.fixed_targets(q,u,c,R,J):results.append({'name':name,**positive(p)})
    return {'status':'PASS_EXACT_STRICT_GLOBAL_QUARTIC_MAJORANT','parameters':base.metadata(q,u,c,R,J),
      'targets':results,'target_source_sha256':TARGET_PIN,
      'scope':'q(w)>=-1{w>u}+R0*floor((u-w)/c)_+ for all real w and all u<=phase_upper; q second derivative globally convex',
      'probabilistic_claim':False}

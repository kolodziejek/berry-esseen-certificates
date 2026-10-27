#!/usr/bin/env python3
"""Bounded exact polynomial phase enclosures; Fourier estimates remain premises."""
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import hashlib,importlib.util,json,sys

def need(x,msg):
    if not x:raise ValueError(msg)

def value(p,x):
    out=F(0)
    for c in reversed(p):out=out*x+c
    return out

def derivative(p):return [j*p[j] for j in range(1,len(p))]

def bernstein(p,l,u):
    d=len(p)-1
    powers=[sum((p[k]*comb(k,j)*l**(k-j)*(u-l)**j for k in range(j,d+1)),F(0)) for j in range(d+1)]
    return [sum((powers[j]*F(comb(i,j),comb(d,j)) for j in range(i+1)),F(0)) for i in range(d+1)]

def square_root_up(x):
    scale=10**12;k=isqrt(x.numerator*scale*scale//x.denominator)
    result=F(k+1,scale);need(result*result>=x,'directed root');return result

def envelope(A,f,q,b,N):
    need(A>=0 and f>=0 and q>0 and b>0 and type(N) is int and N>0,'phase domain')
    T=A+f*f/(4*q)
    need(T<N*b,'strict full raw gate')
    # degree-six upper bound, valid because r(h)-N*b is strictly negative.
    p=[A,f,-q+(A-N*b)/(2*N),f/(2*N),
       -q/(2*N)+(A-N*b)/(8*N*N),f/(8*N*N),-q/(8*N*N)]
    radius=(f+square_root_up(f*f+4*q*A))/(2*q)
    cap=F(-((-radius.numerator)//radius.denominator))
    need(value([A,f,-q],cap)<=0 and f-2*q*cap<0,'whole exterior excluded by raw bound')
    first,second=derivative(p),derivative(derivative(p))
    # Eight intervals certify concavity; this is not sampled positivity.
    concavity=[max(bernstein(second,cap*F(i,8),cap*F(i+1,8))) for i in range(8)]
    need(max(concavity)<0,'strict continuous polynomial concavity')
    lo,hi=F(0),cap
    need(value(first,lo)>=0 and value(first,hi)<0,'unique stationary root bracket')
    for _ in range(32):
        mid=(lo+hi)/2
        if value(first,mid)>0:lo=mid
        else:hi=mid
    need(value(first,lo)>=0>=value(first,hi),'outward critical bracket')
    stationary=sum((c*(hi if c>=0 else lo)**j for j,c in enumerate(p)),F(0))
    finite=max(A,value(p,cap),stationary)
    infinite=A+f*f/(4*(q+b/2))
    return {'raw':T,'phase_resource':max(finite,infinite),'finite_endpoint':finite,
        'infinite_endpoint':infinite,'stationary_bracket':[lo,hi],
        'threshold_cap':cap,'concavity_maxima':concavity,'polynomial':p}

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def run():
    need(__debug__ and not sys.flags.optimize,'assertions enabled')
    here=Path(__file__).resolve().parent;root=here.parents[2]
    source=root/'mathematics/fixed-target-v5/2026-10-27/cell_check.py'
    need(hashlib.sha256(source.read_bytes()).hexdigest()=='6827a67e64cfea5b89d823ffd34821fa942b3c3add702ee9721c89d65f443aa5','first cover source')
    spec=importlib.util.spec_from_file_location('v5first',source)
    base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    obj=json.loads((source.parent/'cell-input.json').read_text(),object_pairs_hook=base.unique)
    blobs={name:(source.parent/'cell-sources'/name).read_bytes() for name in base.PINS}
    first=base.run(obj,blobs)
    c0,c1=F(obj['c_lower']),F(obj['c_upper']);N=42;rows=[]
    for row in first['rows']:
        endpoints=[]
        for t in (c0,c1):
            A=row['KF']+t*row['A'];f=t*row['K_abs']+row['normal_H_coefficient']+row['slope']
            q=t*row['rho_lower']-row['gamma_abs']/5;b=t*row['rho_lower']
            endpoints.append(envelope(A,f,q,b,N))
        U=max(x['phase_resource'] for x in endpoints)
        old_extra=(c0*row['rho_lower']-row['fixed_raw']/N)/2
        old=max(row['KF']+t*row['A']+(t*row['K_abs']+row['normal_H_coefficient']+row['slope'])**2/
                (4*(t*row['rho_lower']-row['gamma_abs']/5+old_extra)) for t in (c0,c1))
        rows.append({'index':row['index'],'rho_lower':row['rho_lower'],'rho_upper':row['rho_upper'],
            'endpoints':endpoints,'new_U':U,'old_U':old,'D_upper':6*U/(N*F(997,2500))})
    need(len(rows)==24 and all(a['rho_upper']==b['rho_lower'] for a,b in zip(rows,rows[1:])),'complete initial cover')
    need(all(r['new_U']<r['old_U'] for r in rows),'strict component improvement on each cell')
    return {'name':'FULL_PHASE_FIRST_COVER_N42_V1','rows':rows,
       'max_U':max(r['new_U'] for r in rows),'max_D':max(r['D_upper'] for r in rows),
       'cells_D_below4':sum(r['D_upper']<4 for r in rows),
       'scope':'New continuous-n phase lemma and exact polynomials; inherited Fourier inputs conditional.'}

if __name__=='__main__':print(json.dumps(encode(run()),indent=2))

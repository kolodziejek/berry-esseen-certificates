#!/usr/bin/env python3
"""Read-only independent reconstruction and Bernstein verification of v6 output."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import comb,isqrt
from copy import deepcopy
import json,sys
PINS={
 'mathematics/fixed-target-v6/2026-10-27/combined_check.py':'f22a0506d8301fb5c747650443980363b6bc06b47ce8fa6c35fb7eab0bc19d18',
 'mathematics/fixed-target-v6/2026-10-27/phase_check.py':'7f57df7ecd4c35f7e05e79e4dd9940f84a6e4127567efb54c5e38afd2abd3da8',
 'mathematics/fixed-target-v6/2026-10-27/phase.tex':'82db7c78b07b4a20a257390d0dfae82a0bcf4bc7e0500856336da5e073205b5e',
 'mathematics/fixed-target-v6/2026-10-27/signed-check.py':'c827917d18b241d7e6255b3c15184ca719044cc3b7ffb8c7474ea5482dd7a847',
 'mathematics/fixed-target-v6/2026-10-27/moment_check.py':'c44f789c35198eabb2d6d07a3843437c4fa29e9b85ebf79505a3bb696987513f',
 'runs/fixed-target-v6-20261027/combined01/stdout.json':'200cc178bed6400f4a6043aac7f136e38a5cfa02a390c4d3a02971caf5c78dca',
 'runs/fixed-target-v6-20261027/signed02/stdout.json':'3376557f83874f571ed1c7cfad10b82930e736427ba597b5c8ed76b3c46b1944',
 'runs/fixed-target-v5-20261027/cell02/check.stdout.json':'7525713bd06a30b9c13693d01949d4f186890128eed3432771953ef9eafef082'}
N=42;C=(F('.4097321837023'),F('.4097321837025'));PHI=F(997,2500);SIG=F('3.162277660')
def need(ok,s):
    if not ok:raise ValueError(s)
def upper(x):return F(-((-x.numerator*10**10)//x.denominator),10**10)
def lower(x):return F(x.numerator*10**10//x.denominator,10**10)
def root_up(x):
    need(x>=0,'root domain');k=isqrt(x.numerator*10**24//x.denominator)
    lo,hi=F(k,10**12),F(k+1,10**12);need(lo*lo<=x<=hi*hi,'root enclosure');return hi
def val(p,x):return sum(c*x**j for j,c in enumerate(p))
def der(p):return [j*p[j] for j in range(1,len(p))]
def bernstein(p,l,u):
    n=len(p)-1
    shifted=[sum(p[k]*comb(k,j)*l**(k-j)*(u-l)**j for k in range(j,n+1)) for j in range(n+1)]
    return [sum(shifted[j]*F(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def polynomial_certificate(z,b):
    A,f,q=map(F,(z['A'],z['f'],z['q']));need(A>0 and f>=0 and q>0 and b>0,'phase input signs')
    raw=A+f*f/(4*q);need(raw<N*b,'selected polynomial raw gate, not previous minimum')
    need(raw==F(z['raw']),'exact raw maximum')
    # Construct r+(r-Nb)(h²/(2N)+h⁴/(8N²)) by convolution.
    r=[A,f,-q];p=r+[F(0)]*4
    for j,c in enumerate([A-N*b,f,-q]):p[j+2]+=c/(2*N);p[j+4]+=c/(8*N*N)
    need(p==list(map(F,z['polynomial'])),'independent polynomial expansion')
    cap=F(z['threshold_cap']);need(cap>0 and val(r,cap)<=0 and val(der(r),cap)<0,'exterior raw exclusion')
    # Independent finite certificates for -P'' on the full [0,cap].
    minus_second=[-x for x in der(der(p))];subdivisions=None
    for count in (1,2,4,8,16):
        if all(min(bernstein(minus_second,cap*j/count,cap*(j+1)/count))>0 for j in range(count)):
            subdivisions=count;break
    need(subdivisions is not None,'continuous concavity Bernstein certificate')
    lo,hi=map(F,z['stationary_bracket']);dp=der(p)
    need(0<=lo<=hi<=cap and val(dp,0)>=0 and val(dp,cap)<0 and val(dp,lo)>=0>=val(dp,hi),'stationary bracket')
    local_upper=max(bernstein(p,lo,hi))
    own_upper=max(A,val(p,cap),local_upper)
    need(own_upper<=F(z['phase_resource']),'independent Bernstein maximum fits claimed resource')
    infinite=A+f*f/(4*(q+b/2))
    need(infinite==F(z['infinite_endpoint']) and infinite<=F(z['phase_resource']),'infinite endpoint retained or dominated')
    return subdivisions
def verify(out,old,signed):
    need(len(out['rows'])==len(old)==len(signed)==24,'24 complete cells');counts=[]
    for i,row in enumerate(out['rows']):
        l,u=1+F(3361*i,96000),1+F(3361*(i+1),96000)
        need(row['index']==i and F(row['rho_lower'])==l and F(row['rho_upper'])==u,'ordered closed partition')
        need(len(row['steps'])==7,'first pass plus six updates')
        src=old[i];g,b,G,M,KF,slope,vH=map(F,(src['gamma_abs'],src['beta_abs'],src['Gamma'],src['M4'],src['KF'],src['slope'],src['normal_H_coefficient']))
        K=F(signed[i]['effective_K_abs']);need(K>=0,'signed absolute coefficient')
        prior=None
        for j,step in enumerate(row['steps']):
            density=F(0);gl=-g;diff=2*u
            if prior is not None:
                T,d=F(prior['raw']),F(prior['defect']);need(0<T<N*C[0]*l and d>=0,'ordered prior license')
                density=PHI*(1-T/(N*C[0]*l));a=SIG-d/l
                y=F(-1) if a<=-1 else max(F(-1),(a-3*root_up(10-a*a))/10)
                circ=lower(l*y if y>=0 else u*y);gl=max(-g,SIG*l-3-d,circ)
                need(gl<=g,'moment interval retains all cells');diff=min(2*u,(1-SIG)*l+3+d,u-gl)
            need(0<=diff<=2*u,'gap charge direction')
            A=min(F(3,2)*b*(2*u+1)+F(3,2)*G*diff+F(3,8)*u*u*(u+1)+u**3/4-l/2,
                  F(3,2)*b*(2*u+1)+2*u*M-l/2)
            need(F(step['K_abs'])==K and F(step['A'])==A and F(step['gamma_lower'])==gl and F(step['density_lower'])==density,'reconstructed same-law coefficients')
            need(len(step['endpoints'])==2,'both CE endpoints')
            for c,z in zip(C,step['endpoints']):
                q=c*l-g/5
                if prior is not None:q=max(q,c*l+min(density*gl,F(2,5)*gl)/2)
                need(F(z['c'])==c and F(z['A'])==KF+c*A and F(z['f'])==c*K+vH+slope and F(z['q'])==q,'endpoint coefficient reconstruction')
                counts.append(polynomial_certificate(z,c*l))
            T=upper(max(F(z['raw']) for z in step['endpoints']));U=upper(max(F(z['phase_resource']) for z in step['endpoints']))
            if prior is not None:T=min(T,F(prior['raw']));U=min(U,F(prior['resource']))
            d=upper(6*U/(N*PHI));nd=upper(6*U/PHI)
            need([F(step[k]) for k in ('raw','resource','defect','weighted_nD')]==[T,U,d,nd],'ordered rounding and retained minima')
            need(T<N*C[0]*l,'new raw license')
            need(F(step['central_gap_margin'])==(SIG-1)*l-d>0,'strict actual-gap gate')
            need(F(step['central_gap_squared_lower'])==2*(l-d/(SIG-1))>0,'squared gap lower bound')
            prior=step
    first=[r['steps'][0] for r in out['rows']]
    need(max(F(x['raw']) for x in first)<F('13.281891'),'first raw target')
    need(max(F(x['resource']) for x in first)<F('10.796596'),'first resource target')
    need(max(F(x['defect']) for x in first)<F('3.867530')<4,'first defect target')
    return dict(polynomials=len(counts),max_concavity_subdivisions=max(counts),
      first_max_raw=str(max(F(x['raw']) for x in first)),first_max_U=str(max(F(x['resource']) for x in first)),
      first_max_D=str(max(F(x['defect']) for x in first)),
      first_min_gap_margin=str(min(F(x['central_gap_margin']) for x in first)),
      final_max_D=str(max(F(r['steps'][-1]['defect']) for r in out['rows'])))
def main():
    need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'fixed unoptimized invocation');root=Path(sys.argv[1])
    blobs={p:(root/p).read_bytes() for p in PINS}
    for p,h in PINS.items():need(sha256(blobs[p]).hexdigest()==h,'source pin '+p)
    get=lambda p:json.loads(blobs[p])
    out=get('runs/fixed-target-v6-20261027/combined01/stdout.json')
    old=get('runs/fixed-target-v5-20261027/cell02/check.stdout.json')['rows']
    signed=get('runs/fixed-target-v6-20261027/signed02/stdout.json')['rows']
    result=verify(out,old,signed);controls=[]
    for name,mutate in [('missing cell',lambda x:x['rows'].pop()),
       ('altered signed coefficient',lambda x:x['rows'][0]['steps'][0].update(K_abs='0')),
       ('altered phase polynomial',lambda x:x['rows'][0]['steps'][0]['endpoints'][0]['polynomial'].__setitem__(2,'0')),
       ('understated resource',lambda x:x['rows'][0]['steps'][0]['endpoints'][0].update(phase_resource='0')),
       ('false gap margin',lambda x:x['rows'][0]['steps'][0].update(central_gap_margin='1'))]:
        bad=deepcopy(out);mutate(bad)
        try:verify(bad,old,signed)
        except ValueError:controls.append(name)
        else:raise ValueError('bad combined object accepted')
    # A previous tiny bound is deliberately irrelevant to this selected polynomial gate.
    try:polynomial_certificate(dict(A='43',f='0',q='1'),F(1))
    except ValueError:controls.append('unlicensed selected polynomial despite unrelated prior bound')
    else:raise ValueError('unsafe raw gate accepted')
    print(json.dumps(dict(name='INDEPENDENT_COMBINED_V6_REVIEW_V1',results=result,source_pins=PINS,
      rejected_controls=controls,no_shared_checker_or_fourier_execution=True),indent=2))
if __name__=='__main__':main()

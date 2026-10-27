#!/usr/bin/env python3
"""Independent two-pass reconstruction; no constructor/Fourier/phase imports."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from copy import deepcopy
import sys,json
PINS={
 'mathematics/fixed-target-v6/2026-10-27/signed-two-pass-check.py':'a2b9309998191c2d7e4477a969cd55ecb516440f56dfa3cf97df5ccddac1e76d',
 'mathematics/fixed-target-v6/2026-10-27/signed-two-pass-proof/signed-two-pass.tex':'2ff60de4c71461f64213518efcce20831c7d9a28fb60a3c533661e43b1596674',
 'runs/fixed-target-v6-20261027/signed-two-pass02/stdout.json':'c52122bea63beaed83de741a347863a39fb0faeaa34dec5dc4b2741a0a88594a',
 'runs/fixed-target-v6-20261027/signed02/stdout.json':'3376557f83874f571ed1c7cfad10b82930e736427ba597b5c8ed76b3c46b1944',
 'runs/fixed-target-v5-20261027/cell02/check.stdout.json':'7525713bd06a30b9c13693d01949d4f186890128eed3432771953ef9eafef082'}
N=42;PHI=F(997,2500);SIG=F('3.162277660');C=(F('.4097321837023'),F('.4097321837025'))
def need(x,s):
    if not x:raise ValueError(s)
def up(x):return F(-((-x.numerator*10**10)//x.denominator),10**10)
def down(x):return F(x.numerator*10**10//x.denominator,10**10)
def sqrtup(x):
    need(x>=0,'square root domain');k=isqrt(x.numerator*10**24//x.denominator)
    lo,hi=F(k,10**12),F(k+1,10**12);need(lo*lo<=x<=hi*hi,'outward root');return hi
def maxquad(B,f,q):
    need(q>0 and f>=0,'quadratic signs');h=f/(2*q);M=B+f*f/(4*q)
    need([M-B,-f,q]==[q*h*h,-2*q*h,q],'global square-completion polynomial identity')
    return M
def verify(o,old,signed):
    need(o['cells']==24 and o['passes']==2 and len(o['rows'])==len(old)==len(signed)==24,'full two-pass shape')
    for i,row in enumerate(o['rows']):
        l,u=1+F(3361*i,96000),1+F(3361*(i+1),96000)
        need(row['index']==i and F(row['rho_lower'])==l and F(row['rho_upper'])==u and len(row['passes'])==2,'closed ordered rho cover')
        src=old[i];g,b,G,M,KF,v,s=map(F,(src['gamma_abs'],src['beta_abs'],src['Gamma'],src['M4'],src['KF'],src['normal_H_coefficient'],src['slope']))
        K=F(signed[i]['effective_K_abs']);need(K>=0 and G>=0,'signed coefficient/gap premise sign')
        prev=None
        for step in row['passes']:
            density=F(0);gl=-g;diff=2*u
            if prev is not None:
                T,d=F(prev['raw']),F(prev['defect']);need(0<=T<N*C[0]*l and d>=0,'previous raw license')
                density=PHI*(1-T/(N*C[0]*l));a=SIG-d/l
                y=F(-1) if a<=-1 else max(F(-1),(a-3*sqrtup(10-a*a))/10)
                gl=max(-g,SIG*l-3-d,down(min(l*y,u*y)))
                need(gl<=g,'no discarded inconsistent cell');diff=min(2*u,(1-SIG)*l+3+d,u-gl)
            need(0<=diff<=2*u,'rho-minus-gamma sign')
            A=min(3*b*(2*u+1)/2+3*G*diff/2+3*u*u*(u+1)/8+u**3/4-l/2,
                  3*b*(2*u+1)/2+2*u*M-l/2)
            need([F(step[k]) for k in ('K_abs','A','gamma_lower','density_lower','rho_minus_gamma_upper')]==[K,A,gl,density,diff],'reconstructed coupled cell coefficients')
            need(len(step['endpoints'])==2,'both fixed-target endpoints');polys=[]
            for c,z in zip(C,step['endpoints']):
                q=c*l-g/5
                if prev is not None:q=max(q,c*l+min(density*gl,F(2,5)*gl)/2)
                B,f=KF+c*A,c*K+v+s
                need([F(z[k]) for k in ('c','constant','linear','quadratic')]==[c,B,f,q],'endpoint polynomial equality')
                polys.append((B,f,q))
            raw_exact=max(maxquad(*p) for p in polys)
            raw=min(up(raw_exact),up(F(src['fixed_raw'])))
            if prev is not None:raw=min(raw,F(prev['raw']))
            need(0<=raw<N*C[0]*l,'Gaussian-weight license')
            eta=(C[0]*l-raw/N)/2;need(eta>0,'positive simple phase price')
            resource_exact=max(maxquad(B,f,q+eta) for B,f,q in polys)
            resource=min(raw,up(resource_exact))
            if prev is not None:resource=min(resource,F(prev['resource']))
            d=up(6*resource/(N*PHI))
            if prev is not None:d=min(d,F(prev['defect']))
            nd=up(6*resource/PHI);gap=(SIG-1)*l-d
            keys=('raw_exact','raw','phase_extra','resource_exact','resource','defect','weighted_nD','actual_gap_margin')
            need([F(step[k]) for k in keys]==[raw_exact,raw,eta,resource_exact,resource,d,nd,gap],'rounding, prior minima and resource order')
            prev=step
    summaries=[]
    for j in range(2):
        rows=[r['passes'][j] for r in o['rows']]
        summaries.append(dict(pass_number=j+1,max_raw=str(max(F(r['raw']) for r in rows)),
          max_resource=str(max(F(r['resource']) for r in rows)),max_defect=str(max(F(r['defect']) for r in rows)),
          max_weighted_nD=str(max(F(r['weighted_nD']) for r in rows)),
          actual_gap_cells=sum(F(r['actual_gap_margin'])>0 for r in rows),
          min_gap_margin=str(min(F(r['actual_gap_margin']) for r in rows))))
    need(summaries[0]['actual_gap_cells']==23 and summaries[1]['actual_gap_cells']==24,'first gap failure retained; second closes all')
    need(F(summaries[1]['max_defect'])==F('3.5746638454')<4,'exact second-pass defect target')
    need(F(summaries[1]['min_gap_margin'])==F(526024602543,1600000000000)>0,'strict all-cell gap margin')
    return summaries
def main():
    need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'fixed unoptimized invocation');root=Path(sys.argv[1])
    blobs={p:(root/p).read_bytes() for p in PINS}
    for p,h in PINS.items():need(sha256(blobs[p]).hexdigest()==h,'source pin '+p)
    get=lambda p:json.loads(blobs[p])
    o=get('runs/fixed-target-v6-20261027/signed-two-pass02/stdout.json')
    old=get('runs/fixed-target-v5-20261027/cell02/check.stdout.json')['rows']
    signed=get('runs/fixed-target-v6-20261027/signed02/stdout.json')['rows']
    result=verify(o,old,signed);controls=[]
    for name,change in [('missing cell',lambda x:x['rows'].pop()),
       ('wrong pass order',lambda x:x['rows'][0]['passes'].reverse()),
       ('raw replaced by resource',lambda x:x['rows'][0]['passes'][0].update(raw=x['rows'][0]['passes'][0]['resource'])),
       ('understated resource',lambda x:x['rows'][-1]['passes'][1].update(resource='1')),
       ('false first-pass gap',lambda x:x['rows'][-1]['passes'][0].update(actual_gap_margin='1')),
       ('altered signed curvature',lambda x:x['rows'][0]['passes'][1]['endpoints'][0].update(quadratic='1'))]:
        bad=deepcopy(o);change(bad)
        try:verify(bad,old,signed)
        except ValueError:controls.append(name)
        else:raise ValueError('two-pass mutation accepted')
    print(json.dumps(dict(name='INDEPENDENT_TWO_PASS_REVIEW_V1',summaries=result,
      source_pins=PINS,rejected_controls=controls,cell_passes=48,endpoint_quadratics=96,
      shared_checker_or_fourier_execution=False),indent=2))
if __name__=='__main__':main()

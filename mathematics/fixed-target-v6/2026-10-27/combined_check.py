#!/usr/bin/env python3
"""Full 24-cell acquisition with reviewed v6 moment/phase bounds.

Freshly recomputes source constants; retained Fourier theorems remain premises.
Six bounded updates, no dense/native certificate generation.
"""
from fractions import Fraction as F
from pathlib import Path
import importlib.util,json,sys,hashlib
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
moment=load('v6moment',HERE/'moment_check.py')
phase=load('v6phase',HERE/'phase_check.py')
signed=load('v6signed',HERE/'signed-check.py')
base=moment.base
N=42;PHILO=F(997,2500);SIGMALO=F(3162277660,10**9)
need=base.need
up=lambda x:F(base.upper(x,10))

def cover(rows):
    need(len(rows)==24,'exact cell count')
    for i,row in enumerate(rows):
        need(row['index']==i and row['rho_lower']==1+F(3361*i,96000)
          and row['rho_upper']==1+F(3361*(i+1),96000),'ordered complete closed cells')

def improved_A(row,diff=None):
    l,u,b,G=row['rho_lower'],row['rho_upper'],row['beta_abs'],row['Gamma']
    if diff is None:diff=2*u
    need(0<=diff<=2*u,'rho minus gamma bound')
    A1=F(3,2)*b*(2*u+1)+F(3,2)*G*diff+F(3,8)*u*u*(u+1)+u**3/4-l/2
    A2=F(3,2)*b*(2*u+1)+2*u*row['M4']-l/2
    return min(A1,A2)

def step(row,c0,c1,prior=None):
    l,u,g=row['rho_lower'],row['rho_upper'],row['gamma_abs']
    K=min(row['K_abs'],signed.signed_cap(l,u,row['beta_abs'])['new_K_abs'])
    A=improved_A(row);gl=-g;density=F(0)
    if prior is not None:
        T,d=prior['raw'],prior['defect']
        need(0<T<N*c0*l and d>=0,'previous raw license')
        density=PHILO*(1-T/(N*c0*l))
        circle,_,_=moment.circle_lower(l,u,d)
        gl=max(-g,SIGMALO*l-3-d,circle)
        need(gl<=g,'no inconsistent row discarded')
        diff=min(2*u,(1-SIGMALO)*l+3+d,u-gl)
        A=min(A,improved_A(row,diff))
    endpoints=[]
    for c in (c0,c1):
        q=c*l-g/5
        if prior is not None:q=max(q,c*l+min(density*gl,F(2,5)*gl)/2)
        # The selected quadratic itself must pass the global phase gate.
        z=phase.envelope(row['KF']+c*A,c*K+row['normal_H_coefficient']+row['slope'],q,c*l,N)
        endpoints.append(dict(c=c,A=row['KF']+c*A,f=c*K+row['normal_H_coefficient']+row['slope'],q=q,**z))
    T=up(max(z['raw'] for z in endpoints));U=up(max(z['phase_resource'] for z in endpoints))
    if prior is not None:T=min(T,prior['raw']);U=min(U,prior['resource'])
    d=up(6*U/(N*PHILO))
    need(T<N*c0*l,'new raw license')
    # Old quadratic price is a comparator, never a substitute for a raw bound.
    eta=(c0*l-T/N)/2
    old_phase=up(max(z['A']+z['f']**2/(4*(z['q']+eta)) for z in endpoints))
    return dict(raw=T,resource=U,defect=d,weighted_nD=up(6*U/PHILO),K_abs=K,A=A,
      gamma_lower=gl,density_lower=density,endpoints=endpoints,old_phase_comparator=old_phase,
      central_gap_margin=(SIGMALO-1)*l-d,
      central_gap_squared_lower=2*(l-d/(SIGMALO-1)))

def controls(rows):
    from copy import deepcopy
    rejected=[]
    for name,action in [('missing cell',lambda r:r.pop()),('duplicate cell',lambda r:r.__setitem__(1,r[0])),
          ('reordered cells',lambda r:r.reverse()),('open gap',lambda r:r[1].__setitem__('rho_lower',r[1]['rho_lower']+F(1,1000)))]:
        bad=deepcopy(rows);action(bad)
        try:cover(bad)
        except ValueError:rejected.append(name)
        else:raise ValueError('bad cover accepted')
    # An excellent unrelated raw bound does not license a too-large selected polynomial.
    try:phase.envelope(F(43),F(0),F(1),F(1),42)
    except ValueError:rejected.append('external raw bound cannot license selected polynomial')
    else:raise ValueError('unsafe phase gate accepted')
    return rejected

def run():
    need(__debug__ and not sys.flags.optimize,'unoptimized interpreter')
    obj=json.loads((base.HERE/'cell-input.json').read_text(),object_pairs_hook=base.unique)
    first=base.run(obj,{name:(base.HERE/'cell-sources'/name).read_bytes() for name in base.PINS})
    cover(first['rows']);c0,c1=F(obj['c_lower']),F(obj['c_upper']);rows=[]
    for row in first['rows']:
        trace=[];prior=None
        for j in range(7):
            prior=step(row,c0,c1,prior);trace.append(prior)
        rows.append(dict(index=row['index'],rho_lower=row['rho_lower'],rho_upper=row['rho_upper'],steps=trace))
    summaries=[]
    for j in range(7):
        s=[r['steps'][j] for r in rows]
        summaries.append(dict(update=j,max_raw=max(r['raw'] for r in s),max_U=max(r['resource'] for r in s),
          max_D=max(r['defect'] for r in s),max_nD=max(r['weighted_nD'] for r in s),
          cells_D_below4=sum(r['defect']<4 for r in s),cells_D_below2=sum(r['defect']<2 for r in s),
          cells_actual_gap=sum(r['central_gap_margin']>0 for r in s),
          min_actual_gap_margin=min(r['central_gap_margin'] for r in s),
          max_old_phase_D=max(up(6*r['old_phase_comparator']/(N*PHILO)) for r in s)))
    need(summaries[0]['max_D']<4 and summaries[0]['max_raw']<F(84,5),'first pass closes D<4/raw<16.8')
    return dict(name='FIXED_TARGET_V6_COMBINED_24_CELLS_V1',status='PASS_CONDITIONAL_SCALAR_ACQUISITION',
       scope='Conditional on initial contact/support and retained full LOW/HIGH Fourier inequalities. Not INITIAL42 or LOCAL42 acceptance.',
       rows=rows,summaries=summaries,rejected_controls=controls(first['rows']),
       source_sha256={str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in
         [HERE/'combined_check.py',HERE/'phase_check.py',HERE/'signed-check.py',HERE/'moment_check.py']})
if __name__=='__main__':print(json.dumps(base.encode(run()),indent=2))

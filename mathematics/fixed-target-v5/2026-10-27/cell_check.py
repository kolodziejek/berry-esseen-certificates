#!/usr/bin/env python3
"""Exact first raw fixed-target cover; 24 rho cells, no feedback/LOW campaign.

Runs only previously read pure scalar kernels. Analytic primitive validity is
an explicit external premise of this computational result, not established here.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
from hashlib import sha256
from copy import deepcopy
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
PINS={
 'kernel.py':'d71f58b7527c3cf6d2146d816e5d124f6f331d1b153e5aaedee5182707647f12',
 'high_window_core.py':'53e181be63852e21abc3f44191cce7237c46d9e9d7868d3b6b94fccb606c7232',
 'local_signed_core.py':'f0c2df790b794413e7fd08c4f3fc20f79c15c27a6456c8eae5013b96eb093c11',
 'accept_initial42.py':'aa759c74fbd9ad39618264ef51b961f13c7833faa77a7f7b33309c27a7cee032'}
EXPECTED={'schema':'FIXED_C_FIRST_RAW_N42_R384_RHO24_V1','n_floor':42,'rho_cells':24,
 'radius':'96/25','rho_lower':'1','rho_upper':'7361/4000',
 'c_lower':str(F('.4097321837023')),'c_upper':str(F('.4097321837025')),
 'comparison_lower':str(F('.4095')),'comparison_cap':str(F('.4247')),
 'raw_prior':None,'defect_prior':None,'phase_rebate':False,'barrier':'0',
 'normalized_raw_target':'10'}

def need(ok,message):
    if not ok: raise ValueError(message)
def unique(pairs):
    obj={}
    for key,value in pairs:
        need(key not in obj,'duplicate JSON key: '+key);obj[key]=value
    return obj
def validate(obj):
    need(type(obj) is dict and obj==EXPECTED,'literal fixed theorem inputs required')
    need(type(obj['n_floor']) is int and type(obj['rho_cells']) is int,'integer floor and count')
    need(obj['phase_rebate'] is False,'no prior phase rebate')
def check_sources(blobs):
    need(set(blobs)==set(PINS),'complete source dependency set')
    for name,pin in PINS.items():need(sha256(blobs[name]).hexdigest()==pin,'source hash mismatch: '+name)
def sqrt_fine(x):
    scale=10**30;k=isqrt(x.numerator*scale**2//x.denominator)
    lo,hi=F(k,scale),F(k+1,scale)
    need(lo*lo<=x<=hi*hi,'fine sqrt enclosure');return lo,hi
def atan(x):
    lo=sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(40)),F(0))
    return lo,lo+x**81/81
def constants(c0,c1):
    a,b=atan(F(1,5)),atan(F(1,239));pl,ph=16*a[0]-4*b[1],16*a[1]-4*b[0]
    sl,sh=sqrt_fine(F(10));dl,dh=sqrt_fine(2*pl)[0],sqrt_fine(2*ph)[1]
    lo,hi=(3+sl)/(6*dh),(3+sh)/(6*dl)
    need(c0<lo<=hi<c1,'outward fixed CE interval')
    need(F('.3031')*F('.646')/(F('.4095')-F('.3031'))==F(7361,4000),'structural rho endpoint identity')
    return {'CE_lower':lo,'CE_upper':hi,'pi_lower':pl,'pi_upper':ph}
def upper(x,digits=12):
    s=10**digits;v=-((-x.numerator*s)//x.denominator);return str(F(v,s))
def lower(x,digits=12):
    s=10**digits;return str(F(x.numerator*s//x.denominator,s))
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def run(obj,blobs):
    validate(obj);check_sources(blobs)
    c0,c1=F(obj['c_lower']),F(obj['c_upper']);ce=constants(c0,c1)
    sys.path.insert(0,str(HERE/'cell-sources'))
    import kernel as k
    import high_window_core as hw
    one,_=hw.install(k)
    R=F(obj['radius']);N=obj['n_floor'];count=obj['rho_cells']
    k.RADIUS=R;k.K4=(R+1)**2/(R+F(1,2));k.K5=(R**3+2*R*R+3*R+F(3,2))/(R+F(1,2));k.constants()
    rho0,rho1=F(obj['rho_lower']),F(obj['rho_upper'])
    windows=(F(1,8),F(4,25),F(9,50),F(1,5),F(11,50),F(1,4))
    rows=[]
    for i in range(count):
        l=rho0+(rho1-rho0)*F(i,count);u=rho0+(rho1-rho0)*F(i+1,count)
        M=min(F('11.1'),R*u,1+k.K4*(u-1));g=min(F('1.85'),u,k.roots(M-1)[1]);eta=min(R*M,1+k.K5*(u-1))
        low=k.sixth(N,M,g,eta)
        d0=F(3,5);event_a=(2-d0*d0)**2/(2*M+6);event_m=2/event_a
        candidates=[]
        for w in windows:
            bound,terms=one(N,event_a,event_m,d0,M,w)
            need(len(terms)==6 and all(t>0 for t in terms),'complete six-piece high bound')
            candidates.append((bound,w,terms))
        high,w,terms=min(candidates,key=lambda row:row[0])
        need(high==k.universal_high(N,M),'independent window enumeration matches scalar kernel')
        KF=F(16,25)*(low[0]+high+low[2]/k.roots(F(N))[0]);slope=F(16,25)*low[1]
        beta=k.roots((u*k.roots(u*u+8)[1]-u*u-2)/2)[1]
        radial=R*(R+2-F(3,2)*l)/(R+F(1,2));need(radial>=F(31,40),'radial negative-part gate')
        kn=3*u*beta+radial*(u-1);ko=6*u-F(3,2)*u*u+3*beta
        kr=R*u/2+max(abs(R/2-F(3,2)*r) for r in (l,u))*g+3*beta;K=min(kn,ko,kr)
        Gamma=k.negative_gap_coefficient(R,l)
        A=min(F(3,2)*beta*(2*u+1)+3*Gamma*u+F(3,8)*u*u*(u+1)+F(8,27)*u**3-l/2,
              F(3,2)*beta*(2*u+1)+2*u*M-l/2)
        vH=min(F(2,5)*3*(u+1)+F(2,5)*max(F(2),M-3)/6,
               F(2,5)*max(F(1,2),F(2,3)*M-F(1,2)))
        need(A>0 and K>=0,'unsigned coefficient gates')
        def envelope(t):
            q=t*l-g/5;f=t*K+vH+slope;need(q>0 and f>=0,'strict raw quadratic gates')
            return KF+t*A+f*f/(4*q)
        fixed_ends=[envelope(t) for t in (c0,c1)];fixed=max(fixed_ends)
        # Compare the independent scalar reconstruction with the decoded
        # source function at each literal multiplier. This is not independent
        # verification of its shared analytic/Fourier primitives.
        for t,expected in zip((c0,c1),fixed_ends):
            actual=k.initial_cell(N,l,u,None,'universal','upper',score_floor=t,own_cap=t)
            need(actual==expected,'reconstructed endpoint differs from source formula')
        old_floor,old_cap=F(obj['comparison_lower']),F(obj['comparison_cap'])
        old_full=max(envelope(old_floor),envelope(old_cap))
        old_source=max(k.initial_cell(N,l,u,None,'universal',endpoint,score_floor=old_floor,own_cap=old_cap) for endpoint in ('lower','upper'))
        license=N*c0*l;need(fixed<license,'adaptive initial raw license')
        need(fixed/l<F(obj['normalized_raw_target']),'fixed normalized raw target')
        rows.append({'index':i,'rho_lower':l,'rho_upper':u,'M4':M,'gamma_abs':g,'M5_abs':eta,'beta_abs':beta,
          'event_a':event_a,'event_m':event_m,'event_d0':d0,'LOW_L0_LH_L2':low,'HIGH_window':w,'HIGH_six_terms':terms,'HIGH_bound':high,
          'KF':KF,'slope':slope,'K_abs':K,'Gamma':Gamma,'A':A,'normal_H_coefficient':vH,
          'fixed_endpoint_bounds':fixed_ends,'fixed_raw':fixed,'old_full_interval_raw':old_full,'old_source_scorecap_raw':old_source,
          'fixed_raw_upper':upper(fixed),'normalized_raw_upper':upper(fixed/l),'adaptive_license_threshold':license,
          'adaptive_license_margin_lower':lower(license-fixed),'old_source_minus_fixed_lower':lower(old_source-fixed),
          'weight_density_factor_lower':lower(1-fixed/(N*c0*l))})
    need(len(rows)==count and rows[0]['rho_lower']==rho0 and rows[-1]['rho_upper']==rho1,'complete endpoint cover')
    need(all(a['rho_upper']==b['rho_lower'] for a,b in zip(rows,rows[1:])),'no rho gap')
    maximum=max(row['fixed_raw']/row['rho_lower'] for row in rows)
    oldmaximum=max(row['old_source_scorecap_raw']/row['rho_lower'] for row in rows)
    margin=min(row['adaptive_license_threshold']-row['fixed_raw'] for row in rows)
    return {'name':obj['schema'],'scope':'Fresh exact first raw scalar rho cover conditional on universal primitive inequalities and initial support; no full acquisition/local proof.','CE_enclosure':ce,'rows':rows,
      'normalized_raw_upper':upper(maximum),'old_source_normalized_upper':upper(oldmaximum),'normalized_improvement_lower':lower(oldmaximum-maximum),
      'minimum_license_margin_lower':lower(margin),'simple_normalized_target':obj['normalized_raw_target'],
      'coarse_density_factor_lower':1-F(obj['normalized_raw_target'])/(N*c0),'native_stage_executed':False}

def controls(obj,blobs):
    cases=[]
    try:json.loads('{"radius":"96/25","radius":"96/25"}',object_pairs_hook=unique)
    except ValueError:cases.append('duplicate input key')
    else:raise ValueError('duplicate JSON key accepted')
    for name,mutate in [
      ('missing radius',lambda x:x.pop('radius')),('corrupted radius',lambda x:x.update(radius='4')),
      ('sign-swapped rho bounds',lambda x:x.update(rho_lower=obj['rho_upper'],rho_upper=obj['rho_lower'])),
      ('missing cell',lambda x:x.update(rho_cells=23)),('wrong index floor',lambda x:x.update(n_floor=41)),
      ('reversed CE enclosure',lambda x:x.update(c_lower=obj['c_upper'],c_upper=obj['c_lower'])),
      ('unlicensed feedback',lambda x:x.update(raw_prior='2')),('positive barrier',lambda x:x.update(barrier='1'))]:
        changed=deepcopy(obj);mutate(changed)
        try:validate(changed)
        except (ValueError,TypeError):cases.append(name)
        else:raise ValueError('bad literal input accepted: '+name)
    missing=dict(blobs);missing.pop('high_window_core.py')
    try:check_sources(missing)
    except ValueError:cases.append('missing high-frequency dependency')
    else:raise ValueError('missing source accepted')
    corrupted=dict(blobs);corrupted['kernel.py']+=b'\n# corruption\n'
    try:check_sources(corrupted)
    except ValueError:cases.append('corrupted kernel bytes')
    else:raise ValueError('corrupt source accepted')
    swapped=dict(blobs);swapped['kernel.py']=swapped['kernel.py'].replace(b'q=cl*lo-g/5',b'q=cl*lo+g/5',1)
    need(swapped['kernel.py']!=blobs['kernel.py'],'sign mutation applied')
    try:check_sources(swapped)
    except ValueError:cases.append('sign-swapped curvature source')
    else:raise ValueError('sign swapped source accepted')
    return cases

if __name__=='__main__':
    need(__debug__ and not sys.flags.optimize,'assertions and exact arithmetic required')
    need(len(sys.argv)==2,'one literal input file')
    obj=json.loads(Path(sys.argv[1]).read_text(),object_pairs_hook=unique);blobs={name:(HERE/'cell-sources'/name).read_bytes() for name in PINS}
    result=run(obj,blobs);result['rejected_controls']=controls(obj,blobs)
    print(json.dumps(encode(result),indent=2,sort_keys=True))

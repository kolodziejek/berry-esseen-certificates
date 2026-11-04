#!/usr/bin/env python3
"""Independent rational reconstruction of the selected 24x2 coarse pass.

Fourier pairs are inputs supplied by the unchanged v5 kernel, NOT independently
verified here. All non-Fourier cell coefficients and pass outputs are rebuilt.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import isqrt
from hashlib import sha256
import importlib.util
import json
import platform
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path('/Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/manuscript_revision_20261029')
OUT = Path('/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/certificate_discharge_20261030/coarse')
V6 = ROOT/'mathematics/fixed-target-v6/2026-10-27'
N, R, PHI, SIGMA = 42, Q(96,25), Q(997,2500), Q(3162277660,10**9)

def check(v, text):
    if not v:
        raise ValueError(text)

def load(name, p):
    spec = importlib.util.spec_from_file_location(name, p)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def floor(x, scale=10**10):
    return Q((x*scale).__floor__(),scale)

def ceil(x, scale=10**10):
    return -floor(-x,scale)

def root_hi(x, scale=10**8):
    check(x >= 0, 'root domain')
    k = isqrt((x*scale**2).__floor__())
    lo, hi = Q(k,scale), Q(k+1,scale)
    check(lo*lo <= x < hi*hi, 'directed square root')
    return hi

def coefficients(i):
    l, u = 1+Q(3361*i,96000), 1+Q(3361*(i+1),96000)
    M = min(R*u, 1+(R+1)**2/(R+Q(1,2))*(u-1))
    check(M < Q(111,10) and u < Q(37,20), 'unused global moment caps')
    g = min(u, root_hi(M-1))
    eta5 = min(R*M,1+(R**3+2*R**2+3*R+Q(3,2))/(R+Q(1,2))*(u-1))
    b = root_hi((u*root_hi(u*u+8)-u*u-2)/2)
    check(0 <= b < 1 and (1+b*b)**2 >= u*u*(1-b*b), 'beta inversion')
    rad = R*(R+2-Q(3,2)*l)/(R+Q(1,2))
    check(rad >= Q(31,40), 'radial gate')
    oldK = min(3*u*b+rad*(u-1), 6*u-Q(3,2)*u*u+3*b,
               R*u/2+max(abs(R/2-Q(3,2)*x) for x in (l,u))*g+3*b)
    h=1+b
    a=lambda r:(3*r-R)/2
    B=lambda r:R*r-Q(3,2)*r*r+3*b+h*a(r)**2/2
    # B'' = -3 + 9h/4. Solve B'=0 in its original expression.
    sites=[l,u]
    if -3+Q(9,4)*h < 0:
        vertex=-(R-Q(3,4)*h*R)/(-3+Q(9,4)*h)
        if l <= vertex <= u:
            sites.append(vertex)
    signedK=max(map(B,sites))
    gates=(h-a(u),3+2*a(l)*h-Q(3,2)*h*h,R-3*u+Q(3,2)*h*h)
    if min(gates)>=0:
        signedK=min(signedK,R*u-Q(3,2)*u*u-3+3*h+a(u)*h*h-h**3/2)
    K=min(oldK,signedK)
    # Separate concave and decreasing terms over 64 CLOSED subintervals.
    gamma_bounds=[Q(0)]
    vertex=2*(R+l)/3
    for j in range(64):
        x0=l+(R-l)*Q(j,64); x1=l+(R-l)*Q(j+1,64)
        x=min(max(vertex,x0),x1)
        gamma_bounds.append(-x*x/4+(R+l)*x/3-R*l/2+l**3*(2*R-l)/(12*x0*x0))
    Gamma=min(Q(5,2),max(gamma_bounds))
    vH=Q(2,5)*max(Q(1,2),Q(2,3)*M-Q(1,2))
    check(vH < Q(2,5)*3*(u+1)+Q(2,5)*max(2,M-3)/6, 'unused vH minimum')
    return dict(l=l,u=u,M=M,g=g,b=b,eta5=eta5,K=K,oldK=oldK,Gamma=Gamma,vH=vH,gates=gates)

def pass_rebuild(caps,KF,slope,c0,c1,previous=None):
    l,u,M,g,b,G,K=(caps[x] for x in ('l','u','M','g','b','Gamma','K'))
    density, gl, delta = Q(0), -g, 2*u
    if previous is not None:
        T,d=previous['raw'],previous['defect']
        check(0 <= T < N*c0*l and d>=0, 'prior licenses')
        density=PHI*(1-T/(N*c0*l))
        a=SIGMA-d/l
        check(a<=SIGMA and SIGMA**2<10, 'circle domain')
        y=max(Q(-1),(a-3*root_hi(10-a*a,10**12))/10) if a>-1 else Q(-1)
        circle=floor(min(l*y,u*y))
        gl=max(-g,SIGMA*l-3-d,circle)
        check(gl<=g, 'no inconsistent cell discarded')
        delta=min(2*u,(1-SIGMA)*l+3+d,u-gl)
    check(0<=delta<=2*u, 'signed gap charge')
    A=min(Q(3,2)*b*(2*u+1)+Q(3,2)*G*delta+Q(3,8)*u*u*(u+1)+u**3/4-l/2,
          Q(3,2)*b*(2*u+1)+2*u*M-l/2)
    check(A>0 and K>=0, 'coefficient signs')
    # The c coefficient is affine before square completion. Its two
    # endpoint maxima suffice on the full closed c interval.
    ends=[]
    for c in (c0,c1):
        q=c*l-g/5
        if previous is not None:
            q=max(q,c*l+min(density*gl,Q(2,5)*gl)/2)
        f=c*K+caps['vH']+slope
        check(q>0 and f>=0, 'square completion')
        ends.append((KF+c*A,f,q))
    raw_exact=max(B+f*f/(4*q) for B,f,q in ends)
    T=ceil(raw_exact)
    check(0<=T<N*c0*l,'fresh raw license')
    eta=(c0*l-T/N)/2
    resource_exact=max(B+f*f/(4*(q+eta)) for B,f,q in ends)
    U=min(T,ceil(resource_exact))
    d=ceil(6*U/(N*PHI))
    if previous is not None:
        check(T<=previous['raw'] and U<=previous['resource'] and d<=previous['defect'],
              'old raw/resource/defect minima inactive')
    return dict(raw=T,resource=U,defect=d,raw_exact=raw_exact,
                resource_exact=resource_exact,phase_extra=eta,A=A,K_abs=K,
                gamma_lower=gl,density_lower=density,rho_minus_gamma_upper=delta,
                weighted_nD=ceil(6*U/PHI),actual_gap_margin=(SIGMA-1)*l-d)

def enc(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,dict): return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [enc(v) for v in x]
    return x

def main():
    check(__debug__ and sys.flags.optimize==0,'unoptimized Python')
    check(not OUT.exists(),'distinct run directory')
    OUT.mkdir(parents=True)
    t=time.monotonic()
    selected=load('audit_selected_coarse',V6/'signed-two-pass-check.py')
    moment=load('audit_circle_inputs',V6/'moment_check.py')
    base=moment.base
    literal=json.loads((base.HERE/'cell-input.json').read_text(),object_pairs_hook=base.unique)
    blobs={name:(base.HERE/'cell-sources'/name).read_bytes() for name in base.PINS}
    # Only Fourier pairs and native expected outputs are inherited.
    first=base.run(literal,blobs)
    native=selected.run(V6/'moment_check.py')
    c0,c1=Q(literal['c_lower']),Q(literal['c_upper'])
    comparisons=[]
    for i,(old,new) in enumerate(zip(first['rows'],native['rows'])):
        c=coefficients(i)
        for key,own in [('rho_lower','l'),('rho_upper','u'),('M4','M'),('gamma_abs','g'),
                        ('M5_abs','eta5'),('beta_abs','b'),('K_abs','oldK'),('Gamma','Gamma'),
                        ('normal_H_coefficient','vH')]:
            check(old[key]==c[own],f'row {i} coefficient {key}')
        rebuilt=[]
        for j in range(2):
            r=pass_rebuild(c,old['KF'],old['slope'],c0,c1,rebuilt[-1] if rebuilt else None)
            for key in r:
                check(r[key]==new['passes'][j][key],f'cell {i} pass {j+1} {key}')
            check(r['raw']<=ceil(old['fixed_raw']),'old first-cover raw minimum inactive')
            rebuilt.append(r)
        comparisons.append(dict(index=i,signed_gates=c['gates'],passes=rebuilt))
    check(len(comparisons)==24 and first['rows'][0]['rho_lower']==1
          and first['rows'][-1]['rho_upper']==Q(7361,4000),'full cover')
    s1,s2=native['summaries']
    check([s1[k] for k in ('max_raw','max_resource','max_defect')]
          ==list(map(Q,('13.2818901598','10.9330610254','3.9164138937'))),'D.3 first row')
    check([s2[k] for k in ('max_raw','max_resource','max_defect')]
          ==list(map(Q,('11.5164967977','9.9790315907','3.5746638454'))),'D.3 second row')
    check(s1['cells_actual_gap']==23 and s2['cells_actual_gap']==24,'actual gap counts')
    check(s2['min_actual_gap_margin']==Q(526024602543,1600000000000),'D.3 exact gap margin')
    # Adversarial controls from the selected verifier run unchanged. Add
    # circle branch / impossible moment controls, absent from that path.
    circle_controls=moment.controls()
    # Opposite-sign beta*gamma law rejects a tempting unlicensed sign premise.
    signed=load('audit_sign_moments',V6/'signed-check.py')
    actual=signed.moments([Q(-96,25),Q(-1,2),Q(37,25)],
                         [Q(325,22211),Q(11708,16533),Q(3650,13167)])
    check(actual['beta']*actual['gamma']<0,'opposite sign control')
    inputs=[V6/'signed-two-pass-check.py',V6/'moment_check.py',V6/'signed-check.py',
            base.HERE/'cell_check.py',base.HERE/'cell-input.json',
            *[base.HERE/'cell-sources'/name for name in base.PINS]]
    hashes={str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in inputs}
    hashes['audit_script']=sha256(Path(__file__).read_bytes()).hexdigest()
    summary=dict(status='PASS_COARSE_RECONSTRUCTION_CONDITIONAL_ON_ANALYTIC_INPUTS',
                 scope='48 rational passes, complete 24-cell cover; Fourier values remain shared inputs',
                 python=platform.python_version(),python_executable=sys.executable,optimize=sys.flags.optimize,
                 elapsed_seconds=time.monotonic()-t,cells=24,passes=48,
                 summaries=native['summaries'],selected_controls=native['rejected_controls'],
                 extra_circle_controls=circle_controls,opposite_sign_control=actual,
                 input_sha256=hashes)
    (OUT/'selected.json').write_text(json.dumps(enc(native),indent=2)+'\n')
    (OUT/'reconstructed.json').write_text(json.dumps(enc(comparisons),indent=2)+'\n')
    (OUT/'summary.json').write_text(json.dumps(enc(summary),indent=2)+'\n')
    print(json.dumps(enc(summary),indent=2))

if __name__=='__main__': main()

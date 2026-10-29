"""Exact actual-marginal controls for the summable-curvature closure.

The scalar theorem is not proved by these examples. The normal/root kernel
is explicitly reused and source-pinned; all actual moments, gap weights,
curvature sums and iid events are reconstructed below.
"""
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
def root(x):
    scale=10**50;k=isqrt(x.numerator*scale*scale//x.denominator)
    lo,hi=F(k,scale),F(k+1,scale);assert lo*lo<=x<hi*hi
    return lo,hi
sl,su=root(F(10))
def cond(var,side):
    if not var:return [(F(0),F(1))]
    A=F(3,5) if side==0 else F(7,10);a=var/A
    return [(-A,a/(A+a)),(a,A/(A+a))] if side==0 else [(-a,A/(A+a)),(A,a/(A+a))]
def binlaw(zs,n):
    if n==0:return [(F(0),F(1))]
    if len(zs)==1:return [(n*zs[0][0],F(1))]
    (a,p),(b,q)=zs;assert p+q==1
    return [(j*a+(n-j)*b,F(comb(n,j))*p**j*q**(n-j)) for j in range(n+1)]
def Wlaw(noises,n,j):
    out={}
    for x,a in binlaw(noises[0],n-j):
        for y,b in binlaw(noises[1],j):out[x+y]=out.get(x+y,F(0))+a*b
    return sorted(out.items())
def curvature(p,n,noises,t):
    q=1-p;v=p*q;vs=[sum(x*x*m for x,m in law) for law in noises]
    lam=n*(q*vs[0]+p*vs[1]);A=max(abs(x) for law in noises for x,_ in law)
    T=lam/q;M=A*A*T+3*T*T;c=max(n*p-q-t,F(0));assert c<=1
    pis=[F(comb(n,j))*p**j*q**(n-j) for j in range(n+1)]
    mass=max(F(comb(n+1,j))*p**j*q**(n+1-j) for j in range(n+2))
    C=F(0)
    for j in range(1,n):
        law=Wlaw(noises,n,j);a=t-j
        Bj=sum(max(a-x,F(0))*m for x,m in law)-max(a,F(0))
        assert Bj>=0
        if pis[j+1]>pis[j]:
            assert sum(x*x*m for x,m in law)<=T
            assert sum(x**4*m for x,m in law)<=M
        C+=(pis[j+1]-pis[j])*Bj
    S=T/4+c*root(T)[1]+F(27,256)*M*(F(5,3)+F(5,4)*c)
    bound=mass*S/((n+1)*v)
    assert C<=bound,(p,n,t,C,bound)
    return C,bound,lam,T,M,mass
controls=[]
for n in [4,8]:
    for p in [F(1,3),F(2,5)]:
        for lam in [F(1,10**12),F(9,100),F(3,10)]:
            for allocation in [F(0),F(1,2),F(1)]:
                q=1-p;noises=[cond(lam*(1-allocation)/(n*q),0),cond(lam*allocation/(n*p),1)]
                for reflect in [False,True]:
                    pp=1-p if reflect else p
                    laws=[ [(-x,m) for x,m in noises[1]], [(-x,m) for x,m in noises[0]]] if reflect else noises
                    for offset in [F(-1,2),F(0),F(1,5)]:
                        t=n*pp-(1-pp)+offset
                        C,bound,_,_,_,_=curvature(pp,n,laws,t)
                        controls.append({'n':n,'p':str(pp),'lambda':str(lam),'allocation':str(allocation),
                            'reflected':reflect,'threshold':str(t),'curvature':str(C),'upper':str(bound)})
# An actual tiny-noise atom shows why the c sqrt(T) term cannot be removed.
p=F(7,20);n=42;e=F(1,10**6);noises=[[(-e,F(1,2)),(e,F(1,2))]]*2;t=F(14)
C,bound,lam,T,M,mass=curvature(p,n,noises,t)
wrong=mass*(T/4+F(27,256)*M*F(5,3))/((n+1)*p*(1-p))
assert C>wrong and (t-n*p)**2<F(46,25)**2*(p*(1-p)+e*e)
wrong_control={'n':n,'p':str(p),'epsilon':str(e),'threshold':str(t),
               'actual_curvature':str(C),'false_bound_without_c_sqrtT':str(wrong)}
# Below 1/3 even actual centered tiny noise can lower the third moment.
p=F(13,50);q=1-p;e=F(1,1000);v=p*q
atoms=[(-e-p,q/2),(e-p,q/2),(1-p,p)]
V=sum(x*x*m for x,m in atoms);M3=sum(abs(x)**3*m for x,m in atoms)
assert M3*M3*v<(1-2*v)**2*V**3

helper=Path(__file__).resolve().parents[2]/'simplification-v10/2026-10-28/actual_law_checks.py'
pin='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
blob=helper.read_bytes();assert hashlib.sha256(blob).hexdigest()==pin
ns={'__name__':'geometry_slack_kernel','__file__':str(helper)};exec(compile(blob,str(helper),'exec'),ns)
I,add,sub,mul,div=map(ns.get,['I','add','sub','mul','div'])
full=[];rejected=[]
for n,p,lam,side in [(126,F(1,3),F(1,50),0),(126,F(1,3),F(1,20),0),
                    (140,F(1,3),F(1,50),1),(200,F(7,20),F(1,50),0),
                    (200,F(7,20),F(1,25),1)]:
    q=1-p;v=p*q;zs=[[(F(0),F(1))],[(F(0),F(1))]]
    zs[side]=cond(lam/(n*(q if side==0 else p)),side)
    law=[(j+x,(q if j==0 else p)*m) for j in [0,1] for x,m in zs[j]]
    centered=sorted((x-p,m) for x,m in law);V=sum(x*x*m for x,m in centered)
    rho_raw=sum(abs(x)**3*m for x,m in centered);gamma=sum(x**3*m for x,m in centered)
    J=sum(sum(x*m for x,m in centered[j+1:])*(centered[j+1][0]-centered[j][0])**2 for j in range(len(centered)-1))
    D=div(I(n),mul(I(V),ns['root'](V)))
    D=mul(D,sub(mul(add(I(3),ns['root'](F(10))),I(rho_raw)),I(gamma+3*J)))
    Qlo=(sl+1)*p*p+(sl-1)*q*q-6*v
    costlo=n*Qlo/root(v)[1]
    a0=max(x for x,_ in zs[0]);a1=max(-x for x,_ in zs[1])
    valid=costlo>=24 and D[1]<=F(129,4) and a0+a1<=F(17,250)
    if not valid:
        rejected.append({'n':n,'p':str(p),'lambda':str(lam),'side':side,'nD':[str(z) for z in D],
                         'cost_lower':str(costlo),'reason':'outside stated geometry theorem inputs'})
        continue
    # Threshold at the atom with no outward jump; immediate rational neighbors.
    k=(n*p+F(1,2)).numerator//(n*p+F(1,2)).denominator
    common0=max(zs[0],key=lambda x:x[1])[0];common1=max(zs[1],key=lambda x:x[1])[0]
    collision=k+(n-k)*common0+k*common1
    dist,den=ns['distribution'](law,n)
    for shift in [F(-1,10**20),F(0),F(1,10**20)]:
        t=collision+shift;assert (t-n*p)**2<=F(46,25)**2*V
        cdf=F(sum(m for x,m in dist if x<=t),den)
        jump=F(sum(m for x,m in dist if x==t),den)
        norm=ns['Phi_interval'](div(I(t-n*p),ns['root'](n*V)))
        rho=div(I(rho_raw),mul(I(V),ns['root'](V)))
        excess=sub(mul(ns['root'](F(n)),sub(I(cdf),norm)),mul(ns['CE'],rho))
        assert excess[1]<-F(1,10*n)
        assert (jump>0)==(shift==0)
        full.append({'n':n,'p':str(p),'lambda':str(lam),'side':side,
          'threshold':str(t),'collision':shift==0,'jump':str(jump),
          'nD_interval':[str(z) for z in D],'geometric_cost_lower':str(costlo),
          'signed_excess_interval':[str(z) for z in excess],
          'margin_to_claim':str(-F(1,10*n)-excess[1])})
assert len(full)>=9
here=Path(__file__).resolve()
print(json.dumps({'status':'PASS_GEOMETRY_SLACK_ACTUAL_CONTROLS',
 'general_curvature_controls':len(controls),'curvature_cases':controls,
 'full_signed_events':len(full),'full_events':full,'outside_scope_candidates':rejected,
 'missing_sqrt_control':wrong_control,
 'negative_controls':['omitting_c_sqrtT_is_false_at_a_tiny_noise_atom',
                      'rho_can_decrease_below_one_third'],
 'normal_distribution_kernel_sha256':pin,
 'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),
 'proof_sha256':hashlib.sha256(here.with_name('geometry-slack.tex').read_bytes()).hexdigest(),
 'python':sys.version,
 'scope':'Bounded exact implementation and actual-law controls; not continuous-domain coverage or an independent implementation of the reused normal kernel.'},indent=2))

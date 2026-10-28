"""Bounded exact actual-law controls for LEFT-01.

Conditional count convolution and the joint inequality are implemented here.
Five full-Delta checks reuse the expressly pinned earlier rational-normal
kernel. Neither finite family establishes the universal theorem by sampling.
"""
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions required')
A=F(7,10); alpha=F(27,50); M=5*alpha**4; m=F(18,25)
cl=F(819,2000); cu=F(41,100); n=42
def root(x):
    den=10**45; k=isqrt(x.numerator*den**2//x.denominator)
    out=F(k,den),F(k+1,den)
    assert out[0]**2<=x<=out[1]**2
    return out
def scaled(raw,var):
    rr=root(var)
    z=[raw/(var*r) for r in rr]
    return min(z),max(z)
def bern_rho(v):
    rr=root(v)
    return (1-2*v)/rr[1],(1-2*v)/rr[0]
def conditional(vv,side):
    if vv==0:return [(F(0),F(1))]
    e=vv/A
    if side==0:return [(-A,e/(A+e)),(e,A/(A+e))]
    return [(-e,A/(A+e)),(A,e/(A+e))]
def repeated(two,N):
    if len(two)==1:return [(N*two[0][0],F(1))]
    (a,pa),(b,pb)=two
    return [(j*a+(N-j)*b,F(comb(N,j))*pa**j*pb**(N-j)) for j in range(N+1)]
def count_events(noises,k,thresholds):
    d0=repeated(noises[0],n-k); d1=repeated(noises[1],k)
    out=[[F(0),F(0)] for _ in thresholds]
    assert sum(w for _,w in d0)==sum(w for _,w in d1)==1
    for a,wa in d0:
        for b,wb in d1:
            x=a+b; mass=wa*wb
            for z,y in zip(thresholds,out):
                if x>z:y[0]+=mass
                if x==z:y[1]+=mass
    return out
def L(r,t):
    return ((3*alpha**2-A*A-6*r*r)*t-3*t*t-4*A*r*t-r**4+
            3*alpha**2*r*r+2*alpha**3*r)/M
cases=[]; collision_events=0; minmargin=None; wrong_units=[]
for p in [F(1,4),F(13,50),F(1,3),F(2,5)]:
    q=1-p;v=p*q;k=(n*p+F(1,2)).numerator//(n*p+F(1,2)).denominator
    for lam in [F(1,10**10),F(1,500),F(1,100)]:
        s=lam/n
        for eta in [F(0),F(1,2),F(1)]:
            vv=[s*(1-eta)/q,s*eta/p]
            noises=[conditional(vv[0],0),conditional(vv[1],1)]
            assert all(sum(x*w for x,w in z)==0 for z in noises)
            assert all(sum(x*x*w for x,w in z)==v0 for z,v0 in zip(noises,vv))
            assert vv[0]/A+vv[1]/A<F(17,250)
            t=(n-k)*vv[0]+k*vv[1]
            raw=q*sum(abs(x-p)**3*w for x,w in noises[0])+p*sum(abs(1+x-p)**3*w for x,w in noises[1])
            B=A+3*p-F(3,2)*(1-2*v)-3*(1-2*v)*s/(8*v)
            joint=scaled(raw-B*s,v+s); rhoB=bern_rho(v)
            diff=(joint[0]-rhoB[1],joint[1]-rhoB[0])
            rho=scaled(raw,v+s)
            events=count_events(noises,k,[F(0),-F(3,2)*t])
            out=[]
            for r,(pr,collision) in zip([F(0),F(3,2)*t],events):
                assert (k-n*p-r)**2<F(46,25)**2*(v+s)
                assert r<=F(1,20)
                gaps=[m*(pr-L(r,t))+C*diff[0] for C in [cl,cu]]
                assert min(gaps)>0
                minmargin=min(gaps+[minmargin]) if minmargin is not None else min(gaps)
                collision_events+=int(collision>0)
                # Opposite upper enclosure tests the tempting n-fold overclaim.
                wrong=m*(pr-L(r,t))+cu*(rho[1]-rhoB[0])-F(7,4)*lam
                if wrong<0:wrong_units.append((str(p),str(lam),str(eta),str(r),str(wrong)))
                out.append({'r':str(r),'strict_own_probability':str(pr),
                    'threshold_atom':str(collision),'joint_margin_lower':str(min(gaps))})
            cases.append({'p':str(p),'n':n,'k':k,'lambda':str(lam),
                'allocation':str(eta),'events':out})
assert len(cases)==36 and collision_events>0 and wrong_units

# Explicit adverse-cubic law, independently squared before any radical bound.
p=F(13,50);v=p*(1-p);s=(1-p)/10**6
raw=v*(1-2*v)+3*p*s
assert raw**2*v<(1-2*v)**2*(v+s)**3

# Full-Delta selected event checks.  No floating search is used: the no-rare
# atom at the nearest integer count supplies the exact threshold.
helper=Path(__file__).resolve().parents[2]/'simplification-v10/2026-10-28/actual_law_checks.py'
pin='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
blob=helper.read_bytes(); assert hashlib.sha256(blob).hexdigest()==pin
ns={'__name__':'leftcount_selected_kernel','__file__':str(helper)}
exec(compile(blob,str(helper),'exec'),ns)
full=[]
specs=[(F(1,4),F(1,100),F(0)),(F(13,50),F(1,100),F(1)),
       (F(1,3),F(1,100),F(1,2)),(F(2,5),F(1,10**10),F(1))]
for p,lam,eta in specs:
    s=lam/n;q=1-p;vv=[s*(1-eta)/q,s*eta/p]
    noises=[conditional(vv[0],0),conditional(vv[1],1)]
    k=(n*p+F(1,2)).numerator//(n*p+F(1,2)).denominator
    threshold=k+(n-k)*vv[0]/A-k*vv[1]/A
    full.append((p,lam,noises,threshold))
p=F(13,50)
full.append((p,n*(1-p)/10**6,
             [[(F(-1,1000),F(1,2)),(F(1,1000),F(1,2))],[(F(0),F(1))]],
             F(11)-F(1,1000)))
selected=[]
for p,lam,noises,x in full:
    atoms=ns['law'](p,*noises);dist,den=ns['distribution'](atoms,n)
    cdf=F(sum(w for z,w in dist if z<=x),den)
    jump=F(sum(w for z,w in dist if z==x),den)
    assert jump>0
    anchor=x+F(109,500);k=anchor.numerator//anchor.denominator
    var=sum((z-p)**2*w for z,w in atoms);raw=sum(abs(z-p)**3*w for z,w in atoms)
    assert n*(var-p*(1-p))==lam and 0<lam<=F(1,100)
    assert (x-n*p)**2<F(46,25)**2*var
    assert -F(109,500)<=x-k<=F(391,500) and 1<=k<n
    z={'threshold':x,'variance':var,'third_raw':raw,'k':k,
       'cdf':cdf,'jump':jump,'lambda':lam}
    result=ns['exact_event'](atoms,n,p,z)
    selected.append({'p':str(p),'lambda':str(lam),'threshold':str(x),
                     'phase':str(x-k),'atom_count':len(dist),**result})
assert hashlib.sha256(helper.read_bytes()).hexdigest()==pin
print(json.dumps({'status':'PASS_LEFT_01_ACTUAL_LAWS','marginal_count':len(cases),
    'exact_own_events':2*len(cases),'coupled_C_endpoint_checks':4*len(cases),
    'own_events_with_threshold_atoms':collision_events,
    'joint_margin_lower_min':str(minmargin),'joint_cases':cases,
    'negative_controls':{'adverse_cubic_actual_law':True,
        'wrong_lambda_instead_of_s_rejected':wrong_units[0]},
    'full_Delta_selected_events':selected,'reused_normal_kernel_sha256':pin,
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'python':sys.version,'scope':'The new coupled bounds use an independent '
    'conditional-convolution implementation. Five full-Delta events reuse the '
    'pinned earlier rational-normal kernel. These are actual iid adversarial '
    'controls, not a sampled proof of the universal comparison.'},indent=2))

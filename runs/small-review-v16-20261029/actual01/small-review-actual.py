"""Actual-law/atom controls for compact small noise at coefficient C=0.

C=0 is the weakest comparison because the independently checked cubic sign
makes Delta_C nonincreasing for C>=0. The complete CDF and normal enclosure
kernel is reused and disclosed, not an independent analytic proof.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
base=Path(__file__).resolve().parents[3]
helper=base/'mathematics/simplification-v10/2026-10-28/actual_law_checks.py'
pin='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
raw=helper.read_bytes();assert hashlib.sha256(raw).hexdigest()==pin
ns={'__name__':'small_review_reused_normal_kernel','__file__':str(helper)}
exec(compile(raw,str(helper),'exec'),ns)
I,add,sub,mul,div=[ns[x] for x in ['I','add','sub','mul','div']]
def centered(a,b):return [(-a,b/(a+b)),(b,a/(a+b))]
zero=[(F(0),F(1))];cases=[]
for n,p,lam,side in [(700,F(3,8),F(1,100),0),(700,F(93,200),F(1,100),1),(701,F(2,5),F(1,10**6),0)]:
    eps=lam/(n*(p if side else 1-p)*F(3,5));noises=[zero,zero]
    noises[side]=centered(F(3,5),eps) if side==0 else centered(eps,F(3,5))
    cases.append((n,p,lam,noises,'rare conditional '+str(side),False))
cases.append((700,F(2,5),F(7,2500),[centered(F(1,500),F(1,500))]*2,'independent symmetric noise; exact collisions',True))
rows=[];laws=[]
for n,p,lam,noises,label,common in cases:
    assert n>=700 and F(3,8)<=p<=F(93,200) and 0<lam<=F(1,100)
    for z in noises:assert sum(w for x,w in z)==1 and sum(x*w for x,w in z)==0
    a0=max(x for x,w in noises[0]);a1=max(-x for x,w in noises[1])
    assert a0+a1<=F(1,250) and all(abs(x)<=F(3,5) for z in noises for x,w in z)
    atoms=[(j+x,(p if j else 1-p)*w) for j in (0,1) for x,w in noises[j]]
    v=p*(1-p);V=sum((x-p)**2*w for x,w in atoms);M3=sum(abs(x-p)**3*w for x,w in atoms)
    assert V==v+lam/n
    rho=div(I(M3),mul(I(V),ns['root'](V)));rhoB=div(I(1-2*v),ns['root'](v))
    assert sub(rho,rhoB)[0]>0
    if common:
        # Here B and U are actually independent. Expand the two binomials
        # separately and collect exact equal atoms; avoid 4-atom occupancies.
        weightsB=[comb(n,j)*p.numerator**j*(p.denominator-p.numerator)**(n-j) for j in range(n+1)]
        weightsU=[comb(n,j) for j in range(n+1)];acc={}
        for j,bm in enumerate(weightsB):
            for ell,um in enumerate(weightsU):
                key=500*j+2*ell-n;acc[key]=acc.get(key,0)+bm*um
        den=(2*p.denominator)**n;dist=[(F(x,500),mass) for x,mass in sorted(acc.items())]
        assert sum(mass for _,mass in dist)==den
        assert len(dist)<(n+1)**2
    else:dist,den=ns['distribution'](atoms,n)
    centers=sorted({min(dist,key=lambda z:abs(z[0]-n*p-shift))[0] for shift in [F(-4,5),F(0),F(4,5)]})
    events=[]
    for center in centers:
        for e in [F(-1,10**25),F(0),F(1,10**25)]:
            t=center+e;shifted=t+F(3,10);k=shifted.numerator//shifted.denominator
            events.append((t,k,e==0,'atom and neighboring sides'))
    # The shared endpoint has two legal anchors. Verify both at one actual law.
    boundary=F((n*p).numerator//(n*p).denominator)+F(7,10)
    if (boundary-n*p)**2<F(46,25)**2*V:
        for k in [int(boundary-F(7,10)),int(boundary+F(3,10))]:
            events.append((boundary,k,None,'both closed phase anchors'))
    for t,k,isatom,kind in events:
        assert (t-n*p)**2<=F(46,25)**2*V and 1<=k<n
        u=t-k;assert F(-3,10)<=u<=F(7,10)
        cdf=F(sum(mass for x,mass in dist if x<=t),den)
        jump=F(sum(mass for x,mass in dist if x==t),den)
        if isatom is not None:assert bool(jump)==isatom
        FB=sum(F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(k+1))
        normal=ns['Phi_interval'](div(I(t-n*p),ns['root'](n*V)))
        normalB=ns['Phi_interval'](div(I(k-n*p),ns['root'](n*v)))
        delta0=mul(ns['root'](F(n)),sub(sub(I(cdf),normal),sub(I(FB),normalB)))
        assert delta0[1]<-lam/100
        rows.append({'law':label,'n':n,'p':str(p),'lambda':str(lam),'threshold':str(t),'anchor':k,'phase':str(u),
                     'kind':kind,'atom':bool(jump),'delta0_interval':list(map(str,delta0)),
                     'gap_afterlambda100':str(-lam/100-delta0[1])})
    laws.append({'n':n,'p':str(p),'lambda':str(lam),'label':label,'atoms':[[str(x),str(w)]for x,w in atoms],
                 'sum_atom_count':len(dist),'inward_sum':str(a0+a1),'rho_minus_rhoB_lower':str(sub(rho,rhoB)[0])})
print(json.dumps({'status':'PASS_SMALL_REVIEW_ACTUAL_LAWS','laws':laws,'event_count':len(rows),'events':rows,
 'kernel_sha256':pin,'scope':'Four actual iid controls at n700/701, including tiny defect, exact collisions and both legal boundary anchors. No continuum coverage is inferred.'},indent=2))

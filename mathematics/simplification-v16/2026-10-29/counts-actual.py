"""Actual iid controls of the new interval; reused outward kernel disclosed."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
base=Path(__file__).resolve().parents[3]
helper=base/'mathematics/simplification-v10/2026-10-28/actual_law_checks.py'
pin='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
raw=helper.read_bytes();assert hashlib.sha256(raw).hexdigest()==pin
ns={'__name__':'counts_v16_reused_outward_kernel','__file__':str(helper)}
exec(compile(raw,str(helper),'exec'),ns)
I,sub,mul,div=[ns[x] for x in ['I','sub','mul','div']]
def centered(a,b):return [(-a,b/(a+b)),(b,a/(a+b))]
zero=[(F(0),F(1))];cases=[]
for n,p,lam,side in [(200,F(2,5),F(3,100),0),(200,F(53,100),F(3,100),1),(201,F(53,100),F(3,40),1)]:
    eps=lam/(n*(p if side else 1-p)*F(3,5));noises=[zero,zero]
    noises[side]=centered(F(3,5),eps) if side==0 else centered(eps,F(3,5))
    cases.append((n,p,lam,noises,'rare conditional '+str(side)))
cases.append((200,F(1,2),F(9,200),[centered(F(3,200),F(3,200))]*2,'common symmetric, collisions'))
cases.append((200,F(2,5),F(11,250),[centered(F(1,100),F(1,100)),centered(F(1,50),F(1,50))],'unequal four atoms'))
rows=[];laws=[]
for n,p,lam,noises,label in cases:
    assert n>=200 and F(2,5)<=p<=F(53,100) and F(3,100)<=lam<=F(9,25)
    for z in noises:assert sum(w for _,w in z)==1 and sum(x*w for x,w in z)==0
    a0=max(x for x,w in noises[0]);a1=max(-x for x,w in noises[1])
    assert a0>=0 and a1>=0 and a0+a1<=F(9,125)
    assert all(abs(x)<=F(3,5) for z in noises for x,w in z)
    atoms=[(j+x,(p if j else 1-p)*w) for j in (0,1) for x,w in noises[j]]
    V=sum((x-p)**2*w for x,w in atoms);M3=sum(abs(x-p)**3*w for x,w in atoms)
    assert V==p*(1-p)+lam/n
    dist,den=ns['distribution'](atoms,n)
    centers=sorted({min(dist,key=lambda z:abs(z[0]-n*p-shift))[0] for shift in [F(-4,5),F(0),F(4,5)]})
    rho=div(I(M3),mul(I(V),ns['root'](V)))
    for center in centers:
        for e in [F(-1,10**20),F(0),F(1,10**20)]:
            t=center+e;assert (t-n*p)**2<=F(46,25)**2*V
            cdf=F(sum(m for x,m in dist if x<=t),den)
            jump=F(sum(m for x,m in dist if x==t),den)
            normal=ns['Phi_interval'](div(I(t-n*p),ns['root'](n*V)))
            score=sub(mul(ns['root'](F(n)),sub(I(cdf),normal)),mul(ns['CE'],rho))
            assert score[1]<-lam/100
            assert (jump>0)==(e==0)
            shifted=t+F(34,125);k=shifted.numerator//shifted.denominator;phase=t-k
            rows.append({'law':label,'n':n,'p':str(p),'lambda':str(lam),'t':str(t),
                         'phase':str(phase),'old_negative_inner':F(-3,20)<=phase<=0,
                         'at_atom':e==0,'jump':str(jump),'excess_interval':list(map(str,score)),
                         'strict_margin_lower':str(-lam/100-score[1])})
    laws.append({'label':label,'n':n,'p':str(p),'lambda':str(lam),'atoms':[[str(x),str(w)]for x,w in atoms],
                 'inward_sum':str(a0+a1),'sum_atom_count':len(dist)})
assert any(r['old_negative_inner'] for r in rows)
assert any(r['old_negative_inner'] and r['at_atom'] for r in rows)
assert any(not r['old_negative_inner'] for r in rows)
print(json.dumps({'status':'PASS_COUNTS_V16_ACTUAL_LAWS','laws':laws,'event_count':len(rows),
 'old_negative_inner_events':sum(r['old_negative_inner'] for r in rows),'events':rows,
 'kernel_sha256':pin,'proof_sha256':hashlib.sha256(Path(__file__).with_name('counts-analytic.tex').read_bytes()).hexdigest(),
 'scope':'Actual-law smoke controls, not domain coverage. Occupancy/normal enclosure kernel reused and source pinned; no independent-verifier claim.'},indent=2))

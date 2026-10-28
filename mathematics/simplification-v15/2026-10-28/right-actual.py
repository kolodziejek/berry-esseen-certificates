"""Bounded actual iid controls for the signed right theorem.

Actual moments and thresholds are rebuilt here. The occupancy/normal-enclosure
kernel is reused explicitly, source pinned, and is not independent verification.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
rootdir=Path(__file__).resolve().parents[3]
helper=rootdir/'mathematics/simplification-v10/2026-10-28/actual_law_checks.py'
pin='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
blob=helper.read_bytes();assert hashlib.sha256(blob).hexdigest()==pin
ns={'__name__':'right_v15_reused_kernel','__file__':str(helper)}
exec(compile(blob,str(helper),'exec'),ns)
I,add,sub,mul,div=map(ns.get,['I','add','sub','mul','div'])
def centered(a,b):return [(-a,b/(a+b)),(b,a/(a+b))]
zero=[(F(0),F(1))];cases=[]
for n,p,lam,side in [(200,F(2,5),F(3,40),0),(200,F(2,5),F(9,25),1),
                      (201,F(53,100),F(9,25),0),(201,F(53,100),F(3,40),1)]:
    eps=lam/(n*(p if side else 1-p)*F(3,5))
    noises=[zero,zero]
    noises[side]=centered(F(3,5),eps) if side==0 else centered(eps,F(3,5))
    cases.append((n,p,lam,noises,'one noisy conditional'))
# An actual four-atom unequal-noise marginal with exact rational lattice.
cases.append((200,F(2,5),F(3,25),[centered(F(1,50),F(1,50)),centered(F(3,100),F(3,100))],'both noisy, four atoms'))
records=[];lawrecords=[]
for n,p,lam,noises,label in cases:
    q=1-p;v=p*q
    assert all(sum(w for _,w in z)==1 and sum(x*w for x,w in z)==0 for z in noises)
    a0=max(x for x,_ in noises[0]);a1=max(-x for x,_ in noises[1])
    assert a0+a1<=F(9,125) and all(abs(x)<=F(3,5) for z in noises for x,_ in z)
    atoms=[(j+x,(q if j==0 else p)*w) for j in [0,1] for x,w in noises[j]]
    V=sum((x-p)**2*w for x,w in atoms);M3=sum(abs(x-p)**3*w for x,w in atoms)
    assert V==v+lam/n
    dist,den=ns['distribution'](atoms,n)
    centers={min(dist,key=lambda z:abs(z[0]-n*p-shift))[0] for shift in [F(-4,5),F(0),F(4,5)]}
    cumulative=0;prefix=[]
    for t,m in dist:cumulative+=m;prefix.append((t,cumulative,m))
    for center in sorted(centers):
        for shift in [F(-1,10**20),F(0),F(1,10**20)]:
            t=center+shift;assert (t-n*p)**2<=F(46,25)**2*V
            cdf=F(sum(m for z,m in dist if z<=t),den)
            jump=F(sum(m for z,m in dist if z==t),den)
            normal=ns['Phi_interval'](div(I(t-n*p),ns['root'](n*V)))
            rho=div(I(M3),mul(I(V),ns['root'](V)))
            excess=sub(mul(ns['root'](F(n)),sub(I(cdf),normal)),mul(ns['CE'],rho))
            assert excess[1]<-lam/100
            assert (jump>0)==(shift==0)
            records.append({'n':n,'p':str(p),'lambda':str(lam),'law':label,'threshold':str(t),
                'at_atom':shift==0,'jump':str(jump),'excess_interval':list(map(str,excess)),
                'gap_to_claim':str(-lam/100-excess[1])})
    lawrecords.append({'n':n,'p':str(p),'lambda':str(lam),'atoms':[[str(x),str(w)] for x,w in atoms],
                       'number_sum_atoms':len(dist),'inward_sum':str(a0+a1)})
print(json.dumps({'status':'PASS_RIGHT_SIGNED_200_ACTUAL_CONTROLS','laws':lawrecords,
 'event_count':len(records),'atom_event_count':sum(r['at_atom'] for r in records),'events':records,
 'kernel_sha256':pin,'proof_sha256':hashlib.sha256(Path(__file__).with_name('right-direct.tex').read_bytes()).hexdigest(),
 'scope':'Five actual iid laws at n200/201 with full outward signed CDF controls; no parameter coverage or acquisition assertion. Reused occupancy/normal kernel is disclosed.'},indent=2))

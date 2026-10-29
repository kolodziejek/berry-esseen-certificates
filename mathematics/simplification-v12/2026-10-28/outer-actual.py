"""Actual iid atom/collision controls in the new outer-phase noise range.

Exact enumeration and rational normal enclosures, not a uniform proof.
Earlier arithmetic helpers are explicitly reused, not called independent.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
root=Path(__file__).resolve().parents[3]
helper=root/'mathematics/simplification-v10/2026-10-28/actual_law_checks.py'
raw=helper.read_bytes();pin='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
assert hashlib.sha256(raw).hexdigest()==pin
ns={'__name__':'exact_event_helpers','__file__':str(helper)};exec(compile(raw,str(helper),'exec'),ns)
law,rare,distribution,exact_event=[ns[k]for k in ['law','rare','distribution','exact_event']]
cases=[];regions=[(F(-34,125),F(-3,20)),(F(0),F(3,40)),(F(3,40),F(3,20)),(F(3,20),F(91,125))]
for n,p,side in [(42,F(2,5),0),(42,F(53,100),1),(43,F(1,2),2)]:
    noises=[[(F(0),F(1))],[(F(0),F(1))]]
    if side==2:noises=[[(F(-1,30),F(1,2)),(F(1,30),F(1,2))]]*2
    else:noises[side]=rare(F(3,5),F(1,150)) if side==0 else [(-u,w)for u,w in rare(F(3,5),F(1,150))]
    assert all(abs(u)<=F(3,5)for z in noises for u,w in z)
    inward=max(F(0),max(u for u,w in noises[0]))+max(F(0),max(-u for u,w in noises[1]))
    assert inward<=F(9,125)
    atoms=law(p,*noises);var=sum((x-p)**2*w for x,w in atoms);lam=n*(var-p*(1-p))
    assert F(3,100)<lam<=F(3,40)
    third=sum(abs(x-p)**3*w for x,w in atoms)
    dist,den=distribution(atoms,n);cdf=0;eligible=[[]for _ in regions]
    for x,mass in dist:
        cdf+=mass;k=(x+F(34,125)).numerator//(x+F(34,125)).denominator;u=x-k
        if (x-n*p)**2>F(46,25)**2*var:continue
        for j,(lo,hi)in enumerate(regions):
            if lo<=u<=hi:
                z={'threshold':x,'cdf':F(cdf,den),'jump':F(mass,den),'k':k,'variance':var,'third_raw':third,'lambda':lam}
                eligible[j].append((abs(u-(lo+hi)/2),z))
    for j,possibles in enumerate(eligible):
        if not possibles:continue
        z=min(possibles,key=lambda pair:pair[0])[1];result=exact_event(atoms,n,p,z)
        cases.append({'n':n,'p':str(p),'side':side,'lambda':str(lam),'inward_sum':str(inward),
          'phase':str(z['threshold']-z['k']),'region':j,'threshold':str(z['threshold']),
          'jump':str(z['jump']),'collisions':side==2,**result})
assert len(cases)>=8 and {c['region']for c in cases}==set(range(4)) and any(c['collisions']for c in cases)
assert hashlib.sha256(helper.read_bytes()).hexdigest()==pin
print(json.dumps({'status':'PASS_EXACT_IID_OUTER_PHASE_EVENTS','scope':'Selected atom thresholds in .03<lambda<=.075; direct exact Delta controls, not uniform coverage',
 'helper_source_sha256':pin,'independent_implementation':False,'cases':cases,'python':sys.version},indent=2))

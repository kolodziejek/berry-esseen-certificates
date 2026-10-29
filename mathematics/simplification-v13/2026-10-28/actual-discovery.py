"""Bounded actual-iid larger-noise exploration; floating scores are NOT proof.

Atom locations, probabilities and collisions are exact. The normal function
and optimization scores are ordinary floats. Never use this as acceptance.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb, erf, pi, sqrt
import hashlib, json, sys
if not __debug__ or sys.flags.optimize: raise RuntimeError('Assertions required')
root=Path(__file__).resolve().parents[3]
helper=root/'mathematics/simplification-v10/2026-10-28/actual_law_checks.py'
raw=helper.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
ns={'__name__':'arithmetic_helpers','__file__':str(helper)}
exec(compile(raw,str(helper),'exec'),ns)
distribution,law=ns['distribution'],ns['law']
ce=(3+sqrt(10))/(6*sqrt(2*pi))
Phi=lambda x:(1+erf(x/sqrt(2)))/2
def centered(lo,hi):
    if not lo or not hi:return [(F(0),F(1))]
    return [(-lo,hi/(lo+hi)),(hi,lo/(lo+hi))]
records=[];skipped=0
for p in map(F,['.25','.3','.4','.42','.5','.53']):
    n=42;q=1-p;A=F('.7')if p<F('.4')else F('.6')
    inward=F('.068')if p<F('.4')else F('.072')
    shift=F('.218')if p<F('.4')else F('.272')
    v=p*q;rhoB=float(1-2*v)/sqrt(float(v))
    fb=[];acc=0.
    for j in range(n+1):
        acc+=float(F(comb(n,j))*p**j*q**(n-j))
        fb.append(sqrt(n)*(acc-Phi(float(j-n*p)/sqrt(n*float(v))))-ce*rhoB)
    bestB=max(fb)
    for lam in map(F,['.1','.25','.4','.6']):
        for w in [F(0),F(1,2),F(1)]:
            a0=lam*(1-w)/(n*q*A);a1=lam*w/(n*p*A)
            if a0+a1>inward:skipped+=1;continue
            atoms=law(p,centered(A,a0),centered(a1,A))
            var=sum((x-p)**2*mass for x,mass in atoms)
            third=sum(abs(x-p)**3*mass for x,mass in atoms)
            assert var==v+lam/n
            rho=float(third)/float(var)**1.5
            dist,den=distribution(atoms,n);cdf=0
            maximum=None;largest_excess=None;events=0
            for x,mass in dist:
                cdf+=mass
                if (x-n*p)**2>F('1.84')**2*var:continue
                events+=1;k=(x+shift).__floor__()
                excess=sqrt(n)*(float(F(cdf,den))-Phi(float(x-n*p)/sqrt(n*float(var))))-ce*rho
                delta=excess-fb[k]
                row={'threshold':str(x),'phase':str(x-k),'k':k,'delta_diagnostic':delta,
                     'excess_diagnostic':excess,'best_anchor_delta_diagnostic':excess-bestB,
                     'jump_diagnostic':float(F(mass,den))}
                if maximum is None or delta>maximum['delta_diagnostic']:maximum=row
                if largest_excess is None or excess>largest_excess['excess_diagnostic']:largest_excess=row
            assert events
            records.append({'n':n,'p':str(p),'A':str(A),'lambda':str(lam),'w':str(w),
                            'inward':str(a0+a1),'atoms':[[str(x),str(m)]for x,m in atoms],
                            'count':len(dist),'eligible_events':events,'worst_local_comparison':maximum,
                            'largest_excess':largest_excess})
print(json.dumps({'status':'DISCOVERY_ONLY','scope':'Actual finite iid sums and exact collisions, floating normal scores, no uniform coverage',
                  'cases':records,'skipped_inward':skipped,'python':sys.version},indent=2))

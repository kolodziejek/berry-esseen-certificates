"""Rationally enclose eight selected larger-noise iid event comparisons.

Discovery selected the events; acceptance recomputes atom masses and moments.
No maximization or continuous-domain claim is made.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
root=Path(__file__).resolve().parents[3]
helper=root/'mathematics/simplification-v10/2026-10-28/actual_law_checks.py'
raw=helper.read_bytes();assert hashlib.sha256(raw).hexdigest()=='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
ns={'__name__':'arithmetic_helpers','__file__':str(helper)};exec(compile(raw,str(helper),'exec'),ns)
source=root/'runs/simplification-v13-20261028/actual01/stdout.json'
rows=json.loads(source.read_text())['cases'];selected=[]
for p,lam,w in [('3/10','1/10','1'),('1/4','1/10','1'),('2/5','3/5','0'),('21/50','3/5','1/2'),
                ('1/2','3/5','1'),('53/100','3/5','1/2'),('1/4','2/5','1/2'),('3/10','3/5','0')]:
    row=next(r for r in rows if(r['p'],r['lambda'],r['w'])==(p,lam,w))
    n=row['n'];p=F(p);atoms=[(F(x),F(z))for x,z in row['atoms']]
    assert sum(z for x,z in atoms)==1 and sum(x*z for x,z in atoms)==p
    var=sum((x-p)**2*z for x,z in atoms);third=sum(abs(x-p)**3*z for x,z in atoms)
    assert n*(var-p*(1-p))==F(lam)
    event=row['worst_local_comparison'];x=F(event['threshold']);k=event['k']
    assert (x-n*p)**2<=F('1.84')**2*var
    dist,den=ns['distribution'](atoms,n)
    cdf=sum(m for y,m in dist if y<=x);jump=sum(m for y,m in dist if y==x)
    assert jump>0
    z={'threshold':x,'k':k,'cdf':F(cdf,den),'jump':F(jump,den),'variance':var,'third_raw':third,'lambda':F(lam)}
    result=ns['exact_event'](atoms,n,p,z)
    selected.append({'n':n,'p':str(p),'lambda':lam,'w':w,'threshold':str(x),'phase':str(x-k),**result})
print(json.dumps({'status':'PASS_EIGHT_EXACT_LARGER_NOISE_EVENTS','scope':'Eight actual iid closed events with rational normal/root/CE enclosures; not uniform comparison or optimizer certification',
                  'discovery_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256(raw).hexdigest(),
                  'independent_implementation':False,'selected':selected,'python':sys.version},indent=2))

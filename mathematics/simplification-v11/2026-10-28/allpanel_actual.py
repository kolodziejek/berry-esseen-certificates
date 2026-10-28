"""Exact selected-event controls for the new all-panel comparison.

Reuses the source-pinned v10 rational kernel, not an independent implementation.
Floating score discovery selects an event; all acceptance arithmetic is rational.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize: raise RuntimeError('Assertions required')
helper=Path(__file__).resolve().parents[2]/'simplification-v10/2026-10-28/actual_law_checks.py'
pin='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
blob=helper.read_bytes();assert hashlib.sha256(blob).hexdigest()==pin
ns={'__name__':'v11_event_helpers','__file__':str(helper)}
exec(compile(blob,str(helper),'exec'),ns)
law,rare,discovery,exact_event=[ns[k]for k in ['law','rare','discovery','exact_event']]
cases=[]
for p,side in [(F(1,4),0),(F(13,50),1),(F(3,10),0),(F(39,100),1),(F(13,50),2)]:
 n=42;noises=[[(F(0),F(1))],[(F(0),F(1))]]
 if side==2:noises[0]=[(F(-1,1000),F(1,2)),(F(1,1000),F(1,2))]
 else:
  noises[side]=rare(F(7,10),F(1,10000))
  if side==1:noises[side]=[(-u,w)for u,w in noises[side]]
 assert all(abs(u)<=F(7,10)for z in noises for u,w in z)
 a0=max(F(0),max(u for u,w in noises[0]));a1=max(F(0),max(-u for u,w in noises[1]))
 assert a0+a1<=F(17,250)
 atoms=law(p,*noises);z=discovery(atoms,n,p)
 # The earlier helper's anchor is not applicable to the new phase interval.
 anchor=z['threshold']+F(109,500)
 z['k']=anchor.numerator//anchor.denominator;z['phase']=z['threshold']-z['k']
 assert F(1,4)<=p<=F(53,100) and n>=42
 assert 0<z['lambda']<=F(1,500)
 assert (z['threshold']-n*p)**2<F(46,25)**2*z['variance']
 assert -F(109,500)<=z['phase']<=F(391,500) and 1<=z['k']<=n-1
 result=exact_event(atoms,n,p,z)
 cases.append({'n':n,'p':str(p),'noise_type':side,'lambda':str(z['lambda']),
 'threshold':str(z['threshold']),'phase':str(z['phase']),'inward_sum':str(a0+a1),
 'atom_count':z['atom_count'],**result})
assert hashlib.sha256(helper.read_bytes()).hexdigest()==pin
print(json.dumps({'status':'PASS_ALLPANEL_EXACT_SELECTED_EVENTS','cases':cases,
 'source_sha256':pin,'python':sys.version,'independent_implementation':False,
 'scope':'Five actual iid events, including adverse rho and both rare-noise signs; no claim to certify the floating maximizer or the universal theorem by sampling.'},indent=2))

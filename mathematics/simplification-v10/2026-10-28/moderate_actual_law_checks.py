"""Exact selected-event controls in the newly proved noise interval.

Reuses our earlier rational event arithmetic; not an independent second
implementation and not a numerical proof of the uniform theorem.
"""
from pathlib import Path
import hashlib
import json
import sys
from fractions import Fraction as F
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions required')
helper=Path(__file__).with_name('actual_law_checks.py')
blob=helper.read_bytes()
assert hashlib.sha256(blob).hexdigest()=='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
ns={'__name__':'v10_exact_event_helpers','__file__':str(helper)}
exec(compile(blob,str(helper),'exec'),ns)
law,rare,discovery,exact_event=[ns[k] for k in ['law','rare','discovery','exact_event']]
cases=[]
for n,p,side,e in [(42,F(2,5),0,F(1,500)),(42,F(53,100),1,F(1,500)),
                  (100,F(21,50),0,F(1,2000)),(42,F(1,2),None,None)]:
    noises=[[(F(0),F(1))],[(F(0),F(1))]]
    if side is None:
        noises=[[(F(-1,50),F(1,2)),(F(1,50),F(1,2))]]*2
    else:
        noises[side]=rare(F(3,5),e) if side==0 else [(-u,w) for u,w in rare(F(3,5),e)]
    assert all(abs(u)<=F(3,5) for z in noises for u,w in z)
    a0=max(F(0),max(u for u,w in noises[0]))
    a1=max(F(0),max(-u for u,w in noises[1]))
    assert a0+a1<=F(9,125)
    atoms=law(p,*noises);z=discovery(atoms,n,p)
    assert F(2,5)<=p<=F(53,100) and n>=42
    assert F(1,500)<z['lambda']<=F(1,50)
    assert (z['threshold']-n*p)**2<F(46,25)**2*z['variance']
    assert -F(34,125)<=z['phase']<=F(91,125) and 1<=z['k']<=n-1
    result=exact_event(atoms,n,p,z)
    cases.append({'n':n,'p':str(p),'side':side,'rare_mass':str(e),
                  'lambda':str(z['lambda']),'inward_sum':str(a0+a1),
                  'threshold':str(z['threshold']),'phase':str(z['phase']),
                  'atom_count':z['atom_count'],**result})
assert hashlib.sha256(helper.read_bytes()).hexdigest()=='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
print(json.dumps({'status':'PASS_EXACT_SELECTED_MODERATE_NOISE_EVENTS',
 'scope':'Four selected actual iid events in .002<lambda<=.02. Every premise and accepted probability/normal comparison is rational; floating maximizer discovery is not certified.',
 'helper_source_sha256':'351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07','independent_implementation':False,
 'cases':cases,'python':sys.version},indent=2))

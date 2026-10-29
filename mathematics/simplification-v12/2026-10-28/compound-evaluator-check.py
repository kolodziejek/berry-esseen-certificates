"""Bounded exact regression and fail-closed controls for the evaluator."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
p=Path(__file__).with_name('compound-evaluator.py')
raw=p.read_bytes();scope={'__name__':'compound_exact','__file__':str(p)}
exec(compile(raw,str(p),'exec'),scope)
exp_bounds=scope['exp_bounds'];moment=scope['hinge_moment'];tail=scope['tail_box']
cases=0
for mu in [F(0),F(1,100),F(1,5)]:
 for nu in [F(0),F(1,3),F(4),F(15)]:
  mean=25*mu+3*nu;var=625*mu+9*nu
  for K in [0,1,3,25,40,75]:
    lo,hi=moment(mu,nu,K)
    assert 0<=lo<=hi<=var+(mean-K)**2
    if K==0:assert lo==hi==var+mean**2
    if mu==nu==0:assert lo==hi==0
    # Positive finite-tail partial sum is an independently evaluated lower
    # bound, not an approximation to the missing tail.
    elo,_=exp_bounds(-mu-nu);lower=F(0)
    pm=F(1)
    for j in range(9):
      if j:pm*=mu/j
      pn=F(1)
      for k in range(61):
        if k:pn*=nu/k
        lower+=max(0,25*j+3*k-K)**2*pm*pn
    assert elo*lower<=hi
    cases+=1
for x in [F(-20),F(-1),F(-1,3),F(0),F(1,3),F(1),F(20)]:
    lo,hi=exp_bounds(x);rlo,rhi=exp_bounds(-x)
    assert lo*rlo<=1<=hi*rhi and hi-lo<F(1,10**10)
assert tail(0,0,0,0,F(1),10)==0
good=tail(F(1,10),F(1,5),F(1),F(2),F(1),30)
assert 0<good<=1
bad=[lambda:tail(F(1,5),F(1,10),0,1,1,0),
     lambda:tail(0,1,0,1,1,100),
     lambda:tail(0,1,-1,1,1,0),
     lambda:tail(0,1,0,1,0,0),
     lambda:moment(F(1,5),0,-1),
     lambda:moment(.2,0,1),
     lambda:moment(0,0,1,0,3)]
# Populate equal-valued exact cache keys before testing malformed float/bool
# arguments. A cache hit must not bypass the type checks.
moment(F(1,2),0,1);moment(0,0,1);exp_bounds(F(1,2));exp_bounds(1)
bad.extend([lambda:moment(.5,0,1),lambda:moment(False,0,1),
            lambda:exp_bounds(.5),lambda:exp_bounds(True)])
for call in bad:
    try:call()
    except (ValueError,TypeError):pass
    else:raise AssertionError('Malformed input accepted')
print(json.dumps({'status':'PASS_COMPOUND_HINGE_EVALUATOR_CONTROLS','point_moment_cases':cases,'malformed_rejections':len(bad),'source_sha256':hashlib.sha256(raw).hexdigest(),'scope':'Complete-tail evaluator controls only; no continuous count comparison or new noise interval claimed.','python':sys.version},indent=2))

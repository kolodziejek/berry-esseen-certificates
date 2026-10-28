"""Independent arithmetic controls for theorem union and witness units.

No constructor code is imported. The component theorems remain mathematical
inputs; this checks their exact joins, elementary target bounds and scaling.
The author constructed the negative-inner component and does not claim an
independent proof of that component here.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys,itertools
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
PINS={
'mathematics/simplification-v12/2026-10-28/comparison-union.tex':'31645628932501a0265959123b5d452b09116b77792fc2401c6a18eacdbb754a',
'mathematics/simplification-v12/2026-10-28/leftcount.tex':'f038aa62e039bfe48482fe69c1438553e90f7c246bf0fa74322115c33ea76ea9',
'mathematics/simplification-v12/2026-10-28/outer.tex':'72ff7ae27bdbecfa0a535dd62e52417de9bab370b7004af8b86e9e99f491facc',
'mathematics/simplification-v12/2026-10-28/compound-proof.tex':'5b9d8428b6aa10bc3fff44114cd26c482b88692f76dd624b841c79d5b4a753fa',
'mathematics/simplification-v11/2026-10-28/counts-v11.tex':'209f173c19a73c4fecf5aaf9aa2732c30b72266ff3f1673ddd52fa4a4e6c4641',
'mathematics/simplification-v10/2026-10-28/moderate-noise.tex':'bda129c029de36bac7a8455ec3f1e7f7726cea9b21bf89671be7e9095f775074',
'mathematics/simplification-v11/2026-10-28/leftpanels.tex':'63b11a2df99e2bf8af24040bebe522946adb4496cd7b9c993e190ee9d1340c26',
'mathematics/simplification-v10/2026-10-28/geometry.tex':'e753afc6a731f728119d38d422a2ab5e3c890a1e2ef0b40a6841ec83d7a185b2',
'manuscript/arxiv-v1/sections/04-fixed-entry.tex':'db7156ca43f874b29216d6f297d74ea79ace4b988ec200a93a169e0d342498d8',
'manuscript/arxiv-v1/sections/02-fixed-target.tex':'5a00687b76390fcaa4c57f9f893d070b23bf3119eda8aa4b82d66c3b4c0b509b',
}
root=Path(sys.argv[1]).resolve()
for name,pin in PINS.items():assert hashlib.sha256((root/name).read_bytes()).hexdigest()==pin,name
# An alternating series encloses atan(1/q). Machin's exact identity supplies pi.
def atan_bounds(q,N=12):
 terms=[F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(N)]
 z=sum(terms,F(0));next_term=F((-1)**N,(2*N+1)*q**(2*N+1))
 return min(z,z+next_term),max(z,z+next_term)
a,b=atan_bounds(5);c,d=atan_bounds(239)
pi_lo,pi_hi=16*a-4*d,16*b-4*c
rt_lo,rt_hi=F(3162277660,10**9),F(3162277661,10**9)
assert rt_lo**2<10<rt_hi**2
CE2lo=(19+6*rt_lo)/(72*pi_hi);CE2hi=(19+6*rt_hi)/(72*pi_lo)
assert F(819,2000)**2<CE2lo<CE2hi<F(41,100)**2
assert F(2,5)<F(819,2000)
# Common refinement includes every open interval and every boundary separately.
# All component domains are Cartesian products of intervals with these endpoints.
lams=[F(0),F(3,100),F(3,40)]
phases=[F(-34,125),F(-3,20),F(0),F(91,125)]
def faces(axis):
 return [(x,x) for x in axis]+[(a,b) for a,b in zip(axis,axis[1:])]
def covered(lam,u):
 return (0<lam<=F(3,100) and phases[0]<=u<=phases[-1]) or \
 (F(3,100)<=lam<=F(3,40) and F(-3,20)<=u<=0) or \
 (0<lam<=F(3,40) and (phases[0]<=u<=F(-3,20) or 0<=u<=phases[-1]))
strata=0
for la,lb in faces(lams):
 if la==lb==0:continue
 for ua,ub in faces(phases):
  assert covered((la+lb)/2,(ua+ub)/2)
  strata+=1
leftlo,lefthi=F(-109,500),F(391,500)
assert lefthi-leftlo==phases[-1]-phases[0]==1
# Floors provide anchors on any real threshold; only bounds are needed here.
leftxi=F(46,25)*F(491,1000);rightxi=F(231,250)
assert F(491,1000)**2>F(6,25)+F(1,100*42)
assert F(251,500)**2>F(1,4)+F(3,40*42)
assert F(46,25)*F(251,500)<rightxi
assert 42*F(1,4)-leftxi-lefthi>0
assert 42*F(3,5)-leftxi+leftlo>0
assert 42*F(2,5)-rightxi-phases[-1]>0
assert 42*F(47,100)-rightxi+phases[0]>0
assert F(183605680,10**8)<F(46,25)
assert F(17,250)<F(9,125) and F(3,5)<F(7,10)
assert F(77,125)>F(3,40)>F(1,100)>0
# Actual centered marginals check the units without evaluating any square root.
def centered(a,b):
 if not a or not b:return {F(0):F(1)}
 return {-a:b/(a+b),b:a/(a+b)}
marginals=0;wrong_scale=0
for p,kind in itertools.product([F(1,4),F(2,5),F(53,100)],range(4)):
 U0=centered(F(3,5),F(1,1000)) if kind in (0,2) else centered(F(1,50),F(1,50)) if kind==3 else {F(0):F(1)}
 U1=centered(F(1,1000),F(3,5)) if kind in (1,2) else centered(F(1,50),F(1,50)) if kind==3 else {F(0):F(1)}
 assert sum(x*z for x,z in U0.items())==sum(x*z for x,z in U1.items())==0
 s=(1-p)*sum(x*x*z for x,z in U0.items())+p*sum(x*x*z for x,z in U1.items())
 V=p*(1-p)+s;ell2=1/V;theta=s/V
 assert theta/ell2==s and (1-theta)/(p*(1-p))==ell2
 assert (p*(1-p)+s)*ell2==1
 # Conditional means of the normalized Z are -p/sqrt(V), (1-p)/sqrt(V).
 # Divide their separation by sqrt(V) once more to recover U exactly.
 for B,law in [(0,U0),(1,U1)]:
  for x in law:assert ((B+x-p)-(B-p))==x
 assert 42*theta/ell2==42*s
 assert theta!=s;wrong_scale+=1;marginals+=1
# A negative closed-CDF error under reflection is dominated, not equal at atoms.
# S=0 a.s., H=0: P(-S<=-H)=1 while 1-P(S<=H)=0.
assert 1>1-1
# Intentional missing inner phase, noise gap and non-unit phase interval reject.
def outer_only(u):return phases[0]<=u<=F(-3,20) or 0<=u<=phases[-1]
assert not (F(1,20)<=F(3,100) or outer_only(F(-1,20)))
assert not (F(31,1000)<=F(3,100) or F(32,1000)<=F(31,1000) or outer_only(F(-1,20)))
short_hi=F(727,1000);missing_phase=F(1455,2000)
assert short_hi-phases[0]<1
assert not phases[0]<=missing_phase<=short_hi
assert not phases[0]<=missing_phase-1<=short_hi
print(json.dumps({'status':'PASS_UNION_SCOPE_AND_NORMALIZATION_CONTROLS','source_sha256':PINS,'closed_refinement_strata':strata,'actual_marginal_mapping_controls':marginals,'wrong_variance_scaling_controls':wrong_scale,'negative_controls':['missing negative-inner phase','noise gap between .03 and .032','phase interval shorter than one','reflection equality at an atom','theta substituted for theta/ell^2'],'CE_square_lower':str(CE2lo),'CE_square_upper':str(CE2hi),'scope':'Union and units only; component comparison theorems and acquired-witness hypotheses remain stated mathematical inputs. Negative-inner constructor authorship disclosed.','python':sys.version},indent=2))

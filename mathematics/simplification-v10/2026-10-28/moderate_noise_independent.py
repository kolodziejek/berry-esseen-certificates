#!/usr/bin/env python3
"""Independent bounded arithmetic and actual-law controls for moderate noise.

No constructor is imported or executed. The two full quartic rectangles are
proved using tensor Bernstein coefficients, rather than a quadratic lower
bound and its vertex. Other checks reconstruct the terminal inequalities
and test exact actual marginals; neither replaces the analytic review.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions required')

root=Path(sys.argv[1]).resolve()
folder=root/'mathematics/simplification-v10/2026-10-28'
required_sources=[folder/'moderate-noise.tex',folder/'moderate_noise_check.py']
assert all(p.is_file() for p in required_sources), 'Missing reviewed source'
A=Q(3,5); alpha=Q(1,2); den=5*alpha**4
noise=Q(1,50); tmax=Q(89,84)*noise

def coefficients(sign,slope,target):
    return {(0,0):(3*alpha**2-A*A)/den-target,
            (0,1):-3/den,(1,0):2*sign/(5*alpha)+slope,
            (1,1):-4*A/den,(2,1):3*alpha**2/den,
            (2,2):-6/den,(4,3):-1/den}

rectangles=[]
for name,sign,slope,zmax,target in [
        ('negative',1,-Q(21,20),Q(2),Q(3,8)),
        ('positive',-1,Q(19,20),Q(3,2),Q(1))]:
    power=coefficients(sign,slope,target)
    bernstein=[]
    for k in range(5):
        for l in range(4):
            value=sum(c*zmax**i*tmax**j*Q(comb(k,i),comb(4,i))
                      *Q(comb(l,j),comb(3,j))
                      for (i,j),c in power.items() if i<=k and j<=l)
            assert value>0
            bernstein.append(value)
    rectangles.append({'name':name,'coefficients':list(map(str,bernstein)),
                       'minimum_margin':str(min(bernstein))})

# A genuinely false stronger bound, not merely a failed proof procedure.
p=coefficients(1,-Q(21,20),Q(0))
negative_corner=sum(c*Q(2)**i*tmax**j for (i,j),c in p.items())
assert negative_corner<Q(1,2)

# At integer r>=1, (r-1)(r-2)>=0 proves r^2<=C(r+2,3).
# The binomial increases with its anchor i>=2, so this is the complete
# factorial-majorant argument. Finite values below are adversarial controls.
for i in range(2,12):
    for r in range(1,30):
        assert r*r<=comb(i+r,i+1)
assert 3*3>comb(1+3,2)  # The same factorial bound is false at anchor 1.

def rest(mu,h):
    b=(1-h/2)/A-1
    assert b>0 and 3*mu<1
    return mu**3/(3*(b+mu)**2*(1-3*mu))

def all_tails(mu,h):
    a=(1-h)/A-1
    assert a>mu>0
    return (mu**2/2+mu**3/6)/(a+mu)**2+rest(mu,h)

mi=Q(9,8)*noise/A**2; mg=Q(7,6)*noise/A**2
inner=Q(1,20); far=Q(91,125); near=Q(1,10)
inner_bracket=Q(3,8)*Q(79,84)-Q(53,50)*all_tails(mi,inner)/noise
inner_margin=Q(73,100)*inner_bracket-Q(1,21)-Q(1,100)
assert inner_bracket>0 and inner_margin>0

own_variance=Q(11,10)*noise
neg=lambda r:r*r/(own_variance+r*r)-Q(5,4)*r
neg_bracket=min(neg(inner),neg(Q(34,125)))-Q(3,2)*all_tails(mg,Q(0))
neg_margin=Q(13,20)*neg_bracket-Q(3,42)*noise-noise/100
assert neg_bracket>0 and neg_margin>0
assert 2*inner*own_variance/(own_variance+inner**2)**2>Q(5,4)

incoming_variance=Q(7,6)*noise
cantelli=lambda u:incoming_variance/(incoming_variance+(1-u)**2)
near_bracket=Q(19,20)*inner-Q(3,2)*(cantelli(near)+rest(mg,near))
near_margin=Q(13,20)*near_bracket-Q(3,42)*noise-noise/100
assert near_bracket>0 and near_margin>0
assert 3*(1-far)**2>incoming_variance
far_base=min(Q(9,10)*u-Q(3,2)*cantelli(u) for u in (near,far))
far_bracket=far_base-Q(3,2)*rest(mg,far)
far_margin=Q(13,20)*far_bracket-Q(3,42)*noise-noise/100
assert far_bracket>0 and far_margin>0

# The first Poisson hinge really has a positive cubic correction. Taylor's
# global fourth-degree upper bound for exp(-mu) proves the following lower
# bound; retaining only mu^2/2 would understate the expectation.
mu=Q(1,16)
poisson_hinge_lower=mu**2/2+mu**3/6-mu**4/24
assert poisson_hinge_lower>mu**2/2

def conditional_sum(count,atoms):
    result={Q(0):Q(1)}
    for _ in range(count):
        nxt={}
        for x,mass in result.items():
            for y,prob in atoms:
                nxt[x+y]=nxt.get(x+y,Q(0))+mass*prob
        result=nxt
    return result

actual=[]
for n in (42,43):
    for prob in (Q(2,5),Q(53,100)):
        for lam in (Q(1,50),Q(1,500),Q(1,10**8)):
            for allocation in ('both','negative','positive'):
                q=1-prob; v=prob*q; s=lam/n
                a0=s/A if allocation=='both' else s/(q*A) if allocation=='negative' else Q(0)
                a1=s/A if allocation=='both' else s/(prob*A) if allocation=='positive' else Q(0)
                c0=[(-A,a0/(A+a0)),(a0,A/(A+a0))] if a0 else [(Q(0),Q(1))]
                c1=[(A,a1/(A+a1)),(-a1,A/(A+a1))] if a1 else [(Q(0),Q(1))]
                assert a0+a1<=Q(9,125) and a0<prob and a1<q
                assert sum(x*w for x,w in c0)==sum(x*w for x,w in c1)==0
                assert q*sum(x*x*w for x,w in c0)+prob*sum(x*x*w for x,w in c1)==s
                third=q*sum(abs(x-prob)**3*w for x,w in c0)+prob*sum(abs(1+x-prob)**3*w for x,w in c1)
                assert third**2*v>=(1-2*v)**2*(v+s)**3
                k=(n*prob.numerator)//prob.denominator
                s0=conditional_sum(n-k,c0); s1=conditional_sum(k,c1)
                law={}
                for x,w in s0.items():
                    for y,z in s1.items():law[x+y]=law.get(x+y,Q(0))+w*z
                assert sum(law.values())==1 and sum(x*w for x,w in law.items())==0
                t=sum(x*x*w for x,w in law.items())
                assert Q(79,84)*lam<=t<=Q(89,84)*lam
                assert abs(sum(x**3*w for x,w in law.items()))<=A*t
                assert sum(x**4*w for x,w in law.items())<=A*A*t+3*t*t
                collision=(n-k)*a0-k*a1
                assert law[collision]>0
                cases=0
                for u in (Q(0),-2*t,2*t,collision):
                    assert abs(u)<=inner
                    assert (k-n*prob+u)**2<=Q(46,25)**2*(v+s)
                    tail=sum(w for x,w in law.items() if x>u)
                    r=abs(u); sign=-1 if u>=0 else 1
                    quartic=((3*alpha**2-A*A)*t-3*t*t-4*A*r*t-6*r*r*t-r**4+3*alpha**2*r*r+2*sign*alpha**3*r)/den
                    assert quartic<=tail
                    f_lower=(Q(19,20) if u>=0 else Q(21,20))*u
                    assert tail+f_lower>Q(3,8)*t
                    cases+=1
                strict=sum(w for x,w in law.items() if x>collision)
                closed=sum(w for x,w in law.items() if x>=collision)
                assert closed-strict==law[collision]>0
                actual.append({'n':n,'p':str(prob),'lambda':str(lam),
                               'allocation':allocation,'cases':cases,
                               'collision_mass':str(law[collision])})

sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
print(json.dumps({'status':'PASS_INDEPENDENT_MODERATE_NOISE_REVIEW',
 'constructor_imports':False,'quartic_rectangles':rectangles,
 'final_margins_above_lambda_over_100':{
  'inner_per_lambda':str(inner_margin),'negative_outer':str(neg_margin),
  'positive_near':str(near_margin),'positive_far':str(far_margin)},
 'actual_laws':len(actual),'actual_own_count_cases':sum(z['cases'] for z in actual),
 'actual_law_controls':actual,
 'negative_controls':{
  'false_negative_quartic_constant':'1/2','actual_corner_value':str(negative_corner),
  'anchor1_factorial_majorant_false':True,
  'first_Poisson_hinge_exceeds_quadratic_only_bound':str(poisson_hinge_lower-mu**2/2),
  'strict_and_closed_own_events_distinguished':len(actual)},
 'source_sha256':{p.name:sha(p) for p in required_sources},
 'script_sha256':sha(Path(__file__)), 'python':sys.version},indent=2))

"""Exact controls on a distribution-free renewal derivation, not a BE proof."""
from fractions import Fraction as F
from math import comb
import json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
def step(dist,law):
    out={}
    for x,w in dist.items():
        for d,p in law:out[x+d]=out.get(x+d,F(0))+w*p
    assert sum(out.values())==1
    return out
def check(law,t):
    assert sum(p for d,p in law)==1 and sum(d*p for d,p in law)==1
    lo=min(d for d,p in law);hi=max(d for d,p in law);b=1-hi+lo
    assert lo>0 and b>=0 and t>=0
    dist={F(0):F(1)};en=F(0);hsum=F(0);age=F(0);mass=F(0)
    def h(x):return sum(p for d,p in law if d>x)-sum(max(d-x,0)*p for d,p in law)
    for j in range(t//lo+1):
        for x,p in dist.items():
            if x>t:continue
            if j:en+=p
            y=t-x;surv=sum(q for d,q in law if d>y)
            hsum+=p*h(y);age+=p*min(y,b)*surv;mass+=p*surv
        dist=step(dist,law)
    g=t-en
    assert mass==1 and g==hsum and g>=age>=0
    return g
laws=[[(F(1),F(1))],[(F(24,25),F(15,16)),(F(8,5),F(1,16))],
      [(F(233,250),F(175,192)),(F(17,10),F(17,192))],
      [(F(1,2),F(1,2)),(F(3,2),F(1,2))],
      [(F(19,20),F(1,2)),(F(1),F(1,4)),(F(11,10),F(1,4))]]
checks=0;zeros=0
for law in laws:
    dist={F(0):F(1)};thresholds={F(0),F(1,100),F(1,2),F(5,2),F(7)}
    for j in range(1,5):
        dist=step(dist,law)
        for x in dist:
            thresholds.add(x)
            if x>F(1,10000):thresholds.add(x-F(1,10000))
    for t in sorted(thresholds):
        g=check(law,t);checks+=1;zeros+=g==0
# Exact finite iid identity (6), with binomial weights and closed collisions.
identities=0
for law in laws:
    n=6;p=F(2,5);dist={F(0):F(1)};dists=[dist]
    for j in range(n):dist=step(dist,law);dists.append(dist)
    for t in [F(0),F(19,20),F(1),F(3,2),F(5,2)]:
        assert 0<=t<n*min(d for d,p in law)
        cdfs=[sum(w for x,w in z.items()if x<=t)for z in dists]
        actual=sum(F(comb(n,j))*p**j*(1-p)**(n-j)*cdfs[j]for j in range(n+1))
        fb=[sum(F(comb(n,l))*p**l*(1-p)**(n-l)for l in range(j+1))for j in range(n)]
        crossing=sum(fb[j]*(cdfs[j]-cdfs[j+1])for j in range(n))
        assert actual==crossing;identities+=1
# False width-free statement: the second renewal exceeds the evaluation point.
bad=[(F(9,10),F(19,21)),(F(39,20),F(2,21))]
assert sum(d*p for d,p in bad)==1 and F(19,21)-F(9,10)==F(1,210)>0
assert check(laws[0],F(7,3))==F(1,3)>0
# Exact domain arithmetic for the acquired one-sided application.
assert F(1,4)+F(77,125)/42<F(103,200)**2
assert F(46,25)*F(103,200)<F(237,250)
assert F(1,4)*42>F(237,250)
assert (F(116,125)-F(53,100))*42>F(237,250)
print(json.dumps({'status':'PASS_EXACT_RENEWAL_CONTROLS','scope':'Renewal sign/age theorem and one-sided iid identity; no bound on full Delta',
                  'law_count':len(laws),'threshold_controls':checks,'zero_deficits':zeros,'iid_identity_controls':identities,
                  'negative_controls':{'width_free_bias':'1/210','deterministic_centering_error':'1/3'},'python':sys.version},indent=2))

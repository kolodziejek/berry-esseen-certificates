"""Bounded deterministic controls. Floating scores are diagnostics only."""
from fractions import Fraction as F
from math import sqrt, erf
import json

def convolution(vals, weights, n):
    total=sum(weights); law={F(0):1}
    for _ in range(n):
        nxt={}
        for a,p in law.items():
            for b,q in zip(vals,weights):
                nxt[a+b]=nxt.get(a+b,0)+p*q
        law=nxt
    assert sum(law.values())==total**n
    return law,total**n

def score(vals,weights,n):
    den=sum(weights); mean=sum(F(w,den)*x for x,w in zip(vals,weights))
    var=sum(F(w,den)*(x-mean)**2 for x,w in zip(vals,weights))
    third=sum(F(w,den)*abs(x-mean)**3 for x,w in zip(vals,weights))
    law,total=convolution(vals,weights,n); partial=0; best=(-1,None,None)
    for raw,mass in sorted(law.items()):
        z=float(raw-n*mean)/sqrt(n*float(var)); normal=(1+erf(z/sqrt(2)))/2
        left=partial/total;partial+=mass;right=partial/total
        for sign,d in [('closed',right-normal),('reflected',normal-left)]:
            value=sqrt(n)*float(var)**1.5/float(third)*d
            if value>best[0]:best=(value,str(raw),sign)
    p=sum(F(w,den) for x,w in zip(vals,weights) if x>mean)
    return {'score':best,'rho':float(third)/float(var)**1.5,'p':str(p),'atoms_in_sum':len(law),'mean':str(mean),'variance':str(var)}

cases=[]
for n in [1,2,4,42]:
    cases += [('symmetric_bernoulli',n,[F(-1),F(1)],[1,1]),('skew_bernoulli',n,[F(0),F(1)],[3,2])]
cases += [('near_pstar_bernoulli',42,[F(0),F(1)],[581,419]),
 ('three_atoms',4,[F(-3),F(-1),F(2)],[1,4,5]),
 ('four_symmetric',4,list(map(F,[-3,-1,1,3])),[1,9,9,1]),
 ('four_asymmetric',4,list(map(F,[-2,-1,1,3])),[2,1,5,2]),
 ('exact_collision',2,[F(-1),F(1),F(1)],[2,1,1]),
 ('near_collision',2,[F(-1),F(1),F(1)+F(1,10**12)],[2,1,1]),
 ('tiny_far_atom',4,list(map(F,[-1,1,1000])),[499999999999,499999999999,2])]
rows=[]
for name,n,vals,weights in cases:
    actual=score(vals,weights,n);p=F(actual['p'])
    skeleton=score([F(0),F(1)],[p.denominator-p.numerator,p.numerator],n)
    if 'bernoulli' in name or name=='exact_collision':
        assert abs(actual['score'][0]-skeleton['score'][0])<1e-12
    rows.append({'name':name,'n':n,'values':list(map(str,vals)),'weights':weights,'actual':actual,'skeleton':skeleton,'excess':actual['score'][0]-skeleton['score'][0]})

# Fixed-location four-atom moment-preserving mass direction.
x=list(map(F,[-3,-1,1,3])); p=[F(1,4)]*4; nu=list(map(F,[-1,3,-3,1]))
assert all(sum(v*y**k for v,y in zip(nu,x))==0 for k in range(3))
f1=2*sum(nu[i]*p[j] for i in range(4) for j in range(4) if x[i]+x[j]<=0)
f2=2*sum(nu[i]*nu[j] for i in range(4) for j in range(4) if x[i]+x[j]<=0)
assert f1==0 and f2==-20
assert sum(nu[i]*abs(x[i])**3 for i in range(4))==0
print(json.dumps({'scope':'15 deterministic law/index controls, no optimizer or random search; normal CDF floating.','cases':rows,'four_atom_direction':{'nodes':list(map(str,x)),'mass_derivative':list(map(str,nu)),'preserved_moments':[0,1,2],'first_event_derivative':str(f1),'second_event_derivative':str(f2),'third_absolute_moment_derivative':'0','feasible_two_sided_epsilon':'abs(epsilon)<1/12','interpretation':'Strict maximum on this one fixed-moment mass line does not establish global optimality.'}},indent=2))

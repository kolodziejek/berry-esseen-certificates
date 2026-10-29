"""Exact independent finite convolutions for the general crossing identity.

This is a control on the elementary proof, not full Delta acceptance.
"""
from fractions import Fraction as F
from math import comb
import itertools,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
def conv(a,b):
    out={}
    for x,p in a.items():
        for y,q in b.items():out[x+y]=out.get(x+y,F(0))+p*q
    assert sum(out.values())==1
    return out
def centered(lo,hi):
    if not lo or not hi:return {F(0):F(1)}
    return {-lo:hi/(lo+hi),hi:lo/(lo+hi)}
def cdf(d,t):return sum(p for x,p in d.items()if x<=t)
cases=[(centered(F('.6'),F('.01')),centered(F('.02'),F('.6'))),
       (centered(F('.7'),F('.03')),centered(F('.03'),F('.7'))),
       (centered(F('.02'),F('.02')),{F(0):F(1)}),
       ({F(0):F(1)},centered(F('.001'),F('.6'))),
       (centered(F('.000001'),F('.000001')),centered(F('.000001'),F('.000001'))),
       ({F(0):F(1)},{F(0):F(1)}),
       ({F('-.02'):F(1,4),F(0):F(1,2),F('.02'):F(1,4)},centered(F('.01'),F('.6')))]
records=[];identities=0;agechecks=0;iidchecks=0;zerogains=0
for ci,(u0,u1)in enumerate(cases):
    assert sum(x*p for x,p in u0.items())==sum(x*p for x,p in u1.items())==0
    a0=max(u0);a1=-min(u1);A=max(u1);b=min(1-A-a1,1-a0-a1)
    assert a0>=0 and a1>=0 and a0+a1<1 and b>=0
    D={1+x:p for x,p in u1.items()}
    def h(x):
        return cdf(u0,x)*(sum(p for d,p in D.items()if d>x)-sum(max(d-x,0)*p for d,p in D.items()))-sum(z*p for z,p in u0.items()if z<=x)
    for n in [2,4,7]:
        pow0=[{F(0):F(1)}];pow1=[{F(0):F(1)}]
        for j in range(n):pow0.append(conv(pow0[-1],u0));pow1.append(conv(pow1[-1],u1))
        dj=[{j+x:p for x,p in conv(pow1[j],pow0[n-j]).items()}for j in range(n+1)]
        vi=[conv(pow1[i-1],pow0[n-i])for i in range(1,n+1)]
        thresholds={F(n,2),F(n,2)-F(1,100000),F(n,2)+F(1,100000),n*a0}
        thresholds.update(x for j in range(n+1)for x in dj[j]if abs(x-F(n,2))<=F(1,20))
        # Deterministic bounded selection; exact proof does not depend on these tests.
        thresholds=sorted(t for t in thresholds if n*a0<=t<n*(1-a1))
        if len(thresholds)>24:thresholds=thresholds[:12]+thresholds[-12:]
        for t in thresholds:
            cdfs=[cdf(d,t)for d in dj]
            assert cdfs[0]==1 and cdfs[-1]==0 and all(x>=y for x,y in zip(cdfs,cdfs[1:]))
            ek=sum(cdfs[1:]);g=t-ek;local=F(0);age=F(0);crossmass=F(0);bias=F(0);localparts=[]
            for i,v in enumerate(vi,1):
                piece=F(0)
                for z,pr in v.items():
                    x=t-(i-1)-z;local+=pr*h(x);piece+=pr*h(x)
                    hstop=sum(max(x-y,0)*w for y,w in u0.items())-sum(max(x-d,0)*w for d,w in D.items())-cdf(D,x)
                    assert h(x)==hstop
                    bias-=pr*sum(y*w for y,w in u0.items()if y<=x)
                    for l,pl in u0.items():
                        for r,pu in u1.items():
                            if l<=x<1+r:
                                crossmass+=pr*pl*pu;age+=pr*pl*pu*min(x-l,b)
                localparts.append(piece)
            assert g==local and crossmass==1 and g>=age>=0 and bias>=0
            identities+=1;agechecks+=1;zerogains+=g==0
            p=F(2,5);marginal={}
            for x,w in u0.items():marginal[x]=marginal.get(x,F(0))+(1-p)*w
            for x,w in u1.items():marginal[1+x]=marginal.get(1+x,F(0))+p*w
            # Actual iid convolution computed without using conditional-count weights.
            actual={F(0):F(1)}
            for j in range(n):actual=conv(actual,marginal)
            fb=[sum(F(comb(n,l))*p**l*(1-p)**(n-l)for l in range(j+1))for j in range(n)]
            expectfb=sum(fb[j]*(cdfs[j]-cdfs[j+1])for j in range(n))
            assert cdf(actual,t)==expectfb;iidchecks+=1
            masses=[F(comb(n,j))*p**j*(1-p)**(n-j)for j in range(n+1)]
            losses=[sum(max(t-x,0)*w for x,w in d.items())for d in dj]
            assert all(localparts[i-1]==losses[i-1]-losses[i]-cdfs[i]for i in range(1,n+1))
            bends=[losses[j]-max(t-j,0)for j in range(n+1)]
            assert all(z>=0 for z in bends)
            k=t.__floor__();u=t-k
            weighted=fb[k]+u*masses[k+1]+sum((masses[j+1]-masses[j])*bends[j]for j in range(1,n))-sum(masses[i]*localparts[i-1]for i in range(1,n+1))
            assert weighted==cdf(actual,t)
        records.append({'case':ci,'n':n,'thresholds':len(thresholds)})
# Direct product-space enumeration of the selected-noise bias, independent of h.
u0=centered(F('.02'),F('.02'));u1={F(0):F(1)};n=2;t=F(1)
directbias=F(0)
for xs in itertools.product(list(u0),repeat=n):
    prob=F(1)
    for x in xs:prob*=u0[x]
    T=[j+sum(xs[j:])for j in range(n+1)]
    k=max(j for j in range(n+1)if T[j]<=t)
    directbias+=prob*(T[k+1]-(k+1))
assert directbias==F(1,100)>0
# Width-free version is false in the interior, including exact collision at t.
bad={F(9,10):F(19,21),F(39,20):F(2,21)}
assert sum(d*p for d,p in bad.items())==1
assert F(19,21)-F(9,10)==F(1,210)>0
# Right and left acquired domain arithmetic; no inference of acquisition itself.
assert F(1,4)+F('.616')/42<F('.515')**2
assert F('1.84')*F('.515')<F('.948')
assert (F('.25')-F('.072'))*42>F('.948')
assert (F('.928')-F('.53'))*42>F('.948')
assert 1-F('.6')-F('.072')==F('.328') and 1-F('.7')-F('.068')==F('.232')
print(json.dumps({'status':'PASS_EXACT_GENERAL_CROSSING_CONTROLS','scope':'Finite identity, sign and age reserve; not the full weighted Berry--Esseen comparison',
                  'conditional_law_pairs':len(cases),'identity_controls':identities,'age_controls':agechecks,'independent_iid_controls':iidchecks,
                  'zero_gains':zerogains,'selected_noise_bias':'1/100','false_width_free_excess':'1/210','cases':records,'python':sys.version},indent=2))

#!/usr/bin/env python3
"""Independent finite-law reconstruction; imports no constructor checker.

Conditional CDFs, actual iid mixture CDF, local kernels, and coupled path
crossings are constructed separately using exact Fractions.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import hashlib, json, sys

checks=[]
controls=[]
cases=0
bias_cases=0
curvature_sign_controls=0

def require(name,x):
    assert x,name
    checks.append(name)

def reject(name,call):
    try: call()
    except (AssertionError,ValueError): controls.append(name); return
    raise AssertionError('accepted invalid inference: '+name)

def must(x): assert x

def centered(a,b):
    assert a>=0 and b>=0
    if not a or not b: return ((Q(0),Q(1)),)
    return ((-a,b/(a+b)),(b,a/(a+b)))

def convolve(a,b):
    out=defaultdict(Q)
    for x,p in a:
        for y,q in b: out[x+y]+=p*q
    return tuple(sorted(out.items()))

def power(a,n):
    ans=((Q(0),Q(1)),)
    for _ in range(n): ans=convolve(ans,a)
    return ans

def shift(a,d): return tuple((x+d,p) for x,p in a)
def cdf(a,t): return sum((p for x,p in a if x<=t),Q(0))
def pos(x): return max(x,Q(0))
def expectation(a,f): return sum((p*f(x) for x,p in a),Q(0))

# No event indicator differentiation is used anywhere.
def old_h(U0,U1,x):
    D=shift(U1,Q(1))
    return cdf(U0,x)*(sum(p for d,p in D if d>x)-expectation(D,lambda d:pos(d-x)))-expectation(U0,lambda u:u if u<=x else Q(0))

def stoploss_h(U0,U1,x):
    D=shift(U1,Q(1))
    return expectation(U0,lambda u:pos(x-u))-expectation(D,lambda d:pos(x-d))-cdf(D,x)

laws=[
 ('zero',centered(Q(0),Q(0)),centered(Q(0),Q(0)),Q(0),Q(0),Q(0)),
 ('symmetric small',centered(Q(1,10),Q(1,10)),centered(Q(1,10),Q(1,10)),Q(1,10),Q(1,10),Q(1,10)),
 ('right both',centered(Q(3,5),Q(3,100)),centered(Q(4,100),Q(3,5)),Q(3,100),Q(4,100),Q(3,5)),
 ('right U0 only',centered(Q(3,5),Q(3,100)),centered(Q(0),Q(0)),Q(3,100),Q(0),Q(0)),
 ('right U1 only',centered(Q(0),Q(0)),centered(Q(4,100),Q(3,5)),Q(0),Q(4,100),Q(3,5)),
 ('left both',centered(Q(7,10),Q(3,100)),centered(Q(19,500),Q(7,10)),Q(3,100),Q(19,500),Q(7,10)),
 ('zero reserve boundary',centered(Q(1,2),Q(1,4)),centered(Q(1,4),Q(3,4)),Q(1,4),Q(1,4),Q(3,4)),
 ('rare far negative',centered(Q(100),Q(1,1000)),centered(Q(1,1000),Q(1,2)),Q(1,1000),Q(1,1000),Q(1,2)),
]
for name,U0,U1,a0,a1,A1 in laws:
    require(name+' centered',expectation(U0,lambda x:x)==0==expectation(U1,lambda x:x))
    require(name+' support',max(x for x,p in U0)<=a0 and min(x for x,p in U1)>=-a1 and max(x for x,p in U1)<=A1 and a0+a1<1 and A1+a1<=1)
    b=min(1-A1-a1,1-a0-a1)
    for n in [1,2,3,4]:
        # Marginal conditional distributions from separate convolutions.
        T=[shift(convolve(power(U1,j),power(U0,n-j)),Q(j)) for j in range(n+1)]
        lower=n*a0; upper=n*(1-a1)
        thresholds={lower}
        thresholds.update(x for law in T for x,p in law if lower<=x<upper)
        ordered=sorted(thresholds|{upper})
        thresholds.update((x+y)/2 for x,y in zip(ordered,ordered[1:]))
        # Full coupling paths are not reconstructed from those CDFs.
        joint=[]
        for pairseq in product(tuple(product(U0,U1)),repeat=n):
            weight=Q(1); us=[]; vs=[]
            for (u,p0),(v,p1) in pairseq:
                weight*=p0*p1; us.append(u); vs.append(v)
            path=[Q(j)+sum(vs[:j])+sum(us[j:]) for j in range(n+1)]
            require('strict path increments',all(x<y for x,y in zip(path,path[1:])))
            joint.append((path,weight))
        p=Q(2,5) if n%2 else Q(53,100)
        mix=tuple((u,(1-p)*w) for u,w in U0)+tuple((1+u,p*w) for u,w in U1)
        # Direct iid product enumeration, independent of conditional binomial formula.
        actual=defaultdict(Q)
        for seq in product(mix,repeat=n):
            mass=Q(1)
            for _,w in seq: mass*=w
            actual[sum(x for x,_ in seq)]+=mass
        actual=tuple(actual.items())
        pi=[Q(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1)]
        FB=[sum(pi[:k+1]) for k in range(n+1)]
        for t in sorted(thresholds):
            EK=Q(0); ER=Q(0); EW=Q(0); EF=Q(0); Kdist=defaultdict(Q)
            for path,w in joint:
                ks=[j for j in range(n) if path[j]<=t<path[j+1]]
                assert len(ks)==1
                k=ks[0]; Kdist[k]+=w
                EK+=w*k; ER+=w*min(t-path[k],b); EW+=w*(path[k+1]-(k+1)); EF+=w*FB[k]
            g=t-EK
            require('count tails reconstruct K',EK==sum(cdf(T[j],t) for j in range(1,n+1)))
            require('age reserve',g>=ER>=0)
            H=Q(0); Hstop=Q(0); selected_bias=Q(0); localage=Q(0); gi=[]
            for i in range(1,n+1):
                leave=convolve(power(U1,i-1),power(U0,n-i))
                Ri=tuple((t-(i-1)-x,w) for x,w in leave)
                val=expectation(Ri,lambda x:old_h(U0,U1,x))
                val2=expectation(Ri,lambda x:stoploss_h(U0,U1,x))
                require('equivalent local kernels',val==val2)
                require('stop-loss difference',val2==expectation(T[i-1],lambda x:pos(t-x))-expectation(T[i],lambda x:pos(t-x))-cdf(T[i],t))
                H+=val; Hstop+=val2; gi.append(val)
                selected_bias-=expectation(Ri,lambda x:expectation(U0,lambda u:u if u<=x else Q(0)))
                D=shift(U1,Q(1))
                localage+=expectation(Ri,lambda x:sum(w for d,w in D if d>x)*expectation(U0,lambda u:min(x-u,b) if u<=x else Q(0)))
            require('exact crossing identity',H==g==Hstop)
            require('selected-noise correction',EW==selected_bias>=0)
            bias_cases += int(EW>0)
            require('age decomposition',ER==localage)
            require('actual iid mixture CDF',cdf(actual,t)==EF==sum(pi[j]*cdf(T[j],t) for j in range(n+1)))
            # Independent summation-by-parts reconstruction with Jensen defects.
            Lj=[expectation(law,lambda x:pos(t-x)) for law in T]
            Bj=[x-pos(t-j) for j,x in enumerate(Lj)]
            require('Jensen defects nonnegative',all(x>=0 for x in Bj))
            curvature=sum((pi[j+1]-pi[j])*Bj[j] for j in range(1,n))
            loss=sum(pi[i]*gi[i-1] for i in range(1,n+1))
            k=int(t); u=t-k
            require('integer anchor is legal',0<=k<n and 0<=u<1)
            require('weighted loss nonnegative',loss>=0)
            require('weighted crossing identity',cdf(actual,t)-FB[k]==u*pi[k+1]+curvature-loss)
            require('linear stop-loss interpolation',pi[0]+pi[1]*t+sum((pi[j+1]-pi[j])*pos(t-j) for j in range(1,n))==FB[k]+u*pi[k+1])
            curvature_sign_controls += int(cdf(actual,t)-FB[k]!=u*pi[k+1]-curvature-loss)
            # Algebraic count part of Delta, with arbitrary choices of reference k.
            for k in {0,int(t),n}:
                if not 0<=k<=n: continue
                EQ=sum(w*(FB[j]-FB[k]-pi[k]*(j-k)) for j,w in Kdist.items())
                require('exact Delta count identity',cdf(actual,t)-FB[k]==-pi[k]*g+EQ+pi[k]*(t-k))
            cases+=1

# Exact acquired-range inequalities; one common cap dominates left/right.
require('variance square root cap',Q(1,4)+Q(77,125)/42<Q(103,200)**2)
require('threshold displacement cap',Q(46,25)*Q(103,200)<Q(237,250))
require('lower acquisition at n42',(Q(1,4)-Q(9,125))*42>Q(237,250))
require('upper acquisition at n42',(1-Q(9,125)-Q(53,100))*42>Q(237,250))
require('right reserve',min(1-Q(3,5)-Q(9,125),1-Q(9,125))==Q(41,125))
require('left reserve',min(1-Q(7,10)-Q(17,250),1-Q(17,250))==Q(29,125))

# Actual iid counterexample if width premise is omitted.
U0=((Q(0),Q(1)),)
U1=((Q(-1,10),Q(19,21)),(Q(19,20),Q(2,21)))
require('counterexample still centered',expectation(U1,lambda x:x)==0)
t=Q(9,10); n=2
EK=sum(cdf(shift(convolve(power(U1,j),power(U0,n-j)),Q(j)),t) for j in [1,2])
require('width violation exact deficit',EK-t==Q(1,210))
reject('dropping width hypothesis',lambda:must(t-EK>=0))
reject('optional-stopping zero selected-noise claim',lambda:must(bias_cases==0))
# Closed atom versus strict crossing distinction already present for zero noise at t=1.
reject('replace closed lower crossing by strict',lambda:must(sum(int(Q(j)<1<Q(j+1)) for j in range(2))==1))
reject('upper threshold endpoint admitted',lambda:must(sum(int(Q(j)<=2<Q(j+1)) for j in range(2))==1))
uncentered=((Q(-1,10),Q(1)),)
uncentered_EK=sum(cdf(shift(power(uncentered,j),Q(j)),Q(19,20)) for j in [1,2])
require('uncentered actual-law deficit',Q(19,20)-uncentered_EK==Q(-1,20))
reject('centeredness omitted',lambda:must(Q(19,20)-uncentered_EK>=0))
require('nonzero selected bias exercised',bias_cases>0)
reject('reversing curvature difference',lambda:must(curvature_sign_controls==0))

source=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent/'crossing.tex'
EXPECTED_SOURCE_SHA256='0dda285adb9aaa24277fdc1d74843c20bc6100b2a64a0cd5ae34bb696a68a6ec'
assert source.is_file(), 'reviewed source missing'
assert hashlib.sha256(source.read_bytes()).hexdigest()==EXPECTED_SOURCE_SHA256, 'reviewed source pin mismatch'
print(json.dumps({'result':'PASS','scope':'crossing identity/sign/age reserve and exact count algebra; not full Delta comparison','actual_law_threshold_cases':cases,'exact_checks':len(checks),'nonzero_selected_noise_cases':bias_cases,'negative_controls':controls,'constructor_code_imported':False,'reviewed_source_pin_verified':True,'source':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest() if source.exists() else None,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))

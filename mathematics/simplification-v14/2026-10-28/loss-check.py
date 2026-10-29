#!/usr/bin/env python3
"""Exact bounded checks for common-noise sharp closure and phase obstruction.
No constructor or inherited acceptance code is imported.
"""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict
from math import comb, isqrt
from functools import lru_cache
from pathlib import Path
import hashlib,json

checks=[]; rejections=[]
def require(name,x):
    assert x,name
    checks.append(name)
def reject(name,fn):
    try: fn()
    except (AssertionError,ValueError): rejections.append(name);return
    raise AssertionError('negative control accepted: '+name)
def must(x): assert x
def floor(x): return x.numerator//x.denominator
def frac(x): return x-floor(x)
def mean(law,f): return sum((p*f(x) for x,p in law),Q(0))
def centered(a,b):
    if a==b==0:return ((Q(0),Q(1)),)
    return ((-a,b/(a+b)),(b,a/(a+b)))
def conv(a,b):
    d=defaultdict(Q)
    for x,p in a:
        for y,q in b:d[x+y]+=p*q
    return tuple(sorted(d.items()))
def power(law,n):
    d=((Q(0),Q(1)),)
    for _ in range(n):d=conv(d,law)
    return d
def actual_product(law,n):
    d=defaultdict(Q)
    for seq in product(law,repeat=n):
        mass=Q(1)
        for _,p in seq:mass*=p
        d[sum(x for x,_ in seq)]+=mass
    return tuple(sorted(d.items()))

# Rational gates in the analytic proofs.
pi_lower=4*sum((Q((-1)**k,2*k+1) for k in range(64)),Q(0))
require('elementary pi lower',pi_lower>Q(25,8))
require('phi0 ceiling',Q(1,1)/(2*Q(25,8))==Q(2,5)**2)
require('Gaussian third moment ceiling',8/Q(25,8)==Q(8,5)**2)
require('CE lower squared',Q(259,1584)>Q(4,25))
require('variance range',Q(1,5)**2/4==Q(1,100))
require('minimum Bernoulli variance',Q(1,4)*Q(3,4)==Q(3,16))
require('variance ratio',Q(1,100)/Q(3,16)==Q(4,75))
require('moment quadratic remainder',Q(3,8)*Q(5,8)*Q(4,75)==Q(1,80))
require('raw moment gain',Q(3,16)-Q(1,10)-Q(1,80)==Q(3,40))
require('normalization gain squared',Q(75,79)**3>Q(9,10)**2)
require('normalized moment gain',Q(3,40)*Q(9,10)==Q(27,400))
require('smooth error full remainder',Q(2,5)/6*(Q(1,5)+Q(8,5)*Q(1,10))==Q(3,125))
require('strict final gain',Q(2,5)*Q(27,400)-Q(3,125)==Q(3,1000))
require('CF cosine constant',18-Q(2,3)*Q(22,7)**4*Q(9,125)**2>17)
require('CF modulus positivity',34*Q(9,125)**2/4<1)
require('right linear CF bound',Q(2975,7832)>Q(3,8))
require('left linear CF bound',Q(2975,7084)>Q(2,5))
require('acquired threshold variance cap',Q(1,4)+Q(9,25)/42<Q(103,200)**2)
require('acquired threshold displacement',Q(46,25)*Q(103,200)<Q(237,250))
require('acquired lower endpoint',(Q(1,4)-Q(9,125))*42>Q(237,250))
require('acquired upper endpoint',(1-Q(9,125)-Q(53,100))*42>Q(237,250))
# Verify the polynomial-division identity for the pi upper bound.
# x^4(1-x)^4=(1+x^2)*(x^6-4x^5+5x^4-4x^2+4)-4.
poly=[Q(0),Q(0),Q(0),Q(0),Q(1),Q(-4),Q(6),Q(-4),Q(1)]
quot=[Q(4),Q(0),Q(-4),Q(0),Q(5),Q(-4),Q(1)]
out=[Q(0)]*9
for j,c in enumerate(quot):out[j]+=c;out[j+2]+=c
out[0]-=4
require('pi upper polynomial identity',out==poly)
require('pi upper integral constant',sum((c/Q(j+1) for j,c in enumerate(quot)),Q(0))==Q(22,7))

laws=[
 ('zero',((Q(0),Q(1)),)),
 ('symmetric width edge',centered(Q(1,10),Q(1,10))),
 ('skew left',centered(Q(19,100),Q(1,100))),
 ('skew right',centered(Q(1,100),Q(19,100))),
 ('rare remote within width',centered(Q(1,10**6),Q(199999,10**6))),
 ('three-point rare',((Q(-1,10),Q(1,1000)),(Q(0),Q(499,500)),(Q(1,10),Q(1,1000)))),
 ('nearby four-point',tuple((x,Q(1,4)) for x in [Q(-1,10),Q(-99,1000),Q(99,1000),Q(1,10)])),
 ('skew three-point',((Q(-1,10),Q(3,10)),(Q(1,50),Q(1,2)),(Q(1,10),Q(1,5)))),
]
moments=0; product_cases=0; normal_cases=[]
for name,U in laws:
    require(name+' centered actual law',sum(p for x,p in U)==1 and all(p>0 for x,p in U) and mean(U,lambda x:x)==0)
    d=max(x for x,p in U)-min(x for x,p in U)
    s=mean(U,lambda x:x*x); mu3=mean(U,lambda x:x**3); m3=mean(U,lambda x:abs(x)**3)
    require(name+' width and moments',d<=Q(1,5) and s<=d*d/4 and m3<=d*s and abs(mu3)<=d*s)
    for p in [Q(1,4),Q(1,3),Q(1,2),Q(2,3),Q(3,4)]:
        q=1-p;v=p*q;M=v*(1-2*v)
        Y=tuple((x,q*w) for x,w in U)+tuple((1+x,p*w) for x,w in U)
        N=mean(Y,lambda y:abs(y-p)**3)
        require('exact raw cubic '+name+str(p),N==M+6*v*s+(2*p-1)*mu3)
        require('variance and centering '+name+str(p),mean(Y,lambda y:y)==p and mean(Y,lambda y:(y-p)**2)==v+s)
        require('normalized moment gain by positive squaring',N>=0 and M+Q(27,400)*s>0 and N*N*v**3 >= (M+Q(27,400)*s)**2*(v+s)**3)
        moments+=1
        for n in [1,2,4]:
            direct=actual_product(Y,n)
            binom=tuple((Q(k),Q(comb(n,k))*p**k*q**(n-k)) for k in range(n+1))
            conditional=conv(binom,power(U,n))
            require('actual product equals conditional mixture',direct==conditional)
            product_cases+=1
            if name in ['zero','symmetric width edge','skew three-point'] and p in [Q(1,4),Q(1,2),Q(3,4)]:
                normal_cases.append((name,p,n,s,N,direct))

# Outward rational normal-CDF checks, separate from the analytic acceptance.
def rounded(x,up,digits=34):
    den=10**digits; num=(x.numerator*den)//x.denominator
    if up and Q(num,den)<x:num+=1
    return Q(num,den)
def sqrt_interval(x,digits=34):
    assert x>=0
    den=10**digits;k=isqrt(x.numerator*den*den//x.denominator);lo=Q(k,den)
    return (lo,lo if lo*lo==x else Q(k+1,den))
def atan_interval(x,N=60):
    vals=[];s=Q(0)
    for k in range(N+2):
        s+=Q((-1)**k,2*k+1)*x**(2*k+1)
        if k>=N:vals.append(s)
    return min(vals),max(vals)
a,b=atan_interval(Q(1,5));c,e=atan_interval(Q(1,239))
pil=rounded(16*a-4*e,False);piu=rounded(16*b-4*c,True)
require('outward pi agrees elementary bounds',Q(25,8)<pil<piu<Q(22,7))
root2pi_l=sqrt_interval(2*pil)[0];root2pi_u=sqrt_interval(2*piu)[1]
ce_l=(3+sqrt_interval(Q(10))[0])/(6*root2pi_u)
ce_u=(3+sqrt_interval(Q(10))[1])/(6*root2pi_l)
@lru_cache(None)
def phi_point(x):
    if x<0:
        lo,hi=phi_point(-x);return 1-hi,1-lo
    if not x:return Q(1,2),Q(1,2)
    N=80
    assert x*x/2<N
    term=x;s=Q(0);vals=[]
    for k in range(N+2):
        if k:term*=-x*x*Q(2*k-1,2*k*(2*k+1))
        s+=term
        if k>=N:vals.append(s)
    ilo,ihi=min(vals),max(vals);assert ilo>=0
    return Q(1,2)+ilo/root2pi_u,Q(1,2)+ihi/root2pi_l
cdf_events=0
for name,p,n,s,N,law in normal_cases:
    v=p*(1-p);rootv_l,rootv_u=sqrt_interval(v);rootsig_l,rootsig_u=sqrt_interval(v+s)
    rho_l=N/((v+s)*rootsig_u)
    gain_u=Q(3,1000)*s/(v*rootv_l)
    target_l=ce_l*rho_l-gain_u
    rootn_l,rootn_u=sqrt_interval(Q(n))
    scale_l,scale_u=sqrt_interval(n*(v+s))
    for t in {law[0][0],law[len(law)//2][0],law[-1][0]}:
        r=t-n*p
        xl,xu=(r/scale_u,r/scale_l) if r>=0 else (r/scale_l,r/scale_u)
        Flo=phi_point(xl)[0];Fhi=phi_point(xu)[1]
        for closed in [False,True]:
            F=sum(w for y,w in law if y<t or (closed and y==t))
            err_u=max(abs(F-Flo),abs(F-Fhi))
            require('outward actual-law sharp bound',rootn_u*err_u<target_l)
            cdf_events+=1

# Exact common-noise crossing probes, including moderate noise and collisions.
phase_cases=[]
for n,a,p in [(42,Q(1,100),Q(1,2)),(160,Q(1,40),Q(7,20)),(512,Q(1,40),Q(1,2))]:
    W=tuple((a*(2*m-n),Q(comb(n,m),2**n)) for m in range(n+1))
    lam=n*a*a
    for u in [Q(0),Q(1,4),Q(1,2),Q(3,4)]:
        t=n*p+u
        require('common-noise raw phase integer anchor',(n*p).denominator==1)
        require('common-noise actual strip',2*a<=Q(17,250) and a<=Q(3,5) and n*a<=t<n*(1-a))
        require('common-noise raw H restriction',u*u < Q(46,25)**2*(p*(1-p)+a*a))
        g=mean(W,lambda w:frac(t-w))
        tail_mean=sum(sum(prob for w,prob in W if j+w<=t) for j in range(1,n+1))
        require('common-noise exact crossing identity',g==t-tail_mean)
        require('quantitative CF bound on actual law',g>=Q(119,44)*lam/(1+17*lam))
        if u>=Q(1,2):require('symmetric excess is nonpositive',g<=u)
        phase_cases.append({'n':n,'amplitude':str(a),'p':str(p),'phase':str(u),'lambda':str(lam),'gain':str(g),'excess':str(g-u)})
        if n==42 and u==Q(3,4):negative_excess=g-u
        if n==42 and u==Q(1,2):zero_excess=g-u
        if n in [160,512] and u==Q(3,4):require('moderate excess strictly negative',g<u)
require('tiny-noise exact excess formula',negative_excess==-Q(sum(comb(42,m) for m in range(9)),2**42))
require('positive-noise zero excess',zero_excess==0)

# Meaningful failures of proposed extensions, not counterexamples to BE.
reject('positive excess over noiseless phase',lambda:must(negative_excess>0))
reject('strict excess at every positive noise',lambda:must(zero_excess>0))
# Dependent copies with common noise ±1/42: W=±1, so g(21)=0.
dependent_g=Q(21)-(Q(20)+Q(22))/2
reject('drop iid-noise independence',lambda:must(dependent_g>=Q(3,8)*Q(1,42)))
# Outside the p-range the moment-payment lemma can fail.
p=Q(1,10);v=p*(1-p);s=Q(1,10000);M=v*(1-2*v);N=M+6*v*s
require('outside-p actual moment decreases',N*N*v**3 < M*M*(v+s)**3)
reject('drop p-range from moment increase',lambda:must(N*N*v**3 >= (M+Q(27,400)*s)**2*(v+s)**3))
# Outside the support width, crossing zero invalidates the cubic expansion.
p=Q(1,4);v=p*(1-p);U=centered(Q(3,10),Q(3,10));s=mean(U,lambda x:x*x)
Y=tuple((u,(1-p)*w) for u,w in U)+tuple((1+u,p*w) for u,w in U)
reject('ignore sign preservation in cubic expansion',lambda:must(mean(Y,lambda y:abs(y-p)**3)==v*(1-2*v)+6*v*s))
# Unequal conditional laws cannot be pooled and made independent of B.
p=Q(2,5);U0=centered(Q(1,10),Q(1,100));U1=((Q(0),Q(1)),)
actual_zero=(1-p)*sum(w for u,w in U0 if u<=0)
pooled_zero=(1-p)*((1-p)*sum(w for u,w in U0 if u<=0)+p)
reject('pool unequal noise laws as independent',lambda:must(actual_zero==pooled_zero))

here=Path(__file__).resolve().parent
print(json.dumps({'result':'PASS','scope':'sharp BE common-independent-noise closure, supplemental unweighted bound and phase counterexamples','rational_checks':len(checks),'actual_moment_cases':moments,'actual_product_cases':product_cases,'outward_CDF_events':cdf_events,'negative_controls':rejections,'phase_cases':phase_cases,'source_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in [here/'loss-closure.tex',here/'loss-common.tex',Path(__file__).resolve()]}},indent=2))

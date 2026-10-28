#!/usr/bin/env python3
"""Exact scalar gates and actual finite conditional convolutions; no grids."""
from fractions import Fraction as F
from math import comb, factorial
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import hashlib, json, sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions required')

checks=[]; negative=[]; cases=[]
def check(name, value):
    assert value, name
    checks.append(name)
def reject(name, value):
    assert not value, "failed negative control: "+name
    negative.append(name)

pi_hi=F(22,7); L=F(9,25)
check('pi upper square below ten',pi_hi*pi_hi<10)
check('pi upper below ten-thirds',pi_hi<F(10,3))
check('bump upper-end minorant',F(2,5)*pi_hi*pi_hi*F(9,125)<F(41,84))
check('left bump also permitted',F(2,5)*pi_hi*pi_hi*F(17,250)<F(29,96))
check('cosine first interval',2*F(51,40)**2>3)
check('cosine last positive sine',F(17,20)-F(44,2625)>0)
check('cosine last interval',2*(F(17,20)-F(44,2625))**2>3*F(84,125)**2)
check('raw threshold envelope',F(46,25)**2*(F(1,4)+L/42)<F(47,50)**2)
check('lower variance U0 coefficient',F(97,50)/F(47,100)<5)
check('lower variance U1 coefficient',F(97,50)/F(2,5)<5)
check('upper variance U0 coefficient',F(47,50)/F(47,100)<3)
check('upper variance U1 coefficient',F(47,50)/F(2,5)<3)
check('five counts lower edge',42*F(2,5)-F(97,50)-1>1)
check('five counts upper edge',42*F(47,100)>F(47,50)+3)
table={125:F(1,250),150:F(1,20),200:F(1,8),250:F(1,6),
       300:F(19,100),400:F(9,40),500:F(6,25)}
coefficients={}
for N,target in table.items():
    a=1-F(5,N); b=1+F(3,N); x=3*a*L
    P=sum(x**j/F(factorial(j)) for j in range(7))
    c=F(2,5)*((1-1/P)/(2*L)-(L*b+3*b*b*L)/16-10*pi_hi*pi_hi/N)
    check('positive exponential denominator',P>1)
    check('complete rational coefficient at '+str(N),c>target)
    coefficients[N]={'lower':str(c),'target':str(target),'margin':str(c-target)}

# A law is a tuple of (position, mass). Every product uses one actual marginal.
zero=((F(0),F(1)),)
def centered_two(lo,hi):
    assert lo<0<hi
    return ((lo,hi/(hi-lo)),(hi,-lo/(hi-lo)))
def moment(law,r):return sum(prob*x**r for x,prob in law)
@lru_cache(None)
def power(law,m):
    if m==0:return ((F(0),F(1)),)
    if len(law)==1:return ((law[0][0]*m,F(1)),)
    (x,p),(y,q)=law
    return tuple((m*x+j*(y-x),F(comb(m,j))*p**(m-j)*q**j) for j in range(m+1))
@lru_cache(None)
def conditional(law0,law1,m0,m1):
    if law0==law1:return power(law0,m0+m1)
    if law0==zero:return power(law1,m1)
    if law1==zero:return power(law0,m0)
    out=defaultdict(F)
    for x,p in power(law0,m0):
        for y,q in power(law1,m1):out[x+y]+=p*q
    return tuple(sorted(out.items()))
def stop_and_cdf(law,x):
    return (sum(p*max(F(0),x-y) for y,p in law),
            sum(p for y,p in law if y<=x))
def kernel(x,law0,law1):
    return (sum(p*max(F(0),x-y) for y,p in law0)
            -sum(p*max(F(0),x-1-y) for y,p in law1)
            -sum(p for y,p in law1 if 1+y<=x))
def run_law(name,n,p,law0,law1):
    q=1-p;v=p*q;s0=moment(law0,2);s1=moment(law1,2)
    lam=n*(q*s0+p*s1)
    a0=max(x for x,_ in law0);a1=-min(x for x,_ in law1)
    check('actual conditional mean zero',moment(law0,1)==moment(law1,1)==0)
    check('actual strip',min(x for x,_ in law0)>=-F(3,5) and max(x for x,_ in law1)<=F(3,5) and a0+a1<=F(9,125))
    check('actual noise range',0<=lam<=L)
    # Four raw shifts plus an actual own-count collision when it lies in range.
    ts=[n*p+x for x in [F(-9,10),F(0),F(1,2),F(9,10)]]
    kc=int(n*p); own=conditional(law0,law1,n-kc,kc)
    near=min(own,key=lambda z:abs(z[0]))[0]
    collision=kc+near
    if abs(collision-n*p)<F(47,50):ts.append(collision)
    for t in dict.fromkeys(ts):
        k=t.numerator//t.denominator
        stop={};cdf={}
        for j in range(k-2,k+4):
            stop[j],cdf[j]=stop_and_cdf(conditional(law0,law1,n-j,j),t-j)
        gs=[stop[i-1]-stop[i]-cdf[i] for i in range(k-1,k+4)]
        check('actual five local losses nonnegative',all(g>=0 for g in gs))
        selected=sum(gs)
        valid=[N for N in table if N<=n]
        if valid:check('actual five-count table bound',selected>=table[max(valid)]*lam)
        tau=(n-k-1)*s0+k*s1
        check('actual frozen variance transport',(1-F(5,n))*lam<=tau<=(1+F(3,n))*lam)
        if n==42:
            # Independently evaluate the local kernel, not just stop-loss differences.
            for i,g in zip(range(k-1,k+4),gs):
                omitted=conditional(law0,law1,n-i,i-1)
                direct=sum(prob*kernel(t-i+1-x,law0,law1) for x,prob in omitted)
                check('actual kernel equals local telescoping',direct==g)
        cases.append({'name':name,'n':n,'p':str(p),'lambda':str(lam),'t':str(t),
                      'five_loss':str(selected),'collision':t==collision})

for n,p in [(42,F(2,5)),(125,F(2,5)),(200,F(53,100))]:
    run_law('zero',n,p,zero,zero)
    eps=F(1,10000) if n==125 else F(1,100)
    symmetric=centered_two(-eps,eps)
    run_law('common symmetric tiny' if n==125 else 'common symmetric',n,p,symmetric,symmetric)
    for lam in [F(3,40),F(9,25)]:
        e0=lam/(n*(1-p)*F(3,5)); e1=lam/(n*p*F(3,5))
        run_law('rare negative endpoint',n,p,centered_two(-F(3,5),e0),zero)
        run_law('rare positive endpoint',n,p,zero,centered_two(-e1,F(3,5)))
    if n<=125:
        eps=F(9,25)/(n*F(3,5))
        run_law('unequal four-atom allocation',n,p,
                centered_two(-F(3,5),eps),centered_two(-eps,F(3,5)))

# Negative controls target real hypotheses, not the main conjecture.
reject('remove centering in smooth replacement: F(x)=x',F(1,10)<=0)
reject('allow overlapping translates to retain multiplicity one',2<=1)
# Z=+-1/2 has characteristic modulus one at2pi and variance1/4.
reject('drop conditional-diameter premise in CF contraction',F(0)>=6*F(1,4))
# At u=1/4,V=5/2 the omitted j=-3 bump is sin²(3pi/4)=1/2.
reject('delete the omitted-translate tail',F(0)>=F(1,2))
reject('extend the table to N42 by the same bound',
       (1-F(5,42))>0 and F(2,5)*(F(3,2)-10*pi_hi*pi_hi/42)>0)

here=Path(__file__).resolve().parent
source=here/'loss-direct.tex'
print(json.dumps({'result':'PASS','exact_checks':len(checks),
 'actual_cases':len(cases),'negative_controls':negative,
 'rational_coefficients':coefficients,'actual_laws':cases,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))

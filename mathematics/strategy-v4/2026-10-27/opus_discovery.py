"""Small deterministic diagnostic; no imported attachment, no search optimizer."""
from fractions import Fraction as F
from math import sqrt, erf, comb
import json

def convolve_integer(vals, weights, n):
    law={0:1}
    for _ in range(n):
        nxt={}
        for a,wa in law.items():
            for b,wb in zip(vals,weights):
                nxt[a+b]=nxt.get(a+b,0)+wa*wb
        law=nxt
    return law

def score(vals,weights,n):
    den=sum(weights)
    mu=sum(F(v*w,den) for v,w in zip(vals,weights))
    var=sum(F(w,den)*(v-mu)**2 for v,w in zip(vals,weights))
    third=sum(F(w,den)*abs(v-mu)**3 for v,w in zip(vals,weights))
    scale=sqrt(n)*float(var)**1.5/float(third)
    cumulative=0; best=(-1,None,None)
    for s,w in sorted(convolve_integer(vals,weights,n).items()):
        z=float(s-n*mu)/sqrt(n*float(var))
        g=(1+erf(z/sqrt(2)))/2
        left=cumulative/den**n
        cumulative+=w
        right=cumulative/den**n
        for sign,d in [('closed',right-g),('reflected',g-left)]:
            if scale*d>best[0]: best=(scale*d,s,sign)
    p=sum(F(w,den) for v,w in zip(vals,weights) if v>mu)
    return best,p

rows=[]
for n in [1,2,3,4,5,10,20,42]:
    best=None; count=0
    for i in range(1,20):
      for j in range(1,20-i):
        weights=[i,j,20-i-j]
        actual,p=score([-1,0,1],weights,n)
        sk,_=score([0,1],[p.denominator-p.numerator,p.numerator],n)
        excess=actual[0]-sk[0]
        count+=1
        if best is None or excess>best['excess']:
            best={'n':n,'values':[-1,0,1],'weights':weights,'denominator':20,'p':str(p),'actual':actual,'skeleton':sk,'excess':excess,'status':'floating normal, exact integer convolution'}
    best['tested_laws']=count
    rows.append(best)
print(json.dumps(rows,indent=2))

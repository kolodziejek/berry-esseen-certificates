"""Independent direct-product controls for the coordinator's crossing theorem."""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import itertools,hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
source=Path(sys.argv[1])/'mathematics/simplification-v13/2026-10-28/crossing.tex'
pin='0dda285adb9aaa24277fdc1d74843c20bc6100b2a64a0cd5ae34bb696a68a6ec'
assert hashlib.sha256(source.read_bytes()).hexdigest()==pin
laws=[({F(-1,50):F(1,2),F(1,50):F(1,2)},{F(0):F(1)}),
({F(-3,5):F(1,31),F(1,50):F(30,31)},{F(-1,50):F(30,31),F(3,5):F(1,31)}),
({F(0):F(1)},{F(-1,50):F(30,31),F(3,5):F(1,31)}),
({F(0):F(1)},{F(0):F(1)})]
controls=0;biased=0
for U0,U1 in laws:
 assert sum(x*w for x,w in U0.items())==sum(x*w for x,w in U1.items())==0
 a0=max(U0);a1=-min(U1);A1=max(U1);b=min(1-A1-a1,1-a0-a1)
 def h(x):return sum(max(x-z,0)*w for z,w in U0.items())-sum(max(x-1-z,0)*w for z,w in U1.items())-sum(w for z,w in U1.items() if 1+z<=x)
 pairs=[(x,y,px*py) for x,px in U0.items() for y,py in U1.items()]
 for n in [3,4]:
  p=F(2,5);pi=[F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(n+1)]
  FB=[sum(pi[:j+1]) for j in range(n+1)]
  for t in [F(n,2)-F(1,100),F(n,2),F(n,2)+F(1,100)]:
   assert n*a0<=t<n*(1-a1)
   EK=age=local=actual=bias=F(0);L=[F(0)]*(n+1);G=[F(0)]*(n+1)
   for sample in itertools.product(pairs,repeat=n):
    weight=F(1)
    for x,y,w in sample:weight*=w
    T=[j+sum(y for x,y,w in sample[:j])+sum(x for x,y,w in sample[j:]) for j in range(n+1)]
    assert all(T[j]<T[j+1] for j in range(n))
    K=max(j for j in range(n+1) if T[j]<=t)
    EK+=weight*K;age+=weight*min(t-T[K],b);actual+=weight*FB[K];bias+=weight*(T[K+1]-K-1)
    for j in range(n+1):L[j]+=weight*max(t-T[j],0)
    for i in range(1,n+1):
     r=t-i+1-sum(y for x,y,w in sample[:i-1])-sum(x for x,y,w in sample[i:])
     assert h(r)>=0;G[i]+=weight*h(r)
   assert t-EK==sum(G) and t-EK>=age>=0 and bias>=0
   k=t.__floor__();u=t-k
   weighted=FB[k]+u*pi[k+1]+sum((pi[j+1]-pi[j])*(L[j]-max(t-j,0)) for j in range(1,n))-sum(pi[i]*G[i] for i in range(1,n+1))
   assert weighted==actual
   controls+=1;biased+=bias>0
assert biased>0
print(json.dumps({'status':'PASS_INDEPENDENT_DIRECT_PRODUCT_CROSSING_CONTROLS','source_sha256':pin,'controls':controls,'nonzero_selected_bias_cases':biased,'method':'Full product-space enumeration of independent conditional pairs; no constructor import or conditional-sum recurrence.','scope':'Finite controls plus independent analytic review; no weighted-noise closure claimed.','python':sys.version},indent=2))

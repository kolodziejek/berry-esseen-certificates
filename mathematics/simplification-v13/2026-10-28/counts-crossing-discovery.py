"""Bounded discovery for the unweighted random crossing; never acceptance.

Actual centered conditional two-point laws; atom locations are exact integers
in units1/1000. Probabilities and the reported margins are floating diagnostics.
"""
from math import comb
from fractions import Fraction as F
from collections import defaultdict
import json,time,sys
n=42;p=F(1,2);scale=1000
small=[0,2,6,12,24,36,48,68];large=[200,600]
laws=set()
for a0 in small:
 for a1 in small:
  if a0+a1>68:continue
  for b0 in large:
   for b1 in large:
    b0=0 if a0==0 else b0;b1=0 if a1==0 else b1
    lam=F(n,2)*F(a0*b0+a1*b1,scale**2)
    if F(3,40)<lam<=F(77,125):laws.add((a0,b0,a1,b1))
assert len(laws)<=200
start=time.monotonic();rows=[];atoms_checked=0
for a0,b0,a1,b1 in sorted(laws):
 probs0=[[comb(j,h)*(a0/(a0+b0))**h*(b0/(a0+b0))**(j-h) for h in range(j+1)] if a0 else [1.] for j in range(n+1)]
 probs1=[[comb(j,h)*(a1/(a1+b1))**h*(b1/(a1+b1))**(j-h) for h in range(j+1)] if a1 else [1.] for j in range(n+1)]
 jumps=defaultdict(float)
 for j in range(1,n):
  for h0,w0 in enumerate(probs0[n-j]):
   for h1,w1 in enumerate(probs1[j]):
    loc=(n-j)*a0+j*(scale-a1)-h0*(a0+b0)+h1*(a1+b1)
    jumps[loc]+=w0*w1
 EK=0.;best=(-1e9,None,None)
 for loc,mass in sorted(jumps.items()):
  EK+=mass
  if abs(loc-n*scale//2)<=900:
   margin=EK-loc/scale;atoms_checked+=1
   if margin>best[0]:best=(margin,loc,EK)
 if best[1] is not None:
  rows.append({'law':[a0,b0,a1,b1],'lambda':str(F(n,2)*F(a0*b0+a1*b1,scale**2)),'max_EK_minus_t':best[0],'threshold':str(F(best[1],scale)),'EK':best[2]})
print(json.dumps({'status':'DISCOVERY_ONLY','law_count':len(laws),'atom_thresholds_tested':atoms_checked,'worst':max(rows,key=lambda r:r['max_EK_minus_t']),'positive_count':sum(r['max_EK_minus_t']>1e-9 for r in rows),'rows':rows,'elapsed_seconds':time.monotonic()-start,'python':sys.version},indent=2))

#!/usr/bin/env python3
"""Bounded diagnostic only: at most 14*6*7*32 small polynomial cells."""
from fractions import Fraction as F
from math import comb
from collections import defaultdict
from zipfile import ZipFile
import json
import check_support_lift as m

def bern(p,a,b):
 d=len(p)-1
 t=[sum(p[j]*comb(j,k)*a**(j-k)*(b-a)**k for j in range(k,d+1)) for k in range(d+1)]
 return [sum(t[j]*F(comb(k,j),comb(d,j)) for j in range(k+1)) for k in range(d+1)]
with ZipFile(m.ARCHIVE) as z:
 proof=json.loads(m.read_member(z,m.LEFT_SHA),object_pairs_hook=m.unique)
groups=defaultdict(list)
for row in m.bind_left_rows(proof):groups[F(row['radius'])].append((F(row['rho_upper']),F(row['beta_absolute_upper'])))
r=min(F(3031,10000)*F(646,1000)/(m.C-F(3031,10000)),F(3322,10000)*F(429,1000)/(m.C-F(3322,10000)))
_,disc=m.roots((2+r*r)**2-4*(1-r*r));_,b=m.roots((disc-2-r*r)/2)
groups[F(96,25)]=[(r,b)]
for R,rs in sorted(groups.items()):
 r=max(x[0] for x in rs);b=max(x[1] for x in rs);U=F(21,5) if R>3.5 else F(39,10)
 q=[r*m.EC/42,3*b,F(3,2)*r,-1]
 ps=[m.A,m.H4,m.J,m.W,m.domination_polynomial([F(0)]),m.scale(q,-1),m.scale(m.contact_polynomial(r,b,[F(0)],F(0)),-1)]
 for size in [1,2,4,8,16,32]:
  gates=[min(bern(p,R+(U-R)*i/size,R+(U-R)*(i+1)/size)) for i in range(size) for p in ps]
  if min(gates)>0:break
 print(json.dumps(dict(R=str(R),r=str(r),b=str(b),U=str(U),count=len(rs),subdivisions=size,minimum=str(min(gates)),passed=min(gates)>0)),flush=True)

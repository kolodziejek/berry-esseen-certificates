#!/usr/bin/env python3
"""Three-case zero-loss support proof; exact endpoint arithmetic, no mesh.

Fresh verification of the NEW fourth-order Gaussian support arithmetic only.
Actual-law resource acquisition and analytic contact remain separate premises.
No archived code is imported or executed. No target overrides are accepted.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile
from math import comb
from copy import deepcopy
import json,sys

ROOT=Path(__file__).resolve().parents[3]
ARCHIVE=ROOT/'verification/finite-tail/sources/backend.zip'
ARCHIVE_SHA='43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52'
PROOF_SHA='419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393'
C=F(819,2000);S=F(81,80);ELL=F(6);N=42
RMIN=F(5,2);RMAX=F(111,40)

class Rejected(ValueError):pass
def need(ok,message):
 if not ok:raise Rejected(message)
def unique(pairs):
 d={}
 for k,v in pairs:
  need(k not in d,'duplicate JSON key');d[k]=v
 return d

def add(*ps):
 q=[F(0)]*max(map(len,ps))
 for p in ps:
  for i,a in enumerate(p):q[i]+=a
 while len(q)>1 and not q[-1]:q.pop()
 return q

def scale(p,a):return [F(x)*a for x in p]
def mul(p,q):
 out=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):out[i+j]+=a*b
 return out

def val(p,x):return sum(a*x**i for i,a in enumerate(p))
def shifted(p,x):return [sum(p[i]*comb(i,j)*x**(i-j) for i in range(j,len(p))) for j in range(len(p))]

A=[F(0),F(-1,2),F(0),F(1,6)]
H4=list(map(F,[3,0,-6,0,1]))
E=add([0,F(3,820),0,0,0,F(1,4100)],scale([-2,0,3],F(17,78720)))
B2=scale(mul(H4,H4),F(1,256*41))

def contact(r,b,sharp=False):
 # r,b are polynomials in the boundary radius. Fixed tuples use constants.
 Q=add([0,0,0,-1],scale(mul(r,[0,0,1]),F(3,2)),scale(mul(b,[0,1]),3),scale(r,F(8,875)))
 if sharp:
  P=add(scale(add(mul(A,A),B2),F(2,5)*S**3),scale(mul(E,A),S**3),scale(mul(Q,A),C))
 else:
  P=add(scale(add(A,scale(H4,F(1,72))),F(2,5)*S**3),scale(E,S**3),scale(Q,C))
 return P

def rays(u,r,b):
 q=-u**3+F(3,2)*r*u*u+3*b*u+F(8,875)*r
 qp=-3*u*u+3*r*u+3*b;qpp=-6*u+3*r
 l=F(2,5)*(u*u/2+F(1,2)+F(8,875))+C*qp
 lp=F(2,5)*u+C*qpp;lpp=F(2,5)-6*C
 values=[q,qp,qpp,l,lp,lpp]
 need(all(x<0 for x in values),'strict whole-ray gates')
 return values

TAYLOR=list(map(F,[
 '123579925563/1343488000000',
 '-467155860219/1679360000000',
 '705959271/13434880000',
 '8703567/167936000',
 '-7499223/839680000',
 '-531441/2099200000']))

def family_gate(lo=RMIN,hi=RMAX):
 need(lo==RMIN and hi==RMAX,'fixed complete radius domain')
 p=scale(contact([F(1,3),F(7,20)],[F(-3,5),F(3,8)]),-1)
 a=shifted(p,lo)
 need(a==TAYLOR,'explicit radius-polynomial identity')
 need(a[1]<0<a[2] and a[3]>0>a[4] and a[5]<0,'derivative coefficient signs')
 h=hi-lo;upper=a[1]+2*a[2]*h+3*a[3]*h*h
 need(upper<0,'uniform decreasing radius polynomial')
 endpoint=val(p,hi)
 need(endpoint>F(1,50),'strict family margin')
 need(F(7,20)*hi+F(1,3)<F(131,100) and F(3,8)*hi-F(3,5)<F(441,1000),'common ray ceilings')
 return {'negative_contact_at_max_radius':str(endpoint),'margin_above_1_50':str(endpoint-F(1,50)),
         'derivative_upper':str(upper),'taylor_coefficients':list(map(str,a)),
         'rays_at_5_2':list(map(str,rays(lo,F(131,100),F(441,1000))))}

def bind(proof):
 need(proof['N']==42 and proof['L']==48 and F(proof['cap'])==F(2113,5000),'original finite source scope')
 need(len(proof['coarse'])==15 and len(proof['fine'])==55,'complete row counts')
 first=proof['first_bridge'];active=[r for r in proof['coarse'] if not r.get('excluded')]
 need(F(first['radius'])==F(121,40),'common bridge radius')
 need(F(first['rho_upper'])==max(F(r['rho']) for r in active),'common preceding rho')
 need(F(first['beta_absolute_upper'])==max(F(r['beta']) for r in active),'common preceding beta')
 need(F(first['rho_upper'])<F(143,100) and F(first['beta_absolute_upper'])<F(93,200),'common simple ceilings')
 rows=[]
 for i,cell in enumerate(proof['fine']):
  need(list(map(F,cell['p']))==[F(135+i,500),F(136+i,500)],'ordered complete probability cover')
  trace=cell['trace'];need(trace and trace[0]['contraction'] is None,'initial common bridge')
  need(F(trace[0]['radius'])==F(121,40),'same common starting radius')
  for prev,step in zip(trace,trace[1:]):
   q=step['contraction'];need(q is not None,'support edge present')
   R=F(q['radius']);r=F(q['rho_upper']);b=F(q['beta_absolute_upper'])
   need(R==F(step['radius'])<F(prev['radius']),'ordered contraction radius')
   need(r==F(prev['resource']['rho']) and b==F(prev['resource']['beta']),'same preceding resource')
   need(RMIN<=R<=RMAX,'covered later radius')
   need(r<=F(7,20)*R+F(1,3) and b<=F(3,8)*R-F(3,5),'affine moment ceilings')
   rows.append(q)
 need(len(rows)==63,'all 63 later contractions')
 for q in [first]+rows:
  need(q['n_band']==[42,48] and F(q['barrier'])==0 and F(q['slow'])==F(19,100) and F(q['current_score_lower'])==C,'historical tuple identity')
 return rows

def main():
 need(not sys.flags.optimize and len(sys.argv)==1,'unoptimized fixed acceptance')
 need(sha256(ARCHIVE.read_bytes()).hexdigest()==ARCHIVE_SHA,'unchanged source archive')
 with ZipFile(ARCHIVE) as z:
  raw=z.read('finite61/blobs/'+PROOF_SHA);need(sha256(raw).hexdigest()==PROOF_SHA,'exact source proof')
  proof=json.loads(raw,object_pairs_hook=unique)
 rows=bind(proof)
 need(S*S>F(42,41) and ELL*ELL<41,'outward elementary constants')
 need(F(281476,89625)>F(160,51)>F(25,8),'Gaussian derivative constants via known Machin lower bound')
 x=F(1,42);a=F(48,125)
 scale_margin=2*a-F(3,4)-(a+F(1,4))*x+(a*a-a)*x*x-a*a*x*x*x
 need(scale_margin>0,'all-index scale correction')
 family=family_gate()
 initial_r=min(F(3031,10000)*F(646,1000)/(C-F(3031,10000)),F(3322,10000)*F(429,1000)/(C-F(3322,10000)))
 r0=F(1841,1000);b0=F(321,500);R0=F(96,25)
 need(initial_r<r0 and 0<b0<1 and (1+b0*b0)**2>r0*r0*(1-b0*b0),'initial moment ceilings')
 need(RMIN<=R0<ELL and val(A,R0)>0 and val(H4,R0)>0,'initial coupling domain')
 need(val(H4,R0)<6*R0*val(A,R0)<6*ELL*val(A,R0),'initial B <= A/4')
 p0=-val(contact([r0],[b0],sharp=True),R0);need(p0>F(1,5),'initial strict contact')
 R1=F(121,40);r1=F(143,100);b1=F(93,200)
 p1=-val(contact([r1],[b1]),R1);need(p1>F(1,100),'common strict contact')
 results={'family':family,'initial':{'radius':str(R0),'negative_contact_times_A':str(p0),'ray_gates':list(map(str,rays(R0,r0,b0)))},
          'common_bridge':{'radius':str(R1),'negative_contact':str(p1),'ray_gates':list(map(str,rays(R1,r1,b1)))}}
 rejected=[]
 def reject(label,fn):
  try:fn()
  except (Rejected,KeyError,TypeError,IndexError):rejected.append(label)
  else:raise Rejected('negative control accepted: '+label)
 reject('expanded_radius_domain',lambda:family_gate(RMIN,F(39,10)))
 reject('omitted_radius_prefix',lambda:family_gate(F(251,100),RMAX))
 reject('false_common_ray_cap',lambda:rays(RMIN,F(3,2),F(1,2)))
 p=deepcopy(proof);p['fine'].pop();reject('missing_probability_cell',lambda:bind(p))
 p=deepcopy(proof);p['fine'].reverse();reject('reordered_probability_cells',lambda:bind(p))
 p=deepcopy(proof);p['fine'][10]['trace'][1]['contraction']['rho_upper']='1';reject('changed_preceding_moment',lambda:bind(p))
 p=deepcopy(proof);p['fine'][10]['trace'][1]['contraction']=None;reject('missing_support_edge',lambda:bind(p))
 reject('duplicate_json_key',lambda:json.loads('{"N":42,"N":43}',object_pairs_hook=unique))
 # Diagnostic failures: these are exact negative controls to overly coarse
 # inequalities, not counterexamples to a probability theorem.
 coarse_initial=-val(contact([r0],[b0]),R0)
 affine_continuation=-val(contact([F(1,3),F(7,20)],[F(-3,5),F(3,8)]),F(39,10))
 need(coarse_initial<0 and affine_continuation<0,'documented coarse-bound obstructions')
 print(json.dumps({'status':'PASS_ELEMENTARY_ZERO_LOSS_SUPPORT_ARITHMETIC',
  'scope':'New all-n>=42 zero-loss support arithmetic for65 bound calls; contact, moment and same-law resource premises remain. No full LOCAL42/base/global acceptance.',
  'native_programs_executed':0,'bernstein_transform_used':False,'mesh_or_search_used':False,
  'support_cases':3,'later_contractions':len(rows),'source_archive_sha256':ARCHIVE_SHA,
  'source_proof_sha256':PROOF_SHA,'scale_margin':str(scale_margin),'results':results,
  'negative_controls':rejected,'coarse_initial_negative_reserve':str(coarse_initial),
  'invalid_affine_continuation_negative_reserve':str(affine_continuation)},indent=2,sort_keys=True))

if __name__=='__main__':main()

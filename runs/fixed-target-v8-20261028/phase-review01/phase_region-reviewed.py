#!/usr/bin/env python3
"""Exact closed-region evaluation of saved same-cell phase envelopes.

This is a resource-interface calculation, not a full confinement acceptor.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
from hashlib import sha256
import json,sys
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def need(x,s):
 if not x:raise ValueError(s)
def root(x):
 need(x>=0,'root domain');scale=10**12;k=isqrt(x.numerator*scale*scale//x.denominator);a,b=F(k,scale),F(k+1,scale)
 need(a*a<=x<=b*b,'root enclosure');return a,b
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 if isinstance(x,list):return [encode(v) for v in x]
 return x
def dec(x):
 if isinstance(x,str):
  try:return F(x)
  except ValueError:return x
 if isinstance(x,dict):return {k:dec(v) for k,v in x.items()}
 if isinstance(x,list):return [dec(v) for v in x]
 return x
def evaluate(cells,pl,pu,hl,hu,lambda_upper=None):
 need(0<pl<=pu<1 and 0<=hl<=hu,'closed region')
 plow=min(pl*(1-pl),pu*(1-pu));phigh=max(pl*(1-pl),pu*(1-pu),F(1,4) if pl<=F(1,2)<=pu else F(0))
 filtered=0;values={s:[] for s in ['plus','minus','absolute']}
 if lambda_upper is not None:
  need(lambda_upper>=0,'nonnegative noise ceiling');theta=lambda_upper/(42*plow+lambda_upper)
  ml=root(plow*plow/(plow+lambda_upper/42))[0];mu=root(phigh)[1]
  bl=1-2*pu-2*(1-pl)*theta;bu=1-2*pl+2*pu*theta
 for cell in cells:
  if cell['pl']>pu or cell['pu']<pl or cell['H']<hl:continue
  if lambda_upper is not None and (cell['m'][1]<ml or cell['m'][0]>mu or cell['beta'][1]<bl or cell['beta'][0]>bu):continue
  filtered+=1;upper=min(hu,cell['H'])
  for sign in values:
   bounds=[]
   for q in cell['quadratics']:
    B,f,Q=q['B'],q[sign],q['Q'];need(Q>0,'positive phase curvature')
    h=max(hl,min(upper,f/(2*Q)));bounds.append(B+f*h-Q*h*h)
   values[sign].append(min(cell['raw'],max(bounds)))
 need(filtered>0,'empty region is reported separately')
 return dict(pl=pl,pu=pu,H_lower=hl,H_upper=hu,lambda_upper=lambda_upper,cells=filtered,resource={s:max(v) for s,v in values.items()})

def main():
 need(__debug__ and not sys.flags.optimize,'ordinary Python')
 p=ROOT/'runs/fixed-target-v8-20261028/phase01/stdout.json';source=json.loads(p.read_text());z=dec(source);cells=z['phase_cells']
 need(z['total_cells']==2048 and len(cells)==z['active_cells']==682,'selected last-stage export')
 for x in cells:
  need(0<x['pl']<=x['pu']<1 and len(x['quadratics'])==2,'actual event/endpoint shape')
  for q in x['quadratics']:
   c=q['c'];terms=[c*k+ph*w for k in x['K1'] for ph in x['density'] for w in x['W']]
   need(q['plus']==max(terms)+x['slope'] and q['minus']==-min(terms)+x['slope'],'independent signed coefficient reconstruction')
   need(q['B']==x['Fourier']+c*x['A'],'constant reconstruction')
   need(q['Q']==c*x['rho'][0]+min(ph*x['gamma'][0]/2 for ph in x['density'])+x['eta'],'curvature reconstruction')
   need(q['plus']<=q['absolute'] and q['minus']<=q['absolute'],'signed versus absolute')
 results=[]
 for l,h in [(F(5,4),F(5,4)),(F(31,25),F(63,50)),(F(6,5),F(13,10))]:
  for lam in [None,F(3,20),F(4,25)]:results.append(evaluate(cells,F(41,100),F(42,100),l,h,lam))
 controls=[]
 def reject(name,fn):
  try:fn()
  except ValueError:controls.append(name)
  else:raise ValueError('accepted invalid '+name)
 reject('reversed phase interval',lambda:evaluate(cells,F(41,100),F(42,100),F(2),F(1)))
 reject('reversed probability interval',lambda:evaluate(cells,F(42,100),F(41,100),F(1),F(2)))
 reject('negative noise',lambda:evaluate(cells,F(41,100),F(42,100),F(1),F(2),F(-1)))
 # The common theta price must not be reflected by replacing p with min(p,1-p).
 p0=F(13,25);theta0=F(1,100);true_upper=1-2*p0+2*p0*theta0
 need(true_upper>1-2*p0+theta0,'p above one half needs correct signed beta price')
 controls.append('invalid plus-Theta beta shortcut')
 print(json.dumps(encode(dict(status='PASS_BOUNDED_PHASE_REGION_EVALUATION',source_sha256=sha256(p.read_bytes()).hexdigest(),regions=results,
 rejected_controls=controls,scope='Exact evaluation of exported valid scalar envelopes on these closed regions; no full confinement or count comparison.')),indent=2))
if __name__=='__main__':main()

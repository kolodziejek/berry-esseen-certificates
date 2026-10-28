#!/usr/bin/env python3
"""Bounded exact exploration of the binary defect charge against phase cells.

This discovery report is conditional on the complete accepted phase export.
It never reports a complete proof or changes an inherited certificate.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,sys
ROOT=Path(__file__).resolve().parents[3]
PHASE=ROOT.parent/'phase-entry-v8/runs/fixed-target-v8-20261028/phase01/stdout.json'
MOMENT=ROOT/'runs/fixed-target-v8-20261028/moment03/stdout.json'
def need(x,s):
 if not x:raise ValueError(s)
def decode(x):
 if isinstance(x,str):
  try:return F(x)
  except ValueError:return x
 if isinstance(x,list):return [decode(v) for v in x]
 if isinstance(x,dict):return {k:decode(v) for k,v in x.items()}
 return x
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,list):return [encode(v) for v in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x
def ceil9(x):return F(-((-x.numerator*10**9)//x.denominator),10**9)
def main():
 need(__debug__ and not sys.flags.optimize,'unoptimized Python')
 blob=PHASE.read_bytes();need(sha256(blob).hexdigest()=='b18599468c975032f4078e7a5f734fd6430b2b7da583789de58d9537d323f690','frozen phase output')
 cells=decode(json.loads(blob))['phase_cells'];moment=decode(json.loads(MOMENT.read_bytes()))
 sigma=F('3.162277660');pstar_l=(4-F('3.162277661'))/2;pstar_u=(4-sigma)/2;kappa=F(997,15000)
 rows=[]
 for panel in moment['panels']:
  if panel['excluded']:continue
  vals={s:[] for s in ('plus','minus')};details=[]
  for cell in cells:
   l=max(panel['pl'],cell['pl']);u=min(panel['pu'],cell['pu'])
   if l>u:continue
   vmax=max(l*(1-l),u*(1-u),F(1,4) if l<=F(1,2)<=u else F(0))
   distance=max(F(0),l-pstar_u,pstar_l-u)
   binary=max(panel['binary_floor'],(6+2*sigma)*cell['m'][0]**3*distance**2/(vmax*vmax))
   signed={}
   for sign in vals:
    upper=[]
    for quad in cell['quadratics']:
     B,f,Q=quad['B'],quad[sign],quad['Q'];need(Q>0,'positive curvature')
     h=max(F(0),min(cell['H'],f/(2*Q)))
     upper.append(B+f*h-Q*h*h)
    resource=min(cell['raw'],max(upper));reserve=resource-42*kappa*binary
    vals[sign].append(reserve);signed[sign]=reserve
   details.append(dict(rho=cell['rho'],beta=cell['beta'],gamma=cell['gamma'],p=[l,u],binary_floor=binary,reserve=signed))
  need(details,'nonempty panel')
  bound={s:ceil9(max(v)) for s,v in vals.items()}
  rows.append(dict(index=panel['index'],p=[panel['pl'],panel['pu']],cells=len(details),reserve_upper=bound,excluded=all(x<0 for x in bound.values()),details=details))
 print(json.dumps(encode(dict(status='BOUNDED_BINARY_PHASE_RESOURCE_PROBE',phase_sha256=sha256(blob).hexdigest(),moment_sha256=sha256(MOMENT.read_bytes()).hexdigest(),rows=rows,excluded=[z['index'] for z in rows if z['excluded']],scope='Exact necessary-condition exploration; requires accepted source cover, common actual-law binary defect inequality, and independent review.')),indent=2))
if __name__=='__main__':main()

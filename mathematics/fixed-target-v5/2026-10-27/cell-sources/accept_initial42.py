#!/usr/bin/env python3
"""New fixed theorem INITIAL42_R384; the old47 proof is unchanged.

Complete signed initialization under its own explicit N42 hypotheses.

Assumes actual support[-3.84,3.84], n>=42, CE<=C_n<=.4247.
The all-p panel cover has exactly 100 closed cells covering [0,1].
This is an entry component, not a complete cutoff theorem.
"""
from fractions import Fraction as F
from pathlib import Path
import copy,hashlib,json,sys
import local_signed_core as c
P=dict(n=42,nmax=98,radius=F('3.84'),cap=F('.4247'),barrier=F(0),grid=[24,24,8,4])
def need(v,s):
 if not v:raise ValueError(s)
def fields(o,names):need(type(o)is dict and set(o)==set(names),'exact object fields')
def rat(x):
 need(type(x)is str and len(x)<100,'rational string');r=F(x);need(str(r)==x,'canonical rational');return r
def unique(pairs):
 d={}
 for key,value in pairs:need(key not in d,'duplicate JSON key');d[key]=value
 return d
def shape(o):
 fields(o,('format','name','steps','panels'))
 need(o['format']=='INITIAL42_FULL_P_V1' and o['name']=='INITIAL42_R384','fixed theorem name')
 rows=o['steps'];need(type(rows)is list and len(rows)==12,'ordered finite stage list')
 raw=d=None
 for row in rows:
  fields(row,('raw','defect','active','excluded'));r,e=rat(row['raw']),rat(row['defect'])
  need(0<r<F('.4')*42 and 0<e<4,'initial feedback license')
  if raw is not None:need(r<=raw and e<=d and (r<raw or e<d),'strict ordered progress')
  need(type(row['active'])is int and type(row['excluded'])is int,'integer cover count')
  need(row['active']>0 and row['excluded']>=0 and row['active']+row['excluded']==18432,'complete signed cover')
  raw,d=r,e
 need(raw<F('2.24') and d<F('.784'),'fixed final coarse target')
 need(type(o['panels'])is list and len(o['panels'])==100,'complete probability cover')
 for j,z in enumerate(o['panels']):
  fields(z,('pl','pu','raw','D','theta','rho','beta','H','cells'))
  need(rat(z['pl'])==F(j,100) and rat(z['pu'])==F(j+1,100),'ordered contiguous closed probability cells')
  need(type(z['cells'])is int and z['cells']>=0,'integer incidence count')
  for key in('raw','D','theta','rho','beta','H'):rat(z[key])
  if z['cells']:
   need(0<rat(z['raw'])<F('2.24') and 0<rat(z['D'])<F('.784'),'coarse panel resource targets')
   need(0<=rat(z['theta'])<1 and 1<=rat(z['rho'])<F('1.526') and 0<=rat(z['beta'])<F('.523') and 0<rat(z['H'])<F('1.947'),'coarse panel moment targets')
  else:need([z[key]for key in('raw','D','theta','rho','beta','H')]==['-1','-1','0','1','0','0'],'empty-panel sentinel only')
 return raw,d
def verify(o,emit=False):
 shape(o);raw=d=None;total=0
 for j,row in enumerate(o['steps']):
  out=c.stage(P,raw,d);r,e=F(row['raw']),F(row['defect'])
  need(out['active']==row['active'] and out['excluded']==row['excluded'],'complete recorded signed cover counts')
  need((raw is not None and r==raw)or out['R']<r,'strict raw ceiling')
  need((d is not None and e==d)or out['D']<e,'strict defect ceiling')
  raw,d=r,e;total+=out['total']
  if emit:print('PASS_INITIAL42_STAGE',j,row,flush=True)
 out=c.stage(P,raw,d);total+=out['total']
 need(d<c.k.SL-1,'every final moment cell has an actual central gap')
 for target,actual in zip(o['panels'],out['panels']):
  need(target['cells']==actual['cells'],'every probability-panel incidence recorded')
  need(F(target['pl'])==actual['pl'] and F(target['pu'])==actual['pu'],'panel endpoints')
  for key in('raw','D','theta','rho','beta','H'):
   need(F(target[key])>=actual[key],'panel upper enclosure '+key)
 return dict(name=o['name'],raw=str(raw),defect=str(d),signed_cells=total,probability_panels=100,nonempty_probability_panels=sum(z['cells']>0 for z in o['panels']))
def controls(o):
 cases=[]
 def add(fn,deep=False):
  z=copy.deepcopy(o);fn(z);cases.append((z,deep))
 add(lambda z:z.pop('format'));add(lambda z:z.update(extra=1));add(lambda z:z.update(name='INITIAL48'))
 add(lambda z:z['steps'].reverse());add(lambda z:z['steps'].insert(1,z['steps'][0]));add(lambda z:z['steps'][0].update(raw='100'))
 add(lambda z:z['steps'][0].update(active=True));add(lambda z:z['panels'].pop());add(lambda z:z['panels'].reverse())
 add(lambda z:z['panels'].insert(1,z['panels'][0]));add(lambda z:z['panels'][0].update(pu='1/50'))
 add(lambda z:z['panels'][0].update(pl='nan'));add(lambda z:z['panels'][0].update(pl='00'))
 add(lambda z:z['steps'][0].update(raw='1'),True)
 add(lambda z:z['steps'][0].update(active=z['steps'][0]['active']-1,excluded=z['steps'][0]['excluded']+1),True)
 for z,deep in cases:
  try:verify(z)if deep else shape(z)
  except (ValueError,TypeError,ZeroDivisionError):pass
  else:raise ValueError('malformed or false initial proof accepted')
 try:json.loads('{"x":1,"x":2}',object_pairs_hook=unique)
 except ValueError:pass
 else:raise ValueError('duplicate JSON key accepted')
 return len(cases)+1
if __name__=='__main__':
 need(__debug__ and not sys.flags.optimize,'optimized Python forbidden');need(len(sys.argv)==2,'one proof file')
 blob=Path(sys.argv[1]).read_bytes();o=json.loads(blob,object_pairs_hook=unique);out=verify(o,True)
 out.update(status='PASS_INITIAL42_C4247_FULL_PROBABILITY_COVER',theorem='INITIAL42_R384_C4247',negative_controls=controls(o),proof_sha256=hashlib.sha256(blob).hexdigest())
 out['source_sha256']={name:hashlib.sha256(Path(name).read_bytes()).hexdigest()for name in('accept_initial42.py','local_signed_core.py','high_window_core.py','kernel.py')}
 print(json.dumps(out,sort_keys=True),flush=True)

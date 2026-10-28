#!/usr/bin/env python3
"""Thirteen closed panels, direct low-noise contact support only.

Replay the bounded elementary moment antecedent, then check two boundaries
and twelve full-ray signs per panel. No Fourier or native kernel is imported.
The acceptance remains conditional on the analytic and v7 entry antecedents.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
from hashlib import sha256
from copy import deepcopy
import json,sys,subprocess,time,types,argparse
HERE=Path(__file__).resolve().parent
SOURCES=HERE/'low-noise-panels-sources'
MANIFEST='f57fa08fb8ade69178b34a5c4dd57b5c083c758dc505e8457238763cbcd55e7a'
HEAT_SHA='23669542b58d2476977a0692234517ef05fce9034b9881a381b7c1708cef6954'
N,NOISE,SIGMA,AMP=42,F(3,40),F(3,5),F(1,2)
def need(ok,why):
 if not ok:raise ValueError(why)
def unique(pairs):
 out={}
 for k,v in pairs:need(k not in out,'duplicate JSON key');out[k]=v
 return out
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encode(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v)for v in x]
 return x
def lo(x):
 need(x>=0,'root domain');v=F(isqrt(x.numerator*10**20//x.denominator),10**10)
 need(v*v<=x<(v+F(1,10**10))**2,'outward root');return v
def load_heat():
 path=HERE/'phase-confinement-heat.py';blob=path.read_bytes();need(sha256(blob).hexdigest()==HEAT_SHA,'reviewed heat source')
 module=types.ModuleType('reviewed_heat');module.__file__=str(path)
 exec(compile(blob,str(path),'exec'),module.__dict__);return module
def replay(evidence):
 blob=(SOURCES/'manifest.json').read_bytes();need(sha256(blob).hexdigest()==MANIFEST,'source manifest')
 pins=json.loads(blob,object_pairs_hook=unique)
 need({p.name for p in SOURCES.iterdir()}==set(pins)|{'manifest.json'}and all(p.is_file()and not p.is_symlink()for p in SOURCES.iterdir()),'exact source tree')
 for name,digest in pins.items():need(sha256((SOURCES/name).read_bytes()).hexdigest()==digest,'source pin '+name)
 cache=evidence/'child-cache';cache.mkdir()
 argv=[sys.executable,'-I','-B','-X','pycache_prefix='+str(cache.resolve()),str(SOURCES/'moment-entry-v8.py')]
 start=time.time();p=subprocess.run(argv,capture_output=True);elapsed=time.time()-start
 (evidence/'moment-stdout.json').write_bytes(p.stdout);(evidence/'moment-stderr.txt').write_bytes(p.stderr)
 receipt=dict(argv=argv,cwd=str(Path.cwd()),returncode=p.returncode,elapsed_seconds=elapsed,
  source_manifest_sha256=MANIFEST,stdout_sha256=sha256(p.stdout).hexdigest(),stderr_sha256=sha256(p.stderr).hexdigest())
 (evidence/'moment-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
 need(p.returncode==0 and not list(cache.rglob('*')),'fresh isolated elementary replay')
 fresh=json.loads(p.stdout,object_pairs_hook=unique)
 need(fresh==json.loads((SOURCES/'moment03-stdout.json').read_text(),object_pairs_hook=unique),'full elementary output recomputed')
 return fresh,receipt
def check_premises(source,heat):
 rows=[z for z in source['panels']if z['index']in range(40,53)]
 need([z['index']for z in rows]==list(range(40,53)),'all thirteen ordered panels')
 for i,z in enumerate(rows,40):
  l,h=F(z['pl']),F(z['pu']);need(l==F(i,100)and h==F(i+1,100)and not z['excluded'],'literal nonempty closed panel')
  need(0<=F(z['d'])<F(72,1000)<AMP,'previous inward bound')
  E,r,bm,bp=[F(z[k])for k in ('ell_l','rho','beta_l','beta_u')]
  for sign,u,b in [('negative',E*(l+SIGMA),-bm),('positive',E*(1+SIGMA-h),bp)]:
   got=heat.boundary(u,r,b);need(got['heat_upper']==F(z['strip_'+sign]['boundary']),'recomputed acquired strip boundary')
   need(got['ray_signs']==[F(x)for x in z['strip_'+sign]['rays']],'recomputed acquired strip rays')
 return rows
def one(index,heat):
 l,h=F(index,100),F(index+1,100)
 v=min(l*(1-l),h*(1-h));V=max(l*(1-l),h*(1-h),F(1,4)if l<=F(1,2)<=h else F(0))
 M=max(h,1-l)
 need(24**2*v**3>(3*M+SIGMA)**2,'both-orientation cubic coefficient')
 theta=NOISE/(N*v+NOISE);ell=lo((1-theta)/V)
 rho=(1-2*v)/lo(v)+24*NOISE/N
 bm=1-2*h-2*(1-h)*theta;bp=1-2*l+2*l*theta
 neg=heat.boundary(ell*(l+AMP),rho,-bm)
 pos=heat.boundary(ell*(1+AMP-h),rho,bp)
 return dict(index=index,p=[l,h],vmin=v,vmax=V,theta_upper=theta,ell_lower=ell,rho_upper=rho,
  beta_lower=bm,beta_upper=bp,negative=neg,positive=pos)
def main():
 need(__debug__ and not sys.flags.optimize,'unoptimized Python')
 ap=argparse.ArgumentParser();ap.add_argument('--evidence',type=Path,required=True);args=ap.parse_args()
 args.evidence.mkdir(parents=True,exist_ok=True);need(not(args.evidence/'moment-stdout.json').exists(),'fresh evidence path')
 heat=load_heat();source,receipt=replay(args.evidence);prior=check_premises(source,heat)
 need(24**2*F(6,25)**3>(3*F(3,5)+SIGMA)**2,'single cubic coefficient on whole [.40,.53]')
 rows=[one(i,heat)for i in range(40,53)]
 need(rows[0]['p'][0]==F(2,5)and rows[-1]['p'][1]==F(53,100)and all(a['p'][1]==b['p'][0]for a,b in zip(rows,rows[1:])),'complete closed union with shared seams')
 controls=[]
 def reject(name,fn):
  try:fn()
  except (ValueError,KeyError):controls.append(name)
  else:raise ValueError('invalid control accepted '+name)
 bad=deepcopy(source);bad['panels']=[z for z in bad['panels']if z['index']!=47]
 reject('missing acquired panel',lambda:check_premises(bad,heat))
 bad=deepcopy(source);bad['panels'].reverse();reject('reordered acquired panels',lambda:check_premises(bad,heat))
 fortyone=rows[1];reject('wrong negative-ray sign',lambda:heat.boundary(fortyone['negative']['radius'],fortyone['rho_upper'],fortyone['beta_upper']))
 reject('wrong variance at p=.5',lambda:need(F(49,100)*F(51,100)>=F(1,4),'interior variance maximum'))
 # A genuine centered, variance-one law refutes the +Theta beta shortcut above .5.
 law=[(F(-26,25),F(12,25)),(F(1,2),F(52,6977)),(F(7226,7475),F(89401,174425))]
 need(sum(w for x,w in law)==1 and sum(x*w for x,w in law)==0 and sum(x*x*w for x,w in law)==1,'standardized orientation control')
 p=sum(w for x,w in law if x>0);m=sum(x*w for x,w in law if x>0);theta=1-m*m/(p*(1-p));beta=sum(x*abs(x)*w for x,w in law)
 reject('above-half +Theta shortcut',lambda:need(beta<=1-2*p+theta,'false beta upper'))
 reject('unlicensed cubic coefficient',lambda:need(18**2*F(6,25)**3>(3*F(3,5)+SIGMA)**2,'cubic gate'))
 reject('duplicate JSON key',lambda:json.loads('{"p":1,"p":2}',object_pairs_hook=unique))
 print(json.dumps(encode(dict(status='PASS_CONDITIONAL_THIRTEEN_PANEL_LOW_NOISE_HALF_AMPLITUDE',
  mathematical_scope='Every n>=42, p in [.40,.53], same-law lambda in [0,.075], all raw H. Conditional on the acquired .6 strips/d<.072 and fixed-target contact/sharp predecessor. Not full-noise confinement, count comparison or global proof.',
  manifest_sha256=MANIFEST,heat_source_sha256=HEAT_SHA,fresh_elementary_replay=receipt,
  panels=rows,noise_interval=[F(0),NOISE],target_amplitude=AMP,panel_count=len(rows),boundary_count=2*len(rows),ray_sign_count=12*len(rows),
  least_boundary_margin=min(-z[s]['heat_upper']for z in rows for s in ('negative','positive')),
  least_ray_sign_margin=min(-x for z in rows for s in ('negative','positive')for x in z[s]['ray_signs']),
  orientation_control=dict(law=law,p=p,theta=theta,beta=beta,false_upper=1-2*p+theta),rejected_controls=controls)),indent=2,sort_keys=True))
if __name__=='__main__':main()

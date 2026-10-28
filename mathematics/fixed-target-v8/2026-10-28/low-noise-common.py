#!/usr/bin/env python3
"""A simpler common moment enclosure for the thirteen low-noise panels."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import types,json,sys
HERE=Path(__file__).resolve().parent
SHA='23669542b58d2476977a0692234517ef05fce9034b9881a381b7c1708cef6954'
def need(ok,why):
 if not ok:raise ValueError(why)
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encode(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v)for v in x]
 return x
def run():
 need(__debug__ and not sys.flags.optimize,'ordinary Python')
 p=HERE/'phase-confinement-heat.py';blob=p.read_bytes();need(sha256(blob).hexdigest()==SHA,'reviewed heat formula')
 hmod=types.ModuleType('heat_common');hmod.__file__=str(p);exec(compile(blob,str(p),'exec'),hmod.__dict__)
 theta,E,rho=F(37,5000),F(249,125),F(221,200)
 v=F(6,25);noise=F(3,40);cubic_margin=24**2*v**3-F(12,5)**2
 need(cubic_margin>0 and noise/(42*v+noise)<theta,'uniform cubic and theta gates')
 need(E>0 and E*E<4*(1-theta),'uniform scale lower')
 rem=rho-24*noise/42
 need(rem>0 and rem*rem*v>(1-2*v)**2,'uniform third moment upper')
 rows=[]
 for i in range(40,53):
  l,u=F(i,100),F(i+1,100)
  bm=1-2*u-2*(1-u)*theta;bp=1-2*l+2*l*theta
  rows.append(dict(index=i,p=[l,u],beta=[bm,bp],negative=hmod.boundary(E*(l+F(1,2)),rho,-bm),positive=hmod.boundary(E*(F(3,2)-u),rho,bp)))
 need(all(a['p'][1]==b['p'][0]for a,b in zip(rows,rows[1:])),'closed seams')
 return dict(status='PASS_CONDITIONAL_COMMON_CAP_THIRTEEN_PANEL_LOW_NOISE',theta_upper=theta,ell_lower=E,rho_upper=rho,
  noise_upper=noise,p_range=[F(2,5),F(53,100)],panels=rows,boundaries=26,ray_signs=156,
  least_boundary_margin=min(-r[s]['heat_upper']for r in rows for s in ('negative','positive')),
  least_ray_margin=min(-x for r in rows for s in ('negative','positive')for x in r[s]['ray_signs']),
  source_sha256=SHA,scope='All n>=42 and all raw H, same-law lambda<=.075, conditional on acquired .6 strip/inward bound and fixed-target support contact. No high-noise claim.')
if __name__=='__main__':print(json.dumps(encode(run()),indent=2,sort_keys=True))

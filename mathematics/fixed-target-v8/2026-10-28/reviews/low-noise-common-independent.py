#!/usr/bin/env python3
"""Independent common-constant check using only this reviewer's heat evaluator."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,sys,types
p=Path(__file__).with_name('low-noise-independent.py')
EXPECTED='ac7184b4b03bc28b54e1e4c549063865e3812be0eaff7d1e8fc0ace47bdf84a6'
b=p.read_bytes()
if sha256(b).hexdigest()!=EXPECTED:raise ValueError('reviewed evaluator source')
module=types.ModuleType('own_heat_review');module.__file__=str(p)
exec(compile(b,str(p),'exec'),module.__dict__)
need=module.require;evaluate=module.evaluate
need(__debug__ and not sys.flags.optimize,'ordinary Python')
theta,ell,rho=F(37,5000),F(249,125),F(221,200)
need(F(5,677)<theta,'uniform noise ceiling')
need(ell*ell<4*(1-theta),'uniform scale lower')
need(rho>F(3,70) and (rho-F(3,70))**2*F(6,25)>F(13,25)**2,'uniform third moment ceiling')
need(24**2*F(6,25)**3>F(12,5)**2,'uniform cubic price')
rows=[]
for i in range(40,53):
 l,u=F(i,100),F(i+1,100)
 bl=1-2*u-2*(1-u)*theta;bu=1-2*l+2*l*theta
 rows.append(dict(index=i,negative=evaluate(ell*(l+F(1,2)),rho,-bl),positive=evaluate(ell*(F(3,2)-u),rho,bu)))
worst=max((r[side]['contact_upper']for r in rows for side in ('negative','positive')))
print(json.dumps(module.encode(dict(status='PASS_INDEPENDENT_COMMON_CONSTANTS',source_evaluator_sha256=sha256(b).hexdigest(),theta=theta,ell=ell,rho=rho,panels=rows,strict_boundaries=26,strict_derivative_gates=156,worst_boundary=worst,scope='Same conditional low-noise thirteen-panel theorem; independent check of coarser uniform constants, no new numerical constructor imported.')),indent=2,sort_keys=True))

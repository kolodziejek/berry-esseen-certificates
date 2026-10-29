#!/usr/bin/env python3
"""Add read-only signed phase export to frozen v7 arithmetic; retain all bounds."""
from pathlib import Path
from hashlib import sha256
here=Path(__file__).resolve().parent;root=here.parents[2]
p=root/'mathematics/fixed-target-v7/2026-10-27/signed_core.py';s=p.read_text()
assert sha256(p.read_bytes()).hexdigest()=='1f40ccb90eb58a7f84dc61a0a5dd9bf6e6eb4e341aa6c9c6d049d08451f5211b'
patches=[("peakR=F(-1);peakD=F(-1);active=excluded=0;reasons={};worst=None", "peakR=F(-1);peakD=F(-1);active=excluded=0;reasons={};worst=None;phase_cells=[]"),
("     if gap:\n      cellRaw=", """     k.need(gap,'phase export requires an actual gap')
     signed_quadratics=[]
     for c,absolute_linear,q in coefs:
      terms=[c*kk+ph*uu for kk in(kl,ku) for ph in(phlo,F(2,5)) for uu in(ulo,uhi)]
      fp=max(terms)+slope;fm=-min(terms)+slope
      k.need(fp<=absolute_linear and fm<=absolute_linear,'signed phase slopes bounded by old absolute slope')
      signed_quadratics.append(dict(c=c,B=kf+c*A,plus=fp,minus=fm,Q=q+eta_phase,absolute=absolute_linear))
     phase_cells.append(dict(rho=[rl,rh],beta=[bl,bu],gamma=[l,h],m=[ml,mu],pl=pl,pu=pu,
        raw=new_raw,old_defect=d,defect_lower=dlower,eta=eta_phase,K1=[kl,ku],W=[ulo,uhi],density=[phlo,F(2,5)],
        A=A,Fourier=kf,slope=slope,H=cellH,radius=R,quadratics=signed_quadratics))
     if gap:
      cellRaw="""),
("panels=panels,moments=moments,worst=worst)","panels=panels,moments=moments,worst=worst,phase_cells=phase_cells)")]
for a,b in patches:
 assert s.count(a)==1;s=s.replace(a,b)
t=s
for a,b in reversed(patches):
 assert t.count(b)==1;t=t.replace(b,a)
assert t==p.read_text()
(here/'phase_core.py').write_text(s)
print(sha256(s.encode()).hexdigest())

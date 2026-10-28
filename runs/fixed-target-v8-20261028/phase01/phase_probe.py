#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import sys,json
here=Path(__file__).resolve().parent;root=here.parents[2]
sys.path.insert(0,str(root/'mathematics/fixed-target-v7/2026-10-27'))
import accept_entry as accepted
import signed_support as support
import phase_core as core
proof_path=root/'mathematics/fixed-target-v7/2026-10-27/entry-proof.json'
assert sha256(proof_path.read_bytes()).hexdigest()=='61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae'
proof=json.loads(proof_path.read_text(),object_pairs_hook=accepted.unique);accepted.shape(proof)
rows=[];cells=[];total=0
for i,(prior,target) in enumerate(zip(proof['steps'][2],proof['steps'][3])):
 if target.get('prior_excluded'):continue
 l,u=1+F(3361*i,96000),1+F(3361*(i+1),96000)
 R,_,_=support.cell_radius(u);assert R==F(target['radius'])
 p=dict(n=42,nmax=42,radius=R,barrier=F(0),cap=accepted.C1,c_lower=accepted.C0,c_upper=accepted.C1,grid=[1,8,8,2],rho_lower=l,rho_upper=u)
 out=core.stage(p,F(prior['raw']),F(prior['defect']))
 accepted.check_row(target,out,F(prior['raw']),F(prior['defect']))
 assert len(out['phase_cells'])==out['active'];cells.extend(out['phase_cells']);total+=out['total']
 rows.append(dict(index=i,active=out['active'],excluded=out['excluded'],raw=out['R'],D=out['D']))
pl,pu,H,lam=F(41,100),F(42,100),F(5,4),F(3,20)
pqlo=min(pl*(1-pl),pu*(1-pu));pqhi=max(pl*(1-pl),pu*(1-pu))
theta=lam/(42*pqlo+lam);ml=core.sl(pqlo*pqlo/(pqlo+lam/42));mu=core.su(pqhi)
betal=1-2*pu-2*(1-pl)*theta;betau=1-2*pl+2*pu*theta
eligible=[x for x in cells if x['pl']<=pu and x['pu']>=pl and x['H']>=H]
noise=[x for x in eligible if x['m'][1]>=ml and x['m'][0]<=mu and x['beta'][1]>=betal and x['beta'][0]<=betau]
summary={}
for name,fam in [('panel_phase',eligible),('panel_phase_noise',noise)]:
 summary[name]={}
 for sign in ['plus','minus','absolute']:
  vals=[min(x['raw'],max(z['B']+z[sign]*H-z['Q']*H*H for z in x['quadratics'])) for x in fam]
  summary[name][sign]=max(vals) if vals else None
 summary[name]['cells']=len(fam)
print(json.dumps(accepted.encode(dict(status='EXPLORATORY_SAME_CELL_PHASE_EXPORT',source_proof_sha256=sha256(proof_path.read_bytes()).hexdigest(),
 total_cells=total,active_cells=len(cells),rows=rows,phase_cells=cells,
 probe=dict(pl=pl,pu=pu,H=H,lambda_value=lam,theta_upper=theta,m_lower=ml,m_upper=mu,beta_lower=betal,beta_upper=betau,summary=summary))),indent=2))
print(json.dumps(accepted.encode(summary)),file=sys.stderr)

"""Independent direct reconstruction of raw-moment dual target tensors."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('unoptimized Python')
HERE=Path(__file__).resolve().parent;SRC=HERE.parent/'construct'
sys.path.insert(0,str(HERE));import independent_polys as t
sys.path.insert(0,str(SRC));import model_dual as m
def need(x,msg):
    if not x:raise ValueError(msg)
def main(out):
    files=[Path(__file__),HERE/'independent_polys.py',SRC/'model.py',SRC/'model_dual.py',SRC/'algebra.py']+sorted((SRC/'contracts').glob('*.json'))+sorted((SRC/'native').glob('*.py'))
    before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    c=dict(raw_interval_tests=0,common_rows=0,dual_coefficients=0,coefficient_mutants=0,guard_controls=0,signed_product_cases=0)
    for key in sorted(m.CONTRACTS):
      r=m.Row(key)
      for lo,hi in ((F(0),r.LAMBDA),(r.LAMBDA/4,r.LAMBDA/2)):
        k=min(r.roots);pl,pu=r.pl,r.pu;ul,uh=r.roots[k];d=r.cell(k,[pl,pu],[ul,uh],[lo,hi])
        vmin,vmax=m.variance_bounds(pl,pu)
        wlo=vmin+lo/5;whi=vmax+r.effective_hi(pl,pu,hi)/5
        sl=wlo*m.normal.root(wlo)[0];sh=whi*m.normal.root(whi)[1]
        gl,gh=map(F,r.cfg['acquired_gamma']);rl,rh=map(F,(r.cfg['rho_lower'],r.cfg['rho_upper']))
        expected=(rl*sl,rh*sh,min(g*s for g in (gl,gh)for s in (sl,sh)),max(g*s for g in (gl,gh)for s in (sl,sh)))
        need(r.raw_bounds(d)==expected,'independent four-product raw bounds');c['raw_interval_tests']+=1
        rows=r.dual_tensors(d);r0,r1=r.inward(pl,pu,lo)
        corners=[(x,y,g0,g1)for x,y in r.polygon(pl,pu,lo,hi)for g0,g1 in product((-r.A0,F(0),r0),(r.A1,F(0),-r1))]
        need(len(rows)==len(corners),'complete dual common corners')
        Rlo,Rhi,Glo,Ghi=expected
        for tensors,(x,y,g0,g1) in zip(rows,corners):
            R=t.add(t.mul(t.V,t.add(t.ONE,t.scale(t.V,-2))),t.scale(t.P,3*x),t.scale(t.Q,3*y),t.scale(t.ONE,-g0*x+g1*y))
            G=t.add(t.mul(t.V,t.add(t.ONE,t.scale(t.P,-2))),t.scale(t.P,-3*x),t.scale(t.Q,3*y),t.scale(t.ONE,g0*x+g1*y))
            slacks=[t.add(t.scale(t.ONE,Rlo),t.scale(R,-1)),t.add(R,t.scale(t.ONE,-Rhi)),
                    t.add(t.scale(t.ONE,Glo),t.scale(G,-1)),t.add(G,t.scale(t.ONE,-Ghi))]
            need(len(tensors)==4,'four ordered prices')
            for tensor,slack in zip(tensors,slacks):
                direct=t.local(t.mul(t.V2,slack),pl,pu,ul,uh)
                need(t.inverse(tensor)==direct,'full independent dual polynomial identity')
                need(all(i<=9 and j==0 for i,j in direct),'dual degree and phase independence')
                bad=list(tensor);bad[0]+=F(1,10**6)
                need(t.inverse(bad)!=direct,'corrupt dual coefficient detected')
                c['dual_coefficients']+=50;c['coefficient_mutants']+=1
            c['common_rows']+=1
        # Guard controls deliberately reach the scalar guard before any quartic work.
        for prices,message in ((['-1','0','0','0'],'nonnegative exact moment prices'),
          (['0','0','0'],'four original moment prices'),
          ([0,'0','0','0'],'rational data must be strings'),
          (['2/2','0','0','0'],'canonical rational string')):
            try:r.admit([], '0',prices,d)
            except ValueError as e:need(str(e)==message,'expected dedicated price guard');c['guard_controls']+=1
            else:raise ValueError('invalid price guard accepted')
    # Explicit all-negative and sign-crossing interval-product controls.
    for gl,gh in ((F(-3,4),F(-1,4)),(F(-1,3),F(2,3)),(F(1,5),F(4,5))):
      sl,sh=F(1,8),F(27,8)
      lower=min(gl*sl,gl*sh);upper=max(gh*sl,gh*sh)
      for g,s in product((gl,(gl+gh)/2,gh),(sl,(sl+sh)/2,sh)):
        need(lower<=g*s<=upper,'signed width product');c['signed_product_cases']+=1
    after={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in files};need(before==after,'all source bytes stable')
    z=dict(status='PASS_EXACT_DUAL_MODEL_RECONSTRUCTION',scope='Conditional dual-license algebra and scalar guards only; no numerical comparison tree or full-row claim.',counts=c,source_sha256=before)
    out=Path(out);out.mkdir(parents=True,exist_ok=False);(out/'RESULT.json').write_text(json.dumps(z,indent=2)+'\n');print(json.dumps({k:v for k,v in z.items()if k!='source_sha256'}))
if __name__=='__main__':main(sys.argv[1])

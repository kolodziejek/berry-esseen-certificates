"""Independent exact polynomial reconstruction of the new three-row model."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('unoptimized Python')
HERE=Path(__file__).resolve().parent;SRC=HERE.parent/'construct'
sys.path.insert(0,str(HERE));import independent_polys as t
sys.path.insert(0,str(SRC));import model as m
def need(x,msg):
    if not x:raise ValueError(msg)
def main(out):
    files=[Path(__file__),HERE/'independent_polys.py',SRC/'model.py',SRC/'algebra.py']+sorted((SRC/'contracts').glob('*.json'))+sorted((SRC/'native').glob('*.py'))
    before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    qs=[[F(j+2,5),F(j-3,7),F(j-2,11),F((-1)**j,13),F(j+1,17)] for j in range(6)]
    counts=dict(rows=0,moment_coefficients=0,target_coefficients=0,coefficient_mutants=0,scalar_enclosures=0)
    scopes=[]
    for key in sorted(m.CONTRACTS):
        r=m.Row(key);l,h=r.pl,r.pu
        ends=(l*(1-l),h*(1-h));vmin=min(ends);vmax=F(1,4)if l<=F(1,2)<=h else max(ends)
        need(m.variance_bounds(l,h)==(vmin,vmax),'independent exact v extrema')
        generic_hi=min(r.LAMBDA,5*max(vmin*vmin/r.MEAN_LO**2-vmin,vmax*vmax/r.MEAN_LO**2-vmax))
        need(r.effective_hi(l,h,r.LAMBDA)==generic_hi,'convex endpoint maximum equals guarded monotone cap')
        k=min(r.roots);ul,uh=r.roots[k]
        domains=[r.cell(k,[l,h],[ul,(ul+uh)/2],[0,r.LAMBDA]),
                 r.cell(max(r.roots),[l,h],[-F(1,4),F(1,4)],[0,r.LAMBDA])]
        scopes.append(dict(row=key,contract=r.contract_sha,domains=[[d[0]]+list(map(str,d[1:]))for d in domains]))
        for d in domains:
            k,pl,pu,ul,uh,lo,hi=d;vlo,vhi=m.variance_bounds(pl,pu)
            hi_eff=min(hi,5*max(vlo*vlo/r.MEAN_LO**2-vlo,vhi*vhi/r.MEAN_LO**2-vhi))
            rr=m.normal.root(vlo+lo/5)[0]
            expected_inward=(min(r.D,pu-r.NEG_LO*rr),min(r.D,1-pl-r.POS_LO*rr))
            need(r.inward(pl,pu,lo)==expected_inward,'independent inward caps');counts['scalar_enclosures']+=1
            rows=r.tensors(*d);targets,diffs,correlated=r.target_tensors(d)
            vertices=r.polygon(pl,pu,lo,hi)
            r0,r1=expected_inward
            corners=[(x,y,g0,g1) for x,y in vertices for g0,g1 in product((-r.A0,F(0),r0),(r.A1,F(0),-r1))]
            need(len(rows)==len(corners)==len(targets)==len(diffs),'same complete moment index')
            amin=k+ul-5*pu;amax=k+uh-5*pl;mono=0<=k+ul and k+uh<=5
            need(correlated==(amax<=0 and amin*amin<=15*vlo),'literal conservative concavity guard')
            whi=vhi+hi_eff/5
            scalar_c=m.normal.CE_LO/(m.normal.root(F(5))[1]*whi*m.normal.root(whi)[1])
            rho_floor=m.normal.CE_LO*r.RHO/m.normal.root(F(5))[1];theta=F(2,3)
            for row,rhs,diff,(x,y,g0,g1) in zip(rows,targets,diffs,corners):
                combined=[sum(qs[j][s]*row[5*j+s][a] for j in range(6) for s in range(5)) for a in range(50)]
                direct=t.direct(k,x,y,g0,g1,qs)
                need(all(i<=9 and j<=4 for i,j in direct),'degree at most (9,4)')
                wanted=t.local(direct,pl,pu,ul,uh)
                need(t.inverse(combined)==wanted,'complete independent moment expansion')
                counts['rows']+=1;counts['moment_coefficients']+=50
                bad=combined[:];bad[29]-=F(1,10**8)
                need(t.inverse(bad)!=wanted,'corrupted coefficient rejected');counts['coefficient_mutants']+=1
                if mono:den=5*pu*(1-pu)+(5*(x+y)if correlated else(lo if amin<0 else hi_eff))
                else:den=5*vlo+5*(x+y)if correlated else(5*vlo+lo if amin<0 else 5*vhi+hi_eff)
                G=m.normal_lower(amin,den)
                R=t.add(t.mul(t.V,t.add(t.ONE,t.scale(t.V,-2))),t.scale(t.P,3*x),t.scale(t.Q,3*y),t.scale(t.ONE,-g0*x+g1*y))
                expected=t.mul(t.V2,t.add(t.scale(t.ONE,G+(1-theta)*rho_floor),t.scale(R,theta*scalar_c)))
                need(t.inverse([a+theta*b for a,b in zip(rhs,diff)])==t.local(expected,pl,pu,ul,uh),'complete common-rho and Gaussian target expansion')
                counts['target_coefficients']+=50
    after={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in files};need(before==after,'stable complete model sources')
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    z=dict(status='PASS_EXACT_TRANSFER_MODEL_RECONSTRUCTION',scope='Independent selected-cell polynomial/source review for all3 original contracts; no full comparison tree or acquisition acceptance.',counts=counts,cells=scopes,source_sha256=before)
    (out/'RESULT.json').write_text(json.dumps(z,indent=2)+'\n');print(json.dumps({k:v for k,v in z.items()if k!='source_sha256'}))
if __name__=='__main__':main(sys.argv[1])

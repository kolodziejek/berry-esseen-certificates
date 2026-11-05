"""Bounded source/endpoint checks before any new comparison campaign."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import ast,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model as m
def main(out):
    expected={'BN39':[1,2,3],'B0_50':[2,3],'B2_S3_34':[1,2,3]};census=[];checks=0
    for key in expected:
        r=m.Row(key);m.need(list(r.roots)==expected[key],'externally reviewed root census')
        vl,vh=m.variance_bounds(r.pl,r.pu)
        for i in range(101):
            p=r.pl+(r.pu-r.pl)*F(i,100);v=p*(1-p);m.need(vl<=v<=vh,'whole-cell variance extrema')
            for t in(F(0),F(5),F(1,2),F(5,2)):
                for lam in(F(0),r.LAMBDA):
                    bracket=5*p+t*(1-2*p)+2*lam
                    m.need(bracket>=5*min(p,1-p)+2*lam>0,'signed endpoint derivative')
                    checks+=1
        # Exact affine root coverage, including possible endpoints and all ties.
        for i in range(101):
            h=r.hlo+(r.hhi-r.hlo)*F(i,100)
            ks=[k for k in range(-2,8)if -F(1,2)<=h-k<=F(1,2)]
            m.need(ks and all(k in r.roots and r.roots[k][0]<=h-k<=r.roots[k][1]for k in ks),'mapped closed threshold covered')
        m.need(2*vl>r.MEAN_LO**2,'actual mean-monotonicity gate')
        poly=r.polygon(r.pl,r.pu,F(0),r.LAMBDA);inward=r.inward(r.pl,r.pu,F(0))
        census.append(dict(row_id=key,contract_sha256=r.contract_sha,p=list(map(str,(r.pl,r.pu))),rho=[r.cfg['rho_lower'],r.cfg['rho_upper']],
          noise=['0',str(r.LAMBDA)],v_bounds=list(map(str,(vl,vh))),threshold_bounds=list(map(str,(r.hlo,r.hhi))),
          roots=[dict(k=k,u=list(map(str,u)))for k,u in r.roots.items()],outer_vertices=[[str(x),str(y)]for x,y in poly],inward=list(map(str,inward))))
    # Check p=1/2-crossing and mirrored intervals, not only the selected rows.
    for a,b,lo,hi in[(F(49,100),F(51,100),F(2499,10000),F(1,4)),(F(1,2),F(51,100),F(2499,10000),F(1,4)),(F(2,5),F(3,5),F(6,25),F(1,4))]:
        m.need(m.variance_bounds(a,b)==(lo,hi),'two-sided/crossing exact variance bounds')
    out.mkdir(parents=True,exist_ok=False)
    result=dict(status='PASS_BOUNDED_INPUT_AND_ENDPOINT_CHECKS',rows=census,derivative_sign_checks=checks,
      scope='Exact source/domain and bounded implementation checks. Analytic monotonicity proof is separate. No score comparison accepted.',
      source_sha256={p.name:m.sha(p)for p in(HERE/'algebra.py',HERE/'model.py',Path(__file__))})
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main(Path(sys.argv[1]).resolve())

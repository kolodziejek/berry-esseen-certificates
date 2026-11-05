"""Same analytic scalar enclosure tested on the selected wider-phase domain."""
from pathlib import Path
from fractions import Fraction as F
import sys,json
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import check_broad as b
def main():
 b.m.need(__debug__ and not sys.flags.optimize,'ordinary Python');out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
 c=b.m.context(39,True);pl=F(77,200);pu=F(39,100);ul=-F(1,100);uh=-ul;count=0
 for x,y in b.r.polygon(c,pl,pu):
  lam=39*(x+y);poly,rec=b.gaussian(39,15,pl,pu,ul,uh,lam)
  for p in[pl,(pl+pu)/2,pu]:
   for u in[ul,F(0),uh]:
    actual=b.m.normal(15+u-39*p,39*p*(1-p)+lam);lower=sum(sum(v*p**j for j,v in enumerate(row))*u**h for h,row in enumerate(poly))
    b.m.need(lower<=actual,'independent exact Gaussian lower evaluation');count+=1
 result={'status':'PASS_WIDE_PHASE_GAUSSIAN_CONTROLS','rigorous_grid_comparisons':count,'p':list(map(str,(pl,pu))),'u':list(map(str,(ul,uh))),'scope':'Bounded implementation controls, not a substitute for the analytic Taylor proof and full Bernstein reader.','source_sha256':b.m.sha(__file__)}
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()

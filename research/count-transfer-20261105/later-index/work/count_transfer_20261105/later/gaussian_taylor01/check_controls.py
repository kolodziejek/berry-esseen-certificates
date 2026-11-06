"""Bounded independent scalar enclosure/expansion controls; not sampled acceptance."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import check_broad as b
def evaluate(poly,p,u):return sum(sum(c*p**j for j,c in enumerate(row))*u**h for h,row in enumerate(poly))
def main():
 m=b.m;m.need(__debug__ and not sys.flags.optimize,'ordinary Python');out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
 pl=F(3847,10000);pu=F(39,100);ul=-F(1,1000);uh=-ul;n=39;k=15;c=m.context(n,True)
 checks=expansions=jets=0;records=[]
 for x,y in b.r.polygon(c,pl,pu):
  lam=n*(x+y);poly,rec=b.gaussian(n,k,pl,pu,ul,uh,lam);pc=(pl+pu)/2;uc=(ul+uh)/2
  gp=sum(map(F,rec['gradient_p']))/2;gu=sum(map(F,rec['gradient_u']))/2;Mpp,Mpt,Muu=map(F,rec['absolute_hessian_bounds']);eta=F(rec['eta']);rem=F(rec['rounding_budget']);f0=F(rec['center_cdf_lower'])
  for ip in range(7):
   p=pl+(pu-pl)*F(ip,6)
   for iu in range(5):
    u=ul+(uh-ul)*F(iu,4);a=k+u-n*p;D=n*p*(1-p)+lam
    lower=m.normal(a,D);P=evaluate(poly,p,u);m.need(P<=lower,'Taylor polynomial below separately evaluated rigorous CDF lower bound');checks+=1
    expansion=f0+gp*(p-pc)+gu*(u-uc)-rem-((Mpp+eta*Mpt)*(p-pc)**2+(Muu+Mpt/eta)*(u-uc)**2)/2
    m.need(P==expansion,'independent centered polynomial expansion');expansions+=1
    Dprime=n*(1-2*p)
    # Multiply all derivatives by sqrt(D). Re-derive via the binomial
    # two-jet of (1+(Dprime/D)h-(n/D)h²)^(-1/2).
    zpp_jet=2*(a*(F(n,2)/D+F(3,8)*(Dprime/D)**2)+F(n,2)*Dprime/D)
    zpp_formula=n*(Dprime+a)/D+3*a*Dprime**2/(4*D**2)
    m.need(zpp_jet==zpp_formula,'independent inverse-square-root two-jet');jets+=1
  records.append({'lambda':str(lam),'gradient_p_width':str(F(rec['gradient_p'][1])-F(rec['gradient_p'][0])),'gradient_u_width':str(F(rec['gradient_u'][1])-F(rec['gradient_u'][0]))})
 invalid=[('negative variance',n,k,pl,pu,ul,uh,-F(1)),('wrong probability side',n,k,F(3,5),F(61,100),ul,uh,F(0)),('reversed phase',n,k,pl,pu,uh,ul,F(0)),('degenerate probability',n,k,pl,pl,ul,uh,F(0))];rejected=[]
 for name,*args in invalid:
  try:b.gaussian(*args)
  except ValueError:rejected.append(name)
  else:raise ValueError('invalid scalar domain admitted')
 r={'status':'PASS_BOUNDED_GAUSSIAN_TAYLOR_CONTROLS','rigorous_gaussian_grid_enclosures':checks,'independent_centered_polynomial_identities':expansions,'inverse_sqrt_twojet_identities':jets,'invalid_domains_rejected':rejected,'vertices':records,'source_sha256':m.sha(__file__),'scope':'These are implementation controls; analytic Hessian bounds and exact full-cell Bernstein verification prove the continuous result.'}
 (out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
if __name__=='__main__':main()

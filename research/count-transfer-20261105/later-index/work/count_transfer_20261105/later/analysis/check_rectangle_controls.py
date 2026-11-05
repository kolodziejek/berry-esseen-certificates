"""Independent polynomial identities, canonical objects and endpoint obstruction."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,sys,copy
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import check_tangent_rectangle as r
import strict_object
def value(a,x):
 z=F(0)
 for c in reversed(a):z=z*x+c
 return z
def inverse(b):
 d=len(b)-1;out=[F(0)]*(d+1)
 for j,bj in enumerate(b):
  for k in range(j,d+1):out[k]+=bj*comb(d,j)*comb(d-j,k-j)*(-1)**(k-j)
 return out
def main():
 need=r.m.need;need(__debug__ and not sys.flags.optimize,'ordinary Python');out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
 obj=strict_object.read(HERE/'N39_TANGENT_CANDIDATE.json');c=r.m.context(39,True);qs=[list(map(F,z))for z in obj['q']];theta=F(obj['theta']);pl=F(3849,10000);pu=pl+F(1,20000);ul=-F(1,1000);uh=-ul
 W=pu*(1-pu)+c['L']/39;coef=r.m.norm.CE_LO/(2*r.m.norm.root(F(39))[1]*W*W*r.m.norm.root(W)[1]);g0=-c['A0'];g1=c['A1'];a,b,d=r.hessian_polynomials(qs,c,coef,theta,g0,g1);det=r.add(r.mul(a,d),r.scale(r.mul(b,b),-F(1)))
 identities=0
 for poly,degree in[(a,41),(d,41),(det,82)]:
  beta=r.bern(poly,pl,pu,degree);local=[sum(poly[j]*comb(j,i)*pl**(j-i)*(pu-pl)**i for j in range(i,len(poly)))for i in range(degree+1)]
  need(inverse(beta)==local,'independent Bernstein inverse exact polynomial identity');identities+=degree+1
 checks=0
 for x,y in r.polygon(c,pl,pu):
  polynomial=r.mixture(qs,x,y,g0,g1)
  for p in[pl,(pl+pu)/2,pu]:
   q=1-p;v=p*q
   for u in[ul,F(0),uh]:
    direct=F(0)
    for j,quartic in enumerate(qs):
     s0=x/q;s1=y/p;t=(39-j)*s0+j*s1;mom=[F(1),F(0),t,(39-j)*g0*s0+j*g1*s1,(39-j)*g0*g0*s0+j*g1*g1*s1+F(38,13)*t*t]
     expectation=sum(quartic[k]*sum(F(comb(k,i))*(j-15-u)**(k-i)*mom[i]for i in range(k+1))for k in range(5))
     direct+=F(comb(39,j))*p**j*q**(39-j)*expectation
    need(v*v*direct==sum(value(polynomial[h],p)*u**h for h in range(5)),'independently computed translated full mixture');checks+=1
 # Canonical-data controls reject before any expensive arithmetic.
 bads=[]
 for name,badvalue in [('boolean',True),('integer',1),('float',0.5),('noncanonical integer','1/1'),('noncanonical zero','-0'),('zero denominator','1/0')]:
  z=copy.deepcopy(obj);z['q'][0][0]=badvalue;bads.append((name,z))
 z=copy.deepcopy(obj);z['theta']=False;bads.append(('boolean blend',z))
 z=copy.deepcopy(obj);z['q']=z['q'][:-1];bads.append(('missing count',z))
 z=copy.deepcopy(obj);z['extra']='ignored';bads.append(('extra object field',z))
 rejected=[]
 for name,z in bads:
  try:strict_object.validate(z)
  except ValueError:rejected.append(name)
  else:raise ValueError('ambiguous object admitted '+name)
 duplicate=out/'duplicate.json';duplicate.write_text('{"q":[],"q":[],"theta":"0"}')
 try:strict_object.read(duplicate)
 except ValueError:rejected.append('duplicate key')
 else:raise ValueError('duplicate object admitted')
 # Exact no-go for the UNSPLIT endpoint lower-Gaussian gate only.
 plo=F(3849,10000);phi=F(3851,10000);v=plo*(1-plo);V=phi*(1-phi);W=V+F(37,200*39)
 cc=r.m.norm.CE_LO/(2*r.m.norm.root(F(39))[1]*W*W*r.m.norm.root(W)[1]);floor=r.m.norm.CE_LO/r.m.norm.root(F(39))[1]
 gaussian=r.m.normal(F(15)+ul-39*phi,39*V);cdf=sum(F(comb(39,j))*plo**j*(1-plo)**(39-j)for j in range(16));difference=gaussian+max(floor,cc*v*(1-2*v)*(5*W-3*v))-cdf;need(difference<0,'unsplit endpoint-enclosure obstruction')
 result={'status':'PASS_RECTANGLE_POLYNOMIAL_AND_CANONICAL_CONTROLS','inverse_polynomial_coefficients':identities,'independent_translated_mixture_identities':checks,'rejected_mutations':rejected,'unsplit_target_minus_zero_noise_cdf':str(difference),'obstruction_scope':'Only the unsplit constant p_hi/u_lo Gaussian gate; the four-strip continuous check is separate.','source_sha256':r.m.sha(__file__)}
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()

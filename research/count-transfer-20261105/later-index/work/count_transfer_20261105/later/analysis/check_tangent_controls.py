"""Independent finite-difference Hessian audit and bounded malformed objects."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import product
import json,sys,copy
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import tangent_pilot as t
def main():
 t.m.need(__debug__ and not sys.flags.optimize,'ordinary Python');out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
 c=t.m.context(39,True);obj=json.loads((HERE/'N39_TANGENT_CANDIDATE.json').read_text());baseline=t.check(c,obj)
 n,p,q,v,k=(c[z]for z in('n','p','q','v','k'));W=v+c['L']/n;coef=t.m.norm.CE_LO/(2*t.m.norm.root(F(n))[1]*W*W*t.m.norm.root(W)[1]);theta=F(obj['theta']);qs=[list(map(F,z))for z in obj['q']]
 def direct(x,y,g0,g1):
  value=F(0)
  for j,quartic in enumerate(qs):
   s0=x/q;s1=y/p;variance=(n-j)*s0+j*s1
   moments=[F(1),F(0),variance,(n-j)*g0*s0+j*g1*s1,(n-j)*g0*g0*s0+j*g1*g1*s1+3*F(n-1,n)*variance**2]
   translated=[sum(F(comb(d,i))*F(j-k)**(d-i)*moments[i]for i in range(d+1))for d in range(5)]
   value+=F(comb(n,j))*p**j*q**(n-j)*sum(a*b for a,b in zip(quartic,translated))
  raw=v*(1-2*v)+3*p*x+3*q*y-g0*x+g1*y
  return value-theta*coef*raw*(5*W-3*(v+x+y))
 identities=0
 for g0,g1 in product((-c['A0'],F(0),c['a0']),(c['A1'],F(0),-c['a1'])):
  f00=direct(F(0),F(0),g0,g1);f10=direct(F(1),F(0),g0,g1);f01=direct(F(0),F(1),g0,g1)
  actual=(f10+direct(-F(1),F(0),g0,g1)-2*f00,direct(F(1),F(1),g0,g1)-f10-f01+f00,f01+direct(F(0),-F(1),g0,g1)-2*f00)
  t.m.need(actual==t.hessian(c,qs,theta,g0,g1),'independently expanded Hessian');identities+=3
 # The tangent-price quadratic by itself is not convex when r0 != r1.
 r0=3*p+c['A0'];r1=3*q+c['A1'];det=(2*r0)*(2*r1)-(r0+r1)**2
 t.m.need(det==-(r0-r1)**2<0,'PSD gate is a genuine extra obligation')
 rejected=[]
 bads=[]
 z=copy.deepcopy(obj);z['q']=z['q'][:-1];bads.append(('missing mixture count',z))
 z=copy.deepcopy(obj);z['theta']='2';bads.append(('price above convex blend',z))
 z=copy.deepcopy(obj);z['q'][15][0]='-1';bads.append(('closed atom corrupted',z))
 z=copy.deepcopy(obj);z['q'][3][4]='0';bads.append(('fourth coefficient zero',z))
 for name,z in bads:
  try:t.check(c,z)
  except ValueError:rejected.append(name)
  else:raise ValueError('corruption admitted '+name)
 r={'status':'PASS_TANGENT_HESSIAN_IDENTITIES_AND_CONTROLS','exact_hessian_entry_identities':identities,'bad_objects_rejected':rejected,'bare_price_hessian_determinant':str(det),'positive_baseline_cdf_margin':baseline['cdf_margin'],'source_sha256':t.m.sha(__file__)}
 (out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
if __name__=='__main__':main()

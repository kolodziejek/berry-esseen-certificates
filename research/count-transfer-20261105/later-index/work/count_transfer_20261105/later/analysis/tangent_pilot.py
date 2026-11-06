"""Additive sharp39 fixed-point tangent-price experiment; no row campaign."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb
import json,sys,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import pilot as m
def data(c):
 n,p,q,v,k=(c[z]for z in('n','p','q','v','k'));W=v+c['L']/n
 coefficient=m.norm.CE_LO/(2*m.norm.root(F(n))[1]*W*W*m.norm.root(W)[1]);floor=m.norm.CE_LO*c['rho']/m.norm.root(F(n))[1]
 base,_=m.expressions(c);rows=[];i=0
 for x,y in c['vertices']:
  for g0,g1 in product((-c['A0'],F(0),c['a0']),(c['A1'],F(0),-c['a1'])):
   raw=v*(1-2*v)+3*p*x+3*q*y-g0*x+g1*y
   target=m.normal(F(k)-n*p,n*(v+x+y))+floor
   rows.append((base[i][0],target,coefficient*raw*(5*W-3*(v+x+y))-floor));i+=1
 return rows,coefficient
def hessian(c,qs,theta,g0,g1):
 n,p,q=(c[z]for z in('n','p','q'));_,cc=data(c)
 h00=h01=h11=F(0)
 for j,row in enumerate(qs):
  scale=6*F(n-1,n)*F(comb(n,j))*p**j*q**(n-j)*F(row[4]);a=F(n-j)/q;b=F(j)/p
  h00+=scale*a*a;h01+=scale*a*b;h11+=scale*b*b
 r0=3*p-g0;r1=3*q+g1
 return h00+6*cc*theta*r0,h01+3*cc*theta*(r0+r1),h11+6*cc*theta*r1
def check(c,obj):
 qs=obj['q'];theta=F(obj['theta']);m.need(len(qs)==40 and 0<=theta<=1,'fixed39 complete majorants')
 flat=[]
 for q in qs:
  m.need(len(q)==5,'five coefficients');q=list(map(F,q));m.need(q[4]>0,'positive leading coefficient')
  m.sturm.positive(m.compact(q,-1,F(1)));m.sturm.positive(m.compact(q,1,F(0)));flat+=q
 determinants=[]
 for g0,g1 in product((-c['A0'],F(0),c['a0']),(c['A1'],F(0),-c['a1'])):
  a,b,d=hessian(c,qs,theta,g0,g1);m.need(a>=0 and d>=0 and a*d-b*b>=0,'exact positive semidefinite quadratic objective');determinants.append(str(a*d-b*b))
 rows,cc=data(c);margin=min(t+theta*diff-sum(a*b for a,b in zip(row,flat))for row,t,diff in rows);m.need(margin>0,'strict scalar objective')
 return {'status':'PASS_EXACT_FIXED_POINT_TANGENT_AND_PSD','n':39,'p':'77/200','k':15,'u':'0','noise':['0',str(c['L'])],'resource_facets':c['resource'],'cdf_margin':str(margin),'price_coefficient':str(cc),'hessian_determinants':determinants,'vertices':len(c['vertices']),'global_rays':80,'full_row':False}
def main():
 import numpy as np
 from scipy.optimize import linprog
 out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False);c=m.context(39,True);rows,cc=data(c);n=39;dim=202;lhs=[];rhs=[]
 for row,t,d in rows:lhs.append(list(map(float,row))+[-float(d),1.]);rhs.append(float(t))
 for j in range(40):
  for sign,sub in [(-1,F(1)),(1,F(0))]:
   targets=[m.compact([F(int(a==b))for a in range(5)],sign,F(0))for b in range(5)];const=m.compact([sub,F(0),F(0),F(0),F(0)],sign,F(0))
   for cell in range(32):
    basis=[m.bern(t,F(cell,32),F(cell+1,32))for t in targets];bc=m.bern(const,F(cell,32),F(cell+1,32))
    for i in range(5):
     z=[0.]*dim
     for d in range(5):z[5*j+d]=-float(basis[d][i])
     lhs.append(z);rhs.append(-float(bc[i])-1e-9)
 p,q=c['p'],c['q'];dirs=[(F(1),F(0)),(F(0),F(1))]+[(F(i,16),F(1))for i in range(-64,65)]
 for g0,g1 in product((-c['A0'],F(0),c['a0']),(c['A1'],F(0),-c['a1'])):
  r0=3*p-g0;r1=3*q+g1
  for dx,dy in dirs:
   z=[0.]*dim
   for j in range(40):z[5*j+4]=-float(6*F(n-1,n)*F(comb(n,j))*p**j*q**(n-j)*(dx*F(n-j)/q+dy*F(j)/p)**2)
   z[-2]=-float(6*cc*(r0*dx*dx+(r0+r1)*dx*dy+r1*dy*dy));lhs.append(z);rhs.append(-1e-9)
 sol=linprog([0.]*201+[-1.],A_ub=np.array(lhs),b_ub=np.array(rhs),bounds=[(-500,500)if d%5<4 else(1e-8,500)for d in range(200)]+[(0,1),(-100,100)],method='highs',options={'time_limit':90,'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
 diag={'status':'FLOATING_DISCOVERY_ONLY','success':bool(sol.success),'message':sol.message}
 if sol.success:
  qs=[]
  for j in range(40):
   z=[F(round(a*10**10),10**10)for a in sol.x[5*j:5*j+5]];z[0]+=F(1,10**6);z[4]+=F(1,10**7);qs.append(list(map(str,z)))
  obj={'q':qs,'theta':str(F(round(sol.x[-2]*10**10),10**10))};(out/'candidate.json').write_text(json.dumps(obj,indent=2)+'\n');diag['floating_margin']=float(sol.x[-1])
  try:diag.update(check(c,obj))
  except ValueError as e:diag['rejection']=str(e)
 diag.update(source_sha256=m.sha(__file__),base_source_sha256=m.sha(m.__file__),scope='Only fixed sharp39 source row p77/200,k15,u0. No p/u cover; no original acquisition rerun.')
 (out/'RESULT.json').write_text(json.dumps(diag,indent=2)+'\n');print(json.dumps(diag))
if __name__=='__main__':main()

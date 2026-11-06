"""Bounded fixed-p/phase general-n discovery and exact scalar readback.

Never a complete original row. Four source-bound relaxations only.
Discovery uses scipy; check() uses Fraction plus the pinned native readers.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from math import comb
import hashlib,json,sys,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'native'))
import quartic_sturm as sturm
import finite_binomial_core as norm
def need(v,m):
 if not v:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
for name,pin in json.loads((HERE/'native/PINS.json').read_text()).items():need(sha(HERE/'native'/name)==pin['sha256'],'native bytes')
def compact(q,sign,sub):
 q=list(q);q[0]-=sub;r=[F(0)]*5
 for j,a in enumerate(q):
  for h in range(5-j):r[j+h]+=a*sign**j*comb(4-j,h)*(-1)**h
 return r
def normal(num,den):
 l,h=norm.root(den)
 if num>=0:
  z=num/h;i=z.numerator*norm.Z//z.denominator
  need(i<=5*norm.Z,'normal range');return F(norm.positive_cdf(i)[0],norm.S)
 z=-num/l;i=-((-z.numerator*norm.Z)//z.denominator)
 need(i<=5*norm.Z,'normal range');return 1-F(norm.positive_cdf(i)[1],norm.S)
def source(n):
 key='n6.BN.p38'if n==6 else'n39.strict.dce5d64054154a1a'
 path=HERE.parent/'selected'/key/'contract.json';obj=json.loads(path.read_text())
 rows=[r for r in obj['rows']if r['index']==38];need(len(rows)==1,'unique source row')
 r=rows[0];need(r['n']==n and F(r.get('K',obj.get('K','-1')))==0,'actual sharp index/target')
 return r,path
def context(n,resource):
 r,path=source(n);p=F(77,200);q=1-p;v=p*q;k=2 if n==6 else 15;u=F(0)
 L=F(r.get('acquired_lambda_upper',r['Lambda']));A0=F(r['outer0']);A1=F(r['outer1'])
 d=F(r.get('acquired_inward_upper',r['d0']));a0=min(d,p);a1=min(d,q)
 if 'sign_premise'in r:
  s=norm.root(v)[0];a0=min(a0,p-F(r['sign_premise']['negative_endpoint_lower'])*s)
  a1=min(a1,q-F(r['sign_premise']['positive_endpoint_lower'])*s)
 if 'acquired_mean'in r:L=min(L,n*(v*v/F(r['acquired_mean'][0])**2-v))
 planes=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),L/n)]
 if 'acquired_beta'in r:
  bl,bu=map(F,r['acquired_beta']);planes += [(-(1+bu),1-bu,v*(bu-1+2*p)),(1+bl,-(1-bl),v*(1-2*p-bl))]
 if resource:
  d0=F(r['d0']);lam=F(r['Lambda']);g=F(r['gap_charge']);h=F(r['noise_charge'])
  planes += [(1/(q*A0)+n*d0/lam,1/(p*A1)+n*d0/lam,d0),(g/(q*A0)+n*h,g/(p*A1)+n*h,F(r['D'])-F(r['binary_charge']))]
 vertices=set()
 for(a,b,c),(d0,e,f)in combinations(planes,2):
  det=a*e-b*d0
  if det:
   x=(c*e-b*f)/det;y=(a*f-c*d0)/det
   if all(A*x+B*y<=C for A,B,C in planes):vertices.add((x,y))
 need(len(vertices)>=3,'nonempty polygon')
 return dict(n=n,p=p,q=q,v=v,k=k,u=u,L=L,A0=A0,A1=A1,a0=a0,a1=a1,vertices=sorted(vertices),
  rho=F(r.get('rho_lower','1')),resource=resource,contract=str(path),contract_sha256=sha(path),row=r,planes=planes)
def expressions(c):
 n,p,q,v,k,u=(c[z]for z in('n','p','q','v','k','u'));amin=F(k)+u-n*p
 correlated=amin<=0 and amin*amin<=3*n*v
 wmax=v+c['L']/n;coef=norm.CE_LO/(norm.root(F(n))[1]*wmax*norm.root(wmax)[1]);floor=norm.CE_LO*c['rho']/norm.root(F(n))[1]
 rows=[]
 for x,y in c['vertices']:
  for g0,g1 in product((-c['A0'],F(0),c['a0']),(c['A1'],F(0),-c['a1'])):
   coeff=[]
   for j in range(n+1):
    t=(n-j)*x/q+j*y/p;s3=(n-j)*g0*x/q+j*g1*y/p
    s4=(n-j)*g0*g0*x/q+j*g1*g1*y/p+3*F(n-1,n)*t*t
    moments=[F(1),F(0),t,s3,s4];shift=F(j-k)-u;b=comb(n,j)*p**j*q**(n-j)
    coeff += [b*sum(F(comb(d,i))*shift**(d-i)*moments[i]for i in range(d+1))for d in range(5)]
   lam=n*(x+y);den=n*v+lam if correlated else n*v+(F(0)if amin<0 else c['L'])
   raw=v*(1-2*v)+3*p*x+3*q*y-g0*x+g1*y
   rows.append((coeff,normal(amin,den)+floor,coef*raw-floor))
 return rows,correlated
def check(c,qs,theta):
 n=c['n'];need(len(qs)==n+1,'all ordered mixture counts');theta=F(theta);need(0<=theta<=1,'convex cube price')
 exact=[]
 for q in qs:
  need(len(q)==5,'five coefficients');q=list(map(F,q));need(q[4]>0,'positive leading coefficient')
  sturm.positive(compact(q,-1,F(1)));sturm.positive(compact(q,1,F(0)));exact+=q
 rows,correlated=expressions(c);m=min(t+theta*d-sum(a*b for a,b in zip(row,exact))for row,t,d in rows)
 need(m>0,'positive exact CDF reserve')
 return dict(status='PASS_EXACT_FIXED_P_PHASE_FULL_NOISE_RELAXATION',n=n,p=str(c['p']),k=c['k'],u=str(c['u']),
  noise=['0',str(c['L'])],resource_facets=c['resource'],vertices=len(c['vertices']),shared_moment_corners=9,
  exact_cdf_margin=str(m),global_rays=2*(n+1),correlated_normal=correlated,contract_sha256=c['contract_sha256'],
  complete_original_row=False,acquisition_rerun=False)
def bern(a,l,h):
 loc=[sum(a[j]*comb(j,i)*l**(j-i)*(h-l)**i for j in range(i,len(a)))for i in range(5)]
 return [sum(loc[j]*F(comb(i,j),comb(4,j))for j in range(i+1))for i in range(5)]
def discover(c):
 import numpy as np
 from scipy.optimize import linprog
 n=c['n'];dim=5*(n+1)+2;lhs=[];rhs=[]
 rows,_=expressions(c)
 for row,t,d in rows:lhs.append(list(map(float,row))+[-float(d),1.]);rhs.append(float(t))
 for j in range(n+1):
  for sign,sub in[(-1,F(1)),(1,F(0))]:
   targets=[compact([F(int(a==b))for a in range(5)],sign,F(0))for b in range(5)]
   const=compact([sub,F(0),F(0),F(0),F(0)],sign,F(0))
   for cell in range(32):
    basis=[bern(t,F(cell,32),F(cell+1,32))for t in targets];cc=bern(const,F(cell,32),F(cell+1,32))
    for b in range(5):
     z=[0.]*dim
     for d in range(5):z[5*j+d]=-float(basis[d][b])
     lhs.append(z);rhs.append(-float(cc[b])-1e-9)
 sol=linprog([0.]*(dim-1)+[-1.],A_ub=np.array(lhs),b_ub=np.array(rhs),bounds=[(-500,500)if d%5<4 else(1e-8,500)for d in range(dim-2)]+[(0,1),(-100,100)],method='highs',options={'time_limit':90,'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
 if not sol.success:return dict(status='FLOATING_LP_FAILED',message=sol.message),None
 qs=[]
 for j in range(n+1):
  z=[F(round(a*10**10),10**10)for a in sol.x[5*j:5*j+5]];z[0]+=F(1,10**6);z[4]+=F(1,10**7);qs.append(list(map(str,z)))
 theta=str(F(round(sol.x[-2]*10**10),10**10));obj=dict(q=qs,theta=theta)
 diagnostic=dict(status='FLOATING_DISCOVERY_ONLY',margin=float(sol.x[-1]),theta=theta)
 if sol.x[-1]>1e-5:
  try:diagnostic=check(c,qs,theta);diagnostic['floating_margin']=float(sol.x[-1])
  except ValueError as e:diagnostic.update(status='RATIONAL_CANDIDATE_REJECTED',reason=str(e))
 return diagnostic,obj
def main():
 need(__debug__ and not sys.flags.optimize,'ordinary Python');out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
 results=[]
 for n,resource in [(6,False),(6,True),(39,False),(39,True)]:
  c=context(n,resource);t=time.monotonic();r,obj=discover(c);r.update(n=n,resource_facets=resource,seconds=time.monotonic()-t)
  name=f'n{n}-resource{int(resource)}';(out/(name+'.json')).write_text(json.dumps({'result':r,'candidate':obj},indent=2)+'\n');results.append(r);print(json.dumps(r),flush=True)
 (out/'RESULT.json').write_text(json.dumps({'scope':'Four bounded fixed-probability/fixed-phase tests, not complete row acceptance.','results':results,'source_sha256':sha(__file__)},indent=2)+'\n')
if __name__=='__main__':main()

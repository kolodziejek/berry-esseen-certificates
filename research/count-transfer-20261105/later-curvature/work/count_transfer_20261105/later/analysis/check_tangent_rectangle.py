"""Bounded exact four-strip extension of the unchanged sharp39 quartics.

Every tensor and Hessian minor is constructed from the source-bound model.
No numerical discovery and no old PASS are accepted as mathematical input.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import product,combinations
import sys,json,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import tangent_pilot as t
m=t.m
def add(a,b):return [(a[i]if i<len(a)else F(0))+(b[i]if i<len(b)else F(0))for i in range(max(len(a),len(b)))]
def scale(a,c):return [v*c for v in a]
def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
def power(a,n):
 z=[F(1)]
 for _ in range(n):z=mul(z,a)
 return z
def bern(a,l,h,d):
 m.need(len(a)<=d+1 and l<h,'degree/order')
 local=[sum(a[j]*comb(j,i)*l**(j-i)*(h-l)**i for j in range(i,len(a)))for i in range(d+1)]
 return [sum(local[j]*F(comb(i,j),comb(d,j))for j in range(i+1))for i in range(d+1)]
P=[F(0),F(1)];Q=[F(1),-F(1)];V=mul(P,Q);V2=mul(V,V);N=39;K=15
MASSES=[scale(mul(power(P,j),power(Q,N-j)),F(comb(N,j)))for j in range(N+1)]
def polygon(c,pl,pu):
 r=c['row'];A0=c['A0'];A1=c['A1'];d=F(r['d0']);lam=F(r['Lambda']);g=F(r['gap_charge']);h=F(r['noise_charge'])
 planes=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),lam/N),
  (1/((1-pl)*A0)+N*d/lam,1/(pu*A1)+N*d/lam,d),
  (g/((1-pl)*A0)+N*h,g/(pu*A1)+N*h,F(r['D'])-F(r['binary_charge']))]
 out=set()
 for(a,b,z),(d0,e,f)in combinations(planes,2):
  den=a*e-b*d0
  if den:
   x=(z*e-b*f)/den;y=(a*f-z*d0)/den
   if all(A*x+B*y<=C for A,B,C in planes):out.add((x,y))
 m.need(len(out)>=3 and (F(0),F(0))in out,'complete nonempty variance polygon');return sorted(out)
def hessian_polynomials(qs,c,coef,theta,g0,g1):
 a=b=d=[F(0)]
 for j,qj in enumerate(qs):
  factor=6*F(N-1,N)*qj[4];base=scale(MASSES[j],factor)
  a=add(a,scale(mul(base,mul(P,P)),F((N-j)**2)))
  b=add(b,scale(mul(base,V),F(j*(N-j))))
  d=add(d,scale(mul(base,mul(Q,Q)),F(j*j)))
 r0=add(scale(P,3),[-g0]);r1=add(scale(Q,3),[g1])
 a=add(a,scale(mul(V2,r0),6*coef*theta));b=add(b,scale(mul(V2,add(r0,r1)),3*coef*theta));d=add(d,scale(mul(V2,r1),6*coef*theta))
 return a,b,d
def mixture(qs,x,y,g0,g1):
 out=[[F(0)]for _ in range(5)]
 for j,qj in enumerate(qs):
  aa=(N-j)*x;bb=j*y;tv=add(scale(P,aa),scale(Q,bb));base0=mul(mul(P,P),Q);base1=mul(P,mul(Q,Q))
  moments=[V2,[F(0)],add(scale(base0,aa),scale(base1,bb)),add(scale(base0,aa*g0),scale(base1,bb*g1)),
   add(add(scale(base0,aa*g0*g0),scale(base1,bb*g1*g1)),scale(mul(tv,tv),3*F(N-1,N)))]
  for order in range(5):
   for i in range(order+1):
    base=scale(mul(MASSES[j],moments[i]),qj[order]*comb(order,i))
    for h in range(order-i+1):out[h]=add(out[h],scale(base,F(comb(order-i,h))*F(j-K)**(order-i-h)*(-1)**h))
 return out
def check_cell(c,qs,theta,pl,pu,ul,uh):
 m.need(F(19,50)<=pl<pu<=F(39,100) and -F(1,2)<=ul<uh<=F(1,2),'original row subcell')
 m.need(F(K)+ul>=0 and F(K)+uh<=N,'Gaussian endpoint monotonicity')
 amin=F(K)+ul-N*pu;amax=F(K)+uh-N*pl;vmin=pl*(1-pl);vmax=pu*(1-pu)
 m.need(amax<=0 and amin*amin<=3*N*vmin,'whole negative Gaussian curvature')
 W=vmax+c['L']/N;coef=m.norm.CE_LO/(2*m.norm.root(F(N))[1]*W*W*m.norm.root(W)[1]);floor=m.norm.CE_LO/m.norm.root(F(N))[1]
 corners=list(product((-c['A0'],F(0),c['a0']),(c['A1'],F(0),-c['a1'])));vertices=polygon(c,pl,pu);psdmins=[]
 for g0,g1 in corners:
  a,b,d=hessian_polynomials(qs,c,coef,theta,g0,g1);det=add(mul(a,d),scale(mul(b,b),-F(1)))
  mins=[min(bern(a,pl,pu,41)),min(bern(d,pl,pu,41)),min(bern(det,pl,pu,82))]
  m.need(min(mins)>=0,'whole-p PSD principal minors');psdmins.append(list(map(str,mins)))
 margin=None
 for x,y in vertices:
  gaussian=m.normal(amin,N*vmax+N*(x+y))
  for g0,g1 in corners:
   expect=mixture(qs,x,y,g0,g1)
   raw=add(mul(V,add([F(1)],scale(V,-2))),add(add(scale(P,3*x),scale(Q,3*y)),[-g0*x+g1*y]))
   tangent=scale(mul(V2,mul(raw,add([5*W-3*(x+y)],scale(V,-3)))),theta*coef)
   target=add(scale(V2,gaussian+(1-theta)*floor),tangent)
   loss=[add(target,scale(expect[0],-1))]+[scale(a,-1)for a in expect[1:]]
   bp=[bern(a,pl,pu,43)for a in loss]
   for i in range(44):
    row=bern([bp[h][i]for h in range(5)],ul,uh,4);z=min(row)
    m.need(z>0,'whole closed probability/phase score tensor');margin=z if margin is None else min(margin,z)
 return dict(p=list(map(str,(pl,pu))),u=list(map(str,(ul,uh))),variance_vertices=len(vertices),tensor_coefficients=44*5*len(vertices)*9,
  psd_polynomial_coefficients=9*(42+42+83),cleared_score_margin=str(margin),psd_minima=psdmins)
def main():
 m.need(__debug__ and not sys.flags.optimize,'ordinary Python');out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False);started=time.monotonic()
 c=m.context(39,True);obj=json.loads((HERE/'N39_TANGENT_CANDIDATE.json').read_text());qs=[list(map(F,z))for z in obj['q']];theta=F(obj['theta']);m.need(len(qs)==40 and 0<=theta<=1,'all original40 polynomials')
 for q in qs:m.need(q[4]>0,'quartic leading');m.sturm.positive(m.compact(q,-1,F(1)));m.sturm.positive(m.compact(q,1,F(0)))
 pl=F(3849,10000);pu=F(3851,10000);ul=-F(1,1000);uh=F(1,1000);cells=[]
 for j in range(4):
  l=pl+(pu-pl)*F(j,4);h=pl+(pu-pl)*F(j+1,4)
  try:r=check_cell(c,qs,theta,l,h,ul,uh)
  except ValueError as e:
   (out/'FAILED.json').write_text(json.dumps({'failed_cell':j,'reason':str(e),'completed':cells},indent=2)+'\n');raise
  cells.append(r);print(json.dumps({'cell':j,'cleared_margin':r['cleared_score_margin'],'seconds':time.monotonic()-started}),flush=True)
 result={'status':'PASS_EXACT_SMALL_CONTINUOUS_SHARP39_RECTANGLE','n':39,'k':15,'p':[str(pl),str(pu)],'u':[str(ul),str(uh)],'noise':['0','37/200'],'closed_p_strips':4,'global_rays':80,'cells':cells,'full_original_row':False,'source_sha256':m.sha(__file__),'candidate_sha256':m.sha(HERE/'N39_TANGENT_CANDIDATE.json')}
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'seconds':time.monotonic()-started}))
if __name__=='__main__':main()

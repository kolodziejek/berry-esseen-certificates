"""One broad negative-phase p rectangle; unchanged quartics, exact Gaussian Taylor."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from itertools import product
import sys,json,time
HERE=Path(__file__).resolve().parent;BASE=HERE.parent/'analysis';sys.path.insert(0,str(BASE))
import check_tangent_rectangle as r
import strict_object
m=r.m
def down(x,g=10**20):return F(x.numerator*g//x.denominator,g)
def up(x,g=10**20):return -down(-x,g)
def interval_mul(a,b):
 xs=[x*y for x in a for y in b];return min(xs),max(xs)
def gaussian(n,k,pl,pu,ul,uh,lam):
 """Power coefficients in p,u of a certified quadratic lower polynomial."""
 m.need(0<pl<pu<F(1,2) and ul<uh and lam>=0,'explicit closed Gaussian domain')
 pc=(pl+pu)/2;uc=(ul+uh)/2;dp=(pu-pl)/2;du=(uh-ul)/2
 a0=F(k)+uc-n*pc;D0=n*pc*(1-pc)+lam;rp=m.norm.root(D0)
 # phi(z0)=phi(0)*exp(-a0²/(2D0)); an alternating enclosure with x<=1.
 x=a0*a0/(2*D0);m.need(0<=x<=1,'alternating exponential domain')
 even=sum((-x)**j/F(factorial(j))for j in range(25));odd=even+(-x)**25/F(factorial(25))
 m.need(0<odd<=even<=1,'positive exact exponential enclosure')
 phi=(down(m.norm.PHI_LO*odd),up(m.norm.PHI_HI*even));inv=(1/rp[1],1/rp[0])
 Dprime=n*(1-2*pc);zp=interval_mul(inv,(-n-a0*Dprime/(2*D0),)*2)
 gp=interval_mul(phi,zp);gt=interval_mul(phi,inv);gp=(down(gp[0]),up(gp[1]));gt=(down(gt[0]),up(gt[1]))
 gp0=sum(gp)/2;gt0=sum(gt)/2;rounding=(gp[1]-gp[0])*dp/2+(gt[1]-gt[0])*du/2
 dmin=n*pl*(1-pl)+lam;smin=m.norm.root(dmin)[0];m.need(smin>0,'positive variance denominator')
 A=max(abs(F(k)+u-n*p)for p in(pl,pu)for u in(ul,uh));B=n*max(abs(1-2*pl),abs(1-2*pu))
 Z=A/smin;Zt=1/smin;Zp=n/smin+A*B/(2*dmin*smin)
 Zpp=n*(B+A)/(dmin*smin)+3*A*B*B/(4*dmin*dmin*smin);Zpt=B/(2*dmin*smin)
 Mpp=up(F(2,5)*(Z*Zp*Zp+Zpp),10**16);Mpt=up(F(2,5)*(Z*Zp*Zt+Zpt),10**16);Mtt=up(F(2,5)*Z*Zt*Zt,10**16)
 eta=du/dp;P=Mpp+Mpt*eta;T=Mtt+Mpt/eta;center=m.normal(a0,D0)
 # center+gp0(p-pc)+gt0(u-uc)-rounding-P(p-pc)^2/2-T(u-uc)^2/2.
 poly=[[center-gp0*pc-gt0*uc-rounding-P*pc*pc/2-T*uc*uc/2,gp0+P*pc,-P/2],[gt0+T*uc],[-T/2]]
 record={'lambda':str(lam),'center':[str(pc),str(uc)],'center_cdf_lower':str(center),'phi_interval':list(map(str,phi)),'gradient_p':list(map(str,gp)),'gradient_u':list(map(str,gt)),
  'rounding_budget':str(rounding),'absolute_hessian_bounds':list(map(str,(Mpp,Mpt,Mtt))),'eta':str(eta),'polynomial':[[str(z)for z in a]for a in poly]}
 return poly,record
def check(obj,pl,pu,ul,uh):
 c=m.context(39,True);qs=[list(map(F,z))for z in obj['q']];theta=F(obj['theta']);N=39;K=15
 m.need(F(19,50)<=pl<pu<=F(39,100) and -F(1,2)<=ul<uh<=F(1,2),'original sharp row')
 m.need(c['a0']<=pl and c['a1']<=1-pu,'same fixed inward caps valid throughout')
 amin=K+ul-N*pu;amax=K+uh-N*pl;vmin=pl*(1-pl);vmax=pu*(1-pu)
 m.need(amax<=0 and amin*amin<=3*N*vmin,'actual Gaussian concavity in variance throughout')
 for q in qs:m.need(q[4]>0,'positive fourth coefficient');m.sturm.positive(m.compact(q,-1,F(1)));m.sturm.positive(m.compact(q,1,F(0)))
 W=vmax+c['L']/N;coef=m.norm.CE_LO/(2*m.norm.root(F(N))[1]*W*W*m.norm.root(W)[1]);floor=m.norm.CE_LO/m.norm.root(F(N))[1]
 corners=list(product((-c['A0'],F(0),c['a0']),(c['A1'],F(0),-c['a1'])));vertices=r.polygon(c,pl,pu);psd=[]
 for g0,g1 in corners:
  a,b,d=r.hessian_polynomials(qs,c,coef,theta,g0,g1);det=r.add(r.mul(a,d),r.scale(r.mul(b,b),-F(1)));mins=[min(r.bern(a,pl,pu,41)),min(r.bern(d,pl,pu,41)),min(r.bern(det,pl,pu,82))]
  m.need(min(mins)>=0,'whole-p exact PSD polynomials');psd.append(list(map(str,mins)))
 reserve=None;gaussians=[]
 for x,y in vertices:
  G,record=gaussian(N,K,pl,pu,ul,uh,N*(x+y));gaussians.append(record)
  for g0,g1 in corners:
   expect=r.mixture(qs,x,y,g0,g1);raw=r.add(r.mul(r.V,r.add([F(1)],r.scale(r.V,-2))),r.add(r.add(r.scale(r.P,3*x),r.scale(r.Q,3*y)),[-g0*x+g1*y]))
   tangent=r.scale(r.mul(r.V2,r.mul(raw,r.add([5*W-3*(x+y)],r.scale(r.V,-3)))),theta*coef)
   target=[r.mul(r.V2,g)for g in G]+[[F(0)],[F(0)]]
   target[0]=r.add(target[0],r.add(r.scale(r.V2,(1-theta)*floor),tangent))
   loss=[r.add(target[h],r.scale(expect[h],-1))for h in range(5)];bp=[r.bern(a,pl,pu,43)for a in loss]
   for i in range(44):
    z=min(r.bern([bp[h][i]for h in range(5)],ul,uh,4));reserve=z if reserve is None else min(reserve,z)
 m.need(reserve>0,'strict broad continuous score tensor')
 return dict(status='PASS_EXACT_BROAD_SHARP39_GAUSSIAN_TAYLOR_RECTANGLE',n=N,k=K,p=list(map(str,(pl,pu))),u=list(map(str,(ul,uh))),noise=['0','37/200'],
  variance_vertices=len(vertices),global_rays=80,score_coefficients=44*5*len(vertices)*9,psd_coefficients=9*167,cleared_margin=str(reserve),gaussian_enclosures=gaussians,psd_minima=psd,full_original_row=False)
def main():
 m.need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'ordinary Python NEW_OUTPUT');out=Path(sys.argv[1]);m.need(not out.exists(),'fresh output')
 pins=json.loads((HERE/'SOURCE_PINS.json').read_text())
 for name,h in pins.items():m.need(m.sha(HERE/name)==h,'all original sources unchanged')
 obj=strict_object.read(BASE/'N39_TANGENT_CANDIDATE.json');out.mkdir();started=time.monotonic()
 try:result=check(obj,F(3847,10000),F(39,100),-F(1,1000),F(1,1000))
 except ValueError as e:
  (out/'FAILED.json').write_text(json.dumps({'status':'BOUND_NOT_ESTABLISHED','reason':str(e),'scope':'One requested broad negative-p rectangle; original fixed coefficients/target retained.'},indent=2)+'\n');raise
 for name,h in pins.items():m.need(m.sha(HERE/name)==h,'stable complete source closure')
 result.update(source_sha256=pins,reader_sha256=m.sha(__file__),object_sha256=m.sha(BASE/'N39_TANGENT_CANDIDATE.json'),seconds=time.monotonic()-started)
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('source_sha256','gaussian_enclosures','psd_minima')}))
if __name__=='__main__':main()

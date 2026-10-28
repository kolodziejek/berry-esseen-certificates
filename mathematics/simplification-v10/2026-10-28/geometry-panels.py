"""One direct evaluation per entry panel; no iterative contraction/import."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
ROOT=Path(__file__).resolve().parents[3]
INPUT=ROOT/'mathematics/fixed-target-v8/2026-10-28/moment-entry-v8-input.json'
PIN='61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae'
SL,SU=F('3.162277660'),F('3.162277661');SCALE=10**12
T,DGLOBAL,R=F('.056'),F('.068'),F('3.14')
def lo(x):return F(x.numerator*SCALE//x.denominator,SCALE)
def hi(x):return -lo(-x)
def sqrtlo(x):
 assert x>=0
 y=F(isqrt(x.numerator*SCALE*SCALE//x.denominator),SCALE)
 assert y*y<=x<(y+F(1,SCALE))**2
 return y
def sqrtup(x):return sqrtlo(x)+F(1,SCALE)
def Q(p):return (2*SL+6)*p*p-(2*SL+4)*p+SL-1
def Qmin(l,u):
 a=(2*SL+4)/(2*(2*SL+6));ps=[l,u]
 if l<=a<=u:ps.append(a)
 return max(F(0),min(Q(p)for p in ps))
def heat(t,r,b):
 assert t*t>3
 S,c,e=F(81,80),F(819,2000),F(8,875)
 q=-t**3+F(3,2)*r*t*t+3*b*t+e*r
 q1=-3*t*t+3*r*t+3*b;q2=-6*t+3*r
 bound=F(2,5)*S**3*((t**3-3*t)/6+abs(t**4-6*t*t+3)/72)+S**3*(t**5/4100+3*t/820+17*(3*t*t-2)/78720)+c*q
 rays=[q,q1,q2,F(2,5)*(t*t/2+F(1,2)+e)+c*q1,F(2,5)*t+c*q2,F(2,5)-6*c]
 return dict(boundary=bound,rays=rays,passed=bound<0 and all(x<0 for x in rays))
def row(z):
 i=z['index'];l,u,Di=[F(z[k])for k in ('pl','pu','D')]
 vmin=min(l*(1-l),u*(1-u));vmax=max(l*(1-l),u*(1-u),F(1,4)if l<=F(1,2)<=u else F(0))
 qmin=Qmin(l,u);cmin=min(3*(SL+1)*(1-u),3*(SL+3)*l)
 ell0=sqrtlo((1-T)/vmax);assert cmin>qmin
 reserve=Di/ell0-qmin
 if i==24:return dict(index=i,excluded=True,reason='global strict p>1/4')
 if reserve<0:return dict(index=i,excluded=True,reason='direct binary charge',reserve=reserve)
 theta=min(T,hi(reserve/(cmin-qmin)));w=1-theta
 ell=sqrtlo(w/vmax);ellu=sqrtup(1/vmin);assert 0<=theta<T or theta==T
 J=Di/(ell*w)-qmin
 if J<0:return dict(index=i,excluded=True,reason='direct binary charge after single theta bound',reserve=J)
 assert 0<=J<F(3,2)
 d=min(DGLOBAL,hi((1-sqrtlo(1-F(2,3)*J))/2))
 A=lo(ell*(l-d));B=lo(ell*(1-u-d));assert A>0 and B>0
 abar=sqrtlo(w*l/(1-l));bbar=sqrtlo(w*(1-u)/u)
 au=sqrtup(u/(1-u));bu=sqrtup((1-l)/l)
 k=lo(min(SL-1+6*B/(R+2*bu),SL+1+6*A/(R+2*au)))
 L=R+2*max(au,bu);r=Di-ell*w*qmin;assert k>0 and r>=0
 rb=hi((1-2*vmin)/sqrtlo(vmin));decay=F(3,2)*sqrtlo(w)
 assert 1-decay*theta>0
 rho=min(F('1.426'),hi(rb+max(F(0),L-decay*rb)*min(theta,r/(k*L))))
 beta_l=lo(1-2*u-2*(1-u)*theta);beta_u=hi(1-2*l+2*l*theta)
 lam=hi(vmax/cmin*(42*Di/(ell*w)-42*qmin))
 zn=heat(ell*(l+F(3,5)),rho,-beta_l);zp=heat(ell*(1-u+F(3,5)),rho,beta_u)
 return dict(index=i,excluded=False,pl=l,pu=u,D=Di,qmin=qmin,cmin=cmin,theta=theta,d=d,ell_l=ell,ell_u=ellu,A=A,B=B,rho=rho,beta_l=beta_l,beta_u=beta_u,lambda_upper=lam,third_moment_price=k,strip_negative=zn,strip_positive=zp)
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encode(v)for k,v in x.items()}
 if isinstance(x,list):return [encode(v)for v in x]
 return x
blob=INPUT.read_bytes();assert hashlib.sha256(blob).hexdigest()==PIN
z=json.loads(blob);assert z['name']=='INITIAL42_FIXED_TARGET_COARSE_V7' and len(z['panels'])==100
active=[]
for i,x in enumerate(z['panels']):
 assert F(x['pl'])==F(i,100) and F(x['pu'])==F(i+1,100)
 if x['cells']:active.append(dict(index=i,**x))
assert [x['index']for x in active]==list(range(24,54))
assert max(F(x['D'])for x in active)<=F('.76682509')
assert max(F(x['radius'])for x in z['steps'][-1]if x.get('active',0)>0)==R
rows=[row(x)for x in active];kept=[x for x in rows if not x['excluded']]
assert [x['index']for x in kept]==list(range(25,53))
strips=[x['index']for x in kept if x['strip_negative']['passed'] and x['strip_positive']['passed']]
assert strips==list(range(40,53))
central=next(x for x in kept if x['index']==41)
for key,bound in [('theta','.054'),('d','.069'),('rho','1.22'),('lambda_upper','.6'),('ell_u','2.034'),('beta_u','.234')]:assert central[key]<F(bound)
for key,bound in [('ell_l','1.9706'),('beta_l','.09736')]:assert central[key]>F(bound)
summary={k:max(x[k]for x in kept)for k in ['theta','d','rho','lambda_upper']}
summary['ell_lower']=min(x['ell_l']for x in kept)
print(json.dumps(encode({'status':'PASS_DIRECT_ONE_PASS_PANEL_CALCULATIONS','source_input_sha256':PIN,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python':sys.version,'updates_per_panel':1,'excluded':[x['index']for x in rows if x['excluded']],'complete_point_six_strips':strips,'global_outward':summary,'panels':rows,'limitations':'Conditional on the global direct-geometry theorem, accepted v7 entry and retained all-threshold heat/ray theorem; no phase/count cover or full conjecture.'}),indent=2))

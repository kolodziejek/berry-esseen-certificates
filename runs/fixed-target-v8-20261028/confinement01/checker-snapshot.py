#!/usr/bin/env python3
"""One fixed probability panel: exact moment/strip proof and ray diagnostic.

No archive imports, native acceptors, Fourier computation, or mesh search.
The final confinement diagnostic covers 8 phase by 8 noise boxes, both signs.
Its failed strict gates are reported, never relabelled as accepted.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import isqrt
import json,sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PINS={
 'mathematics/strategy-v4/2026-10-27/excess.tex':'a7105d57f4f353a7fcdd32947b1feae044b3df5dc29558afb48c575e9ea4a2d0',
 'manuscript/arxiv-v1/sections/04-support.tex':'562b9ed903f996f643abef552314b2a70a6e250f9f7d01e5a589c18a9e53dfc5',
 'manuscript/arxiv-v1/appendices/uniform-bridge.tex':'3535cdd8b73b6296af0e6799b4a9b6d4789a5525cfd9502f513a8f1a1e2d456a',
 'manuscript/arxiv-v1/appendices/fourier-analysis.tex':'0274a491a12fec13d87a391ce88184cc7229210168fc72bc88974e5382670a1f',
 'mathematics/fixed-target-v5/2026-10-27/response-proof/response.tex':'274c9f75df734313cdbd34b62eb74629988bb981f3ba83e376a0b682a1a9aa1b',
}
INPUT_SHA='61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae'
N=42
SL=F('3.162277660')
CL,CU=F('0.4095'),F('0.40974')
l,h=F(41,100),F(21,50)
vl,vh=l*(1-l),h*(1-h)
D,TH0=F(7,10),F(27,100)
TH,d0=F(54,1000),F(69,1000)
R,rho0=F(96,25),F(61,50)
E,FL=F('1.9706'),F('2.034')
SIGMA,R0,TAU=F(3,5),F(49,100),F(1,5)
T,HMAX,LAMBDA=F('2.016'),F('1.814'),F(3,5)
KAPPA=F(997,15000)

def need(ok,why):
 if not ok:raise ValueError(why)

def sqrt_lo(x):
 need(x>=0,'square root domain');scale=10**10
 y=F(isqrt(x.numerator*scale*scale//x.denominator),scale)
 need(y*y<=x<(y+F(1,scale))**2,'directed square root')
 return y

def sqrt_hi(x):return sqrt_lo(x)+F(1,10**10)
def pos(x):return max(F(0),x)

def unique(pairs):
 out={}
 for key,value in pairs:
  need(key not in out,'duplicate key');out[key]=value
 return out

def bind(data):
 need(len(data['panels'])==100,'complete source probability table')
 for i,z in enumerate(data['panels']):
  need(F(z['pl'])==F(i,100) and F(z['pu'])==F(i+1,100),'closed ordered source panels')
 z=data['panels'][41]
 need(z['cells']>0 and F(z['pl'])==l and F(z['pu'])==h,'literal nonempty panel')
 need(F(z['D'])<D and F(z['theta'])<TH0 and F(z['raw'])<T and F(z['H'])<HMAX,'strict outward input ceilings')
 return z

def moment_chain():
 need(SL>1 and SL*SL<10 and D<SL-1,'actual central gap license')
 au,bu=sqrt_hi(h/(1-h)),sqrt_hi((1-l)/l)
 ab=(SL-1-D)/3
 al,bl=ab/bu,ab/au
 cg=2*sqrt_lo(ab*vl)
 need(0<cg<1 and al>0 and bl>0,'initial central endpoints')
 theta,d=TH0,1-cg
 steps=[]
 for j in range(4):
  am=sqrt_lo((1-theta)*l/(1-l));bm=sqrt_lo((1-theta)*(1-h)/h)
  kp=(SL-1)*(bl+2*bm)+6*bl
  km=(SL+1)*(al+2*am)+6*al
  theta=min(theta,D/min(kp,km))
  ee=sqrt_lo((1-theta)/vh);mm=sqrt_lo((1-theta)*vl)
  d=min(d,D/(6*mm*ee*ee*cg))
  cg=max(cg,1-d)
  al=max(al,ee*(l-d));bl=max(bl,ee*(1-h-d))
  steps.append(dict(step=j+1,theta=theta,d=d,negative_endpoint=al,
                    positive_endpoint=bl,increment=cg,cost_positive=kp,cost_negative=km))
 need(theta<TH and d<d0,'fixed four-step output targets')
 need(0<E and E*E<(1-TH)/vh and FL*FL>1/vl,'scale bounds')
 al=E*(l-d0);bl=E*(1-h-d0)
 ell_max_q3=R+2*bu
 ratio=min(SL-1+6*bl/(R+2*bu),SL+1+6*al/(R+2*au))
 rb=(1-2*vl)/sqrt_lo(vl)
 decay=F(29,20)
 need(decay*decay<F(9,4)*(1-TH),'skeleton decay slope')
 need(ell_max_q3-decay*rb>0,'piecewise moment maximum slope')
 threshold=min(TH,D/(ratio*ell_max_q3))
 rho=rb+(ell_max_q3-decay*rb)*threshold
 need(rho<rho0,'coherent third moment cap')
 bminus=1-2*h-2*(1-h)*TH;bplus=1-2*l+TH
 cost_theta=min((SL-1)*(bl+2*sqrt_lo((1-TH)*(1-h)/h))+6*bl,
                (SL+1)*(al+2*sqrt_lo((1-TH)*l/(1-l)))+6*al)
 noise=N*D*vh/((1-TH)*cost_theta)
 need(noise<LAMBDA,'weighted noise ceiling')
 return dict(steps=steps,rho_upper=rho,beta_lower=bminus,beta_upper=bplus,
             noise_upper=noise,theta_cost=cost_theta,third_moment_cost=ratio,
             q3_upper=ell_max_q3,skeleton_rho_upper=rb,endpoint_A=al,endpoint_B=bl)

def heat_boundary(u,b):
 need(u>0 and u*u>3,'extended heat boundary domain')
 S=F(81,80);need(S*S>F(42,41),'heat scale')
 A=(u**3-3*u)/6;H4=u**4-6*u*u+3
 rem=u**5/4100+3*u/820+17*(3*u*u-2)/78720
 Q=-u**3+F(3,2)*rho0*u*u+3*b*u+F(8,875)*rho0
 Qp=-3*u*u+3*rho0*u+3*b;Qpp=-6*u+3*rho0
 boundary=F(2,5)*S**3*(A+abs(H4)/72)+S**3*rem+CL*Q
 rays=[Q,Qp,Qpp,F(2,5)*(u*u/2+F(1,2)+F(8,875))+CL*Qp,
       F(2,5)*u+CL*Qpp,F(2,5)-6*CL]
 need(boundary<0 and all(z<0 for z in rays),'strict boundary and whole-ray signs')
 return dict(radius=u,beta_direction=b,heat_upper=boundary,ray_gates=rays,
             H4=H4,absolute_H4_used=abs(H4))

def confinement(moment):
 """Independent exact evaluation of the parameterized retained inequalities."""
 need(0<d0<R0<SIGMA and 1-SIGMA-2*d0>0,'initial strip geometry')
 need(d0+2*TAU<R0 and 1-d0-TAU>0 and 1-2*d0-2*TAU>0,'upper interval geometry')
 buffer=F(1,100000)
 need(SIGMA+d0<1-d0 and SIGMA+d0-TAU-buffer<1-d0,'strict lower interval widths')
 need(24**2*vl**3>(3*(1-l)+SIGMA)**2,'conditional cubic coefficient')
 fd=F(1037,1000)
 need(fd*fd>max(F(N,N-1)**3,F(N,N-2)),'two deleted-index factors')
 rL=l-(1-l)/(N-2);rR=h+h/(N-2)
 need(0<rL<rR<1,'binomial modes')
 vs=min(rL*(1-rL),rR*(1-rR))
 M=sqrt_hi(F(4,25)/(vs*(1-F(1,12*(N-2)))**2))
 cp=2*F('5.16')*E*E*(1-h-d0)**2
 cm=2*F('7.16')*E*E*(l-d0)**2
 bs=min(3*F('4.16')*E*(1-h-d0),3*F('6.16')*E*(l-d0))
 alpha=min(cp*l*E,cm*(1-h)*E)
 need(min(cp,cm,bs,alpha)>0,'single resource coefficients')
 eta_phase=(CL-T/N)/2
 need(eta_phase>0,'raw Gaussian license and phase price')
 f=F(2,5)*FL;Bstar=F(6,5)
 need(Bstar*Bstar>(1-l)/l,'positive half-line physical endpoint')
 a_e=fd*M*(1/l+1/(1-h))/2
 g=1-SIGMA-2*d0
 records=[]
 for sign in (1,-1):
  for j in range(8):
   hl,hh=HMAX*F(j,8),HMAX*F(j+1,8)
   for k in range(8):
    ll,lh=LAMBDA*F(k,8),LAMBDA*F(k+1,8)
    rhostar=min(rho0,moment['skeleton_rho_upper']+24*lh/N)
    bm,bp=moment['beta_lower'],moment['beta_upper']
    philo=F('0.39886')*(1-hh*hh/(2*N));need(philo>0,'density lower bound')
    vplus=F(2,5)*hh if sign==1 else -philo*hl
    need(vplus+3*CU*rhostar>0,'negative-side square-completion direction')
    minus=FL*pos((vplus+3*CU*rhostar)**2/(12*CL)-3*CL*bm)
    plus=FL*pos(F(2,5)*hh*Bstar+3*CU*Bstar*(Bstar-1)-3*CL*bm)
    Lgap=E*philo-max(minus,plus)/N
    Uplus=f+FL/N*(3*CU*bp+(F(2,5)*hh+3*CU*rhostar)**2/(12*CL))
    tstar=-E*(l+TAU+buffer)
    vertex=min(tstar,-rhostar/2)
    Bmin=bm+rhostar*vertex+vertex*vertex
    vertex2=min(tstar,-(vplus+3*CL*rhostar)/(6*CL))
    qmin=3*CL*(bm+rhostar*vertex2+vertex2*vertex2)+vplus*vertex2+3*(CU-CL)*min(F(0),Bmin)
    L=E*philo-FL*pos(-qmin)/N
    need(L>0 and Lgap>0 and Uplus>0,'slope positivity')
    budget=T-eta_phase*hl*hl
    remaining=budget/KAPPA-bs*E*E*ll
    base=dict(sign=sign,phase=[hl,hh],noise=[ll,lh],budget=budget)
    if remaining<=0:
     records.append(dict(**base,resource_excluded=True));continue
    G=remaining/alpha
    bad=min(lh/(lh+N*l*TAU*TAU),G/(N*TAU+G))
    sides=[]
    for side in ('lower','upper'):
     if side=='lower':
      vH=-hl/FL if sign==1 else hh/E
      DI=pos(vH-l-TAU-buffer);DJ=pos(vH+1-l-buffer)
      ad,aJ=L,1/g;lhs=L*(R0-TAU-buffer)
     else:
      DI=pos(d0+TAU+hh/E-l);DJ=pos(1+d0+2*TAU+hh/E-l)
      ad,aJ=Lgap+Uplus,1/TAU;lhs=Lgap-SIGMA*Uplus
     AA=fd*M*(DI/l+DJ/(1-h));BB=fd*M
     z=max((ad/l+2*a_e)/(E*cp),(ad/(1-h)+2*a_e)/(E*cm),KAPPA*aJ/(1-TH))
     need(z*remaining+AA>0,'inverse-index sign')
     errors=[(z*remaining+AA)/N+BB*bad]
     vertices=[((ad/l+2*a_e)/(E*cp)*remaining/N,remaining/(E*cp*l)),
               ((ad/(1-h)+2*a_e)/(E*cm)*remaining/N,remaining/(E*cm*(1-h))),
               (KAPPA*aJ/(1-TH)*remaining/N,F(0))]
     for kk in range(11):
      tangent=F(kk,10)*G
      slope=N*TAU/(N*TAU+tangent)**2;intercept=tangent*tangent/(N*TAU+tangent)**2
      errors.append(AA/N+max(v+BB*slope*w for v,w in vertices)+BB*intercept)
     error=min(errors)
     sides.append(dict(side=side,lhs=lhs,error=error,margin=lhs-error,passed=lhs>error))
    records.append(dict(**base,resource_excluded=False,sides=sides))
 all_sides=[dict(sign=z['sign'],phase=z['phase'],noise=z['noise'],**s) for z in records if not z['resource_excluded'] for s in z['sides']]
 worst=min(all_sides,key=lambda s:s['margin'])
 failed=sum(not s['passed'] for s in all_sides)
 return dict(target_amplitude=R0,phase_cells=8,noise_cells=8,signs=2,boxes=len(records),
     resource_excluded=sum(z['resource_excluded'] for z in records),ray_gates=len(all_sides),failed_ray_gates=failed,
     complete_confinement_pass=(failed==0),worst=worst,records=records,
     scope='New scalar diagnostic only; failure of a sufficient bound is not a counterexample to confinement.')

def run():
 need(__debug__ and not sys.flags.optimize,'unoptimized Python')
 for name,digest in PINS.items():need(sha256((ROOT/name).read_bytes()).hexdigest()==digest,'source pin '+name)
 blob=(HERE/'confinement-sources/entry-proof.json').read_bytes()
 need(sha256(blob).hexdigest()==INPUT_SHA,'frozen entry object')
 data=json.loads(blob,object_pairs_hook=unique);panel=bind(data)
 moment=moment_chain()
 neg=heat_boundary(F(9,5),-moment['beta_lower'])
 positive=heat_boundary(F(93,40),moment['beta_upper'])
 need(F(9,5)<E*(l+SIGMA) and F(93,40)<E*(1+SIGMA-h),'physical radii imply Bernoulli strip')
 diagnostic=confinement(moment)
 rejected=[]
 def reject(name,call):
  try:call()
  except ValueError:rejected.append(name)
  else:raise ValueError('bad control accepted: '+name)
 from copy import deepcopy
 bad=deepcopy(data);bad['panels'].pop();reject('missing probability panel',lambda:bind(bad))
 bad=deepcopy(data);bad['panels'].reverse();reject('reordered probability cover',lambda:bind(bad))
 bad=deepcopy(data);bad['panels'][41]['D']='4/5';reject('understated input defect',lambda:bind(bad))
 reject('duplicate key',lambda:json.loads('{"D":1,"D":2}',object_pairs_hook=unique))
 reject('false coarse positive radius',lambda:heat_boundary(F(23,10),moment['beta_upper']))
 reject('wrong beta reflection on negative radius',lambda:heat_boundary(F(9,5),moment['beta_upper']))
 reject('old upper-tau choice without its gate',lambda:need(d0+2*7*R0/15<R0,'upper geometry'))
 reject('claiming half amplitude without every ray gate',lambda:need(diagnostic['complete_confinement_pass'],'failed scalar gates'))
 return dict(status='PASS_CONDITIONAL_PANEL_STRIP_WITH_UNRESOLVED_HALF_AMPLITUDE',
   scope='Conditional on fixed-target contact, sharp predecessor, acquired entry row and weighted nD. All-index moment/strip proof; no full local acceptance.',
   panel=panel,input_sha256=INPUT_SHA,source_sha256=PINS,moments=moment,
   physical_support=dict(negative=neg,positive=positive),strip=SIGMA,inward_bound=d0,
   confinement_diagnostic=diagnostic,negative_controls=rejected,
   checker_sha256=sha256(Path(__file__).read_bytes()).hexdigest())

if __name__=='__main__':
 print(json.dumps(run(),default=lambda x:str(x) if isinstance(x,F) else x,sort_keys=True,indent=2))

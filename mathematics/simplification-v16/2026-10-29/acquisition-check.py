"""Exact gates and actual-law controls for the scalar n700 acquisition.

No panel export, old constructor, or interval proof object is imported.
The proof supplies the analytic implications and whole-ray continuation.
"""
from fractions import Fraction as F
from pathlib import Path
import json,sys,hashlib
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
SL=F('3.162277660');SU=F('3.162277661');N=700;B=F('32.20665378');D=F(47,1000)
z=(SL-1-D)/3;L0=F(9,25);U0=F(12,25);L=F(3,8);U=F(93,200)
T0=F(3,500);T=F(9,2500);d=F(1,250);e0=F(167,100);e1=F(199,100);e=F(499,250)
r=F(9,8);vmin=L*(1-L);A=F(3,5)
gates={}
def gate(name,x):
 assert name not in gates;gates[name]=F(x);assert x>0,(name,x)
def Q(p,s=SL):return (2*s+6)*p*p-(2*s+4)*p+s-1
# All irrational replacements are made with their verified sign.
gate('sigma_lower',10-SL*SL);gate('sigma_upper',SU*SU-10)
gate('n700_defect',N*D-B);gate('central_gap',SL-1-D)
gate('z_positive',z);gate('z_below_one',1-z)
gate('critical_point_above_coarse_left',(4-SU)/2-L0)
gate('critical_point_below_coarse_right',U0-(4-SL)/2)
for name,p in [('left',L0),('right',U0)]:
 gate('coarse_'+name+'_Q_positive',Q(p))
 gate('coarse_'+name+'_exclusion',4*z**3*Q(p)**2-D*D)
gate('ell_coarse',4*z-e0*e0)
kp=(1-U0)*((SL+5)*z+2*(SL-1));km=L0*((SL+7)*z+2*(SL+1))
gate('noise_price_positive',kp-F(26,5));gate('noise_price_negative',km-F(26,5))
gate('theta_coarse',e0*F(26,5)*T0-D)
gate('ell_intermediate',4*(1-T0)-e1*e1)
gate('coarse_inward_lt_point2',4*z*L0*(1-L0)-F(4,5)**2)
C0=min(3*(SL+1)*(1-U0),3*(SL+3)*L0)
gate('C0_above_6point49',C0-F('6.49'))
gate('direct_noise_positive',C0-(SU+7)*F(1,5))
gate('direct_d_monotonic',6*(1-T0)*F(3,5)-T0*(SU+7))
gate('inward_lt_point004',e1*(1-T0)*6*d*(1-d)-D)
Qmax=max(Q(L0,SU),Q(U0,SU));gate('coarse_Q_below_point05',F(1,20)-Qmax)
gate('theta_monotonic_at_dzero',(2-3*T0)*C0-3*Qmax)
# Q/sqrt(v) is decreasing left of p* below1/2. At the right end, use
# Q(p)>=Q(U)>D/2 and sqrt(v)<=1/2; this avoids a false right monotonicity
# claim when p is below1/2.
gate('fine_left_Q',Q(L));gate('fine_left_exclusion',Q(L)**2-D*D*L*(1-L))
gate('fine_right_Q',Q(U));gate('fine_right_exclusion',2*Q(U)-D)
gate('critical_point_inside_fine',(4-SU)/2-L)
gate('critical_point_below_fine_right',U-(4-SL)/2)
C=min(3*(SL+1)*(1-U),3*(SL+3)*L)
gate('theta_refined',e1*C*T-D);gate('ell_final',4*(1-T)-e*e)
# rho<=rho_B+D/(sigma-1), needing no numerical support radius.
gate('rhoB_below_1point1',F(11,10)**2*vmin-(1-2*vmin)**2)
gate('rho_noise_price',SL-1-F(54,25))
gate('rho_below_9over8',r-F(11,10)-D/F(54,25))
beta_l=1-2*U-2*(1-U)*T;beta_u=1-2*L+2*L*T
assert beta_l==F('0.066148') and beta_u==F('0.2527')
# General cubic/AMGM budget: a few exact root lower bounds suffice here.
rad0=6*(1-d)*(SL+1)*L
rad1=6*(1-d)*(SL-1)*(1-U)
rad1left=6*(1-d)*(SL-1)*F(3,5)
gate('amgm_root0',rad0-9);gate('amgm_root1',rad1-F(13,5)**2)
gate('amgm_root1_left',rad1left-F(27,10)**2)
y0=3*(SL+3)*L-(SU+7)*d+6
y1=3*(SL+1)*(1-U)-(SU+5)*d+F(26,5)
y1left=3*(SL+1)*F(3,5)-(SU+5)*d+F(27,5)
gate('Y0_gt_12point8',y0-F(64,5));gate('Y1_gt_11point8',y1-F(59,5))
gate('Y1left_gt_12point8',y1left-F(64,5))
gate('global_lambda_lt_point35',e**3*F(59,5)*F(7,20)-B)
gate('left_lambda_lt_point32',e**3*F(64,5)*F(8,25)-B)
# Two whole rays, independent of probability panels and raw threshold.
def ray(label,t,b):
 S=F(81,80);eta=F(8,875);c=F(819,2000)
 q=-t**3+F(3,2)*r*t*t+3*b*t+eta*r
 q1=-3*t*t+3*r*t+3*b;q2=-6*t+3*r
 h=S**3*(F(2,5)*((t**3-3*t)/6+abs(t**4-6*t*t+3)/72)
           +t**5/4100+3*t/820+17*(3*t*t-2)/78720)
 values=[t*t-3,-h-c*q,-q,-q1,-q2,
  -F(2,5)*(t*t/2+F(1,2)+eta)-c*q1,-F(2,5)*t-c*q2,-F(2,5)+6*c]
 for i,x in enumerate(values):gate(label+'_ray_'+str(i),x)
 return {'boundary':str(t),'beta_price':str(b),'eight_margins':[str(x) for x in values]}
rays=[ray('negative',e*(L+A),-beta_l),ray('positive',e*(1-U+A),beta_u)]
gate('raw_H_join',F(46,25)-F('1.83605680'))
gate('left_amplitude_join',F(7,10)-A);gate('left_inward_join',F(17,250)-d)
gate('right_inward_join',F(9,125)-d)

# Q(sqrt10) arithmetic, implemented here for exact actual-law tests.
def qa(x,y):return x[0]+y[0],x[1]+y[1]
def qs(x,y):return x[0]-y[0],x[1]-y[1]
def qm(x,y):return x[0]*y[0]+10*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def qscale(x,c):return x[0]*c,x[1]*c
def sign(x):
 a,b=x
 if b==0:return (a>0)-(a<0)
 if a==0:return (b>0)-(b<0)
 if a>0 and b>0:return 1
 if a<0 and b<0:return -1
 if a>0:return (a*a>10*b*b)-(a*a<10*b*b)
 return (10*b*b>a*a)-(10*b*b<a*a)
def canonical(atoms):
 out={}
 for x,w in atoms:out[x]=out.get(x,F(0))+w
 return sorted((x,w)for x,w in out.items()if w)
def noise(amplitude,var,side):
 if var==0:return [(F(0),F(1))]
 a=var/amplitude
 return ([(-amplitude,a/(amplitude+a)),(a,amplitude/(amplitude+a))] if side==0 else
         [(-a,amplitude/(amplitude+a)),(amplitude,a/(amplitude+a))])
def law_stats(n,p,lam,side,amplitude=F(3,5)):
 q=1-p;v=p*q;s=lam/n;noises=[[(F(0),F(1))],[(F(0),F(1))]]
 if side==2:
  noises=[noise(amplitude,s,0),noise(amplitude,s,1)]
 else:noises[side]=noise(amplitude,s/(q if side==0 else p),side)
 atoms=canonical([(u-p,q*w)for u,w in noises[0]]+[(1+u-p,p*w)for u,w in noises[1]])
 assert sum(w for x,w in atoms)==1 and sum(x*w for x,w in atoms)==0
 V=sum(x*x*w for x,w in atoms);M=sum(abs(x)**3*w for x,w in atoms);G=sum(x**3*w for x,w in atoms)
 J=sum(sum(x*w for x,w in atoms if x>=b)*(b-a)**2 for (a,wa),(b,wb)in zip(atoms,atoms[1:]))
 assert V==v+s
 dn=(3*M-G-3*J,M)
 budget=sign(qs((B*B*V**3,F(0)),qscale(qm(dn,dn),n*n)))>=0 and sign(dn)>=0
 a0=max(u for u,w in noises[0]);a1=max(-u for u,w in noises[1]);dd=a0+a1
 assert max(x for x,w in atoms if x<0)<0<min(x for x,w in atoms if x>0)
 qq=(p*p-q*q-6*v,p*p+q*q)
 cp=(3*q,3*q);cm=(9*p,3*p)
 kp=qs(cp,((5*dd),dd));km=qs(cm,((7*dd),dd));kk=kp if sign(qs(kp,km))<=0 else km
 lower=qa(qscale(qq,v),qa((6*v*dd*(1-dd),F(0)),qscale(kk,s)))
 assert sign(qs(dn,lower))>=0
 if budget and n>=N:
  assert L<p<U and s/V<T and dd<d and e*e*V<1
  assert M*M<r*r*V**3 and lam<F(7,20)
  if p<=F(2,5):assert lam<F(8,25)
 return {'n':n,'p':str(p),'lambda':str(lam),'noise_side':side,
  'noise_amplitude':str(amplitude),'satisfies_nD_budget':budget,
  'inward_sum':str(dd),'rho_squared':str(M*M/V**3),
  'D_numerator_Qsqrt10':[str(x)for x in dn],
  'outer_radius_below_3point14':all(x*x<F('3.14')**2*V for x,w in atoms)}
actual=[]
for n in [700,1400]:
 for p in [F(2,5),F(21,50),F(9,20)]:
  for lam,side in [(F(0),0),(F(1,10**12),0),(F(1,100),1),(F(1,10),2)]:
   actual.append(law_stats(n,p,lam,side))
assert any(x['satisfies_nD_budget'] for x in actual)
# A rare .8 noise satisfies the geometric assumptions, including the old
# radius3.14, but violates the .6 strip: contact is a genuine extra edge.
no_contact=law_stats(700,F(21,50),F(1,10**6),0,F(4,5))
assert no_contact['satisfies_nD_budget'] and no_contact['outer_radius_below_3point14']
assert F(no_contact['noise_amplitude'])>A
# Without n>=700 the probability conclusion fails even for actual Bernoulli.
low_n=law_stats(42,F(3,10),F(0),0)
assert low_n['satisfies_nD_budget'] and F(low_n['p'])<L
# The geometric defect is signed; reflection does not preserve its budget.
reflected=law_stats(700,F(29,50),F(0),0)
assert not reflected['satisfies_nD_budget']
# Exact arithmetic field sanity checks including both sign branches.
assert sign((F(-3),F(1)))>0 and sign((F(3),F(-1)))<0
assert sign((F(-4),F(1)))<0 and sign((F(4),F(-1)))>0
here=Path(__file__).resolve();proof=here.with_name('acquisition-direct.tex')
print(json.dumps({'status':'PASS_SCALAR_ACQUISITION_N700','scalar_gates':len(gates),
 'gates':{k:str(v)for k,v in gates.items()},'two_whole_rays':rays,
 'actual_law_controls':actual,'actual_law_control_count':len(actual),
 'budget_eligible_actual_laws':sum(x['satisfies_nD_budget']for x in actual),
 'negative_controls':{'geometry_without_contact':no_contact,'missing_n700':low_n,'unlicensed_reflection':reflected},
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest()if proof.exists()else None,
 'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),'python':sys.version,
 'scope':'Post-entry analytic shortcut; no new Fourier or contact proof, no finite-base or unconditional cutoff claim.'},indent=2))

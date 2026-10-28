"""Exact scalar gates for the all-panel small-noise candidate."""
from fractions import Fraction as F
import json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
A=F(7,10);d=F(17,250);U=F(1,500);N=F(42);v=F(3,16)
lo=-F(109,500);hi=F(391,500);b=F(1,20);D=F(171,100);xi=F(46,25)*F(501,1000)
Z=lambda x:2*x+F(53,100)+4*x**3/N
B0=F(4);cv=F(4);checks={}
def gate(k,x):checks[k]=x
for name,delta,a,fl,fu in [('global',D,hi,F(2,3),F(3,2)),('inner',F(1),b,F(9,10),F(27,25))]:
 eta=(B0*U+(2*delta*a+a*a)/(2*v)+Z(delta))/N
 gate(name+'_f_lower',1-eta-fl);gate(name+'_f_upper',fu*(1-eta)-1)
assert hi-lo==1
assert lo==(A-1-2*d)/2 and hi==(A+1-2*d)/2
gate('delta',D-xi-hi);gate('innerdelta',1-xi-b)
gate('sqrtvar',F(501,1000)**2-F(1,4)-U/N)
gate('count_lower',F(1,4)-D/N-F(1,5))
gate('count_upper',F(29,50)-F(53,100)-D/N)
gate('segment_variance',F(1,5)*F(4,5)-F(159,1000))
gate('entropy3',24-F(3,5)/F(4,25)**2)
gate('logderivative',4-F(3,5)/F(4,25))
gate('stirling_remainder',F(53,100)-1/(12*F(4,25)))
gate('B0',B0-1/(2*v)-D*D/(2*N*v*v))
mass=lambda z:2*F(19943,50000)*(1-(z*z/(2*v)+Z(z))/N)
gate('mass_global',mass(D)-F(14,25));gate('mass_inner',mass(1)-F(69,100))
gate('mode_mass',v*(1-Z(1)/N)**2-F(2,5)**2)
gate('global_ratio',F(9,5)*F(14,25)-1)
gate('inner_ratio',F(107,100)-1-F(53,100)/(N*v))
gate('incoming_inner_variance',F(6,5)-1-cv*2/N)
gate('incoming_global_variance',F(4,3)-1-cv*(D+1)/N)
gate('own_global_variance',F(7,6)-1-cv*D/N)
negative=F(3,2)*(1-2*v)+d-F(3,4)+3*(1-2*v)*U/(8*N*v)
gate('moment_repair',F(4,3)**2*v**3-(F(41,100)*negative)**2)
gate('normal_repair',F(5,2)**2*v**3-F(1,5)**2)
gate('CEcap',36*F(41,100)**2*2*F(314159,100000)-(3+F(3162277661,10**9))**2)
gate('global_repair',6-F(5,2)*D-F(4,3));gate('inner_repair',4-F(5,2)-F(4,3))
alpha=F(3,5);den=5*alpha**4;tmax=F(23,21)*U;cm=F(1,4);cp=F(4,5)
def qm(c0,c1,c2,z):
 vals=[c0,c0+c1*z+c2*z*z]
 if c2>0 and 0<-c1/(2*c2)<z:vals.append(c0-c1*c1/(4*c2))
 return min(vals)
def quartic(sig,fl,z):
 return min(qm((3*alpha**2-A*A-3*t)/den,2*sig/(5*alpha)+fl-4*A*t/den,(3*alpha**2*t-6*t*t-t**3*z*z)/den,z)for t in [F(0),tmax])
zm=F(3,2);zp=F(1)
gate('quartic_negative',quartic(1,-F(27,25),zm)-cm)
gate('quartic_positive',quartic(-1,F(9,10),zp)-cp)
gate('negative_switch',zm*zm/(1+zm*zm*tmax)-F(27,25)*zm-cm)
gate('negative_switch_derivative',2*zm/(1+zm*zm*tmax)**2-F(27,25))
gate('negative_endpoint',b*b/(tmax+b*b)-F(27,25)*b-cm*tmax)
gate('negative_switch_inside',b-zm*tmax);gate('positive_switch_inside',b-zp*tmax)
gate('positive_linear',F(9,10)*zp-cp)
def Q(mu,h):
 a=(1-h)/A-1
 return mu*mu*(F(1,2)+mu/6)/(a+mu)**2
def J(mu,h,start=2):
 denb=1/A-1-h/(start*A)
 first=F(1,3)*mu**3 if start==2 else F(3,8)*mu**4
 return first/((denb+mu)**2*(1-3*mu))
muI=F(6,5)*U/A**2;muG=F(4,3)*U/A**2
for label,mu,h,j in [('inner',muI,b,2),('negative',muG,F(0),2),('positive',muG,hi,3)]:
 gate(label+'_tail_denominator',1/A-1-h/(j*A));gate(label+'_tail_ratio',1-3*mu)
gate('first_inner_monotone',(1-b)/A-1-muI)
gate('first_negative_monotone',1/A-1-muG)
TI=Q(muI,b)+J(muI,b)
br=cm*F(19,21)-F(107,100)*TI/U
gate('inner_bracket',br);gate('inner_final',F(69,100)*br-F(4,42)-F(1,100))
TG=F(7,6)*U
neg=min(r*r/(TG+r*r)-F(3,2)*r for r in[b,-lo])
gate('negative_concavity',3*b*b-TG)
br=neg-F(9,5)*(Q(muG,0)+J(muG,0))
gate('negative_bracket',br);gate('negative_final',F(14,25)*br-6*U/N-U/100)
t=F(4,3)*U
gate('positive_concavity1',3*(1-hi)**2-t);gate('positive_concavity2',3*(2-hi)**2-2*t)
base=min(F(2,3)*u-F(9,5)*(t/(t+(1-u)**2)+2*t/(2*t+(2-u)**2))for u in[b,hi])
br=base-F(9,5)*J(muG,hi,3)
gate('positive_bracket',br);gate('positive_final',F(14,25)*br-6*U/N-U/100)
# Negative controls: reject three tempting but false shortcuts.
pbad=F(13,50);vbad=pbad*(1-pbad);sbad=(1-pbad)/10**6
mbad=vbad*(1-2*vbad)+3*pbad*sbad
assert mbad**2*vbad < (1-2*vbad)**2*(vbad+sbad)**3
def exact_own_corner(z,t):
 return (3*alpha**2-A*A-3*t)/den+(2/(5*alpha)-F(27,25)-4*A*t/den)*z+(3*alpha**2*t-6*t*t)*z*z/den-t**3*z**4/den
assert exact_own_corner(zm,tmax)<F(1,3)
assert (2-hi)/A+2*muG-2<0
negative_controls=['adverse_third_moment_is_real','stronger_own_constant_rejected','second_hinge_domain_rejected']
fail={k:str(v)for k,v in checks.items()if v<=0}
print(json.dumps({'status':'PASS_ALLPANEL_SCALAR_GATES'if not fail else'FAILED','gate_count':len(checks),'negative_controls':negative_controls,'failed':fail,'margins':{k:str(v)for k,v in checks.items()if 'final'in k},'checks':{k:str(v)for k,v in checks.items()},'scope':'Scalar gates only; complete probability/geometry join requires proof and review'},indent=2))
assert not fail

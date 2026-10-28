"""Exact finite gates for the independently derived direct geometry bounds."""
from fractions import Fraction as F
from math import comb
import hashlib,json,sys
from pathlib import Path
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions must remain enabled')
def P(*c):return [F(x) for x in c]
def add(a,b):return [(a[i]if i<len(a)else F(0))+(b[i]if i<len(b)else F(0))for i in range(max(len(a),len(b)))]
def scale(a,c):return [x*c for x in a]
def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
def der(a):return [(i+1)*a[i+1] for i in range(len(a)-1)]
def val(a,x):
 z=F(0)
 for c in reversed(a):z=z*x+c
 return z
def qmin(a,l,h):
 assert len(a)<=3
 xs=[l,h]
 if len(a)==3 and a[2]>0:
  v=-a[1]/(2*a[2])
  if l<=v<=h:xs.append(v)
 return min(val(a,x)for x in xs)
def bern(a,l,h):
 n=len(a)-1
 power=[sum(a[j]*comb(j,k)*l**(j-k)*(h-l)**k for j in range(k,n+1))for k in range(n+1)]
 return [sum(power[k]*F(comb(i,k),comb(n,k))for k in range(i+1))for i in range(n+1)]
s=F('3.162277660');su=F('3.162277661');D=F('.76682509');N=42;ND=F('32.20665378');z=(s-1-D)/3
T=F('.056');W=1-T;d0=F('.068');l=F('.24');h=F('.54');v=P(0,1,-1)
Q=P(s-1,-2*s-4,2*s+6);Qu=P(su-1,-2*su-4,2*su+6)
Cp=P(3*(s+1),-3*(s+1));Cm=P(0,3*(s+3));Bmax=su+7
checks={}
def ck(name,ok,value=None):
 if not ok:raise AssertionError(name+': '+str(value))
 checks[name]=str(value)if value is not None else True
ck('sqrt10 enclosure',s*s<10<su*su)
ck('weighted gives D0',ND==N*D)
ck('z positive and <1/2',0<z<F(1,2),z)
ck('Q upper .4',max(val(Qu,l),val(Qu,h))<F(2,5))
ck('all C lower 4.4',min(val(Cp,h),val(Cm,l))>F('4.4'))
Kp=F('.46')*((s+5)*z+2*(s-1));Km=F('.24')*((s+7)*z+2*(s+1))
ck('coarse physical K>=3.13',min(Kp,Km)>F('3.13'),min(Kp,Km))
ck('theta>=.2 contradicts D0',F(313,250)**2*z>D*D)
ck('endpoint g lower .59',4*z*F('.1824')/W>F('.59')**2)
ck('endpoint g upper .77',z/F('.8')<F('.77')**2)
ck('endpoint d(1-d)>.17',min(F('.59')*F('.41'),F('.77')*F('.23'))>F('.17'))
ck('endpoint K positive',F('4.4')-Bmax*F('.41')>0)
ck('endpoint ell>1.7',F('.8')/F('.25')>F('1.7')**2)
ck('endpoint inward cost > D0',F('1.7')*6*F('.8')*F('.17')>D)
ck('d0 noise monotonicity',F('1.4')*F('4.4')-3*F('.4')>0)
polys={}
for name,C,x,margin in [('theta_plus',Cp,F('.45'),F('.0017')),('theta_minus',Cm,F('.39'),F('.011'))]:
 A=add(scale(Q,W),scale(C,T));ck(name+' positive squaring base',qmin(A,l,h)>0);poly=add(scale(mul(A,A),W),scale(v,-D*D));polys[name]=poly
 cmin=qmin(der(der(poly)),l,h)
 ck(name+' second derivative',cmin>=2*D*D,cmin)
 low=val(poly,x)-val(der(poly),x)**2/(4*D*D)
 ck(name+' tangent lower',low>margin,low)
ck('global d<.42',4*z*F('.1824')>F('.58')**2)
ck('direct branches increasing in d',6*W*F('.16')-T*Bmax>0)
ck('d=.068 increases with theta',(2-3*T)*(F('4.4')-Bmax*d0)-3*(F('.4')+6*d0*(1-d0))>0)
A=add(Q,P(6*d0*(1-d0)));ck('displacement positive squaring base',qmin(A,l,h)>0);poly=add(mul(A,A),scale(v,-D*D));polys['displacement']=poly
ck('displacement second derivative',qmin(der(der(poly)),l,h)>=2*D*D)
x=F('.424');low=val(poly,x)-val(der(poly),x)**2/(4*D*D)
ck('displacement tangent lower',low>F('.0012'),low)
ck('weighted constant 17.558',ND*ND<F('17.558')**2*4*W**3)
base=add(P('17.558'),scale(Q,-N))
Up=scale(mul(P(0,1),base),1/(3*(s+1)));Um=scale(mul(P(1,-1),base),1/(3*(s+3)))
ck('lambda plus increasing before 1/3',qmin(der(Up),l,F(1,3))>0)
ck('lambda plus second <= -13',max(val(der(der(Up)),F(1,3)),val(der(der(Up)),h))<=-13)
x=F('.455');up=val(Up,x)+val(der(Up),x)**2/26
ck('lambda plus < .615289',up<F('.615289'),up)
ck('lambda minus second <= -12',max(val(der(der(Um)),l),val(der(der(Um)),h))<=-12)
x=F('.392');up=val(Um,x)+val(der(Um),x)**2/24
ck('lambda minus < .565358',up<F('.565358'),up)
ck('ell>1.94',4*W>F('1.94')**2)
ck('barB<1.8',F('.76')/F('.24')<F('1.8')**2)
ck('positive coefficient >= 2.5',s-1+6*F('1.94')*(F('.46')-d0)/(F('3.14')+2*F('1.8'))>F('2.5'))
ck('negative coefficient >= 2.5',s+1>F('2.5'))
A=add(add(P(1),scale(v,-2)),scale(Q,-F(2,5)))
ck('rho bracket nonnegative',min(bern(A,l,h))>0)
M=F('1.426')-F(2,5)*D
poly=add(scale(v,M*M),scale(mul(A,A),-1));polys['rho']=poly
ck('rho quartic second >= .4',qmin(der(der(poly)),l,h)>=F('.4'))
x=F('.258');low=val(poly,x)-val(der(poly),x)**2/F('.8')
ck('rho quartic tangent lower',low>F('.00015'),low)
ck('p<=1/4 impossible',val(Q,F(1,4))**2>D*D*F(3,16))
# No floating-point value is used in an acceptance comparison.
print(json.dumps({'status':'PASS_DIRECT_GLOBAL_GEOMETRY_GATES','hypotheses':{'p':['6/25','27/50'],'n_min':42,'nD_max':str(ND),'support_radius_for_rho_only':'157/50','common_actual_gap_budget':True},'conclusions':{'theta_strict_upper':str(T),'d_strict_upper':str(d0),'lambda_strict_upper':'77/125','rho_strict_upper':'713/500','p_strict_lower':'1/4'},'gates':checks,'quartic_coefficients':{k:[str(x)for x in v]for k,v in polys.items()},'cubic_upper_coefficients':{'positive':[str(x)for x in Up],'negative':[str(x)for x in Um]},'python':sys.version,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact scalar implications of the proved budget and stated inputs; not global Berry--Esseen or complete confinement/count acceptance.'},indent=2))

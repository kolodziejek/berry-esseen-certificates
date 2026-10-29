#!/usr/bin/env python3
"""Exact arithmetic kernels for new entry theorems; no discovery target selection.

All divisions, continuous-cell interfaces and all-index damping gates are
checked. The separate fixed acceptors supply floors, ordered targets and cover
counts. This module neither reads certificates nor writes files.
"""
from fractions import Fraction as F
from math import isqrt,comb
from functools import lru_cache
import sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('optimized Python forbidden')
RADIUS=F(9,2)
K4=(RADIUS+1)**2/(RADIUS+F(1,2))
K5=(RADIUS**3+2*RADIUS**2+3*RADIUS+F(3,2))/(RADIUS+F(1,2))
SL=F(3162277660,10**9);SU=F(3162277661,10**9);PHI=F(997,2500)
def need(c,s):
 if not c:raise ValueError(s)
def down(x,scale=10**8):return F(x.numerator*scale//x.denominator,scale)
def up(x,scale=10**8):return -down(-x,scale)
def roots(x,scale=10**8):
 need(x>=0,'nonnegative square root');k=isqrt(x.numerator*scale**2//x.denominator);a,b=F(k,scale),F(k+1,scale)
 need(a*a<=x<=b*b,'root enclosure');return a,b
@lru_cache(maxsize=32768)
def exphi(x):
 need(x>=0,'exponential sign')
 y=down(min(x,F(64)),10**6);term=F(1);total=term
 for j in range(1,65):term=term*y/j;total+=term
 need(total>0,'exponential divisor');return up(1/total,10**14)
def constants():
 need(F(23,10)<=RADIUS<=6,'actual support radius')
 need(SL*SL<10<SU*SU,'sqrt10 enclosure')
 need(PHI*PHI*F(44,7)<1,'normal density lower')
 need(PHI*(3+SL)/6>F(819,2000),'Esseen lower')
 need(F(251,100)**2>F(44,7),'Gaussian normalization')
 p=16*(F(1,5)-F(1,3*5**3)+F(1,5*5**5)-F(1,7*5**7))-F(4,239)
 need(p>F(333,106),'Machin lower')
 t=2*F(1,5)/(1-F(1,5)**2);t=2*t/(1-t*t)
 need((t-F(1,239))/(1+t/239)==1,'Machin angle branch')
 need(F(4431,2500)**2<F(333,106),'sqrt pi lower')
 # pi<22/7 from the positive integral x^4(1-x)^4/(1+x2).
 co=[F(4),F(0),F(-4),F(0),F(5),F(-4),F(1)];out=[F(0)]*9
 for j,c in enumerate(co):out[j]+=c;out[j+2]+=c
 out[0]-=4
 need(out==[0,0,0,0,1,-4,6,-4,1]and sum(c/F(j+1)for j,c in enumerate(co))==F(22,7),'pi upper identity')
def high(n,a,m,d0,mu4,window):
 need(type(n)is int and n>2,'HIGH index')
 need(0<a<=1 and m>0 and 0<d0<=12 and 1<=mu4<=F(111,10),'actual event HIGH scope')
 need(0<window<=F(1,8),'peak window')
 p,sp=F(333,106),F(4431,2500);h=p-F(22,7)**3*window**2/6;b=F(9,10)
 rate=(1-max(1-t*t+(mu4+3)*t**4/12 for t in(F(1,2),b)))/2
 k=a*F(23,48)**2*d0*d0;lo,hi=roots(F(n))
 for c in(rate,a*h*h*window*window,a*F(23,48)**2,F(1,8)):
  need(c>0 and 2*n*c>1,'complete HIGH all-index monotonicity')
 s3=sum((F(1,j**3)for j in range(1,21)),F(0))+F(1,800)
 s5=sum((1/(F(j)-window)**5 for j in range(1,21)),F(0))+1/(4*(20-window)**4)
 terms=(2*hi*exphi(n*rate),m*(s3+3*s5/(n*a*h*h))/(4*p*sp*h*roots(a)[0]),m*hi*exphi(n*a*h*h*window*window)/(2*p*p),exphi(n*k*b*b)/(2*b**4*k*lo),hi*exphi(n*a*F(23,48)**2)/(2*b*b),3*hi*exphi(F(n,8)))
 need(len(terms)==6 and all(x>0 for x in terms),'all six frequency pieces')
 return up(sum(terms),10**10),terms
def universal_high(n,M):
 d0=F(3,5);a=(2-d0*d0)**2/(2*M+6)
 return high(n,a,2/a,d0,M,F(1,8))[0]
def sixth(n,M,g,eta):
 need(type(n)is int and n>2 and 1<=M<=F(111,10)and 0<=g<=F(37,20)and eta>0,'extended sixth LOW scope')
 if M<=5:
  z=6*(M-1)+(10-2*M)*g-6*g*g+g**3 if 10-2*M-12*g+3*g*g>=0 else 6*(M-1)+(10-2*M)**2/(4*(6-g))
 else:z=6*(M-1)+(2*M-10)**2/24
 r0=max(RADIUS,2*g)
 need(r0>=RADIUS and r0>=2*g and r0>g,'actual-radius Pearson scope')
 if M<=5:
  tg=min(g,(10-2*M)/(2*(r0-g)))
  zr=r0*(M-1)+(10-2*M)*tg-(r0-g)*tg*tg
 else:
  tg=min(g,(2*M-10)/(2*r0))
  zr=r0*(M-1)+(2*M-10)*tg-r0*tg*tg
 z=min(z,zr)
 z=min(z,eta+10*g)/120;a=max(F(2),M-3)/24
 e=RADIUS*eta/720+g*g/72+(F(1,2)+g*g/144)**3/5;b=a+z/2+e/4
 a0=F(n-1,2*n);b0=(45-M)/96*(1-F(2,n))
 c0=roots(F(22,7)/(16*a0**3))[1];c1=c0/2
 need(0<b0<F(1,2)and (F(1,2)+g*g/144)/4<F(1,6),'sixth remainder and damping')
 need(g<2 and 6-2*g>0,'Pearson endpoint domain')
 return c0*z+c1*a*g+F(251,17280)*g**3,c0*a+F(251,4800)*g*g,e/(2*a0*a0)+b*b/(2*b0**3)
def score_cap(r):
 need(r>=1,'score cap moment domain')
 return min(F(469,1000),F(3031,10000)*(1+F(323,500)/r),F(1661,5000)*(1+F(429,1000)/r))
@lru_cache(maxsize=32768)
def negative_gap_coefficient(radius,rho_lower):
 """Exact interval bound on the radius-dependent negative-gap integral."""
 need(1<=rho_lower<=radius<=6,'negative gap domain')
 const=rho_lower**3*(2*radius-rho_lower)/12
 vertex=2*(radius+rho_lower)/3;peak=F(0)
 for i in range(64):
  l=rho_lower+(radius-rho_lower)*F(i,64)
  u=rho_lower+(radius-rho_lower)*F(i+1,64)
  x=max(l,min(u,vertex))
  val=-x*x/4+(radius+rho_lower)*x/3-radius*rho_lower/2+const/(l*l)
  peak=max(peak,val)
 return min(F(5,2),peak)
def initial_cell(n,lo,hi,previous,kind,endpoint,defect=None,phase_rebate=False,score_floor=F(819,2000),own_cap=F(469,1000)):
 need(1<=lo<hi<=F(37,20),'complete rho cell')
 need(kind in('universal','gap'),'initial event kind')
 d=None if previous is None else F(15000)*previous/(997*n)
 if defect is not None:d=defect
 if kind=='gap':
  need(d is not None and 0<d<2,'proved generic actual-gap domain')
  rw=roots(F(37,10)*d)[1];hh=roots(6+2*SU)[1]*roots(12+F(37,10)*d)[1]/6+rw/(3*roots(6+2*SL)[0])
  top=max(hh,((2*roots(SU+1)[1]-roots(SL-1)[0])*hh+3*rw)/roots(6+2*SL)[0]);alpha=top/6
  need(alpha<3,'outer gap J coefficient')
  rcap=min(F(37,20),(3+d)/(SL-1));ea=1/(2*hi*hi)
  need(hi<=rcap,'same-cell opposite-sign probability')
 M=min(F(111,10),RADIUS*hi,1+K4*(hi-1))
 if kind=='gap':M=min(M,hh*hi+RADIUS*d/2)
 g=min(F(37,20),hi,roots(M-1)[1])
 eta=min(RADIUS*M,1+K5*(hi-1))
 if kind=='gap':eta=min(eta,hh*hh*hi+RADIUS**2*d/2)
 l0,lh,l2=sixth(n,M,g,eta);hc=universal_high(n,M)
 if kind=='gap':hc=min(hc,high(n,ea,2/ea,roots(2-d)[0],M,F(1,8))[0])
 kf=F(16,25)*(l0+hc+l2/roots(F(n))[0]);slope=F(16,25)*lh
 beta=roots((hi*roots(hi*hi+8)[1]-hi*hi-2)/2)[1]
 radial=RADIUS*(RADIUS+2-F(3,2)*lo)/(RADIUS+F(1,2))
 need(radial>=F(31,40),'radial negative part dominated')
 knew=3*hi*beta+radial*(hi-1)
 if kind=='universal':kold=6*hi-F(3,2)*hi*hi+3*beta
 else:
  gl=(F(79,25)*lo-3-d,F(79,25)*hi-3-d)
  kp=M+3*beta-F(3,2)*min(r*z for r in(lo,hi)for z in gl)
  km=3*hi+3*beta+max((F(3,2)*r-3)*z for r in(lo,hi)for z in gl);kold=max(kp,km)
 kradius=RADIUS*hi/2+max(abs(RADIUS/2-F(3,2)*t)for t in(lo,hi))*g+3*beta
 k=min(knew,kold,kradius);diff=2*hi if d is None else (1-F(79,25))*lo+3+d
 ngap=negative_gap_coefficient(RADIUS,lo)
 A=min(F(3,2)*beta*(2*hi+1)+F(3,2)*ngap*diff+F(3,8)*hi*hi*(hi+1)+F(8,27)*hi**3-lo/2,F(3,2)*beta*(2*hi+1)+2*hi*M-lo/2)
 j=3*(hi+1)if kind=='universal'else alpha*(hi+1)+(3-alpha)*d/2
 hh=min(F(2,5)*j+(F(2,5)*max(F(2),M-3)/6 if kind=='universal'else F(2,5)*max(F(2),M-3)/6),F(2,5)*max(F(1,2),F(2,3)*M-F(1,2)))
 need(endpoint in('lower','upper'),'continuous-score endpoint')
 cl,cu=(score_floor,score_floor)if endpoint=='lower'else(max(score_floor,min(own_cap,score_cap(hi))),max(score_floor,min(own_cap,score_cap(lo))))
 linear=cu*k+hh+slope
 if d is not None:
  gamma_lower=max(-g,SL*lo-3-d)
  if gamma_lower>g:return F(-1)
  if gamma_lower>=0:
   # Each sign's Cauchy moment inequality constrains beta jointly with gamma.
   difference=max(F(0),hi-gamma_lower)
   ba,bb=-beta,beta
   if (1-beta)**3>(1+beta)*difference*difference:return F(-1)
   for _ in range(36):
    bm=(ba+bb)/2
    if (1-bm)**3>(1+bm)*difference*difference:ba=bm
    else:bb=bm
   beta_lower=ba
   need(-1<beta_lower<=beta<1,'signed moment beta interval')
   # Fourth moment Cauchy on each sign, retaining the gamma cancellation.
   gamma_star=max(gamma_lower,min(g,F(3,2)*hi*(1+beta)-lo-RADIUS*(1+beta)/2))
   klo=(lo+gamma_star)**2/(2*(1+beta))-RADIUS*(hi-gamma_star)/2-3*beta-F(3,2)*hi*gamma_star
   candidate=[gamma_lower,g,max(gamma_lower,min(g,lo)),max(gamma_lower,min(g,lo+(RADIUS/2-F(3,2)*lo)*(1-beta_lower)))]
   khi=max(RADIUS*(hi+x)/2-max(F(0),lo-x)**2/(2*(1-beta_lower))-3*beta_lower-F(3,2)*lo*x for x in candidate)
   klo=max(-k,klo);khi=min(k,khi);need(klo<=khi,'signed fourth moment intersection')
   ph=PHI*(1-F(5,2)*previous/n)
   signed_linear=max(abs(c*x+v*u)for c in(cl,cu)for x in(klo,khi)for v in(ph,F(2,5))for u in(-F(1,2),F(2,3)*M-F(1,2)))+slope
   linear=min(linear,signed_linear)
   if kind=='gap'and beta_lower>0:
    abeta=(1+beta_lower*beta_lower)**2/(2*hi*hi)
    hbeta=high(n,abeta,2/abeta,roots(2-d)[0],M,F(1,8))[0]
    hc=min(hc,hbeta);kf=F(16,25)*(l0+hc+l2/roots(F(n))[0])
 if d is None:q=cl*lo-g/5
 else:
  phi=PHI*(1-F(5,2)*previous/n);need(phi>0,'initial feedback density')
  q=cl*lo+phi*(F(79,25)*lo-3-d)/2-(F(2,5)-phi)*max(d-F(4,25),F(0))/2
 q=max(q,cl*lo-g/5)
 if phase_rebate:
  need(previous is not None and d is not None,'phase rebate prior raw ceiling')
  efloor=1-F(5,2)*previous/n
  coefficient=F(819,2000)*lo-F(1,15)*d
  need(efloor>0 and coefficient>0,'phase rebate positive coefficient')
  q+=efloor*coefficient/2
 need(q>0 and k>=0 and A>0,'initial signed envelope domain')
 return kf+cu*A+linear*linear/(4*q)

def general_geometry(d,steps=24):
 need(0<d<=F(7,10),'extended general-geometry candidate scope')
 need(F(147,100)**2<SL-1 and F(51,25)**2<SL+1 and F(88,25)**2>6+2*SU,'initial endpoint constants')
 h,w=roots(2-d)[0],roots(F(37,10)*d)[1]
 al=down((F(147,100)*h-w)/F(88,25));bl=down((F(51,25)*h-w)/F(88,25));need(al>0 and bl>0,'positive inner endpoints')
 theta=F(1);trace=[]
 for _ in range(steps):
  theta=min(theta,up(d/(F(29,5)*min(F(104,25)*al,F(54,25)*bl))))
  need(0<theta<1,'general variance domain')
  rad=roots(d/(F(616,25)*(1-theta)**2))[1];pl=(4-SU)/2-rad;pu=(4-SL)/2+rad
  need(0<pl<pu<1,'general probability domain')
  amin=roots((1-theta)*pl/(1-pl))[0];bmin=roots((1-theta)*(1-pu)/pu)[0]
  al=max(al,down(amin-d/(2*(1-pu)*F(179,25)*al*al)));bl=max(bl,down(bmin-d/(2*pl*F(129,25)*bl*bl)))
  trace.append((al,bl,theta,pl,pu))
 return dict(al=al,bl=bl,theta=theta,pl=pl,pu=pu,trace=trace)
def general_cell(d,l,u,glob,steps=8):
 need(0<l<u<1,'actual p cell')
 al,bl,theta=glob['al'],glob['bl'],glob['theta'];dist=max(F(0),(4-SU)/2-u,l-(4-SL)/2);trace=[]
 su=max(l*(1-l),u*(1-u),F(1,4)if l<=F(1,2)<=u else F(0))
 def binary_charge(t):return (6+2*SL)*roots((1-t)**3)[0]/roots(su)[1]*dist*dist
 for _ in range(steps):
  residual=d-binary_charge(theta)
  if residual<0:return None
  coefficient=min(3*(SL+1)*bl,3*(SL+3)*al);need(coefficient>0,'joint variance coefficient')
  theta=min(theta,up(residual/coefficient))
  amin=roots((1-theta)*l/(1-l))[0];bmin=roots((1-theta)*(1-u)/u)[0]
  al=max(al,down(amin-d/(2*(1-u)*F(179,25)*al*al)));bl=max(bl,down(bmin-d/(2*l*F(129,25)*bl*bl)))
  ml=roots((1-theta)*min(l*(1-l),u*(1-u)))[0]
  shift=residual/(6*ml*(al+bl));need(ml>0,'joint endpoint shift divisor')
  al=max(al,down(amin-shift));bl=max(bl,down(bmin-shift))
  trace.append((al,bl,theta,coefficient))
 s=min(l*(1-l),u*(1-u));su=max(l*(1-l),u*(1-u),F(1,4)if l<=F(1,2)<=u else F(0))
 amax=roots(u/(1-u))[1];bmax=roots((1-l)/l)[1];vmax=max(amax,bmax);m=roots((1-theta)*s)[0]
 rq=roots((1-2*s)**2/s)[1];gq=max(roots((1-2*t)**2/(t*(1-t)))[1]for t in(l,u))
 l3=RADIUS+2*vmax;l4=RADIUS**2+2*RADIUS*vmax+3*vmax*vmax;rho=min(F(37,20),up(rq+theta*(l3-rq)))
 bbase=max(abs(1-2*l),abs(1-2*u));beta=up(bbase+(1-bbase)*theta)
 M=up(min(1+K4*(rho-1),(1-theta)**2*(1/s-3)+l4*theta));g=min(F(37,20),up(gq+theta*(l3-gq)),roots(M-1)[1])
 eq=rq*(1-4*s+2*s*s)/(s*(1-2*s));l5=RADIUS**3+2*RADIUS**2*vmax+3*RADIUS*vmax*vmax+4*vmax**3;eta=up(min(RADIUS*M,(1-theta)**2*eq+l5*theta))
 need(l3>rq and l3>gq and l4>2*(1/s-3)and l5>2*eq,'cell moment monotonicity')
 need(0<al<=amax and 0<bl<=bmax and 1<=M<=F(111,10),'actual central rectangle')
 v=1-theta
 if v>F(2,3):
  def K(p,w):return (1-2*p)*((F(3,2)*w**3-w*w)/(p*(1-p))-3*w**3+w*w+3*w)
  # K decreases in p; its inner bracket increases in w for w>=2/3.
  need(F(3,2)*v**3-v*v>=0 and -3*v**3+v*v+3*v>0,'K probability derivative')
  need(9*v*v-6*v+3>0,'K variance derivative lower bound')
  err=theta*(l4+3+F(3,2)*l3*(rho+gq));klo=-max(K(l,v),K(l,F(1)))-err;khi=-min(K(u,v),K(u,F(1)))+err
  if 0<l<u<F(1,2)and 3*min(al,bl)>=F(3,2)*rq:
   low,high=signed_k_error(l,u,al,bl,theta,rho)
   klo=max(klo,-max(K(l,v),K(l,F(1)))+low);khi=min(khi,-min(K(u,v),K(u,F(1)))+high)
   need(klo<=khi,'signed conditional K intersection')
 else:
  km=M+3*beta+F(3,2)*rho*g;klo=-km;khi=km
 P1=lambda a,b:b**3/3+a*b*b/2-a**3/6;P2=lambda a,b:b**4/4+a*b**3/3-a**4/12
 p1=min(P1(al,bl),P1(amax,bl));p2=min(P2(al,bl),P2(amax,bl))
 residual=d-binary_charge(theta)
 if residual<0:return None
 coefficient=min(3*(SL+1)*bl,3*(SL+3)*al)
 Tupper=residual*max(vmax/(3*(al+bl)),l3/coefficient)
 douter=min(d,(SU+1)*Tupper)
 m4lower=max(F(1),(1-theta)**2*(1/su-3))
 etalower=(1-theta)**2*roots(1-theta)[0]*(1-4*su+2*su*su)/(su*roots(su)[1])
 jc=(m if p2>=0 else roots(su)[1])*p2;jlo=(m if p1>=0 else roots(su)[1])*p1-RADIUS/F(2)/(SL+1)*douter
 j0=max(F(1,3),(2-3*l)/(6*l*(1-l)));jhi=j0+RADIUS*douter/4
 return dict(al=al,bl=bl,theta=theta,pl=l,pu=u,M=M,g=g,Rho=rho,Beta=beta,eta=eta,klo=klo,khi=khi,jc=jc,j0=j0,ulo=jlo+(m4lower-3)/6,uhi=jhi+(M-3)/6,douter=douter,etalower=etalower,event_a=2*s,l3=l3,l4=l4,gq=gq,trace=trace)
def central_bound(p,rho):
 l,u=p['pl'],p['pu'];s0=min(l*(1-l),u*(1-u));su=max(l*(1-l),u*(1-u),F(1,4)if l<=F(1,2)<=u else F(0))
 al,bl=p['al'],p['bl'];au=roots(u/(1-u))[1];bu=roots((1-l)/l)[1]
 ml=roots((1-p['theta'])*s0)[0];mu=roots(su)[1];need(al<=au and bl<=bu,'central joint rectangle')
 coeff={(0,3):rho/3,(1,2):rho/2,(3,0):-rho/6,(0,4):-F(1,4),(1,3):-F(1,3),(4,0):F(1,12)}
 power={}
 for (i,j),c in coeff.items():
  for k in range(i+1):
   for h in range(j+1):power[k,h]=power.get((k,h),F(0))+c*comb(i,k)*comb(j,h)*al**(i-k)*(au-al)**k*bl**(j-h)*(bu-bl)**h
 out=[]
 for i in range(5):
  for j in range(5):
   z=sum((c*F(comb(i,k),comb(4,k))*F(comb(j,h),comb(4,h))for (k,h),c in power.items()if k<=i and h<=j),F(0));out.append((mu if z>=0 else ml)*z)
 return max(out)

def general_envelope(n,d,prev,p,cap=F(469,1000),score_floor=F(819,2000),phase_rebate=False,barrier=F(0)):
 M,g,eta=p['M'],p['g'],p['eta'];lc,lh,ln=sixth(n,M,g,eta)
 a=p['event_a'];d0=max(p['al']+p['bl'],roots(2-d)[0]);hh,_=high(n,a,2/a,d0,M,F(9,100))
 kf=F(16,25)*(lc+hh+ln/roots(F(n))[0]);slope=F(16,25)*lh;phi=PHI*(1-F(5,2)*prev/n);need(phi>0,'general density')
 vals=[]
 for c in(score_floor,cap):
  b=max(abs(c*k+ph*u)for k in(p['klo'],p['khi'])for ph in(phi,F(2,5))for u in(p['ulo'],p['uhi']))
  for rho in(F(1),p['Rho']):
   A=F(3,2)*p['Beta']*(rho+2*roots(max(p['pl']*(1-p['pl']),p['pu']*(1-p['pu']),F(1,4)if p['pl']<=F(1,2)<=p['pu']else F(0)))[1])+3*central_bound(p,rho)+F(3,8)*max(rho*rho/(SL-1),(RADIUS-rho)**2/(SL+1))*p['douter']+(rho/2-F(3,8))*M-rho/2+F(1,8)-max(F(0),p['etalower']-F(3,2)*M+F(1,2))/4+F(3,2)*p['Beta']*g
   q=c*rho+phi*(F(79,25)*rho-3-d)/2-(F(2,5)-phi)*max(d-F(4,25),F(0))/2;need(q>0,'general envelope divisor')
   if phase_rebate:
    efloor=1-F(5,2)*prev/n;coefficient=F(819,2000)*rho-F(1,15)*d
    need(efloor>0 and coefficient>0,'general phase rebate coefficient');q+=efloor*coefficient/2
   vals.append(kf+c*A+(b+slope)**2/(4*q)-barrier*rho)
 return vals

def paired(n,p,d):
 M,g=p['M'],p['g'];u=p['pu'];s=u*(1-u)
 need(0<p['pl']<u<F(1,2),'paired signed probability scope')
 ss=p['pl']*(1-p['pl']);rBmax=roots((1-2*ss)**2/ss)[1]
 need(3*min(p['al'],p['bl'])>=F(3,2)*rBmax,'actual rho variance reserve')
 rmin=max(F(1),roots((1-2*s)**2/s)[0]);gl=max(F(0),SL*rmin-3-d)
 need(1<=M<=2 and 0<=gl<=g<=1 and M-1-gl*gl>=0,'paired actual moment domain')
 need(RADIUS>g,'radius Pearson quadratic denominator')
 tstar=min(g,(10-2*M)/(2*(RADIUS-g)))
 sig=RADIUS*(M-1)+(10-2*M)*tstar-(RADIUS-g)*tstar*tstar
 Z=min(sig,p['eta']+10*g)/120
 zl=max(-Z,(8*gl-gl**3-(RADIUS+2*gl)*(M-1-gl*gl))/120);zu=Z;cl=(3-M)*gl/144;cu=(2-gl*gl)*g/144
 if 3*g*g<=2:cu=min(cu,(2*g-g**3)/144)
 need(zl<=zu and 0<=cl<=cu,'paired coefficient rectangle')
 I=roots(F(11,7))[1];fac=F(n,n-1)*roots(F(n,n-1))[1]
 def J(z,c):
  if z<=0:return I*(-z+3*c)
  if c==0:return I*z
  old=I*abs(z-3*c)+6*roots(c*z)[1]*exphi(z/(2*c))
  x=z/c;depth=11 if x>=3 else 12;den=F(1)
  for j in range(depth,0,-1):den=1+F(j)/(x*den)
  scaled_mills=1/den;coefficient=6+2*(3-x)*scaled_mills/x
  need(coefficient>0,'Mills cancellation coefficient')
  signed_gaussian=(I if z>=3*c else roots(F(333,212))[0])*(z-3*c)
  improved=signed_gaussian+roots(c*z)[1]*coefficient*exphi(x/2)
  need(improved>=0,'nonnegative cancellation norm bound')
  return min(old,improved)
 aa=(2-gl*gl)/24;lc=fac*max(J(z,c)for z in(zl,zu)for c in(cl,cu))+fac*I/(n-1)*(F(35,48)*aa*g**3+F(35,24)*Z*g*g)+F(251,17280)*g**3
 lh=fac*I*(aa+F(5,2)*Z*g/(n-1))+F(251,4800)*g*g
 m6=min(RADIUS*p['eta'],1+3*g*g+g**4+(RADIUS**2+2*RADIUS*g+3*g*g+2)*(M-1-gl*gl));e=m6/720+g*g/72+(F(1,2)+g*g/144)**3/5;B=aa+Z/2+e/4
 a0=F(n-1,2*n);b0=F(43,96)*(1-F(2,n));l2=e/(2*a0*a0)+B*B/(2*b0**3)
 return lc,lh,l2,rmin
def late_geometry(d):
 need(0<d<=F(29,500),'late bridge domain')
 theta=F(20,261)*d;rad=roots(d/(F(616,25)*(1-theta)**2))[1]
 return dict(al=F(3,4),bl=F(21,20),theta=theta,pl=max(F(37,100),(4-SU)/2-rad),pu=min(F(47,100),(4-SL)/2+rad))
def late_envelope(n,d,previous,p,cap):
 lc,lh,l2,rmin=paired(n,p,d);M,g=p['M'],p['g'];a=p['event_a'];d0=max(p['al']+p['bl'],roots(2-d)[0])
 hh,_=high(n,a,2/a,d0,M,F(9,100));kf=F(212,333)*(lc+hh+l2/roots(F(n))[0]);slope=F(212,333)*lh
 phi=F(0)if previous is None else PHI*(1-F(5,2)*previous/n);need(phi>=0,'late density')
 rows=[]
 for c in(F(819,2000),cap):
  b=max(abs(c*k+ph*u)for k in(p['klo'],p['khi'])for ph in(phi,F(2,5))for u in(p['ulo'],p['uhi']))
  for rho in(rmin,p['Rho']):
   A=kf+c*(F(3,2)*p['Beta']*(rho+2*roots(max(p['pl']*(1-p['pl']),p['pu']*(1-p['pu']),F(1,4)if p['pl']<=F(1,2)<=p['pu']else F(0)))[1])+3*central_bound(p,rho)+F(3,8)*max(rho*rho/(SL-1),(RADIUS-rho)**2/(SL+1))*p['douter']+(rho/2-F(3,8))*M-rho/2+F(1,8)-max(F(0),p['etalower']-F(3,2)*M+F(1,2))/4+F(3,2)*p['Beta']*g)
   ff=b+slope;qq=c*rho+phi*(F(79,25)*rho-3-d)/2;need(qq>0,'late signed quadratic')
   value=A+ff*ff/(4*qq);rows.append((A,ff,qq,value,value/rmin))
 return rows

# Exact same-law conditional signed cancellation, used only in late geometry.
def quadratic_extrema(xl,xu,al,au,t):
 need(0<xl<=xu and 0<al<=au,'signed quadratic rectangle')
 def q(x,a):return x*x+2*a*x+3*a*a-3-F(3,2)*t*(x+2*a)
 def clip(x,l,u):return min(u,max(l,x))
 corners=[q(x,a)for x in(xl,xu)for a in(al,au)]
 values=corners[:]
 for x in(xl,xu):values.append(q(x,clip(t/2-x/3,al,au)))
 for a in(al,au):values.append(q(clip(3*t/4-a,xl,xu),a))
 if xl<=3*t/8<=xu and al<=3*t/8<=au:values.append(q(3*t/8,3*t/8))
 return min(values),max(corners)
def signed_k_error(l,u,al,bl,theta,rho):
 gvlo=roots((1-theta)**3*(1-2*u)**2/(u*(1-u)))[0]
 gvhi=roots((1-2*l)**2/(l*(1-l)))[1]
 rmin=roots((1-2*u*(1-u))**2/(u*(1-u)))[0]
 aplo=roots((1-theta)*(1-u)/u)[0];aphi=roots((1-l)/l)[1]
 amlo=roots((1-theta)*l/(1-l))[0];amhi=roots(u/(1-u))[1]
 poslo=quadratic_extrema(bl,RADIUS,aplo,aphi,rho+gvhi)[0]
 poshi=quadratic_extrema(bl,RADIUS,aplo,aphi,rmin+gvlo)[1]
 neglo=-quadratic_extrema(al,RADIUS,amlo,amhi,rmin-gvhi)[1]
 neghi=-quadratic_extrema(al,RADIUS,amlo,amhi,rho-gvlo)[0]
 return theta*min(F(0),poslo,neglo),theta*max(F(0),poshi,neghi)

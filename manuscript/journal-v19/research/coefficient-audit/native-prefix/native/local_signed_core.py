#!/usr/bin/env python3
"""Exact rational local signed-moment entry covers with full [0,1] p panels.
No target selection or file I/O. New HIGH_WINDOW50 scope; frozen barrier
kernels remain unchanged.

All covers use one common actual law. A fixed external acceptor supplies the
ordered invariants and named theorem; this module alone makes no cutoff claim.
"""
from fractions import Fraction as F
import kernel as k
import high_window_core
high_window_core.install(k)
ZERO=F(0);ONE=F(1);HALF=F(1,2)
def lo(x):return k.down(x)
def hi(x):return k.up(x)
def sl(x):return k.roots(x)[0]
def su(x):return k.roots(x)[1]
def pos(x):return max(ZERO,x)
def init(p):
 k.RADIUS=p['radius'];r=k.RADIUS
 k.K4=(r+1)**2/(r+HALF);k.K5=(r**3+2*r*r+3*r+F(3,2))/(r+HALF);k.constants()
 k.need(type(p['n'])is int and 3<=p['n']<=p['nmax'],'index band')
 k.need(0<=p['barrier']<3 and F('.4095')<=p['cap']<=F('.469'),'score scope')
 for x in p['grid']:k.need(type(x)is int and x>0,'positive integer cover grid')
def stage(p,raw=None,d=None):
 init(p);n,R,K,cap=p['n'],p['radius'],p['barrier'],p['cap'];nr,nb,ng,nm=p['grid']
 k.need((raw is None)==(d is None),'ordered raw and defect invariants')
 if raw is not None:k.need(0<raw<F(2,5)*n and 0<d<4,'feedback initialization')
 c0=F('.4095')+K/p['nmax'];rhomax=min(F('1.85'),F('.3031')*F('.646')/(c0-F('.3031')),F('.3322')*F('.429')/(c0-F('.3322')))
 peakR=F(-1);peakD=F(-1);active=excluded=0;reasons={}
 panels=[dict(pl=F(j,100),pu=F(j+1,100),raw=F(-1),D=F(-1),theta=ZERO,rho=ONE,beta=ZERO,H=ZERO,cells=0)for j in range(100)]
 moments=dict(rho=ONE,beta=ZERO,theta=ZERO,H=ZERO,pl=ONE,pu=ZERO)
 def drop(count,reason):
  nonlocal excluded
  excluded+=count;reasons[reason]=reasons.get(reason,0)+count
 for ir in range(nr):
  rl=1+(rhomax-1)*F(ir,nr);rh=1+(rhomax-1)*F(ir+1,nr)
  M=min(F('11.1'),R*rh,1+k.K4*(rh-1));eta=min(R*M,1+k.K5*(rh-1));ga=min(F('1.85'),rh,su(M-1))
  ba=su((rh*su(rh*rh+8)-rh*rh-2)/2);Gamma=k.negative_gap_coefficient(R,rl)
  k.need(0<ba<1,'signed beta cover')
  for ib in range(nb):
   bl=-ba+2*ba*F(ib,nb);bu=-ba+2*ba*F(ib+1,nb);bmin=ZERO if bl<=0<=bu else min(abs(bl),abs(bu))
   mU=HALF*min(su(1-bmin*bmin),min((R-rl+2*a+R*a*a)/(a*(2*R+a))for a in [F(j,10)for j in range(2,13)]))
   gl=max(-ga,sl((1+bl)**3/(1-bl))-rh);gu=min(ga,rh-sl((1-bu)**3/(1+bu)))
   if d is not None:gl=max(gl,k.SL*rl-6*mU-d)
   gl,gu=lo(gl),hi(gu)
   if gl>gu:drop(ng*nm,'empty signed third interval');continue
   for ig in range(ng):
    l=gl+(gu-gl)*F(ig,ng);h=gl+(gu-gl)*F(ig+1,ng)
    ds=[g-r*b for g in(l,h)for r in(rl,rh)for b in(bl,bu)];dist=max(ZERO,min(ds),-max(ds));den=1-bmin*bmin
    if rl*rl+dist*dist/den>M:drop(nm,'fourth projection');continue
    asl=[(1+bl)/2,(1-bu)/2];asu=[(1+bu)/2,(1-bl)/2]
    bsl=[pos((rl+l)/2),pos((rl-h)/2)];bsu=[(rh+h)/2,(rh-l)/2]
    if min(bsu)<=0:drop(nm,'positive third sign moments');continue
    ml=max((1+bmin*bmin)/(2*rh),*(a*a/b for a,b in zip(asl,bsu)))
    if ml>mU:drop(nm,'common first moment interval');continue
    DU=[R*a-b for a,b in zip(asu,bsl)]
    if min(DU)<0:drop(nm,'negative support deficit');continue
    def fmean(t):return 2*t+sum(pos(R*t-a)**2/z for a,z in zip(asu,DU)if z>0)
    if fmean(ml)>R:drop(nm,'sign probabilities exceed one');continue
    mu=mU
    if fmean(mu)>R:
     zl=ml
     for _ in range(32):
      zm=(zl+mu)/2
      if fmean(zm)>R:mu=zm
      else:zl=zm
    mlo,mhi=lo(ml),min(mU,hi(mu));k.need(0<mlo<=mhi,'rounded mean cover')
    for im in range(nm):
     ml=mlo+(mhi-mlo)*F(im,nm);mu=mlo+(mhi-mlo)*F(im+1,nm)
     denm=[R*mu-a for a in asl];DL=[pos(R*a-b)for a,b in zip(asl,bsu)]
     if min(denm)<0 or any(z==0 and q>0 for z,q in zip(denm,DL)):drop(1,'first support deficit');continue
     corrections=[q*q/z if z>0 else ZERO for q,z in zip(DL,denm)]
     c4u=[hi(R*b-q)for b,q in zip(bsu,corrections)];Mc=min(M,hi(R*rh-sum(corrections)))
     etac=min(eta,hi(R*Mc-sum(pos(R*b-c)**2/z for b,c,z in zip(bsl,c4u,DU)if z>0)))
     if min(c4u)<0 or Mc<1 or etac<1 or rl*rl+dist*dist/den>Mc:drop(1,'bounded-support moment feasibility');continue
     dlower=max(ZERO,k.SL*rl-h-6*mu)
     if d is not None and dlower>d:drop(1,'compulsory gap defect');continue
     g=min(max(abs(l),abs(h)),su(Mc-1));l0,lh,l2=k.sixth(n,Mc,g,etac);hc=k.universal_high(n,Mc)
     gap=d is not None and d<(k.SL-1)*rl
     if gap:
      pl=2*ml*ml/(1+bu);pu=1-2*ml*ml/(1-bl)
      if pl>pu:drop(1,'actual sign probability interval');continue
      k.need(0<pl<=pu<1,'event probability endpoints')
      event=max((1+bmin*bmin)**2/(2*rh*rh),2*min(pl*(1-pl),pu*(1-pu)))
      gap2=(rl-d/(k.SL-1))/mu;k.need(gap2>0,'central gap distance')
      mev=min(2/event,max((1+4*mu*mu+b)/(2*t)+(1+4*mu*mu-b)/(2*(1-t))for b in(bl,bu)for t in(pl,pu)))
      hc=min(hc,k.high(n,event,mev,sl(gap2),Mc,F(1,8))[0])
     kf=F(16,25)*(l0+hc+l2/sl(F(n)));slope=F(16,25)*lh
     Jh=min(rh+2*mu,((3+k.SU)*rh-l)/3);Jl=max(ZERO,((3+k.SL)*rl-h-d)/3)if d is not None else ZERO
     if Jl>Jh:drop(1,'actual gap mass interval');continue
     bj=F(3,2)*max(b*(J+ga)for b in(bl,bu)for J in(Jl,Jh)for ga in(l,h))
     cross=max(r*ga for r in(rl,rh)for ga in(l,h));crossmin=min(r*ga for r in(rl,rh)for ga in(l,h))
     kl=pos(rl+l)**2/(2*(1+bu))-R*(rh-l)/2-3*bu-F(3,2)*cross
     ku=R*(rh+h)/2-pos(rl-h)**2/(2*(1-bl))-3*bl-F(3,2)*crossmin
     c4lo=[b*b/a for b,a in zip(bsl,asu)]
     kl=max(kl,c4lo[0]-c4u[1]-3*bu-F(3,2)*cross);ku=min(ku,c4u[0]-c4lo[1]-3*bl-F(3,2)*crossmin)
     if kl>ku:drop(1,'signed fourth interval');continue
     penalty=max(dist**4/(4*rh*den*den),pos(rl+l)*pos(min(ds))**2/(8*(1+bu)**2)+pos(rl-h)*pos(-max(ds))**2/(8*(1-bl)**2))
     charge=F(3,2)*Gamma*(rh-l)+F(3,8)*rh*rh*Jh;ulo=-HALF;uhi=F(2,3)*Mc-HALF
     if gap:
      Au=min(R,asu[1]/ml);Bu=min(R,asu[0]/ml)
      def endpoint(v,b,wl,wu):
       if wl*b<=d:return ZERO
       z=(wu+6)*mu
       return (6*v+sl(36*v*v+4*z*(wl*b-d)))/(2*z)
      Al=endpoint(asl[1],bsl[1],k.SL+1,k.SU+1);Bl=endpoint(asl[0],bsl[0],k.SL-1,k.SU-1)
      if Al>Au or Bl>Bu:drop(1,'central endpoint rectangle');continue
      qm=max(ZERO,sl(k.SL+1)*Al-su(k.SU-1)*Bu,sl(k.SL-1)*Bl-su(k.SU+1)*Au)**2
      dlower=max(dlower,ml*qm);dout=d-ml*qm
      if dout<0:drop(1,'central asymmetry budget');continue
      def G(a,r):return r**4/12+r**3*a/6-r*a**3/6+a**4/12
      central=3*mu*max(G(Au,rl),G(Au,rh));kp=pos(rh-Bl)**2;km=(R-rl)**2
      tp=min(pos(bsu[0]-ml*Bl*Bl),dout/(k.SL-1));tm=min(pos(bsu[1]-ml*Al*Al),dout/(k.SL+1))
      outer=min(F(3,8)*max(kp/(k.SL-1),km/(k.SL+1))*dout,F(3,8)*(kp*tp+km*tm));charge=min(charge,central+outer)
      def P1(a,b):return b**3/3+a*b*b/2-a**3/6
      pcl=min(P1(Al,Bl),P1(Au,Bl));pcl*=ml if pcl>=0 else mu
      pch=P1(max(Al,min(Au,Bu)),Bu);pch*=mu if pch>=0 else ml
      m4l=max(rl*rl+dist*dist/den,sum(c4lo))
      ulo=max(ulo,pcl-R*tm/2+(m4l-3)/6);uhi=min(uhi,pch+R*tp/2+(Mc-3)/6)
      if ulo>uhi:drop(1,'signed integral interval');continue
     A=min(bj+charge+rh**3/4-rl/2-penalty,bj+2*rh*Mc-rl/2)
     phlo=ZERO if raw is None else k.PHI*(1-F(5,2)*raw/n);k.need(phlo>=0,'density floor')
     ccap=min(cap,k.score_cap(rl))
     if raw is not None:
      numerator=raw/n-k.PHI*(1-F(5,2)*raw/n)*dlower/6
      if numerator<0:drop(1,'nonnegative excess score');continue
      ccap=min(ccap,F('.40974')+numerator/rl)
      if ccap<c0:drop(1,'own score interval');continue
     vals=[];budgets=[];cellH=ZERO
     for c in(c0,ccap):
      linear=max(abs(c*kk+ph*u)for kk in(kl,ku)for ph in(phlo,F(2,5))for u in(ulo,uhi))+slope
      q=c*rl+min(ph*l/2 for ph in(phlo,F(2,5)));k.need(q>0,'signed phase quadratic')
      vals.append(kf+c*A+linear*linear/(4*q));qb=q
      if raw is not None:
       coeff=F('.4095')*rl-d/15;k.need(coeff>0,'conserved-phase coefficient');qb+=(1-F(5,2)*raw/n)*coeff/2
      budgets.append(kf+c*A+linear*linear/(4*qb)-K*rl)
      cellH=max(cellH,(linear+su(linear*linear+4*qb*max(ZERO,kf+c*A)))/(2*qb))
     peakR=max(peakR,max(vals));peakD=max(peakD,F(15000,997*n)*max(budgets));active+=1
     if gap:
      cellRaw=min(raw,max(vals));cellD=min(d,F(15000,997*n)*max(budgets))
      moments['rho']=max(moments['rho'],rh);moments['beta']=max(moments['beta'],abs(bl),abs(bu));moments['H']=max(moments['H'],cellH)
      moments['pl']=min(moments['pl'],pl);moments['pu']=max(moments['pu'],pu)
      for z in panels:
       ll,uu=max(pl,z['pl']),min(pu,z['pu'])
       if ll>uu:continue
       variance=max(ll*(1-ll),uu*(1-uu),F(1,4)if ll<=HALF<=uu else ZERO)
       theta=max(ZERO,1-ml*ml/variance)
       z['raw']=max(z['raw'],cellRaw);z['D']=max(z['D'],cellD);z['theta']=max(z['theta'],theta)
       z['rho']=max(z['rho'],rh);z['beta']=max(z['beta'],abs(bl),abs(bu));z['H']=max(z['H'],cellH);z['cells']+=1
       moments['theta']=max(moments['theta'],theta)
 k.need(active+excluded==nr*nb*ng*nm,'complete signed cover cardinality')
 return dict(R=peakR,D=peakD,active=active,excluded=excluded,reasons=reasons,total=nr*nb*ng*nm,panels=panels,moments=moments)

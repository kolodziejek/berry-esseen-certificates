"""Both-half Gaussian Taylor scalar and uniform noise-curvature upper bound.

Generalizes gaussian_scalar.py to 0 < pl < pu < 1 using the endpoint variance
minimum vmin = min(pl*(1-pl), pu*(1-pu)) proved in gaussian_endpoint.tex, and
adds the uniform noise-curvature upper bound M >= d²/dlambda² Phi(a/sqrt(D)).
"""
from fractions import Fraction as F
from math import factorial
from types import SimpleNamespace
import algebra as a
m=SimpleNamespace(need=a.need,norm=a.normal,normal=a.normal_lower)
def down(x,g=10**20):return F(x.numerator*g//x.denominator,g)

def up(x,g=10**20):return -down(-x,g)

def interval_mul(a,b):
 xs=[x*y for x in a for y in b];return min(xs),max(xs)

def gaussian(n,k,pl,pu,ul,uh,lam):
 """Power coefficients in p,u of a certified quadratic lower polynomial on 0<pl<pu<1."""
 m.need(type(n)is int and n>0 and type(k)is int and 0<pl<pu<1 and ul<uh and lam>=0,'explicit closed Gaussian domain')
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
 vmin=min(pl*(1-pl),pu*(1-pu));dmin=n*vmin+lam;smin=m.norm.root(dmin)[0];m.need(smin>0,'positive variance denominator')
 A=max(abs(F(k)+u-n*p)for p in(pl,pu)for u in(ul,uh));B=n*max(abs(1-2*pl),abs(1-2*pu))
 Z=A/smin;Zt=1/smin;Zp=n/smin+A*B/(2*dmin*smin)
 Zpp=n*(B+A)/(dmin*smin)+3*A*B*B/(4*dmin*dmin*smin);Zpt=B/(2*dmin*smin)
 Mpp=up(F(2,5)*(Z*Zp*Zp+Zpp),10**16);Mpt=up(F(2,5)*(Z*Zp*Zt+Zpt),10**16);Mtt=up(F(2,5)*Z*Zt*Zt,10**16)
 eta=du/dp;P=Mpp+Mpt*eta;T=Mtt+Mpt/eta;center=m.normal(a0,D0)
 # center+gp0(p-pc)+gt0(u-uc)-rounding-P(p-pc)^2/2-T(u-uc)^2/2.
 poly=[[center-gp0*pc-gt0*uc-rounding-P*pc*pc/2-T*uc*uc/2,gp0+P*pc,-P/2],[gt0+T*uc],[-T/2]]
 record={'lambda':str(lam),'center':[str(pc),str(uc)],'center_cdf_lower':str(center),'phi_interval':list(map(str,phi)),'gradient_p':list(map(str,gp)),'gradient_u':list(map(str,gt)),
  'rounding_budget':str(rounding),'absolute_hessian_bounds':list(map(str,(Mpp,Mpt,Mtt))),'eta':str(eta),'vmin':str(vmin),'dmin':str(dmin),'polynomial':[[str(z)for z in a]for a in poly]}
 return poly,record

def curvature(n,k,pl,pu,ul,uh,lo=F(0)):
 """Uniform upper bound on d²/dlambda² Phi((k+u-np)/sqrt(npq+lambda)) over [pl,pu]x[ul,uh]x[lo,infty)."""
 m.need(type(n)is int and n>0 and type(k)is int and 0<pl<pu<1 and ul<uh and lo>=0,'ordered curvature domain')
 amin=F(k)+ul-n*pu;amax=F(k)+uh-n*pl
 vmin=min(pl*(1-pl),pu*(1-pu));dmin=n*vmin+lo;sqrtlo=m.norm.root(dmin)[0]
 m.need(dmin>0 and sqrtlo>0 and sqrtlo*sqrtlo<=dmin,'positive directed denominator')
 m.need(min(amin,F(0))**2<=3*dmin,'negative numerator has nonpositive noise curvature')
 M=3*max(amax,F(0))*m.norm.PHI_HI/(4*dmin*dmin*sqrtlo)
 m.need(M>=0,'nonnegative uniform curvature upper bound')
 return M,dict(numerator=[str(amin),str(amax)],vmin=str(vmin),D_lower=str(dmin),sqrt_D_lower=str(sqrtlo),phi_zero_upper=str(m.norm.PHI_HI),gaussian_noise_curvature_upper=str(M))

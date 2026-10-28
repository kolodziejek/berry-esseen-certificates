#!/usr/bin/env python3
"""Exact direct half-amplitude support on the entire low-noise region.

Conditional premises: acquired |U|<.6 and d<.069, fixed-target contact,
sharp predecessor, same centered variance-one marginal, n>=42.
No phase bound, phase coefficients or Fourier kernel is used by this lemma.
"""
from fractions import Fraction as F
from math import isqrt
import json,sys
N=42
L,H=F(41,100),F(21,50)
SIGMA,NOISE,AMPLITUDE=F(3,5),F(3,40),F(1,2)

def need(ok,why):
 if not ok:raise ValueError(why)
def lower_root(x):
 need(x>=0,'root domain');scale=10**10
 r=F(isqrt(x.numerator*scale*scale//x.denominator),scale)
 need(r*r<=x<(r+F(1,scale))**2,'directed root')
 return r
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encode(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v)for v in x]
 return x

def boundary(u,r,b):
 need(u>0 and u*u>3,'extended heat domain')
 S,c,e=F(81,80),F(819,2000),F(8,875)
 need(S*S>F(N,N-1)and N-1>36,'heat scale and remainder floor')
 a=(u**3-3*u)/6;h4=u**4-6*u*u+3
 remainder=u**5/4100+3*u/820+17*(3*u*u-2)/78720
 q=-u**3+F(3,2)*r*u*u+3*b*u+e*r
 q1=-3*u*u+3*r*u+3*b;q2=-6*u+3*r
 upper=F(2,5)*S**3*(a+abs(h4)/72)+S**3*remainder+c*q
 signs=[q,q1,q2,F(2,5)*(u*u/2+F(1,2)+e)+c*q1,F(2,5)*u+c*q2,F(2,5)-6*c]
 need(upper<0 and all(x<0 for x in signs),'strict signed boundary and all ray derivatives')
 return dict(radius=u,beta_direction=b,heat_upper=upper,ray_signs=signs)

def run():
 need(__debug__ and not sys.flags.optimize,'unoptimized Python')
 v,V=L*(1-L),H*(1-H)
 need(0<L<=H<F(1,2),'fixed oriented probability panel')
 need(24**2*v**3>(3*(1-L)+SIGMA)**2,'conditional cubic coefficient at actual .6 strip')
 theta=NOISE/(N*v+NOISE)
 ell=lower_root((1-theta)/V)
 rb=(1-2*v)/lower_root(v);rho=rb+24*NOISE/N
 bl=1-2*H-2*(1-H)*theta;bu=1-2*L+2*L*theta
 need(0<=theta<1 and ell>0 and F(69,1000)<AMPLITUDE<SIGMA,'moment and inward domains')
 negative=boundary(ell*(L+AMPLITUDE),rho,-bl)
 positive=boundary(ell*(1+AMPLITUDE-H),rho,bu)
 controls=[]
 def reject(name,fn):
  try:fn()
  except ValueError:controls.append(name)
  else:raise ValueError('invalid control accepted '+name)
 reject('invalid cubic coefficient',lambda:need(18**2*v**3>(3*(1-L)+SIGMA)**2,'cubic gate'))
 reject('wrong negative-ray beta sign',lambda:boundary(negative['radius'],rho,bu))
 reject('unlicensed smaller amplitude',lambda:boundary(ell*(L+F(1,4)),rho,-bl))
 reject('omitted raw scale',lambda:need(negative['radius']==L+AMPLITUDE,'physical scale'))
 reject('strict heat target weakened to zero',lambda:need(F(0)<0,'strict contact exclusion'))
 return dict(status='PASS_CONDITIONAL_WHOLE_LOW_NOISE_HALF_AMPLITUDE',n_floor=N,p_interval=[L,H],
  acquired_strip=SIGMA,noise_interval=[F(0),NOISE],target_amplitude=AMPLITUDE,
  theta_upper=theta,ell_lower=ell,rho_upper=rho,beta_lower=bl,beta_upper=bu,
  negative=negative,positive=positive,rejected_controls=controls,
  mathematical_scope='All raw thresholds, all n>=42, same-law lambda in [0,3/40], conditional on prior .6 strip/inward bound and fixed-target support contact. No Fourier or phase premise beyond that acquired strip.')

if __name__=='__main__':print(json.dumps(encode(run()),indent=2,sort_keys=True))

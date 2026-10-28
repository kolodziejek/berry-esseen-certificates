#!/usr/bin/env python3
"""Independent exact half-amplitude test on thirteen closed probability panels.

Conditional input: actual centered variance-one law, n>=42, fixed-target
support contact with sharp predecessor, |U|<=3/5, inward displacement<.072.
No project code, phase export, Fourier kernel or numerical input is imported.
"""
from fractions import Fraction as F
from math import isqrt
import json,sys
N=42
NOISE=F(3,40)
SIGMA=F(3,5)
AMPLITUDE=F(1,2)
S=F(81,80)
CLOW=F(819,2000)
E=F(8,875)
def require(condition,message):
    if not condition:raise ValueError(message)
def root_lower(x):
    require(x>=0,'nonnegative radicand')
    scale=10**12
    value=F(isqrt(x.numerator*scale*scale//x.denominator),scale)
    require(value*value<=x<(value+F(1,scale))**2,'directed square root')
    return value
def variance_bounds(l,u):
    require(0<l<=u<1,'ordered probability interval')
    endpoints=[l*(1-l),u*(1-u)]
    return min(endpoints),max(endpoints+[F(1,4)]if l<=F(1,2)<=u else endpoints)
def evaluate(radius,rho,beta):
    require(radius>0 and radius*radius>3,'positive cubic heat domain')
    cubic=(radius**3-3*radius)/6
    quartic=radius**4-6*radius*radius+3
    error=radius**5/4100+3*radius/820+17*(3*radius*radius-2)/78720
    q=[-radius**3+F(3,2)*rho*radius**2+3*beta*radius+E*rho,
       -3*radius**2+3*rho*radius+3*beta,-6*radius+3*rho]
    derivative=[F(2,5)*(radius**2/2+F(1,2)+E)+CLOW*q[1],
                F(2,5)*radius+CLOW*q[2],F(2,5)-6*CLOW]
    upper=S**3*(F(2,5)*(cubic+abs(quartic)/72)+error)+CLOW*q[0]
    require(upper<0,'strict boundary contact exclusion')
    require(all(x<0 for x in q+derivative),'six whole-ray signs')
    return dict(radius=radius,beta_direction=beta,contact_upper=upper,Q_derivatives=q,L_derivatives=derivative)
def one(index):
    l,u=F(index,100),F(index+1,100)
    v,V=variance_bounds(l,u)
    coefficient=3*max(u,1-l)+SIGMA
    require(24**2*v**3>coefficient**2,'common cubic coefficient on both orientations')
    theta=NOISE/(N*v+NOISE)
    ell=root_lower((1-theta)/V)
    rho=(1-2*v)/root_lower(v)+24*NOISE/N
    low=1-2*u-2*(1-u)*theta
    high=1-2*l+2*l*theta
    require(0<=theta<1 and low<=high,'moment domains')
    negative=evaluate(ell*(l+AMPLITUDE),rho,-low)
    positive=evaluate(ell*(1+AMPLITUDE-u),rho,high)
    return dict(index=index,p=[l,u],vmin=v,vmax=V,cubic_numerator_upper=coefficient,
                cubic_squared_margin=24**2*v**3-coefficient**2,theta_upper=theta,
                ell_lower=ell,rho_upper=rho,beta=[low,high],negative=negative,positive=positive)
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return{k:encode(v)for k,v in x.items()}
    if isinstance(x,list):return[encode(v)for v in x]
    return x
def main():
    require(__debug__ and not sys.flags.optimize,'unoptimized Python')
    require(S*S>F(N,N-1) and N-1>36,'uniform heat scale')
    require(F(72,1000)<AMPLITUDE<SIGMA,'prior inward displacement bound')
    rows=[one(i)for i in range(40,53)]
    require(rows[0]['p'][0]==F(2,5) and rows[-1]['p'][1]==F(53,100),'full endpoint range')
    require(all(a['p'][1]==b['p'][0]for a,b in zip(rows,rows[1:])),'no missing closed seam')
    controls=[]
    def reject(name,fn):
        try:fn()
        except ValueError:controls.append(name)
        else:raise ValueError('negative control accepted '+name)
    reject('insufficient uniform cubic coefficient18',lambda:require(18**2*F(6,25)**3>(3*F(3,5)+SIGMA)**2,'cubic coefficient'))
    reject('wrong interior maximum of pq',lambda:require(variance_bounds(F(49,100),F(51,100))[1]==F(2499,10000),'interior maximum'))
    row=rows[1]
    reject('wrong beta on reflected support ray',lambda:evaluate(row['negative']['radius'],row['rho_upper'],row['beta'][1]))
    reject('unlicensed quarter-amplitude heat radius',lambda:evaluate(row['ell_lower']*(row['p'][0]+F(1,4)),row['rho_upper'],-row['beta'][0]))
    reject('omitted raw scale',lambda:require(row['negative']['radius']==row['p'][0]+AMPLITUDE,'physical radius'))
    reject('non-strict contact boundary',lambda:require(F(0)<0,'strict negativity'))
    # The same elementary sign calculation gives a concrete above-half control.
    law=[(F(-26,25),F(12,25)),(F(1,2),F(52,6977)),(F(7226,7475),F(89401,174425))]
    require(sum(w for x,w in law)==1 and sum(x*w for x,w in law)==0 and sum(x*x*w for x,w in law)==1,'actual-law control')
    p=sum(w for x,w in law if x>0);m=sum(x*w for x,w in law if x>0)
    theta=1-m*m/(p*(1-p));beta=sum(x*abs(x)*w for x,w in law)
    require(1-2*p-2*(1-p)*theta<=beta<=1-2*p+2*p*theta,'both-orientation beta bound')
    reject('incorrect plus-theta shortcut above one half',lambda:require(beta<=1-2*p+theta,'actual-law sign control'))
    boundary=[(r['index'],side,r[side]['contact_upper'])for r in rows for side in ('negative','positive')]
    worst=max(boundary,key=lambda z:z[2])
    print(json.dumps(encode(dict(status='PASS_INDEPENDENT_THIRTEEN_PANEL_LOW_NOISE',panels=rows,
      p_range=[F(2,5),F(53,100)],noise_range=[F(0),NOISE],target_amplitude=AMPLITUDE,
      strict_boundaries=len(boundary),strict_continuation_gates=6*len(boundary),worst_boundary=list(worst),
      rejected_controls=controls,scope='All raw thresholds and actual n>=42; conditional on sharp fixed-target contact and prior .6 strip/inward bound. No full-noise or other-panel confinement claim.')),indent=2,sort_keys=True))
if __name__=='__main__':main()

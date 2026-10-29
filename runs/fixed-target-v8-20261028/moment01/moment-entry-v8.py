#!/usr/bin/env python3
"""All30 probability panels: elementary exact moment and actual-gap feedback.

No Fourier or certificate module is imported. The accepted v7 input and
the stated same-law weighted gap inequality are explicit mathematical premises.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json,sys

HERE=Path(__file__).resolve().parent
INPUT_SHA='61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae'
SL,SU=F('3.162277660'),F('3.162277661')
N,STEPS,SCALE=42,8,10**10

def need(v,s):
    if not v:raise ValueError(s)
def floor(x):return F(x.numerator*SCALE//x.denominator,SCALE)
def ceil(x):return -floor(-x)
def sqlo(x):
    need(x>=0,'nonnegative root');v=F(isqrt(x.numerator*SCALE*SCALE//x.denominator),SCALE)
    need(v*v<=x<(v+F(1,SCALE))**2,'outward root');return v
def squp(x):return sqlo(x)+F(1,SCALE)
def unique(pairs):
    d={}
    for k,v in pairs:need(k not in d,'duplicate key');d[k]=v
    return d
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return{k:encode(v)for k,v in x.items()}
    if isinstance(x,(tuple,list)):return[encode(v)for v in x]
    return x

def variance_range(l,u):
    need(0<l<=u<1,'closed probability interval')
    return min(l*(1-l),u*(1-u)),max(l*(1-l),u*(1-u),F(1,4)if l<=F(1,2)<=u else F(0))

def binary_floor(l,u,theta,vmax):
    need(0<=theta<1 and vmax>0,'binary floor domain')
    pstar_l,pstar_u=(4-SU)/2,(4-SL)/2
    distance=max(F(0),l-pstar_u,pstar_l-u)
    return floor((6+2*SL)*sqlo((1-theta)**3)*distance*distance/squp(vmax))

def costs(l,u,theta,A,B):
    abar=sqlo((1-theta)*l/(1-l));bbar=sqlo((1-theta)*(1-u)/u)
    return floor(min((SL-1)*(B+2*bbar)+6*B,(SL+1)*(A+2*abar)+6*A))

def panel(row,R):
    l,u,D,theta=[F(row[k])for k in ('pl','pu','D','theta')]
    need(0<=theta<1 and 0<D<SL-1,'actual central gap license')
    vmin,vmax=variance_range(l,u)
    au,bu=squp(u/(1-u)),squp((1-l)/l)
    AB=(SL-1-D)/3
    A,B=floor(AB/bu),floor(AB/au)
    g=floor(2*sqlo(AB*vmin));need(0<g<=1 and A>0 and B>0,'initial central geometry')
    d=ceil(1-g);trace=[]
    for j in range(STEPS):
        oldtheta,oldd=theta,d
        paid=binary_floor(l,u,theta,vmax);residual=D-paid
        if residual<0:return dict(index=row['index'],pl=l,pu=u,excluded=True,reason='binary floor exceeds D',step=j+1,binary_floor=paid,D=D,trace=trace)
        K=costs(l,u,theta,A,B);need(K>0,'positive noise coefficient')
        theta=min(theta,ceil(residual/K))
        paid=binary_floor(l,u,theta,vmax);residual=D-paid
        if residual<0:return dict(index=row['index'],pl=l,pu=u,excluded=True,reason='updated binary floor exceeds D',step=j+1,binary_floor=paid,D=D,trace=trace)
        ml,ell=sqlo((1-theta)*vmin),sqlo((1-theta)/vmax)
        need(ml>0 and ell>0 and g>0,'shift divisors')
        d=min(d,ceil(residual/(6*ml*ell*ell*g)))
        g=max(g,floor(1-d));A=max(A,floor(ell*max(F(0),l-d)));B=max(B,floor(ell*max(F(0),1-u-d)))
        need(0<=theta<=oldtheta and 0<=d<=oldd<1 and g<=1,'ordered elementary contraction')
        trace.append(dict(step=j+1,theta=theta,d=d,A=A,B=B,g=g,binary_floor=paid,residual=residual,noise_cost=K))
    K=costs(l,u,theta,A,B);paid=binary_floor(l,u,theta,vmax);residual=D-paid
    need(residual>=0 and K>0,'final joint resource')
    ell_l=sqlo((1-theta)/vmax);ell_u=squp(1/vmin)
    # General orientation: retain both tagged conditional-mean radii.
    L=R+2*max(au,bu)
    ratio=floor(min(SL-1+6*B/(R+2*bu),SL+1+6*A/(R+2*au)))
    need(ratio>0,'third moment price')
    rb=ceil((1-2*vmin)/sqlo(vmin));decay=F(3,2)*sqlo(1-theta)
    turnover=min(theta,residual/(ratio*L))
    rho=min(F(row['rho']),ceil(rb+max(F(0),L-decay*rb)*turnover))
    beta_l=max(-F(row['beta']),floor(1-2*u-2*(1-u)*theta))
    beta_u=min(F(row['beta']),ceil(1-2*l+2*l*theta))
    need(beta_l<=beta_u,'signed beta interval')
    displacement_intercept=ceil(residual/(6*(1-theta)*(A+B)))
    noise_intercept=ceil(N*vmax*residual/(K*(1-theta)))
    return dict(index=row['index'],pl=l,pu=u,excluded=False,D=D,theta=theta,d=d,A=A,B=B,g=g,
        rho=rho,beta_l=beta_l,beta_u=beta_u,ell_l=ell_l,ell_u=ell_u,
        lambda_upper=noise_intercept,joint_displacement_intercept=displacement_intercept,
        binary_floor=paid,residual=residual,noise_cost=K,third_moment_price=ratio,trace=trace)

def check_law(name,law):
    need(sum(w for x,w in law)==1 and all(w>0 for x,w in law),'law masses')
    need(sum(x*w for x,w in law)==0 and sum(x*x*w for x,w in law)==1,'standardized law')
    p=sum(w for x,w in law if x>0);q=1-p
    need(all(x!=0 for x,w in law),'actual control gap')
    m=sum(x*w for x,w in law if x>0);a,b=m/q,m/p
    A=min(-x for x,w in law if x<0);B=min(x for x,w in law if x>0)
    rho=sum(abs(x)**3*w for x,w in law);gamma=sum(x**3*w for x,w in law);beta=sum(x*abs(x)*w for x,w in law)
    theta=1-m*m/(p*q);DA,DB=a-A,b-B
    xs=sorted(x for x,w in law)
    J=sum(sum(x*w for x,w in law if x>=v)*(v-u)**2 for u,v in zip(xs,xs[1:]))
    # The exact algebraic lower inequality is affine in sigma: SL is enough
    # for this identity control, while the iteration uses the true nonnegative B0.
    D=(3+SL)*rho-gamma-3*J
    binary=m*((SL+1)*a*a+(SL-1)*b*b-6*a*b)
    shift=6*m*((A+B)*(DA+DB)+DA*DB)
    noise=sum(w*(x-(b if x>0 else -a))**2*((SL-1)*(x+2*b)+6*B if x>0 else (SL+1)*(-x+2*a)+6*A) for x,w in law)
    need(D>=binary+shift+noise,'same-law weighted gap cost')
    need(1-2*p-2*q*theta<=beta<=1-2*p+2*p*theta,'both-orientation beta bounds')
    return dict(name=name,p=p,theta=theta,beta=beta,cost_reserve=D-binary-shift-noise,
                invalid_half_interval_upper=1-2*p+theta)

def main():
    need(__debug__ and not sys.flags.optimize,'unoptimized interpreter')
    need(SL*SL<10<SU*SU,'sqrt10 enclosure')
    blob=(HERE/'moment-entry-v8-input.json').read_bytes();need(sha256(blob).hexdigest()==INPUT_SHA,'frozen accepted object')
    data=json.loads(blob,object_pairs_hook=unique)
    need(data['name']=='INITIAL42_FIXED_TARGET_COARSE_V7' and len(data['panels'])==100,'named fixed-target input')
    rows=[]
    for i,z in enumerate(data['panels']):
        need(F(z['pl'])==F(i,100) and F(z['pu'])==F(i+1,100),'ordered closed source cover')
        if z['cells']:rows.append(dict(index=i,**z))
    need([z['index']for z in rows]==list(range(24,54)),'all30 nonempty source panels')
    R=max(F(z['radius'])for z in data['steps'][-1]if z.get('active',0)>0)
    need(R==F(157,50),'global support from all surviving rho rows')
    outputs=[panel(z,R)for z in rows];active=[z for z in outputs if not z['excluded']]
    p=F(13,25);q=1-p;an=F(26,25);m=q*an;bp=m/p;second=(1-q*an*an)/p
    xp=F(1,2);yp=(second-xp*bp)/(bp-xp);w=(yp-bp)/(yp-xp)
    skew=[(-an,q),(xp,p*w),(yp,p*(1-w))]
    laws=[check_law('symmetric Bernoulli',[(-F(1),F(1,2)),(F(1),F(1,2))]),
          check_law('skew Bernoulli',[(-F(2,3),F(9,13)),(F(3,2),F(4,13))]),
          check_law('reflected skew Bernoulli',[(F(2,3),F(9,13)),(-F(3,2),F(4,13))]),
          check_law('symmetric four point',[(-F(2),F(1,10)),(-F(1,2),F(2,5)),(F(1,2),F(2,5)),(F(2),F(1,10))]),
          check_law('small distant atoms',[(-F(10),F(1,266)),(-F(1,2),F(66,133)),(F(1,2),F(66,133)),(F(10),F(1,266))]),
          check_law('p=.52 one-sided noise',skew)]
    need(laws[-1]['beta']>laws[-1]['invalid_half_interval_upper'],'actual-law counterexample to +Theta shortcut')
    controls=[]
    def reject(name,fn):
        try:fn()
        except ValueError:controls.append(name)
        else:raise ValueError('invalid control accepted '+name)
    reject('cross-half variance endpoint maximum',lambda:need(variance_range(F(49,100),F(51,100))[1]<=F(2499,10000),'interior maximum'))
    reject('half-interval beta upper above .5',lambda:need(laws[-1]['beta']<=laws[-1]['invalid_half_interval_upper'],'false beta upper'))
    reject('wrong weighted count normalization',lambda:need(N*F(1,10)<=F(1,10),'missing N'))
    reject('changing acquired input',lambda:need(sha256(blob+b' ').hexdigest()==INPUT_SHA,'input hash'))
    reject('claim every panel excluded',lambda:need(not active,'surviving panels'))
    summary=dict(initial_panels=len(rows),active_panels=len(active),excluded_panels=[z['index']for z in outputs if z['excluded']],
       p_lower=min(z['pl']for z in active),p_upper=max(z['pu']for z in active),
       theta=max(z['theta']for z in active),d=max(z['d']for z in active),rho=max(z['rho']for z in active),
       lambda_upper=max(z['lambda_upper']for z in active),ell_lower=min(z['ell_l']for z in active),ell_upper=max(z['ell_u']for z in active))
    print(json.dumps(encode(dict(status='PASS_CONDITIONAL_ALL_PANEL_MOMENT_CONTRACTION',input_sha256=INPUT_SHA,
      support=R,iterations=STEPS,summary=summary,panels=outputs,actual_law_controls=laws,
      positive_noise_counterexample_law=skew,rejected_controls=controls,
      limitations='Elementary consequence of accepted fixed-target entry and weighted gap inequality; no support-strip or count exclusion is claimed.')),indent=2,sort_keys=True))

if __name__=='__main__':main()

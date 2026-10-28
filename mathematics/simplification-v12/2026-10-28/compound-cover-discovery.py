"""Bounded floating exploration of CLOSED-box sufficient estimates.

This script chooses rational quartic/hinge candidates; it accepts no theorem.
The following exact checker will reconstruct every selected inequality.
"""
from math import exp,factorial,comb
import json,itertools

A=.6;d=.072;unit=.024;Xi=.924;cv=2.5;v=.24
K0=3.16;eta_hi=1/42

def centered_moment(T,w,y):
    mu=T*(1-w)/A**2;nu=T*w/d**2;K=y/unit+25*mu+3*nu
    pm=[1.];pn=[1.]
    for j in range(1,int(K//25)+1):pm.append(pm[-1]*mu/j)
    for k in range(1,int(K//3)+1):pn.append(pn[-1]*nu/k)
    deficit=0.
    for j in range(len(pm)):
      for k in range(int((K-25*j)//3)+1):
        deficit+=(K-25*j-3*k)**2*pm[j]*pn[k]
    full=625*mu+9*nu+(25*mu+3*nu-K)**2
    return max(0.,unit**2*(full-exp(-mu-nu)*deficit))

def tail_rest(lam,r,m=4):
    mu=2.5*lam/A**2
    return mu**(m+1)/(factorial(m+1)*(m*(1/A-1)+r/A+mu)**2*(1-mu/(m+2)))

def tails(box):
    l,L,rl,rh,wl,wh=box;D=Xi+rh
    T=L*(1+cv*(D+1)*eta_hi*wh)
    options=[(centered_moment(T,wl,y/200)/(1+rl-y/200)**2,y) for y in range(40,221,5) if y/200<1+rl]
    first,y=min(options)
    rest=tail_rest(L,rl)
    anchors=[]
    for i in [2,3]:
      mu=min(2.5*L,L*(1+cv*(D+i)*eta_hi))/A**2
      opts=[(mu**(j+1)/(factorial(j+1)*((i+rl)/A+mu-j)**2),j) for j in range(2,7) if (i+rl)/A+mu>j]
      val,j=min(opts);rest+=val;anchors.append(j)
    return first+rest,y,anchors

def bernstein4(coeff,lo,hi):
    q=[sum(coeff[k]*comb(k,j)*lo**(k-j)*(hi-lo)**j for k in range(j,5)) for j in range(5)]
    return [sum(q[j]*comb(i,j)/comb(4,j) for j in range(i+1)) for i in range(5)]

def bound(box,alpha,tail):
    l,L,rl,rh,wl,wh=box;D=Xi+rh
    Z=.625*D+.375+D**3/42
    mlo=2*.39886*(1-(D*D/(2*v)+Z)/42)
    R=1+max(0,.53+D-1)/(42*v-.6*max(0,D-1))
    P=(2*Xi*rh+rh*rh)/(2*v)+Z
    E=42*(exp(P/42)-1)
    M=5*alpha**4
    best=1e100;witness=None
    for lam,w,eta,m,s0,s1,x0,x1 in itertools.product([l,L],[wl,wh],[0.,eta_hi],[mlo,.85],[-1,1],[-1,1],[-A,d],[-d,A]):
      t0=lam*(1-w)*(1+s0*cv*Xi*eta);b0=lam*(1-w)*s0*cv*eta
      t1=lam*w*(1+s1*cv*Xi*eta);b1=lam*w*s1*cv*eta
      t=t0+t1;b=b0+b1
      coeff=[0.]*5
      for x,tt,bb in [(x0,t0,b0),(x1,t1,b1)]:
        c=3*alpha**2-x*x
        coeff[0]+=c*tt;coeff[1]+=c*bb-4*x*tt
        coeff[2]+=-4*x*bb-6*tt;coeff[3]+=-6*bb
      coeff[0]-=3*t*t;coeff[1]-=6*t*b;coeff[2]-=3*b*b
      coeff[1]+=2*alpha**3;coeff[2]+=3*alpha**2;coeff[4]-=1
      coeff=[c*m/M for c in coeff]
      coeff[0]+=-m*R*tail+K0*eta*lam*(1.2*(1-w)+1.41*w-x0*(1-w)+x1*w-.78-.8125*lam*eta)-1.75*Xi*lam*eta
      coeff[1]+=-m*(1+E*eta)-1.75*lam*eta
      value=min(bernstein4(coeff,rl,rh))
      if value<best:best=value;witness=(lam,w,eta,m,s0,s1,x0,x1)
    return best,witness

def cantelli(box,tail):
    l,L,rl,rh,wl,wh=box;D=Xi+rh
    Z=.625*D+.375+D**3/42
    mlo=2*.39886*(1-(D*D/(2*v)+Z)/42)
    R=1+max(0,.53+D-1)/(42*v-.6*max(0,D-1))
    E=42*(exp(((2*Xi*rh+rh*rh)/(2*v)+Z)/42)-1)
    T=L*(1+cv*D/42);hf=1+E/42
    if rl<=0 or 2*rl*T/(T+rl*rl)**2<=hf:return -1e100
    own=min(r*r/(T+r*r)-hf*r for r in [rl,rh])
    bracket=own-R*tail
    mass=mlo if bracket>=0 else .85
    return mass*bracket-(1.75*D-1)*L/42

def boxes(noise_parts=3,phase_parts=12,allocation_parts=8):
    ls=[.03+.045*i/noise_parts for i in range(noise_parts+1)]
    rs=[.15*i/phase_parts for i in range(phase_parts+1)]
    ws=[i/allocation_parts for i in range(allocation_parts+1)]
    return [(ls[i],ls[i+1],rs[j],rs[j+1],ws[k],ws[k+1]) for i in range(noise_parts) for j in range(phase_parts) for k in range(allocation_parts)]

if __name__=='__main__':
    # First bounded pilot: 12 representative boxes, not a coverage check.
    pilot=[(.03,.045,r,r+.0125,w,w+.125) for r,w in [(0,0),(.05,.375),(.0875,.875),(.1375,.875)]]
    pilot+=[(.045,.06,*b[2:]) for b in pilot[:4]]
    pilot+=[(.06,.075,*b[2:]) for b in pilot[:4]]
    rows=[]
    for box in pilot:
      tail,y,anchors=tails(box)
      best=max(((*bound(box,a/100,tail),a) for a in range(45,81,5)),key=lambda x:x[0])
      rows.append({'box':box,'margin':best[0],'quartic_alpha_hundredths':best[2],'hinge_y_hundredths':y,'later_anchors':anchors,'tail':tail,'witness':best[1]})
    print(json.dumps({'status':'DISCOVERY_ONLY_CLOSED_BOX_PILOT','boxes':len(rows),'rows':rows},indent=2))

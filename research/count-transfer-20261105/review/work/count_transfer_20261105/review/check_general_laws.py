"""Exact independent both-p-half scalar and actual-law semantic controls."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
from math import comb,isqrt
import json,hashlib,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('unoptimized Python')
N=5
def need(a,msg):
    if not a:raise ValueError(msg)
def extrema(l,h):
    vals=[l*(1-l),h*(1-h)];return min(vals),max(vals+[F(1,4)] if l<=F(1,2)<=h else vals)
def ratio_le(a,d,b,e):
    need(d>0 and e>0,'positive denominators')
    if a<=0<=b:return True
    if b<0<a:return False
    return a*a*e<=b*b*d if a>=0 else a*a*e>=b*b*d
def rootlo(a):
    S=10**24;k=isqrt(a.numerator*S*S//a.denominator);r=F(k,S)
    need(r*r<=a<(r+F(1,S))**2,'directed square root');return r
def law(a,b):return {F(0):F(1)} if not a*b else {-a:b/(a+b),b:a/(a+b)}
def conv(a,b):
    d={}
    for x,r in a.items():
      for y,s in b.items():d[x+y]=d.get(x+y,F(0))+r*s
    return d
def power(d,n):
    r={F(0):F(1)}
    for _ in range(n):r=conv(r,d)
    return r
def moment(d,n):return sum(r*x**n for x,r in d.items())
def reflect(d):return {-x:r for x,r in d.items()}
def mixed(p,d0,d1):
    d={}
    for x,r in d0.items():d[x]=d.get(x,F(0))+(1-p)*r
    for x,r in d1.items():d[1+x]=d.get(1+x,F(0))+p*r
    return d
def main(out):
    c=dict(scalar_tests=0,endpoint_gaussian_tests=0,curvature_tests=0,actual_pairs=0,
      conditional_convolutions=0,full_mixture_identities=0,reflection_identities=0,collision_checks=0,
      zero_components=0,tiny_components=0,mean_sign_caps=0,negative_controls=0)
    cells=[(F(38,100),F(40,100)),(F(1,2),F(51,100)),(F(61,100),F(63,100)),(F(49,100),F(51,100))]
    for l,h in cells:
      vmin,vmax=extrema(l,h)
      ps=[l+(h-l)*F(i,8) for i in range(9)]
      for p in ps:need(vmin<=p*(1-p)<=vmax,'complete quadratic extrema');c['scalar_tests']+=1
      for tlo,thi,lo,hi in product((F(0),F(1,2),F(1),F(2),F(4)),(F(1),F(3),F(5)),(F(0),F(1,20)),(F(1,10),F(3,5))):
        if thi<=tlo:continue
        amin=tlo-N*h;amax=thi-N*l
        endpoint_den=N*h*(1-h)+(lo if amin<0 else hi)
        fallback_den=N*vmin+lo if amin<0 else N*vmax+hi
        guarded=amax<=0 and amin*amin<=3*(N*h*(1-h)+lo)
        for p,t,z in product(ps,(tlo,(tlo+thi)/2,thi),(lo,(lo+hi)/2,hi)):
            a=t-N*p;D=N*p*(1-p)+z
            need(ratio_le(amin,fallback_den,a,D),'general signed Gaussian lower bound')
            need(ratio_le(amin,endpoint_den,a,D),'monotone exact-endpoint Gaussian lower bound')
            need(N*p+t*(1-2*p)+2*z>0,'positive derivative bracket on t in [0,n]')
            c['endpoint_gaussian_tests']+=1
            if guarded:
                need(a<=0 and a*a<=3*D and a*(3*D-a*a)<=0,'global guarded negative-phase concavity')
                c['curvature_tests']+=1
      # Exact conditional laws include zero, rare outward atoms, and sign-endpoint limits.
      for p in (l,(l+h)/2,h):
        q=1-p;v=p*q
        options0=[(F(0),F(0)),(F(1,10),F(1,10)),(F(7,10),F(1,10**12)),(F(1,10**9),p/2)]
        options1=[(F(0),F(0)),(F(1,10),F(1,10)),(F(1,10**12),F(4,5)),(q/2,F(1,10**9))]
        for (A,b),(a,B) in product(options0,options1):
            d0,d1=law(A,b),law(a,B);d=mixed(p,d0,d1)
            need(moment(d0,1)==moment(d1,1)==0,'centered conditional laws')
            s0,s1=moment(d0,2),moment(d1,2);x=q*s0;y=p*s1;w=v+x+y;lam=N*(x+y)
            c['actual_pairs']+=1;c['zero_components']+=int(s0==0)+int(s1==0)
            c['tiny_components']+=int(0<s0<F(1,10**8))+int(0<s1<F(1,10**8))
            beta=sum(r*(z-p)*abs(z-p) for z,r in d.items())/w
            R=sum(r*abs(z-p)**3 for z,r in d.items());G=sum(r*(z-p)**3 for z,r in d.items())
            need(beta==(v*(1-2*p)-x+y)/w,'same-law beta identity')
            need(R==v*(1-2*v)+3*(p*x+q*y)-q*moment(d0,3)+p*moment(d1,3),'absolute cube identity')
            need(G==v*(1-2*p)+3*(-p*x+q*y)+q*moment(d0,3)+p*moment(d1,3),'signed cube identity')
            whole=power(d,N);count={}
            for j in range(N+1):
                dj=conv(power(d0,N-j),power(d1,j));mass=F(comb(N,j))*p**j*q**(N-j)
                for z,r in dj.items():count[j+z]=count.get(j+z,F(0))+mass*r
                c['conditional_convolutions']+=1
            need(whole==count,'full actual iid law equals six-count mixture');c['full_mixture_identities']+=1
            rd=mixed(q,reflect(d1),reflect(d0));need(rd=={1-z:r for z,r in d.items()},'reflected class identity')
            rw=power(rd,N);need(rw=={N-z:r for z,r in whole.items()},'reflected product law')
            rb=sum(r*(z-q)*abs(z-q) for z,r in rd.items())/w
            rr=sum(r*abs(z-q)**3 for z,r in rd.items());rg=sum(r*(z-q)**3 for z,r in rd.items())
            need(rb==-beta and rr==R and rg==-G,'reflected signed and absolute moments');c['reflection_identities']+=1
            for z in sorted(whole)[::max(1,len(whole)//3)]:
                left=sum(r for t,r in rw.items() if t<=N-z)
                strict=sum(r for t,r in whole.items() if t<z)
                need(left+strict==1,'closed reflected event complements open original event');c['collision_checks']+=1
            mlo=F(21,50);gap=F(1,100);hi=F(3,5)
            if lam<=hi and v*v>=mlo*mlo*w and (p-max(d0))**2>=gap*gap*w and (q+min(d1))**2>=gap*gap*w:
                cap=N*max(vmin*vmin/(mlo*mlo)-vmin,vmax*vmax/(mlo*mlo)-vmax)
                r=rootlo(vmin)
                need(lam<=cap and max(d0)<=h-gap*r and -min(d1)<=1-l-gap*r,'independent mean/sign tightening')
                c['mean_sign_caps']+=1
    # Outside the threshold gate, choosing p_hi can fail.
    need(not ratio_le(-F(3),F(4,5),-F(5,2),F(9,20)),'outside [0,n] endpoint rule false');c['negative_controls']+=1
    need(F(7,10)*(1-F(7,10))<F(3,5)*(1-F(3,5)),'right-half lower variance is not the left endpoint');c['negative_controls']+=1
    need(F(1,4)>F(49,100)*F(51,100),'cross-half upper variance includes stationary point');c['negative_controls']+=1
    need(not ratio_le(-F(1),F(2),-F(1),F(1)),'negative numerator cannot use maximum denominator');c['negative_controls']+=1
    # Centered raw X with an atom at zero breaks the naive reflected sign probability q.
    X={-F(1):F(1,4),F(0):F(1,2),F(1):F(1,4)}
    pp=sum(r for x,r in X.items() if x>0);pr=sum(r for x,r in X.items() if x<0)
    need(pr!=1-pp,'zero atom blocks naive reflection of the positive mass');c['negative_controls']+=1
    need(sum(r for x,r in X.items() if x<=0)+sum(r for x,r in X.items() if -x<=0)>1,'closed complement loses atom');c['negative_controls']+=1
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    d=dict(status='PASS_EXACT_GENERAL_SCALAR_AND_LAW_CONTROLS',scope='Independent conditional scalar/semantic checks, not any new full row or acquisition.',counts=c,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (out/'RESULT.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d))
if __name__=='__main__':main(sys.argv[1])

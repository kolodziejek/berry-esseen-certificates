"""Small floating compound-Poisson diagnostic; truncated sums are NOT proof."""
import math,json,bisect
A=.6;d=.072;N=42;v=.24;cv=2.5;lam=.075
xi=1.84*math.sqrt(.25+lam/N)

def pois(mu):
    if mu==0:return [(0,1.)]
    ans=[];p=math.exp(-mu)
    for j in range(int(mu+12*math.sqrt(mu)+20)+1):
        if j:p*=mu/j
        ans.append((j,p))
    return ans

def cp2(t0,t1,b):
    m0=t0/A**2;m1=t1/d**2
    points=sorted((A*(j-m0)+d*(k-m1),p*q) for j,p in pois(m0) for k,q in pois(m1))
    xs=[x for x,p in points];mass=[0.];first=[0.];second=[0.]
    for x,p in reversed(points):
        mass.append(mass[-1]+p);first.append(first[-1]+x*p);second.append(second[-1]+x*x*p)
    best=(t0+t1)/(t0+t1+b*b);anchor=None
    for j in range(-10,int(b*20)):
        y=j/20
        pos=len(xs)-bisect.bisect_right(xs,y)
        numerator=second[pos]-2*y*first[pos]+y*y*mass[pos]
        val=max(0,numerator)/(b-y)**2
        if val<best:best=val;anchor=y
    return best,anchor

def one(r,w):
    D=xi+r;Z=.625*D+.375+D**3/N
    mlo=2*.39886*(1-(D*D/(2*v)+Z)/N);mhi=.85
    fm=math.exp(((r*r+2*xi*r)/(2*v)+Z)/N)
    R=1+max(0,.53+D-1)/(N*v-.6*max(0,D-1))
    ts=[(1-cv*D/N)*lam,(1+cv*D/N)*lam]
    tails=0;anchors=[]
    for i in range(1,5):
        t=(1+cv*(D+i)/N)*lam
        val,j=cp2((1-w)*t,w*t,i+r);tails+=val;anchors.append(j)
    V=(1+cv*(D+1)/N)*lam
    z=A/V
    Btail=math.exp(-V/A**2*((1+z)*math.log1p(z)-z))
    tails+=Btail**5/(1-Btail)
    K=.4/(N*(.25+lam/N)**1.5);B=.78+3*.52*lam/(8*N*v)
    normal=1.75*D*lam/N
    best=(-math.inf,None)
    for ai in range(20,121,2):
      alpha=ai/100;den=5*alpha**4
      poly=-r**4+3*alpha*alpha*r*r+2*alpha**3*r
      margins=[]
      for m in [mlo,mhi]:
       for t in ts:
        beta=K*lam*den/(m*t)
        kap0=-4*r-beta;kap1=-4*r+beta
        c0=max(A*A+kap0*A,d*d-kap0*d)
        c1=max(A*A-kap1*A,d*d+kap1*d)
        own=((3*alpha**2-6*r*r-c0*(1-w)-c1*w)*t-3*t*t+poly)/den-r*fm
        margin=m*(own-R*tails)-normal+K*lam*(1.2*(1-w)+1.41*w-B)
        margins.append(margin)
      val=min(margins)
      if val>best[0]:best=(val,alpha)
    own=(r*r/(ts[1]+r*r) if r else 0)-r*fm
    m=mlo if own-R*tails>=0 else mhi
    cm=m*(own-R*tails)-normal+K*lam*(1.2*(1-w)+1.41*w-d-B)
    if cm>best[0]:best=(cm,'Cantelli')
    return dict(r=r,w=w,margin=best[0],alpha=best[1],tail=tails,anchors=anchors)

if __name__=='__main__':
    cases=[one(i/100,w/4) for i in range(16) for w in range(5)]
    print(json.dumps({'status':'DISCOVERY_ONLY_TRUNCATED_POISSON_SUMS','lambda':lam,'cases':len(cases),'worst':min(cases,key=lambda x:x['margin']),'failures':sum(x['margin']<=0 for x in cases),'by_allocation':[dict(w=w/4,worst=min((x for x in cases if x['w']==w/4),key=lambda x:x['margin'])) for w in range(5)]},indent=2))

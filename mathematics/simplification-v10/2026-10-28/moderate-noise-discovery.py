"""Bounded double-precision exploration only; no continuous-domain acceptance."""
import math,json
A=.6;N=42;v=.24;cv=2.5;xi=1.84*math.sqrt(.25+.075/N)

def poisson_hinge(mu,j):
    term=math.exp(-mu);s=max(-j,0)**2*term
    for k in range(1,120):
        term*=mu/k;s+=max(k-j,0)**2*term
    return s

def p2(V,b):
    mu=V/A**2;x=b/A+mu
    best=V/(V+b*b);anchor=None
    for j in range(max(0,int(x))+1):
        if j>=x:break
        y=poisson_hinge(mu,j)/(x-j)**2
        if y<best:best=y;anchor=j
    return best,anchor

def bennett(V,b):
    t=A*b/V
    return math.exp(-(V/A**2)*((1+t)*math.log1p(t)-t))

def quartic(t,u,a):
    r=abs(u);sig=-1 if u>=0 else 1
    return ((3*a*a-A*A)*t-3*t*t-4*A*r*t-6*r*r*t-r**4+3*a*a*r*r+2*sig*a**3*r)/(5*a**4)

def own(lam,u):
    D=xi+abs(u);zl=lambda D:.625*D+.375+D**3/N
    if u>=0:
        G=max(0,2*xi*u-u*u);f=u*(1-(lam/(2*v)+G/(2*v)+zl(D))/N)
    else:
        r=-u;G=r*r+2*xi*r;eta=G/(2*v)+zl(D);f=u/(1-eta/N)
    ts=[lam*(1-cv*D/N),lam*(1+cv*D/N)]
    # Full quartic has concave t dependence; endpoints suffice for each a.
    opts=[(min(quartic(t,u,a) for t in ts)+f,a) for a in [j/200 for j in range(50,241)]]
    if u>=0:opts.append((f,None))
    else:opts.append((u*u/(ts[1]+u*u)+f,None))
    return max(opts,key=lambda a:a[0]),D

def trial(lam,u):
    (O,alpha),D=own(lam,u)
    tails=0;anchors=[]
    for i in range(1,5):
        t=(1+cv*(D+i)/N)*lam
        ti,j=p2(t,i-u);tails+=ti;anchors.append(j)
    V=(1+cv*(D+1)/N)*lam
    bo=1-max(0,u)/5;B=bennett(V,bo);tails+=B**5/(1-B)
    R0=(1+max(0,.53+D-1)/(N*v-.6*max(0,D-1)))*(1+max(0,.53+D-2)/(N*v))
    kappa=1.75*max(0,xi-u)
    # Favorable cubic gain dropped here; root estimates remain sufficient.
    m=2*.39886*(1-(D*D/(2*v)+.625*D+.375+D**3/N)/N)
    bracket=O-R0*tails
    margin=m*bracket-kappa*lam/N
    return dict(lam=lam,u=u,margin=margin,per_lambda=margin/lam,own=O,tail=tails,ratio=R0,alpha=alpha,anchors=anchors,D=D)
rows=[]
for lam in [.002,.005,.01,.02,.03,.05,.075]:
    cases=[trial(lam,-.272+i/200) for i in range(201)]
    rows.append(dict(lam=lam,worst=min(cases,key=lambda x:x['margin']),failed=sum(x['margin']<=0 for x in cases)))
print(json.dumps({'status':'DISCOVERY_ONLY','method':'quartic/Cantelli own; four integer-anchor P2 incoming terms plus Bennett tail','tested_cells':7*201,'rows':rows},indent=2))

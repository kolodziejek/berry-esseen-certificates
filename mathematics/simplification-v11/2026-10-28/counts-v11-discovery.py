"""Bounded double-precision endpoint exploration; not a proof or certificate."""
import math,json

A=.6; d=.072; v=.24; cv=2.5; U=.075
xi=1.84*math.sqrt(.25+U/42)

def candidate(lam,r,N,alpha,h,with_gain=True):
    inv=0 if N is None else 1/N
    D=xi+r
    zl=.625*D+.375+D**3/42
    mlo=2*.39886*(1-(D*D/(2*v)+zl)*inv)
    mhi=.85
    fm=math.exp(((r*r+2*xi*r)/(2*v)+zl)*inv)
    R=1+max(0,.53+D-1)/(v/inv-.6*max(0,D-1)) if inv else 1
    omlo=1-cv*D*inv; omhi=1+cv*D*inv
    den=5*alpha**4
    poly=-r**4+3*alpha**2*r*r+2*alpha**3*r
    K=(.4*inv/(.25+lam*inv)**1.5) if with_gain else 0
    B=.78+3*.52*lam*inv/(8*v)
    normal=1.75*D*lam*inv
    eA=math.expm1(h*A)-h*A
    ed=math.expm1(h*d)-h*d
    values=[]
    for j in [0,1]:
        mg=omhi*lam*(eA/A**2 if j==0 else ed/d**2)
        rat=math.exp(-h+(cv*lam*inv*ed/d**2 if j else 0))
        tail=math.exp(-h*r+mg)*rat/(1-rat) if rat<1 else math.inf
        for m in [mlo,mhi]:
            for om in [omlo,omhi]:
                t=om*lam; beta=K*lam*den/(m*t)
                kap=-4*r+(-beta if j==0 else beta)
                cost=max(A*A+kap*A,d*d-kap*d) if j==0 else max(A*A-kap*A,d*d+kap*d)
                own=((3*alpha**2-6*r*r-cost)*t-3*t*t+poly)/den-r*fm
                margin=m*(own-R*tail)-normal+K*lam*((1.2 if j==0 else 1.41)-B)
                values.append((margin,j,m,om,tail,own))
    z=min(values)
    return z[0],dict(variance_endpoint=z[1],mass=z[2],variance_factor=z[3],tail=z[4],own=z[5],alpha=alpha,h=h)

if __name__=='__main__':
    rows=[]
    # 360 phase/noise/n cases; each tests common tilt and common quartic
    # parameters at just the two variance endpoints, not an allocation mesh.
    for N in [42,None]:
      for lam in [.02,.03,.05,.075]:
        cases=[]
        for ir in range(45):
          r=ir/200
          best=max((candidate(lam,r,N,a/100,h/10) for a in range(40,92,2) for h in range(25,81,2)),key=lambda x:x[0])
          cases.append(dict(r=r,margin=best[0],**best[1]))
        rows.append(dict(n=N,lambda_value=lam,worst=min(cases,key=lambda x:x['margin']),failures=sum(x['margin']<=0 for x in cases)))
    print(json.dumps({'status':'DISCOVERY_ONLY','cases':360,'method':'common quartic and common Bennett tilt; both allocation endpoints; coupled third-moment penalty; n42 and formal n=infinity diagnostic','rows':rows},indent=2))

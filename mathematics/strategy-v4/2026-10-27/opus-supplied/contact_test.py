import numpy as np, math
from scipy.special import ndtr, gammaln
from scipy.optimize import minimize_scalar
CE=(3+math.sqrt(10))/(6*math.sqrt(2*math.pi)); phi=lambda x: math.exp(-x*x/2)/math.sqrt(2*math.pi)
def bcdf(n,p):
    k=np.arange(n+1); pmf=np.exp(gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)+k*np.log(p)+(n-k)*np.log1p(-p)); return np.cumsum(pmf)
def best_threshold(n,p):
    q=1-p; s=math.sqrt(p*q); F=bcdf(n,p); k=np.arange(n+1); H=(k-n*p)/s
    d=F-ndtr(H/math.sqrt(n)); i=int(np.argmax(d)); rho=(p*p+q*q)/s
    return math.sqrt(n)*d[i]/rho, H[i], F[i], rho
def score(n,p): return best_threshold(n,p)[0]
def contact_sup(n):
    grid=np.linspace(0.05,0.95,1801); vals=[score(n,p) for p in grid]; p0=grid[int(np.argmax(vals))]
    r=minimize_scalar(lambda p:-score(n,p),bounds=(max(.01,p0-.002),min(.99,p0+.002)),method='bounded',options={'xatol':1e-12})
    p=r.x; q=1-p; s=math.sqrt(p*q); C,H,F,rho=best_threshold(n,p)
    beta=(-p*(p/s)**2*q/p*0+ q*0)  # placeholder, computed below
    A=p/s; B=q/s; beta=-q*A*A+p*B*B; z=H/math.sqrt(n)
    Fm=bcdf(n-1,p) if n>1 else np.array([1.0])
    def Fn1(t):  # P(S_{n-1} <= t), S_{n-1}=(K-(n-1)p)/s
        if n==1: return 1.0 if t>=0 else 0.0
        x=(n-1)*p+t*s; j=math.floor(x+1e-12)
        return 0.0 if j<0 else (1.0 if j>=n-1 else Fm[j])
    def I(y):
        return (n**1.5*(Fn1(H-y)-F)+n*y*phi(z)+H*phi(z)/2*(y*y-1)+1.5*C*rho*(y*y-1)-C*(abs(y)**3-rho-3*y*beta))/rho
    ys=np.linspace(-6,6,24001); Iv=np.array([I(y) for y in ys])
    # evaluate just left/right of the jump points of Fn1 too
    jumps=[(H-((j-(n-1)*p)/s)) for j in range(n)] if n>1 else [H]
    extra=[I(y+e) for y in jumps for e in (-1e-9,1e-9) if abs(y)<6]
    sup=max(Iv.max(),max(extra) if extra else -1e9); ysup=ys[int(np.argmax(Iv))]
    return p,C,I(-A),I(B),sup,ysup
print(f"C_E={CE:.6f}")
for n in [1,2,3,4,5,6,8,10,15,20,30,41,42,60,100]:
    p,C,Ia,Ib,sup,ys=contact_sup(n)
    print(f"n={n:3d} p={p:.5f} C={C:.6f} I(-A)={Ia:+.2e} I(B)={Ib:+.2e} sup_y I={sup:+.3e} at y={ys:+.3f}")

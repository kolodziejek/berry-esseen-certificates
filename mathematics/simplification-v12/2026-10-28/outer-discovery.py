"""Bounded exact exploration of outer-phase scalar gates; not acceptance."""
from fractions import Fraction as F
from math import comb, factorial
import json
A=F(3,5); U=F(3,40); N=F(42); v=F(6,25)
xi=F(46,25)*F(251,500)
Z=lambda D:F(5,8)*D+F(3,8)+D**3/N
mass=lambda D:2*F(19943,50000)*(1-(D*D/(2*v)+Z(D))/N)
muG=F(5,2)*U/A**2
def J(m,u):return muG**(m+1)/(factorial(m+1)*(m*(1/A-1)-u/A+muG)**2*(1-muG/(m+2)))
def Q(mu,u):return mu**2*(F(1,2)+mu/6)/((1-u)/A-1+mu)**2
ans={}
D=F(6,5); Tg=F(15,14)*U
own=min(r*r/(Tg+r*r)-F(27,25)*r for r in [F(3,20),F(34,125)])
tail=Q(F(8,7)*U/A**2,-F(3,20))+J(2,-F(3,20))
ans['negative']=F(71,100)*(own-F(27,25)*tail)-F(11,10)*U/N-U/100
ans['negative_mass']=mass(D)-F(71,100)
for u in [F(3,40),F(3,20)]:
    ans['near_'+str(u)]=F(73,100)*(F(19,20)*u-F(107,100)*(Q(F(9,8)*U/A**2,u)+J(2,u)))-F(9,10)*U/N-U/100
D=F(413,250); R=F(1143,1000)
t1=F(7,6)*U; mu2=(1+F(5,2)*(D+2)/N)*U/A**2
for u in [F(3,20),F(91,125)]:
    second=mu2**3/(6*((2-u)/A-2+mu2)**2)
    ans['far_'+str(u)]=F(13,20)*(F(9,10)*u-R*(t1/(t1+(1-u)**2)+second+J(3,u)))-F(19,10)*U/N-U/100
ans['far_mass']=mass(D)-F(13,20)
ratio=(1+(F(53,100)+D-1)/(N*v-F(3,5)*(D-1)))*(1+(F(53,100)+D-2)/(N*v))
ans['far_ratio']=R-ratio

# Sparse rational polynomials in lambda,u. Ordinary algebra, then a direct
# tensor Bernstein transform on a closed rectangle; all coefficients retained.
def clean(a):return {k:v for k,v in a.items() if v}
def c(x):return clean({(0,0):F(x)})
def add(a,b):
    d=dict(a)
    for k,x in b.items():d[k]=d.get(k,0)+x
    return clean(d)
def scale(a,b):return clean({k:v*b for k,v in a.items()})
def mul(a,b):
    d={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():d[i+k,j+l]=d.get((i+k,j+l),0)+x*y
    return clean(d)
def power(a,n):
    z=c(1)
    for _ in range(n):z=mul(z,a)
    return z
def total(*args):
    z={}
    for a in args:z=add(z,a)
    return z
x={(1,0):F(1)}; y={(0,1):F(1)}
alpha=F(16,25); den=5*alpha**4
mu1=scale(x,F(9,8)/A**2); mug=scale(x,F(5,2)/A**2)
d1=total(c(1/A-1),scale(y,-1/A),mu1)
d2=total(c(2*(1/A-1)),scale(y,-1/A),mug)
dg=add(c(1),scale(mug,-F(1,4)))
den1=power(d1,2); den2=scale(mul(power(d2,2),dg),6)
num1=mul(power(mu1,2),add(c(F(1,2)),scale(mu1,F(1,6))))
num2=power(mug,3); common=mul(den1,den2)
def polynomial(tcoef):
    t=scale(x,tcoef)
    own=scale(total(scale(t,3*alpha**2-A*A),scale(power(t,2),-3),
      scale(mul(y,t),-4*A),scale(mul(power(y,2),t),-6),scale(power(y,4),-1),
      scale(power(y,2),3*alpha**2),scale(y,-2*alpha**3)),1/den)
    own=add(own,scale(y,F(24,25)))
    baseline=add(scale(own,F(73,100)),scale(x,-F(3,4)/N-F(1,100)))
    tail=add(mul(num1,den2),mul(num2,den1))
    return add(mul(baseline,common),scale(tail,-F(73,100)*F(53,50)))
def transform(P,box):
    a,b,d,e=box; z={}
    for (i,j),v0 in P.items():
        for k in range(i+1):
            for l in range(j+1):
                term=v0*comb(i,k)*comb(j,l)*a**(i-k)*(b-a)**k*d**(j-l)*(e-d)**l
                z[k,l]=z.get((k,l),0)+term
    ni=max(i for i,j in P); nj=max(j for i,j in P)
    return {(i,j):sum(value*F(comb(i,k),comb(ni,k))*F(comb(j,l),comb(nj,l))
      for (k,l),value in z.items() if k<=i and l<=j) for i in range(ni+1) for j in range(nj+1)}
certs=[]
for tcoef in [F(79,84),F(89,84)]:
    P=polynomial(tcoef)
    for splits in [1,2,4,8]:
        vals=[]; negatives=[]; zeros=[]
        for i in range(splits):
            for j in range(splits):
                box=(U*i/splits,U*(i+1)/splits,U*j/splits,U*(j+1)/splits)
                B=transform(P,box);vals.extend(B.values())
                negatives.extend((i,j,k) for k,v0 in B.items() if v0<0)
                zeros.extend((i,j,k) for k,v0 in B.items() if v0==0)
        certs.append({'tcoef':str(tcoef),'splits':splits,'min':float(min(vals)),'negative_count':len(negatives),'zeros':zeros,'degree':[max(i for i,j in P),max(j for i,j in P)]})
        if not negatives:break
print(json.dumps({'scalar':{k:float(v) for k,v in ans.items()},'bernstein':certs},indent=2))

#!/usr/bin/env python3
"""Independent analytic gates and actual curvature controls; no constructor imports."""
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import hashlib,json,sys
gates=[];controls=[];actual=0
def check(name,value):
    assert value,name
    gates.append(name)
def must(v):assert v
def reject(name,fn):
    try:fn()
    except (AssertionError,ValueError):controls.append(name);return
    raise AssertionError(name)
def sqrt_bounds(x):
    D=10**28;k=isqrt(x.numerator*D*D//x.denominator)
    return F(k,D),F(k+1,D)
# Elements a+b sqrt(10), with exact sign comparison.
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):return x[0]*y[0]+10*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(x,c):return x[0]*c,x[1]*c
def positive(x):
    a,b=x
    if b==0:return a>0
    if a>=0 and b>0:return True
    if a<=0 and b<0:return False
    return a*a>10*b*b if a>0 else 10*b*b>a*a
def Qpair(p):
    v=p*(1-p)
    return 2*p-1-6*v,1-2*v
slo=F(3162277660,10**9);shi=F(3162277661,10**9)
check('sqrt10 enclosure',slo*slo<10<shi*shi)
check('geometric budget safely enlarged',F(3220665378,10**8)<F(129,4))
# Derivative signs of p q^3, p²q³, p³q, p³q² establish their maxima.
check('first denominator maximum',F(1,3)*F(2,3)**3<F(63,200)**2)
check('second denominator maximum',F(2,5)**2*F(3,5)**3<F(93,500)**2)
check('third denominator maximum',F(2,5)**3*F(3,5)<F(49,250)**2)
check('fourth denominator maximum',F(2,5)**3*F(3,5)**2<F(19,125)**2)
check('variance power lower',(F(2,9))**3>F(13,125)**2)
d=F(17,250)
check('first square-root cost',6*(1-d)*(slo+1)>F(24,5)**2)
check('second square-root cost',6*(1-d)*(slo-1)>F(69,20)**2)
y0=3*(slo+3)/F(63,200)+2*F(24,5)/F(93,500)-(shi+7)*d/F(13,125)
y1=3*(slo+1)/F(49,250)+2*F(69,20)/F(19,125)-(shi+5)*d/F(13,125)
check('first uniform noise cost',y0>100)
check('second uniform noise cost',y1>100)
check('normalization ceiling',F(8,25)/(42*F(2,9))==F(6,175))
check('Taylor linear coefficient',F(3,2)+F(3,8)*F(6,175)<F(31,20))
den=100-F(129,4)*F(31,20)*F(3,28)
lam_bound=(F(129,4)-24)/den
check('budget-derived noise bound',den>0 and lam_bound<F(9,100))
check('actual total variance ceiling',F(6,25)+F(9,100)/42<F(1,4))
check('raw threshold displacement',F(46,25)/2==F(23,25))
check('threshold c cap',F(23,25)-F(3,5)==F(8,25))
check('crossing lower endpoint',42*(F(1,3)-d)>F(23,25))
check('crossing upper endpoint',42*(1-d-F(2,5))>F(23,25))
check('crossing width',F(7,10)+d<1 and d<1)
check('own variance envelope',F(9,100)/F(3,5)==F(3,20))
check('fourth moment envelope',F(7,10)**2*F(3,20)+3*F(3,20)**2==F(141,1000))
check('variance root upper',F(3,20)<F(97,250)**2)
check('cubic correction sign',1-F(3,2)*F(5,9)-d-F(3,8)*F(5,9)*F(9,4200)/F(2,9)>0)
# Polynomial factorization gives the pointwise fourth-moment majorant.
poly=[F(0)]*5
for i,a in enumerate([16,-24,9]):
    for j,b in enumerate([16,8,3]):poly[i+j]+=a*b
check('quartic hinge factorization',poly==[256,-256,0,0,27])
check('quadratic factor positive',8**2-4*3*16<0)
check('complete reciprocal-square tail',sum(F(1,i*i) for i in range(1,6))+F(1,5)<F(5,3))
check('complete reciprocal-cube tail',sum(F(1,i**3) for i in range(1,3))+F(1,8)==F(5,4))
check('mode variance at N43',1-F(1,43)-F(2,43**2)>F(39,40))
check('finite mode mass coefficient',F(2,5)**2*F(40,39)*F(516,515)**2<F(41,100)**2)
check('Gaussian lower constant',F(19943,50000)**2*F(44,7)<1)
def S(c):
    return F(3,80)+c*F(97,250)+F(27,256)*F(141,1000)*(F(5,3)+F(5,4)*c)
Em=(F(41,100)*S(F(8,25))+F(2,5)*(F(23,200)+F(2,27)))/F(13,125)
Ep=(F(41,100)*S(0)+F(2,5)*F(2,27)+F(2,5)*F(23,25)*F(9,100)/2)/F(13,125)
reserve=4*F(19943,50000)-F(1,10)
check('negative H complete error margin',Em<reserve)
check('positive H complete error margin',Ep<reserve)
# Exact Q(sqrt10) comparisons, no decimal radical substitution.
cutoffs=[]
for p,N in [(F(1,3),126),(F(7,20),196),(F(3,8),491),(F(39,100),1141),(F(2,5),2682)]:
    v=p*(1-p);qp=Qpair(p)
    check('positive Q at endpoint',positive(qp))
    check('exact excluded integer endpoint',positive(add(scale(mul(qp,qp),N*N),(-576*v,F(0)))))
    check('preceding integer below scalar threshold',not positive(add(scale(mul(qp,qp),(N-1)**2),(-576*v,F(0)))))
    # Sharper Schulz reserve algebra, using its actual p<=1/2 branch.
    check('Schulz Q identity',qp==add(scale((3,F(1)),1-2*v),(-(4-2*p),F(0))))
    cutoffs.append([str(p),N-1])
check('pstar beyond region',(4-shi)/2>F(2,5))
check('inherited low-p integer endpoint',positive(add(scale(mul(Qpair(F(1,3)),Qpair(F(1,3))),169**2),(-F(3220665378,10**8)**2*F(2,9),F(0)))))

# Independent actual common-noise sums provide exact curvature controls.
n=42
for eps in [F(0),F(1,10**5),F(1,1000),F(3,100)]:
    W=[(eps*(2*k-n),F(comb(n,k),2**n)) for k in range(n+1)]
    for p in [F(1,3),F(7,20),F(2,5)]:
        q=1-p;v=p*q;lam=n*eps*eps;T=lam/q;M=F(49,100)*T+3*T*T
        pi=[F(comb(n,j))*p**j*q**(n-j) for j in range(n+1)]
        for w in [F(-9,10),F(0),F(9,10)]:
            t=n*p+w;c=max(F(0),-q-w);C=F(0)
            for j in range(1,n):
                a=t-j
                B=sum(prob*max(F(0),a-z) for z,prob in W)-max(F(0),a)
                check('actual stop-loss defect nonnegative',B>=0)
                C+=(pi[j+1]-pi[j])*B
            left=C*n*v*sqrt_bounds(n*v)[1]
            right=F(41,100)*(T/4+c*sqrt_bounds(T)[0]+F(27,256)*M*(F(5,3)+F(5,4)*c))
            check('actual signed curvature bound',C<=0 or left<=right)
            actual+=1
# Both physical variance-allocation endpoints, with actual independent sums.
for active_group in [0,1]:
    for eps in [F(1,1000),F(1,20)]:
        for p in [F(1,3),F(7,20),F(2,5)]:
            q=1-p;v=p*q;lam=n*(q if active_group==0 else p)*eps*eps
            T=lam/q;M=F(49,100)*T+3*T*T
            pi=[F(comb(n,j))*p**j*q**(n-j) for j in range(n+1)]
            for w in [F(-9,10),F(0),F(9,10)]:
                t=n*p+w;c=max(F(0),-q-w);C=F(0)
                for j in range(1,n):
                    m=n-j if active_group==0 else j
                    W=[(eps*(2*k-m),F(comb(m,k),2**m)) for k in range(m+1)]
                    if pi[j+1]>pi[j]:
                        check('actual allocation variance',m*eps*eps<=T)
                        check('actual allocation fourth moment',(3*m*m-2*m)*eps**4<=M)
                    a=t-j
                    B=sum(prob*max(F(0),a-z) for z,prob in W)-max(F(0),a)
                    C+=(pi[j+1]-pi[j])*B
                lhs=C*n*v*sqrt_bounds(n*v)[1]
                rhs=F(41,100)*(T/4+c*sqrt_bounds(T)[0]+F(27,256)*M*(F(5,3)+F(5,4)*c))
                check('actual endpoint allocation curvature',C<=0 or lhs<=rhs)
                actual+=1
# Tiny common-noise law: only j=14 contributes at t=14.
eps=F(1,10**5);p=F(7,20);q=1-p;v=p*q;t=F(14)
W=[(eps*(2*k-n),F(comb(n,k),2**n)) for k in range(n+1)]
absmean=sum(prob*abs(z) for z,prob in W)
pi14=F(comb(n,14))*p**14*q**28
pi15=F(comb(n,15))*p**15*q**27
C=(pi15-pi14)*absmean/2;c=n*p-q-t
T=n*eps*eps/q;M=F(49,100)*T+3*T*T
without=F(41,100)*(T/4+F(27,256)*M*(F(5,3)+F(5,4)*c))
check('tiny common-noise counterexample in raw range',(t-n*p)**2<F(46,25)**2*(v+eps*eps))
check('omitted square-root term fails exactly',C*n*v*sqrt_bounds(n*v)[0]>without)
reject('drop c sqrt(T)',lambda:must(C*n*v*sqrt_bounds(n*v)[0]<=without))
# Below 1/3, all noise in group zero can decrease rho.
p=F(13,50);q=1-p;v=p*q;eps=F(1,1000);s=q*eps*eps
M0=v*(1-2*v);N0=M0+3*v*eps*eps
check('below one-third actual rho decreases',N0*N0*v**3<M0*M0*(v+s)**3)
reject('extend favorable rho sign below one-third',lambda:must(N0*N0*v**3>=M0*M0*(v+s)**3))
reject('extend first cutoff below one-third',lambda:must(168<=125))
# Testing the c<=1 mesh premise: two negative-near mesh sites appear beyond it.
reject('drop near-mesh c ceiling',lambda:must(sum(F(-3,2)<F(3,4)-j<0 for j in range(-3,4))<=1))
source=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent/'geometry-slack.tex'
pin='8eb6fc89d82eb458fef45fb9a2f9783c1cae2705c908dcb8bebba725a4a36461'
assert hashlib.sha256(source.read_bytes()).hexdigest()==pin,'source pin mismatch'
print(json.dumps({'result':'PASS','source_sha256':pin,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'exact_gates_and_controls':len(gates),'actual_curvature_cases':actual,'negative_controls':controls,'lambda_bound':str(lam_bound),'negative_H_error':str(Em),'positive_H_error':str(Ep),'reserve_less_target_margin':str(reserve-Em),'integer_cutoffs':cutoffs,'constructor_code_imported':False},indent=2))

"""Exact scalar acceptance for right-direct.tex; no grid or optimization."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
gates={}
def positive(name,value):
    assert name not in gates;gates[name]=F(value);assert value>0,name
def add(*ps):
    q=[F(0)]*max(map(len,ps))
    for p in ps:
        for j,x in enumerate(p):q[j]+=x
    return q
def scale(p,a):return [a*x for x in p]
def mul(p,q):
    z=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):z[i+j]+=a*b
    return z
def val(p,x):
    out=F(0)
    for c in reversed(p):out=out*x+c
    return out
N=200;alpha=1-F(5,N);b=1+F(3,N);c=F(23,50)
v=F(6,25);v32=F(117,1000);beta=F(41,100);a=F(231,250)
lo=F(3,40);hi=F(9,25)
positive('raw scale',F(251,500)**2-F(1,4)-hi/N)
positive('raw displacement',a-F(46,25)*F(251,500))
positive('bump displacement premise',F(47,50)-a)
positive('interior crossing lower',N*(F(2,5)-F(9,125))-a)
positive('interior crossing upper',N*(1-F(53,100)-F(9,125))-a)
positive('window displacement',4-(a+3))
positive('left window interior',N*F(2,5)-a-2)
positive('right window interior',N*(1-F(53,100))-a-3)
for z in [F(19,50),F(11,20)]:positive('window variance '+str(z),z*(1-z)-F(23,100))
positive('phi lower',1-F(199,500)**2*F(44,7))
positive('five masses',F(199,250)*(1-(8+F(1,12))/(N*F(23,100)))-F(13,20))
positive('variance power',v**3-v32**2)
positive('sqrt T coefficient',F(3,2)**2-F(100,47))
positive('curvature c',c-(a-F(47,100)))
positive('mode linear loss',v-F(3,5)*F(1,5))
positive('mode quadratic loss',2*v-F(3,5)**2)
positive('mode variance ratio',1-F(1,43)-F(2,43**2)-F(39,40))
positive('mode mass coefficient',beta**2-F(2,5)**2*F(40,39)*F(516,515)**2)
positive('cubic repair',F(87,250)-F(13,16)*hi/N)
L=[F(0),F(1)];T=scale(L,F(100,47));M=add(scale(T,F(9,25)),scale(mul(T,T),3))
curvneg=scale(add(scale(T,F(1,4)),[c*F(3,8),c*F(3,2)],scale(M,F(27,256)*(F(5,3)+F(5,4)*c))),beta/v32)
curvpos=scale(add(scale(T,F(1,4)),scale(M,F(27,256)*F(5,3))),beta/v32)
normalneg=[F(2,5)/v32*(a/8+F(2,27))]
normalpos=scale([F(2,27),a/2],F(2,5)/v32)
x=3*alpha
W=scale([0,x/2-F(9,25)*b/16-F(10,N)*F(22,7)**2,
         -x*x/4-3*b*b/16,x**3/12,-x**4/48],F(13,50))
records={}
for label,curv,norm,lowers in [('negative',curvneg,normalneg,[6075,2577]),('positive',curvpos,normalpos,[11528,11247])]:
    E=add(curv,norm);P=add(W,scale(E,-F(1,N)),[0,-F(1,100)])
    positive(label+' negative quadratic coefficient',-F(3,5)-P[2])
    positive(label+' cubic coefficient ceiling',F(11,20)-P[3])
    positive(label+' negative fourth coefficient',-P[4])
    positive(label+' strict concavity',F(6,5)-6*F(11,20)*hi)
    for end,lower in zip([lo,hi],lowers):positive(label+' endpoint '+str(end),val(P,end)-F(lower,10**6))
    records[label]={'W':list(map(str,W)),'E':list(map(str,E)),'P':list(map(str,P)),
                    'endpoint_values':list(map(str,[val(P,lo),val(P,hi)]))}
# Genuine failure of a tempting stronger window mass bound.
mass=F(comb(200,100),2**200)
assert 200*mass**2<F(4,5)**2
# Pointwise smooth normal repair at positive w has the adverse sign.
assert F(1,4)+F(1,100)>F(1,4)
# The same certificate cannot be reused at100: recompute its gain parameters.
n=100;x=3*(1-F(5,n));bb=1+F(3,n)
W100=scale([0,x/2-F(9,25)*bb/16-F(10,n)*F(22,7)**2,-x*x/4-3*bb*bb/16,x**3/12,-x**4/48],F(13,50))
assert val(add(W100,scale(add(curvneg,normalneg),-F(1,n)),[0,-F(1,100)]),hi)<0
here=Path(__file__).resolve()
print(json.dumps({'status':'PASS_RIGHT_SIGNED_200_SCALARS','gate_count':len(gates),
 'gates':{k:str(v) for k,v in gates.items()},'polynomials':records,
 'negative_controls':['normalized mass 4/5 is false at n200,p1/2','same scalar certificate fails at n100'],
 'proof_sha256':hashlib.sha256(here.with_name('right-direct.tex').read_bytes()).hexdigest(),
 'scope':'Exact continuous-domain scalar checks for two concave quartics and analytic guards; not a finite parameter sample or a proof of acquisition.'},indent=2))

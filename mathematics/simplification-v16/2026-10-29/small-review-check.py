"""Independent rational reconstruction of the elementary compact small-noise proof.

No constructor checker is imported. The quartic rectangle is proved by its
full tensor Bernstein coefficients, not by the constructor's z^4 relaxation.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse,hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
parser=argparse.ArgumentParser();parser.add_argument('--proof',required=True,type=Path);args=parser.parse_args()
PIN='da583ea6712fa159345aa22d402faaa5cd60c518aec51c8aff033c09df636e11'
raw=args.proof.read_bytes()
if hashlib.sha256(raw).hexdigest()!=PIN:raise ValueError('Unreviewed proof bytes')
gates={}
def pos(name,x):
    assert name not in gates;gates[name]=F(x);assert x>0,name
A=F(3,5);alpha=F(13,25);N=700;L=F(1,100);T=F(101,10000)
v=F(15,64);D=F(5,3);b=F(1,20);eta=F(2,525);d=F(1,250)
Z=lambda x:F(3,5)*x+F(3,8)+x**3/840
pos('variance below1/4',F(1,4)-F(93,200)*F(107,200)-L/N)
pos('global displacement',D-F(23,25)-F(7,10))
pos('inner displacement',1-F(23,25)-b)
pos('segment lower',F(3,8)-D/N-F(37,100))
pos('segment upper',F(47,100)-F(93,200)-D/N)
pos('count interior lower',N*F(3,8)-D-1)
pos('count interior upper',N*F(107,200)-D-1)
# The extrema of segment derivative bounds occur at .37 on this sub-half interval.
seg=F(37,100)*F(63,100);skew=F(26,100)
pos('segment variance',seg-F(23,100))
pos('entropy third derivative',5-skew/seg**2)
pos('prefactor derivative',F(6,5)-skew/seg)
pos('factorial remainder',F(3,8)-1/(12*seg))
assert F(5,6*N)==F(1,840)
pos('phi lower',1-F(199,500)**2*F(44,7))
pos('mass lower',F(199,250)*(1-(D**2/(2*v)+Z(D))/N)-F(3,4))
pos('mode variance ratio',1-F(1,43)-F(2,43**2)-F(39,40))
pos('mode41/100',F(41,100)**2-F(2,5)**2*F(40,39)*F(516,515)**2)
pos('mode17/20',F(17,20)**2*v-F(41,100)**2)
pos('global count ratio',F(6,5)-F(17,20)/F(3,4))
pos('inner count ratio',F(51,50)-1-F(93,200)/(N*v))
pos('inner later counts decrease',2-F(93,200)-1)
pos('variance log coefficient',F(11,5)-1/(2*v)-D**2/(2*N*v**2))
for label,dd,bb,lo,hi in [('inner',F(1),b,F(99,100),F(101,100)),('global',D,F(7,10),F(49,50),F(51,50))]:
    exponent=(F(11,5)*L+(2*dd*bb+bb*bb)/(2*v)+Z(dd))/N
    pos(label+' exponential domain',1-exponent)
    pos(label+' f lower',1-exponent-lo)
    pos(label+' f upper',hi-1/(1-exponent))
pos('cubic sign',F(9,8)-d-F(51,64)-F(17,20)*L/N)
pos('normal repair coefficient',4*v**3-F(1,5)**2)
pos('own count variance',F(1,100)-eta*D)
pos('switch inside phase',b-F(3,2)*T)
pos('own tolambda',F(3,5)*F(99,100)-F(59,100))
series={4:(5,F(13,12)),3:(3,F(5,4)),2:(5,F(5,3))}
for power,(cut,cap) in series.items():
    bound=sum(F(1,i**power) for i in range(1,cut+1))+F(1,(power-1)*cut**(power-1))
    pos('whole zeta'+str(power),cap-bound)
def K(aa):return A*A*(F(13,12)*aa+F(5,4)*eta)+3*L*(F(13,12)*aa*aa+F(5,2)*aa*eta+F(5,3)*eta*eta)
innerK=K(1+eta);outerK=K(1+eta*D)
pos('inner whole tail',F(53,100)-innerK/(1-b)**4)
pos('outer whole tail',F(43,100)-outerK)
# Full F(z,t)-3/5, retaining its z^4 t^3 term. Power coefficient (z,t).
M=5*alpha**4;tensor={}
for label,sigma,b0 in [('negative',1,F(-101,100)),('positive',-1,F(99,100))]:
    coeff={(0,0):(3*alpha**2-A**2)/M-F(3,5),(0,1):-3/M,
      (1,0):F(2*sigma)/(5*alpha)+b0,(1,1):-4*A/M,
      (2,1):3*alpha**2/M,(2,2):-6/M,(4,3):-1/M}
    values=[]
    for i in range(5):
        for j in range(4):
            val=sum(c*F(3,2)**a*T**b*F(comb(i,a),comb(4,a))*F(comb(j,b),comb(3,b))
                    for (a,b),c in coeff.items() if a<=i and b<=j)
            pos('tensor '+label+' '+str((i,j)),val);values.append(val)
    tensor[label]={'coefficients':list(map(str,values)),'minimum':str(min(values))}
    # Agreement with direct polynomial formula at rational interior points.
    for zz,tt in [(F(0),F(0)),(F(3,2),T),(F(3,5),T/3)]:
        direct=(3*alpha**2-A*A-3*tt)/M+(F(2*sigma)/(5*alpha)+b0-4*A*tt/M)*zz+(3*alpha**2*tt-6*tt*tt)*zz*zz/M-tt**3*zz**4/M-F(3,5)
        assert direct==sum(c*zz**a*tt**b for (a,b),c in coeff.items())
# Strict polynomial minorant maximum: (9+6sqrt3)/20<1.
pos('minorant maximum',11**2-36*3)
# Cantelli switches and outer endpoints are analytically reduced, then exact.
pos('switch derivative',3/(1+F(9,4)*T)**2-F(101,100))
pos('switch endpoint dividedbyvariance',F(9,4)/(1+F(9,4)*T)-F(303,200)-F(3,5))
pos('inner far Cantelli endpoint',b*b/(T+b*b)-F(101,100)*b-F(3,5)*T)
pos('negativeouter derivative',2*b*T/(T+b*b)**2-F(51,50))
for r in [b,F(3,10)]:pos('negativeouter endpoint '+str(r),r*r/(T+r*r)-F(51,50)*r-F(7,50))
for u in [b,F(7,10)]:pos('positiveouter endpoint '+str(u),F(49,50)*u-F(6,5)*F(43,100)*L/(1-u)**4-F(1,25))
final={
 'inner':F(3,4)*(F(59,100)-F(51,50)*F(53,100))-F(2,N)-F(1,100),
 'negativeouter':F(3,4)*(14-F(6,5)*F(43,100))-F(4,N)-F(1,100),
 'positiveouter':3-F(4,N)-F(1,100)}
for name,x in final.items():pos('final '+name,x)
assert F(-3,10)<-b<0<b<F(7,10)
assert F(7,10)-F(-3,10)==1
# Genuine controls of stronger or incorrectly normalized sufficient assertions.
assert outerK>F(42,100)
assert innerK/(1-b)**4>F(52,100)
# F_- at t=T,z=1.5 is below .8; only .6 is asserted.
assert tensor['negative']['coefficients'][-1]==tensor['negative']['minimum']
fmin=F(3,5)+F(tensor['negative']['coefficients'][-1]);assert fmin<F(4,5)
# Actual-law counterexample to deleting the positive-phase denominator:
# n700,p3/8,lambda.01, U0 in{-.6,1/26250},U1=0, t262.7,k262.
# Incoming count263 has437 noisy U0's; any rare jump gives W263<-.3.
m=437;eps=F(1,26250);theta=F(1,15751)
assert m*eps-A-eps < -F(3,10)
actual_lower=m*theta-F(m*(m-1),2)*theta**2
assert actual_lower>F(43,100)*L
assert F(700)*F(5,8)*A*eps==L
assert (F(2627,10)-F(700)*F(3,8))**2<F(46,25)**2*(v+L/700)
print(json.dumps({'status':'PASS_INDEPENDENT_COMMON_SMALL_NOISE','source_sha256':PIN,
 'gate_count':len(gates),'gates':{k:str(x) for k,x in gates.items()},'quartic_tensor':tensor,
 'whole_tail_constants':{'innerK':str(innerK),'outerK':str(outerK)},
 'actual_phase_denominator_counterexample_lower':str(actual_lower),
 'final_margins_afterlambda100':{k:str(x) for k,x in final.items()},
 'negative_controls':['.42 outer-tail sufficient coefficient fails','.52 inner-tail sufficient coefficient fails','quartic .8 sufficient constant fails','actual rare-jump law refutes omission of positive phase denominator'],
 'scope':'Independent algebra/closed-domain reconstruction, not acceptance of acquisition or the full conjecture. No constructor import.'},indent=2))

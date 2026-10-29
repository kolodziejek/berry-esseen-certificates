"""Exact scalar checks for the elementary compact-strip small-noise proof.

The continuous-domain reductions are derived in small-common.tex. This file
reconstructs all scalar guards, complete series bounds and quartic endpoint
checks without importing a constructor, a probability evaluator or proof cells.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
gates={}
def gate(name,x):
    x=F(x);assert name not in gates;gates[name]=x;assert x>0,(name,x)
N=700;p0=F(3,8);p1=F(93,200);v=p0*(1-p0)
L=F(1,100);A=F(3,5);d=F(1,250);H=F(46,25)
D=F(5,3);b=F(1,20);T=F(101,10000);eta=F(2,525)
alpha=F(13,25);M=5*alpha**4;zmax=F(3,2)
def Z(x):return 3*x/5+F(3,8)+x**3/840
gate('variance maximum below quarter',F(1,4)-p1*(1-p1)-L/N)
assert H/2==F(23,25)
gate('global delta bound',D-F(23,25)-F(7,10))
gate('inner delta bound',1-F(23,25)-b)
gate('Stirling segment lower',p0-D/N-F(37,100))
gate('Stirling segment upper',F(47,100)-p1-D/N)
gate('segment variance',F(37,100)*F(63,100)-F(23,100))
gate('entropy third derivative',5-F(26,100)/F(23,100)**2)
gate('log prefactor derivative',F(6,5)-F(26,100)/F(23,100))
gate('factorial remainder',F(3,8)-1/(12*F(23,100)))
gate('interior count lower',N*p0-D-1)
gate('interior count upper',N*(1-p1)-D-1)
gate('log derivative lambda coefficient',F(11,5)-1/(2*v)-D*D/(2*N*v*v))
for label,DD,bb,lower,upper in [('inner',F(1),b,F(99,100),F(101,100)),
                                ('global',D,F(7,10),F(49,50),F(51,50))]:
    x=(F(11,5)*L+(2*DD*bb+bb*bb)/(2*v)+Z(DD))/N
    gate(label+' log denominator',1-x)
    gate(label+' normal derivative lower',1-x-lower)
    gate(label+' normal derivative upper',upper-1/(1-x))
gate('phi lower',1-2*F(22,7)*F(199,500)**2)
gate('own binomial mass',2*F(199,500)*(1-(D*D/(2*v)+Z(D))/N)-F(3,4))
gate('mode variance price',1-F(1,43)-F(2,43**2)-F(39,40))
gate('mode coefficient',F(41,100)**2-F(2,5)**2*F(40,39)*F(516,515)**2)
gate('maximum binomial mass',F(17,20)**2*v-F(41,100)**2)
gate('global count ratio',F(6,5)-F(17,15))
gate('inner count ratio',F(51,50)-1-p1/(N*v))
gate('inner subsequent ratio',2-p1-1)
gate('actual conditional signs lower',p0-d)
gate('actual conditional signs upper',1-p1-d)
gate('actual favorable cubic',F(9,8)-d-F(51,64)-F(17,20)*L/N)
gate('normal variance coefficient',4*v**3-F(1,5)**2)
gate('global normal repair',4-2*D)
gate('physical own variance lower',1-D*eta-F(99,100))
gate('physical own variance upper',F(101,100)-1-D*eta)
assert eta==1/(N*p0)
for power,first,upper in [(4,5,F(13,12)),(3,3,F(5,4)),(2,5,F(5,3))]:
    gate('complete reciprocal-power sum '+str(power),
         upper-sum((F(1,j**power)for j in range(1,first+1)),F(0))-F(1,(power-1)*first**(power-1)))
def K(a):
    c=eta
    return A*A*(13*a/12+5*c/4)+3*L*(13*a*a/12+5*a*c/2+5*c*c/3)
KI=K(1+eta)/(1-b)**4;KG=K(1+eta*D)
gate('full inner fourth-moment tail',F(53,100)-KI)
gate('full outer fourth-moment tail',F(43,100)-KG)
gate('strict-event polynomial minorant max',F(11,6)**2-3)
quad_records=[]
for sign,slope,label in [(1,-F(101,100),'negative'),(-1,F(99,100),'positive')]:
    for t in [F(0),T]:
        # Lower quadratic after z^4 <= zmax^2 z^2; the original F is concave in t.
        c0=(3*alpha**2-A*A-3*t)/M
        c1=2*sign/(5*alpha)+slope-4*A*t/M
        c2=(3*alpha**2*t-6*t*t-zmax*zmax*t**3)/M
        assert c2>=0
        if sign==1:
            gate(label+' quadratic decreasing at '+str(t),-c1-2*c2*zmax)
            val=c0+c1*zmax+c2*zmax*zmax
        else:
            gate(label+' quadratic increasing at '+str(t),c1)
            val=c0
        gate(label+' quartic rectangle endpoint '+str(t),val-F(3,5))
        quad_records.append({'phase':label,'t':str(t),'coefficients':list(map(str,[c0,c1,c2])),'minimum_lower':str(val)})
gate('switch lies in inner interval',b-zmax*T)
gate('Cantelli derivative at switch',3/(1+F(9,4)*T)**2-F(101,100))
gate('Cantelli first endpoint',F(9,4)/(1+F(9,4)*T)-F(303,200)-F(3,5))
gate('Cantelli second endpoint',b*b/(T+b*b)-F(101,100)*b-F(3,5)*T)
gate('positive inner beyond switch',F(99,100)*zmax-F(3,5))
gate('own count reserve',F(3,5)*F(99,100)-F(59,100))
gate('outer Cantelli initial derivative',2*b*T/(T+b*b)**2-F(51,50))
for r in [b,F(3,10)]:gate('negative outer endpoint '+str(r),r*r/(T+r*r)-F(51,50)*r-F(7,50))
for u in [b,F(7,10)]:gate('positive outer endpoint '+str(u),F(49,50)*u-F(6,5)*F(43,100)*L/(1-u)**4-F(1,25))
gate('final inner margin',F(3,4)*(F(59,100)-F(51,50)*F(53,100))-F(2,N)-F(1,100))
gate('final negative outer margin',F(3,4)*(14-F(6,5)*F(43,100))-F(4,N)-F(1,100))
gate('final positive outer margin',3-F(4,N)-F(1,100))
# Controls reject overly coarse replacements, not the Berry--Esseen theorem.
coarse=(A*A/p0+3*L/p0**2)*F(13,12)/(1-b)**4
assert coarse>F(59,100),'A count-independent maximum variance would lose the needed margin'
u=F(3,4)
assert F(49,50)*u-F(6,5)*F(43,100)*L/(1-u)**4<0,'Do not widen the chosen phase endpoint to .75 with these bounds'
here=Path(__file__).resolve()
print(json.dumps({'status':'PASS_ELEMENTARY_COMPACT_SMALL_NOISE_SCALARS',
 'gate_count':len(gates),'positive_gates':{k:str(v)for k,v in gates.items()},
 'inner_tail_coefficient':str(KI),'outer_tail_coefficient':str(KG),
 'quartic_rectangle':quad_records,
 'negative_controls':['count-independent maximum variance is too coarse','same positive-phase bound fails at .75'],
 'proof_sha256':hashlib.sha256(here.with_name('small-common.tex').read_bytes()).hexdigest(),
 'scope':'Complete rational guards after analytic reductions; no Pinelis/Poisson evaluator, proof cells, sampling or acquisition claim.'},indent=2))

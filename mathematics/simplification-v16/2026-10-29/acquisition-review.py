"""Independent exact review of post-entry acquisition and its local join.

No constructor is imported or executed. Polynomial identities, scalar licenses,
Taylor coefficients on the two infinite rays, and actual finite laws are
checked separately from the constructor's field-arithmetic implementation.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
parser=argparse.ArgumentParser();parser.add_argument('--source-root',type=Path,required=True)
source_root=parser.parse_args().source_root.resolve()
here=Path(__file__).resolve().parent
manifest=json.loads((here/'acquisition-review-sources.json').read_text())
for relative,pin in manifest['sources'].items():
    data=(source_root/relative).read_bytes()
    assert hashlib.sha256(data).hexdigest()==pin, relative
    assert hashlib.sha256(data+b'\n').hexdigest()!=pin

gates={}
def positive(name,value):
    value=F(value);assert name not in gates;assert value>0,(name,value);gates[name]=str(value)

# Tiny polynomial ring Q[p,a0,a1]. Independent exact expansion of the
# deterministic central-plus-outer gap cost; no polynomial package needed.
class P:
    def __init__(self,d):self.d={k:F(v) for k,v in d.items() if v}
    @staticmethod
    def cast(x):return x if isinstance(x,P) else P({(0,0,0):F(x)})
    def __add__(self,other):
        d=self.d.copy()
        for k,v in P.cast(other).d.items():d[k]=d.get(k,0)+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,other):return self+-P.cast(other)
    def __rsub__(self,other):return P.cast(other)+-self
    def __mul__(self,other):
        d={}
        for k,v in self.d.items():
            for l,w in P.cast(other).d.items():
                key=tuple(a+b for a,b in zip(k,l));d[key]=d.get(key,0)+v*w
        return P(d)
    __rmul__=__mul__
    def __pow__(self,n):
        result=P.cast(1)
        for unused in range(n):result=result*self
        return result

p=P({(1,0,0):1});a=P({(0,1,0):1});b=P({(0,0,1):1});q=1-p;d=a+b
x,y=p-a,q-b
constant_gap_change=6*(q*y+p*x-x*x-y*y-x*y+p*q)
assert (constant_gap_change-6*(d*(1-d)+a*b)).d=={}
# The conditional third-moment identity: expectation of the difference is
# zero exactly when E Z=M, not for an arbitrary relaxed noise law.
Z,M=P({(1,0,0):1}),P({(0,1,0):1})
assert (Z**3-M**3-(Z-M)**2*(Z+2*M)-3*M*M*(Z-M)).d=={}
# Multiply the one-sided cubic factor by a^2, then average powers of Z.
# E[(a-Z)(aZ+t)^2]=a^3 t-a^2 mu3-a t^2 for centered Z.
a,t,mu=P({(1,0,0):1}),P({(0,1,0):1}),P({(0,0,1):1})
averaged=a**3*t+2*a*a*t*0+a*t*t-a*a*mu-2*a*t*t-t*t*0
assert (averaged-(a**3*t-a*a*mu-a*t*t)).d=={}

sl,su=F('3.162277660'),F('3.162277661')
budget,D0,N=F('32.20665378'),F('.047'),700
positive('sqrt10 lower',10-sl*sl);positive('sqrt10 upper',su*su-10)
positive('initial defect',N*D0-budget)
z=(sl-1-D0)/3;positive('central gap product',z);positive('product below 1',1-z)
def Q(p,sigma):return (sigma+1)*p*p+(sigma-1)*(1-p)**2-6*p*(1-p)
lo,hi=F('.36'),F('.48');p0,p1=F(3,8),F(93,200)
positive('minimizer above .36',(4-su)/2-lo)
positive('minimizer below .48',hi-(4-sl)/2)
for endpoint in (lo,hi):
    qb=Q(endpoint,sl);positive('coarse square base '+str(endpoint),qb)
    positive('coarse probability exclusion '+str(endpoint),4*z**3*qb*qb-D0**2)
positive('ell greater than 1.67',4*z-F('1.67')**2)
positive('positive residual price', (1-hi)*((sl+5)*z+2*(sl-1))-F('5.2'))
positive('negative residual price', lo*((sl+7)*z+2*(sl+1))-F('5.2'))
positive('theta below .006',F('1.67')*F('5.2')*F('.006')-D0)
positive('ell greater than 1.99',4*F('.994')-F('1.99')**2)
positive('inward below .2',4*z*lo*(1-lo)-F('.8')**2)
Cmin=min(3*(sl+1)*(1-hi),3*(sl+3)*lo)
Qmax=max(Q(lo,su),Q(hi,su))
positive('all direct noise branches positive',Cmin-(su+7)/5)
positive('all direct branches increasing in d',6*F('.994')*F('.6')-F('.006')*(su+7))
positive('large inward endpoint impossible',F('1.99')*F('.994')*6*F('.004')*F('.996')-D0)
positive('theta monotonic before variance removal',(2-3*F('.006'))*Cmin-3*Qmax)
positive('left fine base',Q(p0,sl));positive('left fine square',Q(p0,sl)**2-D0**2*p0*(1-p0))
positive('right fine direct',2*Q(p1,sl)-D0)
positive('fine minimizer left',(4-su)/2-p0);positive('fine minimizer right',p1-(4-sl)/2)
fineC=min(3*(sl+1)*(1-p1),3*(sl+3)*p0)
positive('theta below .0036',F('1.99')*fineC*F('.0036')-D0)
positive('ell greater than 1.996',4*F('.9964')-F('1.996')**2)
vmin=p0*(1-p0)
positive('Bernoulli rho bound',F('1.1')**2*vmin-(1-2*vmin)**2)
positive('rho price',sl-1-F('2.16'))
positive('rho below 9/8',F(9,8)-F('1.1')-D0/F('2.16'))
betal=1-2*p1-2*(1-p1)*F('.0036');betau=1-2*p0+2*p0*F('.0036')
assert betal==F('.066148') and betau==F('.2527')
for label,prob,sig,root in [('negative',p0,sl+1,F(3)),('positive',1-p1,sl-1,F('2.6')),('left positive',F('.6'),sl-1,F('2.7'))]:
    positive('AMGM radical '+label,6*F('.996')*sig*prob-root*root)
Y0=3*(sl+3)*p0-(su+7)*F('.004')+6
Y1=3*(sl+1)*(1-p1)-(su+5)*F('.004')+F('5.2')
Y1left=3*(sl+1)*F('.6')-(su+5)*F('.004')+F('5.4')
positive('negative cubic price',Y0-F('12.8'))
positive('positive cubic price',Y1-F('11.8'))
positive('left cubic price',Y1left-F('12.8'))
positive('common noise ceiling',F('1.996')**3*F('11.8')*F('.35')-budget)
positive('left noise ceiling',F('1.996')**3*F('12.8')*F('.32')-budget)

# Heat constants are licensed on n>=42, with no raw-H restriction.
S=F(81,80);eta=F(8,875);c0=F(819,2000);rho=F(9,8)
positive('heat scaling',S*S-F(42,41))
positive('heat eta',eta-S*S*(2*S+1)/(2*(S+1)**2*42))
positive('CE lower multiplier',(19+6*sl)/(72*F(22,7))-c0*c0)
def translate(coeff,point):
    return [sum(coeff[j]*comb(j,i)*point**(j-i) for j in range(i,len(coeff))) for i in range(len(coeff))]
rays=[]
for label,point,directional_beta in [('negative',F('1.996')*(p0+F('.6')),-betal),('positive',F('1.996')*(1-p1+F('.6')),betau)]:
    positive(label+' heat radius',point*point-3)
    qp=[eta*rho,3*directional_beta,F(3,2)*rho,-F(1)]
    lp=[F(2,5)*(F(1,2)+eta)+3*c0*directional_beta,3*c0*rho,F(1,5)-3*c0]
    qt,lt=translate(qp,point),translate(lp,point)
    for i,value in enumerate(qt):positive(label+' negative Q ray coefficient '+str(i),-value)
    for i,value in enumerate(lt):positive(label+' negative L ray coefficient '+str(i),-value)
    h=S**3*(F(2,5)*((point**3-3*point)/6+abs(point**4-6*point**2+3)/72)+point**5/4100+3*point/820+17*(3*point*point-2)/78720)
    positive(label+' boundary exclusion',-h-c0*qt[0])
    rays.append({'ray':label,'boundary':str(point),'shifted_Q':list(map(str,qt)),'shifted_L':list(map(str,lt)),'boundary_margin':str(-h-c0*qt[0])})

# Actual finite marginals, using interval enclosures of sqrt10 rather than
# the constructor's quadratic-field arithmetic. The law itself is rational.
actual=[]
def actual_law(p,amplitude,lam,group=0,n=700):
    q=1-p;s=lam/n;prob=q if group==0 else p
    inward=s/(prob*amplitude)
    if group==0:
        noise=[(-amplitude,inward/(amplitude+inward)),(inward,amplitude/(amplitude+inward))]
        atoms=[(u-p,q*w) for u,w in noise]+[(q,p)]
    else:
        noise=[(-inward,amplitude/(amplitude+inward)),(amplitude,inward/(amplitude+inward))]
        atoms=[(-p,q)]+[(q+u,p*w) for u,w in noise]
    atoms=sorted(atoms)
    assert sum(w for x,w in atoms)==1 and sum(x*w for x,w in atoms)==0
    variance=sum(x*x*w for x,w in atoms);M=sum(abs(x)**3*w for x,w in atoms);G=sum(x**3*w for x,w in atoms)
    J=sum((right-left)**2*sum(x*w for x,w in atoms if x>=right) for (left,unused),(right,unused2) in zip(atoms,atoms[1:]))
    # All these three-point laws have at most one outer gap on each side,
    # so the unsimplified gap budget is an exact identity, coefficient by
    # coefficient in 1 and sqrt10. This tests the actual gap sum itself.
    Am=-max(x for x,w in atoms if x<0);Ap=min(x for x,w in atoms if x>0)
    a0,a1=p-Am,q-Ap;dd=a0+a1
    cost_const=p*q*(p*p-q*q-6*p*q)+6*p*q*(dd*(1-dd)+a0*a1)
    cost_sigma=p*q*(p*p+q*q)
    for x,w in atoms:
        magnitude=abs(x);mean=q if x>0 else p
        residual=x-(q if x>0 else -p)
        cost_sigma+=w*residual**2*(magnitude+2*mean)
        cost_const+=w*residual**2*((-1 if x>0 else 1)*(magnitude+2*mean)+6*(Ap if x>0 else Am))
    assert cost_const==3*M-G-3*J and cost_sigma==M
    denom=variance**3
    Dlo=(3+sl)*M-G-3*J;Dup=(3+su)*M-G-3*J
    assert Dlo>=0
    licensed=n*n*Dup*Dup<budget*budget*denom
    rejected=n*n*Dlo*Dlo>budget*budget*denom
    assert licensed or rejected
    if licensed:
        assert p0<p<p1 and inward<F('.004') and s/variance<F('.0036')
        assert F('1.996')**2*variance<1 and M*M<F(9,8)**2*denom
        assert lam<F('.35')
    record={'p':str(p),'amplitude':str(amplitude),'lambda':str(lam),'group':group,'budget_licensed':licensed}
    actual.append(record)
    return licensed
for p in [F(2,5),F(21,50),F(9,20)]:
    for group in (0,1):
        actual_law(p,F(3,5),F(1,1000000),group)
assert actual_law(F(21,50),F(4,5),F(1,1000000))
# This last genuine rational marginal meets the budget but has U0=-.8;
# it refutes dropping the contact premise, not the conjecture.

# Composition licenses: identical raw variables, both closed noise endpoints,
# and an actual reflected atom distinguish >= from equality.
positive('raw threshold join',F(46,25)-F('1.83605680'))
assert [F(0),F(1,100),F(7,20)]==[F(0),F('.01'),F('.35')]
for p in [p0,F(2,5),p1]:
    for lam in [F(0),F(1,100),F(7,20)]:
        s=lam/700;v=p*(1-p);ell2=1/(v+s);theta=s*ell2
        assert v*ell2+theta==1 and theta/ell2==s
        assert lam==700*theta/ell2
        for H in [F(-46,25),F(0),F(46,25)]:
            # Squared physical displacement t-np = H/ell.
            assert H*H/ell2==H*H*(v+s)
# S is an actual two-point sum at n=1. Reflection produces an extra atom.
atoms=[(-F(1),F(1,2)),(F(1),F(1,2))];H=F(1)
closed=sum(w for x,w in atoms if x<=H);strict=sum(w for x,w in atoms if x<H)
reflected=sum(w for x,w in atoms if -x<=-H)
assert reflected==1-strict and reflected>1-closed

print(json.dumps({'status':'PASS_INDEPENDENT_ACQUISITION_JOIN_REVIEW','scalar_gate_count':len(gates),'gates':gates,
 'symbolic_identities':['central and outer gap constant','conditional third-moment decomposition','one-sided cubic factor'],
 'ray_coefficients':rays,'actual_laws':actual,
 'negative_controls':['geometry alone does not imply amplitude .6','reflected closed discrepancy need not equal negative closed discrepancy','source alteration rejected by pins'],
 'source_pins':manifest['sources'],'scope':'Independent post-entry algebra and join review; retained contact/heat/entry and finite base remain explicit inputs'},indent=2))

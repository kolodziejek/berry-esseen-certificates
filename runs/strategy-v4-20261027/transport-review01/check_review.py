"""Independent formal algebra and sign controls, not schedule acceptance."""
from fractions import Fraction as F

def add(*xs):
    out={}
    for x in xs:
        for k,v in x.items(): out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def mul(x,y):
    out={}
    for k,v in x.items():
        for l,w in y.items():
            m=tuple(sorted(k+l));out[m]=out.get(m,0)+v*w
    return {k:v for k,v in out.items() if v}
def neg(x):return {k:-v for k,v in x.items()}
def sub(x,y):return add(x,neg(y))
def var(name):return {(name,):F(1)}
rn,f,fb,gh,gb,g0,rho,rhob,c=[var(s) for s in 'rootn F FB GH GB G0 rho rhoB c'.split()]
a=sub(mul(rn,sub(f,gh)),mul(c,rho))
left=sub(add(a,mul(c,rhob)),mul(rn,sub(fb,gb)))
rhs=add(mul(rn,add(f,neg(fb),neg(gh),g0)),mul(rn,sub(gb,g0)),mul(c,sub(rhob,rho)))
assert left==rhs
print('Formal fixed-target master identity: every polynomial coefficient agrees.')
old_times_rho=sub(mul(rhob,add(mul(c,rho),a)),mul(rho,mul(rn,sub(fb,gb))))
difference=sub(old_times_rho,mul(rho,left))
assert difference==mul(a,sub(rhob,rho)) and difference
print('Rejected retaining the old ratio-score left side: after multiplying by rho, the defect is a(rhoB-rho).')
assert F(1,100)*(F(5,4)-F(3,2))==F(-1,400)
# The negative moment gain must use an upper multiplier for a lower bound.
gain=F(-1,7); low=F(2,5); target=F(40973,100000); high=F(2113,5000)
assert low<target<high and high*gain<=target*gain<low*gain
print('Negative gain control: lower-multiplier substitution is rejected.')
# A non-strict upper envelope does not exclude the a=0, CB=c boundary.
a0=F(0); cb=target
assert a0+F(5,4)*(target-cb)==0
assert not (a0+F(5,4)*(target-cb)<0)
print('Equality boundary retained: a=0 and CB=c is compatible with an RHS upper bound of zero.')
print('Scope: formal identities and sign controls; no claim about complete Fourier bounds, row covers, strict native predicates or theorem acceptance.')

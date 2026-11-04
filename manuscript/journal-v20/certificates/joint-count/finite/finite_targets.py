"""Same four witnesses with an explicitly supplied intermediate loss coefficient."""
from fractions import Fraction as F
from model import targets,ETA
from polynomials import X,Y,add,scalar,scale,mul,power

def parameterized_targets(c,eta):
    """Final score targets are external; eta changes only the lower-loss witness."""
    out=targets(c);T=c['ownhi']*c['lmax'];t=scale(X,T);gap=1-c['d0'];change=ETA-F(eta)
    for sign,zmax,name in [(-1,F(5,3),'negative_quartic'),(1,F(6,5),'positive_quartic')]:
        r=scale(mul(t,Y),zmax);d=add(scalar(gap),scale(r,-sign))
        out[name]=add(out[name],scale(power(d,4),change))
    for sign,zmax,name in [(-1,F(5,3),'negative_Cantelli'),(1,F(6,5),'positive_normal')]:
        r=add(scale(t,zmax),mul(add(scalar(F(1,2)),scale(t,-zmax)),Y));d=add(scalar(gap),scale(r,-sign))
        factor=mul(t,power(d,4))
        if sign<0:factor=mul(factor,add(t,power(r,2)))
        out[name]=add(out[name],scale(factor,change))
    return out

def scalar_gate(c,eta,kind):
    eta=F(eta)
    # Both b∈[m,1] and t/lambda∈[ownlo,ownhi] have the same law.
    reserve=min(c['mass']*eta*c['ownlo'],eta*c['ownhi'])-c['repair']/c['N']
    if kind=='positive_allowance':allowance=c['barrier_allowance']
    elif kind=='binomial_reserve':allowance=c['epsilon']*c['rhoB_lower']/c['lmax']
    else:allowance=-F(1,1000)
    return reserve+allowance

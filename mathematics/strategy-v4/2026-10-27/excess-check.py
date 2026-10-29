"""Independent bounded identities and finite-law controls; no native certificate code.

Exact Fraction algebra verifies polynomial identities, not analytic compactness or
uniform Fourier bounds. The proof of those analytic claims is in excess.tex.
"""
from fractions import Fraction as Q
from collections import defaultdict
from itertools import product
import json


class Poly:
    """Sparse exact Laurent polynomial; variables have fixed integer exponents."""
    names = 's H c rho beta gamma J J1 J2 M4 M5 X4 F a eps L phi'.split()
    size = len(names)

    def __init__(self, value=0):
        self.d = value if isinstance(value, dict) else {(0,) * self.size: Q(value)}
        self.d = {k: Q(v) for k, v in self.d.items() if v}

    @classmethod
    def var(cls, name, power=1):
        k = [0] * cls.size
        k[cls.names.index(name)] = power
        return cls({tuple(k): Q(1)})

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        d = defaultdict(Q, self.d)
        for k, v in other.d.items(): d[k] += v
        return Poly(dict(d))

    __radd__ = __add__
    def __neg__(self): return Poly({k: -v for k, v in self.d.items()})
    def __sub__(self, other): return self + (-other if isinstance(other, Poly) else -Q(other))
    def __rsub__(self, other): return -self + other
    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        d = defaultdict(Q)
        for a, x in self.d.items():
            for b, y in other.d.items(): d[tuple(i+j for i, j in zip(a, b))] += x*y
        return Poly(dict(d))
    __rmul__ = __mul__
    def __pow__(self, n):
        assert n >= 0
        r = Poly(1)
        for _ in range(n): r = r*self
        return r


v = {name: Poly.var(name) for name in Poly.names}
s,H,c,rho,beta,gamma,J,J1,J2,M4,M5,X4,F,a,eps,L,phi = [v[x] for x in Poly.names]
si = Poly.var('s', -1)
Kq = M5*Q(1,4)-rho*M4*Q(1,2)-beta*gamma*Q(3,2)+rho*Q(1,2)
K1 = X4-3*beta-rho*gamma*Q(3,2)
# Construct the polynomial Q_H first; take its moments independently.
q0 = F+(H*phi+c*rho)*si**3*Q(1,2)
q1 = -phi*si-3*c*beta*si**3
q2 = -(H*phi+3*c*rho)*si**3*Q(1,2)
q3 = c*si**3
Qtau = q0+q1*gamma*Q(1,2)+q2*M4*Q(1,3)+q3*M5*Q(1,4)
assert not (Qtau-(F-gamma*phi*si*Q(1,2)+(H*phi*(3-M4)*Q(1,6)+c*Kq)*si**3)).d
M = s*(q1+q2*gamma+q3*X4)
assert not (M+phi-(-gamma*H*phi*si**2*Q(1,2)+c*K1*si**2)).d
G = c*beta*J*Q(3,2)+(H*phi+3*c*rho)*J1-3*c*J2
gap_slack = -q1*J*Q(1,2)-2*q2*J1-3*q3*J2-L
assert not (gap_slack-(phi*J*si*Q(1,2)+G*si**3-L)).d
# Use the hinge identity, keeping the excess independent of the coefficient c.
Phi = F-(c*rho+a)*si
z = H*si
T = Phi-eps*Q(1,2)-gamma*phi*si*Q(1,3)+z*(M+phi)-z*z*(F-Phi)
P0 = H*H*(c*rho+a+gamma*phi*Q(1,2))-H*(c*K1+phi*(M4-3)*Q(1,6))+c*Kq
assert not (s*(Qtau-T)-(c*rho+a-gamma*phi*Q(1,6)+P0*si**2+s*eps*Q(1,2))).d
Rc = c*(beta*J*Q(3,2)+3*rho*J1-3*J2-Kq)+H*(c*K1+phi*(J1+(M4-3)*Q(1,6)))-H*H*(c*rho+gamma*phi*Q(1,2))-s**3*eps*Q(1,2)
target = (s*s+H*H)*a+s*s*c*rho-s*s*phi*(gamma+3*J)*Q(1,6)+s**3*L-Rc
assert not (s**3*((Qtau-T)-gap_slack)-target).d
wrong = s*s*a+s*s*c*rho-s*s*phi*(gamma+3*J)*Q(1,6)+s**3*L-Rc
assert (target-wrong).d == (H*H*a).d  # Missing H^2 a must fail.
print('EXACT PASS: contact polynomial moments, two slack expansions, hinge elimination, (n+H^2)a.')
print('NEGATIVE CONTROL: replacing (n+H^2)a by n a leaves exactly H^2 a.')


def convolution(law, n):
    d = {Q(0): Q(1)}
    for _ in range(n):
        out = defaultdict(Q)
        for x,p in d.items():
            for y,q in law.items(): out[x+y] += p*q
        d = dict(out)
    return d


def cdf(law, h, closed=True):
    return sum((p for x,p in law.items() if x <= h if closed), Q(0)) if closed else sum((p for x,p in law.items() if x < h), Q(0))


def poly_mul(x, y):
    out = [Q(0)]*(len(x)+len(y)-1)
    for i,a0 in enumerate(x):
        for j,b0 in enumerate(y): out[i+j] += a0*b0
    return out


def direct_mixture_derivative(law, n, threshold, point):
    atoms = [(x,[p,-p]) for x,p in law.items()]+[(point,[Q(0),Q(1)])]
    total = [Q(0)]*(n+1)
    for tup in product(atoms, repeat=n):
        if sum(x for x,p in tup) <= threshold:
            p = [Q(1)]
            for x,q in tup: p = poly_mul(p,q)
            for j,v in enumerate(p): total[j] += v
    return total[1]


laws = {
    'symmetric': {Q(-1):Q(1,2), Q(1):Q(1,2)},
    'skew_positive': {Q(-1,2):Q(4,5), Q(2):Q(1,5)},
    'skew_reflected': {Q(1,2):Q(4,5), Q(-2):Q(1,5)},
    'three_point_zero': {Q(-2):Q(1,8),Q(0):Q(3,4),Q(2):Q(1,8)},
    'four_point': {Q(-2):Q(1,10),Q(-1,2):Q(2,5),Q(1,2):Q(2,5),Q(2):Q(1,10)},
}
for m in [10,100,1000]:
    laws['far_atom_'+str(m)] = {Q(-m):Q(1,2*m**3),Q(m):Q(1,2*m**3),Q(-1):Q(m-1,2*m),Q(1):Q(m-1,2*m),Q(0):Q(m*m-1,m**3)}
cases = derivatives = collisions = 0
for name,law in laws.items():
    assert sum(law.values()) == 1
    assert sum(x*p for x,p in law.items()) == 0
    assert sum(x*x*p for x,p in law.items()) == 1
    xs = sorted(law)
    for n in [2,3]:
        sn, prev = convolution(law,n), convolution(law,n-1)
        thresholds = sorted(set([Q(-3,2),Q(0),Q(7,4),min(sn),max(sn),*list(sn)[::max(1,len(sn)//3)]]))
        for h in thresholds:
            # Direct zero-bias convolution integral, splitting at every jump.
            cuts = sorted(set(xs+[h-t for t in prev if xs[0] < h-t < xs[-1]]))
            integ = Q(0)
            for lo,hi in zip(cuts,cuts[1:]):
                mid=(lo+hi)/2
                tau=sum((x*p for x,p in law.items() if x>=mid),Q(0))
                integ += (hi-lo)*tau*cdf(prev,h-mid)
            T=sum(((x*x-h*x)*p for x,p in sn.items() if x<=h),Q(0))/n
            assert integ == T
            F0=cdf(sn,h); Mraw=sum((x*p for x,p in sn.items() if x<=h),Q(0))
            hinge=sum((x-h)*abs(x-h)*p for x,p in sn.items())
            assert hinge == n+h*h-2*n*T+2*h*Mraw-2*h*h*F0
            for lo,hi in zip(xs,xs[1:]):
                mass=sum((p for t,p in prev.items() if lo<=h-t<hi),Q(0))
                assert cdf(prev,h-lo)-cdf(prev,h-hi) == mass
                wrongmass=sum((p for t,p in prev.items() if lo<=h-t<=hi),Q(0))
                collisions += wrongmass != mass
            for point in [Q(-3,2),Q(0),Q(5,2)]:
                direct=direct_mixture_derivative(law,n,h,point)
                assert direct == n*(cdf(prev,h-point)-F0)
                derivatives += 1
            cases += 1
assert collisions > 0
print(json.dumps({'finite_laws':len(laws),'zero_bias_and_hinge_cases':cases,'raw_mixture_derivatives':derivatives,'detected_closed_upper_gap_mutations':collisions},sort_keys=True))

# Open events are not upper semicontinuous at the reflected jump.
law=laws['symmetric']; y0=Q(1); h=Q(0)
assert cdf(law,h-y0,False)==0 and cdf(law,h-(y0-Q(1,10)),False)==Q(1,2)
assert cdf(law,h-y0)==Q(1,2)
print('NEGATIVE CONTROL: open-event contact loses upper semicontinuity at an atom.')
# Uniform third-moment bounds do not imply UI3; this exact standardized family
# converges weakly to symmetric Bernoulli but its third absolute moment tends to 2.
for m in [10,100,1000]:
    law=laws['far_atom_'+str(m)]
    assert sum(abs(x)**3*p for x,p in law.items()) == Q(2)-Q(1,m)
    assert sum(abs(x)**3*p for x,p in law.items() if abs(x)>m/2) == 1
print('NEGATIVE CONTROL: bounded rho family has rho->2 but limiting Bernoulli rho=1 (UI3 fails).')
# A weak comparison endpoint cannot exclude zero excess.
c0,cb,rho_b=Q(3,4),Q(1,2),Q(1)
repair=rho_b*(c0-cb)
assert rho_b*(cb-c0)+repair==0
print('NEGATIVE CONTROL: comparison <= exact binomial margin permits a=0.')
print('Scope: exact algebra and finite-law identities only; no certificate acceptance or optimizer sampling.')

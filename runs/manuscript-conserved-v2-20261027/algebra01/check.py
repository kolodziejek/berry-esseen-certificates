"""Exact formal algebra and scope controls for the promoted conserved identity.

No native Fourier/resource checker is imported or executed.
The analytic integration and inversion arguments are reviewed in the TeX proof.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import subprocess

NAMES = ['C','rho','beta','gamma','phi0','phase','H','s','cdf0',
         'J','J1','J2','L','m4','m5','signed4','epsilon','k']
ZERO = (0,)*len(NAMES)


class P:
    def __init__(self, value=0):
        self.d = value if isinstance(value, dict) else ({ZERO:F(value)} if value else {})

    def __add__(self, other):
        other = other if isinstance(other,P) else P(other)
        out = dict(self.d)
        for k,v in other.d.items(): out[k] = out.get(k,F(0))+v
        return P({k:v for k,v in out.items() if v})

    __radd__ = __add__

    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self, other): return self + (-other if isinstance(other,P) else -P(other))
    def __rsub__(self, other): return P(other)-self

    def __mul__(self, other):
        other = other if isinstance(other,P) else P(other)
        out = {}
        for a,x in self.d.items():
            for b,y in other.d.items():
                k = tuple(i+j for i,j in zip(a,b))
                out[k] = out.get(k,F(0))+x*y
        return P({k:v for k,v in out.items() if v})

    __rmul__ = __mul__

    def __pow__(self, n):
        if n<0:
            assert len(self.d)==1
            (k,v),=self.d.items()
            return P({tuple(n*x for x in k):v**n})
        out=P(1)
        for _ in range(n):out=out*self
        return out

    def __truediv__(self, other):
        other = other if isinstance(other,P) else P(other)
        return self*(other**-1)


def variable(name):
    e=list(ZERO);e[NAMES.index(name)]=1
    return P({tuple(e):F(1)})


def same(a,b):return not (a-b).d


v={name:variable(name) for name in NAMES}
C,rho,beta,gamma,phi0,phase,H,s,cdf0,J,J1,J2,L,m4,m5,signed4,eps,k=[v[x] for x in NAMES]
n=s*s;z=H/s;phi=phi0*phase
Factual=cdf0+C*rho/s
Kq=m5/4-rho*m4/2-3*beta*gamma/2+rho/2
K1=signed4-3*beta-3*rho*gamma/2

# Integrate n Q_H against the independently listed zero-bias moments.
EQ=(n*Factual+(H*phi+C*rho)/(2*s)
    -(s*phi+3*C*beta/s)*gamma/2
    -(H*phi+3*C*rho)/(2*s)*m4/3+C/s*m5/4)/n
second_without_T=Factual-gamma*phi/(2*s)+(H*phi*(3-m4)/6+C*Kq)/(s**3)
assert same(EQ,second_without_T)

# Multiply contact by X, use the four actual signed moments, divide by sqrt n.
M=(-s*phi-3*C*beta/s-(H*phi+3*C*rho)*gamma/(2*s)+C*signed4/s)/s
assert same(M+phi,-gamma*z*phi/(2*s)+C*K1/n)

# The hinge comparison and the second slack produce the printed P_0.
delta_q=eps+2*gamma*phi/(3*s)
T=cdf0-delta_q/2+z*(M+phi)-z*z*(C*rho/s)
Azero=second_without_T-T
P0=H*H*(C*rho+gamma*phi/2)-H*(C*K1+phi*(m4-3)/6)+C*Kq
assert same(s*Azero,C*rho-gamma*phi/6+P0/n+s*eps/2)
G=3*C*beta*J/2+(H*phi+3*C*rho)*J1-3*C*J2
Agap=phi*J/(2*s)+G/(s**3)-L
raw=C*(3*beta*J/2+3*rho*J1-3*J2-Kq)+H*(C*K1+phi*(J1+(m4-3)/6))-H*H*(C*rho+gamma*phi/2)-n*s*eps/2
assert same(raw,G-P0-n*s*eps/2)
CE=k*phi0/6;D=k*rho-gamma-3*J
lhs=n*(C-CE)*rho+n*CE*rho*(1-phase)+n*phi0*phase*D/6+n*s*L
assert same(lhs-raw,-n*s*(Agap-Azero))
unweighted=n*(C-CE)*rho+n*phi0*D/6+n*s*L
assert same(lhs,unweighted+n*(1-phase)*(CE*rho-phi0*D/6))

# Formal false-rule controls: wrong hinge sign, lost scale, or lost leakage.
assert not same(lhs-raw,-n*s*(Agap-(Azero+eps)))
assert not same(lhs-raw,-n*(Agap-Azero))
assert not same(lhs-raw,-n*s*((Agap+L)-Azero))

# Endpoint atom control for the gap identity: nu=delta_b, Q=1 on [a,b].
a,b=F(-1),F(2)
gap_slack=F(0)
correct_leakage=F(0)
closed_upper_endpoint_leakage=b-a
assert gap_slack==correct_leakage
assert gap_slack != -closed_upper_endpoint_leakage

# The extra phase price is not positive from arbitrary loose bounds alone.
rho_value=F(1);defect_upper=F(10)
assert F(819,2000)*rho_value-defect_upper/15 < 0
N=F(42);raw_upper=F(20)
assert 1-5*raw_upper/(2*N)<0

path='manuscript/arxiv-v1/appendices/fourier-analysis.tex'
old=subprocess.check_output(['git','show','ec370aa:'+path],text=True)
new=Path(path).read_text()
main=Path('manuscript/arxiv-v1/sections/05b-conserved.tex').read_text()
labels=lambda text:set(re.findall(r'\\label\{([^}]+)\}',text))
missing=labels(old)-(labels(new)|labels(main))
assert missing=={'ms:fourier:afcore:lem:physical-defect'}
assert not labels(new)&labels(main)
marker='\\subsubsection{Signed moments with a common first moment}'
normalise=lambda text:re.sub(r'(?<![0-9.])\.(?=[0-9])','0.',text)
assert normalise(old[old.index(marker):]) == new[new.index(marker):]
print(json.dumps({
    'status':'PASS_PROMOTED_IDENTITY_ALGEBRA_AND_PRESERVATION',
    'algebra':'zero-bias contact integral, truncated first moment, second slack, conserved identity and unweighting regrouping',
    'negative_controls':['wrong hinge-remainder sign','missing sqrt(n) scale','omitted leakage','upper endpoint atom incorrectly included','loose defect cap giving negative phase price','raw ceiling giving nonpositive density floor'],
    'preservation':'entire coefficient atlas and following sections unchanged modulo leading zeros',
    'alias_required_in_root_geometry':sorted(missing),
    'scope':'formal algebra and source-preservation checks; no native certificate or full analytic-chain acceptance'
},indent=2))

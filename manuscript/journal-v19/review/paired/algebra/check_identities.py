#!/usr/bin/env python3
"""Bounded exact algebra audit, not a numerical-family acceptance program."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('optimization forbidden')
NAMES = ('x', 'g', 'm4', 'm5', 'm6', 'R', 'M', 't', 'h')
ZERO = (0,) * len(NAMES)

class P:
    def __init__(self, value=0):
        self.terms = ({k:F(v) for k,v in value.items() if v}
                      if isinstance(value, dict) else ({ZERO:F(value)} if value else {}))
    def __add__(self, other):
        other = other if isinstance(other, P) else P(other)
        ans = dict(self.terms)
        for k,v in other.terms.items(): ans[k] = ans.get(k,F(0)) + v
        return P(ans)
    __radd__ = __add__
    def __neg__(self): return P({k:-v for k,v in self.terms.items()})
    def __sub__(self, other): return self + -(other if isinstance(other,P) else P(other))
    def __rsub__(self, other): return -self + other
    def __mul__(self, other):
        other = other if isinstance(other,P) else P(other)
        ans = {}
        for a,v in self.terms.items():
            for b,w in other.terms.items():
                k = tuple(i+j for i,j in zip(a,b))
                ans[k] = ans.get(k,F(0)) + v*w
        return P(ans)
    __rmul__ = __mul__
    def __pow__(self, n):
        if type(n) is not int or n < 0: raise ValueError('nonnegative integer degree')
        out = P(1)
        for _ in range(n): out = out*self
        return out
    def derivative(self, name):
        j = NAMES.index(name); out = {}
        for k,v in self.terms.items():
            if k[j]:
                a = list(k);a[j]-=1;out[tuple(a)] = v*k[j]
        return P(out)

def variable(name):
    k = [0]*len(NAMES);k[NAMES.index(name)] = 1
    return P({tuple(k):F(1)})

x,g,m4,m5,m6,R,M,t,h = map(variable,NAMES)

def expectation(poly):
    moments = {0:P(1),1:P(0),2:P(1),3:g,4:m4,5:m5,6:m6}
    out = P(0)
    for k,c in poly.terms.items():
        if k[0] not in moments: raise ValueError('unknown moment')
        a = list(k);a[0]=0
        out += P({tuple(a):c})*moments[k[0]]
    return out

def require_identity(lhs,rhs):
    if (lhs-rhs).terms: raise ValueError('nonzero polynomial residual')

def main():
    out = Path(sys.argv[1]);out.mkdir(exist_ok=False)
    Q=x*x-g*x-1
    p=R*(M-1)+(10-2*M)*t-R*t*t+t**3
    q=R*(M-1)+(2*M-10)*t-R*t*t-t**3
    identities = [
      ('pearson_second',expectation(Q*Q),m4-1-g*g),
      ('pearson_fifth',g**3+2*g+expectation(Q*Q*(x+2*g)),m5),
      ('pearson_sixth',1+3*g*g+g**4+expectation(Q*Q*((x+g)**2+2*g*g+2)),m6),
      ('signed_upper_z',8*t-t**3+(R-2*t)*(M-1-t*t),p),
      ('signed_lower_z',-8*t+t**3+(R+2*t)*(M-1-t*t),q),
      ('positive_z_derivative',(-q).derivative('t'),10-2*M+2*R*t+3*t*t),
      ('quadratic_upper_p',R*(M-1)+(10-2*M)*t-(R-g)*t*t-p,t*t*(g-t)),
      ('quadratic_upper_q',R*(M-1)+(2*M-10)*t-R*t*t-q,t**3),
      ('positive_c_upper',(2-h*h)*g-(2-t*t)*t,(g-t)*(2-h*h)+t*(t*t-h*h)),
      ('positive_c_lower',(3-m4)*t-(3-M)*h,(M-m4)*t+(3-M)*(t-h)),
      ('dominant_P',p-q,4*(5-M)*t+2*t**3),
    ]
    for _,lhs,rhs in identities: require_identity(lhs,rhs)
    # Independent Gaussian-moment recurrence, after division by t^3.
    moment = {0:F(1)}
    for j in range(1,6): moment[j]=(2*j-1)*moment[j-1]
    gaussian = [moment[5]/(6**4),moment[4]/(2*6**2),moment[1],moment[3]/6]
    assert gaussian == [F(35,48),F(35,24),F(1),F(5,2)]
    rejected = []
    for name,lhs,rhs in identities[:8]:
        try: require_identity(lhs,rhs+1)
        except ValueError: rejected.append(name+'_changed_constant')
        else: raise AssertionError('false identity admitted')
    # The old damping constant is invalid above M=2.
    n=47; mm=F(5,2)
    assert F(43,96)*(1-F(2,n)) > (45-mm)/96*(1-F(2,n))
    result = {'schema':'PAIRED_EXACT_ALGEBRA_AUDIT_V1',
      'status':'PASS_EXACT_IDENTITIES_AND_REJECTION_CONTROLS',
      'identities':[name for name,_,_ in identities],
      'gaussian_coefficients':[str(v)for v in gaussian],
      'rejected_false_identities':rejected,
      'damping_countercheck':{'M':'5/2','N':47,'old43_constant_exceeds_allowed':True},
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'Exact polynomial equalities and rational constants only. Sign domains, integration, uniform remainders and native coverage are proved separately; no numerical family rerun.'}
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__': main()

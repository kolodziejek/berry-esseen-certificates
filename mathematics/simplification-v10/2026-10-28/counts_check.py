#!/usr/bin/env python3
"""Exact bounded checks for the shifted-count derivation; not a global cover."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions must remain enabled')

def need(value, name):
    if not value:
        raise AssertionError(name)

def pos(x): return max(F(0), x)
def choose(x, k): return F(comb(x, k)) if x >= k else F(0)
def triangular(x):
    return sum((pos(x-j) for j in range(1, max(1, int(x)+1))), F(0))
def floor(x): return x.numerator // x.denominator
def frac(x): return x-floor(x)
def convolution(a, b):
    out = {}
    for x, px in a.items():
        for y, py in b.items():
            out[x+y] = out.get(x+y, F(0)) + px*py
    return out
def power(a, n):
    out = {F(0): F(1)}
    for _ in range(n): out = convolution(out, a)
    return out
def prob(law, predicate): return sum((p for x,p in law.items() if predicate(x)), F(0))
def mean(law, k=1): return sum((p*x**k for x,p in law.items()), F(0))

A, d = F(3,5), F(9,125)
zeta, low, high = 1-d, F(-34,125), F(91,125)
need(high-low == 1 and -zeta < low < high < zeta, 'phase width/domain')
need(1-2*d-high == 1-A+low == F(16,125), 'individual mark distances')
need(1-3*d-high == 1-A-d+low == F(7,125), 'common mark distances')
need(F(5,2)*zeta-A-high == F(124,125), 'forward mark tail')
need(F(5,2)*zeta-A+low == F(181,125), 'backward mark tail')
need(A+d == F(84,125) < 1, 'harmonic span')
der = lambda j: 3*low*j*j+2*zeta*j-low
cubic = lambda j: (F(j)**3-j)/(6*(zeta*j+low)**3)
C3 = F(1953125,7739786)
need(der(2)>0 and der(3)<0 and cubic(3)>cubic(2), 'two cubic candidates')
need(cubic(3)==C3, 'exact third crossing constant')

negative_controls = []
need(1-A-F(1,2)<0, 'nearest anchor fails individual mark domain')
negative_controls.append('The old nearest phase interval has a negative first backward mark distance')
need(cubic(3)>cubic(2), 'single-j cubic coefficient must reject')
negative_controls.append('Keeping only j=2 underestimates the third-crossing coefficient')
need(triangular(F(7,2))>pos(F(7,2)-1), 'old chi<2 coefficient must reject')
negative_controls.append('Replacing T(chi) by (chi-1)+ fails as a coefficient when chi>2')

# Exact discrete-curvature checks, including illegal extensions and chi>=2.
curvature_cases = large_chi_cases = 0
for n in range(1,11):
    for p in map(F, ['1/5','2/5','1/2','3/5','4/5']):
        q = 1-p; v = p*q
        mass = [F(comb(n,j))*p**j*q**(n-j) for j in range(n+1)]
        fb = lambda k: sum(mass[:max(0,min(n+1,k+1))], F(0))
        maximum = max(mass)
        for k in range(n+1):
            chi = (n+1)*p-k
            for r in range(-n-2,n+3):
                lhs = fb(k+r)-fb(k)-r*mass[k]
                rhs = maximum/((n+1)*v)*(triangular(chi)*max(r,0)
                      +pos(chi)*choose(max(-r,0),2)+choose(max(-r,0),3))
                need(lhs<=rhs, 'discrete curvature')
                curvature_cases += 1
                large_chi_cases += chi>=2

# Test the analytic phase supremum against an exact rational grid. This is a
# regression/adversarial test, not a certificate of a continuous supremum.
def phase_value(u,b,z):
    return triangular(b+u)/(z-u)**2+pos(b+u)/(z+min(u,z/3))**2
def phase_sup(l,h,b,z):
    values = [phase_value(l,b,z),phase_value(h,b,z)]
    u = z-2*b
    if z>b and l<=u<=h and u<=z/3 and u<=1-b:
        values.append(1/(4*(z-b)))
    return max(values)
phase_cases = 0
for z in [F(2,5), F(2,3), zeta, F(1)]:
    for b in [F(j,7) for j in range(-14,36)]:
        for l,h in [(-z*F(9,10),z*F(9,10)),(-z/2,z*F(4,5)),(F(0),z*F(4,5))]:
            upper = phase_sup(l,h,b,z)
            for i in range(41):
                need(phase_value(l+(h-l)*i/40,b,z)<=upper,'three-candidate supremum')
                phase_cases += 1

# Actual discrete laws: rare outward atoms, tiny inward displacement, one
# deterministic conditional component, endpoint collisions, and p>1/2.
def binary_noise(a, direction):
    if direction == 0:
        return {-A:a/(A+a), a:A/(A+a)}
    return {-a:A/(A+a), A:a/(A+a)}
laws = [
    ({F(0):F(1)},{F(0):F(1)}),
    (binary_noise(F(1,40),0),binary_noise(F(1,40),1)),
    (binary_noise(F(1,1000000),0),{F(0):F(1)}),
    ({F(0):F(1)},binary_noise(F(1,1000000),1)),
]
actual_cases = path_cases = atom_collisions = 0
for n in [3,4]:
    for U0,U1 in laws:
        need(mean(U0)==mean(U1)==0, 'conditional centering')
        need(max(U0)-min(U1)<=d, 'inward support')
        s0,s1 = mean(U0,2),mean(U1,2)
        pair = [(x,y,px*py) for x,px in U0.items() for y,py in U1.items()]
        vartheta = sum((pp*pos(y-x) for x,y,pp in pair),F(0))
        for p in [F(2,5),F(1,2),F(53,100)]:
            q=1-p;v=p*q;s=q*s0+p*s1
            actual = {}
            for x,px in U0.items(): actual[x]=actual.get(x,F(0))+q*px
            for y,py in U1.items(): actual[1+y]=actual.get(1+y,F(0))+p*py
            sumlaw = power(actual,n)
            cubic_actual=sum((px*abs(y-p)**3 for y,px in actual.items()),F(0))
            need(cubic_actual>=v*(1-2*v)+(3*min(p,q)-d)*s,'all-p cubic')
            mass=[F(comb(n,j))*p**j*q**(n-j) for j in range(n+1)]
            fb=lambda k:sum(mass[:max(0,min(n+1,k+1))],F(0))
            for k in range(1,n):
                vk=convolution(power(U1,k),power(U0,n-k));t=mean(vk,2)
                A0=convolution(power(U1,k),power(U0,n-k-1))
                A1=convolution(power(U1,k-1),power(U0,n-k))
                for u in [low,F(-1,40),F(0),F(1,40),F(1,2),high]:
                    for eta in [F(1,5),F(1)]:
                        erf=er=erpos=er2=er3=F(0)
                        for pairs in product(pair,repeat=n):
                            weight=F(1)
                            zero=[];one=[]
                            for x,y,pp in pairs:
                                zero.append(x);one.append(y);weight*=pp
                            vals=[sum(one[:j],F(0))+sum(zero[j:],F(0)) for j in range(n+1)]
                            V=lambda j:vals[max(0,min(n,j))]
                            K=max(j for j in range(-n-5,2*n+6) if j+V(j)<=k+u)
                            R=K-k;W=V(k);z=u-W
                            forward=sum((pos(zero[k+i-1]-one[k+i-1]) for i in range(1,n-k+1) if W<=u-zeta*i),F(0))
                            backward=sum((pos(one[k-i]-zero[k-i]) for i in range(1,k+1) if W>u+eta+i),F(0))
                            need(R<=floor(z+eta)+(forward+backward)/eta,'pathwise mark')
                            erf+=weight*fb(K);er+=weight*R
                            erpos+=weight*max(R,0);er2+=weight*choose(max(-R,0),2);er3+=weight*choose(max(-R,0),3)
                            atom_collisions += W==u
                            path_cases+=1
                        direct=prob(sumlaw,lambda x:x<=k+u)
                        need(erf==direct,'actual iid/count coupling identity')
                        need(erpos<=t/(zeta-u)**2,'first crossing')
                        need(er2<=t/(zeta+min(u,zeta/3))**2,'second crossing')
                        need(er3**2<=C3**2*t*t*(A*A+3*t),'third crossing')
                        gain=sum((pr*frac(u+eta-x) for x,pr in vk.items()),F(0))
                        tails=sum((prob(A0,lambda x:x<=u+d-zeta*i)+prob(A1,lambda x:x>u+eta+i-A) for i in range(1,2*n+10)),F(0))
                        # The next thresholds are beyond the bounded deleted supports.
                        j=2*n+10
                        need(u+d-zeta*j<min(A0) and u+eta+j-A>max(A1),'tail completeness')
                        need(er<=u+eta-gain+vartheta*tails/eta,'deleted marked expectation')
                        actual_cases+=1
need(atom_collisions>0,'threshold atoms exercised')

# Explicit endpoint atom convention negative control.
need(prob({F(0):F(1)},lambda x:x<=0)!=prob({F(0):F(1)},lambda x:x<0),'closed/open control')
negative_controls.append('A closed count-plane atom cannot be replaced by an open event')

print(json.dumps({
    'status':'PASS_SHIFTED_COUNT_IDENTITIES_AND_BOUNDED_CONTROLS',
    'mathematical_scope':'Analytic derivations are in counts.tex; these finite tests are not a complete count-comparison cover',
    'execution_scope':'Exact rational algebra and actual finite-law regressions; no floating optimization',
    'phase':[str(low),str(high)],'third_crossing_coefficient':str(C3),
    'discrete_curvature_cases':curvature_cases,'cases_with_chi_at_least_two':large_chi_cases,
    'phase_grid_regression_points':phase_cases,'actual_law_cases':actual_cases,
    'pathwise_checks':path_cases,'observed_own_count_atom_collisions':atom_collisions,
    'negative_controls':negative_controls,'python':sys.version,
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
},indent=2))

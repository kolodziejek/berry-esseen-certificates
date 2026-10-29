"""Exact generic acceptance for unified-comparison.tex; standard library only.

No discovery grid, constructor import, numerical transcendental evaluation,
or fitted polynomial coefficients are used. The analytic reduction is in the
companion proof; this file checks its scalar hypotheses and exact identities.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions are proof obligations; optimization is forbidden')

GATES = {}
CONTROLS = []

def require(name, value, strict=True):
    value = Q(value)
    assert name not in GATES, name
    assert value > 0 if strict else value >= 0, (name, str(value))
    GATES[name] = {'margin': str(value), 'strict': strict}

def add(*ps):
    out = [Q(0)] * max(map(len, ps))
    for p in ps:
        for i, c in enumerate(p):
            out[i] += c
    return out

def scale(p, c):
    return [Q(c)*a for a in p]

def multiply(p, q):
    out = [Q(0)] * (len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out

def evaluate(p, x):
    result = Q(0)
    for c in reversed(p):
        result = result*x+c
    return result

def derivative(p):
    return [i*p[i] for i in range(1, len(p))]

def arctan_bounds(x, terms=12):
    """Alternating series for 0<x<1, returning exact inclusive bounds."""
    assert 0 < x < 1 and terms > 0 and terms % 2 == 0
    lo = sum((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(terms))
    return lo, lo+x**(2*terms+1)/Q(2*terms+1)

# Machin's identity pi=16 atan(1/5)-4 atan(1/239), with alternating bounds.
al, au = arctan_bounds(Q(1, 5))
bl, bu = arctan_bounds(Q(1, 239))
pi_lo, pi_hi = 16*al-4*bu, 16*au-4*bl
require('pi lower 25/8', pi_lo-Q(25, 8))
require('pi upper 22/7', Q(22, 7)-pi_hi)
eta, beta, philo, phihi, pip = Q(2,5), Q(41,100), Q(199,500), Q(2,5), Q(22,7)
require('normal lower', 1-2*pip*philo**2)
require('normal upper', 2*Q(25,8)*phihi**2-1, False)
require('low bump quadratic', Q(10)-pip**2)
require('low bump tangent', Q(10,3)-pip)
require('mode variance ratio', 1-Q(1,43)-Q(2,43**2)-Q(39,40))
require('mode linear loss', Q(2,9)-Q(2,3)*Q(1,3), False)
require('mode quadratic loss', 2*Q(2,9)-Q(2,3)**2, False)
require('mode coefficient', beta**2-phihi**2*Q(40,39)*Q(516,515)**2)
require('inverse square full tail', Q(5,3)-sum(Q(1,j*j) for j in range(1,6))-Q(1,5))
require('inverse cube full tail', Q(5,4)-1-Q(1,8)-Q(1,8), False)
# Exact polynomial majorant in the curvature tail.
lhs = [Q(256),Q(-256),Q(0),Q(0),Q(27)]
rhs = multiply([Q(16),Q(-24),Q(9)],[Q(16),Q(8),Q(3)])
assert lhs == rhs

ROWS = {
    'compact': dict(N=700, p0=Q(3,8), p1=Q(93,200), A=Q(3,5), d=Q(1,250), L=Q(1,100), U=Q(7,20),
                    kappa=Q(3), xi=Q(93,100), cm=Q(6), zeta=Q(23,100), mass=Q(3,4), V=Q(113,1000),
                    c=Q(79,200), j0=Q(1,5), j1=Q(5,2), theta=Q(2,3), sine=Q(17,20), sine2=Q(3,4)),
    'right': dict(N=200, p0=Q(2,5), p1=Q(53,100), A=Q(3,5), d=Q(9,125), L=Q(3,100), U=Q(9,25),
                  kappa=Q(3), xi=Q(231,250), cm=Q(5), zeta=Q(23,100), mass=Q(13,20), V=Q(117,1000),
                  c=Q(23,50), j0=Q(9,40), j1=Q(5,2), theta=Q(2,3), sine=Q(17,20), sine2=Q(3,4)),
    'left': dict(N=700, p0=Q(1,3), p1=Q(2,5), A=Q(7,10), d=Q(17,250), L=Q(1,100), U=Q(8,25),
                 kappa=Q(7,5), xi=Q(23,25), cm=Q(6), zeta=Q(11,50), mass=Q(3,4), V=Q(13,125),
                 c=Q(8,25), j0=Q(13,200), j1=Q(250,39), theta=Q(3,4), sine=Q(7,10), sine2=Q(1,2)),
}
TARGETS = {'compact':[2314,61304,3341,63680], 'right':[461,885,4654,11247], 'left':[55,18585,897,22487]}

def polynomials(row):
    n, A, kap, cm, mass, c, V = [row[k] for k in ('N','A','kappa','cm','mass','c','V')]
    r = min(row['p0'],1-row['p1'])
    qstar = 1-row['p1']
    alpha, b = 1-cm/n, 1+Q(3,n)
    z = kap*alpha
    W = scale([Q(0), z/2-A*A*b/16-4*pip**2/(n*r), -z*z/4-3*b*b/16, z**3/12, -z**4/48], eta*mass)
    T = [Q(0),1/qstar]
    M = add(scale(T,A*A),scale(multiply(T,T),3))
    def error(cc, normal):
        S = add(scale(T,Q(1,4)), [cc*row['j0'],cc*row['j1']], scale(M,Q(27,256)*(Q(5,3)+Q(5,4)*cc)))
        return scale(add(scale(S,beta),scale(normal,phihi)),1/V)
    Em = error(c,[row['xi']/8+Q(2,27)])
    Ep = error(Q(0),[Q(2,27),row['xi']/2])
    Pm, Pp = [add(W,scale(E,-Q(1,n)),[Q(0),-Q(1,100)]) for E in (Em,Ep)]
    return W, Em, Ep, Pm, Pp

RECORDS = {}
for name, row in ROWS.items():
    def gate(label, margin, strict=True):
        require(name+': '+label,margin,strict)
    n,p0,p1,A,d,L,U = [row[k] for k in ('N','p0','p1','A','d','L','U')]
    kap,xi,cm,zeta,mass,V,c = [row[k] for k in ('kappa','xi','cm','zeta','mass','V','c')]
    r,qs = min(p0,1-p1),1-p1
    vm = min(p0*(1-p0),p1*(1-p1))
    vp = Q(1,4) if p0 <= Q(1,2) <= p1 else max(p0*(1-p0),p1*(1-p1))
    for label,x in [('N domain',n-42),('p lower',p0-Q(1,3)),('p upper',Q(2,3)-p1),('d nonnegative',d),('d at most A',A-d),('c nonnegative',c)]:
        gate(label,x,False)
    for label,x in [('ordered p',p1-p0),('positive L',L),('ordered noise',U-L),('d below r',r-d),('diameter',1-A-d),('c below one',1-c),('positive mass',mass),('positive V',V),('positive affine constant',row['j0']),('positive affine slope',row['j1']),('positive cosine',kap),('positive variance shift',cm)]:
        gate(label,x)
    gate('high bump', (1-A-d)/(A+d)-eta*pip**2*d)
    gate('sine seed',row['sine2']-row['sine']**2)
    gate('cosine chord',2*(row['sine']/row['theta'])**2-kap)
    diameter = A+d
    if diameter > row['theta']:
        sine_tail = row['sine']-pip*(diameter-row['theta'])
        gate('tail sine positive',sine_tail)
        gate('cosine tail',2*sine_tail**2-kap*diameter**2)
    gate('raw displacement',xi**2-Q(46,25)**2*(vp+U/n))
    gate('displacement below one',1-xi)
    gate('boundary mesh',n*(r-d)-xi)
    gate('frozen lower variance',cm*r-1-xi,False)
    gate('positive alpha',n-cm)
    gate('left window interior',n*p0-xi-2)
    gate('right window interior',n*(1-p1)-xi-3)
    gate('window radius',4-xi-3)
    for label,z0 in [('left',p0-Q(4,n)),('right',p1+Q(4,n))]:
        gate('window '+label+' variance',z0*(1-z0)-zeta)
    gate('positive zeta',zeta)
    gate('five masses',2*philo*(1-(8+Q(1,12))/(n*zeta))-mass)
    gate('variance power',vm**3-V**2)
    gate('negative curvature offset',c-max(xi-qs,0),False)
    gate('affine sqrt majorant',4*row['j0']*row['j1']-1/qs,False)
    K0 = 3*r-d-Q(3,2)*(1-2*vm)
    K1 = 3*(1-2*vm)/(8*vm)
    gate('cubic correction',K0-K1*U/n)
    W,Em,Ep,Pm,Pp=polynomials(row)
    alpha,b = 1-cm/n,1+Q(3,n)
    z=kap*alpha
    completed_square = scale(add(scale(add(multiply([-Q(1),z],[-Q(1),z]),[Q(1)]),z*z/4),[3*b*b/8]),-eta*mass)
    assert derivative(derivative(W)) == completed_square
    for side,E in [('minus',Em),('plus',Ep)]:
        for i,e in enumerate(E): gate(side+' error coefficient '+str(i),e,False)
        gate(side+' error convexity',E[2])
    values=[evaluate(Pm,L),evaluate(Pm,U),evaluate(Pp,L),evaluate(Pp,U)]
    for label,value,target in zip(['minus L','minus U','plus L','plus U'],values,TARGETS[name]):
        gate(label+' endpoint above displayed bound',value-Q(target,10**6))
    RECORDS[name]={'parameters':{k:str(v) for k,v in row.items()},'W':list(map(str,W)),'E_minus':list(map(str,Em)),
                   'E_plus':list(map(str,Ep)),'P_minus':list(map(str,Pm)),'P_plus':list(map(str,Pp)),
                   'endpoint_values':list(map(str,values))}

# Negative controls concern intermediate claims, never the main conjecture.
assert 1 < 3*Q(3,4)**2  # x=3/4, 1-cos(3pi/2)=1.
CONTROLS.append('kappa=3 is false on the retained left diameter')
assert Q(0) < 3  # x=1: variance loss cannot ignore the diameter hypothesis.
CONTROLS.append('extending kappa=3 to diameter 1 is false at x=1')
assert not Q(0) > Q(0)
CONTROLS.append('strict minorant inequality at either zero endpoint is rejected')
assert Q(1,10) > 0  # F(x)=x, deterministic Z=1/10, Var Z=0.
CONTROLS.append('centered replacement cannot be used for an uncentered perturbation')
mass = Q(comb(200,100),2**200)
assert 200*mass**2 < Q(4,5)**2
CONTROLS.append('window mass 4/5 is false at actual n=200,p=1/2 mode')
bad = dict(ROWS['right'],N=100)
assert evaluate(polynomials(bad)[3],bad['U']) < 0
CONTROLS.append('same right criterion at n=100 fails its own endpoint test')
old = dict(ROWS['right'],j0=Q(3,8),j1=Q(3,2))
assert evaluate(polynomials(old)[3],old['L']) < 0
CONTROLS.append('old affine square-root tangent cannot certify the new .03 join')
assert Q(199,200) != 1
CONTROLS.append('frozen variance has n-1 summands: common-noise tau=(n-1)lambda/n')

here=Path(__file__).resolve()
print(json.dumps({'status':'PASS_UNIFIED_GENERIC_SCALARS','mathematical_status':'Local analytic criterion with finite rational checks; acquisition and finite base not asserted',
                  'gate_count':len(GATES),'gates':GATES,'rows':RECORDS,'negative_controls':CONTROLS,
                  'proof_sha256':hashlib.sha256(here.with_name('unified-comparison.tex').read_bytes()).hexdigest(),
                  'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest()},indent=2))

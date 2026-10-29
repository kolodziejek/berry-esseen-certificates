"""Exact scalar proof of the all-phase right extension; no certificate cells.

No constructor modules are imported. Retained proof bytes are pinned, and the
new quartics are reconstructed from the displayed formulas. Rational checks
are arithmetic evidence; the probability reductions are in counts-analytic.tex.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions must remain enabled')
BASE=Path(__file__).resolve().parents[3]
PINS={
 'mathematics/simplification-v15/2026-10-28/loss-direct.tex':'1bb19aee8183fbf70e81424dfb4503a54877a1938cd073bf58e751556e387ead',
 'mathematics/simplification-v15/2026-10-28/right-direct.tex':'5946340c178bc54c5094fcde567ec2c260a1abd0d39daf16306dadbb12971d67',
 'mathematics/simplification-v13/2026-10-28/crossing.tex':'0dda285adb9aaa24277fdc1d74843c20bc6100b2a64a0cd5ae34bb696a68a6ec',
 'mathematics/simplification-v14/2026-10-28/geometry-slack.tex':'8eb6fc89d82eb458fef45fb9a2f9783c1cae2705c908dcb8bebba725a4a36461',
 'mathematics/simplification-v11/2026-10-28/counts-v11.tex':'209f173c19a73c4fecf5aaf9aa2732c30b72266ff3f1673ddd52fa4a4e6c4641',
}
def verify_sources(blobs):
    if set(blobs)!=set(PINS):raise ValueError('Missing or additional source')
    for path,pin in PINS.items():
        if hashlib.sha256(blobs[path]).hexdigest()!=pin:raise ValueError('Changed source: '+path)
blobs={p:(BASE/p).read_bytes() for p in PINS};verify_sources(blobs)

def add(*ps):
    out=[F(0)]*max(map(len,ps))
    for p in ps:
        for i,x in enumerate(p):out[i]+=x
    return out

def scale(p,x):return [x*c for c in p]
def mul(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return out

def value(p,x):
    r=F(0)
    for c in reversed(p):r=r*x+c
    return r

def deriv(p):return [i*p[i] for i in range(1,len(p))]
gates={}
def positive(name,x):
    if name in gates:raise ValueError('Duplicate gate')
    gates[name]=F(x)
    if x<=0:raise AssertionError(name)

N=200;lo=F(3,100);hi=F(9,25);v=F(6,25);vl=F(117,1000)
a=F(231,250);c=F(23,50);alpha=F(39,40);b=F(203,200);z=3*alpha
for name,x in {
 'sqrt variance':F(251,500)**2-F(1,4)-hi/N,
 'raw displacement':a-F(46,25)*F(251,500),
 'bump theorem displacement':F(47,50)-a,
 'crossing lower':N*(F(2,5)-F(9,125))-a,
 'crossing upper':N*(F(47,100)-F(9,125))-a,
 'window displacement':4-a-3,
 'left five indices':N*F(2,5)-a-2,
 'right five indices':N*F(47,100)-a-3,
 'window variance lower':F(19,50)*F(31,50)-F(23,100),
 'window variance upper':F(11,20)*F(9,20)-F(23,100),
 'phi lower':1-F(199,500)**2*F(44,7),
 'mass13/20':F(199,250)*(1-(8+F(1,12))/(N*F(23,100)))-F(13,20),
 'variance power':v**3-vl**2,
 'sqrt T coefficient':F(9,4)-F(100,47),
 'curvature c':c-(a-F(47,100)),
 'mode linear loss':v-F(3,5)*F(1,5),
 'mode quadratic loss':2*v-F(3,5)**2,
 'mode variance ratio':1-F(1,43)-F(2,43**2)-F(39,40),
 'mode coefficient':F(41,100)**2-F(2,5)**2*F(40,39)*F(516,515)**2,
 'cubic sign':F(87,250)-F(13,16)*hi/N,
 'tangent license':4*F(5,2)*F(9,40)-F(100,47),
 'CE exceeds2/5':F(3)+F(79,25)-F(12,5)*F(251,100),
 'sqrt10 lower':10-F(79,25)**2,
 'sqrt2pi upper':F(251,100)**2-F(44,7),
}.items():positive(name,x)
# Segment endpoints are weak equalities at N=200; the actual count displacement
# is strict <4. Check exact closed segment inclusion, without a fictitious gap.
assert F(2,5)-F(4,N)==F(19,50)
assert F(53,100)+F(4,N)==F(11,20)
# Exact polynomial identities for the tangent: after x=sqrt(lambda),
# (5/3)x²-x+3/20 = (5/3)(x-3/10)².
assert [F(3,20),F(-1),F(5,3)]==scale(mul([F(-3,10),1],[F(-3,10),1]),F(5,3))
L=[F(0),F(1)];T=scale(L,F(100,47));M=add(scale(T,F(9,25)),scale(mul(T,T),3))
J=[F(9,40),F(5,2)]
W=scale([0,z/2-F(9,25)*b/16-F(10,N)*F(22,7)**2,
         -z*z/4-3*b*b/16,z**3/12,-z**4/48],F(13,50))
def error(c,positive_sign=False,j=J):
    S=add(scale(T,F(1,4)),scale(j,c),scale(M,F(27,256)*(F(5,3)+F(5,4)*c)))
    normal=scale([F(2,27),F(231,500)],F(2,5)) if positive_sign else [F(2,5)*(F(231,2000)+F(2,27))]
    return scale(add(scale(S,F(41,100)),normal),1/vl)
# Global concavity identity; no interpolation or sampling is used here.
expected=scale(add(scale(add(mul([-1,z],[-1,z]),[1]),z*z/4),[3*b*b/8]),-F(13,50))
assert deriv(deriv(W))==expected
records={}
for label,E,ceilings in [('negative',error(c),[461,885]),('positive',error(F(0),True),[4654,11247])]:
    assert all(x>0 for x in E)
    P=add(W,scale(E,-F(1,N)),[0,-F(1,100)])
    positive(label+' error curvature',2*E[2])
    # W'' is globally negative and subtracting a positive constant preserves it.
    assert deriv(deriv(P))==add(expected,[-2*E[2]/N])
    endpoints=[]
    for end,bound in zip([lo,hi],ceilings):
        q=value(P,end);positive(label+' endpoint '+str(end),q-F(bound,10**6));endpoints.append(str(q))
    records[label]={'W':list(map(str,W)),'E':list(map(str,E)),'P':list(map(str,P)),'endpoints':endpoints}
# Two exact boundary failures of prior or unjustified sufficient inequalities.
old=add(W,scale(error(c,j=[F(3,8),F(3,2)]),-F(1,N)),[0,-F(1,100)])
assert value(old,lo)<0
new=add(W,scale(error(c),-F(1,N)),[0,-F(1,100)])
assert value(new,F(0))<0
# A more aggressively lowered tangent does not cover the upper endpoint.
small=add(W,scale(error(c,j=[F(3,16),F(3)]),-F(1,N)),[0,-F(1,100)])
assert value(small,hi)<0
# Exact union logic, every boundary plus each open stratum.
axes=[F(0),lo,F(3,40),hi]
strata=axes+[(x+y)/2 for x,y in zip(axes,axes[1:])]
for x in strata:
    assert x==0 or 0<x<=lo or lo<=x<=hi
assert F(91,125)-F(-34,125)==1
# Source-mutation controls exercise the actual acceptance validator.
mutations=0
for path in PINS:
    bad=dict(blobs);bad[path]+=b'\n'
    try:verify_sources(bad)
    except ValueError:mutations+=1
    else:raise AssertionError('Changed source accepted')
bad=dict(blobs);bad.pop(next(iter(bad)))
try:verify_sources(bad)
except ValueError:mutations+=1
else:raise AssertionError('Missing source accepted')
print(json.dumps({'status':'PASS_RIGHT_ANALYTIC_003_TO_036','gate_count':len(gates),
 'gates':{k:str(v) for k,v in gates.items()},'polynomials':records,
 'negative_controls':{'old_tangent_lower_endpoint':str(value(old,lo)),
  'unsupported_zero_noise_endpoint':str(value(new,F(0))),
  'overaggressive_tangent_upper_endpoint':str(value(small,hi))},
 'source_mutation_rejections':mutations,'union_strata':list(map(str,strata)),
 'source_pins':PINS,'proof_sha256':hashlib.sha256(Path(__file__).with_name('counts-analytic.tex').read_bytes()).hexdigest(),
 'scope':'Full continuous scalar interval [.03,.36], all n>=200 via explicit estimates. No proof of acquisition or unrestricted cutoff; no claim to replace n42 theorem.',
 'python':sys.version},indent=2))

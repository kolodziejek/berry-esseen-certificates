from fractions import Fraction as F
from collections import defaultdict
from math import comb
from pathlib import Path
import hashlib,json,sys

def convolve(a,b):
    out=defaultdict(F)
    for x,p in a.items():
        for y,q in b.items(): out[x+y]+=p*q
    return dict(out)
def noise(law0,law1,n,j):
    out={F(0):F(1)}
    for i in range(n):out=convolve(out,law1 if i<j else law0)
    return out
def expect(law,fun):return sum((p*fun(x) for x,p in law.items()),F(0))
def pos(x):return max(F(0),x)
def cdf(law,t,closed=True):return expect(law,lambda x:x<=t if closed else x<t)

def crossing(law0,law1,n,p,t,strict_mutant=False):
    # Independent direct convolution and the paper's finite summation identity.
    q=1-p;k=t.numerator//t.denominator;u=t-k
    weights=[F(comb(n,j))*p**j*q**(n-j) for j in range(n+1)]
    laws=[{x+j:w for x,w in noise(law0,law1,n,j).items()} for j in range(n+1)]
    actual=sum((weights[j]*cdf(laws[j],t) for j in range(n+1)),F(0))
    L=[expect(law,lambda x:pos(t-x)) for law in laws]
    assert L[0]==t and L[-1]==0 and cdf(laws[0],t)==1
    B=[L[j]-pos(t-j) for j in range(n+1)]
    assert all(x>=0 for x in B)
    def chi(x):
        return expect(law0,lambda z:pos(x-z))-expect(law1,lambda z:pos(x-1-z))-expect(law1,lambda z:1+z<x if strict_mutant else 1+z<=x)
    chivals=[]
    for i in range(1,n+1):
        omitted=noise(law0,law1,n-1,i-1)
        chivals.append(expect(omitted,lambda z:chi(t-i+1-z)))
    FB=lambda j:sum(weights[:j+1],F(0))
    rhs=(1-u)*FB(k)+u*FB(k+1)+sum(((weights[j+1]-weights[j])*B[j] for j in range(1,n)),F(0))-sum((weights[i]*chivals[i-1] for i in range(1,n+1)),F(0))
    return actual-rhs

A=F(3,5);d=F(1,500)
left={-A:d/(A+d),d:A/(A+d)}
right={-d:A/(A+d),A:d/(A+d)}
zero={F(0):F(1)}
for law in (left,right,zero):assert expect(law,lambda z:z)==0
checks=0;rejects=0
for law0,law1 in [(left,right),(left,zero),(zero,right),(zero,zero)]:
    n=3;p=F(2,5)
    atoms={x+j for j in range(n+1) for x in noise(law0,law1,n,j)}
    thresholds={F(1),F(7,5),F(2)}|{x for x in atoms if n*d<x<n*(1-d)}
    for t in sorted(thresholds):
        assert crossing(law0,law1,n,p,t)==0
        checks+=1
        if crossing(law0,law1,n,p,t,strict_mutant=True)!=0:rejects+=1
assert rejects>0
orientation=1/(4*(A*A+3*F(101,10000)))-F(16,25)
assert orientation==F(52,97575)>0
assert 2*F(51,40)**2-3==F(201,800)>0
assert F(3,4)*(F(59,100)-F(51,50)*F(53,100))-F(2,700)==F(4787,140000)>F(1,100)
source=Path('/Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/manuscript_revision_20261029/manuscript/compact-v16/sections/08-direct-comparison.tex')
print(json.dumps({'status':'PASS_INDEPENDENT_COUNT_DIAGNOSTICS','python':sys.version,'crossing_exact_cases':checks,'strict_instead_of_closed_mutant_rejections':rejects,'orientation_margin':str(orientation),'sine_chord_quadratic_margin':str(F(201,800)),'manuscript_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Isolated exact finite-summation and atom diagnostics at n=3, plus scalar margins. These are not tests of the n>=700 theorem or a continuous-domain certificate.'},indent=2))

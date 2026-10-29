"""Bounded exact actual-law controls; these do not replace the analytic proof.

Conditional binomial convolution is evaluated by integer prefix probabilities
and first moments, separately from the generic scalar checker.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions required')

class BinomialNoise:
    def __init__(self, number, lo, hi):
        assert number >= 0 and lo < 0 < hi
        self.n,self.lo,self.hi = number,lo,hi
        self.step=hi-lo
        probability=-lo/self.step
        aa,dd=probability.numerator,probability.denominator
        bb=dd-aa
        self.den=dd**number
        self.prefix=[0];self.moment=[0]
        weight=bb**number
        for j in range(number+1):
            self.prefix.append(self.prefix[-1]+weight)
            self.moment.append(self.moment[-1]+j*weight)
            if j < number:
                numerator=weight*(number-j)*aa
                divisor=(j+1)*bb
                assert numerator % divisor == 0
                weight=numerator//divisor
        assert self.prefix[-1] == self.den
        assert self.step*Q(self.moment[-1],self.den)+number*lo == 0

    def cutoff(self,x):
        r=(x-self.n*self.lo)/self.step
        return min(self.n,max(-1,r.numerator//r.denominator))

    def cdf(self,x):
        return Q(self.prefix[self.cutoff(x)+1],self.den)

    def stoploss(self,x):
        j=self.cutoff(x)+1
        return (x-self.n*self.lo)*Q(self.prefix[j],self.den)-self.step*Q(self.moment[j],self.den)

def atomic_noise(lo,hi):
    p=-lo/(hi-lo)
    return [(lo,1-p),(hi,p)]

def floor(x):
    return x.numerator//x.denominator

RECORDS=[]
CASES=0
for row,n,p,A,d,lamlo,lamhi,kap,cm,r in [
    ('compact',700,Q(2,5),Q(3,5),Q(1,250),Q(1,100),Q(7,20),Q(3),Q(6),Q(3,8)),
    ('right',200,Q(2,5),Q(3,5),Q(9,125),Q(3,100),Q(9,25),Q(3),Q(5),Q(2,5)),
    ('left',700,Q(2,5),Q(7,10),Q(17,250),Q(1,100),Q(8,25),Q(7,5),Q(6),Q(1,3)),
]:
    for lam in (lamlo,lamhi):
        for group in (0,1):
            probability=p if group else 1-p
            inward=lam/(n*probability*A)
            assert 0 < inward <= d
            lo,hi=(-A,inward) if group == 0 else (-inward,A)
            atoms=atomic_noise(lo,hi)
            U0=atoms if group == 0 else [(Q(0),Q(1))]
            U1=atoms if group == 1 else [(Q(0),Q(1))]
            assert sum(x*w for x,w in atoms)==0
            assert n*probability*sum(x*x*w for x,w in atoms)==lam
            cache={}
            def law(count):
                if count not in cache:cache[count]=BinomialNoise(count,lo,hi)
                return cache[count]
            def conditional(j):
                return law(j if group else n-j)
            for w in (Q(-1,2),Q(0),Q(1,2)):
                t=n*p+w;k=floor(t)
                assert w*w<Q(46,25)**2*(p*(1-p)+lam/n)
                gs=[]
                for i in range(k-1,k+4):
                    frozen=law(i-1 if group else n-i)
                    x=t-i+1
                    gh=sum(pr*frozen.stoploss(x-u0) for u0,pr in U0)
                    gh-=sum(pr*(frozen.stoploss(x-1-u1)+frozen.cdf(x-1-u1)) for u1,pr in U1)
                    direct=conditional(i-1).stoploss(t-i+1)-conditional(i).stoploss(t-i)-conditional(i).cdf(t-i)
                    assert gh==direct and gh>=0
                    gs.append(gh)
                a=1-cm/n;b=1+Q(3,n);x=kap*a*lam
                reserve=Q(2,5)*((x-x*x/2+x**3/6-x**4/24)/2-(A*A*b*lam+3*b*b*lam*lam)/16-4*Q(22,7)**2*lam/(n*r))
                assert sum(gs)>reserve
                RECORDS.append({'row':row,'n':n,'lambda':str(lam),'variance_group':group,'raw_displacement':str(w),
                                'sum_five_losses':str(sum(gs)),'analytic_reserve':str(reserve)})
                CASES+=1

# Full identity for an actual common-noise marginal. The conditional sum
# has atoms at t=2-e and t=2+e; the frozen four-fold noise has an atom at
# zero. Thus t=2 itself tests a frozen-noise collision, not a sum atom.
n=5;p=Q(2,5);e=Q(1,100)
noise=BinomialNoise(n,-e,e)
frozen=BinomialNoise(n-1,-e,e)
atoms=atomic_noise(-e,e)
pi=[Q(comb(n,j))*p**j*(1-p)**(n-j) for j in range(n+1)]
def FB(j):return sum(pi[:j+1])
full_controls=0
for t in [Q(2)-e,Q(2),Q(2)+e,Q(5,2)]:
    k=floor(t);u=t-k
    gj=[]
    for i in range(1,n+1):
        x=t-i+1
        g=sum(pr*frozen.stoploss(x-y) for y,pr in atoms)
        g-=sum(pr*(frozen.stoploss(x-1-y)+frozen.cdf(x-1-y)) for y,pr in atoms)
        direct=noise.stoploss(t-i+1)-noise.stoploss(t-i)-noise.cdf(t-i)
        assert g==direct and g>=0
        gj.append(g)
    curvature=sum((pi[j+1]-pi[j])*(noise.stoploss(t-j)-max(t-j,0)) for j in range(1,n))
    actual=sum(pi[j]*noise.cdf(t-j) for j in range(n+1))
    reconstructed=(1-u)*FB(k)+u*FB(k+1)+curvature-sum(pi[i]*gj[i-1] for i in range(1,n+1))
    assert actual==reconstructed
    full_controls+=1
assert frozen.cdf(Q(0))-frozen.cdf(-e)>0
# For the common-noise case the frozen variance is exactly (n-1)*s,
# disproving replacement by n*s even though every summand is centered.
assert (n-1)*e*e != n*e*e

here=Path(__file__).resolve()
print(json.dumps({'status':'PASS_UNIFIED_ACTUAL_LAWS','local_row_cases':CASES,'checked_five_count_identities':5*CASES,
                  'full_weighted_identities_at_atoms_and_neighbors':full_controls,
                  'scope':'Exact finite-law adversarial controls, not domain coverage or a proof of the normal comparison',
                  'records':RECORDS,'proof_sha256':hashlib.sha256(here.with_name('unified-comparison.tex').read_bytes()).hexdigest(),
                  'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest()},indent=2))

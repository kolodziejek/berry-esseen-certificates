"""Exact atom arithmetic; rational verification of selected small-noise events.

The near-resonance table is floating-point score discovery, explicitly separate
from exact arithmetic and from the uniform analytic proof.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd, isqrt, sqrt, erf, pi
from pathlib import Path
import json
import sys

if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions must remain enabled')

def lcm(a,b): return a//gcd(a,b)*b
def distribution(atoms,n):
    scale=den=1
    for x,p in atoms:
        scale=lcm(scale,x.denominator);den=lcm(den,p.denominator)
    vals=[int(x*scale) for x,p in atoms];weights=[int(p*den) for x,p in atoms]
    assert sum(weights)==den and min(weights)>0
    powers=[[w**j for j in range(n+1)] for w in weights]
    result={}
    def recur(i,left,loc,mass):
        if i==len(atoms)-1:
            key=loc+left*vals[i];value=mass*powers[i][left]
            result[key]=result.get(key,0)+value
        else:
            for j in range(left+1):
                recur(i+1,left-j,loc+j*vals[i],mass*comb(left,j)*powers[i][j])
    recur(0,n,0,1)
    assert sum(result.values())==den**n
    return [(F(x,scale),mass) for x,mass in sorted(result.items())],den**n

def law(p,noise0,noise1):
    assert sum(w for u,w in noise0)==sum(w for u,w in noise1)==1
    assert sum(u*w for u,w in noise0)==sum(u*w for u,w in noise1)==0
    return [(u,(1-p)*w) for u,w in noise0]+[(1+u,p*w) for u,w in noise1]

def rare(d,e): return [(-d,e),(e*d/(1-e),1-e)]
def discovery(atoms,n,p):
    mean=sum(x*w for x,w in atoms);var=sum((x-mean)**2*w for x,w in atoms)
    third=sum(abs(x-mean)**3*w for x,w in atoms)
    assert mean==p and var>0
    dist,den=distribution(atoms,n)
    cdf=0;best=(-1,None,None,None)
    for x,mass in dist:
        cdf+=mass
        z=float(x-n*p)/sqrt(n*float(var))
        delta=float(F(cdf,den))-(1+erf(z/sqrt(2)))/2
        score=sqrt(n)*float(var)**1.5/float(third)*delta
        if score>best[0]:best=(score,x,F(cdf,den),F(mass,den))
    score,x,cdf,jump=best
    k=(x+F(34,125)).numerator//(x+F(34,125)).denominator
    v=p*(1-p);lam=n*(var-v)
    FB=sum(F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(k+1))
    CB=sqrt(n)*sqrt(float(v))/float(1-2*v)*(float(FB)-(1+erf(float(k-n*p)/sqrt(2*n*float(v))))/2)
    return {'score':score,'threshold':x,'cdf':cdf,'jump':jump,'k':k,'phase':x-k,
            'CB':CB,'lambda':lam,'variance':var,'third_raw':third,
            'H':float(x-n*p)/sqrt(float(var)),'atom_count':len(dist)}

# Interval operations used only in acceptance below, not to discover a maximum.
def I(x): return (F(x),F(x))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    x=[a[i]*b[j] for i in (0,1) for j in (0,1)]
    return min(x),max(x)
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def root(x):
    assert x>=0
    s=10**45;k=isqrt(x.numerator*s*s//x.denominator)
    out=F(k,s),F(k+1,s)
    assert out[0]**2<=x<=out[1]**2
    return out
def atan_interval(x,n):
    a=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    b=a+(-1)**n*x**(2*n+1)/F(2*n+1)
    return min(a,b),max(a,b)
PI=sub(mul(I(16),atan_interval(F(1,5),34)),mul(I(4),atan_interval(F(1,239),10)))
PHI0=div(I(1),(root(2*PI[0])[0],root(2*PI[1])[1]))
CE=mul(div(add(I(3),root(F(10))),I(6)),PHI0)
def Phi_rational(x):
    if x<0:return sub(I(1),Phi_rational(-x))
    assert x<=2
    def integ(n):return sum(((-1)**j*x**(2*j+1)/F(2**j*factorial(j)*(2*j+1)) for j in range(n+1)),F(0))
    return add(I(F(1,2)),mul(PHI0,(integ(51),integ(50))))
def Phi_interval(x):return Phi_rational(x[0])[0],Phi_rational(x[1])[1]
def exact_event(atoms,n,p,z):
    x=z['threshold'];v=p*(1-p);var=z['variance'];r=z['third_raw'];k=z['k']
    norm=Phi_interval(div(I(x-n*p),root(n*var)))
    normB=Phi_interval(div(I(k-n*p),root(n*v)))
    FB=sum(F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(k+1))
    rho=div(I(r),mul(I(var),root(var)))
    rhoB=div(I(1-2*v),root(v))
    error=add(mul(root(F(n)),sub(sub(I(z['cdf']),norm),sub(I(FB),normB))),mul(CE,sub(rhoB,rho)))
    assert error[1]<-z['lambda']/100
    # Preserve the threshold atom rather than treating a close sum as equal.
    assert z['cdf']-(z['cdf']-z['jump'])==z['jump']>0
    return {'error_interval':[str(x) for x in error],
            'strict_margin_lower':str(-z['lambda']/100-error[1])}

def main():
    accepted=[]
    for n,p,side,e in [(42,F(2,5),0,F(1,5000)),(42,F(53,100),1,F(1,5000)),
                      (100,F(21,50),0,F(1,20000)),(43,F(1,2),1,F(1,1000000))]:
        noises=[[(F(0),F(1))],[(F(0),F(1))]]
        noises[side]=rare(F(3,5),e) if side==0 else [(-u,w) for u,w in rare(F(3,5),e)]
        atoms=law(p,*noises);z=discovery(atoms,n,p)
        assert 0<z['lambda']<=F(1,500) and abs(z['H'])<1.84
        result=exact_event(atoms,n,p,z)
        accepted.append({'n':n,'p':str(p),'side':side,'rare_mass':str(e),
                         'lambda':str(z['lambda']),'threshold':str(z['threshold']),
                         'phase':str(z['phase']),'atom_count':z['atom_count'],**result})
    # Four-point nearby law and exact collisions.
    noises=[[(F(-1,1000),F(1,2)),(F(1,1000),F(1,2))]]*2
    atoms=law(F(1,2),*noises);z=discovery(atoms,42,F(1,2));result=exact_event(atoms,42,F(1,2),z)
    accepted.append({'n':42,'p':'1/2','kind':'four-point symmetric conditional noise',
                     'lambda':str(z['lambda']),'threshold':str(z['threshold']),
                     'atom_count':z['atom_count'],**result})
    # Repeat the supplied near-resonance design with exact atom keys and masses.
    # The irrational proposed p* is replaced by an explicitly named rational.
    diagnostic=[];p=F(41886117,100000000)
    for n in (42,100):
        for d in (F(1,2),F(4,5),F(9,10),F(19,20)):
            for e in (F(1,200),F(1,50)):
                atoms=law(p,rare(d,e),[(F(0),F(1))]);z=discovery(atoms,n,p)
                diagnostic.append({'n':n,'jump':str(d),'rare_mass':str(e),
                    'lambda':float(z['lambda']),'score_diagnostic':z['score'],
                    'own_Bernoulli_score_diagnostic':z['CB'],
                    'phase_exact':str(z['phase']),'outside_small_noise_theorem':True})
    assert len(accepted)==5 and len(diagnostic)==16
    print(json.dumps({'status':'PASS_EXACT_SELECTED_SMALL_NOISE_EVENTS',
          'scope':'Five exact iid event comparisons with rational normal enclosures. Floating maximizer discovery is not certified; the universal conclusion relies on the analytic proof.',
          'accepted':accepted,'near_resonance_diagnostic':diagnostic,
          'diagnostic_scope':'Exact finite distribution arithmetic; scores use ordinary erf, not acceptance. None of these16laws satisfies the small-noise theorem premises.',
          'diagnostic_probability':str(p),'supplied_code_imported_or_executed':False,
          'python':sys.version},indent=2))

if __name__=='__main__':main()

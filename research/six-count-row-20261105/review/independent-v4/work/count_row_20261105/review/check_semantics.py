"""Independent exact actual-law tests of the six-count analytic reduction.

No constructor imports. This does not accept a certificate or acquire a row.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb
from pathlib import Path
import hashlib, json, sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('unoptimized Python is required')

N=5; A0=F(82453,125000); A1=F(703209,1000000)
PL=F(19,50); PH=F(39,100); CAP=F(7687,25000)
BL=F(-15293,500000); BH=F(307221,1000000); INWARD=F(471533,500000)
def need(x,message):
    if not x: raise ValueError(message)
def mean(d,r): return sum(w*x**r for x,w in d.items())
def law(a,b):
    if a==0 or b==0:return {F(0):F(1)}
    return {-a:b/(a+b),b:a/(a+b)}
def convolve(a,b):
    out={}
    for x,p in a.items():
      for y,q in b.items():out[x+y]=out.get(x+y,F(0))+p*q
    return out
def power(a,n):
    out={F(0):F(1)}
    for _ in range(n):out=convolve(out,a)
    return out
def poly(c,z):return sum(a*z**i for i,a in enumerate(c))
def moment_expression(p,x,y,g0,g1,k,u,coeffs):
    q=1-p;total=F(0)
    for j,c in enumerate(coeffs):
        t=(N-j)*x/q+j*y/p
        ms=[F(1),F(0),t,(N-j)*g0*x/q+j*g1*y/p,
            (N-j)*g0*g0*x/q+j*g1*g1*y/p+F(12,5)*t*t]
        a=j-k-u
        e=sum(c[r]*comb(r,i)*a**(r-i)*ms[i] for r in range(5) for i in range(r+1))
        total+=F(comb(N,j))*p**j*q**(N-j)*e
    return total
def vertices_at(p):
    v=p*(1-p)
    planes=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),CAP/N),
      (-(1+BH),1-BH,v*(BH-1+2*p)),(1+BL,-(1-BL),v*(1-BL-2*p))]
    found=set()
    for (a,b,c),(d,e,f) in combinations(planes,2):
        det=a*e-b*d
        if det:
            x=(c*e-b*f)/det;y=(a*f-c*d)/det
            if all(A*x+B*y<=C for A,B,C in planes):found.add((x,y))
    need(len(found)>=3,'test polygon is two dimensional')
    return sorted(found)

def main(out):
    count=dict(actual_pairs=0,admitted_beta_noise_pairs=0,conditional_convolutions=0,
      direct_mixture_equalities=0,atom_collisions=0,zero_components=0,tiny_variance_components=0,
      moment_bound_tests=0,vertex_bound_tests=0,beta_identities=0,rho_numerator_identities=0,
      gaussian_sign_checks=0,negative_controls=0)
    coeffs=[[F(2+j,3),F(j-3,7),F(j-2,10),F((-1)**j,9),F(j+1,50)] for j in range(6)]
    corner=tuple(product((-A0,F(0),PH),(A1,F(0),-(1-PL))))
    for p in (PL,F(77,200),PH):
      q=1-p;v=p*q;vs=vertices_at(p)
      configs=[(F(0),F(0)),(F(1,10),F(1,10)),(A0,F(1,10**12)),
        (F(1,1000000),p),(F(1,4),p),(A0,F(1,100)),(F(3,5),F(1,20)),(A0,p)]
      configs1=[(F(0),F(0)),(F(1,10),F(1,10)),(F(1,10**12),A1),
        (q,F(1,1000000)),(q,F(1,3)),(F(1,100),A1),(F(1,20),F(3,5)),(q,A1)]
      for (out0,inn0),(inn1,out1) in product(configs,configs1):
        if inn0+inn1>INWARD:continue
        d0=law(out0,inn0);d1=law(inn1,out1)
        s0=mean(d0,2);s1=mean(d1,2);m30=mean(d0,3);m31=mean(d1,3)
        x=q*s0;y=p*s1;w=v+x+y;lam=N*(x+y)
        count['actual_pairs']+=1
        count['zero_components']+=int(s0==0)+int(s1==0)
        count['tiny_variance_components']+=int(0<s0<F(1,10**8))+int(0<s1<F(1,10**8))
        mixed={}
        for z,r in d0.items():mixed[z]=mixed.get(z,F(0))+q*r
        for z,r in d1.items():mixed[1+z]=mixed.get(1+z,F(0))+p*r
        need(mean(mixed,1)==p,'common mean')
        rawbeta=sum(r*(z-p)*abs(z-p) for z,r in mixed.items())/w
        need(rawbeta==(v*(1-2*p)-x+y)/w,'exact signed second identity')
        count['beta_identities']+=1
        R=sum(r*abs(z-p)**3 for z,r in mixed.items())
        need(R==v*(1-2*v)+3*(p*x+q*y)-q*m30+p*m31,'exact absolute third identity')
        count['rho_numerator_identities']+=1
        need(mean(d0,4)<=(inn0-out0)*m30+out0*inn0*s0,'class zero support polynomial')
        need(mean(d1,4)<=(out1-inn1)*m31+out1*inn1*s1,'class one support polynomial')
        admitted=lam<=CAP and BL<=rawbeta<=BH
        count['admitted_beta_noise_pairs']+=int(admitted)
        cond=[];mixture={}
        for j in range(6):
            c=convolve(power(d0,N-j),power(d1,j));cond.append(c)
            count['conditional_convolutions']+=1
            t=(N-j)*s0+j*s1
            need(mean(c,1)==0 and mean(c,2)==t,'conditional first two moments')
            need(mean(c,3)==(N-j)*m30+j*m31,'conditional third moment')
            exact4=(N-j)*mean(d0,4)+j*mean(d1,4)+3*t*t-3*((N-j)*s0*s0+j*s1*s1)
            need(mean(c,4)==exact4,'exact conditional fourth moment')
            need(exact4<=(N-j)*mean(d0,4)+j*mean(d1,4)+F(12,5)*t*t,'finite Cauchy upper bound')
            mass=F(comb(N,j))*p**j*q**(N-j)
            for z,r in c.items():mixture[j+z]=mixture.get(j+z,F(0))+mass*r
        direct=power(mixed,N)
        need(direct==mixture,'same-marginal full convolution equals complete count mixture')
        count['direct_mixture_equalities']+=1
        # Actual event-plane atoms, zero phase and signed phases are all tested.
        cases=[(k,u) for k in (1,2,3) for u in (F(-1,2),F(0),F(1,2))]
        atoms=sorted(direct)
        for z in atoms[::max(1,len(atoms)//3)]:
            k=int(z+F(1,2));cases.append((k,z-k));count['atom_collisions']+=1
        for k,u in cases:
            direct_cdf=sum(r for z,r in direct.items() if z<=k+u)
            count_cdf=sum(F(comb(N,j))*p**j*q**(N-j)*sum(r for z,r in c.items() if z<=k+u-j) for j,c in enumerate(cond))
            need(direct_cdf==count_cdf,'closed collision convention')
        # Several signed translated quartic mixtures; no global majorant claim here.
        for k,u in ((1,F(-1,2)),(2,F(0)),(3,F(1,2))):
            actual=sum(F(comb(N,j))*p**j*q**(N-j)*sum(r*poly(coeffs[j],z+j-k-u) for z,r in c.items()) for j,c in enumerate(cond))
            bound=max(moment_expression(p,x,y,g0,g1,k,u,coeffs) for g0,g1 in corner)
            need(actual<=bound,'nine common moment corners bound actual mixture')
            count['moment_bound_tests']+=1
            if admitted:
                vertex=max(moment_expression(p,X,Y,g0,g1,k,u,coeffs) for X,Y in vs for g0,g1 in corner)
                need(actual<=vertex,'polygon vertex bound for admitted pair')
                count['vertex_bound_tests']+=1
    # Rational order of a/sqrt(D), compared by signed squares; no floating normal.
    def le_ratio(a,d,b,e):
        if a<=0<=b:return True
        if b<0<a:return False
        return a*a*e<=b*b*d if a>=0 else a*a*e>=b*b*d
    for k,ul,uh in ((1,F(-1,2),F(1,2)),(2,F(-1,2),F(1,2)),(3,F(-1,2),F(1,2))):
        amin=k+ul-N*PH
        den=N*PL*(1-PL) if amin<0 else N*PH*(1-PH)+CAP
        for p,u,l in product((PL,F(77,200),PH),(ul,(ul+uh)/2,uh),(F(0),CAP/2,CAP)):
            need(le_ratio(amin,den,k+u-N*p,N*p*(1-p)+l),'signed cell normal lower argument')
            count['gaussian_sign_checks']+=1
    # Four exact counterexamples to tempting but invalid replacements.
    neg=6*F(1,2)**2+12*F(1,2)*1+2*1
    need(neg>max(F(6),F(8)),'negative variance correction destroys convexity');count['negative_controls']+=1
    sym=law(F(1,10),F(1,10));need(mean(sym,4)>0 and mean(sym,3)==0,'false pointwise fourth/gamma bound');count['negative_controls']+=1
    need(not le_ratio(-F(1),F(2),-F(1),F(1)),'upper noise cannot lower a negative normal argument');count['negative_controls']+=1
    atom={F(0):F(1)};need(sum(r for z,r in atom.items() if z<=0)>sum(r for z,r in atom.items() if z<0),'closed event cannot be replaced by open');count['negative_controls']+=1
    # Curvature sign can be checked exactly after removing its positive factor.
    for a,D in product((F(-1,2),F(-1,10),F(0)),(F(1,2),F(1),F(2))):
        need(a*(3*D-a*a)<=0,'guarded negative-phase Gaussian concavity')
    need(F(1,10)*(3-F(1,100))>0,'positive phase is not covered by that concavity guard')
    count['negative_controls']+=1
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    result=dict(status='PASS',mathematical_scope='Independent exact finite-law controls of conditional reduction; no full-row certificate or acquisition claim.',counts=count,
      source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main(sys.argv[1])

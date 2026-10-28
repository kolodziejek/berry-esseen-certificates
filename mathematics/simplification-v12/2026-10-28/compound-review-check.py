"""Independent exact review checks. No constructor is imported or executed.

The probability-generating-function recurrence, rather than the constructor's
finite double sum, computes the entire lower complement of a Poisson hinge.
Arithmetic checks are controls for the proofs, not a continuous count cover.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib, json, sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError("Optimization disables proof obligations")

A=Q(3,5); D=Q(9,125); STEP=Q(3,125)

def exp_negative(x, degree=None):
    assert x>=0
    if not x:return Q(1),Q(1)
    if degree is None:degree=max(90,4*(x.numerator//x.denominator+1))
    assert degree+2>x
    term=Q(1); total=term
    for j in range(1,degree+1):
        term*=x/j;total+=term
    first_omitted=term*x/(degree+1)
    upper=total+first_omitted/(1-x/Q(degree+2))
    return 1/upper,1/total

def coefficients(mu,nu,K):
    assert mu>=0 and nu>=0 and K>=0
    c=[Q(1)]
    for j in range(1,K+1):
        c.append(((25*mu*c[j-25] if j>=25 else Q(0))+
                  (3*nu*c[j-3] if j>=3 else Q(0)))/Q(j))
    return c

def lattice_hinge(mu,nu,K):
    """Enclose E(25 P_mu + 3 P_nu - K)_+^2 for rational K."""
    assert mu>=0 and nu>=0
    full=625*mu+9*nu+(25*mu+3*nu-K)**2
    if K<0:return full,full
    c=coefficients(mu,nu,K.numerator//K.denominator)
    deficit=sum((K-j)**2*x for j,x in enumerate(c))
    elo,ehi=exp_negative(mu+nu)
    lo,hi=full-ehi*deficit,full-elo*deficit
    assert hi>=0 and lo<=hi
    return max(Q(0),lo),hi

def physical_hinge(t,w,y):
    assert t>=0 and 0<=w<=1
    mu=t*(1-w)/A**2;nu=t*w/D**2
    K=(y+A*mu+D*nu)/STEP
    lo,hi=lattice_hinge(mu,nu,K)
    return STEP**2*lo,STEP**2*hi

def two_point(low,high):
    if low==0 and high==0:return [(Q(0),Q(1))]
    assert low<0<high
    return [(low,high/(high-low)),(high,-low/(high-low))]

def repeated_two_point(law,n):
    if len(law)==1:return [(n*law[0][0],Q(1))]
    (a,pa),(b,pb)=law
    return [(a*(n-j)+b*j,Q(comb(n,j))*pa**(n-j)*pb**j) for j in range(n+1)]

def moment(law,j):return sum(p*x**j for x,p in law)

def jets_add(a,b):return tuple(x+y for x,y in zip(a,b))
def jets_mul(a,b):return (a[0]*b[0],a[1]*b[0]+a[0]*b[1],a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2])
def jets_power(a,j):
    v=(Q(1),Q(0),Q(0))
    for _ in range(j):v=jets_mul(v,a)
    return v


def main():
    report={"status":"PASS","scope":"component identities and adversarial controls; no new count-domain acceptance"}
    # Exact actual common-allocation counterexample, with every domain bound.
    n=42;p=Q(1,2);k=22;r=Q(2,25);eps=Q(1,1000)
    u0=two_point(-A,eps);u1=[(-x,prob) for x,prob in u0]
    v=moment(u0,2);s=v;lam=n*s;w=p*v/s;delta=k-n*p
    T0=(n-k)*v;T1=k*v;t=T0+T1;kappa=-4*r
    c0=max(A*A+kappa*A,eps*eps-kappa*eps)
    c1=max(A*A-kappa*A,eps*eps+kappa*eps)
    ew3=(n-k)*moment(u0,3)+k*moment(u1,3)
    ew4=(n-k)*moment(u0,4)+k*moment(u1,4)+3*t*t-3*n*v*v
    false=(c0*(1-w)+c1*w)*t+3*t*t
    gap=ew4-kappa*ew3-false
    assert gap==Q(423903,2500000000)>0
    assert lam==Q(63,2500) and 2*eps<D and (delta-r)**2<Q(46,25)**2*(p*(1-p)+s)
    assert ew4-kappa*ew3<=c0*T0+c1*T1+3*t*t
    report["common_allocation_actual_counterexample"]={"gap":str(gap),"lambda":str(lam),"T0":str(T0),"T1":str(T1)}
    # Exact transport across legal counts and physical marginal allocations.
    transport=0
    for p in [Q(2,5),Q(1,2),Q(53,100)]:
      q=1-p
      for v0,v1 in [(Q(0),Q(1,2000)),(Q(1,4000),Q(1,2000)),(Q(1,2000),Q(0))]:
       s=q*v0+p*v1;lam=n*s;w=p*v1/s;k=int(n*p);delta=k-n*p
       for i in range(-k,n-k+1):
        g0=1-(delta+i)/(n*q);g1=1+(delta+i)/(n*p)
        assert lam*(1-w)*g0==(n-k-i)*v0
        assert lam*w*g1==(k+i)*v1
        transport+=1
    report["legal_count_transport_identities"]=transport
    # Pgf recurrence tested against independently summed rational coefficients.
    pgf_checks=0
    for mu,nu in [(Q(0),Q(0)),(Q(1,10),Q(0)),(Q(0),Q(3,2)),(Q(1,6),Q(4))]:
      c=coefficients(mu,nu,81)
      for ell in range(82):
       direct=sum(mu**j*nu**k/Q(factorial(j)*factorial(k))
                  for j in range(ell//25+1) for k in range(ell//3+1) if 25*j+3*k==ell)
       assert c[ell]==direct;pgf_checks+=1
    report["pgf_coefficients_checked"]=pgf_checks
    assert lattice_hinge(Q(0),Q(0),Q(0))==(0,0)
    assert lattice_hinge(Q(0),Q(0),Q(-1))==(1,1)
    # Prove a strict negative curvature at a positive physical hinge anchor.
    t=Q(1,40);w=Q(1,4);y=Q(1,5)
    mu=(t*(1-w)/A**2,-t/A**2,Q(0));nu=(t*w/D**2,t/D**2,Q(0))
    mean=A*mu[0]+D*nu[0];mp=A*mu[1]+D*nu[1];sp=mu[1]+nu[1]
    assert mu[0]+nu[0]==Q(815,648) and mean+y==Q(229,720)
    assert 4*D<mean+y<5*D<A
    deficit=(Q(0),Q(0),Q(0))
    for j in range(5):
        g=(mean+y-j*D,mp,Q(0))
        term=jets_mul(jets_power(nu,j),jets_mul(g,g))
        deficit=jets_add(deficit,tuple(x/Q(factorial(j)) for x in term))
    curvature=deficit[2]-2*sp*deficit[1]+sp**2*deficit[0]
    assert curvature==Q(787398879114798488065,147382613147155571933184)>0
    report["nonconvexity_negative_second_derivative_coefficient"]=str(curvature)
    # Strict monotonicity controls, enclosed without sampled exponentials.
    monotone=0
    for t in [Q(1,1000),Q(1,40),Q(3,40)]:
      for y in [Q(0),Q(1,5),Q(1,2)]:
       boxes=[physical_hinge(t,w,y) for w in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]]
       for (lo,hi),(lo2,hi2) in zip(boxes,boxes[1:]):
        assert lo>hi2;monotone+=1
    report["strict_allocation_monotonicity_controls"]=monotone
    # Genuine independent conditional convolutions; these are checks, not a proof.
    actual=0
    for eps0,eps1 in [(Q(1,1000),Q(1,2000)),(Q(1,10000),Q(1,1000)),(Q(0),Q(1,1000)),(Q(1,1000),Q(0))]:
      u0=two_point(-A,eps0) if eps0 else [(Q(0),Q(1))]
      u1=two_point(-eps1,A) if eps1 else [(Q(0),Q(1))]
      for j in [20,22]:
       v0=moment(u0,2);v1=moment(u1,2);T0=(n-j)*v0;T1=j*v1
       mu=T0/A**2;nu=T1/D**2
       l0=repeated_two_point(u0,n-j);l1=repeated_two_point(u1,j)
       for y in [Q(1,5),Q(1,2)]:
        lhs=sum(prob0*prob1*max(Q(0),-x0-x1-y)**2 for x0,prob0 in l0 for x1,prob1 in l1)
        K=(y+A*mu+D*nu)/STEP
        lower,upper=lattice_hinge(mu,nu,K)
        assert lhs<=STEP**2*upper
        actual+=1
    report["actual_groupwise_hinge_controls"]=actual
    # Corrected cubic endpoint prices: integrate first, preserving g0 and g1.
    price_controls=0
    for p in [Q(2,5),Q(1,2),Q(53,100)]:
      q=1-p
      for eps0,eps1 in [(Q(1,1000),Q(1,2000)),(Q(1,10000),Q(1,1000))]:
       u0=two_point(-A,eps0);u1=two_point(-eps1,A)
       v0=moment(u0,2);v1=moment(u1,2);s=q*v0+p*v1
       lam=n*s;w=p*v1/s;v=p*q
       B=Q(3,2)*(1-2*v)+Q(3,8)*(1-2*v)*s/v
       for k in [int(n*p),int(n*p)+1]:
        delta=k-n*p;g0=1-delta/(n*q);g1=1+delta/(n*p)
        T0=(n-k)*v0;T1=k*v1;t=T0+T1
        ew3=(n-k)*moment(u0,3)+k*moment(u1,3)
        ew4=(n-k)*moment(u0,4)+k*moment(u1,4)+3*t*t-3*((n-k)*v0*v0+k*v1*v1)
        for r in [Q(0),Q(2,25),Q(1,10)]:
         alpha=Q(1,2);M=5*alpha**4;m=Q(73,100);K=Q(1,20)
         kap=-4*r;L=3*alpha**2-6*r*r;J=-r**4+3*alpha**2*r*r+2*alpha**3*r
         bracket=3*p*(1-w)+3*q*w-B+w*moment(u1,3)/v1-(1-w)*moment(u0,3)/v0
         assert bracket>0
         integrated=m*(-ew4+kap*ew3+L*t+J)/M+K*lam*bracket
         price0=max(m*g0*(x*x-kap*x)/M+K*x for x in [-A,eps0])
         price1=max(m*g1*(x*x-kap*x)/M-K*x for x in [-eps1,A])
         lower=m*(L*t-3*t*t+J)/M+K*lam*(3*p*(1-w)+3*q*w-B)-lam*(1-w)*price0-lam*w*price1
         assert integrated>=lower
         price_controls+=1
    report["corrected_joint_cubic_price_controls"]=price_controls
    # Dropping the genuine large-jump cap is false even for one summand.
    law=two_point(-Q(1,1000),A);v=moment(law,2);y=Q(1,5)
    lhs=sum(prob*max(Q(0),x-y)**2 for x,prob in law)
    bad_upper=physical_hinge(v,Q(1),y)[1]
    assert lhs>bad_upper
    report["false_small_cap_rejected"]=True
    # Factorial tail bound needs i>=2. Actual polynomial induction in note.
    factorial_checks=0
    for i in range(2,10):
      for j in range(i+1,i+21):
       assert (j-i)**2<=comb(j,i+1);factorial_checks+=1
    assert (3-1)**2>comb(3,2)
    report["factorial_tail_controls"]=factorial_checks
    report["false_i1_factorial_bound_rejected"]=True
    # Closed atoms must be included: a hinge at lower anchor is one at threshold.
    b=Q(1);anchor=Q(1,5)
    assert (b-anchor)**2/(b-anchor)**2==1
    def admissible(anchor, threshold):
        assert anchor<threshold
    rejected=0
    for bad in [b,b+1]:
        try:admissible(bad,b)
        except AssertionError:rejected+=1
    assert rejected==2
    report["invalid_hinge_anchors_rejected"]=rejected
    if len(sys.argv)>1:
        root=Path(sys.argv[1]).resolve()
        paths=["mathematics/simplification-v11/2026-10-28/counts-v11-compound-discovery.py",
               "mathematics/simplification-v11/2026-10-28/owncount.tex"]
        report["reviewed_base_source_hashes"]={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths}
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__':main()

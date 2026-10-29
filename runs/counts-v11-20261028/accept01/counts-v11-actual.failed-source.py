"""Exact rare-jump, conditional moment, event collision and neighbor controls."""
from fractions import Fraction as F
from math import comb,factorial
import json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')

def binomial(m,p):return [(j,F(comb(m,j))*p**j*(1-p)**(m-j)) for j in range(m+1)]
def prob(law,fn):return sum((w for x,w in law if fn(x)),F(0))
def moment(law,j):return sum((w*x**j for x,w in law),F(0))
def three_atom_sum(atoms,n):
    out=[];powers=[[w**j for j in range(n+1)] for x,w in atoms]
    for i in range(n+1):
      for j in range(n-i+1):
        k=n-i-j
        out.append((i*atoms[0][0]+j*atoms[1][0]+k*atoms[2][0],F(comb(n,i)*comb(n-i,j))*powers[0][i]*powers[1][j]*powers[2][k]))
    return out

laws=events=collisions=zero_neighbors=positive_neighbors=0
max_cubic_identity_error=F(0)
for p in [F(2,5),F(1,2),F(53,100)]:
 for lam in [F(1,50),F(3,100),F(3,40)]:
  for side in [0,1]:
    n=42;q=1-p;v=p*q;A=F(3,5);weight=q if side==0 else p
    b=lam/(n*weight*A);s=lam/n;k=int(n*p);delta=k-n*p
    assert b<=F(9,125)
    noise=[(-A,b/(A+b)),(b,A/(A+b))] if side==0 else [(-b,A/(A+b)),(A,b/(A+b))]
    atoms=[(x,weight*w) for x,w in noise]+[(F(1),p)] if side==0 else [(F(0),q)]+[(1+x,weight*w) for x,w in noise]
    assert sum(w for x,w in atoms)==1 and moment(atoms,1)==p
    assert moment([(x-p,w) for x,w in atoms],2)==v+s
    raw3=sum(w*abs(x-p)**3 for x,w in atoms)
    m3=moment(noise,3);variance=moment(noise,2)
    cubic_identity=v*(1-2*v)+3*v*variance+(p*m3 if side else -q*m3)
    assert raw3==cubic_identity
    # Exact squared normalization verifies rho>=rho_B without radicals.
    assert raw3**2*v>(1-2*v)**2*(v+s)**3
    def W(j):
        m=n-j if side==0 else j
        return [((m*b-(A+b)*z) if side==0 else (-m*b+(A+b)*z),w) for z,w in binomial(m,b/(A+b))]
    bins=binomial(n,p);full=three_atom_sum(atoms,n)
    own=W(k);collision=(n-k)*b if side==0 else -k*b
    for u in [F(-1,10),F(0),F(1,10),collision]:
        assert -F(34,125)<=u<=F(91,125)
        assert (delta+u)**2<=F(46,25)**2*(v+s)
        cdf=prob(full,lambda x:x<=k+u)
        conditional=sum(pi*prob(W(j),lambda w:w<=k+u-j) for j,pi in bins)
        FB=sum(pi for j,pi in bins if j<=k)
        difference=-sum(pi*prob(W(j),lambda w:w>k+u-j) for j,pi in bins if j<=k)
        difference+=sum(pi*prob(W(j),lambda w:w<=k+u-j) for j,pi in bins if j>k)
        assert cdf==conditional and cdf-FB==difference
        alpha=F(13,25)
        h=lambda x:(-x**4+3*alpha**2*x*x+2*alpha**3*x)/(5*alpha**4)
        assert sum(w*h(x-u) for x,w in own)<=prob(own,lambda x:x>u)
        t=moment(own,2);kap=4*u
        cap=max(A*A+kap*A,b*b-kap*b) if side==0 else max(A*A-kap*A,b*b+kap*b)
        assert moment(own,4)-kap*moment(own,3)<=cap*t+3*t*t
        neighbor=prob(W(k-1),lambda x:x>u+1)
        if side==0:
            assert neighbor==0;zero_neighbors+=1
        elif neighbor>0:positive_neighbors+=1
        if u==collision:
            assert prob(own,lambda x:x==u)>0
            assert prob(own,lambda x:x>=u)>prob(own,lambda x:x>u)
            collisions+=1
        events+=1
    laws+=1

# Bernoulli endpoint: both conditional noises vanish; every count identity is exact.
for p in [F(2,5),F(1,2),F(53,100)]:
    n=42;k=int(n*p);bins=binomial(n,p)
    for u in [F(-1,10),F(0),F(1,10)]:
        assert sum(w for j,w in bins if j<=k+u)==sum(w for j,w in bins if F(j-k)<=u)
print(json.dumps({'status':'PASS_EXACT_RARE_JUMP_AND_COLLISION_CONTROLS','actual_nonzero_laws':laws,'exact_event_cases':events,'own_atom_collisions':collisions,'zero_neighbor_cases':zero_neighbors,'positive_neighbor_cases':positive_neighbors,'Bernoulli_endpoint_cases':9,'scope':'These finite actual-law controls verify algebra and event conventions, not uniform theorem coverage. The lambda=.075 cases remain outside the new theorem.','python':sys.version},indent=2))

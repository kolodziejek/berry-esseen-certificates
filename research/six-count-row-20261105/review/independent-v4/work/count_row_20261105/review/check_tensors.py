"""Independent inverse-Bernstein and direct cleared-expectation review.

The constructor supplies tensors only. This reader expands Bernstein bases
back to ordinary monomials and independently builds the direct moment formula.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import product
import hashlib,importlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('no optimized Python')
HERE=Path(__file__).resolve().parent;CONSTRUCT=HERE.parent/'construct'
sys.path.insert(0,str(CONSTRUCT))
m=importlib.import_module('model');m2=importlib.import_module('model_v2');m3=importlib.import_module('model_v3')
def need(x,msg):
    if not x:raise ValueError(msg)
def tidy(p):return {ij:a for ij,a in p.items() if a}
def add(*ps):
    r={}
    for p in ps:
      for ij,a in p.items():r[ij]=r.get(ij,F(0))+a
    return tidy(r)
def scale(p,c):return tidy({ij:c*a for ij,a in p.items()})
def mul(p,q):
    r={}
    for (i,j),a in p.items():
      for (k,l),b in q.items():r[i+k,j+l]=r.get((i+k,j+l),F(0))+a*b
    return tidy(r)
ONE={(0,0):F(1)};P={(1,0):F(1)};U={(0,1):F(1)};Q=add(ONE,scale(P,-1));V=mul(P,Q);V2=mul(V,V)
def power(p,n):
    r=ONE
    for _ in range(n):r=mul(r,p)
    return r
def local(p,pl,pu,ul,uh):
    r={}
    for (i,j),a in p.items():
      for h in range(i+1):
       for k in range(j+1):
        r[h,k]=r.get((h,k),F(0))+a*comb(i,h)*pl**(i-h)*(pu-pl)**h*comb(j,k)*ul**(j-k)*(uh-ul)**k
    return tidy(r)
def inverse(b):
    need(len(b)==50,'tensor shape');r={}
    for a in range(10):
      for c in range(5):
       z=b[5*a+c]*comb(9,a)*comb(4,c)
       for i in range(a,10):
        for j in range(c,5):
         r[i,j]=r.get((i,j),F(0))+z*comb(9-a,i-a)*comb(4-c,j-c)*(-1)**(i-a+j-c)
    return tidy(r)
def direct(k,x,y,g0,g1,qs):
    total={}
    for j,c in enumerate(qs):
        a=add(scale(ONE,F(j-k)),scale(U,-1))
        T=add(scale(P,(5-j)*x),scale(Q,j*y))
        G=add(scale(P,(5-j)*x*g0),scale(Q,j*y*g1))
        L=add(scale(P,(5-j)*x*g0*g0),scale(Q,j*y*g1*g1))
        first=mul(V2,add(*(scale(power(a,r),c[r]) for r in range(5))))
        second=mul(mul(T,V),add(scale(ONE,c[2]),scale(a,3*c[3]),scale(power(a,2),6*c[4])))
        third=mul(mul(G,V),add(scale(ONE,c[3]),scale(a,4*c[4])))
        fourth=add(scale(mul(L,V),c[4]),scale(mul(T,T),F(12,5)*c[4]))
        mass=scale(mul(power(P,j),power(Q,5-j)),F(comb(5,j)))
        total=add(total,mul(mass,add(first,second,third,fourth)))
    return total
def main(out):
    sources=[Path(__file__)]+[CONSTRUCT/n for n in ('model.py','model_v2.py','model_v3.py','accept.py')]+list((CONSTRUCT/'native').glob('*'))
    sources=[p for p in sources if p.is_file()]
    before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    qs=[[F(j+2,5),F(j-3,7),F(j-2,11),F((-1)**j,13),F(j+1,17)] for j in range(6)]
    tests=[(m,(2,m.PL,m.PU,F(-1,100),F(1,100))),
      (m2,(2,m.PL,m.PU,F(-1,2),F(-2,5))),
      (m3,(2,m.PL,m.PU,F(-1,2),F(-2,5),F(0),m.LAMBDA/2)),
      (m3,(1,m.PL,m.PU,F(1,4),F(1,2),m.LAMBDA/2,m.LAMBDA))]
    counts=dict(complete_moment_rows=0,exact_moment_coefficients=0,exact_target_coefficients=0,
      independent_ray_polynomials=0,mutant_rejections=0,negative_relaxed_R_vertices=0)
    for version,domain in tests:
        k,pl,pu,ul,uh=domain[:5];rows=version.tensors(*domain)
        vertices=version.polygon(pl,pu,*domain[5:]) if version is m3 else version.polygon(pl,pu)
        expected=[(x,y,g0,g1) for x,y in vertices for g0,g1 in product((-m.A0,F(0),min(m.D,pu)),(m.A1,F(0),-min(m.D,1-pl)))]
        need(len(rows)==len(expected),'all independent corners')
        for row,(x,y,g0,g1) in zip(rows,expected):
            b=[sum(qs[j][r]*row[5*j+r][i] for j in range(6) for r in range(5)) for i in range(50)]
            got=inverse(b);raw=direct(k,x,y,g0,g1,qs)
            need(all(i<=9 and j<=4 for i,j in raw),'independent degree bound')
            want=local(raw,pl,pu,ul,uh)
            need(got==want,'complete inverse Bernstein expectation equality')
            counts['complete_moment_rows']+=1;counts['exact_moment_coefficients']+=50
            broken=b[:];broken[17]+=F(1,10**9)
            need(inverse(broken)!=want,'a coefficient corruption is detected');counts['mutant_rejections']+=1
        if version is m3:
            targets,diffs,flag=version.target_tensors(domain)
            lo,hi=domain[5:];amin=k+ul-5*pu;amax=k+uh-5*pl
            need(flag==(amax<=0 and amin*amin<=15*pl*(1-pl)),'independent curvature guard')
            wmax=pu*(1-pu)+hi/5
            c=m.normal.CE_LO/(m.normal.root(F(5))[1]*wmax*m.normal.root(wmax)[1])
            floor=m.normal.CE_LO*m.RHO/m.normal.root(F(5))[1]
            theta=F(2,3)
            for rhs,diff,(x,y,g0,g1) in zip(targets,diffs,expected):
                den=5*pl*(1-pl)+5*(x+y) if flag else (5*pl*(1-pl)+lo if amin<0 else 5*pu*(1-pu)+hi)
                scalar=m.normal_lower(amin,den)+(1-theta)*floor
                R=add(mul(V,add(ONE,scale(V,-2))),scale(P,3*x),scale(Q,3*y),scale(ONE,-g0*x+g1*y))
                want=local(mul(V2,add(scale(ONE,scalar),scale(R,theta*c))),pl,pu,ul,uh)
                need(inverse([a+theta*b for a,b in zip(rhs,diff)])==want,'independent blended target identity')
                counts['exact_target_coefficients']+=50
                for p in (pl,pu):
                    r=p*(1-p)*(1-2*p*(1-p))+3*(p*x+(1-p)*y)-g0*x+g1*y
                    counts['negative_relaxed_R_vertices']+=int(r<0)
        else:
            targets=[version.target_tensor(*domain)]*len(rows) if version is m else version.target_tensors(domain)
            for b in targets:
                got=inverse(b);need(all(j==0 for i,j in got),'fixed Gaussian bound independent of phase coordinate')
                counts['exact_target_coefficients']+=50
    # Direct ray reconstruction, including the event-plane constant on the left.
    for q in qs:
      for sign,sub in ((-1,F(1)),(1,F(0))):
        got=m.compact_ray(q,sign,sub)
        for t in (F(0),F(1,7),F(1,2),F(6,7)):
            want=(1-t)**4*(sum(q[j]*(sign*t/(1-t))**j for j in range(5))-sub)
            need(sum(a*t**j for j,a in enumerate(got))==want,'independent compact ray identity')
        need(got[0]==q[0]-sub and sum(got)==q[4],'ray endpoints include atom and infinity')
        counts['independent_ray_polynomials']+=1
    after={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources};need(before==after,'all reviewed source bytes stable')
    result=dict(status='PASS',scope='Independent full coefficient reconstruction on four selected closed cells, not a numerical proof-object or full-row admission.',counts=counts,source_sha256=before)
    out=Path(out);out.mkdir(parents=True,exist_ok=False);(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main(sys.argv[1])

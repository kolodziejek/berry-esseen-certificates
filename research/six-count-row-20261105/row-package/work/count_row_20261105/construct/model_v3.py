"""Additive noise-slab, same-law cubic price. Original target is unchanged."""
from model import *
import model as original
def cell(k,ps,us,noise):
    d=original.cell(k,ps,us);lo,hi=map(F,noise)
    need(0<=lo<hi<=LAMBDA,'closed noise slab');return d+(lo,hi)
@lru_cache(maxsize=128)
def polygon(pl,pu,lo,hi):
    rhi=mul(V,(BHI-1,F(2)));rlo=mul(V,(1-BLO,-F(2)))
    planes=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),hi/N),(-F(1),-F(1),-lo/N),
      (-(1+BHI),1-BHI,max(bernstein(rhi,pl,pu,3))),(1+BLO,-(1-BLO),max(bernstein(rlo,pl,pu,3)))]
    vs=set()
    for(a,b,c),(d,e,f)in combinations(planes,2):
        det=a*e-b*d
        if not det:continue
        x=(c*e-b*f)/det;y=(a*f-c*d)/det
        if all(A*x+B*y<=C for A,B,C in planes):vs.add((x,y))
    need(len(vs)>=3,'nonempty noise-slab outer polygon');return tuple(sorted(vs))
def tensors(k,pl,pu,ul,uh,lo,hi):
    shift={(j,d):bernstein(power((F(j-k),-F(1)),d),ul,uh,DEGU)for j in range(6)for d in range(5)}
    base0=mul(mul(P,P),Q);base1=mul(P,mul(Q,Q))
    masses=[scale(mul(power(P,j),power(Q,N-j)),F(comb(N,j)))for j in range(6)]
    out=[]
    for x,y in polygon(pl,pu,lo,hi):
      for g0,g1 in product((-A0,F(0),min(D,pu)),(A1,F(0),-min(D,1-pl))):
        row=[]
        for j,mass in enumerate(masses):
            aa=(N-j)*x;bb=j*y;tv=add(scale(P,aa),scale(Q,bb))
            mom=[V2,(F(0),),add(scale(base0,aa),scale(base1,bb)),
              add(scale(base0,aa*g0),scale(base1,bb*g1)),
              add(add(scale(base0,aa*g0*g0),scale(base1,bb*g1*g1)),scale(mul(tv,tv),F(12,5)))]
            bm=[bernstein(mul(mass,m),pl,pu,DEGP)for m in mom]
            for d in range(5):row.append(tuple(sum(F(comb(d,i))*bm[i][a]*shift[j,d-i][b]for i in range(d+1))for a in range(10)for b in range(5)))
        out.append(row)
    return out
def target_tensors(domain):
    k,pl,pu,ul,uh,lo,hi=domain;amin=F(k)+ul-N*pu;amax=F(k)+uh-N*pl
    correlated=amax<=0 and amin*amin<=3*N*pl*(1-pl)
    wmax=pu*(1-pu)+hi/N
    c=normal.CE_LO/(normal.root(F(N))[1]*wmax*normal.root(wmax)[1])
    floor=normal.CE_LO*RHO/normal.root(F(N))[1]
    targets=[];improvements=[]
    for x,y in polygon(pl,pu,lo,hi):
      for g0,g1 in product((-A0,F(0),min(D,pu)),(A1,F(0),-min(D,1-pl))):
        den=N*pl*(1-pl)+N*(x+y)if correlated else(N*pl*(1-pl)+lo if amin<0 else N*pu*(1-pu)+hi)
        target0=normal_lower(amin,den)+floor
        raw=add(mul(V,add((F(1),),scale(V,-2))),add(add(scale(P,3*x),scale(Q,3*y)),(-g0*x+g1*y,)))
        difference=add(scale(raw,c),(-floor,))
        targets.append(tuple(v for v in bernstein(scale(V2,target0),pl,pu,DEGP)for _ in range(5)))
        improvements.append(tuple(v for v in bernstein(mul(V2,difference),pl,pu,DEGP)for _ in range(5)))
    return targets,improvements,correlated
def admit(qs,theta,domain,rows=None):
    theta=rational(theta);need(0<=theta<=1,'fixed convex rho weight')
    need(type(qs)is list and len(qs)==6,'six ordered actual count polynomials');exact=[]
    for row in qs:
        need(type(row)is list and len(row)==5,'five quartic coefficients')
        q=list(map(rational,row));need(q[4]>0,'strict positive leading coefficient')
        sturm.positive(compact_ray(q,-1,F(1)));sturm.positive(compact_ray(q,1,F(0)));exact.extend(q)
    rows=tensors(*domain)if rows is None else rows
    targets,diffs,correlated=target_tensors(domain);need(len(targets)==len(rows),'all common vertices')
    margin=None
    for row,rhs,diff in zip(rows,targets,diffs):
        z=min(rhs[a]+theta*diff[a]-sum(exact[d]*row[d][a]for d in range(30))for a in range(50))
        need(z>0,'strict whole-cell tensor bound');margin=z if margin is None else min(margin,z)
    k,pl,pu,ul,uh,lo,hi=domain
    return dict(k=k,p=list(map(str,(pl,pu))),u=list(map(str,(ul,uh))),noise=list(map(str,(lo,hi))),theta=str(theta),
      vertices=len(polygon(pl,pu,lo,hi)),moment_pairs=9,global_rays=12,tensor_coefficients=50*len(rows),
      cleared_margin=str(margin),gaussian_noise_correlation=correlated)

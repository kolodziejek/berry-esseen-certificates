"""Exact n5 transfer model: three externally fixed original contracts.

Both probability halves are handled directly. No reflection or original
acquisition is inferred from this conditional comparison reader.
"""
from algebra import *
from itertools import combinations,product
CONTRACTS={
 'BN39':'8d2a6ec51bf43b45a7ce2de62d5ed734a90498924cb60c833a3976394eef3d9a',
 'B0_50':'2939dcca05896e1c6393c50944df8dd5e872efb26076a7304df45d9f6d07a93f',
 'B2_S3_34':'a9e2574fbb79e8d21d7bf6d5a9bc152ba6981878101c0dafd3eb7088233ba6d5'}
def variance_bounds(pl,pu):
    need(0<pl<=pu<1,'probability interval')
    ends=[pl*(1-pl),pu*(1-pu)]
    return min(ends),max(ends+[F(1,4)]if pl<=F(1,2)<=pu else ends)
def floor(x):return x.numerator//x.denominator
def ceil(x):return -((-x.numerator)//x.denominator)
class Row:
    N=5
    def __init__(self,key):
        need(type(key)is str and key in CONTRACTS,'fixed external row identity')
        self.key=key;self.contract_sha=CONTRACTS[key]
        path=HERE/'contracts'/f'{key}.json';need(sha(path)==self.contract_sha,'unchanged original contract')
        record=json.loads(path.read_text(),object_pairs_hook=unique)
        need(type(record['n'])is int and record['n']==5 and len(record['rows'])==1,'literal n5 contract')
        c=record['rows'][0];need(c['n']==5 and c['K']=='0','original CE/K0 target')
        need(c['sign_premise']['schema']=='ACTUAL_SIGN_CONDITIONED_MARGINAL_V1'and c['sign_premise']['conditional_means_zero']is True,'actual sign-conditioned centered premises')
        self.cfg=c;self.pl,self.pu=map(F,c['p']);self.A0=F(c['outer0']);self.A1=F(c['outer1']);self.D=F(c['acquired_inward_upper'])
        self.LAMBDA=F(c['acquired_lambda_upper']);self.BLO,self.BHI=map(F,c['acquired_beta']);self.RHO=F(c['rho_lower'])
        self.MEAN_LO=F(c['acquired_mean'][0]);self.NEG_LO=F(c['sign_premise']['negative_endpoint_lower']);self.POS_LO=F(c['sign_premise']['positive_endpoint_lower'])
        need(0<self.pl<self.pu<1 and self.RHO>0 and self.LAMBDA>0 and min(self.A0,self.A1,self.MEAN_LO,self.NEG_LO,self.POS_LO)>0,'positive original scalar domains')
        scale=F(c['acquired_scale_upper']);self.hlo=5*self.pl-F(c['Hminus'])*scale;self.hhi=5*self.pu+F(c['Hplus'])*scale
        # Both closed nearest-count representations survive every half-integer tie.
        self.roots={k:(max(-F(1,2),self.hlo-k),min(F(1,2),self.hhi-k))for k in range(ceil(self.hlo-F(1,2)),floor(self.hhi+F(1,2))+1)}
        need(self.roots and all(l<h for l,h in self.roots.values()),'nondegenerate complete threshold catalogue')
    def cell(self,k,ps,us,noise):
        need(type(k)is int and k in self.roots,'licensed integer center')
        pl,pu=map(F,ps);ul,uh=map(F,us);lo,hi=map(F,noise)
        need(self.pl<=pl<pu<=self.pu and -F(1,2)<=ul<uh<=F(1,2),'closed probability/phase cell')
        need(0<=lo<hi<=self.LAMBDA,'original closed noise slab')
        return k,pl,pu,ul,uh,lo,hi
    def effective_hi(self,pl,pu,hi):
        vmin,vmax=variance_bounds(pl,pu)
        need(2*vmin>self.MEAN_LO**2,'mean/noise monotonicity in v')
        return min(hi,5*(vmax*vmax/self.MEAN_LO**2-vmax))
    def inward(self,pl,pu,lo):
        vmin,_=variance_bounds(pl,pu);r=normal.root(vmin+lo/5)[0]
        a0=min(self.D,pu-self.NEG_LO*r);a1=min(self.D,1-pl-self.POS_LO*r)
        need(a0>=0 and a1>=0,'nonnegative outward inward ceilings');return a0,a1
    @lru_cache(maxsize=256)
    def polygon(self,pl,pu,lo,hi):
        hi=self.effective_hi(pl,pu,hi);need(lo<hi,'nonempty mean-noise slab')
        rhi=mul(V,(self.BHI-1,F(2)));rlo=mul(V,(1-self.BLO,-F(2)))
        planes=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),hi/5),(-F(1),-F(1),-lo/5),
          (-(1+self.BHI),1-self.BHI,max(bernstein(rhi,pl,pu,3))),
          (1+self.BLO,-(1-self.BLO),max(bernstein(rlo,pl,pu,3)))]
        out=set()
        for(a,b,c),(d,e,f)in combinations(planes,2):
            det=a*e-b*d
            if not det:continue
            x=(c*e-b*f)/det;y=(a*f-c*d)/det
            if all(A*x+B*y<=C for A,B,C in planes):out.add((x,y))
        need(len(out)>=3,'nondegenerate exact outer polygon; no empty-domain acceptance')
        return tuple(sorted(out))
    def tensors(self,k,pl,pu,ul,uh,lo,hi):
        shift={(j,d):bernstein(power((F(j-k),-F(1)),d),ul,uh,4)for j in range(6)for d in range(5)}
        base0=mul(mul(P,P),Q);base1=mul(P,mul(Q,Q))
        masses=[scale(mul(power(P,j),power(Q,5-j)),F(comb(5,j)))for j in range(6)];out=[]
        r0,r1=self.inward(pl,pu,lo)
        for x,y in self.polygon(pl,pu,lo,hi):
          for g0,g1 in product((-self.A0,F(0),r0),(self.A1,F(0),-r1)):
            row=[]
            for j,mass in enumerate(masses):
                aa=(5-j)*x;bb=j*y;tv=add(scale(P,aa),scale(Q,bb))
                mom=[V2,(F(0),),add(scale(base0,aa),scale(base1,bb)),
                  add(scale(base0,aa*g0),scale(base1,bb*g1)),
                  add(add(scale(base0,aa*g0*g0),scale(base1,bb*g1*g1)),scale(mul(tv,tv),F(12,5)))]
                bm=[bernstein(mul(mass,m),pl,pu,9)for m in mom]
                for d in range(5):row.append(tuple(sum(F(comb(d,i))*bm[i][a]*shift[j,d-i][b]for i in range(d+1))for a in range(10)for b in range(5)))
            out.append(row)
        return out
    def target_tensors(self,domain):
        k,pl,pu,ul,uh,lo,hi=domain;amin=F(k)+ul-5*pu;amax=F(k)+uh-5*pl
        vmin,vmax=variance_bounds(pl,pu)
        correlated=amax<=0 and amin*amin<=15*vmin
        # For 0<=k+u<=n, the standardized numerator decreases with p.
        # The endpoint p_hi may therefore supply numerator AND variance.
        same_endpoint=0<=F(k)+ul and F(k)+uh<=5
        hi=self.effective_hi(pl,pu,hi);wmax=vmax+hi/5
        c=normal.CE_LO/(normal.root(F(5))[1]*wmax*normal.root(wmax)[1]);lower=normal.CE_LO*self.RHO/normal.root(F(5))[1]
        targets=[];improvements=[];r0,r1=self.inward(pl,pu,lo)
        for x,y in self.polygon(pl,pu,lo,hi):
          for g0,g1 in product((-self.A0,F(0),r0),(self.A1,F(0),-r1)):
            if same_endpoint:
                den=5*pu*(1-pu)+(5*(x+y)if correlated else(lo if amin<0 else hi))
            else:den=5*vmin+5*(x+y)if correlated else(5*vmin+lo if amin<0 else 5*vmax+hi)
            target0=normal_lower(amin,den)+lower
            raw=add(mul(V,add((F(1),),scale(V,-2))),add(add(scale(P,3*x),scale(Q,3*y)),(-g0*x+g1*y,)))
            difference=add(scale(raw,c),(-lower,))
            targets.append(tuple(v for v in bernstein(scale(V2,target0),pl,pu,9)for _ in range(5)))
            improvements.append(tuple(v for v in bernstein(mul(V2,difference),pl,pu,9)for _ in range(5)))
        return targets,improvements,correlated
    def admit(self,qs,theta,domain,rows=None):
        theta=rational(theta);need(0<=theta<=1,'fixed convex rho weight')
        need(type(qs)is list and len(qs)==6,'all six ordered count polynomials');exact=[]
        for row in qs:
            need(type(row)is list and len(row)==5,'five coefficients')
            q=list(map(rational,row));need(q[4]>0,'positive leading quartic')
            sturm.positive(compact_ray(q,-1,F(1)));sturm.positive(compact_ray(q,1,F(0)));exact.extend(q)
        rows=self.tensors(*domain)if rows is None else rows
        targets,diffs,correlated=self.target_tensors(domain);need(len(targets)==len(rows),'complete common vertex set')
        margin=None
        for row,rhs,diff in zip(rows,targets,diffs):
            z=min(rhs[a]+theta*diff[a]-sum(exact[d]*row[d][a]for d in range(30))for a in range(50))
            need(z>0,'strict complete-cell tensor inequality');margin=z if margin is None else min(margin,z)
        k,pl,pu,ul,uh,lo,hi=domain
        return dict(row_id=self.key,k=k,p=list(map(str,(pl,pu))),u=list(map(str,(ul,uh))),noise=list(map(str,(lo,hi))),theta=str(theta),
          vertices=len(self.polygon(pl,pu,lo,hi)),moment_pairs=9,global_rays=12,tensor_coefficients=50*len(rows),
          cleared_margin=str(margin),gaussian_noise_correlation=correlated)

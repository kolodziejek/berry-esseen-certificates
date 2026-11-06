"""Exact n=5 all-Taylor curvature-corrected model across both probability halves.

Combines the both-half Gaussian Taylor lower polynomial (using endpoint variance
minimum vmin = min(pl*(1-pl), pu*(1-pu))), uniform noise-curvature correction
H_F(p) - 25 M J >= 0 when amax > 0, and optional raw-moment dual prices.
"""
from algebra import *
from itertools import combinations,product
from gaussian_scalar import curvature,gaussian
from selector import CONTRACTS,ceil,derive_roots,floor,select_contract

def variance_bounds(pl,pu):
    need(0<pl<=pu<1,'probability interval')
    ends=[pl*(1-pl),pu*(1-pu)]
    return min(ends),max(ends+[F(1,4)]if pl<=F(1,2)<=pu else ends)

class Row:
    N=5
    def __init__(self,spec):
        entry=select_contract(spec)
        self.entry=entry;self.key=entry.get('row_id',entry['path']);self.contract_sha=entry['sha256']
        self.path=entry['path'];self.band=entry['band'];self.slab_family=entry['slab_family'];self.index=entry['index']
        c=entry['row'];need(c['n']==5 and c['K']=='0','original CE/K0 target')
        need(c['sign_premise']['schema']=='ACTUAL_SIGN_CONDITIONED_MARGINAL_V1'and c['sign_premise']['conditional_means_zero']is True,'actual sign-conditioned centered premises')
        self.cfg=c;self.pl,self.pu=map(rational,c['p']);self.A0=rational(c['outer0']);self.A1=rational(c['outer1']);self.D=rational(c['acquired_inward_upper'])
        self.LAMBDA=rational(c['acquired_lambda_upper']);self.BLO,self.BHI=map(rational,c['acquired_beta']);self.RHO=rational(c['rho_lower']);self.RHO_HI=rational(c['rho_upper'])
        self.GAMMA_LO,self.GAMMA_HI=map(rational,c['acquired_gamma'])
        self.MEAN_LO=rational(c['acquired_mean'][0]);self.NEG_LO=rational(c['sign_premise']['negative_endpoint_lower']);self.POS_LO=rational(c['sign_premise']['positive_endpoint_lower'])
        need(0<self.pl<self.pu<1 and 0<self.RHO<=self.RHO_HI and self.GAMMA_LO<=self.GAMMA_HI and self.LAMBDA>0 and min(self.A0,self.A1,self.MEAN_LO,self.NEG_LO,self.POS_LO)>0,'positive original scalar domains')
        self.hlo,self.hhi,self.roots=derive_roots(c)
    def cell(self,k,ps,us,noise):
        need(type(k)is int and not isinstance(k,bool)and k in self.roots,'licensed integer center')
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
    def raw_bounds(self,domain):
        k,pl,pu,ul,uh,lo,hi=domain;vmin,vmax=variance_bounds(pl,pu)
        wl=vmin+lo/5;wh=vmax+self.effective_hi(pl,pu,hi)/5
        sl=wl*normal.root(wl)[0];sh=wh*normal.root(wh)[1]
        rl,rh=self.RHO,self.RHO_HI;gl,gh=self.GAMMA_LO,self.GAMMA_HI
        need(0<rl<=rh and gl<=gh and 0<sl<=sh,'original normalized moment domains')
        return rl*sl,rh*sh,min(gl*sl,gl*sh),max(gh*sl,gh*sh)
    def dual_tensors(self,domain):
        k,pl,pu,ul,uh,lo,hi=domain;rl,rh,gl,gh=self.raw_bounds(domain)
        r0,r1=self.inward(pl,pu,lo);out=[]
        for x,y in self.polygon(pl,pu,lo,hi):
          for g0,g1 in product((-self.A0,F(0),r0),(self.A1,F(0),-r1)):
            raw=add(mul(V,add((F(1),),scale(V,-2))),add(add(scale(P,3*x),scale(Q,3*y)),(-g0*x+g1*y,)))
            signed=add(mul(V,(F(1),-F(2))),add(add(scale(P,-3*x),scale(Q,3*y)),(g0*x+g1*y,)))
            slacks=[add((rl,),scale(raw,-1)),add(raw,(-rh,)),add((gl,),scale(signed,-1)),add(signed,(-gh,))]
            out.append([tuple(z for z in bernstein(mul(V2,s),pl,pu,9)for _ in range(5))for s in slacks])
        return out
    def target_tensors(self,domain):
        k,pl,pu,ul,uh,lo,hi=domain
        vmin,vmax=variance_bounds(pl,pu)
        M_curv,curv_rec=curvature(5,k,pl,pu,ul,uh,lo)
        hi_eff=self.effective_hi(pl,pu,hi);wmax=vmax+hi_eff/5
        c=normal.CE_LO/(normal.root(F(5))[1]*wmax*normal.root(wmax)[1]);lower=normal.CE_LO*self.RHO/normal.root(F(5))[1]
        targets=[];improvements=[];r0,r1=self.inward(pl,pu,lo)
        for x,y in self.polygon(pl,pu,lo,hi):
            G,_=gaussian(5,k,pl,pu,ul,uh,5*(x+y))
            powers=[mul(V2,tuple(g))for g in G]+[(F(0),),(F(0),)]
            powers[0]=add(powers[0],scale(V2,lower))
            bp=[bernstein(g,pl,pu,9)for g in powers]
            target=tuple(z for i in range(10)for z in bernstein(tuple(bp[h][i]for h in range(5)),ul,uh,4))
            for g0,g1 in product((-self.A0,F(0),r0),(self.A1,F(0),-r1)):
                raw=add(mul(V,add((F(1),),scale(V,-2))),add(add(scale(P,3*x),scale(Q,3*y)),(-g0*x+g1*y,)))
                difference=add(scale(raw,c),(-lower,))
                targets.append(target)
                improvements.append(tuple(v for v in bernstein(mul(V2,difference),pl,pu,9)for _ in range(5)))
        return targets,improvements,M_curv,curv_rec
    def psd_check(self,qs,pl,pu,M_curv):
        masses=[scale(mul(power(P,j),power(Q,5-j)),F(comb(5,j)))for j in range(6)]
        h00=(F(0),);h01=(F(0),);h11=(F(0),)
        for j,q in enumerate(qs):
            c4=q[4];a=F(5-j);b=F(j);w=scale(masses[j],F(24,5)*c4)
            h00=add(h00,scale(mul(w,mul(P,P)),a*a))
            h01=add(h01,scale(mul(w,mul(P,Q)),a*b))
            h11=add(h11,scale(mul(w,mul(Q,Q)),b*b))
        if M_curv>0:
            corr=scale(V2,25*M_curv)
            h00=add(h00,scale(corr,-1));h01=add(h01,scale(corr,-1));h11=add(h11,scale(corr,-1))
        b00=bernstein(h00,pl,pu,7);b11=bernstein(h11,pl,pu,7)
        bdet=bernstein(add(mul(h00,h11),scale(mul(h01,h01),-1)),pl,pu,14)
        mins=(min(b00),min(b11),min(bdet))
        need(min(mins)>=0,'curvature-corrected exact PSD Hessian polynomials')
        return list(map(str,mins))
    def admit(self,qs,theta,domain,prices=None,rows=None):
        theta=rational(theta);need(0<=theta<=1,'fixed convex rho weight')
        if prices is None:prices=[F(0)]*4
        else:
            need(type(prices)is list and len(prices)==4,'four original moment prices')
            prices=list(map(rational,prices));need(min(prices)>=0,'nonnegative exact moment prices')
        need(type(qs)is list and len(qs)==6,'all six ordered count polynomials');exact=[];parsed_qs=[]
        for row in qs:
            need(type(row)is list and len(row)==5,'five coefficients')
            q=list(map(rational,row));need(q[4]>0,'positive leading quartic')
            sturm.positive(compact_ray(q,-1,F(1)));sturm.positive(compact_ray(q,1,F(0)))
            exact.extend(q);parsed_qs.append(q)
        k,pl,pu,ul,uh,lo,hi=domain
        rows=self.tensors(*domain)if rows is None else rows
        targets,diffs,M_curv,curv_rec=self.target_tensors(domain);need(len(targets)==len(rows),'complete common vertex set')
        psd_mins=self.psd_check(parsed_qs,pl,pu,M_curv)
        use_prices=any(p>0 for p in prices)
        duals=self.dual_tensors(domain)if use_prices else None
        margin=None
        for idx,(row,rhs,diff)in enumerate(zip(rows,targets,diffs)):
            dual_row=duals[idx]if use_prices else None
            z=min(rhs[a]+theta*diff[a]+(sum(prices[i]*dual_row[i][a]for i in range(4))if use_prices else F(0))-sum(exact[d]*row[d][a]for d in range(30))for a in range(50))
            need(z>0,'strict complete-cell tensor inequality');margin=z if margin is None else min(margin,z)
        return dict(row_id=self.key,contract_sha256=self.contract_sha,k=k,p=list(map(str,(pl,pu))),u=list(map(str,(ul,uh))),noise=list(map(str,(lo,hi))),
          theta=str(theta),prices=list(map(str,prices)),vertices=len(self.polygon(pl,pu,lo,hi)),moment_pairs=9,global_rays=12,
          psd_coefficients=31,psd_minima=psd_mins,gaussian_noise_curvature_upper=str(M_curv),
          tensor_coefficients=50*len(rows),cleared_margin=str(margin),method='gaussian_taylor_both_halves_v1')

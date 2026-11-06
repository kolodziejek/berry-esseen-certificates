"""Exact n=5 all-Taylor curvature-corrected 4-pair model across both probability halves.

Combines the both-half Gaussian Taylor lower polynomial (using endpoint variance
minimum vmin = min(pl*(1-pl), pu*(1-pu))), uniform noise-curvature correction
H_F(p) - 25 M J >= 0 when amax > 0, variance-allocation cone (alpha in [al, ah]),
Cauchy-Schwarz third-moment shifts with shifted support-square affine fourth-moment
envelopes, the 4-endpoint-pair moment reduction, and optional raw-moment dual prices.
"""
from algebra import *
from itertools import combinations,product
from gaussian_scalar import curvature,gaussian
from selector import CONTRACTS,ceil,derive_roots,floor,select_contract

def variance_bounds(pl,pu):
    need(0<pl<=pu<1,'probability interval')
    ends=[pl*(1-pl),pu*(1-pu)]
    return min(ends),max(ends+[F(1,4)]if pl<=F(1,2)<=pu else ends)

def _unpack(domain):
    if len(domain)==7:return (*domain,F(0),F(1))
    need(len(domain)==9,'7-tuple or 9-tuple cell domain')
    return domain

class Row:
    N=5
    def __init__(self,spec):
        entry=select_contract(spec)
        self.entry=entry;self.key=entry.get('row_id',entry['path']);self.contract_sha=entry['sha256']
        self.path=entry['path'];self.band=entry['band'];self.slab_family=entry['slab_family'];self.series=entry.get('series',entry['band']);self.index=entry['index']
        c=entry['row'];need(c['n']==5 and c['K']=='0','original CE/K0 target')
        need(c['sign_premise']['schema']=='ACTUAL_SIGN_CONDITIONED_MARGINAL_V1'and c['sign_premise']['conditional_means_zero']is True,'actual sign-conditioned centered premises')
        self.cfg=c;self.pl,self.pu=map(rational,c['p']);self.A0=rational(c['outer0']);self.A1=rational(c['outer1']);self.D=rational(c['acquired_inward_upper'])
        self.LAMBDA=rational(c['acquired_lambda_upper']);self.BLO,self.BHI=map(rational,c['acquired_beta']);self.RHO=rational(c['rho_lower']);self.RHO_HI=rational(c['rho_upper'])
        self.GAMMA_LO,self.GAMMA_HI=map(rational,c['acquired_gamma'])
        self.MEAN_LO=rational(c['acquired_mean'][0]);self.NEG_LO=rational(c['sign_premise']['negative_endpoint_lower']);self.POS_LO=rational(c['sign_premise']['positive_endpoint_lower'])
        need(0<self.pl<self.pu<1 and 0<self.RHO<=self.RHO_HI and self.GAMMA_LO<=self.GAMMA_HI and self.LAMBDA>0 and min(self.A0,self.A1,self.MEAN_LO,self.NEG_LO,self.POS_LO)>0,'positive original scalar domains')
        self.hlo,self.hhi,self.roots=derive_roots(c)
    def cell(self,k,ps,us,noise,alpha=(0,1)):
        need(type(k)is int and not isinstance(k,bool)and k in self.roots,'licensed integer center')
        pl,pu=map(F,ps);ul,uh=map(F,us);lo,hi=map(F,noise);al,ah=map(F,alpha)
        need(self.pl<=pl<pu<=self.pu and -F(1,2)<=ul<uh<=F(1,2),'closed probability/phase cell')
        need(0<=lo<hi<=self.LAMBDA and 0<=al<ah<=1,'original closed noise/alpha slab')
        return (k,pl,pu,ul,uh,lo,hi)if(al,ah)==(F(0),F(1))else(k,pl,pu,ul,uh,lo,hi,al,ah)
    def effective_hi(self,pl,pu,hi):
        vmin,vmax=variance_bounds(pl,pu)
        need(2*vmin>self.MEAN_LO**2,'mean/noise monotonicity in v')
        return min(hi,5*(vmax*vmax/self.MEAN_LO**2-vmax))
    def inward(self,pl,pu,lo):
        vmin,_=variance_bounds(pl,pu);r=normal.root(vmin+lo/5)[0]
        a0=min(self.D,pu-self.NEG_LO*r);a1=min(self.D,1-pl-self.POS_LO*r)
        need(a0>=0 and a1>=0,'nonnegative outward inward ceilings');return a0,a1
    def moment_corners(self,pl,pu,lo,xmin=F(0),ymin=F(0)):
        r0,r1=self.inward(pl,pu,lo)
        s0_min=xmin/(1-pl);s1_min=ymin/pu
        d0_out=min(self.A0,s0_min/self.A0);d0_in=min(r0,s0_min/r0)if r0>0 else F(0)
        d1_out=min(self.A1,s1_min/self.A1);d1_in=min(r1,s1_min/r1)if r1>0 else F(0)
        g0_lo=-self.A0+d0_out;g0_hi=max(g0_lo,r0-d0_in)
        g1_hi=self.A1-d1_out;g1_lo=min(g1_hi,-r1+d1_in)
        K0=lambda g:(r0-self.A0-2*d0_in)*g+self.A0*r0-(self.A0-2*r0)*d0_in-d0_in*d0_in
        K1=lambda g:(self.A1-r1+2*d1_in)*g+self.A1*r1-(self.A1-2*r1)*d1_in-d1_in*d1_in
        c0=((g0_lo,K0(g0_lo)),(g0_hi,K0(g0_hi)))
        c1=((g1_hi,K1(g1_hi)),(g1_lo,K1(g1_lo)))
        return c0,c1,g0_lo,g0_hi,g1_lo,g1_hi
    @lru_cache(maxsize=512)
    def polygon(self,pl,pu,lo,hi,al=F(0),ah=F(1)):
        hi_eff=self.effective_hi(pl,pu,hi);need(lo<hi_eff and 0<=al<ah<=1,'nonempty mean-noise/alpha slab')
        vmin,_=variance_bounds(pl,pu)
        rhi=mul(V,(self.BHI-1,F(2)));rlo=mul(V,(1-self.BLO,-F(2)))
        base_planes=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),hi_eff/5),(-F(1),-F(1),-lo/5),
          (-(1+self.BHI),1-self.BHI,max(bernstein(rhi,pl,pu,3))),
          (1+self.BLO,-(1-self.BLO),max(bernstein(rlo,pl,pu,3))),
          (al,-(1-al),F(0)),(-ah,1-ah,F(0))]
        def solve_planes(planes):
            out=set()
            for(a,b,c),(d,e,f)in combinations(planes,2):
                det=a*e-b*d
                if not det:continue
                x=(c*e-b*f)/det;y=(a*f-c*d)/det
                if all(A*x+B*y<=C for A,B,C in planes):out.add((x,y))
            need(len(out)>=3,'nondegenerate exact outer polygon; no empty-domain acceptance')
            return tuple(sorted(out))
        pts=solve_planes(base_planes)
        if lo==0 and(al,ah)==(F(0),F(1)):return pts
        xmin=min(x for x,y in pts);ymin=min(y for x,y in pts)
        _,_,g0_lo,g0_hi,g1_lo,g1_hi=self.moment_corners(pl,pu,lo,xmin,ymin)
        _,rh,gl,gh=self.raw_bounds((self.roots[min(self.roots)],pl,pu,F(0),F(1,2),lo,hi))
        bvG=bernstein(mul(V,(F(1),-F(2))),pl,pu,3);vG_min,vG_max=min(bvG),max(bvG)
        planes=base_planes+[
          (3*pl-g0_hi,3*(1-pu)+g1_lo,rh-vmin*(1-2*vmin)),
          (-(3*pu-g0_lo),3*(1-pu)+g1_lo,gh-vG_min),
          (3*pl-g0_hi,-(3*(1-pl)+g1_hi),-gl+vG_max)]
        return solve_planes(planes)
    def cell_corners(self,pl,pu,lo,hi,al=F(0),ah=F(1)):
        poly=self.polygon(pl,pu,lo,hi,al,ah)
        xmin=min(x for x,y in poly);ymin=min(y for x,y in poly)
        c0,c1,*_=self.moment_corners(pl,pu,lo,xmin,ymin)
        return poly,c0,c1
    def tensors(self,k,pl,pu,ul,uh,lo,hi,al=F(0),ah=F(1)):
        shift={(j,d):bernstein(power((F(j-k),-F(1)),d),ul,uh,4)for j in range(6)for d in range(5)}
        base0=mul(mul(P,P),Q);base1=mul(P,mul(Q,Q))
        masses=[scale(mul(power(P,j),power(Q,5-j)),F(comb(5,j)))for j in range(6)];out=[]
        poly,c0,c1=self.cell_corners(pl,pu,lo,hi,al,ah)
        for x,y in poly:
          for(g0,k0),(g1,k1)in product(c0,c1):
            row=[]
            for j,mass in enumerate(masses):
                aa=(5-j)*x;bb=j*y;tv=add(scale(P,aa),scale(Q,bb))
                mom=[V2,(F(0),),add(scale(base0,aa),scale(base1,bb)),
                  add(scale(base0,aa*g0),scale(base1,bb*g1)),
                  add(add(scale(base0,aa*k0),scale(base1,bb*k1)),scale(mul(tv,tv),F(12,5)))]
                bm=[bernstein(mul(mass,m),pl,pu,9)for m in mom]
                for d in range(5):row.append(tuple(sum(F(comb(d,i))*bm[i][a]*shift[j,d-i][b]for i in range(d+1))for a in range(10)for b in range(5)))
            out.append(row)
        return out
    def raw_bounds(self,domain):
        k,pl,pu,ul,uh,lo,hi,*_=domain;vmin,vmax=variance_bounds(pl,pu)
        wl=vmin+lo/5;wh=vmax+self.effective_hi(pl,pu,hi)/5
        sl=wl*normal.root(wl)[0];sh=wh*normal.root(wh)[1]
        rl,rh=self.RHO,self.RHO_HI;gl,gh=self.GAMMA_LO,self.GAMMA_HI
        need(0<rl<=rh and gl<=gh and 0<sl<=sh,'original normalized moment domains')
        return rl*sl,rh*sh,min(gl*sl,gl*sh),max(gh*sl,gh*sh)
    def dual_tensors(self,domain):
        k,pl,pu,ul,uh,lo,hi,al,ah=_unpack(domain);rl,rh,gl,gh=self.raw_bounds(domain)
        poly,c0,c1=self.cell_corners(pl,pu,lo,hi,al,ah);out=[]
        for x,y in poly:
          for(g0,_),(g1,_)in product(c0,c1):
            raw=add(mul(V,add((F(1),),scale(V,-2))),add(add(scale(P,3*x),scale(Q,3*y)),(-g0*x+g1*y,)))
            signed=add(mul(V,(F(1),-F(2))),add(add(scale(P,-3*x),scale(Q,3*y)),(g0*x+g1*y,)))
            slacks=[add((rl,),scale(raw,-1)),add(raw,(-rh,)),add((gl,),scale(signed,-1)),add(signed,(-gh,))]
            out.append([tuple(z for z in bernstein(mul(V2,s),pl,pu,9)for _ in range(5))for s in slacks])
        return out
    def target_tensors(self,domain):
        k,pl,pu,ul,uh,lo,hi,al,ah=_unpack(domain)
        vmin,vmax=variance_bounds(pl,pu)
        M_curv,curv_rec=curvature(5,k,pl,pu,ul,uh,lo)
        poly,c0,c1=self.cell_corners(pl,pu,lo,hi,al,ah)
        wmax=vmax+(self.effective_hi(pl,pu,hi)/5 if(lo==0 and(al,ah)==(F(0),F(1)))else max(x+y for x,y in poly))
        c=normal.CE_LO/(normal.root(F(5))[1]*wmax*normal.root(wmax)[1]);lower=normal.CE_LO*self.RHO/normal.root(F(5))[1]
        targets=[];improvements=[]
        for x,y in poly:
            G,_=gaussian(5,k,pl,pu,ul,uh,5*(x+y))
            powers=[mul(V2,tuple(g))for g in G]+[(F(0),),(F(0),)]
            powers[0]=add(powers[0],scale(V2,lower))
            bp=[bernstein(g,pl,pu,9)for g in powers]
            target=tuple(z for i in range(10)for z in bernstein(tuple(bp[h][i]for h in range(5)),ul,uh,4))
            for(g0,_),(g1,_)in product(c0,c1):
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
        k,pl,pu,ul,uh,lo,hi,al,ah=_unpack(domain)
        rows=self.tensors(k,pl,pu,ul,uh,lo,hi,al,ah)if rows is None else rows
        targets,diffs,M_curv,curv_rec=self.target_tensors(domain);need(len(targets)==len(rows),'complete common vertex set')
        psd_mins=self.psd_check(parsed_qs,pl,pu,M_curv)
        use_prices=any(p>0 for p in prices)
        duals=self.dual_tensors(domain)if use_prices else None
        margin=None
        for idx,(row,rhs,diff)in enumerate(zip(rows,targets,diffs)):
            dual_row=duals[idx]if use_prices else None
            z=min(rhs[a]+theta*diff[a]+(sum(prices[i]*dual_row[i][a]for i in range(4))if use_prices else F(0))-sum(exact[d]*row[d][a]for d in range(30))for a in range(50))
            need(z>0,'strict complete-cell tensor inequality');margin=z if margin is None else min(margin,z)
        return dict(row_id=self.key,contract_sha256=self.contract_sha,k=k,p=list(map(str,(pl,pu))),u=list(map(str,(ul,uh))),
          noise=list(map(str,(lo,hi))),alpha=list(map(str,(al,ah))),
          theta=str(theta),prices=list(map(str,prices)),vertices=len(self.polygon(pl,pu,lo,hi,al,ah)),moment_pairs=4,global_rays=12,
          psd_coefficients=31,psd_minima=psd_mins,gaussian_noise_curvature_upper=str(M_curv),
          tensor_coefficients=50*len(rows),cleared_margin=str(margin),method='gaussian_taylor_both_halves_4pair_v1')

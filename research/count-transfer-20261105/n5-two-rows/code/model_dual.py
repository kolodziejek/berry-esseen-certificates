"""Original same-law rho/gamma constraints, with four exact nonnegative prices.

The baseline model is unchanged. Prices multiply necessary raw-moment
slacks; they do not change C_E or any acquired contract target.
"""
from model import *
import model as baseline
class Row(baseline.Row):
    def raw_bounds(self,domain):
        k,pl,pu,ul,uh,lo,hi=domain;vmin,vmax=variance_bounds(pl,pu)
        wl=vmin+lo/5;wh=vmax+self.effective_hi(pl,pu,hi)/5
        sl=wl*normal.root(wl)[0];sh=wh*normal.root(wh)[1]
        rl,rh=map(F,(self.cfg['rho_lower'],self.cfg['rho_upper']));gl,gh=map(F,self.cfg['acquired_gamma'])
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
    def admit(self,qs,theta,prices,domain,rows=None):
        theta=rational(theta);need(0<=theta<=1,'fixed convex rho weight')
        need(type(prices)is list and len(prices)==4,'four original moment prices')
        prices=list(map(rational,prices));need(min(prices)>=0,'nonnegative exact moment prices')
        need(type(qs)is list and len(qs)==6,'six common count polynomials');exact=[]
        for row in qs:
            need(type(row)is list and len(row)==5,'five quartic coefficients')
            q=list(map(rational,row));need(q[4]>0,'positive leading coefficient')
            sturm.positive(compact_ray(q,-1,F(1)));sturm.positive(compact_ray(q,1,F(0)));exact.extend(q)
        rows=self.tensors(*domain)if rows is None else rows
        targets,diffs,correlated=self.target_tensors(domain);duals=self.dual_tensors(domain)
        need(len(rows)==len(targets)==len(duals),'all common vertices and gamma pairs');margin=None
        for row,rhs,diff,dual in zip(rows,targets,diffs,duals):
            z=min(rhs[a]+theta*diff[a]+sum(prices[i]*dual[i][a]for i in range(4))-sum(exact[d]*row[d][a]for d in range(30))for a in range(50))
            need(z>0,'strict whole-cell priced tensor bound');margin=z if margin is None else min(margin,z)
        k,pl,pu,ul,uh,lo,hi=domain
        return dict(row_id=self.key,k=k,p=list(map(str,(pl,pu))),u=list(map(str,(ul,uh))),noise=list(map(str,(lo,hi))),theta=str(theta),prices=list(map(str,prices)),
          raw_moment_bounds=list(map(str,self.raw_bounds(domain))),vertices=len(self.polygon(pl,pu,lo,hi)),moment_pairs=9,global_rays=12,
          tensor_coefficients=50*len(rows),cleared_margin=str(margin),gaussian_noise_correlation=correlated)

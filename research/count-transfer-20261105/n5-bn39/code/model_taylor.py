"""Additive whole-cell Gaussian target; baseline moment/corner proof unchanged."""
import model as base
from model import *
from gaussian_scalar import gaussian

class Row(base.Row):
    def target_tensors(self,domain):
        k,pl,pu,ul,uh,lo,hi=domain;amin=F(k)+ul-5*pu;amax=F(k)+uh-5*pl
        vmin,vmax=variance_bounds(pl,pu)
        need(0<pl<pu<F(1,2)and amax<=0 and amin*amin<=15*vmin,'complete negative-Gaussian variance-concavity domain')
        hi=self.effective_hi(pl,pu,hi);wmax=vmax+hi/5
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
        return targets,improvements,True

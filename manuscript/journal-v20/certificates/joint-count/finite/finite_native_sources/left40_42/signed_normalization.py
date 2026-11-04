"""Exact global signed-Gaussian derivative application for TINY40.

Analytic premise: the local signed Gaussian lemma, with common global entropy
and mass constants returned by normalization.py. Hplus bounds positive H only.
"""
from fractions import Fraction as F
from normalization import _generate,normalization_gates,need

def generate(base,Hplus):
    c=_generate(base);g=normalization_gates(base,c)
    need(type(Hplus)is F and 0<=Hplus<=base['H'],'positive-H endpoint')
    N=c['N'];v=c['v'];D=c['delta'];Z=c['zeta'];h=Hplus/c['elo'];b=F(1,2)
    vertex=min(b,h);Gplus=max(F(0),2*h*vertex-vertex*vertex)
    eta=(b*b+2*h*b)/(2*v)+Z
    need(N*v>D*D and 0<eta<N,'global negative Gaussian domains')
    lower=1-((c['lmax']+Gplus)/(2*v)+Z)/N
    upper=1/(1-eta/N)
    need(0<lower and upper>0,'signed derivative positivity')
    c['derivative_lo']=max(c['derivative_lo'],lower)
    c['derivative_hi']=min(c['derivative_hi'],upper)
    c.update(signed_Hplus=Hplus,signed_hcap=h,signed_Gplus=Gplus,signed_eta=eta)
    g.update(signed_variance=str(N*v-D*D),signed_eta_denominator=str(N-eta),signed_derivative_lower=str(lower),signed_derivative_upper=str(upper))
    return c,g

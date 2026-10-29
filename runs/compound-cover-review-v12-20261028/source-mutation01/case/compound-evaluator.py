"""Exact outward quadratic-hinge bounds for two Poisson jump sizes.

All returned endpoints are fractions. The finite lower-complement identity
accounts for the entire Poisson tail. No floating point enters acceptance.
"""
from fractions import Fraction as F
from functools import lru_cache
import sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Optimization disables proof obligations')


def _fraction(x):
    if not isinstance(x,(int,F)) or isinstance(x,bool):
        raise TypeError('Exact integer or Fraction required')
    return F(x)


@lru_cache(maxsize=8192,typed=True)
def exp_bounds(x,order=24):
    """Enclose exp(x) using a finite Taylor sum and a geometric remainder."""
    x=_fraction(x)
    if not isinstance(order,int) or isinstance(order,bool) or order<1:
        raise ValueError('Positive integer Taylor order required')
    if x==0:return F(1),F(1)
    if x<0:
        lo,hi=exp_bounds(-x,order)
        return 1/hi,1/lo
    scale=0;y=x
    while y>1:y/=2;scale+=1
    term=F(1);lo=F(1)
    for j in range(1,order+1):
        term*=y/j;lo+=term
    first=term*y/(order+1)
    hi=lo+first/(1-y/(order+2))
    for _ in range(scale):lo*=lo;hi*=hi
    assert 0<lo<=hi
    return lo,hi


@lru_cache(maxsize=8192,typed=True)
def hinge_moment(mu,nu,K,large_step=25,small_step=3):
    """Enclose E[(large_step P_mu + small_step P_nu - K)_+^2]."""
    mu=_fraction(mu);nu=_fraction(nu);K=_fraction(K)
    if mu<0 or nu<0:raise ValueError('Poisson intensities must be nonnegative')
    if K<0:raise ValueError('A nonnegative rational hinge is required')
    if any(not isinstance(a,int) or isinstance(a,bool) or a<=0 for a in (large_step,small_step)):
        raise ValueError('Positive integer jump sizes required')
    jm=K//large_step;km=K//small_step
    pm=[F(1)];pn=[F(1)]
    for j in range(1,jm+1):pm.append(pm[-1]*mu/j)
    for k in range(1,km+1):pn.append(pn[-1]*nu/k)
    complement=F(0)
    for j in range(jm+1):
        for k in range((K-large_step*j)//small_step+1):
            gap=K-large_step*j-small_step*k
            complement+=gap*gap*pm[j]*pn[k]
    mean=large_step*mu+small_step*nu
    full=large_step**2*mu+small_step**2*nu+(mean-K)**2
    elo,ehi=exp_bounds(-mu-nu)
    lo=max(F(0),full-ehi*complement)
    hi=full-elo*complement
    assert 0<=lo<=hi
    return lo,hi


def tail_box(mu_lo,mu_hi,nu_lo,nu_hi,b_lo,K,unit=F(3,125),large_step=25,small_step=3):
    """Upper bound a centered compound-Poisson closed tail throughout a box.

    P(unit*(a(P_mu-mu)+c(P_nu-nu)) >= b) is bounded for all box
    intensities and every b>=b_lo. K stays fixed on the complete box.
    """
    mu_lo,mu_hi,nu_lo,nu_hi,b_lo,unit=map(_fraction,(mu_lo,mu_hi,nu_lo,nu_hi,b_lo,unit))
    if not (0<=mu_lo<=mu_hi and 0<=nu_lo<=nu_hi and b_lo>0 and unit>0):
        raise ValueError('Ordered nonnegative intensities and positive threshold/unit required')
    denominator=b_lo/unit+large_step*mu_lo+small_step*nu_lo-K
    if denominator<=0:raise ValueError('Hinge not admissible throughout the closed box')
    _,numerator=hinge_moment(mu_hi,nu_hi,K,large_step,small_step)
    return min(F(1),numerator/denominator**2)


def centered_tail(total_variance_hi,small_allocation_lo,b_lo,y,
                  unit=F(3,125),large_step=25,small_step=3):
    """Closed-tail bound from monotonicity of the centered quadratic hinge.

    Requires actual comparator total variance <=total_variance_hi and
    its fraction assigned to the smaller jump >=small_allocation_lo.
    The physical hinge y is fixed; it must satisfy 0<=y<b_lo.
    Monotonicity is an analytic obligation stated in compound-proof.tex.
    """
    T,w,b,y,unit=map(_fraction,(total_variance_hi,small_allocation_lo,b_lo,y,unit))
    if not (T>=0 and 0<=w<=1 and 0<=y<b and unit>0):
        raise ValueError('Invalid centered-hinge domain')
    if not (isinstance(large_step,int) and isinstance(small_step,int)
            and 0<small_step<=large_step):
        raise ValueError('Ordered positive integer jump sizes required')
    A=unit*large_step;d=unit*small_step
    mu=T*(1-w)/A**2;nu=T*w/d**2
    K=y/unit+large_step*mu+small_step*nu
    _,upper=hinge_moment(mu,nu,K,large_step,small_step)
    return min(F(1),unit**2*upper/(b-y)**2)


def infinite_incoming_tail(lam_hi,r_lo,first=4,A=F(3,5)):
    """Sum i>=first using variance<=5lambda/2 and integer Poisson hinges."""
    from math import factorial
    lam,r,A=map(_fraction,(lam_hi,r_lo,A))
    if not (lam>=0 and r>=0 and 0<A<1 and isinstance(first,int) and first>=2):
        raise ValueError('Invalid factorial-tail domain')
    mu=F(5,2)*lam/A**2
    if mu>=first+2:raise ValueError('Geometric factorial ratio not below one')
    denominator=first*(1/A-1)+r/A+mu
    assert denominator>0
    return mu**(first+1)/(factorial(first+1)*denominator**2*(1-mu/(first+2)))


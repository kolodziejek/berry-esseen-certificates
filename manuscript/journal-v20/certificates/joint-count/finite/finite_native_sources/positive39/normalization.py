"""Checked finite-binomial constants for TINY42, with no discovery imports.

For n=39, p in the supplied closed subinterval of (0,1/2),
|H|<=Hmax, theta<=Theta, d<=d0, and lambda<=maxnoise, every generated
constant is checked by exact rational gates before it is returned.
The caller must acquire those input hypotheses separately.
"""
from fractions import Fraction as F
from math import isqrt
import sys

if sys.flags.optimize or not __debug__:
    raise RuntimeError('Unoptimized Python required')

def need(ok, message):
    if not ok:
        raise ValueError(message)

def rootlo(q):
    need(q > 0, 'positive square-root argument')
    return F(isqrt(q.numerator*10**12//q.denominator)-1,10**6)

def rootup(q):
    need(q > 0, 'positive square-root argument')
    return F(isqrt(q.numerator*10**12//q.denominator)+1,10**6)

def up(x):
    return F(-((-x.numerator*100000)//x.denominator)+1,100000)

def down(x):
    return F((x.numerator*100000)//x.denominator-1,100000)

def _domain(base):
    need(type(base) is dict and type(base.get('N')) is int and base['N']==39, 'fixed single index39')
    for key in ('pl','pu','theta','H','d0','amplitude','maxnoise','Ccap'):
        need(type(base.get(key)) is F, 'exact rational input '+key)
    need(F('.4')<=base['Ccap']<=F('.45'),'explicit hypothetical upper score premise')
    need(0<base['pl']<base['pu']<F(1,2), 'probability below one half')
    need(0<=base['theta']<1 and base['H']>=0, 'variance and phase scope')
    need(0<=base['d0']<base['pl'], 'inward gap scope')
    need(0<base['maxnoise'] and 0<base['amplitude'] and base['amplitude']+base['d0']<F(1,2), 'noise and span scope')

def _generate(base):
    _domain(base)
    c=dict(base);N=c['N'];c['lmax']=c['maxnoise'];lm=c['lmax'];c['tiny']=F('.026')
    c['elo']=rootlo((1-c['theta'])/(c['pu']*(1-c['pu'])))
    need(c['elo']>0,'positive outward span lower bound')
    c['delta']=up(max(F(1),c['H']/c['elo']+F(1,2)));d=c['delta']
    c['v']=down(c['pl']*(1-c['pl']));v=c['v']
    c['left']=down(c['pl']-d/N);c['right']=up(c['pu']+d/N)
    c['vf']=down(c['left']*(1-c['left']))
    need(v>0 and c['vf']>0 and 0<c['left']<F(1,2) and c['left']<c['right']<1 and c['left']+c['right']<1,'finite entropy segment')
    c['entropy']=up((1-2*c['left'])/c['vf']**2)
    c['logder']=up((1-2*c['left'])/c['vf'])
    c['remainder']=up(1/(12*c['vf']))
    c['zeta']=up(c['logder']*d/2+c['remainder']+c['entropy']*d**3/(6*N))
    c['sqrtmass']=rootup(c['pu']*(1-c['pu']))
    c['mass']=down(F('.39886')/c['sqrtmass']*(1-(d*d/(2*v)+c['zeta'])/N))
    c['logcoef']=up(1/(2*v)+d*d/(2*N*v*v))
    phase=(d+F(1,4))/(2*v)+c['zeta']
    c['logcap']=up((c['logcoef']*lm+phase)/N)
    need(0<c['logcap']<1,'exponential multiplier denominator')
    c['ef']=1/(1-c['logcap'])
    c['normal_v']=up(c['ef']*c['logcoef']);c['normal_c']=up(c['ef']*phase)
    c['derivative_lo']=down(1-(c['normal_v']*lm+c['normal_c'])/N)
    c['derivative_hi']=up(1+(c['normal_v']*lm+c['normal_c'])/N)
    c['cv']=up(1/c['pl']);c['ownlo']=down(1-c['cv']*d/N);c['ownhi']=up(1+c['cv']*d/N)
    c['incoming']=up(1+c['cv']*(d+1)/N);c['outer']=up(1+c['cv']*(d+F(1,2))/N)
    den=1-(d-1)/(N*c['pl']);need(den>0,'incoming count ratio denominator')
    c['ratio']=up(1+(c['pu']+d-1)/(N*v*den))
    vmax=c['pu']*(1-c['pu'])+lm/N
    c['repair_multiplier']=down(F('.4')/rootup(vmax**3))
    c['repair_pos']=up(F('.4')/(2*rootlo(v**3)))
    raw=6*c['pl']-3*c['pl']**2-F(3,2)-c['d0']-3*(1-2*v)*lm/(8*v*N)
    c['repair_multiplier_upper']=up(c['Ccap']/rootlo(v**3))
    c['cubic_gain']=min(c['repair_multiplier']*raw,c['repair_multiplier_upper']*raw)
    c['repair']=max(F(0),up(c['repair_pos']*d-c['cubic_gain']))
    c['span']=c['amplitude']+c['d0'];x=F('3.14159')*c['span']
    sinlo=x-x**3/6+x**5/120-x**7/5040
    c['rate']=down(2*sinlo*sinlo/c['span']**2)
    return c

def normalization_gates(base,c):
    """Re-derive all output inequalities; changed hypotheses reject."""
    _domain(base)
    for key,value in base.items():
        need(key in c and c[key]==value, 'changed input hypothesis '+key)
    N=base['N'];v=c['v'];d=c['delta'];lm=c['lmax'];g={}
    need(c['repair']>=0,'nonnegative repair before the all-index replacement')
    def pos(name,x):
        x=F(x);need(name not in g,'duplicate gate '+name);need(x>0,('nonpositive normalization gate',name,str(x)));g[name]=str(x)
    need(lm==base['maxnoise'],'same all-index noise ceiling')
    need(c['tiny']==F('.026'),'fixed tiny/LOW seam marker')
    def atan(x):
        a=sum((-1)**j*x**(2*j+1)/(2*j+1)for j in range(20));return a,a+x**41/41
    a,b=atan(F(1,5)),atan(F(1,239));pil=16*a[0]-4*b[1];pih=16*a[1]-4*b[0]
    need((F(120,119)-F(1,239))/(1+F(120,119)/239)==1,'Machin tangent identity')
    pos('Machin_positive_angle',4*(F(1,5)-F(1,375))-F(1,239));pos('Machin_branch',1-F(4,5))
    pos('pi_lower',pil-F('3.14159'));pos('pi_upper',F(22,7)-pih)
    pos('normal_lower',1-2*pih*F('.39886')**2);pos('normal_upper',2*pil*F('.4')**2-1)
    pos('ell_positive',c['elo']);pos('ell_lower',1-c['theta']-c['elo']**2*c['pu']*(1-c['pu']))
    pos('delta_phase',d-c['H']/c['elo']-F(1,2));pos('mode_covered',d-1)
    pos('actual_variance',c['pl']*(1-c['pl'])-v);pos('variance_positive',v)
    pos('segment_left',c['pl']-d/N-c['left']);pos('segment_right',c['right']-c['pu']-d/N)
    pos('segment_positive',c['left']);pos('segment_below_one',1-c['right']);pos('segment_left_farthest',1-c['left']-c['right'])
    pos('segment_variance',c['left']*(1-c['left'])-c['vf']);pos('segment_variance_positive',c['vf'])
    pos('count_positive',N*c['pl']-d-2);pos('count_below_n',N*(1-c['pu'])-d-2)
    pos('entropy_third',c['entropy']-(1-2*c['left'])/c['vf']**2)
    pos('log_variance_derivative',c['logder']-(1-2*c['left'])/c['vf'])
    pos('factorial_error',c['remainder']-1/(12*c['vf']))
    zeta=c['logder']*d/2+c['remainder']+c['entropy']*d**3/(6*N)
    pos('zeta_ceiling',c['zeta']-zeta);pos('sqrt_pq',c['sqrtmass']**2-c['pu']*(1-c['pu']));pos('sqrt_pq_positive',c['sqrtmass'])
    pos('mass_positive',c['mass'])
    pos('mass_lower',F('.39886')/c['sqrtmass']*(1-(d*d/(2*v)+c['zeta'])/N)-c['mass'])
    pos('mass_upper_exponential_domain',1-c['zeta']/N)
    pos('mass_upper',v*(1-c['zeta']/N)**2-F('.4')**2)
    phase=(d+F(1,4))/(2*v)+c['zeta']
    pos('log_variance',c['logcoef']-1/(2*v)-d*d/(2*N*v*v))
    pos('log_ceiling',c['logcap']-(c['logcoef']*lm+phase)/N)
    pos('logcap_positive',c['logcap']);pos('exponential_denominator',1-c['logcap'])
    need(c['ef']==1/(1-c['logcap']),'exact exponential multiplier')
    pos('normal_variance',c['normal_v']-c['ef']*c['logcoef']);pos('normal_phase',c['normal_c']-c['ef']*phase)
    pos('derivative_positive',c['derivative_lo'])
    pos('derivative_error_lower',1-c['derivative_lo']-(c['normal_v']*lm+c['normal_c'])/N)
    pos('derivative_error_upper',c['derivative_hi']-1-(c['normal_v']*lm+c['normal_c'])/N)
    pos('variance_coefficient',c['cv']*c['pl']-1)
    pos('own_variance_positive',c['ownlo'])
    pos('own_variance_upper',c['ownhi']-1-c['cv']*d/N);pos('own_variance_lower',1-c['ownlo']-c['cv']*d/N)
    pos('incoming_variance',c['incoming']-1-c['cv']*(d+1)/N)
    pos('outer_variance',c['outer']-1-c['cv']*(d+F(1,2))/N)
    denominator=1-(d-1)/(N*c['pl']);pos('rising_denominator',denominator)
    pos('rising_ratio',c['ratio']-1-(c['pu']+d-1)/(N*v*denominator));pos('rising_all_later',2-c['pu']-d)
    vmax=c['pu']*(1-c['pu'])+lm/N
    pos('repair_multiplier_positive',c['repair_multiplier'])
    pos('cubic_multiplier',F('.4')**2-c['repair_multiplier']**2*vmax**3)
    pos('normal_repair_positive',c['repair_pos']);pos('normal_repair',4*c['repair_pos']**2*v**3-F('.4')**2)
    raw=6*c['pl']-3*c['pl']**2-F(3,2)-c['d0']-3*(1-2*v)*lm/(8*v*N)
    pos('upper_cubic_multiplier_positive',c['repair_multiplier_upper'])
    pos('upper_cubic_multiplier',c['repair_multiplier_upper']**2*v**3-c['Ccap']**2)
    need(c['cubic_gain']==min(c['repair_multiplier']*raw,c['repair_multiplier_upper']*raw),'piecewise signed cubic gain')
    pos('global_repair',c['repair']-c['repair_pos']*d+c['cubic_gain'])
    need(c['span']==c['amplitude']+c['d0'],'actual conditional support span')
    span=c['span'];pos('span_positive',span);pos('span_below_half',F(1,2)-span)
    x=F('3.14159')*span;sinlo=x-x**3/6+x**5/120-x**7/5040
    pos('sine_lower_positive',sinlo);pos('alternating_sine_domain',6-x*x)
    pos('rate_positive',c['rate']);pos('harmonic_rate',2*sinlo*sinlo-c['rate']*span*span)
    return g

def generate_checked(base):
    c=_generate(base)
    normalization_gates(base,c)
    return c

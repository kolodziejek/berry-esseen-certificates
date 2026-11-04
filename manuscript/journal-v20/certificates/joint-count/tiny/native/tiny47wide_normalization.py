"""Fixed finite-binomial normalization for CONDITIONAL_TINY47_WIDE_A.
Scope: n>=47,p in[.304,.47],|H|<=1.393,theta<=.0154,d<=.0181,
|U|<=.425,0<lambda<=.05. Acquisition is separate.
"""
from fractions import Fraction as F
from math import factorial
import sys
if sys.flags.optimize or not __debug__:raise RuntimeError('Unoptimized Python required')
CFG={'H':F('1393/1000'),'N':47,'amplitude':F('17/40'),'cv':F('328949/100000'),'d0':F('181/10000'),'delta':F('30017/25000'),'derivative_hi':F('112901/100000'),'derivative_lo':F('87099/100000'),'ef':F('100000/88573'),'elo':F('1988121/1000000'),'entropy':F('548949/50000'),'incoming':F('28851/25000'),'left':F('6961/25000'),'lmax':F('1/20'),'logcap':F('11427/100000'),'logcoef':F('8456/3125'),'logder':F('220569/100000'),'mass':F('1421/2000'),'normal_c':F('147753/25000'),'normal_v':F('305503/100000'),'outer':F('3497/3125'),'ownhi':F('21681/20000'),'ownlo':F('18319/20000'),'pl':F('38/125'),'pu':F('47/100'),'ratio':F('53421/50000'),'remainder':F('20741/50000'),'repair':F('59489/25000'),'repair_multiplier':F('79921/25000'),'repair_pos':F('102761/50000'),'right':F('12389/25000'),'sqrtmass':F('4991/10000'),'theta':F('77/5000'),'v':F('21157/100000'),'vf':F('2009/10000'),'zeta':F('180639/100000')}

def check():
 c=CFG;N=c['N'];v=c['v'];delta=c['delta'];lm=c['lmax'];g={}
 def pos(k,x):
  x=F(x)
  if not x>0:raise ValueError('nonpositive gate '+k+': '+str(x))
  if k in g:raise ValueError('duplicate gate')
  g[k]=str(x)
 def atan(x):
  a=sum((-1)**j*x**(2*j+1)/(2*j+1)for j in range(20));return a,a+x**41/41
 a,b=atan(F(1,5)),atan(F(1,239));pil=16*a[0]-4*b[1];pih=16*a[1]-4*b[0]
 if not (F(120,119)-F(1,239))/(1+F(120,119)/239)==1:raise ValueError('Machin identity')
 pos('Machin_positive_angle',4*(F(1,5)-F(1,375))-F(1,239));pos('Machin_branch',1-F(4,5))
 pos('pi_lower',pil-F('3.14159'));pos('pi_upper',F(22,7)-pih)
 pos('normal_lower',1-2*pih*F('.39886')**2);pos('normal_upper',2*pil*F('.4')**2-1)
 pos('ell_lower',1-c['theta']-c['elo']**2*c['pu']*(1-c['pu']))
 pos('delta',delta-c['H']/c['elo']-F('.5'))
 pos('actual_variance',c['pl']*(1-c['pl'])-v)
 pos('segment_left',c['pl']-delta/N-c['left']);pos('segment_right',c['right']-c['pu']-delta/N)
 pos('segment_below_half',F('.5')-c['right']);pos('segment_variance',c['left']*(1-c['left'])-c['vf'])
 pos('count_positive',N*c['pl']-delta-2);pos('count_below_n',N*(1-c['pu'])-delta-2)
 pos('entropy_third',c['entropy']-(1-2*c['left'])/c['vf']**2)
 pos('log_variance_derivative',c['logder']-(1-2*c['left'])/c['vf']);pos('factorial_error',c['remainder']-1/(12*c['vf']))
 zeta=c['logder']*delta/2+c['remainder']+c['entropy']*delta**3/(6*N)
 pos('zeta_ceiling',c['zeta']-zeta);pos('sqrt_pq',c['sqrtmass']**2-c['pu']*(1-c['pu']))
 pos('mass_lower',F('.39886')/c['sqrtmass']*(1-(delta**2/(2*v)+c['zeta'])/N)-c['mass'])
 pos('mass_upper',v*(1-c['zeta']/N)**2-F('.4')**2);pos('mode_covered',delta-1)
 phase=(delta+F('.25'))/(2*v)+c['zeta']
 pos('log_variance',c['logcoef']-1/(2*v)-delta**2/(2*N*v*v))
 pos('log_ceiling',c['logcap']-(c['logcoef']*lm+phase)/N)
 if c['ef'] !=1/(1-c['logcap']):raise ValueError('exact exponential multiplier')
 pos('normal_variance',c['normal_v']-c['ef']*c['logcoef']);pos('normal_phase',c['normal_c']-c['ef']*phase)
 pos('derivative_error_lower',1-c['derivative_lo']-(c['normal_v']*lm+c['normal_c'])/N)
 pos('derivative_error_upper',c['derivative_hi']-1-(c['normal_v']*lm+c['normal_c'])/N)
 pos('variance_coefficient',c['cv']*c['pl']-1)
 pos('own_variance_upper',c['ownhi']-1-c['cv']*delta/N);pos('own_variance_lower',1-c['ownlo']-c['cv']*delta/N)
 pos('incoming_variance',c['incoming']-1-c['cv']*(delta+1)/N)
 pos('outer_variance',c['outer']-1-c['cv']*(delta+F('.5'))/N)
 denominator=1-(delta-1)/(N*c['pl']);pos('rising_denominator',denominator)
 pos('rising_ratio',c['ratio']-1-(c['pu']+delta-1)/(N*v*denominator))
 pos('rising_all_later',2-c['pu']-delta)
 vmax=c['pu']*(1-c['pu'])+lm/N
 pos('cubic_multiplier',F('.4')**2-c['repair_multiplier']**2*vmax**3)
 pos('normal_repair',4*c['repair_pos']**2*v**3-F('.4')**2)
 raw=6*c['pl']-3*c['pl']**2-F('1.5')-c['d0']-3*(1-2*v)*lm/(8*v*N)
 pos('cubic_raw',raw);pos('global_repair',c['repair']-c['repair_pos']*delta+c['repair_multiplier']*raw)
 return g

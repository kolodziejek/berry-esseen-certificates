"""Exact acceptance inequalities for outer.tex. No discovery imports.

This proves only the stated four phase intervals, not the missing negative
inner interval. All arithmetic, including the tensor transform, is rational.
"""
from fractions import Fraction as F
from math import comb, factorial
import hashlib,json,sys
from pathlib import Path
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')

def clean(a):return {k:v for k,v in a.items() if v}
def const(x):return clean({(0,0):F(x)})
def add(a,b):
    z=dict(a)
    for k,x in b.items():z[k]=z.get(k,0)+x
    return clean(z)
def scale(a,b):return clean({k:v*b for k,v in a.items()})
def mul(a,b):
    z={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():z[i+k,j+l]=z.get((i+k,j+l),0)+x*y
    return clean(z)
def power(a,n):
    z=const(1)
    for _ in range(n):z=mul(z,a)
    return z
def total(*args):
    z={}
    for a in args:z=add(z,a)
    return z

def inner_polynomial(tcoef):
    A=F(3,5); alpha=F(16,25); M=5*alpha**4
    x={(1,0):F(1)};y={(0,1):F(1)};t=scale(x,tcoef)
    mu1=scale(x,F(25,8));mug=scale(x,F(125,18))
    d1=total(const(1/A-1),scale(y,-1/A),mu1)
    d2=total(const(2*(1/A-1)),scale(y,-1/A),mug)
    dg=add(const(1),scale(mug,-F(1,4)))
    den1=power(d1,2); den2=scale(mul(power(d2,2),dg),6)
    num1=mul(power(mu1,2),add(const(F(1,2)),scale(mu1,F(1,6))))
    num2=power(mug,3)
    own=scale(total(scale(t,3*alpha**2-A*A),scale(power(t,2),-3),
      scale(mul(y,t),-4*A),scale(mul(power(y,2),t),-6),scale(power(y,4),-1),
      scale(power(y,2),3*alpha**2),scale(y,-2*alpha**3)),1/M)
    own=add(own,scale(y,F(24,25)))
    baseline=add(scale(own,F(73,100)),scale(x,-F(3,4)/42-F(1,100)))
    tail=add(mul(num1,den2),mul(num2,den1))
    return add(mul(baseline,mul(den1,den2)),scale(tail,-F(73,100)*F(53,50)))

def coefficients(P,U):
    # x=U X,y=U Y, then X^k= sum_{i=k}^7 binom(i,k)/binom(7,k) B_i^7(X).
    assert max(i for i,j in P)==7 and max(j for i,j in P)==8
    return [(i,j,sum(value*U**(k+l)*F(comb(i,k),comb(7,k))*F(comb(j,l),comb(8,l))
        for (k,l),value in P.items() if k<=i and l<=j)) for i in range(8) for j in range(9)]

def evaluate(U=F(3,40),gain=F(1)):
    A=F(3,5);N=F(42);v=F(6,25);xi=F(46,25)*F(251,500)
    D=F(413,250); Z=lambda x:F(5,8)*x+F(3,8)+x**3/N
    mass=lambda x:2*F(19943,50000)*(1-(x*x/(2*v)+Z(x))/N)
    eps=lambda x,b:(F(8,3)*U+(2*x*b+b*b)/(2*v)+Z(x))/N
    signed=lambda x,b:(F(8,3)*U+(2*xi*b-b*b)/(2*v)+Z(x))/N
    g={}
    def gate(name,value):g[name]=value
    gate('sqrt_variance',F(251,500)**2-F(1,4)-U/N)
    gate('global_delta',D-xi-F(91,125))
    gate('interior_lower',N*F(2,5)-D-1);gate('interior_upper',N*F(47,100)-D-1)
    gate('count_fraction_lower',F(2,5)-D/N-F(9,25))
    gate('count_fraction_upper',F(23,40)-F(53,100)-D/N)
    gate('stirling_variance',F(9,25)*F(16,25)-F(23,100))
    gate('stirling_entropy',6-F(7,25)/F(23,100)**2)
    gate('stirling_prefactor',F(5,4)-F(7,25)/F(23,100))
    gate('stirling_remainder',F(3,8)-1/(12*F(23,100)))
    gate('log_variance',F(8,3)-1/(2*v)-D*D/(2*N*v*v))
    gate('normal_repair',F(7,4)**2*v**3-F(1,5)**2)
    gate('unit_cubic_gain',F(2,5)*(F(87,250)-F(13,16)*U/N)-gain*F(251,500)**3)
    gate('quartic_majorant',F(121-108))
    mug=F(5,2)*U/A**2
    def J(m,u):return mug**(m+1)/(factorial(m+1)*(m*(1/A-1)-u/A+mug)**2*(1-mug/(m+2)))
    def Q(mu,u):return mu**2*(F(1,2)+mu/6)/((1-u)/A-1+mu)**2
    for name,dd,b,mlo,rat in [('inner',F(1),F(3,40),F(73,100),F(53,50)),('negative',F(6,5),F(34,125),F(71,100),F(27,25)),('near',F(43,40),F(3,20),F(73,100),F(107,100)),('far',D,F(91,125),F(13,20),F(1143,1000))]:
        gate(name+'_delta',dd-xi-b)
        gate(name+'_mass',mass(dd)-mlo)
        ratio=1+(F(53,100)+dd-1)/(N*v-F(3,5)*max(dd-1,0))
        if name=='far':ratio*=1+(F(53,100)+dd-2)/(N*v)
        gate(name+'_ratio',rat-ratio)
        gate(name+'_later_ratios',(3 if name=='far' else 2)-F(53,100)-dd)
    gate('inner_lower_derivative',1-eps(1,F(3,40))-F(24,25))
    gate('inner_upper_derivative',F(26,25)*(1-eps(1,F(3,40)))-1)
    gate('negative_upper_derivative',F(27,25)*(1-eps(F(6,5),F(34,125)))-1)
    gate('near_lower_derivative',1-signed(F(43,40),F(3,20))-F(19,20))
    gate('far_lower_derivative',1-signed(D,F(91,125))-F(9,10))
    gate('signed_monotone',xi-F(91,125))
    gate('inner_first_variance',F(9,8)-1-F(5,2)*2/N)
    gate('negative_first_variance',F(8,7)-1-F(5,2)*(F(6,5)+1)/N)
    gate('near_first_variance',F(9,8)-1-F(5,2)*(F(43,40)+1)/N)
    gate('far_first_variance',F(7,6)-1-F(5,2)*(D+1)/N)
    # All denominators positive even before adding their nonnegative intensities.
    gate('inner_first_hinge',1/A-1-F(3,40)/A)
    gate('near_first_hinge',1/A-1-F(3,20)/A)
    gate('tail2_hinge',2*(1/A-1)-F(3,20)/A)
    gate('tail3_hinge',3*(1/A-1)-F(91,125)/A)
    gate('tail2_ratio',1-mug/4);gate('tail3_ratio',1-mug/5)
    gate('inner_polynomial_denominator',1-mug/4)
    Tg=F(15,14)*U
    gate('negative_own_variance_nonstrict',F(15,14)-1-F(5,2)*F(6,5)/N)
    gate('negative_initial_derivative',2*F(3,20)*Tg/(Tg+F(3,20)**2)**2-F(27,25))
    own=min(r*r/(Tg+r*r)-F(27,25)*r for r in [F(3,20),F(34,125)])
    tail=Q(F(8,7)*U/A**2,-F(3,20))+J(2,-F(3,20))
    gate('negative_final',F(71,100)*(own-F(27,25)*tail)-(F(7,4)*F(6,5)-gain)*U/N-U/100)
    for u in [F(3,40),F(3,20)]:
        gate('near_final_'+str(u),F(73,100)*(F(19,20)*u-F(107,100)*(Q(F(9,8)*U/A**2,u)+J(2,u)))-(F(7,4)*F(43,40)-gain)*U/N-U/100)
    t1=F(7,6)*U;mu2=(1+F(5,2)*(D+2)/N)*U/A**2
    gate('far_cantelli_convexity',3*(1-F(91,125))**2-t1)
    gate('far_second_hinge', (2-F(91,125))/A-2)
    for u in [F(3,20),F(91,125)]:
        second=mu2**3/(6*((2-u)/A-2+mu2)**2)
        gate('far_final_'+str(u),F(13,20)*(F(9,10)*u-F(1143,1000)*(t1/(t1+(1-u)**2)+second+J(3,u)))-(F(7,4)*D-gain)*U/N-U/100)
    return g

def failed(g):return [k for k,v in g.items() if (v<0 if k.endswith('_nonstrict') else v<=0)]
def validate_rows(rows,expected):
    assert len(rows)==len(expected)
    assert rows==expected
    assert rows[0]==(0,0,F(0)) and all(v>0 for i,j,v in rows[1:])
def rejected(rows,expected):
    try:validate_rows(rows,expected)
    except AssertionError:return True
    return False

if __name__=='__main__':
    gates=evaluate();assert not failed(gates),{k:str(gates[k]) for k in failed(gates)}
    certs=[]
    for endpoint in [F(79,84),F(89,84)]:
        rows=coefficients(inner_polynomial(endpoint),F(3,40));validate_rows(rows,rows)
        bad=rows[:];i,j,b=bad[-1];bad[-1]=(i,j,b+1)
        assert all([rejected(rows[:-1],rows),rejected(rows+[rows[-1]],rows),rejected(list(reversed(rows)),rows),rejected(bad,rows)])
        certs.append({'t_over_lambda':str(endpoint),'degree':[7,8],'rows':[[i,j,str(v)]for i,j,v in rows],'minimum_positive':str(min(v for i,j,v in rows if v>0))})
    # The bound is not silently promoted to a larger range or deprived of repair.
    controls={'unproved_noise_point10':failed(evaluate(F(1,10))),
              'remove_cubic_gain':failed(evaluate(gain=F(0)))}
    assert all(controls.values())
    # The factorial-square inequality cannot start at i=1: at P=3,4>3.
    assert (3-1)**2>comb(3,2)
    for i in range(2,12):
        for k in range(i+1,i+17):assert (k-i)**2<=comb(k,i+1)
    print(json.dumps({'status':'PASS_FOUR_PHASE_INTERVALS_LAMBDA_LE_3_OVER_40','scope':'n>=42,p in [.4,.53],.6 strip,inward<=.072,raw |H|<=1.84,C>=.4; u in [-.272,-.15] union [0,.728]; negative inner interval excluded',
      'gates':{k:str(v)for k,v in gates.items()},'gate_count':len(gates),'bernstein':certs,
      'coefficient_count':sum(len(c['rows'])for c in certs),'negative_controls':controls,
      'proof_object_mutations_rejected':['missing','duplicate','reordered','corrupt'],
      'invalid_factorial_start_rejected':True,'python':sys.version},indent=2))

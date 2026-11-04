"""Fixed exact obligations for the NEW CONDITIONAL_TINY47_WIDE_A theorem.

The analytic innovations are the shifted fourth-moment sign majorant and
the cubic centered-Poisson comparison; this code does not prove those steps.
"""
from fractions import Fraction as F
from math import factorial,isqrt
import sys
from tiny47wide_normalization import CFG,check as normalization
if sys.flags.optimize:raise RuntimeError('Unoptimized Python required')
def need(b,s):
 if not b:raise ValueError(s)
def rootlo(x):return F(isqrt(x.numerator*10**16//x.denominator),10**8)
def rootup(x):return rootlo(x)+F(1,10**8)
def ceiling(x):return F(-((-x.numerator*10**12)//x.denominator),10**12)
def poisson_cubic(mu,anchor,threshold):
 need(mu>0 and threshold>anchor>=0,'Poisson cubic domain')
 last=32;need(last>anchor+2,'Poisson truncation position')
 finite=sum(mu**k/F(factorial(k))*max(F(0),F(k)-anchor)**3 for k in range(last+1))
 first=mu**(last+1)/F(factorial(last+1))*(last+1-anchor)**3
 ratio=mu/F(last+2)*((last+2-anchor)/(last+1-anchor))**3
 need(0<ratio<1,'Poisson geometric tail')
 exp_lower=sum(mu**k/F(factorial(k))for k in range(25))
 return ceiling((finite+first/(1-ratio))/exp_lower/(threshold-anchor)**3)
def bennett(a,V,b):
 x=1+a*b/V;need(x>1,'Bennett logarithm domain');power=0
 while x>=2:x/=2;power+=1
 def log2atanh(y):return 2*sum(y**(2*j+1)/(2*j+1)for j in range(20))
 lo=power*log2atanh(F(1,3))+log2atanh((x-1)/(x+1))
 exponent=(b/a+V/(a*a))*lo-b/a
 need(0<exponent<16,'Bennett exponent domain')
 return ceiling(1/(sum((exponent/16)**j/F(factorial(j))for j in range(17))**16))
def log_upper(x):
 need(x>=1,'log upper domain');power=0
 while x>=2:x/=2;power+=1
 def bound(y):
  return 2*sum(y**(2*j+1)/(2*j+1)for j in range(20))+2*y**41/(41*(1-y*y))
 return power*bound(F(1,3))+bound((x-1)/(x+1))
def quadratic_min(a,b,c,z):
    need(z>0,'quadratic interval')
    vals=[a,a+b*z+c*z*z]
    if c>0:
        v=max(F(0),min(z,-b/(2*c)));vals.append(a+b*v+c*v*v)
    return min(vals)
def evaluate():
    c=CFG;g={k:F(v)for k,v in normalization().items()};rows=[]
    def put(k,x):
        need(k not in g,'duplicate gate');g[k]=F(x)
    N=c['N'];L=c['lmax'];A=c['amplitude'];t=c['ownhi']*L;lo=c['derivative_lo'];hi=c['derivative_hi']
    K=F(9)/(4*F('.4641'));a=F('.4784');den=K*a**4
    put('quartic_maximum',((K-F(9,4))*F(2,3))**2-3)
    put('quartic_maximum_branch',K-F(9,4))
    def near(sign,normal,z,name):
        c0=(3*a*a-A*A)/den;linear0=2*sign/(K*a)+normal
        v0=min(c0,c0+linear0*z)
        cm=(3*a*a-A*A-3*t)/den;linear=linear0-4*A*t/den
        q=(3*a*a*t-6*t*t-t**3*z*z)/den
        put('near_quadratic:'+name,q)
        return min(v0,quadratic_min(cm,linear,q,z))
    zn=F('1.66');zp=F('1.2');neg=F('.514');positive=F('1.036')
    put('negative_split',F('.5')-zn*t);put('positive_split',F('.5')-zp*t)
    put('negative_near',near(1,-hi,zn,'negative')-neg)
    put('negative_far',zn*zn/(1+zn*zn*t)-hi*zn-neg)
    put('negative_far_derivative',2*zn/(1+zn*zn*t)**2-hi)
    put('negative_endpoint',1/(1+4*t)-hi/2-neg*t)
    put('positive_near',near(-1,lo,zp,'positive')-positive)
    put('positive_far',lo*zp-positive)
    V=c['incoming']*L;mu=V/(A*A)
    specs=[('negative',F(1),F(1),F('1.25'),neg*c['ownlo'],True),
           ('positive0',F('.9'),F('.95'),F('1'),positive*c['ownlo'],True)]
    specs.extend(('positive'+str(i),1-F(i+1,10),1-F(i+1,20),F(anchor),lo*F(i,10)/L,False)for i,anchor in enumerate(('1','0','0','1'),1))
    for name,b,bout,anchor,own,scaled in specs:
        threshold=b/A+mu;first=poisson_cubic(mu,anchor,threshold)
        if not scaled:first=min(first,V/(V+b*b),bennett(A,V,b))
        outer=bennett(A,V,bout);put('outer_subunit:'+name,1-outer)
        if scaled:
            put('anchor_before_threshold:'+name,b/A-anchor)
            first_k=anchor.numerator//anchor.denominator+1
            put('first_scaled_monotone:'+name,first_k-1-mu-3*mu/(threshold-anchor))
            put('outer_scaled_monotone:'+name,bout/A-mu*log_upper(1+A*bout/V)-F('.5'))
        tails=first+outer*outer/(1-outer);bracket=own-c['ratio']*tails/L
        put('positive_bracket:'+name,bracket)
        reserve=c['mass']*bracket-c['repair']/N;put('strict_comparison:'+name,reserve-F('.001'))
        rows.append(dict(name=name,first=str(first),outer=str(outer),anchor=str(anchor),reserve=str(reserve)))
    return dict(schema='CONDITIONAL_TINY47_WIDE_A_V1',contract={k:str(v)for k,v in c.items()},gates={k:str(v)for k,v in g.items()},
       bad={k:str(v)for k,v in g.items()if v<=0},rows=rows,
       own=dict(polynomial_parameter=str(a),quartic_denominator=str(K),negative_split=str(zn),positive_split=str(zp),negative=str(neg),positive=str(positive)))
if __name__=='__main__':
    import json
    o=evaluate();print(json.dumps(o,indent=2));need(not o['bad'],'nonpositive exact gates')

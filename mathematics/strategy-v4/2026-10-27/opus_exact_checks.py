"""Independent, bounded rational checks for the Opus shortcut audit.

No NumPy/SciPy, supplied imports, optimization or native certificate programs.
Exact Fraction arithmetic is the acceptance path; displayed decimals are outward.
"""
from fractions import Fraction as F
from math import isqrt, comb, factorial
from functools import lru_cache
import json

DIGITS = 35
SCALE = 10 ** DIGITS

def sqrt_interval(q):
    assert q >= 0
    k = isqrt(q.numerator * SCALE * SCALE // q.denominator)
    lo, hi = F(k, SCALE), F(k + 1, SCALE)
    assert lo * lo <= q <= hi * hi
    return lo, hi

def atan_interval(q, terms=70):
    assert 0 < q < 1 and terms % 2 == 0
    terms_list = [(-1) ** k * q ** (2*k+1) / (2*k+1) for k in range(terms)]
    lo = sum(terms_list)
    hi = lo + q ** (2*terms+1) / (2*terms+1)
    return lo, hi

a, b = atan_interval(F(1,5)), atan_interval(F(1,239))
PI = (16*a[0]-4*b[1], 16*a[1]-4*b[0])
assert F(314159,100000) < PI[0] < PI[1] < F(314160,100000)
C = (sqrt_interval(1/(2*PI[1]))[0], sqrt_interval(1/(2*PI[0]))[1])

@lru_cache(None)
def normal_at_rational(x):
    if x < 0:
        lo,hi = normal_at_rational(-x)
        return 1-hi,1-lo
    if not x:
        return F(1,2),F(1,2)
    if x > 8:
        return normal_at_rational(F(8))[0], F(1)
    # Integrate the Taylor bounds for exp(-t^2/2): odd partial sum
    # below the exponential, following even partial sum above it.
    term=x; value=term
    for k in range(1,160):
        term *= -x*x*F(2*k-1,2*k*(2*k+1))
        value += term
    low_integral=value
    term *= -x*x*F(319,320*321)
    upper_integral=value+term
    assert 0 <= low_integral <= upper_integral
    lo=F(1,2)+C[0]*low_integral
    hi=F(1,2)+C[1]*upper_integral
    assert 0 <= lo <= hi <= 1
    return lo,hi

def normal_of_ratio(numerator, square_denominator):
    assert square_denominator > 0
    lo,hi=sqrt_interval(square_denominator)
    if numerator >= 0:
        return normal_at_rational(numerator/hi)[0], normal_at_rational(numerator/lo)[1]
    return normal_at_rational(numerator/lo)[0], normal_at_rational(numerator/hi)[1]

def outward(interval, digits=12):
    scale=10**digits
    lo=interval[0].numerator*scale//interval[0].denominator
    hi=-((-interval[1].numerator*scale)//interval[1].denominator)
    return [str(F(lo,scale)),str(F(hi,scale))]

def skeleton_upper(n,p):
    assert 0<p<1
    v=p*(1-p)
    multiplier=sqrt_interval(n*v)[1]/(1-2*v)
    cumulative=F(0); largest=F(0); rows=[]
    for j in range(n+1):
        mass=comb(n,j)*p**j*(1-p)**(n-j)
        normal=normal_of_ratio(j-n*p,n*v)
        after=cumulative+mass
        discrepancy=max(after-normal[0],normal[1]-cumulative)
        largest=max(largest,discrepancy)
        rows.append({'k':j,'normal':outward(normal),'discrepancy_upper':str(discrepancy)})
        cumulative=after
    assert cumulative == 1
    return multiplier*largest,rows

def at_event_lower(n, vals, weights, raw_threshold, probability):
    assert sum(weights)==1 and all(w>0 for w in weights)
    mean=sum(w*x for x,w in zip(vals,weights))
    var=sum(w*(x-mean)**2 for x,w in zip(vals,weights))
    third=sum(w*abs(x-mean)**3 for x,w in zip(vals,weights))
    scale=sqrt_interval(n*var**3)[0]/third
    normal=normal_of_ratio(raw_threshold-n*mean,n*var)
    discrepancy=probability-normal[1]
    assert discrepancy>0
    return scale*discrepancy, {'mean':str(mean),'variance':str(var),'third_absolute_central_moment':str(third),'normal':outward(normal)}

# Exact multinomial coefficient, independent of the discovery convolution.
def event_probability(vals,weights,n,threshold):
    assert len(vals)==3
    total=F(0)
    for i in range(n+1):
      for j in range(n-i+1):
        k=n-i-j
        if i*vals[0]+j*vals[1]+k*vals[2] <= threshold:
            total += comb(n,i)*comb(n-i,j)*weights[0]**i*weights[1]**j*weights[2]**k
    return total

results=[]
for name,n,vals,weights,t in [
 ('n2_zero',2,[F(-1),F(0),F(1)],[F(1,20),F(9,10),F(1,20)],F(0)),
 ('n2_no_zero',2,[F(-1),F(1,1000),F(1)],[F(1,20),F(9,10),F(1,20)],F(1,500)),
 ('n42_standardized_rational',42,[F(-20),F(0),F(20)],[F(1,800),F(399,400),F(1,800)],F(0)),
]:
    mean=sum(w*x for x,w in zip(vals,weights))
    p=sum(w for x,w in zip(vals,weights) if x>mean)
    probability=event_probability(vals,weights,n,t)
    actual,details=at_event_lower(n,vals,weights,t,probability)
    sk,rows=skeleton_upper(n,p)
    assert actual>sk
    assert actual-sk>F(1,1000)
    # Negative control: reversing the established strict comparison rejects.
    reversed_claim=actual<=sk
    assert not reversed_claim
    results.append({'name':name,'n':n,'raw_values':list(map(str,vals)),'weights':list(map(str,weights)),'raw_threshold':str(t),'event_probability':str(probability),'p_positive_after_centering':str(p),'actual_score_lower_outward':outward((actual,actual))[0],'skeleton_score_upper_outward':outward((sk,sk))[1],'strict_margin_lower_outward':outward((actual-sk,actual-sk))[0],'details':details,'normal_edges':rows,'reversed_claim_rejected':True})

# The normal routine's elementary controls, including symmetry and a known
# rational local integral bound; this is not an independent implementation.
assert normal_at_rational(F(0))==(F(1,2),F(1,2))
assert normal_at_rational(F(-1))==(1-normal_at_rational(F(1))[1],1-normal_at_rational(F(1))[0])
assert F(84,100)<normal_at_rational(F(1))[0]<normal_at_rational(F(1))[1]<F(85,100)

# Exact collision control for raw {-1,1,1+epsilon}, weights {1/2,1/4,1/4}.
# Centering places the two middle sums at +/-epsilon/2. Rounding both to
# zero produces CDF 3/4 there; the true centered CDF is 1/2.
eps=F(1,10**12)
vals=[F(-1),F(1),F(1)+eps]; weights=[F(1,2),F(1,4),F(1,4)]
mu=sum(x*w for x,w in zip(vals,weights))
true=event_probability(vals,weights,2,2*mu)
assert mu==eps/4 and true==F(1,2)
assert F(3,4)-true==F(1,4)
print(json.dumps({'scope':'Rational witness lower bounds versus every Bernoulli skeleton jump edge; exact event collisions. No full Berry--Esseen or local-domination theorem.','normal_method':'Machin pi bounds; integer square-root enclosures; integrated exponential Taylor bounds; monotonicity beyond 8.','witnesses':results,'collision_error':'1/4','all_assertions_passed':True},indent=2))

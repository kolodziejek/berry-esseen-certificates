from fractions import Fraction as F
from math import erfc, sqrt
import json
# Independent rational comparisons by integer cross multiplication.
checks={}
checks['sqrt_cap_n47']=46*1011**2-47*1000**2
checks['excess_margin_numerator']=3*1150000-10*335909
checks['own_cap_margin_numerator']=4247*4700-1957*10000
checks['CE_square_margin_numerator']=1681*11304-1900*10000
checks['pi_lower_margin_numerator']=281476*50-157*89625
assert all(v>0 for v in checks.values())
# Reconstruct the displayed total from separately cleared denominator 150000.
# (.41/2)+(1.011/15)+(2*1.011/(25*6))=(30750+10110+2022)/150000.
assert 30750+10110+2022 == 42882
assert F(47*42882,46*150000)==F(335909,1150000)
# These independently verify scope restrictions of this chosen envelope.
assert 45*1011**2-46*1000**2<0
assert F(335909,1150000)>F(29,100)
checks['sqrt_cap_n46_failure']=45*1011**2-46*1000**2
laws=[
 ('symmetric_Bernoulli',[(0,F(1,2)),(1,F(1,2))],47),
 ('skew_Bernoulli_2_over_5',[(0,F(3,5)),(1,F(2,5))],47),
 ('endpoint_near_Bernoulli_1_over_100',[(0,F(99,100)),(1,F(1,100))],47),
 ('reflected_Bernoulli_99_over_100',[(0,F(1,100)),(1,F(99,100))],47),
 ('tiny_middle_atom',[(-1,F(499999,1000000)),(0,F(1,1000000)),(1,F(1,2))],47),
 ('tiny_remote_atom',[(-1,F(499999,1000000)),(1,F(1,2)),(1000,F(1,1000000))],47),
 ('four_point_collisions',[(-2,F(1,10)),(-1,F(2,5)),(1,F(2,5)),(2,F(1,10))],47),
 ('nearby_four_point',[(-101,F(1,4)),(-99,F(1,4)),(99,F(1,4)),(101,F(1,4))],4),
]
rows=[]
for name,law,last in laws:
 assert sum(p for x,p in law)==1
 mu=sum(x*p for x,p in law)
 var=sum((x-mu)**2*p for x,p in law)
 third=sum(abs(x-mu)**3*p for x,p in law)
 assert var>0 and third>0
 rho=float(third)/float(var)**1.5
 dist={0:F(1)};prev=None;worst=(float('inf'),None);maxabsz=0
 for n in range(1,last+1):
  nxt={}
  for a,pa in dist.items():
   for x,p in law:nxt[a+x]=nxt.get(a+x,F(0))+pa*p
  dist=nxt
  assert sum(dist.values())==1
  cum=F(0);delta=0.0
  for x,p in sorted(dist.items()):
   z=float(F(x)-n*mu)/sqrt(n*float(var))
   maxabsz=max(maxabsz,abs(z))
   Phi=.5*erfc(-z/sqrt(2))
   delta=max(delta,abs(float(cum)-Phi))
   cum+=p
   delta=max(delta,abs(float(cum)-Phi))
  score=sqrt(n)*delta/rho
  if prev is not None:
   rhs=sqrt(n/(n-1))*prev+sqrt(n)/(15*(n-1)**1.5)+2*sqrt(n)/(25*(n-1)**2)
   margin=rhs-score
   assert margin>1e-12,(name,n,margin)
   if margin<worst[0]:worst=(margin,n)
  prev=score
 rows.append({'law':name,'n_range':[2,last],'minimum_margin_float':worst[0],'at_n':worst[1],'max_standardized_atom_threshold_float':maxabsz,'last_support_size':len(dist)})
print(json.dumps({'status':'PASS_BOUNDED_DIAGNOSTICS','integer_checks':checks,'actual_laws':rows,'scope':'Independent integer algebra plus finite-law same-law recurrence diagnostics. Convolutions and moments use exact rational arithmetic; Gaussian evaluation and resulting margins use ordinary math.erfc floating point and are not rigorous enclosures.'},indent=2,sort_keys=True))

from fractions import Fraction as F
from functools import reduce
from math import gcd
import json
SL=F('3.162277660');SU=F('3.162277661');D0=F('.047');B=F('32.20665378')
checks={}
def record(name,value):
 assert value>0,(name,value)
 checks[name]=str(value)
z=(SL-1-D0)/3
def Q(p):return (SL+1)*p*p+(SL-1)*(1-p)**2-6*p*(1-p)
record('probability_036_squared_margin',4*z**3*Q(F('.36'))**2-D0**2)
record('probability_048_squared_margin',4*z**3*Q(F('.48'))**2-D0**2)
record('inward_displacement_margin',F('1.99')*F('.994')*6*F('.004')*F('.996')-D0)
record('probability_038_margin',Q(F(3,8))-D0/2)
record('drop_combined_d_terms',6*F('.994')*F('.996')-F('.006')*(SU+7))
record('count_variance_margin',F('1.996')**3*F('11.8')*F('.35')-B)
assert F('1.996')**3*F('11.8')*F('.35')>F('32.84')
# Lattice calculations before standardization: J_std=Jraw/variance^(3/2),
# h_std=hraw/sqrt(variance). Thus J_std>=h_std iff Jraw>=hraw*variance.
laws=[([-1,1],[F(1,2),F(1,2)]),([0,1],[F(2,3),F(1,3)]),([-1,0,1],[F(1,4),F(1,2),F(1,4)]),([-2,-1,1,2],[F(1,4)]*4),([0,2,5],[F(1,10),F(3,10),F(3,5)]),([-100,0,1],[F(1,100000),F(49999,100000),F(1,2)]),([-4,-1,5],[F(1,3)]*3)]
records=[]
for xs,ps in laws:
 assert sum(ps)==1
 mu=sum(F(x)*p for x,p in zip(xs,ps));ys=[F(x)-mu for x in xs]
 var=sum(y*y*p for y,p in zip(ys,ps));h=reduce(gcd,[xs[i+1]-xs[i] for i in range(len(xs)-1)])
 mass=F(0);jraw=F(0)
 for i in range(len(xs)-1):
  gap=ys[i+1]-ys[i];tau=sum(y*p for y,p in zip(ys[i+1:],ps[i+1:]));assert tau>=0
  mass+=tau*gap;jraw+=tau*gap*gap
 assert mass==var and jraw>=h*var
 if len(set(xs[i+1]-xs[i] for i in range(len(xs)-1)))==1:assert jraw==h*var
 records.append(dict(support=xs,variance=str(var),maximal_span=h,gap_mass=str(mass),Jraw=str(jraw),margin=str(jraw-h*var)))
# Negative control: equality J=h cannot be assumed when lattice sites are missing.
assert records[3]['margin']!='0'
# Exact solved-identity checks, independent rational tuples including zero costs.
identity_checks=0
for n in [2,42,700]:
 for a in [F(0),F(1,3)]:
  for H in [F(0),F(7,5)]:
   e=F(3,4);c=F(2,5);rho=F(9,8);phi=F(2,5);D=F(1,100);Lterm=F(1,50)
   R=(n+H*H)*a+n*c*rho*(1-e)+n*phi*e*D/6+Lterm
   solved=(R-n*c*rho*(1-e)-n*phi*e*D/6-Lterm)/(n+H*H)
   assert solved==a and n*phi*e*D/6<=R
   identity_checks+=1
print(json.dumps(dict(status='PASS_OPUS_GEOMETRY_NOTES',mathematical_scope='Diagnostics of new explanations; continuous lattice and conservation arguments are proved in TeX.',rational_margins=checks,lattice_examples=records,identity_diagnostics=identity_checks,rejected_false_equality_for_missing_lattice_sites=True),indent=2))

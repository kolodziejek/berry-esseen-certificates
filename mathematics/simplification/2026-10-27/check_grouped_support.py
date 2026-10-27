#!/usr/bin/env python3
"""Fixed exact 14-interval zero-loss support certificate, all n>=42.

Only imports our new source-binding helper, never archived programs. This checks
polynomial signs, whole-ray signs, parameter binding and Bernstein inversion;
analytic contact/heat inequalities and resource acquisition remain premises.
"""
from fractions import Fraction as F
from math import comb
from collections import defaultdict
from copy import deepcopy
from zipfile import ZipFile
from hashlib import sha256
import json
import sys
import check_support_lift as binding

# Fixed rational targets, not adjustable search tolerances. Columns R,r,b,count.
TABLE = [
 ('5/2','603319/500000','32128627/100000000',17),
 ('101/40','475374/390625','8224681/25000000',5),
 ('51/20','61183419/50000000','33662533/100000000',4),
 ('103/40','30833983/25000000','8698269/25000000',5),
 ('13/5','30994887/25000000','35540061/100000000',4),
 ('21/8','24988347/20000000','36644311/100000000',5),
 ('53/20','125900813/100000000','37372893/100000000',4),
 ('107/40','63303431/50000000','1201521/3125000',4),
 ('27/10','63753427/50000000','489197/1250000',4),
 ('109/40','128341449/100000000','20069857/50000000',4),
 ('11/4','25857241/20000000','41146991/100000000',4),
 ('111/40','129968327/100000000','42077471/100000000',3),
 ('121/40','71458741/50000000','46459359/100000000',1),
 ('96/25','7361/4000','641562334877/1000000000000',1),
]
C=F(819,2000); S=F(202424330939,200000000000); ELL=F(6403124237432,10**12)
need=binding.need

def plus(*ps):
 out=[F(0)]*max(map(len,ps))
 for p in ps:
  for k,x in enumerate(p):out[k]+=x
 while len(out)>1 and out[-1]==0:out.pop()
 return out

def scale(p,x):return [a*x for a in p]
def mul(p,q):
 out=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):out[i+j]+=a*b
 return out

def at(p,x):return sum(a*x**i for i,a in enumerate(p))

def coefficients(p,l,h):
 need(l<h,'nonempty closed radial interval')
 d=len(p)-1
 power=[sum(p[i]*comb(i,j)*l**(i-j)*(h-l)**j for i in range(j,d+1)) for j in range(d+1)]
 bs=[sum(power[j]*F(comb(k,j),comb(d,j)) for j in range(k+1)) for k in range(d+1)]
 validate_transform(power,bs)
 return bs

def validate_transform(power,bs):
 d=len(power)-1
 need(len(bs)==d+1,'complete coefficient vector')
 reconstructed=[comb(d,j)*sum((-1)**(j-k)*comb(j,k)*bs[k] for k in range(j+1)) for j in range(d+1)]
 need(reconstructed==power,'independent inverse Bernstein identity')

def polynomials(r,b):
 A=[F(0),F(-1,2),F(0),F(1,6)]
 J=list(map(F,[0,-15,0,0,0,1])); H4=list(map(F,[3,0,-6,0,1]))
 D=scale(J,F(1,120*41)); W=plus(A,scale(D,F(-15,2)))
 B=scale(mul(H4,H4),F(1,256*41))
 E=plus(scale([0,0,0,0,0,0,1],F(51,14400*41)/ELL),scale([-2,0,3],F(51,960*41)/ELL),[0,F(1,8*41**2)])
 Q=[r*F(48,125)/42,3*b,F(3,2)*r,F(-1)]
 G=plus(mul(plus(scale(A,F(1,2)),scale(D,-3),scale(H4,F(-1,12)/ELL)),W),B)
 P=plus(scale(plus(mul(A,W),B),F(2,5)*S**3),scale(mul(E,W),S**3),scale(mul(Q,W),C))
 return dict(A=A,H4=H4,J=J,W=W,G=G,negative_Q=scale(Q,-1),negative_P=scale(P,-1))

def rays(u,r,b):
 Q=-u**3+F(3,2)*r*u*u+3*b*u+r*F(48,125)/42
 Qp=-3*u*u+3*r*u+3*b; Qpp=-6*u+3*r
 L=F(2,5)*(u*u/2+F(1,2)+F(48,125)/42)+C*Qp
 Lp=F(2,5)*u+C*Qpp; Lpp=F(2,5)-6*C
 gates=[Q,Qp,Qpp,L,Lp,Lpp]
 need(all(x<0 for x in gates),'strict entire-ray propagation')
 return gates

def bind_table(table,rows):
 groups=defaultdict(list)
 for row in rows:groups[F(row['radius'])].append((F(row['rho_upper']),F(row['beta_absolute_upper'])))
 expected=[(str(R),str(max(x[0] for x in rs)),str(max(x[1] for x in rs)),len(rs)) for R,rs in sorted(groups.items())]
 # Initial moment inputs from the two retained published bounds; root enclosure
 # certifies the chosen b, independently of historical certificate coefficients.
 r=min(F(3031,10000)*F(646,1000)/(C-F(3031,10000)),F(3322,10000)*F(429,1000)/(C-F(3322,10000)))
 b=F(641562334877,10**12)
 need(0<b<1 and (1+b*b)**2>r*r*(1-b*b),'initial outward beta ceiling')
 expected.append(('96/25',str(r),str(b),1))
 need(table==expected,'all 65 invocations bound to exact componentwise group maxima')

def check(table):
 need(ELL>0 and ELL**2<41 and S**2>F(42,41),'outward constants')
 a=F(48,125);x=F(1,42)
 scale_margin=2*a-F(3,4)-(a+F(1,4))*x+(a*a-a)*x*x-a*a*x*x*x
 need(scale_margin>0,'all-index scale correction')
 result=[];values=[]
 for R,r,b,count in table:
  R,r,b=map(F,(R,r,b));U=F(21,5) if R==F(96,25) else F(39,10)
  need(F(5,2)<=R<U,'complete radial segment')
  ps=polynomials(r,b);mins={};bs_all={}
  for name,p in ps.items():
   bs=coefficients(p,R,U)
   need(min(bs)>F(1,4),'fixed strict coefficient margin: '+name)
   mins[name]=str(min(bs));bs_all[name]=list(map(str,bs));values.extend(bs)
  result.append(dict(radius=str(R),rho=str(r),beta=str(b),invocations=count,splice=str(U),
                     minima=mins,ray_gates=list(map(str,rays(U,r,b))),coefficients=bs_all))
 need(len(values)==672,'complete 14 by 48 coefficient cover')
 return result,values,scale_margin

def main():
 need(not sys.flags.optimize and len(sys.argv)==1,'unoptimized fixed acceptance invocation')
 need(sha256(binding.ARCHIVE.read_bytes()).hexdigest()==binding.ARCHIVE_SHA,'baseline archive identity')
 with ZipFile(binding.ARCHIVE) as z:
  p=json.loads(binding.read_member(z,binding.LEFT_SHA),object_pairs_hook=binding.unique)
 rows=binding.bind_left_rows(p)
 bind_table(TABLE,rows)
 result,values,margin=check(TABLE)
 rejected=[]
 def reject(name,fn):
  try:fn()
  except (binding.Rejected,KeyError,TypeError,IndexError):rejected.append(name)
  else:raise binding.Rejected('negative control accepted: '+name)
 reject('missing_group',lambda:bind_table(TABLE[:-1],rows))
 t=deepcopy(TABLE);t[1]=t[0];reject('duplicate_group',lambda:bind_table(t,rows))
 reject('reordered_groups',lambda:bind_table(TABLE[::-1],rows))
 t=deepcopy(TABLE);t[0]=(t[0][0],'1',t[0][2],t[0][3]);reject('lower_moment_cap',lambda:bind_table(t,rows))
 t=deepcopy(TABLE);t[0]=('251/100',*t[0][1:]);reject('missing_radial_prefix',lambda:bind_table(t,rows))
 reject('corrupt_bernstein_coefficient',lambda:validate_transform([F(1),F(2),F(3)],[F(1),F(2),F(7)]))
 reject('missing_bernstein_coefficient',lambda:validate_transform([F(1),F(2)],[F(1)]))
 reject('negative_polynomial',lambda:need(min(coefficients([F(-1),F(0),F(-1)],F(0),F(1)))>0,'negative polynomial'))
 reject('false_ray_cap',lambda:rays(F(39,10),F(4),F(1,2)))
 # Nonconstant and constant direct controls prevent a vacuous transform check.
 need(coefficients([F(1),F(-2),F(3)],F(0),F(1))==[F(1),F(0),F(2)],'quadratic control')
 need(coefficients([F(7)],F(2),F(3))==[F(7)],'constant control')
 print(json.dumps(dict(status='PASS_GROUPED_ZERO_LOSS_SUPPORT_ARITHMETIC',
  mathematical_scope='All n>=42 support polynomial/ray signs for 65 bound calls. Contact/heat analysis and actual-law resource acquisition remain hypotheses; no full LOCAL42 or Berry--Esseen acceptance.',
  native_certificate_programs_executed=0,intervals=14,subdivision_search=False,
  coefficients_checked=len(values),global_coefficient_minimum=str(min(values)),strict_lower_margin='1/4',
  scale_margin=str(margin),negative_controls=rejected,groups=result),indent=2,sort_keys=True))

if __name__=='__main__':main()

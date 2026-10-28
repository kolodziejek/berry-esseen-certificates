#!/usr/bin/env python3
"""Exact derivative proof of continuous folded low-noise contact exclusion.
No grid, interpolation, or imported constructor/evaluator is used.
"""
from fractions import Fraction as F
import json,sys
TH,E,R=F(37,5000),F(249,125),F(221,200)
S,C,e=F(81,80),F(819,2000),F(8,875)
left,right=F(9,10)*E,F(11,10)*E
a,d=2*(1-TH)/E,-2+3*TH

def need(ok,why):
 if not ok:raise ValueError(why)
def plus(*ps):return[sum(p[i]if i<len(p)else F(0)for p in ps)for i in range(max(map(len,ps)))]
def times(k,p):return[k*x for x in p]
def product(p,q):
 out=[F(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):out[i+j]+=x*y
 return out
def derivative(p):return[i*p[i]for i in range(1,len(p))]or[F(0)]
def value(p,t):
 out=F(0)
 for x in reversed(p):out=out*t+x
 return out
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return{k:encode(v)for k,v in x.items()}
 if isinstance(x,list):return[encode(v)for v in x]
 return x

def main():
 need(__debug__ and not sys.flags.optimize,'ordinary Python')
 need(F(5,677)<TH and E*E<4*(1-TH),'common variance gates')
 need(R>F(3,70) and(R-F(3,70))**2*F(6,25)>F(13,25)**2,'common rho gate')
 need(24**2*F(6,25)**3>F(12,5)**2,'common cubic coefficient')
 u=[F(0),F(1)];b=[d,a]
 H4=[F(3),F(0),F(-6),F(0),F(1)]
 cubic=[F(0),-F(1,2),F(0),F(1,6)]
 error=[-F(34,78720),F(3,820),F(51,78720),F(0),F(0),F(1,4100)]
 Q=plus([e*R,F(0),F(3,2)*R,F(-1)],times(3,product(b,u)))
 P=plus(times(S**3,plus(times(F(2,5),plus(cubic,times(-F(1,72),H4))),error)),times(C,Q))
 explicit=[S**3*(-F(1,60)-F(34,78720))+C*e*R,
 S**3*(-F(1,5)+F(3,820))+3*C*d,
 S**3*(F(1,30)+F(51,78720))+C*(F(3,2)*R+3*a),
 S**3/F(15)-C,-S**3/F(180),S**3/F(4100)]
 need(P==explicit,'exact quintic expansion coefficient identity')
 P1=derivative(P);P2=derivative(P1);P3=derivative(P2)
 # These polynomials are radial derivatives holding beta fixed at the
 # boundary value b(t), unlike derivatives(Q) along that boundary family.
 Q1=plus([F(0),3*R,F(-3)],times(3,b));Q2=[3*R,F(-6)]
 L=plus([F(1,5)+F(2,5)*e,F(0),F(1,5)],times(C,Q1))
 L1=plus([F(0),F(2,5)],times(C,Q2));L2=F(2,5)-6*C
 gates={'domain':3-left*left,'H4_right':value(H4,right),
 'P3_left':value(P3,left),'P3_right':value(P3,right),'P2_left':value(P2,left),
 'negative_P1_right':-value(P1,right),'P_right':value(P,right),
 'total_Q2_left':value(derivative(derivative(Q)),left),
 'negative_total_Q1_right':-value(derivative(Q),right),'Q_right':value(Q,right),
 'total_Q1_derivative_left':value(derivative(Q1),left),'Q1_left':value(Q1,left),'Q2_left':value(Q2,left),
 'total_L_derivative_left':value(derivative(L),left),'L_left':value(L,left),'L1_left':value(L1,left),'L2':L2}
 need(P3[2]>0,'convex quadratic third derivative')
 need(all(x<0 for x in gates.values()),'all strict endpoint/derivative gates')
 # P3<0 -> P2 decreasing<0 -> P1 decreasing but positive -> P increasing.
 # Q''<0 and Q'(right)>0 -> Q increasing. Q1,L,Q2,L1 decrease.
 print(json.dumps(encode(dict(status='PASS_CONTINUOUS_FOLDED_LOW_NOISE',u_interval=[left,right],p_interval=[F(2,5),F(53,100)],noise_interval=[F(0),F(3,40)],
 common_theta=TH,common_ell=E,common_rho=R,beta_affine=[d,a],quintic=P,
 radial_polynomials=dict(Q=Q,Q1=Q1,Q2=Q2,L=L,L1=L1,L2=[L2]),negative_endpoint_gates=gates,
 scope='Entire continuous p and low-noise domain under the same acquired-strip/contact premises. Total boundary-family derivatives are used only for interval verification; radial continuation holds beta fixed. No larger-noise or other-panel result.')),indent=2,sort_keys=True))
if __name__=='__main__':main()

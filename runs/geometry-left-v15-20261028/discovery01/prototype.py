from fractions import Fraction as F
import json
N=700;lo=F(1,100);hi=F(8,25);a=1-F(6,N);b=1+F(3,N);z=F(7,5)*a
m=F(3,4);A=F(7,10);vthree=F(13,125);beta=F(41,100);phi=F(2,5)
def add(x,y):return [(x[i] if i<len(x) else F(0))+(y[i] if i<len(y) else F(0)) for i in range(max(len(x),len(y)))]
def scale(x,c):return [a*c for a in x]
def mul(x,y):
 out=[F(0)]*(len(x)+len(y)-1)
 for i,a in enumerate(x):
  for j,b in enumerate(y):out[i+j]+=a*b
 return out
def ev(x,t):return sum((a*t**i for i,a in enumerate(x)),F(0))
x=[F(0),F(1)];T=scale(x,F(5,3));M=add(scale(T,A*A),scale(mul(T,T),3))
W=scale([F(0),z/2-A*A*b/16-12*F(22,7)**2/N,-z*z/4-3*b*b/16,z**3/12,-z**4/48],m*F(2,5))
polys={}
for name,c in [('negative',F(8,25)),('positive',F(0))]:
 sqrt_upper=[F(13,200),F(250,39)]
 S=add(add(scale(T,F(1,4)),scale(sqrt_upper,c)),scale(M,F(27,256)*(F(5,3)+F(5,4)*c)))
 E=scale(S,beta)
 if name=='negative':E=add(E,[phi*(F(23,200)+F(2,27))])
 else:E=add(E,[phi*F(2,27),phi*F(23,25)/2])
 E=scale(E,1/vthree)
 P=add(add(W,scale(E,-F(1,N))),scale(x,-F(1,100)))
 second=2*P[2]+6*P[3]*hi
 assert P[4]<0 and second<0
 endpoints=[ev(P,y) for y in [lo,hi]]
 print(name,[float(y) for y in endpoints],float(second))
 polys[name]={'coefficients':[str(y) for y in P],'endpoint_margins':[str(y) for y in endpoints],'second_derivative_upper':str(second)}
print(json.dumps({'N':N,'polynomials':polys},indent=2))

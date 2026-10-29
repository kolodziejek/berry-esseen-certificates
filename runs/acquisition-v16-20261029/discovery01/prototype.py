from fractions import Fraction as F
from math import sqrt
sl=F('3.162277660');su=F('3.162277661');D=F('0.047');z=(sl-1-D)/3
print('z',float(z))
K=min(F('.46')*((sl+5)*z+2*(sl-1)),F('.24')*((sl+7)*z+2*(sl+1)))
print('k',float(K), 'theta0',float(D/(F('1.67')*F('3.7'))))
T=F('.008');W=1-T
print('dmax',float(1-2*sqrt(float(z*F('.1824')))))
print('dmonotonic',float(6*W*F('.42')-T*(su+7)))
print('d004cost',float(F('1.99')*W*6*F('.004')*(1-F('.004'))))
C=min(3*(sl+1)*F('.46'),3*(sl+3)*F('.24'))
print('theta derivative',float((2-3*T)*(C-(su+7)*F('.004'))-3*(F('.4')+6*F('.004'))))
def Q(p):return (2*sl+6)*p*p-(2*sl+4)*p+sl-1
for p in [F(3,8),F(93,200)]:print('pbound',float(Q(p)),float(Q(p)**2-D*D*p*(1-p)))
C=min(3*(sl+1)*F('.535'),3*(sl+3)*F('.375'))
print('C refined',float(C),'theta refined',float(D/(F('1.99')*C)))
print('rho',float(F(17,32)/sqrt(float(F(15,64)))+D/(sl-1)))
e=F('1.996');r=F(9,8);T=F('.0036');bl=F('.07')-2*F('.535')*T;bu=F('.25')+2*F('.375')*T
for side,t,b in [('negative',e*(F('.375')+F('.6')),-bl),('positive',e*(F('.535')+F('.6')),bu)]:
 S=F(81,80);c=F(819,2000);eta=F(8,875)
 q=-t**3+F(3,2)*r*t*t+3*b*t+eta*r
 h=S**3*(F(2,5)*((t**3-3*t)/6+abs(t**4-6*t*t+3)/72)+t**5/4100+3*t/820+17*(3*t*t-2)/78720)
 q1=-3*t*t+3*r*t+3*b;q2=-6*t+3*r
 rays=[q,q1,q2,F(2,5)*(t*t/2+F(1,2)+eta)+c*q1,F(2,5)*t+c*q2,F(2,5)-6*c]
 print(side,'t',float(t),'beta',float(b),'heatbound',float(h+c*q),'rays',[float(x)for x in rays])
for nm,p,q in [('global',F('.375'),F('.535')),('left',F('.375'),F('.6'))]:
 y0=3*(sl+3)*p-(su+7)*F('.004')+2*sqrt(float(6*F('.996')*(sl+1)*p))
 y1=3*(sl+1)*q-(su+5)*F('.004')+2*sqrt(float(6*F('.996')*(sl-1)*q))
 print(nm,y0,y1,'lambda',float(F('32.20665378')/(e**3*min(y0,y1))))

#!/usr/bin/env python3
"""HIGH_WINDOW50 kernel; fixed algebra acceptance is a separate driver.

The earlier frozen entry kernels are not changed. Install only in a newly
named experiment/theorem. Every candidate retains all six frequency pieces.
"""
import kernel

def install(target=kernel):
 def one(n,a,m,d0,M,w):
  k=target;F=k.F;p,sp=F(333,106),F(4431,2500);b=F(9,10)
  k.need(type(n)is int and n>2 and 0<a<=1 and m>0 and 0<d0<=12 and 1<=M<=F(111,10),'HIGH_WINDOW50 event domain')
  k.need(0<w<=F(1,4),'HIGH_WINDOW50 disjoint peak cores')
  h=p-F(22,7)**3*w*w/6;k.need(h>0,'HIGH_WINDOW50 positive sine slope')
  rate=(1-max(1-t*t+(M+3)*t**4/12 for t in(F(1,2),b)))/2
  kap=a*F(23,48)**2*d0*d0;nl,nu=k.roots(F(n))
  for c in(rate,a*h*h*w*w,a*F(23,48)**2,F(1,8)):
   k.need(c>0 and 2*n*c>1,'HIGH_WINDOW50 all-index monotonicity')
  s3=sum((F(1,j**3)for j in range(1,21)),F(0))+F(1,800)
  s5=sum((1/(F(j)-w)**5 for j in range(1,21)),F(0))+1/(4*(20-w)**4)
  first=2*nu*k.exphi(n*rate)
  slope=(1-(M+3)*F(53,600))/2;cquarter=F(1,8)-(M+3)/384
  if slope>0:
   k.need(cquarter>0 and 2*n*cquarter>1,'HIGH_WINDOW50 first-piece monotonicity')
   x=n*slope/4;rat=(x+2)/(x*x+4*x+2)
   first=min(first,2*nu*k.exphi(n*cquarter)*rat)
  zero=k.exphi(n*kap*b*b)/(2*b**4*kap*nl);x=n*kap*b*b
  if x>=F(1,4):zero=min(zero,nu*k.exphi(x)*(x+2)/(2*b*b*(x*x+4*x+2)))
  xc=F(n,8);rc=(xc+2)/(xc*xc+4*xc+2);gc=k.roots(M-1)[1]
  comparator=nu*k.exphi(xc)*(2*rc+gc/3)
  k.need(n>=5,'HIGH_WINDOW50 comparator monotonicity')
  terms=(first,m*(s3+3*s5/(n*a*h*h))/(4*p*sp*h*k.roots(a)[0]),m*nu*k.exphi(n*a*h*h*w*w)/(2*p*p),zero,nu*k.exphi(n*a*F(23,48)**2)/(2*b*b),comparator)
  k.need(all(x>0 for x in terms),'HIGH_WINDOW50 all six positive pieces')
  return k.up(sum(terms),10**10),terms
 def best(n,a,m,d0,M,window):
  F=target.F
  pool=[window,F(1,8),F(4,25),F(9,50),F(1,5),F(11,50),F(1,4)]
  return min((one(n,a,m,d0,M,w)for w in pool),key=lambda z:z[0])
 target.high=best
 return one,best

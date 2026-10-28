"""Small floating-point discovery; not acceptance."""
import math,json
s=math.sqrt(10);D=.76682509;W=.944;z=(3.162277660-1-D)/3
Q=lambda p:(s+1)*p*p+(s-1)*(1-p)**2-6*p*(1-p)
r={}
for name,f in [('lambda+',lambda p:p*(17.558-42*Q(p))/(3*(s+1))),('lambda-',lambda p:(1-p)*(17.558-42*Q(p))/(3*(s+3))),('rho',lambda p:(1-2*p*(1-p)-.4*Q(p))/math.sqrt(p*(1-p))+.4*D)]:
 ps=[.24+.30*i/10000 for i in range(10001)];p=max(ps,key=f);r[name]={'p':p,'value':f(p)}
r['z']=z;r['noise_K_lower']=min(.46*((s+5)*z+2*(s-1)),.24*((s+7)*z+2*(s+1)))
r['coarse_theta_lower']=2*math.sqrt(z)*.2*3.13
r['dmax_upper']=1-2*math.sqrt(z*.1824)
r['d_derivative_lower']=6*W*(1-2*(1-2*math.sqrt(z*.1824)))-.056*(s+7)
print(json.dumps(r,indent=2))

"""Explore the unweighted crossing bias; floating probabilities, not proof."""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
root=Path(__file__).resolve().parents[3]
source=root/'runs/simplification-v13-20261028/actual01/stdout.json'
laws=json.loads(source.read_text())['cases'];rows=[]
for row in laws:
    n=row['n'];p=F(row['p']);q=1-p;A=F(row['A']);lam=F(row['lambda']);w=F(row['w'])
    a0=lam*(1-w)/(n*q*A);a1=lam*w/(n*p*A)
    e0=float(a0/(A+a0));e1=float(a1/(A+a1));dist={}
    for j in range(n+1):
        for i0 in range(n-j+1):
            mass0=comb(n-j,i0)*e0**i0*(1-e0)**(n-j-i0)
            if not mass0:continue
            for i1 in range(j+1):
                mass=mass0*comb(j,i1)*e1**i1*(1-e1)**(j-i1)
                if not mass:continue
                x=j+(n-j-i0)*a0-i0*A+i1*A-(j-i1)*a1
                dist[x]=dist.get(x,0.)+mass
    cdf=0;best=(-1e9,None)
    for x,mass in sorted(dist.items()):
        cdf+=mass
        if not(n*a0<=x<n*(1-a1)):continue
        bias=cdf-1-float(x)
        if bias>best[0]:best=bias,x
    rows.append({'p':str(p),'lambda':str(lam),'w':str(w),'n':n,'max_bias_diagnostic':best[0],'threshold':str(best[1])})
print(json.dumps({'status':'DISCOVERY_ONLY','scope':'Unweighted conditional count CDF sum; exact atom keys and float masses; not an inequality proof','cases':rows,'python':sys.version},indent=2))

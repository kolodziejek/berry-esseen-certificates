"""Bounded actual-law diagnostics of the weighted reserve, not acceptance.

All atom positions are exact Fractions; conditional masses, normal CDF and
scores are floats. Neither continuous coverage nor rounded positivity is proof.
"""
from fractions import Fraction as F
from math import comb,sqrt,erf,pi
from bisect import bisect_right
import json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
CE=(3+sqrt(10))/(6*sqrt(2*pi));Phi=lambda x:(1+erf(x/sqrt(2)))/2
def noise(a,b):
    if not a or not b:return [(F(0),F(1))]
    return [(-a,b/(a+b)),(b,a/(a+b))]
def power(z,n):
    if len(z)==1:return [(F(0),1.)]
    (a,p),(b,q)=z
    return [(j*a+(n-j)*b,comb(n,j)*float(p)**j*float(q)**(n-j))for j in range(n+1)]
def prefix(items):
    out={}
    for x,p in items:out[x]=out.get(x,0.)+p
    xs=sorted(out);ps=[0.];ms=[0.]
    for x in xs:ps.append(ps[-1]+out[x]);ms.append(ms[-1]+float(x)*out[x])
    assert abs(ps[-1]-1)<1e-12
    return xs,ps,ms
def query(table,t):
    xs,ps,ms=table;k=bisect_right(xs,t)
    return ps[k],float(t)*ps[k]-ms[k]
records=[];rejected=[]
for p in map(F,['.25','.3','.4','.42','.5','.53']):
    for lam in map(F,['.075','.15','.30']):
        for w in [F(0),F(1,2),F(1)]:
            for factor in [F(1),F(1,2)]:
                n=42;q=1-p;v=p*q
                A0=F('.6')*factor;A1=(F('.7')if p<F('.4')else F('.6'))*factor
                a0=lam*(1-w)/(n*q*A0);a1=lam*w/(n*p*A1)
                cap=F('.068')if p<F('.4')else F('.072')
                if a0+a1>cap:continue
                u0=noise(A0,a0);u1=noise(a1,A1)
                atoms=[(x-p,q*z)for x,z in u0]+[(1+x-p,p*z)for x,z in u1]
                atoms=sorted(atoms);V=v+lam/n
                M=sum(abs(x)**3*z for x,z in atoms);gamma=sum(x**3*z for x,z in atoms)
                J=sum(sum(x*z for x,z in atoms[j+1:])*(atoms[j+1][0]-atoms[j][0])**2 for j in range(len(atoms)-1))
                budget=n*((3+sqrt(10))*float(M)-float(gamma)-3*float(J))/float(V)**1.5
                if budget>32.20665378:
                    rejected.append({'p':str(p),'lambda':str(lam),'w':str(w),'factor':str(factor),'budget_diagnostic':budget});continue
                tables=[];thresholds=set()
                for j in range(n+1):
                    tab=prefix([(j+x+y,px*py)for x,px in power(u1,j)for y,py in power(u0,n-j)])
                    tables.append(tab)
                    thresholds.update(t for t in tab[0]if (t-n*p)**2<=F('1.84')**2*V)
                thresholds.update(F(j)for j in range(n+1)if (j-n*p)**2<=F('1.84')**2*V)
                masses=[comb(n,j)*float(p)**j*float(q)**(n-j)for j in range(n+1)]
                FB=[];ac=0.
                for z in masses:ac+=z;FB.append(ac)
                rho=float(M)/float(V)**1.5;rhoB=float(1-2*v)/sqrt(float(v))
                worst=None;least=None;unweighted=None
                for t in sorted(thresholds):
                    FL=[query(z,t)for z in tables];cdf=[z[0]for z in FL];loss=[z[1]for z in FL]
                    assert cdf[0]>1-1e-12 and cdf[n]<1e-12
                    gs=[loss[i-1]-loss[i]-cdf[i]for i in range(1,n+1)]
                    assert min(gs)>-1e-12
                    G=sqrt(n)*sum(masses[i]*gs[i-1]for i in range(1,n+1))
                    curv=sqrt(n)*sum((masses[j+1]-masses[j])*(loss[j]-max(float(t-j),0))for j in range(1,n))
                    k=t.__floor__();u=float(t-k);normdiff=Phi(float(t-n*p)/sqrt(n*float(V)))-Phi(float(k-n*p)/sqrt(n*float(v)))
                    repair=sqrt(n)*(u*masses[k+1]-normdiff)+CE*(rhoB-rho)
                    exact_delta=-G+curv+repair
                    c=max(0.,float(n*p-q-t));s=float(lam/n)
                    curb=sqrt(n)*(s/(4*float(v))+c*sqrt(s)/(2*float(v)*sqrt(n+1)))
                    bound=-G+curb+repair
                    row={'threshold':str(t),'phase':str(t-k),'H':float(t-n*p)/sqrt(float(V)),
                         'weighted_loss':G,'unweighted_loss':sum(gs),'signed_curvature':curv,'curvature_bound':curb,
                         'phase_normal_cubic_repair':repair,'delta':exact_delta,'upper_with_exact_loss':bound,'loss_per_lambda':G/float(lam)}
                    if worst is None or bound>worst['upper_with_exact_loss']:worst=row
                    if least is None or G<least['weighted_loss']:least=row
                    if unweighted is None or sum(gs)<unweighted['unweighted_loss']:unweighted=row
                records.append({'n':n,'p':str(p),'lambda':str(lam),'w':str(w),'factor':str(factor),'inward':str(a0+a1),
                                'budget_diagnostic':budget,'events':len(thresholds),'worst_bound':worst,'least_weighted_loss':least,'least_unweighted_loss':unweighted})
print(json.dumps({'status':'DISCOVERY_ONLY','scope':'Actual-law weighted-loss diagnostics; exact atom positions with floating probabilities/scores, no coverage or proof',
                  'cases':records,'excluded_by_budget_diagnostic':rejected,'python':sys.version},indent=2))

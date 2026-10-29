"""Floating diagnostics with physical conditional-variance transport.

No acceptance: the inherited Poisson expectation is truncated floating point.
This experiment checks whether a conservative correction destroys the signal.
"""
from pathlib import Path
import hashlib,json,math
old=Path(__file__).resolve().parents[2]/'simplification-v11/2026-10-28/counts-v11-compound-discovery.py'
raw=old.read_bytes();scope={'__name__':'diagnostic_helper','__file__':str(old)}
exec(compile(raw,str(old),'exec'),scope)
cp2=scope['cp2'];A=.6;d=.072;N=42;v=.24;cv=2.5

def one(lam,r,w):
 xi=1.84*math.sqrt(.25+lam/N);D=xi+r;Z=.625*D+.375+D**3/N
 mlo=2*.39886*(1-(D*D/(2*v)+Z)/N);mhi=.85
 fm=math.exp(((r*r+2*xi*r)/(2*v)+Z)/N)
 R=1+max(0,.53+D-1)/(N*v-.6*max(0,D-1))
 tails=0;anchors=[]
 for i in range(1,5):
  # Each physical variance group is inflated separately. This common
  # envelope is valid even though both upper endpoints need not coexist.
  t=(1+cv*(D+i)/N)*lam
  val,j=cp2((1-w)*t,w*t,i+r);tails+=val;anchors.append(j)
 V=(1+cv*(D+1)/N)*lam;z=A/V
 Bt=math.exp(-V/A**2*((1+z)*math.log1p(z)-z))
 tails+=Bt**5/(1-Bt)
 K=.4/(N*(.25+lam/N)**1.5);B=.78+3*.52*lam/(8*N*v)
 normal=1.75*D*lam/N;Lambda0=lam*(1-w);Lambda1=lam*w
 # Physical allocation: t0=g0*Lambda0, t1=g1*Lambda1. The exact
 # g0/g1 share delta; their rectangular enlargement is a relaxation.
 G0=[1-D/(N*.47),1+D/(N*.47)]
 G1=[1-D/(N*.4),1+D/(N*.4)]
 best=(-math.inf,None)
 for ai in range(20,121,2):
  alpha=ai/100;M=5*alpha**4;kap=-4*r
  poly=-r**4+3*alpha**2*r*r+2*alpha**3*r
  margins=[]
  for m in [mlo,mhi]:
   for g0 in G0:
    for g1 in G1:
     t=g0*Lambda0+g1*Lambda1
     c0=max(m/M*g0*(x*x-kap*x)+K*x for x in [-A,d])
     c1=max(m/M*g1*(x*x-kap*x)-K*x for x in [-d,A])
     own=m/M*((3*alpha**2-6*r*r)*t-3*t*t+poly)-c0*Lambda0-c1*Lambda1
     gain=K*lam*(1.2*(1-w)+1.41*w-B)
     margin=own-m*(r*fm+R*tails)-normal+gain
     margins.append(margin)
  value=min(margins)
  if value>best[0]:best=(value,alpha)
 tg=G0[1]*Lambda0+G1[1]*Lambda1
 own=(r*r/(tg+r*r) if r else 0)-r*fm
 cm=min(m*(own-R*tails) for m in [mlo,mhi])-normal+K*lam*(1.2*(1-w)+1.41*w-d-B)
 if cm>best[0]:best=(cm,'Cantelli')
 return {'lambda':lam,'r':r,'physical_allocation':w,'margin':best[0],'alpha':best[1],'tail':tails,'anchors':anchors}

rows=[]
for lam in [.05,.075]:
 cases=[one(lam,j/100,w/4)for j in range(16)for w in range(5)]
 rows.append({'lambda':lam,'cases':len(cases),'worst':min(cases,key=lambda x:x['margin']),
  'failures':sum(x['margin']<=0 for x in cases),'by_allocation':[min([x for x in cases if x['physical_allocation']==w/4],key=lambda x:x['margin'])for w in range(5)]})
print(json.dumps({'status':'DISCOVERY_PHYSICAL_VARIANCE_TRANSPORT_ONLY','helper_sha256':hashlib.sha256(raw).hexdigest(),'rows':rows,'scope':'Finite floating sample at n42; no uniform theorem or continuous coverage.'},indent=2))

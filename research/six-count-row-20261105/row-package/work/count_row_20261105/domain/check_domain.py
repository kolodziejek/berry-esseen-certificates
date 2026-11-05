"""Read-only domain census, atom controls, and independent cleared-degree identities."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb
from copy import deepcopy
from collections import defaultdict
import json,sys,hashlib
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import domain as d

def conv(a,b):
 out=defaultdict(F)
 for x,px in a.items():
  for y,py in b.items():out[x+y]+=px*py
 return dict(out)
def powerlaw(a,n):
 ans={F(0):F(1)}
 for _ in range(n):ans=conv(ans,a)
 return ans
def cdf(a,h,closed=True):return sum((v for x,v in a.items()if x<=h if closed),F(0)) if closed else sum((v for x,v in a.items()if x<h),F(0))
def pmul(a,b):
 z=defaultdict(F)
 for (i,j),v in a.items():
  for (k,l),w in b.items():z[i+k,j+l]+=v*w
 return {k:v for k,v in z.items()if v}
def padd(a,b):
 z=defaultdict(F,a)
 for k,v in b.items():z[k]+=v
 return {k:v for k,v in z.items()if v}
def pscale(a,c):return {k:v*c for k,v in a.items()if v*c}
def ppow(a,n):
 ans={(0,0):F(1)}
 for _ in range(n):ans=pmul(ans,a)
 return ans
def peval(a,p,u):return sum((v*p**i*u**j for(i,j),v in a.items()),F(0))
P={(1,0):F(1)};Q={(0,0):F(1),(1,0):-F(1)}
def masscleared(j,dp=0,dq=0):return pscale(pmul(ppow(P,j+2-dp),ppow(Q,7-j-dq)),F(comb(5,j)))
def cleared(qs,k,x,y,g0,g1):
 result={}
 for j in range(6):
  a,b=5-j,j
  moments=[masscleared(j),{},padd(pscale(masscleared(j,0,1),a*x),pscale(masscleared(j,1,0),b*y)),padd(pscale(masscleared(j,0,1),a*x*g0),pscale(masscleared(j,1,0),b*y*g1))]
  m4=padd(pscale(masscleared(j,0,1),a*x*g0*g0),pscale(masscleared(j,1,0),b*y*g1*g1))
  sq=padd(pscale(masscleared(j,0,2),a*a*x*x),pscale(masscleared(j,2,0),b*b*y*y))
  sq=padd(sq,pscale(masscleared(j,1,1),2*a*b*x*y));moments.append(padd(m4,pscale(sq,F(12,5))))
  shift={(0,0):F(j-k),(0,1):-F(1)}
  for r,c in enumerate(qs[j]):
   for i in range(r+1):result=padd(result,pscale(pmul(ppow(shift,r-i),moments[i]),c*comb(r,i)))
 return result

def direct(qs,k,x,y,g0,g1,p,u):
 q=1-p;result=F(0)
 for j in range(6):
  a,b=5-j,j;t=a*x/q+b*y/p
  ms=[F(1),F(0),t,a*g0*x/q+b*g1*y/p,a*g0*g0*x/q+b*g1*g1*y/p+F(12,5)*t*t]
  val=sum(qs[j][r]*comb(r,i)*(j-k-u)**(r-i)*ms[i]for r in range(5)for i in range(r+1))
  result+=comb(5,j)*p**j*q**(5-j)*val
 return result*(p*q)**2

def run(obj):
 d.accept(obj);cfg=obj['all_original_hypotheses'];lo,hi=map(F,obj['derived']['h'])
 intervals=sorted((F(z['phase'][0])+z['nearest_k'],F(z['phase'][1])+z['nearest_k'])for z in obj['signed_phase_roots'])
 cursor=lo
 for a,b in intervals:d.need(a<=cursor and b>=a,'no missing closed threshold interval');cursor=max(cursor,b)
 d.need(cursor==hi,'exact right threshold endpoint')
 htests=sorted({lo,hi,F(1),F(3,2),F(2),F(5,2),F(3),*[lo+(hi-lo)*F(i,32)for i in range(33)]})
 for h in htests:
  selected=[z for z in obj['signed_phase_roots']if F(z['phase'][0])<=h-z['nearest_k']<=F(z['phase'][1])]
  d.need(selected,'closed root exists');d.need(all(abs(h-z['nearest_k'])<=F(1,2)for z in selected),'nearest relation')
 for h,ks in [(F(3,2),{1,2}),(F(5,2),{2,3})]:
  got={z['nearest_k']for z in obj['signed_phase_roots']if F(z['phase'][0])<=h-z['nearest_k']<=F(z['phase'][1])}
  d.need(got==ks,'both atom/tie faces retained')
 for h in [F(-1),F(6)]:d.need(not any(F(z['phase'][0])<=h-z['nearest_k']<=F(z['phase'][1])for z in obj['signed_phase_roots']),'unlicensed outer thresholds not pretended covered')
 # Independent coordinate/mean identities on a rational grid in p,H,scale.
 coordinate=0
 for p,H,scale in product([F(19,50),F(77,200),F(39,100)],[-F(cfg['Hminus']),F(-1),F(0),F(1),F(cfg['Hplus'])],[F(1,3),F(1,2),F(cfg['acquired_scale_upper'])]):
  h=5*p+scale*H;d.need(lo<=h<=hi,'raw threshold enclosure');d.need((h-5*p)/scale==H,'raw coordinate inverse');coordinate+=1
 # Exact same-marginal convolutions, including zero atom and zero noise.
 lawsets=[({F(0):F(1)},{F(0):F(1)}),
  ({F(-1,10):F(1,2),F(1,10):F(1,2)},{F(0):F(1)}),
  ({F(-1,10):F(3,5),F(3,20):F(2,5)},{F(-1,20):F(1,2),F(1,20):F(1,2)}),
  ({F(-77,200):F(1,2),F(77,200):F(1,2)},{F(0):F(1)})]
 mixture_checks=reflection_checks=collisions=0;p=F(77,200);q=1-p
 for u0,u1 in lawsets:
  d.need(sum(x*v for x,v in u0.items())==sum(x*v for x,v in u1.items())==0,'centered classes')
  ylaw=defaultdict(F)
  for x,v in u0.items():ylaw[x]+=q*v
  for x,v in u1.items():ylaw[1+x]+=p*v
  total=powerlaw(dict(ylaw),5)
  components=[conv(powerlaw(u0,5-j),powerlaw(u1,j))for j in range(6)]
  for h in sorted(set(total)|{lo,hi,F(-5),F(8),F(3,2),F(5,2)}):
   actual=cdf(total,h);mix=sum(F(comb(5,j))*p**j*q**(5-j)*cdf(components[j],h-j)for j in range(6))
   d.need(actual==mix,'entire common-marginal mixture identity');mixture_checks+=1
   refl={-x:v for x,v in total.items()};d.need(1-actual==cdf(refl,-h,False),'strict reflection identity');reflection_checks+=1
   if h in total:
    d.need(cdf(refl,-h)-cdf(refl,-h,False)==total[h],'closed reflection atom correction');collisions+=1
   for k in [1,2,3]:
    u=h-k;d.need(all(cdf(components[j],h-j)==cdf(components[j],u+k-j)for j in range(6)),'phase shift identity')
 vertices=[tuple(map(F,z))for z in obj['outer_polygon']['vertices']]
 r0,r1=map(F,obj['outer_polygon']['inward_caps']);a0,a1=F(cfg['outer0']),F(cfg['outer1'])
 gammas=list(product([-a0,F(0),r0],[a1,F(0),-r1]));qs=[[F((j+1)*(i+2),20)for i in range(5)]for j in range(6)]
 polynomials=identities=0;maxdegree=[0,0]
 for k,(x,y),(g0,g1)in product([1,2,3],vertices,gammas):
  poly=cleared(qs,k,x,y,g0,g1);degree=(max(a for a,b in poly),max(b for a,b in poly));d.need(degree[0]<=9 and degree[1]<=4,'proved degree envelope');polynomials+=1
  maxdegree=[max(maxdegree[i],degree[i])for i in range(2)]
  for p,u in product([F(19,50),F(77,200),F(39,100)],[-F(1,2),F(0),F(1,2)]):
   d.need(peval(poly,p,u)==direct(qs,k,x,y,g0,g1,p,u),'independent cleared expectation identity');identities+=1
 # Test the beta identity using actual centered class pairs on an independent p grid.
 beta_checks=0
 for p,(u0,u1)in product([F(19,50),F(77,200),F(39,100)],lawsets[:3]):
  q=1-p;s0=sum(x*x*v for x,v in u0.items());s1=sum(x*x*v for x,v in u1.items());x=q*s0;y=p*s1;w=p*q+x+y
  beta=(q*sum((z-p)*abs(z-p)*v for z,v in u0.items())+p*sum((q+z)*abs(q+z)*v for z,v in u1.items()))/w
  d.need(beta==(p*q*(q-p)-x+y)/w,'same-law signed beta');beta_checks+=1
 return {'threshold_test_points':len(htests),'coordinate_checks':coordinate,'mixture_checks':mixture_checks,'reflection_checks':reflection_checks,'atom_collisions':collisions,'beta_actual_laws':beta_checks,'degree_polynomials':polynomials,'independent_degree_identities':identities,'maximum_degree':maxdegree}

def controls(obj):
 bads=[]
 def add(name,fn):
  z=deepcopy(obj);fn(z);bads.append((name,z))
 add('missing signed root',lambda z:z['signed_phase_roots'].pop())
 add('duplicated root',lambda z:z['signed_phase_roots'].__setitem__(1,deepcopy(z['signed_phase_roots'][0])))
 add('reordered canonical roots',lambda z:z['signed_phase_roots'].reverse())
 add('nearest confused with mixture',lambda z:z['derived'].update(nearest_indices=list(range(6))))
 add('truncated mixture',lambda z:z['derived'].update(mixture_counts=[1,2,3]))
 add('wrong index',lambda z:z.update(n=6))
 add('boolean index',lambda z:z.update(n=True))
 add('omitted negative phase',lambda z:z['signed_phase_roots'][0]['phase'].__setitem__(0,'0'))
 add('open face',lambda z:z['signed_phase_roots'][0].update(closed=False))
 add('endpoint removed',lambda z:z['signed_phase_roots'][1]['phase'].__setitem__(1,'49/100'))
 add('changed target',lambda z:z.update(K='1'))
 add('changed p row',lambda z:z['all_original_hypotheses']['p'].__setitem__(0,'77/200'))
 add('weakened rho lower',lambda z:z['all_original_hypotheses'].update(rho_lower='1'))
 add('original affine Lambda replaced',lambda z:z['all_original_hypotheses'].update(Lambda=z['all_original_hypotheses']['acquired_lambda_upper']))
 add('wrong resource hash',lambda z:z['source'].update(resource_sha256='0'*64))
 add('hidden acquisition claim',lambda z:z['original_contract_flags'].update(resource_verified=True))
 add('missing beta plane',lambda z:z['outer_polygon']['planes'].pop())
 add('missing variance vertex',lambda z:z['outer_polygon']['vertices'].pop())
 add('normal standardized H confusion',lambda z:z['coordinate_identities'].update(bernoulli_threshold='h=n*p+sqrt(n*w)*H'))
 rejected=[]
 for name,z in bads:
  try:d.accept(z)
  except(ValueError,TypeError,KeyError):rejected.append(name)
  else:raise ValueError('mutant accepted '+name)
 try:json.loads('{"n":5,"n":6}',object_pairs_hook=d.unique)
 except ValueError:rejected.append('duplicate JSON key')
 else:raise ValueError('duplicate key accepted')
 return rejected
if __name__=='__main__':
 d.need(__debug__ and not sys.flags.optimize,'unoptimized process');out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
 pins={str(p):d.sha(p)for p in [HERE/'domain.py',HERE/'domain.json',Path(__file__)]}
 obj=d.load(HERE/'domain.json');stats=run(obj);rejected=controls(obj)
 d.need(all(d.sha(Path(p))==h for p,h in pins.items()),'unchanged sources')
 result={'status':'PASS_EXACT_SOURCE_BOUND_DOMAIN_AND_ALGEBRA_CONTROLS','mathematical_status':'Conditional domain and moment-polynomial implication independently derived; no score certificate or complete row acceptance.',
  'execution_status':'Fresh exact rational census, endpoint/atom/convolution controls, polynomial identities and metadata rejections.',
  'statistics':stats,'negative_controls':rejected,'source_pins':pins,'domain_sha256':d.sha(HERE/'domain.json'),'full_row_score_claimed':False}
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'result_sha256':d.sha(out/'RESULT.json'),'statistics':stats,'negative_controls':len(rejected)}))

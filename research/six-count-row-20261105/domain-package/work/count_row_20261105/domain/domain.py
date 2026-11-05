"""Exact domain projection for one original acquired n5 BN row. No score proof."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import comb
import hashlib,json,sys
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
CONTRACT='work/cutoff5_20261020/root/count5_prepare_v1/gamma16_01/n5/BN/panel038/contract.json'
CONTRACT_SHA='2b3f626ba3a9e954e4700bf206cf7a364f44958bb901b463198249dda2f37e48'
BASE=Path(CONTRACT).parent
SOURCE_PATHS=[CONTRACT,
 'work/cutoff5_20261020/root/signed_gamma_paired5_v1/BN/panel038.json',
 *[str(BASE/x) for x in ['contract_helpers.py','mean_noise.py','generalized_scope.py','exact35_core.py']],
 'work/cutoff5_20261020/audit/count5_readback_v1/common.py',
 'work/cutoff5_20261020/audit/count5_readback_v1/check.py',
 'work/cutoff5_20261020/audit/resource5_readback_v4/BN_READBACK.json',
 'work/cutoff5_20261020/audit/count5_readback_v1/n5_BN_COMPLETE.json']
def need(ok,msg):
 if not ok: raise ValueError(msg)
def unique(pairs):
 d={}
 for k,v in pairs:need(k not in d,'duplicate key');d[k]=v
 return d
def load(p):return json.loads(p.read_text(),object_pairs_hook=unique)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)
def up(z,scale=10**6):z=F(z);return F(-((-z.numerator*scale)//z.denominator),scale)
def down(z,scale=10**6):z=F(z);return F(z.numerator*scale//z.denominator,scale)
def bernstein3(poly,l,h):
 # Exact affine substitution, then degree3 power-to-Bernstein conversion.
 a=[sum(poly[j]*F(comb(j,i))*l**(j-i)*(h-l)**i for j in range(i,4)) for i in range(4)]
 return [sum(a[i]*F(comb(k,i),comb(3,i)) for i in range(k+1)) for k in range(4)]
def outer_polygon(cfg,l,h):
 bl,bh=map(F,cfg['acquired_beta']);cap=F(cfg['acquired_lambda_upper'])/cfg['n']
 upper=(F(0),bh-1,3-bh,F(-2));lower=(F(0),1-bl,bl-3,F(2))
 bs=[bernstein3(poly,l,h) for poly in (upper,lower)]
 planes=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),cap),
         (-(1+bh),1-bh,max(bs[0])),(1+bl,-(1-bl),max(bs[1]))]
 vertices=set()
 for a,b in combinations(planes,2):
  det=a[0]*b[1]-a[1]*b[0]
  if not det:continue
  x=(a[2]*b[1]-a[1]*b[2])/det;y=(a[0]*b[2]-a[2]*b[0])/det
  if all(A*x+B*y<=C for A,B,C in planes):vertices.add((x,y))
 need(len(vertices)>=3,'nondegenerate compact outer polygon')
 return {'planes':[[str(t) for t in z]for z in planes],
  'beta_rhs_bernstein':[[str(t)for t in z]for z in bs],
  'vertices':[[str(t)for t in z]for z in sorted(vertices)],
  'inward_caps':[str(min(F(cfg['acquired_inward_upper']),h)),str(min(F(cfg['acquired_inward_upper']),1-l))],
  'scope':'Fixed rational outer polygon and fixed inward endpoints on this p cell; includes every actual same-law variance pair. Extra tuples may be unrealizable.'}
def expected():
 cp=ROOT/CONTRACT;need(sha(cp)==CONTRACT_SHA,'exact original contract')
 c=load(cp);need(type(c['n'])is int and c['n']==5 and c['band']=='BN' and c['index']==38 and len(c['rows'])==1,'literal row')
 cfg=c['rows'][0];need(c['resource_verified']is False and c['cutoff_proved']is False,'preserved conditional artifact meaning')
 r=load(ROOT/c['resource_path']);need(sha(ROOT/c['resource_path'])==c['resource_sha256'],'same selected resource bytes')
 raw=r['result']['raw_row'];original=r['result']['result'];seed=r['result']['initial']
 need(r['index']==38 and r['status']=='RESOURCE_ROW_DIAGNOSTIC' and r['result']['excluded']is False,'retained original source row')
 need(cfg['p']==[original['pl'],original['pu']]==[raw['pl'],raw['pu']]==['19/50','39/100'],'same full probability panel')
 need(original['N']==cfg['n']==5 and original['K']==cfg['K']=='0','actual index and target')
 need(cfg['rho_lower']=='11/10' and cfg['rho_upper']=='23/20','full original rho band')
 for src,dst in [('D','D'),('d0','d0'),('lambda_max','Lambda'),('H_minus','Hminus'),('H_plus','Hplus'),('radius_minus','radius_minus'),('radius_plus','radius_plus'),('outer0','outer0'),('outer1','outer1')]:
  need(F(cfg[dst])==up(original[src]),'source upper '+dst)
 for src,dst in [('charge_b','binary_charge'),('charge_g','gap_charge'),('charge_h','noise_charge')]:need(F(cfg[dst])==down(original[src]),'source charge '+dst)
 need(len(cfg['quadratics'])==len(original['quadratics'])==6,'all phase resource quadratics')
 for a,b in zip(cfg['quadratics'],original['quadratics']):
  for key in ['A','Fplus','Fminus','Qbudget']:need(F(a[key])==(down if key=='Qbudget'else up)(b[key]),'directed phase resource '+key)
 need(F(cfg['acquired_mean'][0])==down(seed['mean_lo']),'same-law mean floor')
 l,h=map(F,cfg['p']);n=cfg['n'];ml=F(cfg['acquired_mean'][0]);vl=l*(1-l);vh=h*(1-h)
 scale=F(cfg['acquired_scale_upper']);noise=F(cfg['acquired_lambda_upper'])
 exactscale=vh/ml; exactnoise=min(F(cfg['Lambda']),n*max(F(0),vl*vl/(ml*ml)-vl,vh*vh/(ml*ml)-vh))
 need(scale==up(exactscale) and noise==min(F(cfg['Lambda']),up(exactnoise)),'independent mean/variance projection')
 hm,hp=F(cfg['Hminus']),F(cfg['Hplus']);lo=n*l-scale*hm;hi=n*h+scale*hp
 need(F(1,2)<lo<1 and 3<hi<F(7,2),'proved nearest-index range')
 roots=[]
 for k in [1,2,3]:
  ul=max(-F(1,2),lo-k);uh=min(F(1,2),hi-k)
  for sign,a,b in [('minus',ul,min(F(0),uh)),('plus',max(F(0),ul),uh)]:
   need(a<=b,'nonempty signed root')
   roots.append({'id':f'k{k}.{sign}','nearest_k':k,'phase':[str(a),str(b)],'probability':cfg['p'],'noise':['0',str(noise)],'closed':True})
 acq=load(ROOT/SOURCE_PATHS[-2]);count=load(ROOT/SOURCE_PATHS[-1])
 need(acq['source_rows']['38']['path']==c['resource_path'] and acq['source_rows']['38']['sha256']==c['resource_sha256'],'historical acquisition selection')
 need(38 in acq['retained'] and 38 in count['retained'],'same historical retained panel')
 need(acq['n']==5 and acq['band']=='BN' and acq['N']==5 and acq['Q']==acq['K']=='0','historical acquisition scope')
 return {'schema':'SOURCE_BOUND_N5_BN_P38_THRESHOLD_DOMAIN_V1','n':5,'band':'BN','index':38,'K':'0',
  'mathematical_status':'Locally derived exact domain implication conditional on the original same-law acquired row; no quartic score or whole-row exclusion proved here.',
  'source':{'contract':CONTRACT,'sha256':CONTRACT_SHA,'resource':c['resource_path'],'resource_sha256':c['resource_sha256']},
  'original_contract_flags':{'resource_verified':False,'cutoff_proved':False},'all_original_hypotheses':cfg,
  'orientation':'Positive closed-event score for the original sign-conditioned marginal. Negative discrepancies require the separately oriented reflected row/attainment reduction.',
  'coordinate_identities':{'X':'(B+U-p)/sqrt(w)','w':'p*(1-p)+lambda/n','raw_sum_threshold':'H','normal_argument':'H/sqrt(n)=(k+u-n*p)/sqrt(n*w)','bernoulli_threshold':'h=n*p+sqrt(w)*H=k+u','mean':'m=p*(1-p)/sqrt(w)'},
  'derived':{'v':[str(vl),str(vh)],'exact_mean_scale_upper':str(exactscale),'scale_upper':str(scale),'exact_mean_noise_upper':str(exactnoise),'noise_upper':str(noise),'h':[str(lo),str(hi)],'nearest_indices':[1,2,3],'mixture_counts':list(range(6))},
  'signed_phase_roots':roots,'outer_polygon':outer_polygon(cfg,l,h),
  'source_pins':{p:{'bytes':(ROOT/p).stat().st_size,'sha256':sha(ROOT/p)}for p in SOURCE_PATHS},
  'remaining_obligations':['Exact global CDF majorants for all six mixture counts','Complete continuous p/phase/noise/common-moment score acceptance on the six declared roots or a proved complete subdivision','Retained original acquisition/contact/threshold premises; no new all-law n5 proof or automatic manuscript deletion']}
def accept(obj):
 want=expected();need(canonical(obj)==canonical(want),'exact complete source-bound domain');return want
if __name__=='__main__':
 need(__debug__ and not sys.flags.optimize,'no optimization');target=Path(sys.argv[1])
 with target.open('x')as f:json.dump(expected(),f,indent=2);f.write('\n')
 print(json.dumps({'status':'WRITTEN_EXACT_CONDITIONAL_DOMAIN','path':str(target),'sha256':sha(target)}))

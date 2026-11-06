"""Independent whole-band literal5 acquired-resource/count composition."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
from collections import Counter
import json,sys
import common as c
H=Path(__file__).resolve().parent;R=H.parents[3];N=R/'work/cutoff6_20261018'
W=R/'work/cutoff6_20261020';V=H.parent.parent;P=V/'root/count5_prepare_v1'
c.need(__debug__ and sys.dont_write_bytecode and not sys.flags.optimize,'ordinary-B')
c.need(len(sys.argv)==2 and sys.argv[1]in ['B0','BN'],'literal full band')
n=5;band=sys.argv[1];name=f'n5_{band}';dest=H/(name+'_COMPLETE.json')
c.need(not dest.exists(),'fresh case result')
for p in ['check.py','common.py','PROOF.txt','SOURCE_COPY.json','PORT.diff']:c.bind(H/p)
copy=c.load(H/'SOURCE_COPY.json',False);c.bind(R/copy['source'],copy['sha256'])
old=(R/copy['source']).read_text()
c.need((H/'common.py').read_text()==old.replace("type(n)is int and n in (7,8,9),'literal separately checked index7,8,9'","type(n)is int and n==5,'literal independently reviewed index5'"),'only two literal index guards ported')
nativepath=H.parent/f'resource5_readback_v4/{band}_READBACK.json';acq=c.load(nativepath)
c.need(acq['status']=='PASS_INDEPENDENT_LITERAL5_ACQUISITION_READBACK' and type(acq['n'])is int and acq['n']==5 and acq['band']==band,'literal full acquisition')
c.need(type(acq['N'])is int and acq['N']==5 and acq['Q']==acq['K']=='0','actual q0 acquired scope')
lo,hi=c.BANDS[band][:2];c.need(acq['rho_interval']==[lo,hi],'same complete rho band')
excluded,retained=acq['excluded'],acq['retained'];count_indices=retained
c.need(sorted(excluded+retained)==list(range(100))and len(set(excluded+retained))==100,'complete acquired partition')
full={'rows':[]}
for i in range(100):
 src=acq['source_rows'][str(i)];c.bind(R/src['path'],src['sha256']);row=c.load(R/src['path'],False)
 c.need(type(row['index'])is int and row['index']==i,'ordered literal source row')
 c.need(row['status']==('RESOURCE_EXCLUSION_DIAGNOSTIC'if i in excluded else'RESOURCE_ROW_DIAGNOSTIC'),'acquired decision')
 full['rows'].append(row)
for p,status in [('count5_port_review_v1/CHECKED.json','PASS_INDEPENDENT_LITERAL5_COUNT_PREPARER_SCOPE_REVIEW'),('count_kernel_analytic_review_v1/CHECKED.json','PASS_INDEPENDENT_COUNT_PROBABILITY_AND_FILTER_ANALYTIC_REVIEW')]:
 review=c.load(H.parent/p);c.need(review['status']==status,'reviewed literal count semantics')
port=c.load(W/'audit/b2_count_readback_v1/FAST_SCALAR_REVIEW.json')
c.need(port['status']=='PASS_INDEPENDENT_EXACT_SCALAR_FASTPATH_PORT','exact scalar kernel review');known=port['new_kernel_sha256']
for p in ['prepare.py','ports.py','PROOF.txt','SOURCE_PORT.diff','TEMPLATE_SOURCES.json']:c.bind(P/p)
jobs={}
for batch in ['pilots01','B0_BN_rest01','gamma16_01']:
 prep=c.load(P/batch/'PREPARED.json');dispatch=c.load(V/f'root/count5_dispatch_v1/{batch}/RESULT.json')
 c.need(prep['status']=='CONDITIONAL_ACTUAL5_FAST_MEAN_BATCH_PREPARED_NO_ACQUISITION' and dispatch['status']=='COMPLETE_LITERAL5_COUNT_ATTEMPTS' and dispatch['all_native_pass']is True and dispatch['prepared_sha256']==c.sha(P/batch/'PREPARED.json'),'exact completed prepared batch')
 c.need(len(prep['rows'])==len(dispatch['rows']),'all prepared attempts accounted')
 for job,done in zip(prep['rows'],dispatch['rows']):
  for key in ['n','band','index','capsule']:c.need(c.same(job[key],done[key]),'same completed count attempt')
  c.need(job['status']=='PREPARED_CONDITIONAL_FIXED_PANEL_NOT_EXECUTED' and done['status']=='PASS_NATIVE_CONDITIONAL_COUNT','all native counts accepted')
  c.need(type(job['n'])is int and job['n']==5 and type(job['index'])is int,'literal job identity')
  if job['band']!=band:continue
  index=job['index'];c.need(index not in jobs,'no duplicate selected count capsule')
  expected=acq['source_rows'][str(index)]
  c.need(job['source']['path']==expected['path']and job['source']['sha256']==expected['sha256'],'exact independently acquired source selection')
  jobs[index]=(batch,job)
c.need(sorted(jobs)==retained,'all and only acquired retained panels have count proofs')
S=N/'fourier/count6_gamma_pilot_v2/BN';template=(S/'count_protocol.py').read_text()
c.bind(S/'count_protocol.py');c.bind(S/'contract.json')
fast=W/'high/panel035_fastcap_v1';ctor=(fast/'construct.py').read_text();c.bind(fast/'construct.py')
def replace_once(s,a,b,times=1):
 c.need(s.count(a)==times,'exact reviewed source port '+a);return s.replace(a,b)
def protocol_source(d,cfg,index):
 s=replace_once(template,"CONTRACT_SHA='"+c.sha(S/'contract.json')+"'","CONTRACT_SHA='"+c.sha(d/'contract.json')+"'")
 for a,b in [('LIMIT=10000','LIMIT=50000'),('time.time()-began<=300','time.time()-began<=1200'),
             ("cfg['n']==6",f"cfg['n']=={n}"),("cfg['index']==42",f"cfg['index']=={index}"),
             ("cfg['p']==['21/50', '43/100']","cfg['p']=="+repr(cfg['p'])),
             ("F(cfg['rho_lower'])==F('11/10') and F(cfg['rho_upper'])==F('23/20')",
              "F(cfg['rho_lower'])==F('"+cfg['rho_lower']+"') and F(cfg['rho_upper'])==F('"+cfg['rho_upper']+"')")]:
  s=replace_once(s,a,b)
 s=replace_once(s,'n=6,index=42',f'n={n},index={index}',2)
 s=s.replace('actual6 BN geometry sharp panel42',f'actual{n} {band} gamma sharp panel{index}')
 s=replace_once(s,'range(7)',f'range({n+1})')
 s=replace_once(s,'len(roots)==7',f'len(roots)=={n+1}').replace('all nearest counts0 through6',f'all nearest counts0 through{n}')
 s=s.replace('ACTUAL6_GAMMA_SHARP_BN_P42_',f'ACTUAL{n}_GAMMA_SHARP_{band}_P{index}_').replace('ACTUAL6_GAMMA_SHARP_BN_JOINT_COUNT42',f'ACTUAL{n}_GAMMA_SHARP_{band}_JOINT_PANEL{index}')
 s=s.replace('COUNT42_FOREST.json','COUNT_FOREST.json').replace('COUNT42_ACCEPTED.json','COUNT_ACCEPTED.json')
 c.need((d/'count_protocol.py').read_text()==s,'complete source-specific acceptor port equality')
 c.need((d/'construct.py').read_text()==replace_once(ctor,'range(7)',f'range({n+1})'),'same fast constructor with literal n+1 roots')
 for file in ['count_protocol.py','construct.py']:c.bind(d/file)
def identity(row,index):
 c.need(type(row['index'])is int and row['index']==index and row['status']=='RESOURCE_ROW_DIAGNOSTIC' and c.same(row,full['rows'][index]),'entire acquired exact same-law resource row')
summaries=[];sources={};target=F('76824784444199314310731654405729617052063596250011448874609/187500000000000000000000000000000000000000000000000000000000')
c.need(F(4097,10000)<target<c.CElo,'same original sharp lower enclosure strictly below independently enclosed C_E')
for index in count_indices:
 batch,job=jobs[index];d=R/job['capsule']
 c.need(d==P/batch/f'n5/{band}/panel{index:03d}','literal count capsule')
 obj=c.load(d/'contract.json',False);cfg=obj['rows'][0]
 c.need(len(obj['rows'])==1 and type(obj['n'])is int and obj['n']==n and obj['band']==band and type(obj['index'])is int and obj['index']==index and obj['resource_verified']is False and obj['cutoff_proved']is False,'literal conditional native contract')
 row=c.load(R/obj['resource_path'],False)
 c.need(obj['resource_path']==job['source']['path'] and obj['resource_sha256']==job['source']['sha256']==c.sha(R/obj['resource_path']),'same exact source identity')
 identity(row,index);c.interface(row,cfg,band,index,n)
 raw=row['result']['raw_row'];r=row['result']['result']
 c.need(list(map(F,cfg['acquired_gamma']))==[c.floorgrid(raw['gamma_lo'],10**6),c.ceilgrid(raw['gamma_hi'],10**6)],'entire signed gamma interval')
 SL=F(3162277660,10**9);rl,D,gh,mu=map(F,[r['rho_lo'],r['D'],raw['gamma_hi'],raw['mean_hi']])
 price=max((SL-1)*rl,SL*rl-gh)-D
 c.need(SL*SL<10 and price>0 and mu>0,'positive same-law physical gap price')
 gap=max(F(raw['A'])+F(raw['B']),c.sqrtlo(max(F(0),2*rl-2*D/(SL-1),2*price/(3*mu)),10**12))
 pl,pu=map(F,cfg['p']);U=c.ceilgrid(1-gap*c.sqrtlo(min(pl*(1-pl),pu*(1-pu)),10**12),10**6)
 c.need(F(cfg['geometry_gap_lower'])==gap and F(cfg['acquired_inward_upper'])==U,'independently derived physical inward cap')
 c.need(F(r['rho_hi'])<=F(cfg['rho_upper'])<=F(hi),'entire acquired rho scope covered')
 protocol_source(d,cfg,index)
 f=c.load(d/'COUNT_FOREST.json',False);a=c.load(d/'COUNT_ACCEPTED.json',False)
 manifest=c.load(d/'KERNEL_COPY_MANIFEST.json',False)['files'];c.need(c.same(manifest,known),'whole reviewed n-general mathematical kernel')
 for file,digest in manifest.items():c.bind(d/file,digest)
 c.need(f['schema']==f'ACTUAL{n}_GAMMA_SHARP_{band}_P{index}_FRESH_COMPENSATED_RESOURCE_JOINT_CLOSED_COUNT_FOREST_V1' and f['target']==str(target),'fixed literal count and original sharp target')
 c.need(a['status']==f'PASS_FRESH_CONDITIONAL_ACTUAL{n}_GAMMA_SHARP_{band}_JOINT_PANEL{index}' and type(a['n'])is int and a['n']==n and type(a['index'])is int and a['index']==index,'same-index native acceptance')
 c.need(a['forest_sha256']==c.sha(d/'COUNT_FOREST.json') and a['contract_sha256']==f['contract_sha256']==c.sha(d/'contract.json') and a['checker_sha256']==f['checker_sha256']==c.sha(d/'count_protocol.py') and a['kernel_sha256']==f['kernel_sha256']==manifest,'entire exact native proof/runtime binding')
 stats=c.geometry(f,cfg,n);c.need(c.same(stats,a['statistics']) and a['fresh_leaf_evaluations']==stats['leaves'],'all n+1 roots and fresh native leaf census')
 c.need(len(a['negative_controls'])==len(set(a['negative_controls']))==24,'all native controls')
 construction=c.load(d/'CONSTRUCTION_RUN.json',False)
 c.need(construction['status']=='STORED_CONDITIONAL_FOREST_CONSTRUCTED_NOT_ACCEPTED' and construction['forest_sha256']==c.sha(d/'COUNT_FOREST.json') and construction['visited']==stats['nodes'],'complete stored original forest')
 for action,result in [('construct',construction),('accept',a)]:
  cap=R/f'runs/cutoff5_20261020/root/{batch}_{band}_{index:03d}_{action}';m=c.capture(cap)
  c.need(m['cwd']==str(d) and m['command'][1:]==(['-B','construct.py']if action=='construct'else['-B','count_protocol.py','accept']),'actual fixed native invocation')
  c.need(c.same(c.read(cap/'stdout.txt'),result),'whole native result capture')
  for file,digest in m['input_sha256'].items():c.bind(d/file,digest)
  if action=='accept':c.need(m['input_sha256']['COUNT_FOREST.json']==a['forest_sha256'],'fresh replay consumed exact proof')
 def leaf(z):
  v=z['roots'][0]['tree']
  while v['kind']=='split':v=v['left']
  return v
 mutations=[('missing root',lambda z:z['roots'].pop()),('duplicated root',lambda z:z['roots'].__setitem__(1,deepcopy(z['roots'][0]))),
  ('reordered roots',lambda z:z['roots'].reverse()),('boolean n',lambda z:z.update(n=True)),('wrong n',lambda z:z.update(n=10)),
  ('inflated target',lambda z:z.update(target='1')),('changed leaf box',lambda z:leaf(z)['box'][0].__setitem__(0,'0')),
  ('false decision',lambda z:leaf(z).update(decision='EMPTY_FAKE'))]
 for label,change in mutations:
  bad=deepcopy(f);change(bad);c.reject(lambda:c.geometry(bad,cfg,n),label)
 for label,change in [('wrong resource index',lambda z:z.update(index=99)),('changed seed',lambda z:z['result']['initial'].update(D='0')),('changed shared budget',lambda z:z['result']['result'].update(d0='0')),('missing history',lambda z:z['result']['history'].clear())]:
  bad=deepcopy(row);change(bad);c.reject(lambda:identity(bad,index),label)
 for label,change in [('replaced original Lambda',lambda z:z.update(Lambda='0')),('false physical scale',lambda z:z.update(acquired_scale_upper='0')),('omitted phase quadratic',lambda z:z['quadratics'].pop()),('wrong acquired mean',lambda z:z['acquired_mean'].__setitem__(0,'0'))]:
  bad=deepcopy(cfg);change(bad);c.reject(lambda:c.interface(row,bad,band,index,n),label)
 summaries.append(dict(index=index,p=cfg['p'],target=str(target),capsule=str(d.relative_to(R)),**stats))
 sources[index]=dict(capsule=str(d.relative_to(R)),contract_sha256=c.sha(d/'contract.json'),forest_sha256=c.sha(d/'COUNT_FOREST.json'),acceptance_sha256=c.sha(d/'COUNT_ACCEPTED.json'))
cover=dict(schema='CONDITIONAL_LITERAL5_CLOSED_100_PANEL_COVER_V1',n=n,band=band,rho=[lo,hi],target=str(target),rows=[])
for j in range(100):
 row=dict(index=j,p=[str(F(j,100)),str(F(j+1,100))],closure='resource'if j in excluded else'count')
 if j in retained:row['source']=sources[j]
 cover['rows'].append(row)
def validate(z):
 c.need(type(z)is dict and set(z)=={'schema','n','band','rho','target','rows'} and z['schema']=='CONDITIONAL_LITERAL5_CLOSED_100_PANEL_COVER_V1','exact complete cover schema')
 c.need(type(z['n'])is int and z['n']==n and z['band']==band and z['rho']==[lo,hi] and z['target']==str(target),'unchanged literal complete band/target')
 c.need(type(z['rows'])is list and len(z['rows'])==100,'complete100-panel cover')
 previous=F(0);census=Counter()
 for j,row in enumerate(z['rows']):
  c.need(type(row['index'])is int and row['index']==j and row['p']==[str(F(j,100)),str(F(j+1,100))] and F(row['p'][0])==previous,'ordered exact closed seams')
  previous=F(row['p'][1]);census[row['closure']]+=1
  if j in excluded:c.need(set(row)=={'index','p','closure'} and row['closure']=='resource','only acquired resource exclusions')
  else:c.need(set(row)=={'index','p','closure','source'} and row['closure']=='count' and c.same(row['source'],sources[j]),'exact acquired count closure')
 c.need(previous==1 and census['resource']==len(excluded) and census['count']==len(retained),'whole closed probability cover')
 return dict(census)
census=validate(cover)
changes=[('missing panel',lambda z:z['rows'].pop()),('duplicated panel',lambda z:z['rows'].__setitem__(1,deepcopy(z['rows'][0]))),
 ('reordered panels',lambda z:z['rows'].reverse()),('boolean cover index',lambda z:z.update(n=True)),('wrong cover index',lambda z:z.update(n=6)),
 ('wrong band',lambda z:z.update(band='other')),('widened rho',lambda z:z.update(rho=['1','6/5'])),
 ('inflated cover target',lambda z:z.update(target='1')),('open seam',lambda z:z['rows'][1]['p'].__setitem__(0,'11/1000')),
 ('omitted endpoint',lambda z:z['rows'][99]['p'].__setitem__(1,'999/1000')),('false cutoff claim',lambda z:z.update(cutoff_proved=True))]
if retained:changes.extend([('unproved resource exclusion',lambda z:z['rows'][retained[0]].update(closure='resource')),('wrong count source',lambda z:z['rows'][retained[0]]['source'].update(contract_sha256='0'*64))])
for label,change in changes:
 bad=deepcopy(cover);change(bad);c.reject(lambda:validate(bad),label)
c.reject(lambda:json.loads('{"n":7,"n":8}',object_pairs_hook=c.unique),'duplicate JSON key')
c.reject(lambda:c.merge({str(nativepath.relative_to(R)):'0'*64}),'corrupted acquisition digest')
c.need(all(c.sha(R/path)==digest for path,digest in c.G.items()),'unchanged whole source graph')
out=dict(status='PASS_COMPLETE_CONDITIONAL_LITERAL5_100_PANEL_EXCLUSION',n=n,band=band,rho=[lo,hi],
 mathematical_status='Conditional on attained contact, adopted C4<=CE input, acquired support/Fourier/INITIAL/resources, and reviewed count inequalities. Complete named literal n/band exclusion; other rho bands and complement remain separate.',
 execution_status='Complete100-panel exact acquired partition and all n+1 original count roots independently reconstructed and joined to source-bound native fresh leaf replays.',
 excluded=excluded,retained=retained,census=census,count_roots=len(retained)*(n+1),count_totals={k:sum(z[k]for z in summaries)for k in ['nodes','leaves']},
 maximum_count_score=str(max([F(z['maximum_score'])for z in summaries],default=F(0))),original_count_target=str(target),
 coverage=cover,count_panels=summaries,independent_mutations=dict(c.controls),native_count_mutations=24*len(retained),cutoff_proved=False,files_sha256=c.G)
with dest.open('x')as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items()if k not in ['files_sha256','coverage','count_panels']},indent=2))

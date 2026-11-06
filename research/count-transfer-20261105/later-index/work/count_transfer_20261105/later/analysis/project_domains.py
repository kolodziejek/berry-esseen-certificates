"""Read-only exact source/domain projection; no acquisition replay."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt,ceil,floor
import json,hashlib,sys
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rootup(x):
 g=10**12;k=isqrt(x.numerator*g*g//x.denominator);a=F(k+1,g);need((a-F(1,g))**2<=x<a*a,'outward root');return a
def main():
 need(__debug__ and not sys.flags.optimize,'ordinary Python');out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
 registry=ROOT/'work/unconditional_legacy_20261030/verification/count/count-pack-v2/MANIFEST.json'
 need(sha(registry)=='f5ddd40aefe85b5ce036b2c23fe540c2032997bf8a51f4999a08573e9a4c34f7','fixed public source registry')
 jobs=json.loads(registry.read_text())['jobs'];records=[];pins={str(registry.relative_to(ROOT)):sha(registry)}
 join6=ROOT/'runs/extension_20261030/foundations/finite69-final-join01/CURRENT_INTERFACES.json'
 join39=ROOT/'work/extension_20261030/finite/actual3539-full-join20261104/RESULT.json'
 six=json.loads(join6.read_text());later=json.loads(join39.read_text())
 for path in [join6,join39]:pins[str(path.relative_to(ROOT))]=sha(path)
 for n,key in [(6,'n6.BN.p38'),(39,'n39.strict.dce5d64054154a1a')]:
  r=jobs[key];p=HERE.parent/'selected'/key/'contract.json';need(sha(p)==r['source']['contract.json']['sha256'],'source-selected contract')
  obj=json.loads(p.read_text());rows=[x for x in obj['rows']if x['index']==38];need(len(rows)==1,'unique selected table row');row=rows[0]
  need(row['n']==obj['n']==n and F(row.get('K',obj.get('K','-1')))==0 and row['p']==['19/50','39/100'],'fixed actual sharp row')
  if n==6:
   edge=next(e for e in six['count_interfaces']if(e['n'],e['band'],e['index'])==(6,'BN',38));need(edge['contract_sha256']==sha(p)and edge['whole_native_domain']is True,'selected same-law n6 interface')
   need(obj['resource_path']==edge['resource_path']and obj['resource_sha256']==edge['resource_sha256'],'same acquired resource')
   acquisition=ROOT/'work/extension_20261030/foundations/finite69-cache-remaining01'/obj['resource_path'];need(sha(acquisition)==obj['resource_sha256'],'original n6 resource bytes')
   scale=F(row['acquired_scale_upper']);noise=F(row['acquired_lambda_upper']);rho=[row['rho_lower'],row['rho_upper']]
  else:
   band=next(b for b in later['bands']if b['n']==39);e=next(e for e in band['panels']if e['index']==38);edge=e['count']
   need(edge['job_id']==key and edge['contract_sha256']==sha(p)and edge['contract']==obj and e['source_role']=='n39-resource','actual39 selected table-row join')
   acquisition=ROOT/'work/extension_20261030/finite/resource35_39-run01/capsule/work/below40_20261007/relative/bridge39_exact/acquisition/acquisition_proof.json'
   need(sha(acquisition)==later['proof_sha256']['n39-resource'],'actual original39 acquisition binding')
   noise=F(row['Lambda']);scale=rootup(F(39,100)*F(61,100)+noise/n);rho=['1','6/5']
  pins[str(acquisition.relative_to(ROOT))]=sha(acquisition);pins[str(p.relative_to(ROOT))]=sha(p)
  pl,pu=map(F,row['p']);lo=n*pl-F(row['Hminus'])*scale;hi=n*pu+F(row['Hplus'])*scale
  krange=list(range(ceil(lo-F(1,2)),floor(hi+F(1,2))+1));roots=[]
  for k in krange:roots.append({'k':k,'phase':[str(max(-F(1,2),lo-k)),str(min(F(1,2),hi-k))]})
  need(min(krange)>=0 and max(krange)<=n,'unclamped threshold coverage')
  probes={lo,hi}
  for k in krange:
   for z in[F(k)-F(1,2),F(k),F(k)+F(1,2)]:
    if lo<=z<=hi:probes.add(z)
  for z in probes:need(any(F(e['phase'][0])<=z-e['k']<=F(e['phase'][1])for e in roots),'all faces/atoms covered')
  records.append({'job_id':key,'actual_n':n,'K':'0','target':'C_E','rho_region':rho,'row':row,'contract_schema':obj.get('schema',obj.get('status')),
   'contract_source':r['original_source_paths']['contract.json'],'contract_local':str(p.relative_to(ROOT)),'contract_sha256':sha(p),
   'acquisition':str(acquisition.relative_to(ROOT)),'source_bound_selected_join':str((join6 if n==6 else join39).relative_to(ROOT)),
   'scale_upper':str(scale),'noise_upper':str(noise),'unclamped_bernoulli_threshold':[str(lo),str(hi)],'closed_nearest_roots':roots,'atom_endpoint_probes':len(probes),
   'mixture_counts':list(range(n+1)),'p_degree_after_pq_squared':n+4,'phase_degree':4,'numerical_acquisition_replayed':False})
 result={'status':'PASS_EXACT_SELECTED_SOURCE_DOMAIN_PROJECTION','scope':'Metadata and mathematical domain projection only; historical selected joins are located and byte-bound, not re-executed here.','rows':records,'source_pins':pins,'script_sha256':sha(__file__)}
 (out/'DOMAIN.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'domains':[{k:r[k]for k in ['job_id','unclamped_bernoulli_threshold','closed_nearest_roots','atom_endpoint_probes']}for r in records]}))
if __name__=='__main__':main()

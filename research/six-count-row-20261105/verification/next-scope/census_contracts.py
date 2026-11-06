"""Read-only field/domain census, not a new certificate campaign."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
SELECTION='work/cutoff5_20261020/root/final_composition_v2/C5_CHECKED.json'
PICKS=[
 'work/cutoff5_20261020/root/count5_prepare_v1/gamma16_01/n5/BN/panel039/contract.json',
 'work/cutoff5_20261020/root/count5_prepare_v1/pilots01/n5/B0/panel050/contract.json',
 'work/cutoff5_20261020/root/count5_prepare_v4/B2_S3_endpoint02/n5/B2/panel034/contract.json']
def need(x,m):
    if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unique(ps):
    d={}
    for k,v in ps:need(k not in d,'duplicate key');d[k]=v
    return d
def main(out):
    before={};rows=[]
    def read(rel,pin=None):
        p=ROOT/rel;need(not p.is_symlink(),'ordinary source');h=sha(p);need(pin is None or h==pin,'source pin '+rel)
        before[rel]=h;return json.loads(p.read_text(),object_pairs_hook=unique)
    sel=read(SELECTION)
    for rel,pin in sorted(sel['files_sha256'].items()):
      if '/n5/' not in rel or not rel.endswith('/contract.json'):continue
      doc=read(rel,pin);need(len(doc['rows'])==1,'single original row');r=doc['rows'][0]
      ap=str(Path(rel).parent/'COUNT_ACCEPTED.json');acc=read(ap,sel['files_sha256'][ap])
      pl,pu=map(F,r['p']);hu=F(r['acquired_scale_upper'])
      hlo=5*pl-F(r['Hminus'])*hu;hhi=5*pu+F(r['Hplus'])*hu
      low=hlo-F(1,2);high=hhi+F(1,2)
      kmin=-((-low.numerator)//low.denominator);kmax=high.numerator//high.denominator
      need(0<=kmin<=kmax<=5,'raw threshold roots contained without clamping')
      rows.append(dict(path=rel,sha256=pin,band=doc['band'],index=doc['index'],row=r,
        old_leaves=acc['statistics']['leaves'],old_receipt=ap,old_receipt_sha256=sel['files_sha256'][ap],
        resource_verified=doc.get('resource_verified'),cutoff_proved=doc.get('cutoff_proved'),
        outer_threshold=[str(hlo),str(hhi)],nearest_roots=list(range(kmin,kmax+1))))
    need(len(rows)==295,'exact selected forest census')
    keys={tuple(sorted(x['row'])) for x in rows};need(len(keys)==1,'same field set')
    required={'p','rho_lower','rho_upper','outer0','outer1','acquired_lambda_upper','acquired_beta','acquired_mean',
      'acquired_scale_upper','acquired_gamma','acquired_inward_upper','sign_premise','Hminus','Hplus'}
    need(required<=set(next(iter(keys))),'all proposed common fields')
    need(all(x['row']['n']==5 and x['row']['K']=='0' for x in rows),'literal index and target')
    signs=[x['row']['sign_premise'] for x in rows]
    need(all(z['schema']=='ACTUAL_SIGN_CONDITIONED_MARGINAL_V1' and z['conditional_means_zero'] is True for z in signs),'same sign-law convention')
    need(all(F(z['negative_endpoint_lower'])>0 and F(z['positive_endpoint_lower'])>0 for z in signs),'strict sign gaps')
    bands={}
    for band in sorted(set(x['band']for x in rows)):
        rs=[x for x in rows if x['band']==band]
        bands[band]=dict(contracts=len(rs),probability_min=str(min(F(x['row']['p'][0])for x in rs)),
          probability_max=str(max(F(x['row']['p'][1])for x in rs)),
          rho_domains=sorted({tuple((x['row']['rho_lower'],x['row']['rho_upper']))for x in rs},key=lambda z:(F(z[0]),F(z[1]))))
    summary=dict(status='PASS_READ_ONLY_SOURCE_DOMAIN_CENSUS',mathematical_scope='Original selected contract field and threshold-domain census only; no COUNT, resource or acquisition arithmetic replay.',
      contracts=len(rows),remaining_after_BN38=294,bands=bands,shared_fields=list(next(iter(keys))),
      at_or_left_half=sum(F(x['row']['p'][1])<=F(1,2) for x in rows),at_or_right_half=sum(F(x['row']['p'][0])>=F(1,2) for x in rows),
      interior_crosses_half=sum(F(x['row']['p'][0])<F(1,2)<F(x['row']['p'][1]) for x in rows),
      positive_sign_gaps=len(rows),conditional_zero_means=len(rows),
      strict_inward_lt_one=sum(0<F(x['row']['acquired_inward_upper'])<1 for x in rows),
      strict_min_pq_inward=sum(F(x['row']['acquired_inward_upper'])<min(F(x['row']['p'][0]),1-F(x['row']['p'][1])) for x in rows),
      nearest_root_censuses=dict(Counter(','.join(map(str,x['nearest_roots']))for x in rows)),
      native_conditional_flags_preserved=all(x['resource_verified']is False and x['cutoff_proved']is False for x in rows),
      selected_candidates=[x for p in PICKS for x in rows if x['path']==p],source_sha256=before)
    need(len(summary['selected_candidates'])==3,'three exact original candidate paths')
    need(all(sha(ROOT/p)==h for p,h in before.items()),'stable source bytes')
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    (out/'CENSUS.json').write_text(json.dumps(rows,indent=2)+'\n');(out/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k not in ('source_sha256','selected_candidates','shared_fields')}))
if __name__=='__main__':main(sys.argv[1])

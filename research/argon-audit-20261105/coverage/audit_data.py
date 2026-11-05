"""Read-only independent catalogue/closed-tree audit. Imports no external code."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
PACKAGE=Path('/Users/bkolodziejek/Documents/BerryEsseen/research/count-transfer-20261105/n5-all-taylor')
def need(ok,why):
    if not ok:raise ValueError(why)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unique(items):
    d={}
    for k,v in items:need(k not in d,'duplicate JSON key');d[k]=v
    return d
def read(p):return json.loads(p.read_text(),object_pairs_hook=unique)
def rat(s):
    need(type(s)is str,'rational string');v=F(s);need(str(v)==s,'canonical rational');return v
def roots(c):
    pl,pu=map(rat,c['p']);scale=rat(c['acquired_scale_upper'])
    need(0<pl<pu<1 and scale>0 and rat(c['Hminus'])>=0 and rat(c['Hplus'])>=0,'source threshold signs')
    lo=5*pl-rat(c['Hminus'])*scale;hi=5*pu+rat(c['Hplus'])*scale
    # Include both centers at a half-integer tie. No integer-center clamping.
    floor=lambda x:x.numerator//x.denominator
    ceil=lambda x:-((-x.numerator)//x.denominator)
    d={k:(max(-F(1,2),lo-k),min(F(1,2),hi-k))for k in range(ceil(lo-F(1,2)),floor(hi+F(1,2))+1)}
    need(d and all(a<b for a,b in d.values()),'all closed nondegenerate root domains')
    return lo,hi,d
def main():
    out=Path(sys.argv[1]);need(not out.exists(),'fresh output');need(__debug__,'ordinary Python')
    paths=sorted(p for p in PACKAGE.rglob('*')if p.is_file())
    need(all(not p.is_symlink()for p in PACKAGE.rglob('*')),'external package has no symlinks')
    before={str(p.relative_to(PACKAGE)):sha(p)for p in paths}
    mf=read(PACKAGE/'FILES.json');listed={z['path']:z for z in mf['files']}
    need(len(listed)==len(mf['files']),'unique manifest entries')
    need(set(before)==set(listed)|{'FILES.json'},'complete package inventory')
    for rel,z in listed.items():
        p=PACKAGE/rel;need(not Path(rel).is_absolute()and '..'not in Path(rel).parts,'safe manifest path')
        need(before[rel]==z['sha256']and p.stat().st_size==z['size'],'package byte identity')
    census=read(PACKAGE/'contracts/CENSUS_295.json')
    old=ROOT/'runs/count_row_20261105/review_next_scope01/checked/CENSUS.json'
    need((PACKAGE/'contracts/CENSUS_295.json').read_bytes()==old.read_bytes(),'identical original independent catalogue')
    need(len(census)==295,'295 original rows');originals={};entry_by_sha={};derived={}
    for e in census:
        p=ROOT/e['path'];need(p.is_file()and sha(p)==e['sha256'],'actual original contract bytes')
        c=read(p);need(type(c['n'])is int and c['n']==5 and len(c['rows'])==1,'one original n5 row')
        need(c['rows'][0]==e['row'],'entire embedded row matches original')
        need(e['sha256']not in entry_by_sha,'unique original sha');entry_by_sha[e['sha256']]=e
        lo,hi,ks=roots(e['row']);need(list(ks)==e['nearest_roots'],'independent complete root census')
        derived[e['sha256']]=ks;originals[e['path']]=e['sha256']
    target=read(PACKAGE/'TARGET.json');need(target['catalogue_sha256']==sha(PACKAGE/'contracts/CENSUS_295.json'),'catalogue target pin')
    need(len(target['rows'])==7 and len({r['row_id']for r in target['rows']})==7,'seven distinct target row identifiers')
    all_roots=[];row_summaries=[];methods=Counter();splits=Counter();positive_prices=0;total_leaves=0;leaf_paths=[]
    for row in target['rows']:
        e=entry_by_sha[row['contract_sha256']];c=e['row'];ks=derived[row['contract_sha256']]
        need(row['contract_path']==e['path'],'target original path')
        need([z['k']for z in row['roots']]==list(ks),'complete target roots')
        need(sha(PACKAGE/'contracts'/f'{row["row_id"]}.json')==e['sha256'],'bundled original contract identity')
        seen=set();count=0;rn=[]
        for z in row['roots']:
            k=z['k'];p=PACKAGE/z['object'];need(sha(p)==z['sha256'],'selected root object')
            need(z['object']not in seen,'unique object in row');seen.add(z['object']);obj=read(p)
            expected={'schema','row_id','contract_path','contract_sha256','n','k','p','u','noise','tree'}
            need(set(obj)==expected and obj['schema']=='N5_ALL_TAYLOR_ROOT_V1','exact root schema')
            need(obj['row_id']==row['row_id']and obj['contract_path']==e['path']and obj['contract_sha256']==e['sha256'],'object source identity')
            need(type(obj['n'])is int and obj['n']==5 and type(obj['k'])is int and obj['k']==k,'literal integer index/root')
            need(obj['p']==c['p']and obj['noise']==['0',c['acquired_lambda_upper']],'full original probability/noise')
            phase=tuple(map(rat,obj['u']));need(phase==ks[k]or phase==(-F(1,2),F(1,2)),'full closed or enlarged phase')
            initial=tuple(map(rat,obj['p']))+phase+tuple(map(rat,obj['noise']))
            leaves=[];vol=F(0)
            def visit(node,d,path):
                nonlocal vol,positive_prices
                need(type(node)is dict and len(path)<=20,'finite tree')
                if set(node)in({'q','theta','method'},{'q','theta','prices','method'}):
                    need(node['method']=='gaussian_taylor_both_halves_v1','fixed analytic method');methods[node['method']]+=1
                    need(type(node['q'])is list and len(node['q'])==6,'six ordered mixture majorants')
                    for q in node['q']:
                        need(type(q)is list and len(q)==5,'quartic shape');v=list(map(rat,q));need(v[4]>0,'positive leading coefficient')
                    need(0<=rat(node['theta'])<=1,'convex blend')
                    if 'prices'in node:
                        need(type(node['prices'])is list and len(node['prices'])==4,'four prices');prices=list(map(rat,node['prices']))
                        need(min(prices)>=0,'nonnegative prices');positive_prices+=int(any(prices))
                    volume=(d[1]-d[0])*(d[3]-d[2])*(d[5]-d[4]);need(volume>0,'nondegenerate leaf')
                    vol+=volume;leaves.append(path);leaf_paths.append([row['row_id'],k,path,list(map(str,d))]);return
                need(set(node)=={'axis','children'}and node['axis']in('p','u','noise'),'known split')
                need(type(node['children'])is list and len(node['children'])==2,'both closed children')
                splits[node['axis']]+=1;i={'p':0,'u':2,'noise':4}[node['axis']];mid=(d[i]+d[i+1])/2
                left=list(d);right=list(d);left[i+1]=mid;right[i]=mid
                visit(node['children'][0],tuple(left),path+'0');visit(node['children'][1],tuple(right),path+'1')
            visit(obj['tree'],initial,'')
            need(vol==(initial[1]-initial[0])*(initial[3]-initial[2])*(initial[5]-initial[4]),'complete dyadic volume')
            need(len(leaves)==z['leaves'],'target leaf count');count+=len(leaves)
            historical=read(PACKAGE/f'evidence/replay01/accepted/{row["row_id"]}/k{k}.json')
            need(historical['object_sha256']==z['sha256']and [v['path']for v in historical['leaves']]==leaves,'historical actual leaf census')
            for v in historical['leaves']:
                need(v['method']=='gaussian_taylor_both_halves_v1'and F(v['cleared_margin'])>0,'historical positive leaf record')
            all_roots.append([row['row_id'],k,len(leaves)]);rn.append(k)
        summary=read(PACKAGE/f'evidence/replay01/accepted/{row["row_id"]}/RESULT.json')
        need(summary['leaves']==count and [z['k']for z in summary['roots']]==rn,'historical whole row census')
        row_summaries.append({'row_id':row['row_id'],'p':c['p'],'rho':[c['rho_lower'],c['rho_upper']],'roots':rn,'leaves':count,'original_sha256':e['sha256']});total_leaves+=count
    historical=read(PACKAGE/'evidence/replay01/accepted/RESULT.json');completion=read(PACKAGE/'COMPLETION.json')
    need(len(all_roots)==20 and total_leaves==63,'actual twenty roots and sixty-three leaves')
    for k,val in [('rows_verified',7),('leaves',63),('global_rays',756),('psd_coefficients',1953),('tensor_coefficients',121500)]:
        need(historical[k]==val and completion[k]==val,'recorded aggregate count '+k)
    need(completion['historical_result_sha256']==sha(PACKAGE/completion['historical_result']),'historical result binding')
    process=read(PACKAGE/'evidence/replay01/capture/PROCESS.json')
    need(process['returncode']==0 and process['inputs_unchanged'],'supplied historical native exit')
    for name in ('stdout','stderr'):need(sha(PACKAGE/f'evidence/replay01/capture/{name}.txt')==process[name+'_sha256'],'historical stream binding')
    after={str(p.relative_to(PACKAGE)):sha(p)for p in paths};need(before==after,'read-only external bytes unchanged')
    for rel,h in originals.items():need(sha(ROOT/rel)==h,'original contract bytes unchanged')
    ambiguity=Counter((e['band'],e['index'])for e in census)
    result={'status':'PASS_READ_ONLY_ORIGINAL_CENSUS_AND_CLOSED_OBJECT_COVERAGE','mathematical_status':'Source and data coverage audit only; no new leaf arithmetic or acquisition replay.',
      'execution_status':'Fresh own stdlib JSON/hash/domain audit; external package code not executed.',
      'original_contracts':295,'catalogue_sha256':sha(PACKAGE/'contracts/CENSUS_295.json'),'bands':dict(Counter(e['band']for e in census)),
      'ambiguous_band_index_pairs':sum(n>1 for n in ambiguity.values()),'selected_rows':row_summaries,'roots':all_roots,
      'root_count':len(all_roots),'leaves':total_leaves,'split_counts':dict(splits),'methods':dict(methods),'positive_price_leaves':positive_prices,
      'package_files':len(paths),'package_source_sha256':before,'external_bytes_unchanged':True,'original_sources_unchanged':True,
      'historical_replay_process':process,'prepare_worktree_used':True}
    out.mkdir(parents=True);(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(out/'LEAF_DOMAINS.json').write_text(json.dumps(leaf_paths,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k not in ('package_source_sha256','roots','historical_replay_process')}))
if __name__=='__main__':main()

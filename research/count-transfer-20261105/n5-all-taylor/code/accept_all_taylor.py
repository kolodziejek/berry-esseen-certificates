"""Stdlib exact acceptance of single-root, whole-row, and multi-row all-Taylor proofs.

No historical success flag admits a leaf: every leaf recomputes 12 Sturm rays,
31 curvature-corrected PSD Bernstein coefficients, and all 50*9*V score tensor
coefficients in exact rational arithmetic.
"""
from pathlib import Path
import argparse,json,sys,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model_all_taylor as m
from selector import CENSUS_PIN,CONTRACTS,select_contract

def source_pins():
    paths=[HERE/'algebra.py',HERE/'gaussian_scalar.py',HERE/'selector.py',HERE/'model_all_taylor.py',Path(__file__)]
    paths+=sorted((HERE/'native').glob('*.py'))+sorted((HERE.parent/'contracts').glob('*.json'))
    return {str(p.relative_to(HERE.parent)):m.sha(p)for p in paths}

def admit_root(obj,row,domain):
    m.need(type(obj)is dict and set(obj)=={'schema','row_id','contract_path','contract_sha256','n','k','p','u','noise','tree'},'exact all-Taylor root schema')
    m.need(obj['schema']=='N5_ALL_TAYLOR_ROOT_V1'and obj['row_id']==row.key and obj['contract_path']==row.path and obj['contract_sha256']==row.contract_sha,'fixed original contract identity')
    m.need(type(obj['n'])is int and not isinstance(obj['n'],bool)and obj['n']==5 and type(obj['k'])is int and not isinstance(obj['k'],bool)and obj['k']==domain[0],'actual n=5 and root k')
    m.need(obj['p']==list(map(str,domain[1:3]))and obj['u']==list(map(str,domain[3:5]))and obj['noise']==list(map(str,domain[5:7])),'complete external closed domain')
    leaves=[];nodes=0
    def visit(node,d,path):
        nonlocal nodes
        nodes+=1;m.need(type(node)is dict and len(path)<=20,'finite exact dyadic tree')
        if set(node)in({'q','theta','method'},{'q','theta','prices','method'}):
            m.need(node['method']=='gaussian_taylor_both_halves_v1','explicit both-half Taylor method')
            val=row.admit(node['q'],node['theta'],d,node.get('prices'))
            leaves.append(dict(path=path,**val));return
        m.need(set(node)=={'axis','children'}and node['axis']in('p','u','noise'),'valid closed subdivision axis')
        c=node['children'];m.need(type(c)is list and len(c)==2,'both closed children required')
        k,pl,pu,ul,uh,lo,hi=d
        if node['axis']=='p':mid=(pl+pu)/2;ds=[(k,pl,mid,ul,uh,lo,hi),(k,mid,pu,ul,uh,lo,hi)]
        elif node['axis']=='u':mid=(ul+uh)/2;ds=[(k,pl,pu,ul,mid,lo,hi),(k,pl,pu,mid,uh,lo,hi)]
        else:mid=(lo+hi)/2;ds=[(k,pl,pu,ul,uh,lo,mid),(k,pl,pu,ul,uh,mid,hi)]
        for i in range(2):visit(c[i],ds[i],path+str(i))
    visit(obj['tree'],domain,'')
    return dict(status='PASS_EXACT_ALL_TAYLOR_CLOSED_REGION',row_id=row.key,contract_path=row.path,contract_sha256=row.contract_sha,
      band=row.band,slab_family=row.slab_family,index=row.index,n=5,k=domain[0],
      p=list(map(str,domain[1:3])),u=list(map(str,domain[3:5])),noise=list(map(str,domain[5:7])),
      nodes=nodes,leaves=leaves,taylor_leaves=len(leaves),baseline_leaves=0,
      global_rays=sum(z['global_rays']for z in leaves),psd_coefficients=sum(z['psd_coefficients']for z in leaves),
      tensor_coefficients=sum(z['tensor_coefficients']for z in leaves))

def admit_row_selection(selection):
    m.need(type(selection)is dict and set(selection)=={'schema','selector','row_id','contract_path','contract_sha256','roots'},'whole-row selection schema')
    m.need(selection['schema']=='N5_ALL_TAYLOR_ROW_SELECTION_V1','fixed whole-row selection schema')
    row=m.Row(selection['selector'])
    m.need(selection['row_id']==row.key and selection['contract_path']==row.path and selection['contract_sha256']==row.contract_sha,'selection matches resolved contract')
    roots=selection['roots'];m.need(type(roots)is list and len(roots)==len(row.roots),'complete original root count')
    m.need([z.get('k')for z in roots]==list(row.roots),'ordered exact root census')
    jobs=[];paths=set()
    for z in roots:
        m.need(type(z)is dict and set(z)=={'k','object','sha256'},'fixed root selector')
        k=z['k'];m.need(type(k)is int and not isinstance(k,bool)and k in row.roots,'literal licensed root')
        unresolved=Path(z['object']);m.need(not unresolved.is_symlink(),'no selected object symlink')
        path=unresolved.resolve();m.need(str(path)not in paths and path.is_file(),'unique regular object')
        paths.add(str(path));m.need(m.sha(path)==z['sha256'],'selected object bytes')
        obj=json.loads(path.read_text(),object_pairs_hook=m.unique)
        phase=row.roots[k]if obj.get('u')==list(map(str,row.roots[k]))else(-m.F(1,2),m.F(1,2))
        m.need(obj.get('u')==list(map(str,phase)),'whole clipped or explicitly enlarged phase root')
        domain=row.cell(k,(row.pl,row.pu),phase,(0,row.LAMBDA));jobs.append((path,z['sha256'],obj,domain))
    return row,jobs

def run_row(selection,out_dir):
    row,jobs=admit_row_selection(selection);out_dir.mkdir(parents=True,exist_ok=False);results=[]
    for path,pin,obj,domain in jobs:
        t0=time.monotonic();res=admit_root(obj,row,domain);res.update(object_sha256=pin,seconds=time.monotonic()-t0)
        rp=out_dir/f'k{domain[0]}.json';rp.write_text(json.dumps(res,indent=2)+'\n')
        z=dict(k=domain[0],p=res['p'],u=res['u'],noise=res['noise'],leaves=len(res['leaves']),taylor_leaves=res['taylor_leaves'],
          baseline_leaves=res['baseline_leaves'],global_rays=res['global_rays'],psd_coefficients=res['psd_coefficients'],
          tensor_coefficients=res['tensor_coefficients'],result_sha256=m.sha(rp),object_sha256=pin)
        results.append(z);print(json.dumps(z),flush=True)
    m.need(all(m.sha(p)==h for p,h,_,_ in jobs),'stable root object bytes')
    summary=dict(status='PASS_FRESH_COMPLETE_ORIGINAL_N5_ALL_TAYLOR_ROW',row_id=row.key,contract_path=row.path,contract_sha256=row.contract_sha,
      band=row.band,slab_family=row.slab_family,index=row.index,n=5,K='0',
      p=list(map(str,(row.pl,row.pu))),rho=list(map(str,(row.RHO,row.RHO_HI))),beta=list(map(str,(row.BLO,row.BHI))),
      roots=results,leaves=sum(z['leaves']for z in results),taylor_leaves=sum(z['taylor_leaves']for z in results),
      baseline_leaves=sum(z['baseline_leaves']for z in results),global_rays=sum(z['global_rays']for z in results),
      psd_coefficients=sum(z['psd_coefficients']for z in results),tensor_coefficients=sum(z['tensor_coefficients']for z in results),
      old_checked_leaves=row.entry['old_leaves'],
      mathematical_status='Conditional positive closed-score implication under this original acquired row; original acquisition not replayed; no all-n5 claim.')
    (out_dir/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('out',type=Path)
    ap.add_argument('--mode',choices=['root','row','multi'],default='multi')
    ap.add_argument('--row');ap.add_argument('--k',type=int);a=ap.parse_args()
    pins=source_pins();in_pin=m.sha(a.input)
    payload=json.loads(a.input.read_text(),object_pairs_hook=m.unique)
    if a.mode=='root':
        row=m.Row(a.row);d=row.cell(a.k,(row.pl,row.pu),row.roots[a.k],(0,row.LAMBDA))
        a.out.mkdir(parents=True,exist_ok=False);res=admit_root(payload,row,d);res.update(source_sha256=pins,object_sha256=in_pin)
        (a.out/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n')
        print(json.dumps({k:v for k,v in res.items()if k!='leaves'}))
    elif a.mode=='row':
        res=run_row(payload,a.out);res.update(source_sha256=pins,selection_sha256=in_pin)
        (a.out/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
    else:
        m.need(type(payload)is dict and set(payload)=={'schema','rows'}and payload['schema']=='N5_ALL_TAYLOR_MULTI_ROW_SELECTION_V1','multi-row selection schema')
        m.need(type(payload['rows'])is list and len(payload['rows'])>=1,'nonempty row list')
        a.out.mkdir(parents=True,exist_ok=False);row_summaries=[];seen_rows=set()
        for row_sel in payload['rows']:
            rid=row_sel.get('row_id');m.need(type(rid)is str and rid not in seen_rows,'unique row_id in multi-row selection');seen_rows.add(rid)
            sub=run_row(row_sel,a.out/rid);row_summaries.append(sub)
        total=dict(status='PASS_FRESH_COMPLETE_ORIGINAL_N5_ALL_TAYLOR_BATCH',rows_verified=len(row_summaries),
          leaves=sum(r['leaves']for r in row_summaries),taylor_leaves=sum(r['taylor_leaves']for r in row_summaries),
          baseline_leaves=sum(r['baseline_leaves']for r in row_summaries),global_rays=sum(r['global_rays']for r in row_summaries),
          psd_coefficients=sum(r['psd_coefficients']for r in row_summaries),tensor_coefficients=sum(r['tensor_coefficients']for r in row_summaries),
          old_checked_leaves=sum(r['old_checked_leaves']for r in row_summaries),
          rows=[{k:v for k,v in r.items()if k!='roots'}for r in row_summaries],
          source_sha256=pins,selection_sha256=in_pin,
          mathematical_status='Conditional positive closed-score implications under each original acquired row; original acquisition not replayed; no all-295 n5 claim.')
        (a.out/'RESULT.json').write_text(json.dumps(total,indent=2)+'\n');print(json.dumps({k:v for k,v in total.items()if k!='source_sha256'}))
    m.need(all(m.sha(HERE.parent/p)==h for p,h in pins.items())and m.sha(a.input)==in_pin,'stable source/input closure')

if __name__=='__main__':main()

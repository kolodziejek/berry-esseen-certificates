"""Stdlib exact acceptance of single-root, whole-row, and complete 295-contract n=5 proofs.

No historical success flag admits a leaf: every leaf recomputes 12 univariate Sturm rays,
31 curvature-corrected PSD Bernstein coefficients, and all 50*4*V score tensor
coefficients in exact rational arithmetic. In multi-row mode, also verifies the
exact 295-contract n=5 4-band (B0=24, BN=32, B2=104, B3=135) probability joins
(283 contiguous probability joins), 102 cross-series beta joins (82 at beta=1/5
and 20 at beta=3/10), and 244 cross-band/cross-slab rho joins at rho=11/10,
23/20, 467/400, 237/200, and 477/400.
"""
from pathlib import Path
import argparse,json,sys,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model_all_taylor as m
from selector import CENSUS_PIN,CONTRACTS,select_all_n5,select_band,select_contract

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
            m.need(node['method']=='gaussian_taylor_both_halves_4pair_v1','explicit both-half 4-pair Taylor method')
            val=row.admit(node['q'],node['theta'],d,node.get('prices'))
            leaves.append(dict(path=path,**val));return
        m.need(set(node)=={'axis','children'}and node['axis']in('p','u','noise','alpha'),'valid closed subdivision axis')
        c=node['children'];m.need(type(c)is list and len(c)==2,'both closed children required')
        k,pl,pu,ul,uh,lo,hi,al,ah=m._unpack(d)
        if node['axis']=='p':mid=(pl+pu)/2;ds=[(k,pl,mid,ul,uh,lo,hi,al,ah),(k,mid,pu,ul,uh,lo,hi,al,ah)]
        elif node['axis']=='u':mid=(ul+uh)/2;ds=[(k,pl,pu,ul,mid,lo,hi,al,ah),(k,pl,pu,mid,uh,lo,hi,al,ah)]
        elif node['axis']=='noise':mid=(lo+hi)/2;ds=[(k,pl,pu,ul,uh,lo,mid,al,ah),(k,pl,pu,ul,uh,mid,hi,al,ah)]
        else:mid=(al+ah)/2;ds=[(k,pl,pu,ul,uh,lo,hi,al,mid),(k,pl,pu,ul,uh,lo,hi,mid,ah)]
        for i in range(2):visit(c[i],ds[i],path+str(i))
    visit(obj['tree'],domain,'')
    return dict(status='PASS_EXACT_ALL_TAYLOR_CLOSED_REGION',row_id=row.key,contract_path=row.path,contract_sha256=row.contract_sha,
      band=row.band,slab_family=row.slab_family,series=row.series,index=row.index,n=5,k=domain[0],
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
      band=row.band,slab_family=row.slab_family,series=row.series,index=row.index,n=5,K='0',
      p=list(map(str,(row.pl,row.pu))),rho=list(map(str,(row.RHO,row.RHO_HI))),beta=list(map(str,(row.BLO,row.BHI))),
      roots=results,leaves=sum(z['leaves']for z in results),taylor_leaves=sum(z['taylor_leaves']for z in results),
      baseline_leaves=sum(z['baseline_leaves']for z in results),global_rays=sum(z['global_rays']for z in results),
      psd_coefficients=sum(z['psd_coefficients']for z in results),tensor_coefficients=sum(z['tensor_coefficients']for z in results),
      old_checked_leaves=row.entry['old_leaves'],
      mathematical_status='Conditional positive closed-score implication under this original acquired row; original acquisition not replayed.')
    (out_dir/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary

def verify_n5_all_join(row_summaries):
    expected=select_all_n5()
    m.need(len(row_summaries)==len(expected)==295,'complete 295-contract n=5 union required')
    m.need([r['row_id']for r in row_summaries]==[e['row_id']for e in expected],'canonical 295-contract order')
    m.need([r['contract_sha256']for r in row_summaries]==[e['sha256']for e in expected],'pinned 295-contract sha256 list')
    slices={
      'B0_B0':row_summaries[0:24],
      'BN_BN':row_summaries[24:56],
      'B2_S0':row_summaries[56:88],
      'B2_S1':row_summaries[88:106],
      'B2_S2':row_summaries[106:140],
      'B2_S3':row_summaries[140:160],
      'B3_S0':row_summaries[160:195],
      'B3_S2':row_summaries[195:231],
      'B3_T0':row_summaries[231:253],
      'B3_T1':row_summaries[253:262],
      'B3_T2':row_summaries[262:284],
      'B3_T3lower':row_summaries[284:295],
    }
    specs=(
      ('B0_B0','B0','B0',24,37,60,m.F(37,100),m.F(61,100),m.F(1),m.F(11,10),None),
      ('BN_BN','BN','BN',32,34,65,m.F(17,50),m.F(33,50),m.F(11,10),m.F(23,20),None),
      ('B2_S0','B2','S0',32,33,64,m.F(33,100),m.F(13,20),m.F(23,20),m.F(467,400),None),
      ('B2_S1','B2','S1',18,33,50,m.F(33,100),m.F(51,100),m.F(23,20),m.F(467,400),m.F(1,5)),
      ('B2_S2','B2','S2',34,32,65,m.F(8,25),m.F(33,50),m.F(467,400),m.F(237,200),None),
      ('B2_S3','B2','S3',20,32,51,m.F(8,25),m.F(13,25),m.F(467,400),m.F(237,200),m.F(1,5)),
      ('B3_S0','B3','S0',35,31,65,m.F(31,100),m.F(33,50),m.F(237,200),m.F(477,400),None),
      ('B3_S2','B3','S2',36,31,66,m.F(31,100),m.F(67,100),m.F(477,400),m.F(6,5),None),
      ('B3_T0','B3','T0',22,31,52,m.F(31,100),m.F(53,100),m.F(237,200),m.F(477,400),m.F(1,5)),
      ('B3_T1','B3','T1',9,32,40,m.F(8,25),m.F(41,100),m.F(237,200),m.F(477,400),m.F(3,10)),
      ('B3_T2','B3','T2',22,31,52,m.F(31,100),m.F(53,100),m.F(477,400),m.F(6,5),m.F(1,5)),
      ('B3_T3lower','B3','T3lower',11,31,41,m.F(31,100),m.F(21,50),m.F(477,400),m.F(6,5),m.F(3,10)),
    )
    series_summary={};half_joins=[];tot_prob_joins=0;capped_rho=[]
    for key,band,sname,exp_len,idx_lo,idx_hi,p_lo,p_hi,r_lo,r_hi_max,b_floor in specs:
        sr=slices[key]
        m.need(len(sr)==exp_len and sr[0]['index']==idx_lo and sr[-1]['index']==idx_hi,f'exact {key} slice')
        m.need(m.rational(sr[0]['p'][0])==p_lo and m.rational(sr[-1]['p'][1])==p_hi,f'exact {key} p endpoints')
        for a,b in zip(sr,sr[1:]):
            m.need(b['index']==a['index']+1,'contiguous panel index join')
            m.need(m.rational(a['p'][1])==m.rational(b['p'][0]),'exact contiguous probability endpoint join')
            m.need(a['band']==b['band']==band and a['series']==b['series']==sname,f'uniform {key} series')
            if m.rational(a['p'][1])==m.F(1,2):
                half_joins.append(dict(series=key,join_p=a['p'][1],left_row=a['row_id'],right_row=b['row_id']))
        for r in sr:
            m.need(m.rational(r['rho'][0])==r_lo and r_lo<m.rational(r['rho'][1])<=r_hi_max,f'exact {key} rho bounds')
            if m.rational(r['rho'][1])<r_hi_max:
                capped_rho.append(dict(row_id=r['row_id'],p=r['p'],rho=r['rho'],nominal_ceiling=str(r_hi_max)))
            if b_floor is not None:m.need(m.rational(r['beta'][0])==b_floor,f'exact {key} beta floor')
        tot_prob_joins+=len(sr)-1
        series_summary[key]=dict(band=band,series=sname,contracts=len(sr),index_range=[idx_lo,idx_hi],
          p_union=[str(p_lo),str(p_hi)],rho_floor=str(r_lo),rho_ceiling_max=str(r_hi_max),
          contiguous_probability_joins=len(sr)-1,roots=sum(len(r['roots'])for r in sr),
          leaves=sum(r.get('leaves',0)for r in sr),old_checked_leaves=sum(r.get('old_checked_leaves',0)for r in sr))

    by_s={k:{r['index']:r for r in slices[k]}for k in slices}
    beta_joins={}
    for left,right,b_join in(
      ('B2_S0','B2_S1',m.F(1,5)),('B2_S2','B2_S3',m.F(1,5)),
      ('B3_S0','B3_T0',m.F(1,5)),('B3_T0','B3_T1',m.F(3,10)),
      ('B3_S2','B3_T2',m.F(1,5)),('B3_T2','B3_T3lower',m.F(3,10))):
        cnt=0
        for idx,rr in by_s[right].items():
            ll=by_s[left][idx]
            m.need(ll['p']==rr['p']and m.rational(ll['beta'][1])==m.rational(rr['beta'][0])==b_join,f'{left}/{right} beta={b_join} join')
            cnt+=1
        beta_joins[f'{left}__{right}']=cnt

    rho_joins={}
    for lower_s,upper_s,r_join in(
      ('B0_B0','BN_BN',m.F(11,10)),
      ('BN_BN','B2_S0',m.F(23,20)),('BN_BN','B2_S1',m.F(23,20)),
      ('B2_S0','B2_S2',m.F(467,400)),('B2_S1','B2_S3',m.F(467,400)),
      ('B2_S2','B3_S0',m.F(237,200)),('B2_S3','B3_T0',m.F(237,200)),('B2_S3','B3_T1',m.F(237,200)),
      ('B3_S0','B3_S2',m.F(477,400)),('B3_T0','B3_T2',m.F(477,400)),('B3_T1','B3_T3lower',m.F(477,400))):
        cnt=0
        for idx,ll in by_s[lower_s].items():
            if idx in by_s[upper_s]and m.rational(ll['rho'][1])==r_join:
                uu=by_s[upper_s][idx]
                m.need(ll['p']==uu['p']and m.rational(uu['rho'][0])==r_join,f'{lower_s}/{upper_s} rho={r_join} join')
                cnt+=1
        rho_joins[f'{lower_s}__{upper_s}']=cnt

    bands_summary={}
    for b in('B0','BN','B2','B3'):
        br=[r for r in row_summaries if r['band']==b]
        bands_summary[b]=dict(contracts=len(br),roots=sum(len(r['roots'])for r in br),
          leaves=sum(r.get('leaves',0)for r in br),old_checked_leaves=sum(r.get('old_checked_leaves',0)for r in br))

    m.need(tot_prob_joins==283 and len(half_joins)==10 and sum(beta_joins.values())==102 and sum(rho_joins.values())==244 and len(capped_rho)==8,'complete 295-contract n=5 join census')
    return dict(
      contracts_verified=len(row_summaries),
      roots_verified=sum(len(r['roots'])for r in row_summaries),
      bands=bands_summary,
      series=series_summary,
      contiguous_probability_joins=tot_prob_joins,
      beta_joins=beta_joins,
      total_beta_joins=sum(beta_joins.values()),
      rho_joins=rho_joins,
      total_rho_joins=sum(rho_joins.values()),
      support_capped_rho_panels=capped_rho,
      half_boundary_joins=half_joins,
    )

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
        m.need(type(payload['rows'])is list and len(payload['rows'])==295,'complete 295-row n=5 selection')
        a.out.mkdir(parents=True,exist_ok=False);row_summaries=[];seen_rows=set()
        for row_sel in payload['rows']:
            rid=row_sel.get('row_id');m.need(type(rid)is str and rid not in seen_rows,'unique row_id in multi-row selection');seen_rows.add(rid)
            sub=run_row(row_sel,a.out/rid);row_summaries.append(sub)
        domain_join=verify_n5_all_join(row_summaries)
        total=dict(status='PASS_FRESH_COMPLETE_ORIGINAL_N5_ALL_295_CONTRACTS',rows_verified=len(row_summaries),
          roots_verified=domain_join['roots_verified'],
          leaves=sum(r['leaves']for r in row_summaries),taylor_leaves=sum(r['taylor_leaves']for r in row_summaries),
          baseline_leaves=sum(r['baseline_leaves']for r in row_summaries),global_rays=sum(r['global_rays']for r in row_summaries),
          psd_coefficients=sum(r['psd_coefficients']for r in row_summaries),tensor_coefficients=sum(r['tensor_coefficients']for r in row_summaries),
          old_checked_leaves=sum(r['old_checked_leaves']for r in row_summaries),
          domain_join=domain_join,
          rows=[{k:v for k,v in r.items()if k!='roots'}for r in row_summaries],
          source_sha256=pins,selection_sha256=in_pin,
          mathematical_status='Complete 295-contract n=5 (B0=24, BN=32, B2=104, B3=135; 903 roots) positive closed-score implication under gaussian_taylor_both_halves_4pair_v1 retaining all original contract hypotheses with verified probability, beta, and rho joins; original acquisition not replayed.')
        (a.out/'RESULT.json').write_text(json.dumps(total,indent=2)+'\n');print(json.dumps({k:v for k,v in total.items()if k!='source_sha256'}))
    m.need(all(m.sha(HERE.parent/p)==h for p,h in pins.items())and m.sha(a.input)==in_pin,'stable source/input closure')

if __name__=='__main__':main()

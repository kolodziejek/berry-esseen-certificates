"""Complete BN39 row with explicit baseline/Taylor leaf dispatch, never PASS flags."""
from pathlib import Path
import argparse,json,sys,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import accept,accept_row,model_taylor
m=accept.m

def admit(obj,row,domain):
    m.need(type(obj)is dict,'mixed object must be a mapping')
    if obj.get('schema')=='N5_THREE_CONTRACT_TRANSFER_V1':
        result=accept.admit(obj,row,domain);result.update(baseline_leaves=len(result['leaves']),taylor_leaves=0);return result
    m.need(type(obj)is dict and set(obj)=={'schema','row_id','contract_sha256','n','k','p','u','noise','tree'},'fixed mixed object schema')
    m.need(obj['schema']=='N5_THREE_CONTRACT_TRANSFER_MIXED_TAYLOR_V1'and obj['row_id']==row.key and obj['contract_sha256']==row.contract_sha,'fixed mixed original identity')
    m.need(type(obj['n'])is int and obj['n']==5 and type(obj['k'])is int and obj['k']==domain[0],'actual mixed index/root')
    m.need(obj['p']==list(map(str,domain[1:3]))and obj['u']==list(map(str,domain[3:5]))and obj['noise']==list(map(str,domain[5:7])),'complete mixed external domain')
    taylor=model_taylor.Row(row.key);leaves=[];nodes=0;methods={'baseline':0,'gaussian_taylor_v1':0}
    def visit(node,d,path):
        nonlocal nodes
        nodes+=1;m.need(type(node)is dict and len(path)<=20,'finite exact mixed tree')
        if set(node)=={'q','theta'}:
            value=row.admit(node['q'],node['theta'],d);method='baseline'
        elif set(node)=={'q','theta','method'}:
            m.need(node['method']=='gaussian_taylor_v1','known explicit analytic method');value=taylor.admit(node['q'],node['theta'],d);method=node['method']
        else:
            m.need(set(node)=={'axis','children'}and node['axis']in('p','u'),'fixed mixed subdivision')
            c=node['children'];m.need(type(c)is list and len(c)==2,'both complete mixed closed children')
            k,pl,pu,ul,uh,lo,hi=d
            if node['axis']=='p':mid=(pl+pu)/2;ds=[(k,pl,mid,ul,uh,lo,hi),(k,mid,pu,ul,uh,lo,hi)]
            else:mid=(ul+uh)/2;ds=[(k,pl,pu,ul,mid,lo,hi),(k,pl,pu,mid,uh,lo,hi)]
            for i in range(2):visit(c[i],ds[i],path+str(i))
            return
        methods[method]+=1;leaves.append(dict(path=path,method=method,**value))
    visit(obj['tree'],domain,'')
    return dict(status='PASS_EXACT_MIXED_CLOSED_REGION',row_id=row.key,contract_sha256=row.contract_sha,n=5,k=domain[0],p=list(map(str,domain[1:3])),u=list(map(str,domain[3:5])),noise=list(map(str,domain[5:7])),nodes=nodes,leaves=leaves,baseline_leaves=methods['baseline'],taylor_leaves=methods['gaussian_taylor_v1'],global_rays=sum(z['global_rays']for z in leaves),tensor_coefficients=sum(z['tensor_coefficients']for z in leaves))

def source_pins():
    pins=accept.source_pins()
    for name in ['accept_row.py','model_taylor.py','gaussian_scalar.py','accept_mixed.py']:pins[name]=m.sha(HERE/name)
    return pins

def main():
    ap=argparse.ArgumentParser();ap.add_argument('selection',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    row=m.Row('BN39');selection=json.loads(a.selection.read_text(),object_pairs_hook=m.unique);sp=m.sha(a.selection);jobs=accept_row.admit_selection(selection,row);pins=source_pins()
    a.out.mkdir(parents=True,exist_ok=False);results=[]
    for path,pin,obj,domain in jobs:
        start=time.monotonic();result=admit(obj,row,domain);result.update(object_sha256=pin,seconds=time.monotonic()-start)
        rp=a.out/f'k{domain[0]}.json';rp.write_text(json.dumps(result,indent=2)+'\n')
        z=dict(k=domain[0],p=result['p'],u=result['u'],noise=result['noise'],leaves=len(result['leaves']),baseline_leaves=result['baseline_leaves'],taylor_leaves=result['taylor_leaves'],global_rays=result['global_rays'],tensor_coefficients=result['tensor_coefficients'],result_sha256=m.sha(rp),object_sha256=pin);results.append(z);print(json.dumps(z),flush=True)
    m.need(all(m.sha(HERE/p)==h for p,h in pins.items())and m.sha(a.selection)==sp and all(m.sha(p)==h for p,h,_,_ in jobs),'stable mixed complete source/input closure')
    result=dict(status='PASS_FRESH_COMPLETE_ORIGINAL_BN39_MIXED_ROW',row_id=row.key,contract_sha256=row.contract_sha,n=5,K='0',roots=results,source_sha256=pins,selection_sha256=sp,mathematical_status='Conditional original positive closed-score implication; original acquisition not replayed; no all-n5 claim.')
    for key in ['leaves','baseline_leaves','taylor_leaves','global_rays','tensor_coefficients']:result[key]=sum(z[key]for z in results)
    (a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()

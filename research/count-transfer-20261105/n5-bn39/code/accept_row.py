"""Complete original row: fresh exact arithmetic on every fixed threshold root."""
from pathlib import Path
import argparse,json,sys,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import accept as reader
m=reader.m
def admit_selection(selection,row):
    m.need(type(selection)is dict and set(selection)=={'schema','row_id','contract_sha256','roots'},'whole-row selection schema')
    m.need(selection['schema']=='N5_TRANSFER_ROOT_SELECTION_V1'and selection['row_id']==row.key and selection['contract_sha256']==row.contract_sha,'original source row target')
    roots=selection['roots'];m.need(type(roots)is list and len(roots)==len(row.roots),'complete original root count')
    m.need([z.get('k')for z in roots]==list(row.roots),'ordered exact root census')
    jobs=[];paths=set()
    for z in roots:
        m.need(type(z)is dict and set(z)=={'k','object','sha256'},'fixed root selector')
        k=z['k'];m.need(type(k)is int and k in row.roots,'literal licensed root')
        unresolved=Path(z['object']);m.need(not unresolved.is_symlink(),'no selected object symlink')
        path=unresolved.resolve();m.need(str(path)not in paths and path.is_file(),'unique regular object')
        paths.add(str(path));m.need(m.sha(path)==z['sha256'],'selected object bytes')
        obj=json.loads(path.read_text(),object_pairs_hook=m.unique)
        # Full phase roots are permitted only as this explicit fixed enlargement.
        phase=row.roots[k]if obj.get('u')==list(map(str,row.roots[k]))else(-m.F(1,2),m.F(1,2))
        m.need(obj.get('u')==list(map(str,phase)),'whole clipped or explicitly enlarged phase root')
        domain=row.cell(k,(row.pl,row.pu),phase,(0,row.LAMBDA));jobs.append((path,z['sha256'],obj,domain))
    return jobs
def main():
    ap=argparse.ArgumentParser();ap.add_argument('selection',type=Path);ap.add_argument('out',type=Path);ap.add_argument('--row',required=True,choices=sorted(m.CONTRACTS));a=ap.parse_args()
    row=m.Row(a.row);selection=json.loads(a.selection.read_text(),object_pairs_hook=m.unique);sp=m.sha(a.selection)
    jobs=admit_selection(selection,row);pins=reader.source_pins();pins['accept_row.py']=m.sha(Path(__file__))
    a.out.mkdir(parents=True,exist_ok=False);results=[]
    for path,pin,obj,domain in jobs:
        t=time.monotonic();result=reader.admit(obj,row,domain);result.update(object_sha256=pin,seconds=time.monotonic()-t)
        resultpath=a.out/f'k{domain[0]}.json';resultpath.write_text(json.dumps(result,indent=2)+'\n')
        results.append(dict(k=domain[0],p=result['p'],u=result['u'],noise=result['noise'],leaves=len(result['leaves']),global_rays=result['global_rays'],tensor_coefficients=result['tensor_coefficients'],result_sha256=m.sha(resultpath),object_sha256=pin))
        print(json.dumps(results[-1]),flush=True)
    m.need(all(m.sha(HERE/p)==h for p,h in pins.items())and m.sha(a.selection)==sp and all(m.sha(p)==h for p,h,_,_ in jobs),'unchanged complete source/input closure')
    result=dict(status='PASS_FRESH_COMPLETE_ORIGINAL_N5_TRANSFER_ROW',row_id=row.key,contract_sha256=row.contract_sha,n=5,K='0',
      mathematical_status='Conditional positive closed-score implication under this original acquired row. No acquisition replay or all-n5 theorem.',
      roots=results,leaves=sum(x['leaves']for x in results),global_rays=sum(x['global_rays']for x in results),tensor_coefficients=sum(x['tensor_coefficients']for x in results),
      source_sha256=pins,selection_sha256=sp)
    (a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()

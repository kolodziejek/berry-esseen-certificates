"""Exactly eleven fixed failed cells; no splitting and no prior PASS admission."""
from pathlib import Path
import argparse,hashlib,json,sys,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model_taylor as m
import discover
OBJECT_SHA='b283408792a6d813424d4b1d6706b1711f195974baf8fe63739bdb206db2bcbb'
def failed_cells(obj,row):
    domain=row.cell(2,[row.pl,row.pu],row.roots[2],[0,row.LAMBDA]);found=[]
    m.need(obj['row_id']=='BN39'and obj['contract_sha256']==row.contract_sha and obj['n']==5 and obj['k']==2 and obj['p']==list(map(str,domain[1:3]))and obj['u']==list(map(str,domain[3:5]))and obj['noise']==list(map(str,domain[5:7])),'fixed partial original domain')
    def walk(node,d,path):
        if set(node)=={'failed'}:found.append((path,d));return
        if set(node)=={'q','theta'}:return
        m.need(set(node)=={'axis','children'}and node['axis']in('p','u')and len(node['children'])==2,'complete previous branches')
        k,pl,pu,ul,uh,lo,hi=d
        if node['axis']=='p':mid=(pl+pu)/2;ds=[(k,pl,mid,ul,uh,lo,hi),(k,mid,pu,ul,uh,lo,hi)]
        else:mid=(ul+uh)/2;ds=[(k,pl,pu,ul,mid,lo,hi),(k,pl,pu,mid,uh,lo,hi)]
        for i in range(2):walk(node['children'][i],ds[i],path+str(i))
    walk(obj['tree'],domain,'');m.need(len(found)==11,'fixed11 failures');return found

def main():
    ap=argparse.ArgumentParser();ap.add_argument('object',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    m.need(m.sha(a.object)==OBJECT_SHA,'selected partial object unchanged');row=m.Row('BN39');obj=json.loads(a.object.read_text(),object_pairs_hook=m.unique);cells=failed_cells(obj,row)
    paths=[HERE/p for p in ['model.py','algebra.py','model_taylor.py','gaussian_scalar.py','discover.py','try_taylor_repairs.py']]+sorted((HERE/'native').glob('*.py'))+sorted((HERE/'contracts').glob('*.json'));pins={str(p.relative_to(HERE)):m.sha(p)for p in paths}
    a.out.mkdir(parents=True,exist_ok=False);start=time.monotonic();results=[]
    for path,d in cells:
        candidate,diag=discover.propose(row,d)
        result=dict(path=path,domain=[d[0]]+list(map(str,d[1:])),candidate=candidate,diagnostic=diag)
        (a.out/(path+'.json')).write_text(json.dumps(result,indent=2)+'\n');results.append(result)
        print(json.dumps({k:v for k,v in result.items()if k!='candidate'and k!='diagnostic'}|dict(status=diag['status'],margin=diag.get('margin'))),flush=True)
    m.need(all(m.sha(HERE/p)==v for p,v in pins.items())and m.sha(a.object)==OBJECT_SHA,'unchanged source/input')
    passed=sum(z['candidate']is not None for z in results)
    result=dict(status='ALL11_EXACT_CANDIDATES'if passed==11 else'INCOMPLETE_TAYLOR_REPAIR',passed=passed,total=11,source_sha256=pins,original_object_sha256=OBJECT_SHA,seconds=time.monotonic()-start,scope='Only11 fixed cells, no subdivision. Separate complete mixed exact replay still required.')
    (a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()

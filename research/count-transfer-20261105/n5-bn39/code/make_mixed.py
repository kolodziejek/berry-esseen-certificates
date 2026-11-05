"""Create-only explicit mixed candidate; all new Taylor leaves are checked here."""
from pathlib import Path
import argparse,copy,json,sys,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model_taylor as m
OLD_SHA='b283408792a6d813424d4b1d6706b1711f195974baf8fe63739bdb206db2bcbb'
def main():
    ap=argparse.ArgumentParser();ap.add_argument('old',type=Path);ap.add_argument('repairs',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    m.need(m.sha(a.old)==OLD_SHA,'pinned entire old partial tree');old=json.loads(a.old.read_text(),object_pairs_hook=m.unique);row=m.Row('BN39');domain=row.cell(2,[row.pl,row.pu],row.roots[2],[0,row.LAMBDA]);patches=[];retained=0
    pins={str(p.relative_to(HERE)):m.sha(p)for p in [HERE/x for x in ['algebra.py','model.py','model_taylor.py','gaussian_scalar.py','make_mixed.py']]+list((HERE/'native').glob('*.py'))+list((HERE/'contracts').glob('*.json'))}
    def visit(node,d,path):
        nonlocal retained
        if set(node)=={'q','theta'}:retained+=1;return copy.deepcopy(node)
        if set(node)=={'failed'}:
            source=a.repairs/(path+'.json');record=json.loads(source.read_text(),object_pairs_hook=m.unique)
            m.need(record['path']==path and record['domain']==[d[0]]+list(map(str,d[1:])),'repair bound to actual closed cell')
            candidate=record['candidate'];m.need(type(candidate)is dict and set(candidate)=={'q','theta'},'complete candidate for failed cell')
            checked=row.admit(candidate['q'],candidate['theta'],d)
            patches.append(dict(path=path,input_sha256=m.sha(source),checked=checked));return dict(method='gaussian_taylor_v1',**candidate)
        m.need(set(node)=={'axis','children'}and node['axis']in('p','u')and type(node['children'])is list and len(node['children'])==2,'complete immutable old dyadic branches')
        k,pl,pu,ul,uh,lo,hi=d
        if node['axis']=='p':mid=(pl+pu)/2;ds=[(k,pl,mid,ul,uh,lo,hi),(k,mid,pu,ul,uh,lo,hi)]
        else:mid=(ul+uh)/2;ds=[(k,pl,pu,ul,mid,lo,hi),(k,pl,pu,mid,uh,lo,hi)]
        return dict(axis=node['axis'],children=[visit(node['children'][i],ds[i],path+str(i))for i in range(2)])
    tree=visit(old['tree'],domain,'');m.need(len(patches)==11 and retained==963,'exact whole previous leaf partition')
    m.need({p.name for p in a.repairs.glob('*.json')}=={z['path']+'.json'for z in patches}|{'RESULT.json'},'no missing/extra repair file')
    mixed=copy.deepcopy(old);mixed['schema']='N5_THREE_CONTRACT_TRANSFER_MIXED_TAYLOR_V1';mixed['tree']=tree
    a.out.mkdir(parents=True,exist_ok=False);p=a.out/'proof_object.json';p.write_text(json.dumps(mixed,indent=2)+'\n')
    m.need(m.sha(a.old)==OLD_SHA and all(m.sha(HERE/p)==h for p,h in pins.items()),'stable original/source')
    result=dict(status='EXPLICIT_MIXED_CANDIDATE',baseline_leaves=retained,taylor_leaves=len(patches),original_object_sha256=OLD_SHA,object_sha256=m.sha(p),source_sha256=pins,patches=patches,scope='Only the11 new leaves rechecked here. Full original row still requires fresh complete mixed acceptance.')
    (a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='patches'}))
if __name__=='__main__':main()

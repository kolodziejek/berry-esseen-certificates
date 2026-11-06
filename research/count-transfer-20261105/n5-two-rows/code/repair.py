"""Additive repair of supplied partial trees under unchanged transfer targets.

An old success marker has no authority. Every retained leaf is recomputed
by the new exact reader before reuse. Missing branches remain failures.
"""
from pathlib import Path
import argparse,json,sys,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model as m
import discover as discovery
def main():
    ap=argparse.ArgumentParser();ap.add_argument('object',type=Path);ap.add_argument('out',type=Path)
    ap.add_argument('--row',required=True,choices=sorted(m.CONTRACTS));ap.add_argument('--k',required=True,type=int);ap.add_argument('--p',nargs=2)
    ap.add_argument('--u',nargs=2);ap.add_argument('--noise',nargs=2)
    ap.add_argument('--extra-depth',type=int,default=4);a=ap.parse_args()
    row=m.Row(a.row);domain=row.cell(a.k,a.p or[row.pl,row.pu],a.u or row.roots[a.k],a.noise or[0,row.LAMBDA]);old=json.loads(a.object.read_text(),object_pairs_hook=m.unique)
    m.need(type(old)is dict and set(old)=={'schema','row_id','contract_sha256','n','k','p','u','noise','tree'},'fixed source tree schema')
    m.need(old['schema']=='N5_THREE_CONTRACT_TRANSFER_V1'and old['row_id']==row.key and old['contract_sha256']==row.contract_sha,'known prior family')
    m.need(type(old['n'])is int and old['n']==5 and type(old['k'])is int and old['k']==a.k,'actual index/center')
    m.need(old['p']==list(map(str,domain[1:3]))and old['u']==list(map(str,domain[3:5]))and old['noise']==list(map(str,domain[5:7])),'complete external root')
    a.out.mkdir(parents=True,exist_ok=False);start=time.monotonic();stats=dict(reused=0,repaired=0,failed=0,nodes=0)
    sources=[HERE/'model.py',HERE/'algebra.py',HERE/'discover.py',Path(__file__)]+sorted((HERE/'native').glob('*.py'))+sorted((HERE/'contracts').glob('*.json'))
    pins={str(p.relative_to(HERE)):m.sha(p)for p in sources};inputpin=m.sha(a.object)
    def log(path,d,**kw):
        z=dict(path=path,domain=[d[0]]+list(map(str,d[1:])),seconds=time.monotonic()-start,**kw)
        with(a.out/'PROGRESS.jsonl').open('a')as f:f.write(json.dumps(z)+'\n')
        print(json.dumps(z),flush=True)
    def children(d,axis):
        k,pl,pu,ul,uh,lo,hi=d
        if axis=='p':mid=(pl+pu)/2;return(k,pl,mid,ul,uh,lo,hi),(k,mid,pu,ul,uh,lo,hi)
        mid=(ul+uh)/2;return(k,pl,pu,ul,mid,lo,hi),(k,pl,pu,mid,uh,lo,hi)
    def repair(d,path,depth):
        obj,diag=discovery.propose(row,d);log(path,d,kind='discovery',**{k:v for k,v in diag.items()if k not in('q','result')})
        if obj is not None:stats['repaired']+=1;return obj
        if depth>=a.extra_depth:stats['failed']+=1;return {'failed':diag}
        axis='u'if d[4]-d[3]>10*(d[2]-d[1])else'p';left,right=children(d,axis)
        return dict(axis=axis,children=[repair(left,path+'0',depth+1),repair(right,path+'1',depth+1)])
    def visit(node,d,path):
        stats['nodes']+=1;m.need(type(node)is dict and len(path)<=20,'finite prior node')
        if set(node)=={'q','theta'}:
            try:row.admit(node['q'],node['theta'],d)
            except ValueError:log(path,d,kind='retained_coefficients_need_repair');return repair(d,path,0)
            stats['reused']+=1;log(path,d,kind='fresh_exact_reuse');return node
        if set(node)=={'failed'}:return repair(d,path,0)
        m.need(set(node)=={'axis','children'}and node['axis']in('p','u'),'fixed prior dyadic node')
        m.need(type(node['children'])is list and len(node['children'])==2,'both prior children')
        left,right=children(d,node['axis'])
        return dict(axis=node['axis'],children=[visit(node['children'][0],left,path+'0'),visit(node['children'][1],right,path+'1')])
    tree=visit(old['tree'],domain,'')
    new=dict(schema='N5_THREE_CONTRACT_TRANSFER_V1',row_id=row.key,contract_sha256=row.contract_sha,n=5,k=a.k,
      p=list(map(str,domain[1:3])),u=list(map(str,domain[3:5])),noise=list(map(str,domain[5:7])),tree=tree)
    (a.out/'proof_object.json').write_text(json.dumps(new,indent=2)+'\n')
    m.need(all(m.sha(HERE/p)==h for p,h in pins.items())and m.sha(a.object)==inputpin,'unchanged source/input bytes')
    result=dict(status='COMPLETE_CANDIDATE'if stats['failed']==0 else'PARTIAL_CANDIDATE',**stats,seconds=time.monotonic()-start,
      source_sha256=pins,input_sha256=inputpin,scope='No prior success marker accepted; every reused leaf passed V4 exact arithmetic. Separate final replay still required.')
    (a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()

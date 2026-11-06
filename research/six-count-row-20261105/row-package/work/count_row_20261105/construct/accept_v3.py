"""Stdlib exact replay of an externally specified closed p/u rectangle."""
from pathlib import Path
import argparse,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model_v3 as m
def admit(obj,k,p,u,noise):
    domain=m.cell(k,p,u,noise)
    m.need(type(obj)is dict and set(obj)=={'schema','contract_sha256','n','k','p','u','noise','tree'},'fixed object fields')
    m.need(obj['schema']=='N5_BN38_SIX_COUNT_CELL_V3'and obj['contract_sha256']==m.PINS['contract.json'],'fixed source target')
    m.need(type(obj['n'])is int and obj['n']==5 and type(obj['k'])is int and obj['k']==k,'exact n and k')
    m.need(obj['p']==list(map(str,domain[1:3]))and obj['u']==list(map(str,domain[3:5]))and obj['noise']==list(map(str,domain[5:7])),'external complete rectangle')
    leaves=[];nodes=0
    def visit(node,d,path):
        nonlocal nodes
        nodes+=1;m.need(type(node)is dict and len(path)<=20,'finite tree node')
        if set(node)=={'q','theta'}:leaves.append(dict(path=path,**m.admit(node['q'],node['theta'],d)));return
        m.need(set(node)=={'axis','children'}and node['axis']in('p','u'),'fixed dyadic subdivision')
        children=node['children'];m.need(type(children)is list and len(children)==2,'both closed children required')
        k,pl,pu,ul,uh,lo,hi=d
        if node['axis']=='p':mid=(pl+pu)/2;left=(k,pl,mid,ul,uh,lo,hi);right=(k,mid,pu,ul,uh,lo,hi)
        else:mid=(ul+uh)/2;left=(k,pl,pu,ul,mid,lo,hi);right=(k,pl,pu,mid,uh,lo,hi)
        visit(children[0],left,path+'0');visit(children[1],right,path+'1')
    visit(obj['tree'],domain,'')
    return dict(status='PASS_EXACT_COMPLETE_CLOSED_RECTANGLE',mathematical_status='Conditional positive closed-CDF implication under original acquired same-law premises; no acquisition replay or full-row claim.',
      n=5,k=k,p=list(map(str,domain[1:3])),u=list(map(str,domain[3:5])),noise=list(map(str,domain[5:7])),
      beta=list(map(str,(m.BLO,m.BHI))),rho_lower=str(m.RHO),nodes=nodes,leaves=leaves,
      rays=sum(z['global_rays']for z in leaves),tensor_coefficients=sum(z['tensor_coefficients']for z in leaves))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('object',type=Path);ap.add_argument('out',type=Path)
    ap.add_argument('--k',required=True,type=int);ap.add_argument('--p',nargs=2,required=True);ap.add_argument('--u',nargs=2,required=True);ap.add_argument('--noise',nargs=2,required=True);a=ap.parse_args()
    pins={str(p.relative_to(HERE)):m.sha(p)for p in [HERE/'model.py',HERE/'model_v3.py',Path(__file__)]+sorted((HERE/'native').glob('*.py'))+[HERE/'native/contract.json']}
    result=admit(json.loads(a.object.read_text(),object_pairs_hook=m.unique),a.k,a.p,a.u,a.noise)
    m.need(all(m.sha(HERE/p)==h for p,h in pins.items()),'acceptance source stability')
    result.update(source_sha256=pins,object_sha256=m.sha(a.object))
    a.out.mkdir(parents=True,exist_ok=False);(a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='leaves'}))
if __name__=='__main__':main()

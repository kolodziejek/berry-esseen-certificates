"""Stdlib exact acceptance of a specified original-contract closed cell."""
from pathlib import Path
import argparse,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model_dual as m
def source_pins():
    paths=[HERE/'model.py',HERE/'model_dual.py',HERE/'algebra.py',Path(__file__)]+sorted((HERE/'native').glob('*.py'))+sorted((HERE/'contracts').glob('*.json'))
    return {str(p.relative_to(HERE)):m.sha(p)for p in paths}
def admit(obj,row,domain):
    m.need(type(obj)is dict and set(obj)=={'schema','row_id','contract_sha256','n','k','p','u','noise','tree'},'exact transfer schema')
    m.need(obj['schema']=='N5_THREE_CONTRACT_TRANSFER_DUAL_V1'and obj['row_id']==row.key and obj['contract_sha256']==row.contract_sha,'externally fixed original identity')
    m.need(type(obj['n'])is int and obj['n']==5 and type(obj['k'])is int and obj['k']==domain[0],'literal n and root')
    m.need(obj['p']==list(map(str,domain[1:3]))and obj['u']==list(map(str,domain[3:5]))and obj['noise']==list(map(str,domain[5:7])),'whole external closed domain')
    leaves=[];nodes=0
    def visit(node,d,path):
        nonlocal nodes
        nodes+=1;m.need(type(node)is dict and len(path)<=20,'finite dyadic node')
        if set(node)=={'q','theta','prices'}:leaves.append(dict(path=path,**row.admit(node['q'],node['theta'],node['prices'],d)));return
        m.need(set(node)=={'axis','children'}and node['axis']in('p','u'),'fixed subdivision schema')
        c=node['children'];m.need(type(c)is list and len(c)==2,'both closed children')
        k,pl,pu,ul,uh,lo,hi=d
        if node['axis']=='p':mid=(pl+pu)/2;left=(k,pl,mid,ul,uh,lo,hi);right=(k,mid,pu,ul,uh,lo,hi)
        else:mid=(ul+uh)/2;left=(k,pl,pu,ul,mid,lo,hi);right=(k,pl,pu,mid,uh,lo,hi)
        visit(c[0],left,path+'0');visit(c[1],right,path+'1')
    visit(obj['tree'],domain,'')
    return dict(status='PASS_EXACT_CLOSED_TRANSFER_REGION',mathematical_status='Conditional positive closed-CDF implication under original acquired same-law premises; no acquisition or complete n5 claim.',
      row_id=row.key,contract_sha256=row.contract_sha,n=5,k=domain[0],p=list(map(str,domain[1:3])),u=list(map(str,domain[3:5])),noise=list(map(str,domain[5:7])),
      rho=[row.cfg['rho_lower'],row.cfg['rho_upper']],beta=list(map(str,(row.BLO,row.BHI))),nodes=nodes,leaves=leaves,
      global_rays=sum(z['global_rays']for z in leaves),tensor_coefficients=sum(z['tensor_coefficients']for z in leaves))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('object',type=Path);ap.add_argument('out',type=Path)
    ap.add_argument('--row',required=True,choices=sorted(m.CONTRACTS));ap.add_argument('--k',required=True,type=int)
    ap.add_argument('--p',nargs=2);ap.add_argument('--u',nargs=2);ap.add_argument('--noise',nargs=2);a=ap.parse_args()
    row=m.Row(a.row);domain=row.cell(a.k,a.p or[row.pl,row.pu],a.u or row.roots[a.k],a.noise or[0,row.LAMBDA]);pins=source_pins();inputpin=m.sha(a.object)
    result=admit(json.loads(a.object.read_text(),object_pairs_hook=m.unique),row,domain)
    m.need(all(m.sha(HERE/p)==h for p,h in pins.items())and m.sha(a.object)==inputpin,'unchanged acceptance inputs')
    result.update(source_sha256=pins,object_sha256=inputpin)
    a.out.mkdir(parents=True,exist_ok=False);(a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='leaves'}))
if __name__=='__main__':main()

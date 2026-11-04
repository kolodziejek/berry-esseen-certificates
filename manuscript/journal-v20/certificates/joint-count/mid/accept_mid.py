"""Exact acceptance: reconstruct Bernstein expansions; no optimizer dependency."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from mid_math import targets,loss_gates,affine,trim,add,mul,power,scale,ETA,TL,TU
if not __debug__ or sys.flags.optimize:raise RuntimeError('optimized Python forbidden')

def need(ok,why):
    if not ok:raise ValueError(why)
def unique(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,'duplicate JSON key');d[k]=v
    return d
def rational(s):
    need(type(s)is str,'rational must be a string');v=F(s)
    need(str(v)==s,'canonical rational required');return v
def tree(p,node,a=F(0),b=F(1),depth=0):
    need(type(node)is dict and depth<=24,'proof node type/depth')
    if set(node)=={'split'}:
        children=node['split'];need(type(children)is list and len(children)==2,'both halves required')
        m=(a+b)/2
        l=tree(p,children[0],a,m,depth+1);r=tree(p,children[1],m,b,depth+1)
        return (l[0]+r[0],max(l[1],r[1]))
    need(set(node)=={'bernstein'},'exact leaf fields')
    beta=node['bernstein'];need(type(beta)is list and len(beta)==5,'fixed degree four')
    beta=list(map(rational,beta));need(min(beta)>=0,'nonnegative Bernstein coefficients')
    # Inverse identity, independently of construction's power-to-Bernstein sum.
    reconstructed=[F(0)]
    for i,v in enumerate(beta):
        basis=mul([F(0)]*i+[F(1)],power([F(1),F(-1)],4-i))
        reconstructed=add(reconstructed,scale(basis,comb(4,i)*v))
    need(trim(reconstructed)==trim(affine(p,a,b-a)),'exact polynomial identity')
    return (1,depth)

def accept(obj):
    need(type(obj)is dict and set(obj)=={'schema','rows'},'exact top-level fields')
    need(obj['schema']=='JOINT_STAIRCASE_MID47_V1','fixed theorem/schema')
    rows=obj['rows'];need(type(rows)is list and len(rows)==200,'complete phase cover')
    leaves=0;depth=0;reserve=None
    for i,row in enumerate(rows):
        need(type(row)is dict and set(row)=={'index','phase','q','proofs'},'exact row fields')
        need(type(row['index'])is int and row['index']==i,'ordered unique row')
        a,b=F(i-100,200),F(i-99,200)
        need(row['phase']==[str(a),str(b)],'fixed closed phase interval')
        need(type(row['q'])is list and len(row['q'])==5,'quartic coefficients')
        q=list(map(rational,row['q']));need(q[4]>=0,'fourth moment coefficient sign')
        gates=loss_gates(q,a);need(min(gates)>=0,'both variance endpoints')
        reserve=min(gates)if reserve is None else min(reserve,*gates)
        ps=targets(q,b);need(type(row['proofs'])is list and len(row['proofs'])==len(ps),'all finite intervals and both rays')
        for p,node in zip(ps,row['proofs']):
            n,d=tree(p,node);leaves+=n;depth=max(depth,d)
    strict=F('1421/2000')*ETA*F('18319/20000')-F('59549/25000')/47-F('1/1000')
    need(strict>0,'original strict score target')
    return {'status':'PASS_JOINT_STAIRCASE_MID47','phase_cells':200,'polynomials':2200,
      'bernstein_leaves':leaves,'bernstein_coefficients':5*leaves,'max_bisection_depth':depth,
      'variance_interval':[str(TL),str(TU)],'noise_interval':['1/20','2/25'],
      'minimum_endpoint_reserve':str(reserve),'strict_reserve_beyond_original_target':str(strict),
      'mathematical_scope':'Conditional implication under acquired same-law global47 support, phase and U=.08 normalization premises. Numerical majorants only; no acquisition proof inferred.',
      'original_target':'rho_B(C-C_B)<-lambda/1000'}

def main():
    path=Path(sys.argv[1]);obj=json.loads(path.read_text(),object_pairs_hook=unique)
    result=accept(obj);result['proof_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()

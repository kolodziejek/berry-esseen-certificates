"""Bounded independent target-transform audit of exactly eleven fixed cells."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import ast,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
SRC=ROOT/'work/count_transfer_20261105/construct'
OLD=ROOT/'work/count_transfer_20261105/later/gaussian_taylor01/check_broad.py'
OBJ=ROOT/'runs/count_transfer_20261105/construct_BN39_k2_refined01/objects/proof_object.json'
sys.path.insert(0,str(SRC));import model_taylor as m
import gaussian_scalar as g
sys.path.insert(0,str(HERE));import independent_polys as ip
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def need(ok,msg):
    if not ok:raise ValueError(msg)
def functions(path):
    text=path.read_text();tree=ast.parse(text)
    return {x.name:ast.get_source_segment(text,x)for x in tree.body if isinstance(x,ast.FunctionDef)}
def main():
    need(__debug__ and not sys.flags.optimize,'ordinary Python')
    out=Path(sys.argv[1]);need(not out.exists(),'fresh output')
    sources=[Path(__file__),HERE/'independent_polys.py',OLD,OBJ]+[SRC/n for n in ('gaussian_scalar.py','model_taylor.py','model.py','algebra.py','GAUSSIAN_SCALAR_PROVENANCE.json')]+sorted((SRC/'native').glob('*.py'))+sorted((SRC/'contracts').glob('*.json'))
    before={str(p.relative_to(ROOT)):sha(p)for p in sources}
    need(sha(OBJ)=='b283408792a6d813424d4b1d6706b1711f195974baf8fe63739bdb206db2bcbb','original failed tree identity')
    original=functions(OLD);copied=functions(SRC/'gaussian_scalar.py')
    names=['down','up','interval_mul','gaussian']
    need(all(original[n]==copied[n]for n in names),'unchanged scalar function bodies')
    row=m.Row('BN39');obj=json.loads(OBJ.read_text());cells=[]
    domain=row.cell(2,[row.pl,row.pu],row.roots[2],[0,row.LAMBDA])
    def walk(node,d,path):
        if set(node)=={'failed'}:cells.append((path,d));return
        if set(node)=={'q','theta'}:return
        need(set(node)=={'axis','children'}and len(node['children'])==2,'original complete split')
        k,l,h,a,b,lo,hi=d
        if node['axis']=='p':c=(l+h)/2;children=[(k,l,c,a,b,lo,hi),(k,c,h,a,b,lo,hi)]
        else:
            need(node['axis']=='u','legal original split');c=(a+b)/2;children=[(k,l,h,a,c,lo,hi),(k,l,h,c,b,lo,hi)]
        for j in range(2):walk(node['children'][j],children[j],path+str(j))
    walk(obj['tree'],domain,'');need(len(cells)==11,'exact eleven-cell scope')
    identities=mutants=vertices=0
    for path,d in cells:
        k,l,h,a,b,lo,hi=d;targets,diffs,correlated=row.target_tensors(d)
        need(correlated and k+b-5*l<=0 and (k+a-5*h)**2<=15*l*(1-l),'actual Gaussian concavity')
        hi=row.effective_hi(l,h,hi);_,vhi=m.variance_bounds(l,h);W=vhi+hi/5
        price=m.normal.CE_LO/(m.normal.root(F(5))[1]*W*m.normal.root(W)[1])
        floor=m.normal.CE_LO*row.RHO/m.normal.root(F(5))[1]
        r0,r1=row.inward(l,h,lo);index=0
        for x,y in row.polygon(l,h,lo,hi):
            G,_=g.gaussian(5,k,l,h,a,b,5*(x+y));vertices+=1
            poly=ip.tidy({(i,j):v for j,z in enumerate(G)for i,v in enumerate(z)})
            target=ip.mul(ip.V2,ip.add(poly,ip.scale(ip.ONE,floor)))
            need(max(i for i,j in target)<=6 and max(j for i,j in target)<=2,'target degree')
            for g0,g1 in product((-row.A0,F(0),r0),(row.A1,F(0),-r1)):
                raw=ip.add(ip.mul(ip.V,ip.add(ip.ONE,ip.scale(ip.V,-2))),ip.scale(ip.P,3*x),ip.scale(ip.Q,3*y),ip.scale(ip.ONE,-g0*x+g1*y))
                improvement=ip.mul(ip.V2,ip.add(ip.scale(raw,price),ip.scale(ip.ONE,-floor)))
                need(ip.inverse(targets[index])==ip.local(target,l,h,a,b),'independent Taylor target inverse')
                need(ip.inverse(diffs[index])==ip.local(improvement,l,h,a,b),'independent original affine price inverse')
                broken=list(targets[index]);broken[25]+=F(1,1000)
                need(ip.inverse(broken)!=ip.local(target,l,h,a,b),'target mutation rejected')
                identities+=100;mutants+=1;index+=1
        need(index==len(targets)==len(diffs),'all vertices and nine shared corners')
    after={str(p.relative_to(ROOT)):sha(p)for p in sources};need(before==after,'source stability')
    result={'status':'PASS_INDEPENDENT_ELEVEN_CELL_TAYLOR_TARGET_ALGEBRA','cells':11,'variance_vertices':vertices,
      'exact_inverse_coefficients':identities,'target_mutants':mutants,'byte_identical_scalar_functions':names,
      'scope':'Exactly the original eleven failed BN39 domains. Independent tensor inverse/price algebra; shared already-reviewed Gaussian scalar. No discovery, full-tree replay, or new acquisition.',
      'sources_unchanged':True,'source_sha256_before':before,'source_sha256_after':after,'paths':[p for p,d in cells]}
    out.mkdir();(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if not k.startswith('source_sha')}))
if __name__=='__main__':main()

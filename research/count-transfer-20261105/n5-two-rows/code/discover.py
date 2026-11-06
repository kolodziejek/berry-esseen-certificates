"""Floating LP discovery; all candidate leaves receive exact acceptance.
Only accept.py is an acceptance entrypoint; this driver may leave failures.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys,time
import numpy as np
from scipy.optimize import linprog
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model as m

def ray_rows():
    st=m.sturm.base;lhs=[];rhs=[]
    for j in range(6):
      for sign,sub in((-1,1),(1,0)):
        targets=[m.compact_ray([F(int(k==d))for k in range(5)],sign,F(0))for d in range(5)]
        constant=m.compact_ray([F(sub),F(0),F(0),F(0),F(0)],sign,F(0))
        for a in range(32):
          co=[m.bernstein(p,F(a,32),F(a+1,32),4)for p in targets]
          cc=m.bernstein(constant,F(a,32),F(a+1,32),4)
          for k in range(5):
            row=[0.]*32
            for d in range(5):row[5*j+d]=-float(co[d][k])
            lhs.append(row);rhs.append(-float(cc[k])-1e-9)
    return lhs,rhs
RAY_LHS,RAY_RHS=ray_rows()
def propose(row,domain):
    rows=row.tensors(*domain);targets,diffs,_=row.target_tensors(domain)
    v2=m.bernstein(m.V2,domain[1],domain[2],9)
    lhs=[];rhs=[]
    for moment_row,target,diff in zip(rows,targets,diffs):
      for a in range(50):
        scale=float(v2[a//5]);lhs.append([float(d[a])/scale for d in moment_row]+[-float(diff[a])/scale,1.]);rhs.append(float(target[a])/scale)
    lhs+=RAY_LHS;rhs+=RAY_RHS
    ans=linprog([0.]*31+[-1.],A_ub=np.array(lhs),b_ub=np.array(rhs),
      bounds=[((-500,500)if d%5<4 else(1e-8,500))for d in range(30)]+[(0,1),(-100,100)],method='highs',
      options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    if not ans.success:return None,dict(status='LP_FAILED',message=ans.message)
    diagnostic=dict(status='NO_STRICT_DISCOVERY_MARGIN',margin=float(ans.x[-1]))
    if ans.x[-1]<=1e-5:return None,diagnostic
    q=[[F(round(x*10**10),10**10)for x in ans.x[5*j:5*j+5]]for j in range(6)]
    for coeff in q:coeff[0]+=F(1,10**6);coeff[4]+=F(1,10**7)
    q=[list(map(str,coeff))for coeff in q]
    try:r=row.admit(q,str(F(round(ans.x[30]*10**10),10**10)),domain,rows)
    except ValueError as e:return None,dict(status='RATIONALIZED_CANDIDATE_REJECTED',message=str(e),q=q,margin=float(ans.x[-1]))
    return {'q':q,'theta':str(F(round(ans.x[30]*10**10),10**10))},dict(status='EXACT_LEAF_CHECKED',result=r,margin=float(ans.x[-1]))
def source_pins():
    paths=[HERE/'model.py',HERE/'algebra.py',Path(__file__)]+sorted((HERE/'native').glob('*.py'))+sorted((HERE/'contracts').glob('*.json'))
    return {str(p.relative_to(HERE)):m.sha(p)for p in paths}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);ap.add_argument('--row',required=True,choices=sorted(m.CONTRACTS))
    ap.add_argument('--k',required=True,type=int);ap.add_argument('--p',nargs=2);ap.add_argument('--u',nargs=2);ap.add_argument('--noise',nargs=2)
    ap.add_argument('--max-depth',type=int,default=10);ap.add_argument('--node-budget',type=int,default=1600);a=ap.parse_args()
    row=m.Row(a.row);domain=row.cell(a.k,a.p or [row.pl,row.pu],a.u or row.roots[a.k],a.noise or [0,row.LAMBDA])
    out=a.out.resolve();out.mkdir(parents=True,exist_ok=False);count=0;leaves=0;failed=0;start=time.monotonic();pins=source_pins()
    def visit(d,path):
        nonlocal count,leaves,failed
        count+=1
        if count>a.node_budget:obj=None;diag=dict(status='NODE_BUDGET_UNRESOLVED')
        else:obj,diag=propose(row,d)
        rec=dict(path=path,domain=[d[0]]+list(map(str,d[1:])),seconds=time.monotonic()-start,**diag)
        with(out/'PROGRESS.jsonl').open('a')as f:f.write(json.dumps(rec)+'\n')
        print(json.dumps({k:v for k,v in rec.items()if k not in('q','result')}),flush=True)
        if obj is not None:leaves+=1;return obj
        # This is a discovery stopping policy, never an infeasibility assertion.
        persistent=diag.get('margin',0)<-0.003 and d[2]-d[1]<=F(1,400)and d[4]-d[3]<=F(1,32)
        if len(path)>=a.max_depth or count>=a.node_budget or persistent:
            failed+=1;return {'failed':diag}
        k,pl,pu,ul,uh,lo,hi=d;axis='u'if uh-ul>10*(pu-pl)else'p'
        if axis=='u':mid=(ul+uh)/2;left=(k,pl,pu,ul,mid,lo,hi);right=(k,pl,pu,mid,uh,lo,hi)
        else:mid=(pl+pu)/2;left=(k,pl,mid,ul,uh,lo,hi);right=(k,mid,pu,ul,uh,lo,hi)
        return dict(axis=axis,children=[visit(left,path+'0'),visit(right,path+'1')])
    tree=visit(domain,'')
    obj=dict(schema='N5_THREE_CONTRACT_TRANSFER_V1',row_id=a.row,contract_sha256=row.contract_sha,n=5,k=a.k,
      p=list(map(str,domain[1:3])),u=list(map(str,domain[3:5])),noise=list(map(str,domain[5:7])),tree=tree)
    (out/'proof_object.json').write_text(json.dumps(obj,indent=2)+'\n')
    m.need(all(m.sha(HERE/p)==h for p,h in pins.items()),'construction source stability')
    result=dict(status='COMPLETE_CANDIDATE'if failed==0 else'PARTIAL_CANDIDATE',row_id=a.row,k=a.k,nodes=count,leaves=leaves,failed=failed,
      source_sha256=pins,seconds=time.monotonic()-start,scope='Candidate construction only. A failure is unresolved, not infeasible. Separate exact replay required.')
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()

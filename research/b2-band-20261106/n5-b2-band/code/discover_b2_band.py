"""Floating LP discovery for the complete 104-contract n=5 B2 band (S0, S1, S2, S3).

Uses ('u', 'noise', 'alpha', 'p') dyadic subdivision with elevated-noise variance
allocation (alpha in [al, ah]), Cauchy-Schwarz support-moment tightening, shifted
support-square affine fourth-moment envelopes, and the 4-endpoint-pair moment
reduction so every contract across the 104-contract B2 band closes with all-Taylor
curvature-corrected certificates, zero baseline fallback leaves, zero empty-domain
leaves, and zero dual prices. Every candidate leaf is immediately checked in exact
rational arithmetic by model_all_taylor.Row.admit() before admission.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import argparse,json,sys,time
import numpy as np
from scipy.optimize import linprog
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model_all_taylor as m
from selector import select_band

def ray_rows(num_vars=36):
    lhs=[];rhs=[]
    for j in range(6):
      for sign,sub in((-1,1),(1,0)):
        targets=[m.compact_ray([F(int(k==d))for k in range(5)],sign,F(0))for d in range(5)]
        constant=m.compact_ray([F(sub),F(0),F(0),F(0),F(0)],sign,F(0))
        for a in range(32):
          co=[m.bernstein(p,F(a,32),F(a+1,32),4)for p in targets]
          cc=m.bernstein(constant,F(a,32),F(a+1,32),4)
          for k in range(5):
            row=[0.]*num_vars
            for d in range(5):row[5*j+d]=-float(co[d][k])
            lhs.append(row);rhs.append(-float(cc[k])-1e-9)
    return lhs,rhs

RAY_LHS,RAY_RHS=ray_rows(36)

def propose(row,domain,use_dual=False):
    k,pl,pu,ul,uh,lo,hi,al,ah=m._unpack(domain)
    rows=row.tensors(k,pl,pu,ul,uh,lo,hi,al,ah);targets,diffs,M_curv,_=row.target_tensors(domain);duals=row.dual_tensors(domain)
    v2=m.bernstein(m.V2,pl,pu,9)
    lhs=[];rhs=[]
    for moment_row,target,diff,dual in zip(rows,targets,diffs,duals):
      for a in range(50):
        scale=float(v2[a//5])
        lhs.append([float(d[a])/scale for d in moment_row]+[-float(diff[a])/scale]+[-float(dual[i][a])/scale for i in range(4)]+[1.])
        rhs.append(float(target[a])/scale)
    lhs+=RAY_LHS;rhs+=RAY_RHS
    if M_curv>0:
        masses=[m.scale(m.mul(m.power(m.P,j),m.power(m.Q,5-j)),F(comb(5,j)))for j in range(6)]
        b00_j=[m.bernstein(m.scale(m.mul(masses[j],m.mul(m.P,m.P)),F(24,5)*(5-j)**2),pl,pu,7)for j in range(6)]
        b01_j=[m.bernstein(m.scale(m.mul(masses[j],m.mul(m.P,m.Q)),F(24,5)*(5-j)*j),pl,pu,7)for j in range(6)]
        b11_j=[m.bernstein(m.scale(m.mul(masses[j],m.mul(m.Q,m.Q)),F(24,5)*j**2),pl,pu,7)for j in range(6)]
        b_corr=m.bernstein(m.scale(m.V2,25*M_curv),pl,pu,7)
        for idx in range(8):
            r01=[0.]*36;r00=[0.]*36;r11=[0.]*36
            for j in range(6):
                r01[5*j+4]=-float(b01_j[j][idx])
                r00[5*j+4]=-float(b00_j[j][idx]-b01_j[j][idx])
                r11[5*j+4]=-float(b11_j[j][idx]-b01_j[j][idx])
            lhs.extend([r01,r00,r11]);rhs.extend([-float(b_corr[idx])-1e-7,-1e-7,-1e-7])
    bounds=[((-500,500)if d%5<4 else(1e-8,500))for d in range(30)]+[(0,1)]+[(0,100 if use_dual else 0)]*4+[(-100,100)]
    ans=linprog([0.]*35+[-1.],A_ub=np.array(lhs),b_ub=np.array(rhs),bounds=bounds,method='highs',
      options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    if not ans.success:return None,dict(status='LP_FAILED',message=ans.message)
    diagnostic=dict(status='NO_STRICT_DISCOVERY_MARGIN',margin=float(ans.x[-1]))
    if ans.x[-1]<=1e-5:return None,diagnostic
    q=[[F(round(x*10**10),10**10)for x in ans.x[5*j:5*j+5]]for j in range(6)]
    for coeff in q:coeff[0]+=F(1,10**6);coeff[4]+=F(1,10**7)
    q=[list(map(str,coeff))for coeff in q]
    theta=str(F(min(10**10,max(0,round(ans.x[30]*10**10))),10**10))
    prices=[str(F(max(0,round(x*10**10)),10**10))for x in ans.x[31:35]]
    try:res=row.admit(q,theta,domain,prices,rows)
    except ValueError as e:return None,dict(status='RATIONALIZED_CANDIDATE_REJECTED',message=str(e),margin=float(ans.x[-1]))
    leaf={'q':q,'theta':theta,'method':'gaussian_taylor_both_halves_4pair_v1'}
    if any(F(p)>0 for p in prices):leaf['prices']=prices
    return leaf,dict(status='EXACT_LEAF_CHECKED',result=res,margin=float(ans.x[-1]))

def valid_poly(row,pl,pu,lo,hi,al,ah):
    try:
        row.polygon(pl,pu,lo,hi,al,ah)
        return True
    except ValueError:
        return False

def build_root(row,k,out_dir,max_depth=14,node_budget=1600,use_dual=False):
    domain=row.cell(k,[row.pl,row.pu],row.roots[k],[0,row.LAMBDA])
    out_dir.mkdir(parents=True,exist_ok=True);count=0;leaves=0;failed=0
    def visit(d,path):
        nonlocal count,leaves,failed
        count+=1
        if count>node_budget:obj=None;diag=dict(status='NODE_BUDGET_UNRESOLVED')
        else:obj,diag=propose(row,d,use_dual=use_dual)
        if obj is not None:leaves+=1;return obj
        if len(path)>=max_depth or count>=node_budget:
            failed+=1;return {'failed':diag}
        kk,pl,pu,ul,uh,lo,hi,al,ah=m._unpack(d);mid_noise=(lo+hi)/2;mid_al=(al+ah)/2
        can_noise=mid_noise<row.effective_hi(pl,pu,hi)and valid_poly(row,pl,pu,lo,mid_noise,al,ah)and valid_poly(row,pl,pu,mid_noise,hi,al,ah)
        can_alpha=lo>0 and valid_poly(row,pl,pu,lo,hi,al,mid_al)and valid_poly(row,pl,pu,lo,hi,mid_al,ah)
        if uh-ul>F(1,4):axis='u'
        elif lo==0 and hi>row.LAMBDA/2 and can_noise:axis='noise'
        elif uh-ul>F(1,8):axis='u'
        elif can_alpha and ah-al>F(1,2):axis='alpha'
        elif hi-lo>row.LAMBDA/4 and can_noise:axis='noise'
        elif can_alpha and ah-al>F(1,8):axis='alpha'
        elif uh-ul>F(1,16):axis='u'
        elif can_alpha and ah-al>F(1,16):axis='alpha'
        else:axis='p'
        if axis=='u':mid=(ul+uh)/2;left=(kk,pl,pu,ul,mid,lo,hi,al,ah);right=(kk,pl,pu,mid,uh,lo,hi,al,ah)
        elif axis=='noise':left=(kk,pl,pu,ul,uh,lo,mid_noise,al,ah);right=(kk,pl,pu,ul,uh,mid_noise,hi,al,ah)
        elif axis=='alpha':left=(kk,pl,pu,ul,uh,lo,hi,al,mid_al);right=(kk,pl,pu,ul,uh,lo,hi,mid_al,ah)
        else:mid=(pl+pu)/2;left=(kk,pl,mid,ul,uh,lo,hi,al,ah);right=(kk,mid,pu,ul,uh,lo,hi,al,ah)
        return dict(axis=axis,children=[visit(left,path+'0'),visit(right,path+'1')])
    tree=visit(domain,'')
    m.need(failed==0,f'unresolved discovery cells on {row.key} k={k}')
    obj=dict(schema='N5_ALL_TAYLOR_ROOT_V1',row_id=row.key,contract_path=row.path,contract_sha256=row.contract_sha,
      n=5,k=k,p=list(map(str,domain[1:3])),u=list(map(str,domain[3:5])),noise=list(map(str,domain[5:7])),tree=tree)
    obj_path=out_dir/f'{row.key}_k{k}.json'
    obj_path.write_text(json.dumps(obj,indent=2)+'\n')
    return obj_path,m.sha(obj_path),count,leaves

def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path)
    ap.add_argument('--rows',nargs='+',default=[e['row_id']for e in select_band('B2')])
    ap.add_argument('--use-dual',action='store_true');a=ap.parse_args()
    a.out.mkdir(parents=True,exist_ok=True);summary=[]
    for rkey in a.rows:
        row=m.Row(rkey);t0=time.monotonic();r_entries=[]
        for k in sorted(row.roots):
            p,h,nodes,leaves=build_root(row,k,a.out,use_dual=a.use_dual)
            r_entries.append(dict(k=k,object=str(p.relative_to(a.out.parent)),sha256=h,nodes=nodes,leaves=leaves))
        tot_leaves=sum(x['leaves']for x in r_entries)
        rec=dict(schema='N5_ALL_TAYLOR_ROW_SELECTION_V1',selector=rkey,row_id=row.key,contract_path=row.path,
          contract_sha256=row.contract_sha,roots=r_entries,total_leaves=tot_leaves,old_leaves=row.entry['old_leaves'],
          seconds=time.monotonic()-t0)
        summary.append(rec);print(json.dumps(rec),flush=True)
    target=dict(schema='N5_ALL_TAYLOR_MULTI_ROW_SELECTION_V1',rows=[
      dict(schema='N5_ALL_TAYLOR_ROW_SELECTION_V1',selector=r['selector'],row_id=r['row_id'],
        contract_path=r['contract_path'],contract_sha256=r['contract_sha256'],
        roots=[dict(k=x['k'],object=x['object'],sha256=x['sha256'])for x in r['roots']])for r in summary])
    (a.out.parent/'TARGET.json').write_text(json.dumps(target,indent=2)+'\n')

if __name__=='__main__':main()

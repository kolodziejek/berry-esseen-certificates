"""Propose four exact subdivision trees. Acceptance is separate."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from model import load_native,targets,CASE_IDS,final_margin,need
from polynomials import bernstein,split

def construct(p,box,depth=0):
    values=bernstein(p,box)
    if min(map(min,values))>=0:return {'coefficients':[[str(v)for v in row]for row in values]}
    need(depth<18,'discovery refinement limit; no acceptance')
    axis=depth%2
    left,right=split(box,axis)
    return {'axis':axis,'children':[construct(p,left,depth+1),construct(p,right,depth+1)]}

if __name__=='__main__':
    out=Path(sys.argv[1]);need(not out.exists(),'create-only candidate')
    c,_,_=load_native();ps=targets(c)
    obj={'schema':'JOINT_COUNT_FOURTH_TINY_TWO_ROWS_V1','comparison':'rho_B(C-C_B)<-lambda/1000',
         'loss_per_own_variance':'1/10','cases':[{'id':name,'tree':construct(ps[name],(F(0),F(1),F(0),F(1)))}for name in CASE_IDS]}
    out.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PROPOSED_NOT_ACCEPTED','final_margin':str(final_margin(c)),'candidate_bytes':out.stat().st_size}))

"""Exact read-only acceptance of four closed-rectangle polynomial witnesses."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from model import load_native,targets,CASE_IDS,final_margin,need,unique,sha
from polynomials import add,scale

def fields(d,expected):
    need(type(d)is dict and set(d)==set(expected),'exact object fields')

def fraction(s):
    need(type(s)is str,'rational string')
    q=F(s);need(str(q)==s,'canonical rational');return q

def expanded_basis(n,k):
    # C(n,k)x^k(1-x)^(n-k), expanded directly in powers.
    return {k+j:F(comb(n,k)*comb(n-k,j)*(-1)**j)for j in range(n-k+1)}

def accept_object(obj):
    fields(obj,('schema','comparison','loss_per_own_variance','cases'))
    need(obj['schema']=='JOINT_COUNT_FOURTH_TINY_TWO_ROWS_V1','fixed schema')
    need(obj['comparison']=='rho_B(C-C_B)<-lambda/1000' and obj['loss_per_own_variance']=='1/10','fixed strict target')
    need(type(obj['cases'])is list and [x.get('id')for x in obj['cases']]==list(CASE_IDS),'complete ordered four-case census')
    c,g,selection=load_native();ps=targets(c);records=[]
    for case in obj['cases']:
        fields(case,('id','tree'));fields(case['tree'],('coefficients',))
        p=ps[case['id']];nx=max(i for i,j in p);ny=max(j for i,j in p)
        rows=case['tree']['coefficients']
        need(type(rows)is list and len(rows)==nx+1,'complete first coordinate degree')
        need(all(type(row)is list and len(row)==ny+1 for row in rows),'complete second coordinate degree')
        values=[[fraction(v)for v in row]for row in rows]
        need(min(map(min,values))>=0,'nonnegative coefficients on entire closed rectangle')
        reconstructed={}
        for k,row in enumerate(values):
            for l,value in enumerate(row):
                if not value:continue
                tensor={(i,j):a*b for i,a in expanded_basis(nx,k).items()for j,b in expanded_basis(ny,l).items()}
                reconstructed=add(reconstructed,scale(tensor,value))
        need(reconstructed==p,'complete polynomial identity, independent inverse transform')
        records.append({'case':case['id'],'degree':[nx,ny],'coefficients':(nx+1)*(ny+1),
                        'minimum':str(min(map(min,values))),'zero_coefficients':sum(v==0 for row in values for v in row)})
    margin=final_margin(c);need(margin>0,'unchanged strict final score')
    return {'status':'PASS_TWO_NATIVE_PANELS_COMPLETE_TINY_PHASE','mathematical_scope':'conditional on existing same-law acquired row inputs; all n>=47, 0<lambda<=1/20, -1/2<=u<=1/2',
            'execution_scope':'fresh exact native normalization and four polynomial identities; no acquisition/integral replay',
            'normalization_gates':len(g),'cases':records,'selected_rows':[{'id':r['id'],'native_index':r['input_index'],'p':r['unchanged_row']['p']}for r in selection['rows']],
            'lower_loss_per_own_variance':'1/10','strict_reserve_beyond_original_target':str(margin),
            'native_target_changed':False,'all_83_rows_accepted':False,'whole_count_LOW_replaced':False,'fourier_calls':0}

if __name__=='__main__':
    path=Path(sys.argv[1]);obj=json.loads(path.read_text(),object_pairs_hook=unique)
    out=accept_object(obj);out['proof_object_sha256']=sha(path)
    print(json.dumps(out,indent=2,sort_keys=True))

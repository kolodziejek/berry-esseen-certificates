"""All83 actual signed-resource rows; exact cheap coefficient comparisons only."""
import ast
from fractions import Fraction as F
import hashlib
import json
from math import comb,isqrt
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from accept_objects import load,need
from coefficient_map import Family

NATIVE=Path(__file__).resolve().parent/'native'
FUNCTIONS=('need','down','up','roots','central_bound','quadratic_extrema','signed_k_error')
PINS={'contracted_kernel.py':'0367aae733dfe2d6467188d941d6fc8ccd7bb6f4bf3aa4c98dca3c4781534d22',
      'signed_resource47_table.json':'8ede412f88e5b0758dadf2590ca0f48f24b579cac22db6e4701cb6de532e6c39'}


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def root_interval(x):
    need(x>=0,'square-root argument')
    scale=10**8
    lo=F(isqrt(x.numerator*scale*scale//x.denominator),scale);hi=lo+F(1,scale)
    need(lo*lo<=x<=hi*hi,'independent root bracket')
    return lo,hi


def inputs():
    need(set(PINS)=={'contracted_kernel.py','signed_resource47_table.json'},'fixed comparison source set')
    for name,h in PINS.items():need(sha(NATIVE/name)==h,'pinned actual source '+name)
    table=load(NATIVE/'signed_resource47_table.json')
    need(table['schema']=='SIGNED_RESOURCE47_INPUT_V1' and table['N']==47,'actual source family')
    rows=table['panels'];need(type(rows)is list and len(rows)==83,'entire actual83-row cover')
    for j,z in enumerate(rows):
        need(type(z['index'])is int and z['index']==j,'actual row identity')
        need(list(map(F,z['p']))==[F(152+j,500),F(153+j,500)],'whole original probability interval')
    return rows


def main():
    need(len(sys.argv)==2,'new output directory')
    out=Path(sys.argv[1]);out.mkdir(exist_ok=False)
    rows=inputs();family=Family(Path(__file__).with_name('proof_objects.json'))
    source=(NATIVE/'contracted_kernel.py').read_text();tree=ast.parse(source)
    nodes=[z for z in tree.body if isinstance(z,ast.FunctionDef) and z.name in FUNCTIONS]
    need([z.name for z in nodes]==list(FUNCTIONS),'fixed original function identities')
    projected=ast.Module(body=nodes,type_ignores=[]);ns={'F':F,'comb':comb,'isqrt':isqrt}
    exec(compile(projected,str(NATIVE/'contracted_kernel.py'), 'exec'),ns)
    (out/'NATIVE_AST.txt').write_text(ast.dump(projected,include_attributes=False,indent=2)+'\n')
    captured=[];signed=0
    for row in rows:
        l,u=map(F,row['p']);theta=F(row['theta']);rho=F(row['rho']);al=F(row['A_lo']);bl=F(row['B_lo']);R=F(row['actual_radius'])
        p=dict(pl=l,pu=u,theta=theta,al=al,bl=bl)
        s0=min(l*(1-l),u*(1-u));su=max(l*(1-l),u*(1-u),F(1,4)if l<=F(1,2)<=u else F(0))
        A=(al,root_interval(u/(1-u))[1]);B=(bl,root_interval((1-l)/l)[1]);m=(root_interval((1-theta)*s0)[0],root_interval(su)[1])
        central=[]
        for r in(F(1),rho):
            old=ns['central_bound'](p,r);new=family.central(A,B,m,r)['G_upper']
            need(old==new,'actual central bound changed at row '+str(row['index']))
            central.append(dict(rho=str(r),native=str(old),new=str(new)))
        rq=root_interval((1-2*s0)**2/s0)[1]
        guard=0<l<u<F(1,2) and 3*min(al,bl)>=F(3,2)*rq
        entry={'row':row['index'],'actual_p':row['p'],'radius':str(R),'central':central,'conditional_native_guard':guard}
        if guard:
            ns['RADIUS']=R
            gv=(root_interval((1-theta)**3*(1-2*u)**2/(u*(1-u)))[0],root_interval((1-2*l)**2/(l*(1-l)))[1])
            rmin=root_interval((1-2*u*(1-u))**2/(u*(1-u)))[0]
            positive_mean=(root_interval((1-theta)*(1-u)/u)[0],root_interval((1-l)/l)[1])
            negative_mean=(root_interval((1-theta)*l/(1-l))[0],root_interval(u/(1-u))[1])
            old=ns['signed_k_error'](l,u,al,bl,theta,rho)
            new=family.conditional_k((bl,R),(al,R),positive_mean,negative_mean,(rmin,rho),gv,theta)
            need(old==new,'actual conditional-K bound changed at row '+str(row['index']))
            entry['conditional_native']=list(map(str,old));entry['conditional_new']=list(map(str,new));signed+=1
        captured.append(entry)
    result={'status':'PASS_ACTUAL_COEFFICIENT_COMPARISON','actual_source_rows':83,'central_calls':166,
            'conditional_K_calls':signed,'rows_without_conditional_guard':83-signed,
            'native_functions':list(FUNCTIONS),'source_pins':PINS,'native_numeric_exports_accepted':False,
            'fourier_calls':0,'scope':'coefficient routines on actual exported rows; source premises not reaccepted'}
    (out/'ROWS.json').write_text(json.dumps(captured,indent=2,sort_keys=True)+'\n')
    (out/'RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':main()

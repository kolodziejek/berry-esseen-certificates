"""Exact acceptance of one externally fixed algebraic family."""
from fractions import Fraction as F
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from poly import NAMES, add, decode, mul, power, scale, variable
from fixed_targets import MATRICES, bernstein_basis, factorizations, matrix_weight, targets


def need(ok, message):
    if not ok: raise ValueError(message)


def fields(o, names):
    need(type(o) is dict and set(o)==set(names),'exact fields')


def unique(pairs):
    out={}
    for k,v in pairs:
        need(k not in out,'duplicate JSON key');out[k]=v
    return out


def load(path):
    data=Path(path).read_bytes();need(len(data)<300000,'bounded input size')
    return json.loads(data,object_pairs_hook=unique)


def verify(o):
    need(__debug__ and not sys.flags.optimize,'optimized Python forbidden')
    fields(o,('format','scope','variables','polynomials','moment_matrices','central_transform','factorizations','square_witnesses'))
    need(o['format']=='SIGNED_COEFFICIENT_FAMILY_V1','fixed format')
    need(o['scope']=='universal_algebra_only_no_numeric_export_acceptance','fixed scope')
    need(o['variables']==list(NAMES),'fixed variable meanings')
    expected=targets();rows=o['polynomials']
    need(type(rows)is list and all(type(z)is dict for z in rows),'polynomial objects')
    need([z.get('id')for z in rows]==list(expected),'complete ordered polynomial family')
    parsed={}
    x,a=variable('x'),variable('a')
    for z in rows:
        fields(z,('id','coefficients'));name=z['id'];q=decode(z['coefficients'])
        actual=mul(power(add(x,scale(a,-1)),2),q) if name.startswith('conditional')else q
        need(actual==expected[name],'coefficient identity '+name)
        if name.startswith('conditional'):need(all(c>0 for c in q.values()),'positive conditional quotient')
        parsed[name]=q
    factor_ids=['P1_A','P1_B','P2_A','P2_B','G_B','G_at_B_rho_A','G_at_B_rho_rhorho','F_t']
    need(type(o['factorizations'])is list and [z.get('id')for z in o['factorizations']]==factor_ids,'complete derivative factorizations')
    for z in o['factorizations']:
        fields(z,('id','factors'));need(type(z['factors'])is list and 1<=len(z['factors'])<=4,'finite factored derivative')
        factors=[decode(p)for p in z['factors']]
        need(factors==factorizations()[z['id']],'fixed factor signs and order')
        need(mul(*factors)==expected[z['id']],'factored derivative identity')
    square_ids=['outer_positive_square','outer_negative_square','F_hessian_form']
    need(type(o['square_witnesses'])is list and [z.get('id')for z in o['square_witnesses']]==square_ids,'complete square witnesses')
    for z in o['square_witnesses']:
        fields(z,('id','terms'));need(type(z['terms'])is list and 1<=len(z['terms'])<=2,'fixed finite squares')
        result={}
        for term in z['terms']:
            fields(term,('weight','linear'));need(type(term['weight'])is str,'square weight rational')
            w=F(term['weight']);need(str(w)==term['weight'] and w>0,'positive square weight')
            linear=decode(term['linear']);need(all(sum(e)<=1 for e in linear),'linear square factors')
            result=add(result,scale(power(linear,2),w))
        need(result==expected[z['id']],'positive square reconstruction')
    matrices=o['moment_matrices']
    need(type(matrices)is list and all(type(z)is dict for z in matrices),'matrix objects')
    need([z.get('id')for z in matrices]==list(MATRICES),'complete weighted moment-matrix family')
    for z in matrices:
        fields(z,('id','weight','entries'));w=matrix_weight(z['id'])
        need(decode(z['weight'])==w,'fixed positive weight')
        need(type(z['entries'])is list and len(z['entries'])==3,'all symmetric matrix entries')
        for j,row in enumerate(z['entries']):need(decode(row)==mul(w,power(x,j)),'Gram entry identity')
    transform=o['central_transform']
    need(type(transform)is list and len(transform)==25,'all25 Bernstein rows')
    coefficients={}
    for z,(i,j) in zip(transform,((i,j)for i in range(5)for j in range(5))):
        fields(z,('index','weights'));need(type(z['index'])is list and all(type(v)is int for v in z['index']) and z['index']==[i,j],'ordered closed-square basis indices')
        rows=z['weights'];need(type(rows)is list,'finite transform weights')
        seen=[]
        for row in rows:
            need(type(row)is list and len(row)==3,'transform coefficient shape')
            k,h,value=row
            need(type(k)is int and type(h)is int and 0<=k<=4 and 0<=h<=4,'fixed transform domain')
            need(type(value)is str and len(value)<80,'transform rational')
            q=F(value);need(str(q)==value and q>0,'positive canonical transform coefficient')
            seen.append((k,h));coefficients[i,j,k,h]=q
        need(seen==sorted(set(seen)),'no duplicate or reordered transform monomial')
    # Independent inverse check: no use of the candidate-generation ratio formula.
    for k in range(5):
        for h in range(5):
            reconstructed=add(*(scale(bernstein_basis(i,j),coefficients.get((i,j,k,h),F(0)))
                                for i in range(5)for j in range(5)))
            need(reconstructed==mul(power(x,k),power(a,h)),'complete Bernstein inverse identity')
    return {'status':'PASS_SIGNED_COEFFICIENT_ALGEBRA','polynomial_cases':len(expected),
            'weighted_matrices':7,'bernstein_basis':25,'inverse_identities':25,
            'closed_domains':True,'native_numeric_exports_accepted':False}


if __name__=='__main__':
    need(len(sys.argv)==2,'one proof object path')
    print(json.dumps(verify(load(sys.argv[1])),sort_keys=True))

"""Positive boundary fixtures and corrupted-object rejection for the fixed family."""
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from accept_objects import load,need,verify
from coefficient_map import Family,coherent_coefficients,outer_bounds,zero_safe_quotient


def main():
    need(len(sys.argv)==2,'new controls directory')
    out=Path(sys.argv[1]);out.mkdir(exist_ok=False)
    obj=load(Path(__file__).with_name('proof_objects.json'));verify(obj)
    family=Family(Path(__file__).with_name('proof_objects.json'));cases=[]
    def mutation(name,fn):
        o=copy.deepcopy(obj);fn(o);cases.append((name,json.dumps(o,sort_keys=True).encode()))
    for field in ('polynomials','moment_matrices','central_transform','factorizations','square_witnesses'):
        mutation('missing_'+field,lambda o,f=field:o[f].pop())
        mutation('duplicate_'+field,lambda o,f=field:o[f].__setitem__(1,o[f][0]))
        mutation('reorder_'+field,lambda o,f=field:o[f].reverse())
    for i,z in enumerate(obj['polynomials']):
        mutation('false_'+z['id'],lambda o,i=i:o['polynomials'][i]['coefficients'][0].__setitem__(1,'19'))
    for i,z in enumerate(obj['moment_matrices']):
        mutation('false_weight_'+z['id'],lambda o,i=i:o['moment_matrices'][i]['weight'][0].__setitem__(1,'19'))
        mutation('false_entry_'+z['id'],lambda o,i=i:o['moment_matrices'][i]['entries'][2][0].__setitem__(1,'19'))
    for i,z in enumerate(obj['factorizations']):
        mutation('false_factor_'+z['id'],lambda o,i=i:o['factorizations'][i]['factors'][0][0].__setitem__(1,'19'))
    mutation('false_bernstein',lambda o:o['central_transform'][12]['weights'][0].__setitem__(2,'19'))
    mutation('boolean_basis_index',lambda o:o['central_transform'][0].update(index=[False,0]))
    mutation('negative_square_weight',lambda o:o['square_witnesses'][0]['terms'][0].update(weight='-1'))
    mutation('false_square_linear',lambda o:o['square_witnesses'][0]['terms'][0]['linear'][0].__setitem__(1,'19'))
    mutation('extra_claim',lambda o:o.update(native_numeric_exports_accepted=True))
    mutation('wrong_scope',lambda o:o.update(scope='full_acquisition_accepted'))
    mutation('noncanonical_fraction',lambda o:o['polynomials'][0]['coefficients'][0].__setitem__(1,'2/4'))
    mutation('float_coefficient',lambda o:o['polynomials'][0]['coefficients'][0].__setitem__(1,0.5))
    mutation('negative_exponent',lambda o:o['polynomials'][0]['coefficients'][0][0].__setitem__(0,-1))
    blob=json.dumps(obj);cases.append(('duplicate_JSON_key',('{"scope":"wrong",'+blob[1:]).encode()))
    rejected=[]
    for name,payload in cases:
        path=out/(name+'.json');path.write_bytes(payload)
        try:verify(load(path))
        except (ValueError,TypeError,KeyError,ZeroDivisionError) as exc:
            rejected.append({'name':name,'reason':str(exc),'sha256':hashlib.sha256(payload).hexdigest()})
        else:raise ValueError('false object accepted: '+name)
    # Real two-point laws, including zero support-deficit denominators and unequal radii.
    positive=[]
    for a in (F(1),F(1,2),F(3,2)):
        b=1/a;p=a*a/(1+a*a);q=1-p;m=p*b
        rho=p*b**3+q*a**3;gamma=p*b**3-q*a**3;beta=p*b*b-q*a*a
        mu4=p*b**4+q*a**4;eta=p*b**5+q*a**5;signed4=p*b**4-q*a**4
        exact=lambda v:(v,v)
        cell={'radii':(b,a),'m':exact(m),'a_plus':exact(p*b*b),'a_minus':exact(q*a*a),
              'b_plus':exact(p*b**3),'b_minus':exact(q*a**3),'rho':exact(rho),
              'beta':exact(beta),'gamma':exact(gamma),'A':exact(a),'B':exact(b),
              'mu4_upper':mu4,'eta5_upper':eta,'outer':{'amount':0,'plus_price':2,'minus_price':4,'plus_cap':0,'minus_cap':0}}
        result=coherent_coefficients(family,cell,rho)
        k1=signed4-3*beta-F(3,2)*rho*gamma
        j1=m*(b**3/3+a*b*b/2-a**3/6);j2=m*(b**4/4+a*b**3/3-a**4/12)
        truthU=j1+(mu4-3)/6;negativeKq=rho*mu4/2-eta/4+F(3,2)*beta*gamma-rho/2
        need(result['mu4']==exact(mu4) and result['eta5_upper']==eta,'exact two-point moment contractions')
        need(result['K1'][0]<=k1<=result['K1'][1] and result['U'][0]<=truthU<=result['U'][1],'signed exact-law containment')
        need(3*(rho*j1-j2)<=result['three_G_upper'] and negativeKq<=result['negative_Kq_upper'],'shared signed charges contain exact law')
        positive.append({'case':'two_point_a='+str(a),'passed':True})
    need(zero_safe_quotient(F(0),F(0))==0,'zero PSD row retained')
    try:zero_safe_quotient(F(1),F(0))
    except ValueError:pass
    else:raise ValueError('nonzero PSD cross entry divided by zero')
    budget={'amount':1,'plus_price':1,'minus_price':1,'plus_cap':1,'minus_cap':1}
    need(outer_bounds(3,3,1,2,budget)['three_G_upper']==F(3,8),'one budget cannot be spent twice')
    negative=family.central((F(3,2),F(3,2)),(F(2,3),F(2,3)),(F(2,5),F(1,2)),F(1))
    p1=F(2,3)**3/3+F(3,2)*F(2,3)**2/2-F(3,2)**3/6
    need(p1<0 and negative['J1_interval']==(p1/2,F(2,5)*p1),'negative central value uses correct m endpoint')
    need(family.conditional_k((1,2),(1,3),(1,1),(1,1),(1,2),(-1,1),0)==(0,0),'zero conditional variance boundary')
    positive += [{'case':name,'passed':True}for name in('PSD_zero_row','one_outer_budget','negative_m_endpoint','zero_conditional_variance')]
    domain_rejections=[]
    for name,call in [
      ('negative_outer_budget',lambda:outer_bounds(3,3,1,2,{**budget,'amount':-1})),
      ('zero_price',lambda:outer_bounds(3,3,1,2,{**budget,'plus_price':0})),
      ('reversed_rectangle',lambda:family.central((2,1),(1,2),(F(1,4),F(1,2)),1)),
      ('negative_mass',lambda:family.central((1,2),(1,2),(-1,1),1)),
      ('theta_one',lambda:family.conditional_k((1,2),(1,2),(1,1),(1,1),(1,2),(0,1),1))]:
        try:call()
        except ValueError:domain_rejections.append(name)
        else:raise ValueError('invalid cell domain accepted: '+name)
    result={'status':'PASS_FIXED_FAMILY_CONTROLS','object_rejections':len(rejected),'rejected':rejected,
            'positive_boundary_cases':positive,'invalid_domain_rejections':domain_rejections,
            'domain_rejection_means':'not applicable; never an automatic law exclusion',
            'native_numeric_exports_accepted':False}
    (out/'RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='rejected'},sort_keys=True))


if __name__=='__main__':main()

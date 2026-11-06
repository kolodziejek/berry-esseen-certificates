"""Exact negative and corruption controls for B0-band join, all-Taylor dispatch, PSD, and 295-contract selector."""
from pathlib import Path
import argparse,copy,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import accept_b0_band as reader
from selector import select_band,select_contract
m=reader.m

def main():
    ap=argparse.ArgumentParser();ap.add_argument('root_obj',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    obj=json.loads(a.root_obj.read_text(),object_pairs_hook=m.unique)
    row=m.Row(obj['row_id']);d=row.cell(obj['k'],obj['p'],obj['u'],obj['noise'])
    good=reader.admit_root(obj,row,d)
    m.need(good['taylor_leaves']>=1 and good['baseline_leaves']==0,'positive all-Taylor root verification')
    rejected=[]

    # 1. Selector disambiguation and validation controls across the 295-contract catalogue.
    selector_tests=[
      ('ambiguous B3 panel 59 by (band,index) alone',{'band':'B3','index':59}),
      ('ambiguous B2 panel 34 by (band,index) alone',{'band':'B2','index':34}),
      ('ambiguous B2 panel 50 by (band,index,p)',{'band':'B2','index':50,'p':['1/2','51/100']}),
      ('ambiguous band only',{'band':'BN'}),
      ('empty selector dict',{}),
      ('empty string selector',''),
      ('unknown string selector','BN999'),
      ('unknown selector key',{'band':'B0','unknown':1}),
      ('boolean panel index',{'band':'B0','index':True}),
      ('noncanonical p interval',{'band':'B0','index':50,'p':['2/4','51/100']}),
      ('reversed rho interval',{'band':'B0','index':50,'rho':['11/10','1']}),
      ('nonmatching contract query',{'band':'B0','index':31})]
    for name,bad_spec in selector_tests:
        try:select_contract(bad_spec)
        except(ValueError,TypeError,KeyError):rejected.append(name)
        else:raise ValueError('bad selector accepted: '+name)

    # Verify unambiguous selector resolution modes on B3_S0_59 vs B3_S2_59 and B0_053 (with k=4).
    s0=select_contract({'band':'B3','slab_family':'B3_S0_01','index':59})
    s2=select_contract({'band':'B3','slab_family':'B3_S2_01','index':59})
    s0_rho=select_contract({'band':'B3','index':59,'rho':['237/200','477/400']})
    s2_rho=select_contract({'band':'B3','index':59,'rho':['477/400','6/5']})
    b53=select_contract({'band':'B0','slab_family':'B0_BN_rest01','index':53})
    m.need(s0['sha256']==s0_rho['sha256']!=s2['sha256']==s2_rho['sha256'],'disambiguated B3 signed slabs')
    m.need(b53['roots']==[2,3,4]and 4 in m.Row('B0_053').roots,'k=4 root present in B0_053')

    # 2. Proof object & tree mutation controls.
    def first_leaf(tree):
        while 'children'in tree:tree=tree['children'][0]
        return tree
    tree_tests=[
      ('unknown analytic method',lambda z:first_leaf(z['tree']).update(method='gaussian_taylor_v1')),
      ('boolean method',lambda z:first_leaf(z['tree']).update(method=True)),
      ('missing theta',lambda z:first_leaf(z['tree']).pop('theta')),
      ('stored PASS leaf',lambda z:z.update(tree={'status':'PASS'})),
      ('failed leaf marker',lambda z:z.update(tree={'failed':{}})),
      ('missing child',lambda z:z.update(tree={'axis':'p','children':[z['tree']]})),
      ('unknown split axis',lambda z:z.update(tree={'axis':'phase','children':[z['tree'],z['tree']]})),
      ('wrong row_id',lambda z:z.update(row_id='B0_050')),
      ('wrong contract_path',lambda z:z.update(contract_path='work/cutoff5_20261020/root/count5_prepare_v1/pilots01/n5/B0/panel050/contract.json')),
      ('wrong contract_sha256',lambda z:z.update(contract_sha256='0'*64)),
      ('wrong n',lambda z:z.update(n=6)),
      ('boolean n',lambda z:z.update(n=True)),
      ('boolean k',lambda z:z.update(k=True)),
      ('changed p coverage',lambda z:z.update(p=['39/100','2/5']if z['p']!=['39/100','2/5']else['1/2','51/100'])),
      ('changed u coverage',lambda z:z.update(u=['-1/4','1/4'])),
      ('changed noise coverage',lambda z:z.update(noise=['0','1/10'])),
      ('noncanonical theta',lambda z:first_leaf(z['tree']).update(theta='2/2')),
      ('negative theta',lambda z:first_leaf(z['tree']).update(theta='-1/10')),
      ('negative dual price',lambda z:first_leaf(z['tree']).update(prices=['-1/10','0','0','0'])),
      ('noncanonical dual price',lambda z:first_leaf(z['tree']).update(prices=['2/2','0','0','0'])),
      ('wrong dual price count',lambda z:first_leaf(z['tree']).update(prices=['0','0','0'])),
      ('missing mixture count',lambda z:first_leaf(z['tree'])['q'].pop()),
      ('extra mixture count',lambda z:first_leaf(z['tree'])['q'].append(first_leaf(z['tree'])['q'][0])),
      ('bad closed atom at 0',lambda z:first_leaf(z['tree'])['q'][0].__setitem__(0,'0')),
      ('negative leading quartic',lambda z:first_leaf(z['tree'])['q'][0].__setitem__(4,'-1')),
      ('corrupted curvature PSD globally valid tiny quartics',lambda z:first_leaf(z['tree']).update(q=[['2','0','0','0','1/1000000000000']for _ in range(6)]))]
    for name,change in tree_tests:
        bad=copy.deepcopy(obj);change(bad)
        try:reader.admit_root(bad,row,d)
        except(ValueError,TypeError,KeyError)as e:
            if name=='corrupted curvature PSD globally valid tiny quartics':
                m.need('curvature-corrected exact PSD Hessian polynomials'in str(e),'isolated PSD rejection after passing 12 Sturm rays')
            rejected.append(name)
        else:raise ValueError('mutant accepted: '+name)

    # 3. Curvature, Gaussian domain, incomplete-root-selection, and B0-band join guards.
    b0_mock=[dict(row_id=e['row_id'],contract_sha256=e['sha256'],band=e['band'],slab_family=e['slab_family'],
      index=e['index'],p=list(e['p']),rho=list(e['rho']),roots=list(e['roots']))for e in select_band('B0')]
    m.need(reader.verify_b0_band_join(b0_mock)['contiguous_probability_joins']==23,'positive B0 band join verification')
    guards=[
      ('excessive negative squared numerator amin^2 > 3 dmin',lambda:row.target_tensors((1,row.pl,row.pu,-m.F(10),-m.F(9),m.F(0),row.LAMBDA))),
      ('probability outside (0,1)',lambda:m.gaussian(5,2,m.F(0),m.F(1,2),-m.F(1,4),m.F(1,4),m.F(0))),
      ('negative noise in Gaussian',lambda:m.gaussian(5,2,row.pl,row.pu,-m.F(1,4),m.F(1,4),-m.F(1,10))),
      ('incomplete root selection dropping k=4 on B0_053',lambda:reader.admit_row_selection({
        'schema':'N5_ALL_TAYLOR_ROW_SELECTION_V1','selector':'B0_053','row_id':'B0_053',
        'contract_path':b53['path'],'contract_sha256':b53['sha256'],
        'roots':[{'k':2,'object':str(a.root_obj),'sha256':m.sha(a.root_obj)},{'k':3,'object':str(a.root_obj),'sha256':m.sha(a.root_obj)}]})),
      ('duplicate JSON key',lambda:json.loads('{"method":"a","method":"b"}',object_pairs_hook=m.unique)),
      ('incomplete B0 band dropping panel 60',lambda:reader.verify_b0_band_join(b0_mock[:-1])),
      ('out-of-order B0 band swapping panels 45 and 46',lambda:reader.verify_b0_band_join(b0_mock[:8]+[b0_mock[9],b0_mock[8]]+b0_mock[10:])),
      ('broken B0 probability join at panel 45',lambda:reader.verify_b0_band_join([dict(r,p=['9/20','11/25'])if r['index']==45 else r for r in b0_mock])),
      ('corrupted B0 contract sha256 in band join',lambda:reader.verify_b0_band_join([dict(r,contract_sha256='0'*64)if r['index']==50 else r for r in b0_mock])),
      ('ambiguous multi-slab band in select_band',lambda:select_band('B2'))]
    for name,fn in guards:
        try:fn()
        except ValueError:rejected.append(name)
        else:raise ValueError('guard admitted: '+name)

    pins=reader.source_pins();pins['code/controls_b0_band.py']=m.sha(Path(__file__))
    a.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='PASS_EXACT_B0_BAND_ALL_TAYLOR_AND_SELECTOR_CONTROLS',positive_row=good['row_id'],positive_k=good['k'],
      negative_controls_count=len(rejected),negative_controls=rejected,source_sha256=pins,
      root_object_sha256=m.sha(a.root_obj),optimized_python_invoked=False)
    (a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='source_sha256'}))

if __name__=='__main__':main()

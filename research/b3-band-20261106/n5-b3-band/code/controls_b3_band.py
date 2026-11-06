"""Exact negative and corruption controls for B3-band join, 4-pair all-Taylor dispatch, PSD, and 295-contract selector."""
from pathlib import Path
import argparse,copy,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import accept_b3_band as reader
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
      ('ambiguous B3 panel 40 by (band,index) alone',{'band':'B3','index':40}),
      ('ambiguous B3 panel 50 by (band,index,p)',{'band':'B3','index':50,'p':['1/2','51/100']}),
      ('ambiguous band only',{'band':'B3'}),
      ('empty selector dict',{}),
      ('empty string selector',''),
      ('unknown string selector','B3_999'),
      ('unknown selector key',{'band':'B3','unknown':1}),
      ('boolean panel index',{'band':'B3','index':True}),
      ('noncanonical p interval',{'band':'BN','index':50,'p':['2/4','51/100']}),
      ('reversed rho interval',{'band':'BN','index':50,'rho':['23/20','11/10']}),
      ('nonmatching contract query',{'band':'B3','index':30})]
    for name,bad_spec in selector_tests:
        try:select_contract(bad_spec)
        except(ValueError,TypeError,KeyError):rejected.append(name)
        else:raise ValueError('bad selector accepted: '+name)

    # Verify unambiguous selector resolution modes on the 6 B3 contracts at panel 40 and 4 B3 contracts at panel 50.
    b3_40=[select_contract({'band':'B3','series':s,'index':40})for s in('S0','S2','T0','T1','T2','T3lower')]
    b3_50=[select_contract({'band':'B3','series':s,'index':50})for s in('S0','S2','T0','T2')]
    m.need(len({e['sha256']for e in b3_40})==6 and len({e['sha256']for e in b3_50})==4,'six distinct B3 contracts at panel 40 and four at panel 50')
    m.need(b3_50[1]['roots']==[1,2,3,4]and 4 in m.Row('B3_S2_01_050').roots,'k=1..4 roots present in B3_S2_01_050')

    # 2. Proof object & tree mutation controls.
    def first_leaf(tree):
        while 'children'in tree:tree=tree['children'][0]
        return tree
    tree_tests=[
      ('legacy 9-pair analytic method',lambda z:first_leaf(z['tree']).update(method='gaussian_taylor_both_halves_v1')),
      ('boolean method',lambda z:first_leaf(z['tree']).update(method=True)),
      ('missing theta',lambda z:first_leaf(z['tree']).pop('theta')),
      ('stored PASS leaf',lambda z:z.update(tree={'status':'PASS'})),
      ('failed leaf marker',lambda z:z.update(tree={'failed':{}})),
      ('missing child',lambda z:z.update(tree={'axis':'p','children':[z['tree']]})),
      ('unknown split axis',lambda z:z.update(tree={'axis':'phase','children':[z['tree'],z['tree']]})),
      ('wrong row_id',lambda z:z.update(row_id='B3_S0_01_031')),
      ('wrong contract_path',lambda z:z.update(contract_path='work/cutoff5_20261020/root/count5_prepare_v4/B3_S0_01/n5/B3/panel031/contract.json')),
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

    # 3. Curvature, Gaussian domain, incomplete-root-selection, and B3-band join guards.
    b3_mock=[dict(row_id=e['row_id'],contract_sha256=e['sha256'],band=e['band'],slab_family=e['slab_family'],
      series=e['series'],index=e['index'],p=list(e['p']),rho=list(e['rho']),beta=list(e['beta']),roots=list(e['roots']))for e in select_band('B3')]
    m.need(reader.verify_b3_band_join(b3_mock)['contiguous_probability_joins']==129,'positive B3 band join verification')
    guards=[
      ('excessive negative squared numerator amin^2 > 3 dmin',lambda:row.target_tensors((1,row.pl,row.pu,-m.F(10),-m.F(9),m.F(0),row.LAMBDA))),
      ('probability outside (0,1)',lambda:m.gaussian(5,2,m.F(0),m.F(1,2),-m.F(1,4),m.F(1,4),m.F(0))),
      ('negative noise in Gaussian',lambda:m.gaussian(5,2,row.pl,row.pu,-m.F(1,4),m.F(1,4),-m.F(1,10))),
      ('incomplete root selection dropping k=4 on B3_S2_01_050',lambda:reader.admit_row_selection({
        'schema':'N5_ALL_TAYLOR_ROW_SELECTION_V1','selector':'B3_S2_01_050','row_id':'B3_S2_01_050',
        'contract_path':b3_50[1]['path'],'contract_sha256':b3_50[1]['sha256'],
        'roots':[{'k':1,'object':str(a.root_obj),'sha256':m.sha(a.root_obj)},{'k':2,'object':str(a.root_obj),'sha256':m.sha(a.root_obj)},{'k':3,'object':str(a.root_obj),'sha256':m.sha(a.root_obj)}]})),
      ('duplicate JSON key',lambda:json.loads('{"method":"a","method":"b"}',object_pairs_hook=m.unique)),
      ('incomplete B3 band dropping last contract',lambda:reader.verify_b3_band_join(b3_mock[:-1])),
      ('out-of-order B3 band swapping S0 panels 45 and 46',lambda:reader.verify_b3_band_join(b3_mock[:14]+[b3_mock[15],b3_mock[14]]+b3_mock[16:])),
      ('broken B3 S0 probability join at panel 45',lambda:reader.verify_b3_band_join([dict(r,p=['9/20','11/25'])if r['row_id']=='B3_S0_01_045'else r for r in b3_mock])),
      ('corrupted B3 S0/T0 beta=1/5 join at panel 45',lambda:reader.verify_b3_band_join([dict(r,beta=['0','3/20'])if r['row_id']=='B3_S0_01_045'else r for r in b3_mock])),
      ('unknown band in select_band',lambda:select_band('B4'))]
    for name,fn in guards:
        try:fn()
        except ValueError:rejected.append(name)
        else:raise ValueError('guard admitted: '+name)

    pins=reader.source_pins();pins['code/controls_b3_band.py']=m.sha(Path(__file__))
    a.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='PASS_EXACT_B3_BAND_ALL_TAYLOR_AND_SELECTOR_CONTROLS',positive_row=good['row_id'],positive_k=good['k'],
      negative_controls_count=len(rejected),negative_controls=rejected,source_sha256=pins,
      root_object_sha256=m.sha(a.root_obj),optimized_python_invoked=False)
    (a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='source_sha256'}))

if __name__=='__main__':main()

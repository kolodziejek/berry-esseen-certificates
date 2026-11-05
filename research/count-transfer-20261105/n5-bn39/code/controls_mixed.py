"""Bounded exact controls for explicit mixed analytic dispatch and closed cover."""
from pathlib import Path
import argparse,ast,copy,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import accept_mixed as reader
m=reader.m

def main():
    ap=argparse.ArgumentParser();ap.add_argument('patch',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    patch=json.loads(a.patch.read_text(),object_pairs_hook=m.unique);d=(patch['domain'][0],)+tuple(map(m.F,patch['domain'][1:]));row=m.Row('BN39')
    obj=dict(schema='N5_THREE_CONTRACT_TRANSFER_MIXED_TAYLOR_V1',row_id='BN39',contract_sha256=row.contract_sha,n=5,k=d[0],p=list(map(str,d[1:3])),u=list(map(str,d[3:5])),noise=list(map(str,d[5:7])),tree=dict(method='gaussian_taylor_v1',**patch['candidate']))
    good=reader.admit(obj,row,d);m.need(good['taylor_leaves']==1 and good['baseline_leaves']==0,'actual Taylor dispatch');rejected=[]
    tests=[('unknown mixed method',lambda z:z['tree'].update(method='gaussian_taylor_v2')),
      ('boolean method',lambda z:z['tree'].update(method=True)),('missing theta',lambda z:z['tree'].pop('theta')),
      ('duplicate method field via wrong schema',lambda z:z['tree'].update(target='pass')),
      ('stored PASS leaf',lambda z:z.update(tree={'status':'PASS'})),('failed leaf',lambda z:z.update(tree={'failed':{}})),
      ('missing child',lambda z:z.update(tree={'axis':'p','children':[z['tree']]})),
      ('unknown split axis',lambda z:z.update(tree={'axis':'noise','children':[z['tree'],z['tree']]})),
      ('wrong original row',lambda z:z.update(row_id='B0_50')),('wrong original contract',lambda z:z.update(contract_sha256='0'*64)),
      ('wrong actual n',lambda z:z.update(n=6)),('boolean center',lambda z:z.update(k=True)),
      ('changed probability coverage',lambda z:z.update(p=['39/100','2/5'])),('changed phase coverage',lambda z:z.update(u=['-1/2','1/2'])),
      ('changed noise coverage',lambda z:z.update(noise=['0','1/10'])),('changed external target',lambda z:z.update(K='1')),
      ('noncanonical theta',lambda z:z['tree'].update(theta='2/2')),('negative rho weight',lambda z:z['tree'].update(theta='-1')),
      ('missing mixture count',lambda z:z['tree']['q'].pop()),('extra mixture count',lambda z:z['tree']['q'].append(z['tree']['q'][0])),
      ('bad closed atom',lambda z:z['tree']['q'][0].__setitem__(0,'0')),('negative quartic',lambda z:z['tree']['q'][0].__setitem__(4,'-1'))]
    for name,change in tests:
        bad=copy.deepcopy(obj);change(bad)
        try:reader.admit(bad,row,d)
        except(ValueError,TypeError,KeyError):rejected.append(name)
        else:raise ValueError('mutant accepted: '+name)
    taylor=reader.model_taylor.Row('BN39')
    guards=[('positive numerator', (2,m.F(39,100),m.F(2,5),m.F(1,4),m.F(1,2),m.F(0),row.LAMBDA)),
      ('right half unsupported by Taylor scalar',(2,m.F(1,2),m.F(51,100),-m.F(1,2),-m.F(1,4),m.F(0),row.LAMBDA)),
      ('excessive squared numerator',(2,m.F(39,100),m.F(2,5),-m.F(10),-m.F(9),m.F(0),row.LAMBDA))]
    for name,bad in guards:
        try:taylor.target_tensors(bad)
        except ValueError:rejected.append(name)
        else:raise ValueError('guard admitted: '+name)
    # Both duplicate-key methods and candidates must fail parsing before dispatch.
    try:json.loads('{"method":"baseline","method":"gaussian_taylor_v1"}',object_pairs_hook=m.unique)
    except ValueError:rejected.append('duplicate JSON method key')
    else:raise ValueError('duplicate JSON admitted')
    pins=reader.source_pins();pins['controls_mixed.py']=m.sha(Path(__file__))
    a.out.mkdir(parents=True,exist_ok=False);result=dict(status='PASS_EXACT_MIXED_DISPATCH_CONTROLS',positive=good,negative_controls=rejected,source_sha256=pins,patch_sha256=m.sha(a.patch),optimized_python_invoked=False)
    (a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='positive'}))
if __name__=='__main__':main()

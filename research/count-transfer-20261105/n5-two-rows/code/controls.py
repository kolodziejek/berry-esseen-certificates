"""Exact rejection controls for original-row identity and complete coverage.

No optimized interpreter is invoked. All mutations are disposable in-memory
objects; source contracts and selected proof objects remain unchanged.
"""
from pathlib import Path
import argparse,copy,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import accept,accept_row
m=accept.m
def main():
    ap=argparse.ArgumentParser();ap.add_argument('object',type=Path);ap.add_argument('selection',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    obj=json.loads(a.object.read_text(),object_pairs_hook=m.unique);row=m.Row('B2_S3_34');d=row.cell(3,(row.pl,row.pu),row.roots[3],(0,row.LAMBDA))
    good=accept.admit(obj,row,d);need=m.need;rejected=[]
    def q(z):
        n=z['tree']
        while'children'in n:n=n['children'][0]
        return n
    changes=[('wrong original row',lambda z:z.update(row_id='BN39')),('missing S3 identity',lambda z:z.update(row_id='B2_34')),
      ('wrong original contract',lambda z:z.update(contract_sha256='0'*64)),('different n',lambda z:z.update(n=6)),
      ('boolean n',lambda z:z.update(n=True)),('different root',lambda z:z.update(k=2)),
      ('smaller probability domain',lambda z:z.update(p=['17/50','69/200'])),
      ('smaller phase domain',lambda z:z.update(u=['-1/2','-1/4'])),
      ('smaller noise domain',lambda z:z.update(noise=['0','1/10'])),
      ('changed rho target',lambda z:z.update(rho_lower='1')),
      ('missing count',lambda z:q(z)['q'].pop()),('duplicate count array',lambda z:q(z)['q'].append(q(z)['q'][0])),
      ('reordered count array',lambda z:q(z)['q'].reverse()),
      ('float coefficient',lambda z:q(z)['q'][0].__setitem__(0,1.0)),('noncanonical coefficient',lambda z:q(z)['q'][0].__setitem__(0,'2/2')),
      ('bad closed-atom value',lambda z:q(z)['q'][0].__setitem__(0,'0')),('negative leading coefficient',lambda z:q(z)['q'][0].__setitem__(4,'-1')),
      ('negative rho weight',lambda z:q(z).update(theta='-1')),('too large rho weight',lambda z:q(z).update(theta='2')),
      ('unverified vertex table',lambda z:q(z).update(vertices=[])),('stored success flag',lambda z:z.update(status='PASS')),
      ('missing dyadic child',lambda z:z.update(tree={'axis':'p','children':[z['tree']]})),
      ('failed discovery leaf',lambda z:z.update(tree={'failed':{'status':'LP_FAILED'}}))]
    for name,f in changes:
        bad=copy.deepcopy(obj);f(bad)
        try:accept.admit(bad,row,d)
        except(ValueError,TypeError,KeyError):rejected.append(name)
        else:raise ValueError('mutant accepted: '+name)
    try:json.loads('{"k":3,"k":3}',object_pairs_hook=m.unique)
    except ValueError:rejected.append('duplicate JSON key')
    else:raise ValueError('duplicate JSON admitted')
    selection=json.loads(a.selection.read_text(),object_pairs_hook=m.unique);accept_row.admit_selection(selection,row)
    selection_changes=[('missing whole root',lambda z:z['roots'].pop()),('duplicate root',lambda z:z['roots'].__setitem__(1,copy.deepcopy(z['roots'][0]))),
      ('reordered roots',lambda z:z['roots'].reverse()),('wrong selection row',lambda z:z.update(row_id='BN39')),
      ('wrong selection source',lambda z:z.update(contract_sha256='0'*64)),('wrong object hash',lambda z:z['roots'][0].update(sha256='0'*64)),
      ('boolean root',lambda z:z['roots'][0].update(k=True)),('extra root',lambda z:z['roots'].append(copy.deepcopy(z['roots'][0])))]
    for name,f in selection_changes:
        bad=copy.deepcopy(selection);f(bad)
        try:accept_row.admit_selection(bad,row)
        except(ValueError,TypeError,KeyError):rejected.append(name)
        else:raise ValueError('selection mutant admitted: '+name)
    # Literal half-boundary and opposite probability-side extrema.
    need(m.variance_bounds(m.F(1,2),m.F(51,100))==(m.F(2499,10000),m.F(1,4)),'right half including1/2')
    need(m.variance_bounds(m.F(49,100),m.F(51,100))==(m.F(2499,10000),m.F(1,4)),'interior half crossing')
    a.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='PASS_TRANSFER_BOUNDARY_CONTROLS',positive_root='B2_S3_34:k3',positive_leaves=len(good['leaves']),rejected=rejected,
      optimized_interpreter_invoked=False,source_sha256={p.name:m.sha(p)for p in(HERE/'algebra.py',HERE/'model.py',HERE/'accept.py',HERE/'accept_row.py',Path(__file__))},
      object_sha256=m.sha(a.object),selection_sha256=m.sha(a.selection))
    (a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()

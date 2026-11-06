"""Disposable corruption checks and independent tensor reconstruction."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import argparse,copy,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import model as m
import accept
def main():
    ap=argparse.ArgumentParser();ap.add_argument('object',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    obj=json.loads(a.object.read_text(),object_pairs_hook=m.unique)
    domain=(2,['19/50','39/100'],['-1/100','1/100'])
    good=accept.admit(obj,*domain);rejections=[]
    def first(z):
        n=z['tree']
        while 'children'in n:n=n['children'][0]
        return n['q']
    mutations=[('missing field',lambda z:z.pop('n')),('wrong n',lambda z:z.update(n=6)),
      ('boolean n',lambda z:z.update(n=True)),('wrong k',lambda z:z.update(k=1)),
      ('wrong p',lambda z:z.update(p=['19/50','391/1000'])),
      ('wrong u',lambda z:z.update(u=['-1/2','1/2'])),('wrong contract',lambda z:z.update(contract_sha256='0'*64)),
      ('unknown target',lambda z:z.update(target='0')),
      ('missing subtree',lambda z:z['tree']['children'].pop()),
      ('extra subtree',lambda z:z['tree']['children'].append(copy.deepcopy(z['tree']['children'][0]))),
      ('wrong axis',lambda z:z['tree'].update(axis='noise')),
      ('missing count',lambda z:first(z).pop()),
      ('float coefficient',lambda z:first(z)[0].__setitem__(0,1.0)),
      ('noncanonical coefficient',lambda z:first(z)[0].__setitem__(0,'2/2')),
      ('negative leading',lambda z:first(z)[0].__setitem__(4,'-1')),
      ('closed atom majorant',lambda z:first(z)[0].__setitem__(0,'0')),
      ('swapped count functions',lambda z:first(z).__setitem__(slice(None),list(reversed(first(z)))))]
    for name,f in mutations:
        bad=copy.deepcopy(obj);f(bad)
        try:accept.admit(bad,*domain)
        except(ValueError,TypeError,KeyError,ZeroDivisionError):rejections.append(name)
        else:raise ValueError('mutant admitted '+name)
    try:json.loads('{"n":5,"n":5}',object_pairs_hook=m.unique)
    except ValueError:rejections.append('duplicate JSON key')
    else:raise ValueError('duplicate admitted')
    # Independent Bernstein inverse expansion on every monomial through9.
    transforms=0
    for d in(3,4,9):
      for power in range(d+1):
       for lo,hi in((F(19,50),F(39,100)),(-F(1,2),F(1,2)),(-F(1,100),F(1,100))):
        a0=tuple(F(int(i==power))for i in range(power+1));b=m.bernstein(a0,lo,hi,d)
        inverse=[F(0)]*(d+1)
        for j,bj in enumerate(b):
         for h in range(d-j+1):inverse[j+h]+=bj*comb(d,j)*comb(d-j,h)*(-1)**h
        expected=[F(comb(power,j))*lo**(power-j)*(hi-lo)**j if j<=power else F(0)for j in range(d+1)]
        m.need(inverse==expected,'independent inverse Bernstein identity');transforms+=1
    # Direct pointwise mixture expectation matches each 30-coefficient tensor.
    d=m.cell(2,['19/50','39/100'],['-1/100','1/100']);rows=m.tensors(*d);checks=0
    ps,us=F(77,200),F(1,200);sp=(ps-d[1])/(d[2]-d[1]);su=(us-d[3])/(d[4]-d[3]);q=1-ps
    bp=[F(comb(9,j))*sp**j*(1-sp)**(9-j)for j in range(10)];bu=[F(comb(4,j))*su**j*(1-su)**(4-j)for j in range(5)]
    idx=0
    from itertools import product
    for x,y in m.polygon(d[1],d[2]):
     for g0,g1 in product((-m.A0,F(0),min(m.D,d[2])),(m.A1,F(0),-min(m.D,1-d[1]))):
      row=rows[idx];idx+=1
      for j in range(6):
        t=(5-j)*x/q+j*y/ps;mu=(5-j)*g0*x/q+j*g1*y/ps
        fourth=(5-j)*g0*g0*x/q+j*g1*g1*y/ps+F(12,5)*t*t
        mom=[F(1),F(0),t,mu,fourth];mass=comb(5,j)*ps**j*q**(5-j)
        for degree in range(5):
          direct=ps**2*q**2*mass*sum(comb(degree,i)*(j-2-us)**(degree-i)*mom[i]for i in range(degree+1))
          tensor=row[j*5+degree];actual=sum(tensor[5*a+b]*bp[a]*bu[b]for a in range(10)for b in range(5))
          m.need(actual==direct,'independent direct common-moment tensor identity');checks+=1
    a.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='PASS_V1_CONTROLS',accepted_leaves=len(good['leaves']),rejected=rejections,inverse_transform_checks=transforms,
      direct_tensor_identities=checks,scope='No acquisition replay. Corrupt trees are disposable in-memory copies.',
      source_sha256={p.name:m.sha(p)for p in(HERE/'model.py',HERE/'accept.py',Path(__file__))},object_sha256=m.sha(a.object))
    (a.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()

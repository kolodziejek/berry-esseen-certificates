#!/usr/bin/env python3
"""Portable exact identity and rejection controls for the MID package."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import copy
import hashlib
import json
import sys

if not __debug__ or sys.flags.optimize:raise RuntimeError('unoptimized Python required')
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import accept_mid as acceptance
import mid_math as mathematics
from accept_mid_bound import bound


def value(poly,x):return sum(a*x**j for j,a in enumerate(poly))


def independent_identity(poly,node,a=F(0),b=F(1)):
    if 'split' in node:
        middle=(a+b)/2
        return independent_identity(poly,node['split'][0],a,middle)+independent_identity(poly,node['split'][1],middle,b)
    coefficients=list(map(F,node['bernstein']))
    assert len(coefficients)==5 and min(coefficients)>=0
    for y in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        reconstructed=sum(coefficients[j]*comb(4,j)*y**j*(1-y)**(4-j) for j in range(5))
        assert reconstructed==value(poly,a+(b-a)*y)
    return 1


def main():
    if len(sys.argv)!=2:raise ValueError('usage: controls.py PATH_TO_SIBLING_TINY')
    manifest=json.loads((HERE/'PACKAGE_FILES.json').read_text(),object_pairs_hook=acceptance.unique)
    for name,record in manifest['files'].items():
        p=HERE/name
        assert p.is_file() and not p.is_symlink()
        data=p.read_bytes()
        assert len(data)==record['bytes'] and hashlib.sha256(data).hexdigest()==record['sha256']
    proof=HERE/'proof_objects.json'
    obj=json.loads(proof.read_text(),object_pairs_hook=acceptance.unique)
    accepted=acceptance.accept(obj)
    count=0
    for row in obj['rows']:
        q=list(map(F,row['q']));b=F(row['phase'][1])
        for p,node in zip(mathematics.targets(q,b),row['proofs']):count+=independent_identity(p,node)
    assert count==accepted['bernstein_leaves']
    rejected=[]
    def reject(name,mutate):
        bad=copy.deepcopy(obj);mutate(bad)
        try:acceptance.accept(bad)
        except (ValueError,KeyError,TypeError,AttributeError,IndexError):rejected.append(name)
        else:raise AssertionError('mutation accepted: '+name)
    old_q=['-36057539/100000000','-215267141/100000000','170603249/100000000','1131571/6250000','0']
    q=list(map(F,old_q));b=F(-3,20);w=F(-100);x=(b-w)/mathematics.C
    assert value(q,w)<mathematics.R0*(x.numerator//x.denominator)
    reject('old_row69_false_far_ray',lambda o:o['rows'][69].__setitem__('q',old_q))
    reject('missing_left_ray',lambda o:o['rows'][0]['proofs'].pop())
    reject('missing_right_ray',lambda o:o['rows'][0]['proofs'].pop(0))
    reject('missing_phase_cell',lambda o:o['rows'].pop())
    reject('changed_phase_boundary',lambda o:o['rows'][0]['phase'].__setitem__(1,'-49/100'))
    reject('negative_fourth_coefficient',lambda o:o['rows'][0]['q'].__setitem__(4,'-1'))
    reject('changed_polynomial_constant',lambda o:o['rows'][0]['q'].__setitem__(0,str(F(o['rows'][0]['q'][0])+1)))
    reject('swapped_rays',lambda o:o['rows'][0]['proofs'].reverse())
    reject('boolean_row_index',lambda o:o['rows'][1].__setitem__('index',True))
    def negative_leaf(o):
        node=o['rows'][0]['proofs'][0]
        while 'split' in node:node=node['split'][0]
        node['bernstein'][0]='-1'
    reject('negative_Bernstein_leaf',negative_leaf)
    joined=bound(Path(sys.argv[1]).resolve(),proof)
    assert len(joined['input_rows'])==83 and joined['nonempty_rows']==71
    print(json.dumps({'status':'PASS_PORTABLE_MID_CONTROLS','polynomial_identity_leaves':count,
        'method':'five exact evaluation points identify each degree-at-most-four leaf polynomial',
        'negative_controls':rejected,'source_bound_input_rows':83,'nonempty_MID_rows':71,
        'empty_MID_rows':12,'strict_reserve':accepted['strict_reserve_beyond_original_target'],
        'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'new_acquisition_or_integral_replay':False},indent=2,sort_keys=True))


if __name__=='__main__':main()

"""Candidate construction from explicit manuscript coefficients; not acceptance."""
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from poly import NAMES


def p(*terms):
    # Handwritten sparse coefficients. A monomial is a tuple of variable names.
    rows = []
    for coefficient, monomial in terms:
        rows.append([[monomial.count(name) for name in NAMES], str(F(coefficient))])
    return sorted(rows)


P = {
 "P1": p((F(1,3),('b',)*3),(F(1,2),('a','b','b')),(-F(1,6),('a',)*3)),
 "P2": p((F(1,4),('b',)*4),(F(1,3),('a','b','b','b')),(-F(1,12),('a',)*4)),
 "G": p((F(1,3),('r','b','b','b')),(F(1,2),('r','a','b','b')),(-F(1,6),('r','a','a','a')),
         (-F(1,4),('b',)*4),(-F(1,3),('a','b','b','b')),(F(1,12),('a',)*4)),
 "P1_A": p((F(1,2),('b','b')),(-F(1,2),('a','a'))),
 "P1_B": p((1,('b','b')),(1,('a','b'))),
 "P2_A": p((F(1,3),('b',)*3),(-F(1,3),('a',)*3)),
 "P2_B": p((1,('b',)*3),(1,('a','b','b'))),
 "G_B": p((1,('r','b','b')),(1,('r','a','b')),(-1,('b',)*3),(-1,('a','b','b'))),
 "G_at_B_rho": p((F(1,12),('r',)*4),(F(1,6),('a','r','r','r')),(-F(1,6),('r','a','a','a')),(F(1,12),('a',)*4)),
 "G_at_B_rho_A": p((F(1,6),('r',)*3),(-F(1,2),('r','a','a')),(F(1,3),('a',)*3)),
 "G_at_B_rho_rhorho": p((1,('r','r')),(1,('r','a'))),
 "F": p((1,('x','x')),(2,('a','x')),(3,('a','a')),(-3,()),(-F(3,2),('t','x')),(-3,('t','a'))),
 "F_x": p((2,('x',)),(2,('a',)),(-F(3,2),('t',))),
 "F_a": p((2,('x',)),(6,('a',)),(-3,('t',))),
 "F_t": p((-F(3,2),('x',)),(-3,('a',))),
 "F_xx": p((2,())), "F_xa": p((2,())), "F_aa": p((6,())),
 "F_stationary": p((-3,()),(-F(27,32),('t','t'))),
 "F_hessian_form": p((2,('u','u')),(4,('u','v')),(6,('v','v'))),
 "outer_positive_square": p((1,('r','r')),(1,('a','a')),(4,('x','x')),(2,('r','a')),(-4,('r','x')),(-4,('a','x'))),
 "outer_negative_square": p((1,('b','b')),(1,('r','r')),(4,('x','x')),(2,('b','r')),(-4,('b','x')),(-4,('r','x'))),
 "projection_determinant": p((1,('u',)),(-1,('b','b','u')),(-1,('r','r')),(-1,('g','g')),(2,('b','r','g'))),
 "projection_square_form": p((1,('u',)),(-1,('b','b','u')),(-1,('r','r')),(-1,('g','g')),(2,('b','r','g'))),
 "conditional2": p((1,())),
 "conditional3": p((1,('x',)),(2,('a',))),
 "conditional4": p((1,('x','x')),(2,('a','x')),(3,('a','a'))),
 "conditional5": p((1,('x',)*3),(2,('a','x','x')),(3,('a','a','x')),(4,('a',)*3)),
}

def main():
    matrices=[]
    for name in ('H0','H1','H2','H3','L0','L1','L2'):
        k=int(name[1]); terms=lambda j: p((1,('x',)*(k+j))) if name[0]=='H' else p((1,('r',)+('x',)*(k+j)),(-1,('x',)*(k+j+1)))
        matrices.append({'id':name,'weight':terms(0),'entries':[terms(j) for j in range(3)]})
    transform=[]
    for i in range(5):
        for j in range(5):
            transform.append({'index':[i,j],'weights':[[k,h,str(F(comb(i,k),comb(4,k))*F(comb(j,h),comb(4,h)))]
                              for k in range(i+1) for h in range(j+1)]})
    factors={
      'P1_A': [p((F(1,2),())),p((1,('b',)),(-1,('a',))),p((1,('b',)),(1,('a',)))],
      'P1_B': [p((1,('b',))),p((1,('a',)),(1,('b',)))],
      'P2_A': [p((F(1,3),())),p((1,('b',)),(-1,('a',))),p((1,('b','b')),(1,('a','b')),(1,('a','a')))],
      'P2_B': [p((1,('b','b'))),p((1,('a',)),(1,('b',)))],
      'G_B': [p((1,('b',))),p((1,('a',)),(1,('b',))),p((1,('r',)),(-1,('b',)))],
      'G_at_B_rho_A': [p((F(1,6),())),p((1,('r',)),(-1,('a',))),p((1,('r',)),(-1,('a',))),p((1,('r',)),(2,('a',)))],
      'G_at_B_rho_rhorho': [p((1,('r',))),p((1,('r',)),(1,('a',)))],
      'F_t': [p((-F(3,2),())),p((1,('x',)),(2,('a',)))]}
    squares=[{'id':'outer_positive_square','terms':[{'weight':'1','linear':p((2,('x',)),(-1,('r',)),(-1,('a',)))}]},
             {'id':'outer_negative_square','terms':[{'weight':'1','linear':p((2,('x',)),(-1,('b',)),(-1,('r',)))}]},
             {'id':'F_hessian_form','terms':[{'weight':'2','linear':p((1,('u',)),(1,('v',)))},{'weight':'4','linear':p((1,('v',)))}]}]
    obj={'format':'SIGNED_COEFFICIENT_FAMILY_V1','scope':'universal_algebra_only_no_numeric_export_acceptance',
         'variables':list(NAMES),'polynomials':[{'id':key,'coefficients':P[key]} for key in P],
         'moment_matrices':matrices,'central_transform':transform,
         'factorizations':[{'id':key,'factors':value}for key,value in factors.items()], 'square_witnesses':squares}
    with Path(__file__).with_name('proof_objects.json').open('x') as f:
        json.dump(obj,f,indent=2);f.write('\n')


if __name__=='__main__': main()

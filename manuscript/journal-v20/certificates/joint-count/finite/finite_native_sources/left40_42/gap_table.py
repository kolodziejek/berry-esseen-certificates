"""Frozen accepted finite-binomial gap inputs; no floating arithmetic."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
HERE=Path(__file__).parent
MANIFEST=json.loads((HERE/'fixed_inputs.json').read_text())
for name,h in MANIFEST.items():
 if sha256((HERE/name).read_bytes()).hexdigest()!=h:raise ValueError('Fixed input '+name)
TABLES=[json.loads((HERE/('binomial%d.json'%n)).read_text())for n in(40,41,42)]
def epsilon(row):
 index=int(F(row['p'][0])*500);vals=[]
 for n,table in zip((40,41,42),TABLES):
  if type(table['n'])is not int or table['n']!=n:raise ValueError('Index scope')
  rows=[r for r in table['rows']if r['index']==index]
  if len(rows)!=1:raise ValueError('Binomial coverage')
  r=rows[0]
  if list(map(F,r['p']))!=list(map(F,row['p'])):raise ValueError('Same probability cell')
  vals.append(F(r['epsilon']))
 if min(vals)<=0:raise ValueError('Positive binomial gap')
 return min(vals)

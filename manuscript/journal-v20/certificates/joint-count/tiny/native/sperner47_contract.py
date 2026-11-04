"""Fixed scope for CONDITIONAL_SPERNER47_A; acquisition is separate."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from sperner47_kernel import rootup
HERE=Path(__file__).resolve().parent
INPUT_SHA256='b9d2aa15ad96181f5a8eb846e76ae296d2c2c8ed1a5975c6f389c2f7d14ff2b7'
def unique(rows):
 d={}
 for k,v in rows:
  if k in d:raise ValueError('Duplicate JSON key')
  d[k]=v
 return d
def input_table(raw=None):
 if raw is None:raw=(HERE/'conditional_input47.json').read_bytes()
 if sha256(raw).hexdigest()!=INPUT_SHA256:raise ValueError('Changed fixed conditional input table')
 d=json.loads(raw,object_pairs_hook=unique)
 if d['schema']!='CONDITIONAL_LOCAL47_COMPARATOR_INPUT_V1' or d['N']!=47:raise ValueError('Wrong conditional input schema')
 rows=d['panels']
 if len(rows)!=45 or F(rows[0]['p'][0])!=F('.38') or F(rows[-1]['p'][1])!=F('.47'):raise ValueError('Wrong probability cover')
 for i,r in enumerate(rows):
  if r['index']!=i or F(r['p'][0])>=F(r['p'][1]):raise ValueError('Invalid ordered probability cell')
  if i and rows[i-1]['p'][1]!=r['p'][0]:raise ValueError('Probability gap or overlap')
 return d
AMPLITUDES=['.375', '.35', '.35', '.35', '.35', '.35', '.35', '.35', '.35', '.325', '.325', '.325', '.325', '.325', '.3', '.3', '.3', '.3', '.3', '.3', '.3', '.275', '.275', '.275', '.275', '.275', '.25', '.25', '.25', '.25', '.25', '.225', '.225', '.225', '.225', '.225', '.2', '.2', '.2', '.2', '.2', '.2', '.2', '.2', '.2']
def config(row,sign):
 if sign not in(-1,1):raise ValueError('Invalid phase sign')
 amp=F(AMPLITUDES[row['index']]);fk='Fminus'if sign<0 else'Fplus';hk='H_minus'if sign<0 else'H_plus'
 return dict(N=47,T=F(row['T']),D=F(row['D']),theta=F(row['theta']),d0=F(row['d0']),H=F(row[hk]),
  C=F('.4253'),rho=F(row['rho']),beta_lo=F(row['beta_lo']),beta_hi=F(row['beta_hi']),
  amplitude=amp,maxnoise=F(row['lambda_max']),lower_buffer=amp*F(5,12),upper_buffer=amp*F(7,15),
  eta=F('0.00001'),phase_sign=sign,noise_min=F(0),strip=F('.55'),rebate=F(0),
  fd=rootup(max(F(47,46)**3,F(47,45))),third=F(24),pc=1,hc=16,lc=24,
  pl=F(row['p'][0]),pu=F(row['p'][1]),raw_quads=[(F(q['A']),F(q[fk]),F(q['Qbudget']))for q in row['quadratics']])

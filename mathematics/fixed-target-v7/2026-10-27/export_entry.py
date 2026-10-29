#!/usr/bin/env python3
"""Discovery-output exporter. Acceptance is a separate exact replay."""
from pathlib import Path
from fractions import Fraction as F
import json
import accept_entry as a
root=a.ROOT;source=root/'runs/fixed-target-v7-20261027/signed07/stdout.json'
z=json.loads(source.read_text(),object_pairs_hook=a.unique)
a.need(z['parameters']==dict(steps=6,beta=8,gamma=8,mean=2,cell_support=True,initial='quadratic'),'selected discovery invocation')
steps=[];panels=a.blank_panels()
for j,h in enumerate(z['history'][:4]):
    rows=[]
    for r in h['rows']:
        if r.get('prior_excluded'):
            rows.append(dict(index=r['index'],prior_excluded=True));continue
        o=r['output'];T=a.ceil(F(o['R'])) if o['active'] else F(-1);d=a.ceil(F(o['D'])) if o['active'] else F(-1)
        rows.append(dict(index=r['index'],radius=F(r['radius']),raw=T,defect=d,active=o['active'],excluded=o['excluded']))
        if j==3 and o['active']:
            decoded=[{k:(v if k=='cells' else F(v)) for k,v in p.items()} for p in o['panels']]
            a.pool(panels,decoded)
    steps.append(rows)
for z in panels:
    for k in a.KEYS:z[k]=a.ceil(z[k])
obj=a.encode(dict(format='FIXED_C_COARSE_ENTRY_V7',name=a.NAME,source_pins=a.PINS,steps=steps,panels=panels));a.shape(obj)
p=a.HERE/'entry-proof.json'
with p.open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
print(p)

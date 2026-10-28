"""Repeat the bounded compound diagnostic at formal 1/n=0; not coverage."""
from pathlib import Path
import json,math
p=Path(__file__).with_name('counts-v11-compound-discovery.py')
scope={'__name__':'discovery_helper','__file__':str(p)}
exec(compile(p.read_bytes(),str(p),'exec'),scope)
scope['N']=math.inf
cases=[scope['one'](i/100,w/4) for i in range(16) for w in range(5)]
print(json.dumps({'status':'DISCOVERY_ONLY_FORMAL_N_INFINITY_TRUNCATED_POISSON','cases':80,'worst':min(cases,key=lambda z:z['margin']),'failures':sum(x['margin']<=0 for x in cases)},indent=2))

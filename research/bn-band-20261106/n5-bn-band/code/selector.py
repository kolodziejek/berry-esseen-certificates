"""General external contract selector and complete BN-band join verifier for n=5.

Resolves any unambiguous contract from the 295-contract original n=5 census and
verifies that the 32 BN contracts (BN_034..BN_065 across gamma16_01, B0_BN_rest01,
and pilots01) form a gap-free contiguous partition of p in [17/50, 33/50]
under rho in [11/10, 23/20].
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
from algebra import HERE, need, rational, sha, unique

CENSUS_PIN='33193caa1a214ac84f938990c61468f269fdc1fb02cf7ed1781922bc2ccd4812'

def floor(x):return x.numerator//x.denominator
def ceil(x):return -((-x.numerator)//x.denominator)

def derive_roots(c):
    pl,pu=map(rational,c['p']);scale=rational(c['acquired_scale_upper'])
    hlo=5*pl-rational(c['Hminus'])*scale;hhi=5*pu+rational(c['Hplus'])*scale
    roots={k:(max(-F(1,2),hlo-k),min(F(1,2),hhi-k))for k in range(ceil(hlo-F(1,2)),floor(hhi+F(1,2))+1)}
    need(roots and all(0<=k<=5 and l<h for k,(l,h)in roots.items()),'nondegenerate complete threshold catalogue')
    return hlo,hhi,roots

@lru_cache(maxsize=1)
def load_catalogue():
    path=HERE.parent/'contracts'/'CENSUS_295.json'
    need(not path.is_symlink()and path.is_file()and sha(path)==CENSUS_PIN,'pinned 295-contract catalogue')
    raw=json.loads(path.read_text(),object_pairs_hook=unique)
    need(type(raw)is list and len(raw)==295,'complete 295-contract census')
    seen_paths=set();seen_shas=set();seen_bsi=set();entries=[]
    for item in raw:
        need(type(item)is dict and {'path','sha256','band','index','row','nearest_roots'}<=set(item),'catalogue entry schema')
        cpath=item['path'];csha=item['sha256'];band=item['band'];idx=item['index'];c=item['row']
        need(type(cpath)is str and type(csha)is str and len(csha)==64 and type(band)is str and band in('B0','BN','B2','B3'),'catalogue identity types')
        need(type(idx)is int and not isinstance(idx,bool)and c['index']==idx and c['n']==5 and c['K']=='0','literal n=5 K=0 panel index')
        parts=cpath.split('/');need(len(parts)==9 and parts[0]=='work'and parts[5]=='n5'and parts[6]==band and parts[8]=='contract.json','canonical original contract path')
        slab_family=parts[4];bsi=(band,slab_family,idx)
        need(cpath not in seen_paths and csha not in seen_shas and bsi not in seen_bsi,'unique path, sha256, and (band,slab_family,index)')
        seen_paths.add(cpath);seen_shas.add(csha);seen_bsi.add(bsi)
        _,_,roots=derive_roots(c)
        need(list(roots)==item['nearest_roots'],'verified complete nearest-root derivation')
        entries.append(dict(path=cpath,sha256=csha,band=band,slab_family=slab_family,index=idx,
          p=list(c['p']),rho=[c['rho_lower'],c['rho_upper']],beta=list(c['acquired_beta']),
          gamma=list(c['acquired_gamma']),roots=list(roots),old_leaves=item['old_leaves'],row=c))
    counts={(e['band'],e['index']):0 for e in entries}
    for e in entries:counts[(e['band'],e['index'])]+=1
    for e in entries:
        e['row_id']=f"{e['band']}_{e['index']:03d}"if counts[(e['band'],e['index'])]==1 else f"{e['slab_family']}_{e['index']:03d}"
    need(len({e['row_id']for e in entries})==295,'unique canonical row_id across 295 catalogue')
    return tuple(entries)

def select_band(band='BN'):
    need(type(band)is str and band in('B0','BN'),'unique-index band selector')
    rows=sorted([e for e in load_catalogue()if e['band']==band],key=lambda e:e['index'])
    need(len(rows)==(24 if band=='B0'else 32),'complete band contract count')
    for a,b in zip(rows,rows[1:]):
        need(b['index']==a['index']+1,'contiguous panel indices')
        need(rational(a['p'][1])==rational(b['p'][0]),'exact contiguous probability join')
    if band=='B0':
        need(rows[0]['index']==37 and rows[-1]['index']==60,'complete B0 index range 37..60')
        need(rational(rows[0]['p'][0])==F(37,100)and rational(rows[-1]['p'][1])==F(61,100),'exact B0 probability coverage [37/100, 61/100]')
        need(all(rational(r['rho'][0])==F(1)and F(1)<rational(r['rho'][1])<=F(11,10)for r in rows),'exact B0 rho floor 1 and ceiling <= 11/10')
    else:
        need(rows[0]['index']==34 and rows[-1]['index']==65,'complete BN index range 34..65')
        need(rational(rows[0]['p'][0])==F(17,50)and rational(rows[-1]['p'][1])==F(33,50),'exact BN probability coverage [17/50, 33/50]')
        need(all(rational(r['rho'][0])==F(11,10)and rational(r['rho'][1])==F(23,20)for r in rows),'exact BN rho slab [11/10, 23/20]')
    return tuple(rows)

CONTRACTS={e['row_id']:e['sha256']for e in select_band('BN')}

def select_contract(spec):
    """Resolve an unambiguous contract from row_id, path, sha256, or selector dict."""
    cat=load_catalogue()
    if type(spec)is str:
        need(spec!='','nonempty string selector')
        if any(e['row_id']==spec for e in cat):
            matches=[e for e in cat if e['row_id']==spec]
        elif len(spec)==64 and all(ch in'0123456789abcdef'for ch in spec):
            matches=[e for e in cat if e['sha256']==spec]
        else:
            matches=[e for e in cat if e['path']==spec]
        need(len(matches)==1,'unknown string contract selector: '+spec)
        return matches[0]
    need(type(spec)is dict and len(spec)>0,'nonempty selector mapping')
    allowed={'row_id','path','sha256','band','slab_family','index','p','rho','beta'}
    need(set(spec)<=allowed,'unsupported selector keys')
    matches=list(cat)
    if 'row_id'in spec:
        v=spec['row_id'];need(type(v)is str and any(e['row_id']==v for e in cat),'known catalogue row_id')
        matches=[e for e in matches if e['row_id']==v]
    if 'path'in spec:
        v=spec['path'];need(type(v)is str and v!='','canonical path string')
        matches=[e for e in matches if e['path']==v]
    if 'sha256'in spec:
        v=spec['sha256'];need(type(v)is str and len(v)==64 and all(c in'0123456789abcdef'for c in v),'canonical sha256 hex')
        matches=[e for e in matches if e['sha256']==v]
    if 'band'in spec:
        v=spec['band'];need(type(v)is str and v in('B0','BN','B2','B3'),'known band')
        matches=[e for e in matches if e['band']==v]
    if 'slab_family'in spec:
        v=spec['slab_family'];need(type(v)is str and v!='','nonempty slab_family')
        matches=[e for e in matches if e['slab_family']==v]
    if 'index'in spec:
        v=spec['index'];need(type(v)is int and not isinstance(v,bool)and 0<v<500,'integer panel index')
        matches=[e for e in matches if e['index']==v]
    for field in ('p','rho','beta'):
        if field in spec:
            pair=spec[field]
            need(type(pair)is list and len(pair)==2 and all(type(x)is str for x in pair),'canonical string interval for '+field)
            lo,hi=map(rational,pair);need(lo<=hi,'ordered interval for '+field)
            matches=[e for e in matches if list(map(rational,e[field]))==[lo,hi]]
    need(len(matches)!=0,'no matching original n=5 contract for selector')
    need(len(matches)==1,'ambiguous original n=5 contract selector: '+str(len(matches))+' matches')
    return matches[0]

"""General external contract selector for all 295 original n=5 contracts.

Handles both probability halves (0 < pl < pu < 1), rho floor 1, k=4 and 4-root
threshold catalogues, and every original B0/BN/B2/B3 signed slab. Ambiguous
queries (such as (band, index) when multiple signed slabs exist) are rejected.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
from algebra import HERE, need, rational, sha, unique

CENSUS_PIN='33193caa1a214ac84f938990c61468f269fdc1fb02cf7ed1781922bc2ccd4812'
CONTRACTS={
 'BN39':'8d2a6ec51bf43b45a7ce2de62d5ed734a90498924cb60c833a3976394eef3d9a',
 'B0_50':'2939dcca05896e1c6393c50944df8dd5e872efb26076a7304df45d9f6d07a93f',
 'B2_S3_34':'a9e2574fbb79e8d21d7bf6d5a9bc152ba6981878101c0dafd3eb7088233ba6d5',
 'BN38':'2b3f626ba3a9e954e4700bf206cf7a364f44958bb901b463198249dda2f37e48',
 'B0_53':'3878f4e5c91437c4c554d4d0b324f6ca295c8899312dba0b33f5473cd8f86b41',
 'B3_S0_59':'8a4952734e9cc1112231c39f80fdddd5acab6fa03baa97b718d268636c69c9dc',
 'B3_S2_59':'77489856c154551a3a403584c01a6649e503a2c1dc3e2b344075396b1e961a9b'}

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
    for alias,pin in CONTRACTS.items():
        bpath=HERE.parent/'contracts'/f'{alias}.json'
        need(not bpath.is_symlink()and bpath.is_file()and sha(bpath)==pin,'pinned bundled contract '+alias)
        rec=json.loads(bpath.read_text(),object_pairs_hook=unique)
        need(type(rec)is dict and rec.get('n')==5 and type(rec.get('rows'))is list and len(rec['rows'])==1,'literal n=5 bundled contract')
        match=[e for e in entries if e['sha256']==pin]
        need(len(match)==1 and match[0]['row']==rec['rows'][0],'bundled contract matches 295-catalogue')
        match[0]['row_id']=alias
    return tuple(entries)

def select_contract(spec):
    """Resolve an unambiguous contract from row_id, path, sha256, or selector dict."""
    cat=load_catalogue()
    if type(spec)is str:
        need(spec!='','nonempty string selector')
        if spec in CONTRACTS:
            matches=[e for e in cat if e.get('row_id')==spec]
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
        v=spec['row_id'];need(type(v)is str and v in CONTRACTS,'known bundled row_id')
        matches=[e for e in matches if e.get('row_id')==v]
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
            pair=spec[field];need(type(pair)in(list,tuple)and len(pair)==2,'two-endpoint interval for '+field)
            lo,hi=map(rational,pair);need(lo<hi,'ordered canonical rational interval for '+field)
            canon=[str(lo),str(hi)]
            matches=[e for e in matches if e[field]==canon]
    need(len(matches)>=1,'no matching original n=5 contract')
    need(len(matches)==1,f'ambiguous original n=5 contract selector: matches {len(matches)} contracts')
    return matches[0]

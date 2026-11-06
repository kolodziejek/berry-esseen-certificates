"""General external contract selector and complete B3-band join verifier for n=5.

Resolves any unambiguous contract from the 295-contract original n=5 census and
verifies that the 135 B3 contracts across the six sub-series S0 (35 contracts,
31..65), S2 (36 contracts, 31..66), T0 (22 contracts, 31..52), T1 (9 contracts,
32..40), T2 (22 contracts, 31..52), and T3lower (11 contracts, 31..41) form
gap-free contiguous probability partitions within each series (129 probability
joins) and join along beta = 1/5 (44 joins) and beta = 3/10 (20 joins).
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

def b2_series(slab_family):
    if slab_family=='B2_S0_01':return 'S0'
    if slab_family=='B2_S1_01':return 'S1'
    if slab_family=='B2_S2_01':return 'S2'
    if slab_family in('B2_S3_endpoint02','B2_S3_01'):return 'S3'
    return None

def b3_series(slab_family):
    return {'B3_S0_01':'S0','B3_S2_01':'S2','B3_T0_01':'T0','B3_T1_01':'T1','B3_T2_01':'T2','B3_T3lower_01':'T3lower'}.get(slab_family)

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
        sr=b2_series(slab_family)if band=='B2'else(b3_series(slab_family)if band=='B3'else band)
        entries.append(dict(path=cpath,sha256=csha,band=band,slab_family=slab_family,
          series=sr,index=idx,
          p=list(c['p']),rho=[c['rho_lower'],c['rho_upper']],beta=list(c['acquired_beta']),
          gamma=list(c['acquired_gamma']),roots=list(roots),old_leaves=item['old_leaves'],row=c))
    counts={(e['band'],e['index']):0 for e in entries}
    for e in entries:counts[(e['band'],e['index'])]+=1
    for e in entries:
        e['row_id']=f"{e['band']}_{e['index']:03d}"if e['band']in('B0','BN')else f"{e['slab_family']}_{e['index']:03d}"
        e['legacy_row_id']=f"{e['band']}_{e['index']:03d}"if counts[(e['band'],e['index'])]==1 else f"{e['slab_family']}_{e['index']:03d}"
    need(len({e['row_id']for e in entries})==295,'unique canonical row_id across 295 catalogue')
    return tuple(entries)

def select_b2_series():
    rows=[e for e in load_catalogue()if e['band']=='B2']
    need(len(rows)==104,'complete 104-contract B2 band count')
    series_map={}
    for sname,exp_len,idx_lo,idx_hi,p_lo,p_hi,r_lo,r_hi_max in(
      ('S0',32,33,64,F(33,100),F(13,20),F(23,20),F(467,400)),
      ('S1',18,33,50,F(33,100),F(51,100),F(23,20),F(467,400)),
      ('S2',34,32,65,F(8,25),F(33,50),F(467,400),F(237,200)),
      ('S3',20,32,51,F(8,25),F(13,25),F(467,400),F(237,200))):
        sr=sorted([e for e in rows if e['series']==sname],key=lambda e:e['index'])
        need(len(sr)==exp_len and sr[0]['index']==idx_lo and sr[-1]['index']==idx_hi,f'complete B2 {sname} index range')
        need(rational(sr[0]['p'][0])==p_lo and rational(sr[-1]['p'][1])==p_hi,f'exact B2 {sname} probability coverage')
        for a,b in zip(sr,sr[1:]):
            need(b['index']==a['index']+1 and rational(a['p'][1])==rational(b['p'][0]),f'contiguous B2 {sname} probability join')
        for r in sr:
            need(rational(r['rho'][0])==r_lo and r_lo<rational(r['rho'][1])<=r_hi_max,f'exact B2 {sname} rho bounds')
            blo,bhi=map(rational,r['beta']);need(-F(1)<blo<bhi<F(1),f'ordered B2 {sname} beta bounds')
            if sname in('S1','S3'):need(blo==F(1,5),f'exact B2 {sname} beta_lo == 1/5')
        series_map[sname]=tuple(sr)
    return series_map

def select_b3_series():
    rows=[e for e in load_catalogue()if e['band']=='B3']
    need(len(rows)==135,'complete 135-contract B3 band count')
    series_map={}
    for sname,exp_len,idx_lo,idx_hi,p_lo,p_hi,r_lo,r_hi_max,b_floor in(
      ('S0',35,31,65,F(31,100),F(33,50),F(237,200),F(477,400),None),
      ('S2',36,31,66,F(31,100),F(67,100),F(477,400),F(6,5),None),
      ('T0',22,31,52,F(31,100),F(53,100),F(237,200),F(477,400),F(1,5)),
      ('T1',9,32,40,F(8,25),F(41,100),F(237,200),F(477,400),F(3,10)),
      ('T2',22,31,52,F(31,100),F(53,100),F(477,400),F(6,5),F(1,5)),
      ('T3lower',11,31,41,F(31,100),F(21,50),F(477,400),F(6,5),F(3,10))):
        sr=sorted([e for e in rows if e['series']==sname],key=lambda e:e['index'])
        need(len(sr)==exp_len and sr[0]['index']==idx_lo and sr[-1]['index']==idx_hi,f'complete B3 {sname} index range')
        need(rational(sr[0]['p'][0])==p_lo and rational(sr[-1]['p'][1])==p_hi,f'exact B3 {sname} probability coverage')
        for a,b in zip(sr,sr[1:]):
            need(b['index']==a['index']+1 and rational(a['p'][1])==rational(b['p'][0]),f'contiguous B3 {sname} probability join')
        for r in sr:
            need(rational(r['rho'][0])==r_lo and r_lo<rational(r['rho'][1])<=r_hi_max,f'exact B3 {sname} rho bounds')
            blo,bhi=map(rational,r['beta']);need(-F(1)<blo<bhi<F(1),f'ordered B3 {sname} beta bounds')
            if b_floor is not None:need(blo==b_floor,f'exact B3 {sname} beta_lo == {b_floor}')
        series_map[sname]=tuple(sr)
    by_s={s:{r['index']:r for r in series_map[s]}for s in series_map}
    for left,right,b_join in(('S0','T0',F(1,5)),('T0','T1',F(3,10)),('S2','T2',F(1,5)),('T2','T3lower',F(3,10))):
        for idx,rr in by_s[right].items():
            ll=by_s[left][idx]
            need(ll['p']==rr['p']and rational(ll['beta'][1])==rational(rr['beta'][0])==b_join,f'exact B3 {left}/{right} beta={b_join} join')
    return series_map

def select_band(band='B3'):
    need(type(band)is str and band in('B0','BN','B2','B3'),'band selector')
    if band=='B2':
        smap=select_b2_series()
        return smap['S0']+smap['S1']+smap['S2']+smap['S3']
    if band=='B3':
        smap=select_b3_series()
        return smap['S0']+smap['S2']+smap['T0']+smap['T1']+smap['T2']+smap['T3lower']
    rows=sorted([e for e in load_catalogue()if e['band']==band],key=lambda e:e['index'])
    need(len(rows)==(24 if band=='B0'else 32),'complete band contract count')
    for a,b in zip(rows,rows[1:]):
        need(b['index']==a['index']+1,'contiguous panel indices')
        need(rational(a['p'][1])==rational(b['p'][0]),'exact contiguous probability join')
    return tuple(rows)

CONTRACTS={e['row_id']:e['sha256']for e in select_band('B3')}

def select_contract(spec):
    """Resolve an unambiguous contract from row_id, path, sha256, or selector dict."""
    cat=load_catalogue()
    if type(spec)is str:
        need(spec!='','nonempty string selector')
        if any(e['row_id']==spec for e in cat):
            matches=[e for e in cat if e['row_id']==spec]
        elif any(e['legacy_row_id']==spec for e in cat):
            matches=[e for e in cat if e['legacy_row_id']==spec]
        elif len(spec)==64 and all(ch in'0123456789abcdef'for ch in spec):
            matches=[e for e in cat if e['sha256']==spec]
        else:
            matches=[e for e in cat if e['path']==spec]
        need(len(matches)==1,'unknown string contract selector: '+spec)
        return matches[0]
    need(type(spec)is dict and len(spec)>0,'nonempty selector mapping')
    allowed={'row_id','path','sha256','band','slab_family','series','index','p','rho','beta'}
    need(set(spec)<=allowed,'unsupported selector keys')
    matches=list(cat)
    if 'row_id'in spec:
        v=spec['row_id'];need(type(v)is str and any(e['row_id']==v or e['legacy_row_id']==v for e in cat),'known catalogue row_id')
        matches=[e for e in matches if e['row_id']==v or e['legacy_row_id']==v]
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
    if 'series'in spec:
        v=spec['series'];need(type(v)is str and v!='','nonempty series')
        matches=[e for e in matches if e['series']==v]
    if 'index'in spec:
        v=spec['index'];need(type(v)is int and not isinstance(v,bool),'integer panel index')
        matches=[e for e in matches if e['index']==v]
    for key in('p','rho','beta'):
        if key in spec:
            v=spec[key];need(type(v)is list and len(v)==2,'two-endpoint interval selector for '+key)
            lo,hi=map(rational,v);need(lo<=hi,'ordered interval selector for '+key)
            matches=[e for e in matches if list(map(rational,e[key]))==[lo,hi]]
    need(len(matches)!=0,'no matching original n=5 contract for selector')
    need(len(matches)==1,f'ambiguous original n=5 contract selector ({len(matches)} matches; specify slab_family, rho, or beta)')
    return matches[0]

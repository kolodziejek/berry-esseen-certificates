"""Full-corner independent polynomial, cell-geometry, and source-domain-join audit of the 104-contract n=5 B2 band.

Gaussian lower polynomials, scalar constants and native univariate global-ray Sturm
acceptance are shared dependencies, not independently re-proved here.
Every cell's variance-allocation polygon, 4-endpoint-pair shifted support-square
fourth-moment envelope, all 4*V vertex-corner expanded moments, zero-dual raw-cubic
price, all 4*4*V inverse polynomial transforms, and the 104-contract B2 sub-series
contiguous probability and beta=1/5 joins are checked independently.
"""
from pathlib import Path,PurePosixPath
from fractions import Fraction as F
from itertools import combinations,product
from math import comb,isqrt
import hashlib,json,sys,time
HERE=Path(__file__).resolve().parent
PKG_MANIFEST='4af1dd9fb86729227d560c667638a242fb80771ade87d76d41046b0436a618cf'
IP_PIN='18f11a2c8a0bd3620cdebf71dad8c2f7a7880c8b8b9637ab792c0174b860c0c1'

def need(x,msg):
    if not x:raise ValueError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def unique(items):
    d={}
    for k,v in items:need(k not in d,'duplicate JSON key');d[k]=v
    return d
def read(p):return json.loads(Path(p).read_text(),object_pairs_hook=unique)
def rat(s):
    need(type(s)is str,'rational string');v=F(s);need(str(v)==s,'canonical rational');return v
def sqrt_bounds(x):
    need(x>=0,'nonnegative square-root input');scale=10**30;k=isqrt(x.numerator*scale*scale//x.denominator)
    return F(k,scale),F(k+1,scale)
def inverse(b,degree):
    need(len(b)==degree+1,'univariate degree');out={}
    for j,c in enumerate(b):
        for i in range(j,degree+1):out[i]=out.get(i,F(0))+c*comb(degree,j)*comb(degree-j,i-j)*(-1)**(i-j)
    return {i:c for i,c in out.items()if c}
def local(poly,pl,pu):
    out={}
    for(i,j),c in poly.items():
        need(j==0,'univariate dual or Hessian')
        for h in range(i+1):out[h]=out.get(h,F(0))+c*comb(i,h)*pl**(i-h)*(pu-pl)**h
    return {i:c for i,c in out.items()if c}
def derive_roots(row):
    pl,pu=map(rat,row['p']);scale=rat(row['acquired_scale_upper']);lo=5*pl-rat(row['Hminus'])*scale;hi=5*pu+rat(row['Hplus'])*scale
    ceil=lambda x:-((-x.numerator)//x.denominator)
    floor=lambda x:x.numerator//x.denominator
    roots={k:(max(-F(1,2),lo-k),min(F(1,2),hi-k))for k in range(ceil(lo-F(1,2)),floor(hi+F(1,2))+1)}
    need(roots and all(0<=k<=5 and a<b for k,(a,b)in roots.items()),'complete original threshold cover')
    return roots
def leaves(node,d,path=''):
    need(type(node)is dict and len(path)<=20,'finite canonical tree')
    if set(node)in({'q','theta','method'},{'q','theta','prices','method'}):
        need(node['method']=='gaussian_taylor_both_halves_4pair_v1','actual 4-pair leaf method');return [(path,node,d)]
    need(set(node)=={'axis','children'}and node['axis']in('p','u','noise','alpha')and type(node['children'])is list and len(node['children'])==2,'complete dyadic split')
    at={'p':1,'u':3,'noise':5,'alpha':7}[node['axis']];mid=(d[at]+d[at+1])/2;left=list(d);right=list(d);left[at+1]=mid;right[at]=mid
    return leaves(node['children'][0],tuple(left),path+'0')+leaves(node['children'][1],tuple(right),path+'1')

def independent_geometry(row,pl,pu,lo,hi,al,ah,Rhi,Glo,Ghi,alg):
    vmin=min(pl*(1-pl),pu*(1-pu));vmax=max([pl*(1-pl),pu*(1-pu)]+([F(1,4)]if pl<=F(1,2)<=pu else []))
    need(2*vmin>row.MEAN_LO**2,'mean/noise monotonicity in v')
    hi_eff=min(hi,5*(vmax*vmax/row.MEAN_LO**2-vmax))
    need(lo<hi_eff and 0<=al<ah<=1,'nonempty mean-noise/alpha slab')
    r=sqrt_bounds(vmin+lo/5)[0]
    r0=min(row.D,pu-row.NEG_LO*r);r1=min(row.D,1-pl-row.POS_LO*r)
    need(r0>=0 and r1>=0,'nonnegative inward ceilings')
    def corners_from(xmin,ymin):
        s0_min=xmin/(1-pl);s1_min=ymin/pu
        d0_out=min(row.A0,s0_min/row.A0);d0_in=min(r0,s0_min/r0)if r0>0 else F(0)
        d1_out=min(row.A1,s1_min/row.A1);d1_in=min(r1,s1_min/r1)if r1>0 else F(0)
        g0_lo=-row.A0+d0_out;g0_hi=max(g0_lo,r0-d0_in)
        g1_hi=row.A1-d1_out;g1_lo=min(g1_hi,-r1+d1_in)
        K0=lambda g:(r0-row.A0-2*d0_in)*g+row.A0*r0-(row.A0-2*r0)*d0_in-d0_in*d0_in
        K1=lambda g:(row.A1-r1+2*d1_in)*g+row.A1*r1-(row.A1-2*r1)*d1_in-d1_in*d1_in
        c0=((g0_lo,K0(g0_lo)),(g0_hi,K0(g0_hi)))
        c1=((g1_hi,K1(g1_hi)),(g1_lo,K1(g1_lo)))
        return c0,c1,g0_lo,g0_hi,g1_lo,g1_hi
    rhi=alg.mul(alg.V,(row.BHI-1,F(2)));rlo=alg.mul(alg.V,(1-row.BLO,-F(2)))
    base_planes=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),hi_eff/5),(-F(1),-F(1),-lo/5),
      (-(1+row.BHI),1-row.BHI,max(alg.bernstein(rhi,pl,pu,3))),
      (1+row.BLO,-(1-row.BLO),max(alg.bernstein(rlo,pl,pu,3))),
      (al,-(1-al),F(0)),(-ah,1-ah,F(0))]
    def solve_planes(planes):
        out=set()
        for(a,b,c),(d,e,f)in combinations(planes,2):
            det=a*e-b*d
            if not det:continue
            x=(c*e-b*f)/det;y=(a*f-c*d)/det
            if all(A*x+B*y<=C for A,B,C in planes):out.add((x,y))
        need(len(out)>=3,'nondegenerate independent polygon')
        return tuple(sorted(out))
    pts=solve_planes(base_planes)
    if lo>0 or(al,ah)!=(F(0),F(1)):
        xmin0=min(x for x,y in pts);ymin0=min(y for x,y in pts)
        _,_,g0_lo,g0_hi,g1_lo,g1_hi=corners_from(xmin0,ymin0)
        bvG=alg.bernstein(alg.mul(alg.V,(F(1),-F(2))),pl,pu,3);vG_min,vG_max=min(bvG),max(bvG)
        planes=base_planes+[
          (3*pl-g0_hi,3*(1-pu)+g1_lo,Rhi-vmin*(1-2*vmin)),
          (-(3*pu-g0_lo),3*(1-pu)+g1_lo,Ghi-vG_min),
          (3*pl-g0_hi,-(3*(1-pl)+g1_hi),-Glo+vG_max)]
        pts=solve_planes(planes)
    xmin=min(x for x,y in pts);ymin=min(y for x,y in pts)
    c0,c1,*_=corners_from(xmin,ymin)
    return pts,c0,c1,hi_eff

def main():
    need(__debug__ and not sys.flags.optimize and len(sys.argv)==3,'ordinary Python PACKAGE NEW_OUTPUT')
    pkg=Path(sys.argv[1]).resolve();out=Path(sys.argv[2]);need(not out.exists(),'fresh output')
    need(sha(pkg/'FILES.json')==PKG_MANIFEST and sha(HERE/'independent_polys.py')==IP_PIN,'fixed supplied source epoch')
    mf=read(pkg/'FILES.json');tracked=[Path(__file__),HERE/'independent_polys.py',pkg/'FILES.json'];paths=set()
    for z in mf['files']:
        rel=z['path'];q=PurePosixPath(rel);need(not q.is_absolute()and '..'not in q.parts and str(q)==rel and rel not in paths,'safe unique manifest path');paths.add(rel)
        p=pkg/rel;need(p.is_file()and not p.is_symlink()and p.stat().st_size==z['size']and sha(p)==z['sha256'],'fixed package bytes');tracked.append(p)
    before={str(p):sha(p)for p in tracked};started=time.monotonic()
    sys.path.insert(0,str(HERE));import independent_polys as ip
    sys.path.insert(0,str(pkg/'code'));import algebra as alg;import gaussian_scalar as gs;import selector as sel;import model_all_taylor as mat

    # 1. Audit 295-contract catalogue, band counts (B0=24, BN=32, B2=104, B3=135), and 104-contract B2 band join.
    cat=sel.load_catalogue();need(len(cat)==295,'catalogue size');groups={};root_census={};band_counts={'B0':0,'BN':0,'B2':0,'B3':0}
    for c in cat:
        band_counts[c['band']]+=1
        rr=derive_roots(c['row']);need(list(rr)==c['roots'],'independent original threshold derivation');root_census[c['sha256']]=rr
        groups.setdefault((c['band'],c['index']),[]).append(c)
    need(band_counts=={'B0':24,'BN':32,'B2':104,'B3':135},'exact 295 band distribution')
    ambiguous=unique_pairs=0
    for(band,index),matches in groups.items():
        if len(matches)>1:
            ambiguous+=1
            try:sel.select_contract(dict(band=band,index=index))
            except ValueError as e:need('ambiguous original n=5 contract selector'in str(e),'exact ambiguity rejection')
            else:raise ValueError('ambiguous query accepted')
        else:unique_pairs+=1;need(sel.select_contract(dict(band=band,index=index))['sha256']==matches[0]['sha256'],'unique selector')
        for c in matches:need(sel.select_contract(dict(band=band,index=index,slab_family=c['slab_family']))['sha256']==c['sha256'],'disambiguated selector')
    need((ambiguous,unique_pairs)==(68,58),'complete selector census')

    b2_rows=sel.select_band('B2')
    need(len(b2_rows)==104,'complete 104-contract B2 sequence')
    ROWS=tuple(r['row_id']for r in b2_rows)

    # 2. Audit target, controls01, and replay01 receipts.
    target=read(pkg/'TARGET.json');need(tuple(r['row_id']for r in target['rows'])==ROWS,'fixed 104 B2 selected rows')
    ctrl=read(pkg/'evidence/controls01/accepted/RESULT.json')
    need(ctrl['status']=='PASS_EXACT_B2_BAND_ALL_TAYLOR_AND_SELECTOR_CONTROLS'and ctrl['negative_controls_count']==48,'controls01 verified')
    native_batch=read(pkg/'evidence/replay01/accepted/RESULT.json')
    need(all(sha(pkg/p)==h for p,h in native_batch['source_sha256'].items()),'native admitted source epoch matches final package')
    need(native_batch['band_join']['contiguous_probability_joins']==100 and native_batch['band_join']['beta_joins_s0_s1']==18 and native_batch['band_join']['beta_joins_s2_s3']==20,'native band_join matches')

    count=dict(rows=0,roots=0,leaves=0,psd=0,score=0,positive_curvature=0,zero_curvature=0,
      nonpositive_numerator=0,sign_crossing_numerator=0,positive_numerator=0,priced_leaves=0,noise_split_nodes=0,alpha_split_nodes=0,
      independent_geometry_checks=0,independent_vertex_corner_rows=0,independent_score_coefficients=0,independent_inverse_identities=0)
    summaries=[];isolated_psd=None;seen_objects=set()

    for rt in target['rows']:
        count['rows']+=1;row=mat.Row(rt['row_id']);roots=root_census[row.contract_sha]
        need(rt['contract_sha256']==row.contract_sha and rt['contract_path']==row.path and [x['k']for x in rt['roots']]==list(roots),'complete original row root census')
        for rm in rt['roots']:
            count['roots']+=1;k=rm['k'];p=pkg/rm['object'];need(p not in seen_objects and sha(p)==rm['sha256'],'unique fixed object');seen_objects.add(p);obj=read(p)
            need(set(obj)=={'schema','row_id','contract_path','contract_sha256','n','k','p','u','noise','tree'},'complete object header')
            need(obj['schema']=='N5_ALL_TAYLOR_ROOT_V1'and obj['row_id']==rt['row_id']and type(obj['n'])is int and obj['n']==5 and type(obj['k'])is int and obj['k']==k,'actual row/index')
            need(obj['contract_path']==row.path and obj['contract_sha256']==row.contract_sha and obj['p']==list(map(str,(row.pl,row.pu)))and obj['u']==list(map(str,roots[k]))and obj['noise']==['0',str(row.LAMBDA)],'complete source-bound p/phase/noise domain')

            def count_axis(node,ax):
                if 'axis'not in node:return 0
                return (1 if node['axis']==ax else 0)+sum(count_axis(c,ax)for c in node['children'])
            count['noise_split_nodes']+=count_axis(obj['tree'],'noise')
            count['alpha_split_nodes']+=count_axis(obj['tree'],'alpha')

            domain=(k,row.pl,row.pu,*roots[k],F(0),row.LAMBDA,F(0),F(1));ls=leaves(obj['tree'],domain);need(len(ls)==rm['leaves'],'actual target leaf count')
            native=read(pkg/'evidence/replay01/accepted'/rt['row_id']/f'k{k}.json');need(native['object_sha256']==rm['sha256'],'native actual object binding')
            native_by={z['path']:z for z in native['leaves']};need(len(native_by)==len(native['leaves'])and set(native_by)=={z[0]for z in ls},'native leaf-path join')

            for path,leaf,d in ls:
                count['leaves']+=1;kk,pl,pu,ul,uh,lo,hi,al,ah=d
                need(type(leaf['q'])is list and len(leaf['q'])==6,'six common count polynomials')
                qs=[]
                for q in leaf['q']:need(type(q)is list and len(q)==5,'five coefficients');qs.append(list(map(rat,q)));need(qs[-1][4]>0,'positive quartic')
                theta=rat(leaf['theta']);need(0<=theta<=1,'convex price')
                need('prices'not in leaf,'zero-dual-price B2 leaf')
                vmin=min(pl*(1-pl),pu*(1-pu));vmax=max([pl*(1-pl),pu*(1-pu)]+([F(1,4)]if pl<=F(1,2)<=pu else []));dmin=5*vmin+lo
                amin=kk+ul-5*pu;amax=kk+uh-5*pl;need(min(amin,F(0))**2<=3*dmin,'negative curvature guard');slo=sqrt_bounds(dmin)[0];need(slo>0,'positive denominator')
                if amax<=0:count['nonpositive_numerator']+=1
                elif amin<0:count['sign_crossing_numerator']+=1
                else:count['positive_numerator']+=1
                M=3*max(amax,F(0))*alg.normal.PHI_HI/(4*dmin*dmin*slo);need(M==gs.curvature(5,kk,pl,pu,ul,uh,lo)[0],'independent curvature bound')
                count['positive_curvature'if M>0 else'zero_curvature']+=1

                H=[{},{},{}]
                for j,q in enumerate(qs):
                    mass=ip.scale(ip.mul(ip.power(ip.P,j),ip.power(ip.Q,5-j)),F(comb(5,j)));a=ip.scale(ip.P,5-j);b=ip.scale(ip.Q,j);coef=F(24,5)*q[4]
                    for z,t in enumerate((ip.mul(a,a),ip.mul(a,b),ip.mul(b,b))):H[z]=ip.add(H[z],ip.scale(ip.mul(mass,t),coef))
                H=[ip.add(h,ip.scale(ip.V2,-25*M))for h in H];det=ip.add(ip.mul(H[0],H[2]),ip.scale(ip.mul(H[1],H[1]),-1));mins=[]
                for poly_h,degree in ((H[0],7),(H[2],7),(det,14)):
                    b=alg.bernstein(tuple(poly_h.get((i,0),F(0))for i in range(degree+1)),pl,pu,degree);need(inverse(b,degree)==local(poly_h,pl,pu),'independent Hessian inverse');need(min(b)>=0,'PSD');count['psd']+=degree+1;mins.append(str(min(b)))
                if isolated_psd is None and M>0:
                    tiny=[[F(2),F(0),F(0),F(0),F(1,10**12)]for _ in range(6)]
                    for q in tiny:alg.sturm.positive(alg.compact_ray(q,-1,F(1)));alg.sturm.positive(alg.compact_ray(q,1,F(0)))
                    try:row.psd_check(tiny,pl,pu,M)
                    except ValueError as e:need('curvature-corrected exact PSD'in str(e),'isolated PSD rejection');isolated_psd=dict(row=rt['row_id'],k=k,path=path,rays_passed=12,PSD_rejected=True)
                    else:raise ValueError('tiny globally valid quartics passed curvature gate')

                hi_eff=row.effective_hi(pl,pu,hi);wl=vmin+lo/5;wh=vmax+hi_eff/5;sl=wl*sqrt_bounds(wl)[0];sh=wh*sqrt_bounds(wh)[1]
                Rlo=row.RHO*sl;Rhi=row.RHO_HI*sh;Glo=min(row.GAMMA_LO*sl,row.GAMMA_LO*sh);Ghi=max(row.GAMMA_HI*sl,row.GAMMA_HI*sh)
                need((Rlo,Rhi,Glo,Ghi)==row.raw_bounds(d),'independent directed raw moment bounds')
                poly_ind,c0_ind,c1_ind,hi_eff_ind=independent_geometry(row,pl,pu,lo,hi,al,ah,Rhi,Glo,Ghi,alg)
                poly,c0,c1=row.cell_corners(pl,pu,lo,hi,al,ah)
                need((poly_ind,c0_ind,c1_ind,hi_eff_ind)==(poly,c0,c1,hi_eff)and len(c0)==2 and len(c1)==2,'independent cell geometry and 4-pair shifted moment corners')
                count['independent_geometry_checks']+=1
                W=vmax+(hi_eff/5 if(lo==0 and(al,ah)==(F(0),F(1)))else max(x+y for x,y in poly))
                price=mat.normal.CE_LO/(mat.normal.root(F(5))[1]*W*mat.normal.root(W)[1]);floor=mat.normal.CE_LO*row.RHO/mat.normal.root(F(5))[1]
                targets,diffs,Mt,_=row.target_tensors(d);need(Mt==M,'target curvature');basis=row.tensors(*d);flat=[z for q in qs for z in q]
                idx=0;margin=None
                for x,y in poly:
                    G,_=gs.gaussian(5,kk,pl,pu,ul,uh,5*(x+y));gp={(i,j):z for j,pol in enumerate(G)for i,z in enumerate(pol)if z};tp=ip.mul(ip.V2,ip.add(gp,ip.scale(ip.ONE,floor)))
                    for(g0,k0),(g1,k1)in product(c0,c1):
                        eb=[sum(flat[j]*basis[idx][j][a]for j in range(30))for a in range(50)]
                        score=[t+theta*z-e for t,z,e in zip(targets[idx],diffs[idx],eb)]
                        R=ip.add(ip.mul(ip.V,ip.add(ip.ONE,ip.scale(ip.V,-2))),ip.scale(ip.P,3*x),ip.scale(ip.Q,3*y),ip.scale(ip.ONE,-g0*x+g1*y))
                        imp=ip.mul(ip.V2,ip.add(ip.scale(R,price),ip.scale(ip.ONE,-floor)))
                        need(ip.inverse(targets[idx])==ip.local(tp,pl,pu,ul,uh),'independent target polynomial inverse')
                        need(ip.inverse(diffs[idx])==ip.local(imp,pl,pu,ul,uh),'independent cubic price inverse')
                        ep=ip.direct(kk,x,y,g0,g1,qs,k0,k1)
                        need(ip.inverse(eb)==ip.local(ep,pl,pu,ul,uh),'independent direct expectation inverse')
                        direct=ip.add(tp,ip.scale(imp,theta),ip.scale(ep,-1))
                        need(ip.inverse(score)==ip.local(direct,pl,pu,ul,uh),'independent combined native score inverse')
                        count['independent_vertex_corner_rows']+=1
                        count['independent_score_coefficients']+=len(score)
                        count['independent_inverse_identities']+=4
                        need(min(score)>0,'strict reconstructed score')
                        z=min(score);margin=z if margin is None else min(margin,z);count['score']+=50
                        idx+=1
                need(idx==len(targets)==len(diffs)==len(basis)==4*len(poly),'complete 4*V vertex/corner product')
                cap=native_by[path]
                need(cap['moment_pairs']==4 and cap['prices']==['0','0','0','0']and cap['alpha']==[str(al),str(ah)]and F(cap['cleared_margin'])==margin and cap['psd_minima']==mins,'exact actual native score and PSD match')
                summaries.append(dict(row=rt['row_id'],k=k,path=path,margin=str(margin)))

    need((count['rows'],count['roots'],count['leaves'],count['psd'],count['score'],count['priced_leaves'])==(104,320,1201,37231,1048200,0),'actual final B2 band census')
    need((count['independent_geometry_checks'],count['independent_vertex_corner_rows'],count['independent_score_coefficients'],count['independent_inverse_identities'])==(1201,20964,1048200,83856),'full independent geometry and corner identity census')
    need(count['nonpositive_numerator']+count['sign_crossing_numerator']+count['positive_numerator']==1201,'complete numerator sign partition')
    need(count['positive_curvature']==count['sign_crossing_numerator']+count['positive_numerator'],'exact positive curvature numerator correspondence')
    need(isolated_psd is not None,'positive-curvature isolated control executed')
    after={str(p):sha(p)for p in tracked};need(before==after,'stable entire source/package epoch')
    result=dict(
      status='PASS_FULL_CORNER_INDEPENDENT_N5_B2_BAND_POLYNOMIAL_AND_GEOMETRY_AUDIT_V3',
      counts=count,
      band_join=native_batch['band_join'],
      isolated_curvature_control=isolated_psd,
      selector=dict(contracts=295,band_counts=band_counts,ambiguous_pairs=ambiguous,unique_pairs=unique_pairs),
      leaves=summaries,
      source_sha256_before=before,
      source_sha256_after=after,
      seconds=time.monotonic()-started,
      shared_dependencies=[
        'Gaussian Taylor scalar and native Gaussian constants',
        'native forward Bernstein transform, checked at all 4*V corners by separate inverse',
        'original acquisition and native univariate global-ray Sturm acceptance'
      ],
      no_all_295_theorem=True
    )
    out.mkdir(parents=True,exist_ok=False);(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k not in('leaves','source_sha256_before','source_sha256_after')}))

if __name__=='__main__':main()

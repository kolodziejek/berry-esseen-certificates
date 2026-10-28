"""Independent coverage/interpolation review; not a rerun of 291 margins.

The source root argument is a read-only snapshot with four pinned inputs.
Coverage is reconstructed by pairwise interior disjointness and exact volume,
not the constructor's common endpoint refinement. Bernstein transforms are
reconstructed by rational interpolation, not the constructor's formula.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import copy,hashlib,itertools,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
root=Path(sys.argv[1])
pins={
 'compound-accept.py':'f98de164169fae176644737b8b68b72044837db2a19dbba26602cea279c3d611',
 'compound-evaluator.py':'f23d657e0bc10b1d3334feeb65ccd43dd2d8b415e4a26fb0e6f7c3ddc853e582',
 'compound-certificate.json':'e3baf63f96f5f7fd6e7f9c6dae1e75448f9f588524e164fdf8c0b2e770ea6a0c',
 'compound-proof.tex':'5b9d8428b6aa10bc3fff44114cd26c482b88692f76dd624b841c79d5b4a753fa'}
for name,pin in pins.items():assert hashlib.sha256((root/name).read_bytes()).hexdigest()==pin
def unique_object(pairs):
    result={}
    for key,value in pairs:
        if key in result:raise ValueError('Duplicate raw JSON object key')
        result[key]=value
    return result
doc=json.loads((root/'compound-certificate.json').read_text(),object_pairs_hook=unique_object)
boxes=[tuple(F(x) for x in row['box']) for row in doc['cells']]
domain=((F(3,100),F(3,40)),(F(0),F(3,20)),(F(0),F(1)))
def independent_cover(rows):
    volume=F(0)
    for b in rows:
        if len(b)!=6 or any(not(a<=b[2*j]<b[2*j+1]<=c) for j,(a,c) in enumerate(domain)):
            return False,'invalid_or_exterior'
        volume+=(b[1]-b[0])*(b[3]-b[2])*(b[5]-b[4])
    for b,c in itertools.combinations(rows,2):
        if all(max(b[2*j],c[2*j])<min(b[2*j+1],c[2*j+1]) for j in range(3)):
            return False,'overlapping_interiors'
    target=F(1)
    for a,c in domain:target*=c-a
    return (volume==target,'closed_cover' if volume==target else 'volume_gap')
assert independent_cover(boxes)==(True,'closed_cover')
volume=sum(((b[1]-b[0])*(b[3]-b[2])*(b[5]-b[4]) for b in boxes),F(0))
coverage_mutations={}
bad=boxes[:-1];coverage_mutations['missing']=independent_cover(bad)[1]
bad=boxes+[boxes[0]];coverage_mutations['duplicate']=independent_cover(bad)[1]
bad=list(boxes);b=list(bad[0]);b[5]=(b[4]+b[5])/2;bad[0]=tuple(b)
coverage_mutations['half_cell_gap']=independent_cover(bad)[1]
bad=list(boxes);bad[-1]=bad[0];coverage_mutations['duplicate_replacing_missing']=independent_cover(bad)[1]
assert all(s!='closed_cover' for s in coverage_mutations.values())

# Execute definitions only, explicitly not the __main__ cell acceptance loop.
ns={'__name__':'reviewed_accept_definitions','__file__':str(root/'compound-accept.py')}
exec(compile((root/'compound-accept.py').read_bytes(),str(root/'compound-accept.py'),'exec'),ns)
validated,elementary=ns['validate'](doc)
assert len(validated)==len(boxes)==291 and elementary==480

def solve(matrix,values):
    a=[list(row)+[rhs] for row,rhs in zip(matrix,values)]
    for i in range(len(a)):
        k=next(k for k in range(i,len(a)) if a[k][i])
        a[i],a[k]=a[k],a[i];d=a[i][i];a[i]=[x/d for x in a[i]]
        for j in range(len(a)):
            if j!=i:
                d=a[j][i];a[j]=[x-d*y for x,y in zip(a[j],a[i])]
    return [r[-1] for r in a]
nodes=[F(j,4) for j in range(5)]
bezier=[[F(comb(4,i))*t**i*(1-t)**(4-i) for i in range(5)] for t in nodes]
intervals=sorted({(b[2],b[3]) for b in boxes})
transform_entries=0
for a,b in intervals:
    constructor=ns['bernstein_matrix'](a,b)
    for degree in range(5):
        values=[(a+(b-a)*t)**degree for t in nodes]
        coefficients=solve(bezier,values)
        for i,beta in enumerate(coefficients):
            assert beta==constructor[i][degree];transform_entries+=1
        # Additional exact off-node evaluation guards the reconstruction.
        for t in [F(1,7),F(2,7),F(6,7)]:
            assert sum(coefficients[i]*comb(4,i)*t**i*(1-t)**(4-i) for i in range(5))==(a+(b-a)*t)**degree

# Independently check all later unsquared hinge denominators and the Cantelli
# endpoint licenses. The latter uses a cruder independent exponential upper
# bound, so it is sufficient for the constructor's sharper enclosure.
def exp_upper16(x):
    assert 0<=x<F(1,10)
    term=F(1);value=term
    for k in range(1,17):term=term*x/k;value+=term
    first=term*x/17
    return value+first/(1-x/18)
A=F(3,5);Xi=F(231,250);N=F(42);v=F(6,25)
minlater=None;mincantelli=None;counts={'quartic':0,'cantelli':0}
for row,b in zip(doc['cells'],boxes):
    l,L,rl,rh,wl,wh=b;D=Xi+rh
    assert 0<=F(row['hinge'])<1+rl
    for i,j in zip([2,3],row['later_anchors']):
        mu=min(F(5,2)*L,L*(1+F(5,2)*(D+i)/N))/A**2
        gap=(i+rl)/A+mu-j
        assert gap>0;minlater=gap if minlater is None else min(minlater,gap)
    counts[row['method']]+=1
    if row['method']=='cantelli':
        Z=F(5,8)*D+F(3,8)+D**3/N
        P=(2*Xi*rh+rh**2)/(2*v)+Z
        eu=exp_upper16(P/N)
        assert ns['exp_bounds'](P/N)[1]<=eu
        T=L*(1+F(5,2)*D/N)
        gap=2*rl*T/(T+rl**2)**2-eu
        assert rl>0 and gap>0
        mincantelli=gap if mincantelli is None else min(mincantelli,gap)
    else:assert F(row['alpha'])>0
assert counts=={'quartic':200,'cantelli':91}

def rejects(doc):
    try:ns['validate'](doc)
    except (ValueError,KeyError,TypeError):return True
    return False
schema={}
for name,alter in [
 ('missing',lambda q:q['cells'].pop()),
 ('duplicate',lambda q:q['cells'].append(q['cells'][0])),
 ('reversed',lambda q:q['cells'].reverse()),
 ('changed_domain',lambda q:q['domain'][0].__setitem__(0,'0')),
 ('hinge_at_threshold',lambda q:q['cells'][0].__setitem__('hinge','1')),
 ('boolean_later_anchor',lambda q:q['cells'][0]['later_anchors'].__setitem__(0,True)),
 ('noncanonical_rational',lambda q:q['cells'][0]['box'].__setitem__(0,'0.03')),
 ('missing_field',lambda q:q['cells'][0].pop('method'))]:
    q=copy.deepcopy(doc);alter(q);assert rejects(q);schema[name]='rejected'

# One complete original cell and one changed quartic parameter. This does not
# reproduce or advertise a fresh full run of the 291-cell certificate.
box,alpha,y,anchors=validated[0];ctx=ns['context'](box,y,anchors)
original=ns['quartic_margin'](box,alpha,ctx)
corrupted=ns['quartic_margin'](box,F(1,100),ctx)
assert original>0 and corrupted<0
try:ns['context'](box,y,(99,anchors[1]))
except ValueError:later_mutation='rejected'
else:raise AssertionError('Invalid later hinge accepted')
assert hashlib.sha256((root/'compound-evaluator.py').read_bytes()+b'\n').hexdigest()!=pins['compound-evaluator.py']

print(json.dumps({'status':'PASS_INDEPENDENT_COMPOUND_COVER_REVIEW',
 'source_pins':pins,'raw_JSON_object_keys_unique':True,
 'cell_count':len(boxes),'method_counts':counts,
 'exact_volume':str(volume),'pairwise_interior_pairs':len(boxes)*(len(boxes)-1)//2,
 'constructor_elementary_cells':elementary,'independent_phase_intervals':len(intervals),
 'independent_interpolated_transform_entries':transform_entries,
 'later_hinge_denominator_min':str(minlater),
 'cantelli_initial_derivative_margin_min':str(mincantelli),
 'coverage_mutations':coverage_mutations,'schema_mutations':schema,
 'first_cell_margin':str(original),'corrupted_alpha_margin':str(corrupted),
 'inadmissible_later_hinge':later_mutation,'full_291_margin_rerun':False,
 'scope':'Independent exact coverage, transform reconstruction, denominator and '
 'Cantelli licenses; read review of acceptance semantics. Analytic compound '
 'transport and full arithmetic acceptance have separate reviews/runs.',
 'python':sys.version},indent=2))

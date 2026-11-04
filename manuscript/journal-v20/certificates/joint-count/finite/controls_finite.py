"""Fixed finite reader controls; every altered source stays in a disposable copy."""
from pathlib import Path
from fractions import Fraction as F
import copy,gzip,json,shutil,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import accept_finite as checker
import finite_native
from model import need,sha,unique
from finite_targets import scalar_gate
HERE=Path(__file__).resolve().parent

def main():
    out=Path(sys.argv[1]);out.mkdir();obj=json.loads((HERE/'finite_proof_objects.json').read_text(),object_pairs_hook=unique)
    failures=[]
    def reject(name,bad):
        path=out/(name+'.json.gz');raw=(json.dumps(bad,sort_keys=True)+'\n').encode()
        with gzip.GzipFile(filename=str(path),mode='wb',mtime=0)as f:f.write(raw)
        try:checker.accept_object(bad)
        except (ValueError,TypeError,KeyError,IndexError,ZeroDivisionError)as exc:failures.append({'case':name,'reason':str(exc),'fixture_sha256':sha(path)})
        else:raise RuntimeError('finite mutation accepted: '+name)
    for name,change in [('missing_last_row',lambda x:x['rows'].pop()),('duplicated_row',lambda x:x['rows'].__setitem__(1,copy.deepcopy(x['rows'][0]))),
                        ('reordered_rows',lambda x:x['rows'].reverse()),('boolean_index',lambda x:x['rows'][0].update(index=False)),
                        ('wrong_score_target',lambda x:x.update(score_targets='zero comparison')),
                        ('unsupported_eta',lambda x:x['rows'][0].update(eta='1/100')),('missing_branch',lambda x:x['rows'][0]['cases'].pop()),
                        ('reordered_branches',lambda x:x['rows'][0]['cases'].reverse()),('extra_claim',lambda x:x.update(acquisition_proved=True))]:
        bad=copy.deepcopy(obj);change(bad);reject(name,bad)
    for name,index,branch,value in [('negative_coefficient',0,0,'-1'),('false_positive_coefficient',0,0,'100'),
                                    ('last_row_false_coefficient',266,3,'100'),('float_coefficient',0,0,0.0),('noncanonical_fraction',0,0,'0/2')]:
        bad=copy.deepcopy(obj);bad['rows'][index]['cases'][branch]['coefficients'][0][0]=value;reject(name,bad)
    bad=copy.deepcopy(obj);bad['rows'][0]['cases'][0]['coefficients'][0].pop();reject('missing_coefficient',bad)
    negative=next(i for i,r in enumerate(obj['rows'])if r['eta']=='-1/20')
    bad=copy.deepcopy(obj);bad['rows'][negative]['eta']='1/10';reject('negative_eta_relabelled',bad)
    source_tests=[]
    for name,change in [('normalizer_bytes',lambda root:(root/'finite_native_sources/positive39/normalization.py').write_text('raise RuntimeError("not an accepted source")\n')),
                        ('changed_binomial_reserve',lambda root:(root/'finite_native_sources/left40_42/binomial40.json').write_text('{}\n')),
                        ('changed_source_manifest',lambda root:(root/'FINITE_NATIVE_SOURCES.json').write_text('{}\n'))]:
        root=out/name;root.mkdir()
        for directory in('finite_native_sources','finite_inputs'):shutil.copytree(HERE/directory,root/directory)
        for file in('FINITE_NATIVE_SOURCES.json','FINITE_INPUTS.json'):shutil.copy2(HERE/file,root/file)
        change(root);saved=finite_native.HERE;finite_native.HERE=root
        try:
            try:checker.accept_object(obj)
            except ValueError as exc:source_tests.append({'case':name,'reason':str(exc)})
            else:raise RuntimeError('changed finite source accepted')
        finally:finite_native.HERE=saved
    native=finite_native.rows();scalar_tests=[];saved_rows=checker.rows
    for key,value in [('mass',F(2)),('ownlo',F(0)),('repair',F(-1))]:
        corrupted=copy.deepcopy(native);corrupted[0]['c'][key]=value;checker.rows=lambda:corrupted
        try:
            try:checker.accept_object(obj)
            except ValueError as exc:scalar_tests.append({'field':key,'value':str(value),'reason':str(exc)})
            else:raise RuntimeError('invalid finite scalar domain accepted')
        finally:checker.rows=saved_rows
    # A concrete endpoint refutes the tempting wrong negative-eta multiplication.
    row=native[negative];c=row['c'];eta=F(-1,20)
    true_endpoint=eta*c['ownhi'];wrong_endpoint=c['mass']*eta*c['ownlo']
    need(wrong_endpoint>true_endpoint,'wrong-sign rule has a strict endpoint counterexample')
    old_gate=wrong_endpoint-c['repair']/c['N']+c['epsilon']*c['rhoB_lower']/c['lmax']
    right_gate=scalar_gate(c,eta,'binomial_reserve')
    need(old_gate>right_gate,'wrong-sign gate demonstrably overstates the reserve')
    try:json.loads('{"rows":[],"rows":[]}',object_pairs_hook=unique)
    except ValueError:duplicate=True
    else:raise RuntimeError('duplicate JSON accepted')
    result={'status':'PASS_FINITE267_CORRUPTION_AND_SIGN_CONTROLS','object_rejections':failures,'source_rejections':source_tests,
            'scalar_domain_rejections':scalar_tests,'duplicate_JSON_rejected':duplicate,
            'negative_eta_endpoint_counterexample':{'native_row':row['index'],'family':row['family'],'eta':str(eta),
                'true_loss_at_b1_tupper':str(true_endpoint),'invalid_m_lower_variance_loss':str(wrong_endpoint),
                'exact_reserve_overstatement':str(old_gate-right_gate)},
            'original_source_bytes_unchanged':True,'no_original_reserve_or_target_changed':True}
    (out/'RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'object_rejections':len(failures),'source_rejections':len(source_tests),
                      'scalar_domain_rejections':len(scalar_tests),'negative_eta_counterexample':True}))

if __name__=='__main__':main()

from pathlib import Path
import subprocess,json,hashlib,re,sys
from fractions import Fraction as F
root=Path.cwd();base='6346fc1b4432bc5982822aa696eb566ed9e1e1ee';start='ec370aadc459460e75ffd6d8d3b7b1f9f8a9cb13';m=root/'manuscript/arxiv-v1';run=root/'runs/manuscript-v2-20261027/integration01';run.mkdir(parents=True,exist_ok=False)
def git(*args):return subprocess.check_output(['git',*args],text=True)
base_entries=git('ls-tree','-r',base).splitlines();original={x.split('\t',1)[1]:x.split('\t',1)[0] for x in base_entries};current={x.split('\t',1)[1]:x.split('\t',1)[0] for x in git('ls-tree','-r','HEAD').splitlines()}
changed=[p for p,v in original.items() if current.get(p)!=v];dirty=set(git('diff','--name-only','HEAD').splitlines())&original.keys();assert not changed and not dirty
(run/'baseline.json').write_text(json.dumps({'baseline':base,'baseline_entries':len(original),'changed_or_missing_baseline_entries':changed,'working_changes_to_baseline_entries':sorted(dirty),'passed':True},indent=2))
oldpaths=[p for p in git('ls-tree','-r','--name-only',start,'manuscript/arxiv-v1').splitlines() if p.endswith('.tex')]
old='\n'.join(git('show',start+':'+p) for p in oldpaths);new='\n'.join(p.read_text() for p in m.rglob('*.tex'));labels=lambda s:set(re.findall(r'\\label\{([^}]+)\}',s));missing=labels(old)-labels(new);assert not missing
# Atlas proof text: allow leading zeros, whitespace, and one updated location sentence.
f='manuscript/arxiv-v1/appendices/fourier-analysis.tex';oldatlas=git('show',start+':'+f);newatlas=Path(f).read_text();marker='\\subsubsection{Signed moments with a common first moment}'
def canon(s):
 s=s[s.index(marker):].replace('The signed identity from the preceding section is','The raw remainder in \\eqref{ms:fourier:rescore:re-raw} is')
 s=re.sub(r'(?<![0-9.])\.(?=[0-9])','0.',s)
 return re.sub(r'\s+',' ',s).strip()
assert canon(oldatlas)==canon(newatlas)
# The moved moment-domain proof is intact after changing section level/location words.
f='manuscript/arxiv-v1/appendices/moment-domain.tex';a=git('show',start+':'+f);b=(m/'sections/02b-moment-domain.tex').read_text();a=a[a.index('\\begin{theorem}'):];b=b[b.index('\\begin{theorem}'):];assert re.sub(r'\s+',' ',a).strip()==re.sub(r'\s+',' ',b).strip()
def s(k,x):return sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(k)),F(0))
piup=16*s(5,F(1,5))-4*s(2,F(1,239));assert piup<F(22,7);assert F(39886,100000)**2<F(7,44)
(run/'preservation.json').write_text(json.dumps({'starting_manuscript_commit':start,'original_labels':len(labels(old)),'current_labels':len(labels(new)),'missing_original_labels':sorted(missing),'atlas_and_tail_preserved_modulo_documented_typography_and_reference_sentence':True,'moved_moment_proof_preserved':True,'gaussian_lower_comparison_exact':True,'scope':'document preservation and two new rational comparisons; not full proof or certificate acceptance'},indent=2))
cmd=[sys.executable,str(m/'tools/check_sources.py')];r=subprocess.run(cmd,capture_output=True,text=True);(run/'source-integrity.json').write_text(r.stdout);(run/'stderr.txt').write_text(r.stderr);assert r.returncode==0
files=[Path('/Users/bkolodziejek/Downloads')/x for x in ['main-revised-preview.pdf','references-added.bib','01b-guide.tex','01-introduction-revised.tex','main-revised.tex','source-arxiv-v1/MANUSCRIPT_REVISION_INSTRUCTIONS.md']]
(run/'attachment-provenance.json').write_text(json.dumps({'authority':'User-supplied suggestions assessed as proposals; not instructions authorizing scope changes','files':{str(p):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in files}},indent=2))
print('PASS: baseline2748, original labels retained, atlas and moment proofs preserved, Gaussian comparisons, source integrity')

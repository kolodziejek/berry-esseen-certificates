from pathlib import Path
from fractions import Fraction as F
import subprocess,hashlib,json,re,sys,time,shutil
root=Path('/Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/manuscript_revision_20261029');p=root/'manuscript/compact-v16';r=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=(r/'before.tex').read_text();current=(p/'sections/08-direct-comparison.tex').read_text()
def first_theorem(text):return re.search(r'\\begin\{theorem\}.*?\\end\{theorem\}',text,re.S)[0]
assert first_theorem(old)==first_theorem(current)
labels=lambda t:re.findall(r'\\label\{([^}]+)\}',t)
assert set(labels(old))<=set(labels(current)) and len(labels(current))==len(set(labels(current)))
assert not re.search(r'\\pi_[ijk01{]|\{Nr\}|(?<![A-Za-z])N=700',current)
assert F(3,4)*(F(59,100)-F(51,50)*F(53,100))-F(2,700)==F(4787,140000)>F(1,100)
assert 1/(4*(F(3,5)**2+3*F(101,10000)))==F(2500,3903)>F(16,25)
# Independent exact diagnostics for the newly displayed zero-threshold inequality.
laws=[[(F(-1),F(1,2)),(F(1),F(1,2))],[(F(-1),F(2,3)),(F(2),F(1,3))],[(F(-1,10**6),F(1,2)),(F(1,10**6),F(1,2))],[(F(-1,1000),F(1000,1001)),(F(1),F(1,1001))],[(F(-1),F(1,4)),(F(0),F(1,2)),(F(1),F(1,4))]]
rows=[]
for law in laws:
 assert sum(x*q for x,q in law)==0
 variance=sum(x*x*q for x,q in law);m4=sum(x**4*q for x,q in law);prob=sum(q for x,q in law if x>0)
 assert prob>=variance**2/(4*m4)
 rows.append(dict(variance=str(variance),fourth_moment=str(m4),probability=str(prob),lower_bound=str(variance**2/(4*m4))))
result=dict(status='PASS_OPUS_COUNT_EXPOSITION_SCALARS',mathematical_status='New explanatory moment inequality derived by Cauchy–Schwarz/Hölder; theorem and all old numerical comparisons retained.',execution_status='Exact rational checks and five diagnostic laws passed; diagnostic laws are not the proof.',old_labels=len(labels(old)),current_labels=len(labels(current)),theorem_statement_byte_identical=True,inner_margin=str(F(4787,140000)),zero_threshold_coefficient=str(F(2500,3903)),diagnostics=rows,python=sys.version,source_sha256=sha(p/'sections/08-direct-comparison.tex'))
(r/'explanation-check.json').write_text(json.dumps(result,indent=2)+'\n')
cmd=[sys.executable,'-I','-B',str(p/'tools/check_revision_count_constants.py')];ts=time.monotonic();x=subprocess.run(cmd,cwd=root,capture_output=True);(r/'count-check.stdout.json').write_bytes(x.stdout);(r/'count-check.stderr.txt').write_bytes(x.stderr);assert x.returncode==0 and json.loads(x.stdout)['status']=='PASS_REVISION_COUNT_CONSTANTS'
records=[dict(command=cmd,returncode=x.returncode,seconds=time.monotonic()-ts,stdout_sha256=hashlib.sha256(x.stdout).hexdigest(),stderr_sha256=hashlib.sha256(x.stderr).hexdigest())]
b=r/'build03';b.mkdir();main=(p/'main.tex').read_text().split(r'\begin{document}',1)[0];(b/'main.tex').write_text(main+r'\begin{document}'+'\n'+r'\setcounter{section}{6}\input{count}'+'\n'+r'\end{document}'+'\n');(b/'count.tex').write_text(current)
for i in range(1,4):
 cmd=['/Library/TeX/texbin/pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','main.tex'];ts=time.monotonic();x=subprocess.run(cmd,cwd=b,capture_output=True);(b/f'pass{i}.stdout.txt').write_bytes(x.stdout);(b/f'pass{i}.stderr.txt').write_bytes(x.stderr);assert x.returncode==0;records.append(dict(command=cmd,returncode=x.returncode,seconds=time.monotonic()-ts,stdout_sha256=hashlib.sha256(x.stdout).hexdigest(),stderr_sha256=hashlib.sha256(x.stderr).hexdigest()))
(r/'receipt.json').write_text(json.dumps(dict(records=records,source_sha256=sha(p/'sections/08-direct-comparison.tex'),explanation_check_sha256=sha(r/'explanation-check.json'),checker_sha256=sha(p/'tools/check_revision_count_constants.py'),python=sys.version),indent=2)+'\n')
log=(b/'main.log').read_text();print('\n'.join(x for x in log.splitlines() if 'Overfull' in x or 'Output written' in x or 'Warning:' in x));print('PASS_OPUS_COUNT_COMPONENT')

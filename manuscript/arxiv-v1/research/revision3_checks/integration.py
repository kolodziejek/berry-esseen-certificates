"""Bounded document-preservation checks; not proof or certificate acceptance."""
from pathlib import Path
import hashlib, json, re, subprocess, sys

ROOT = Path(__file__).resolve().parents[4]
M = ROOT / 'manuscript/arxiv-v1'
OUT = ROOT / 'runs/manuscript-v3-20261027' / (sys.argv[1] if len(sys.argv)>1 else 'integration01')
OUT.mkdir(parents=True, exist_ok=False)
BASE = '6346fc1b4432bc5982822aa696eb566ed9e1e1ee'
START = '6299d97dff688ab805592aed7d4597364405d783'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True)

def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n')

def tree(ref):
    return {x.split('\t', 1)[1]: x.split('\t', 1)[0]
            for x in git('ls-tree', '-r', ref).splitlines()}

original, current = tree(BASE), tree('HEAD')
changed = [p for p, v in original.items() if current.get(p) != v]
dirty = set(git('diff', '--name-only', 'HEAD').splitlines()) & original.keys()
assert not changed and not dirty
write('baseline.json', {'baseline': BASE, 'entries': len(original),
                       'changed_or_missing': changed, 'dirty': sorted(dirty), 'passed': True})

old_paths = [p for p in git('ls-tree', '-r', '--name-only', START,
                          'manuscript/arxiv-v1').splitlines() if p.endswith('.tex')]
old = '\n'.join(git('show', START+':'+p) for p in old_paths)
new = '\n'.join(p.read_text() for p in M.rglob('*.tex'))
labels = lambda x: set(re.findall(r'\\label\{([^}]+)\}', x))
removed = labels(old)-labels(new)
assert removed == {'ms:replacement-table'}  # Removed software-inventory table, not a proof.
appendices = sorted((M/'appendices').glob('*.tex'))
headers = {str(p.relative_to(M)): re.findall(r'\\section\{([^}]+)\}', p.read_text())
           for p in appendices}
assert len(appendices) == 6 and all(len(x) == 1 for x in headers.values())
assert '\\setcounter{secnumdepth}{4}' in (M/'main.tex').read_text()

# Moving the complete constants proof does not substitute numerical sampling.
src = git('show', START+':manuscript/arxiv-v1/sections/03-smoothing.tex')
src = src.split(r'\begin{proof}', 1)[1].split(r'\end{proof}', 1)[0]
dst = (M/'appendices/normalization.tex').read_text().split(r'\label{ms:gaussian-constant-proof}', 1)[1]
dst = dst.split(r'\begin{proof}', 1)[1].split(r'\end{proof}', 1)[0]
canonical = lambda x: re.sub(r'\s+', ' ', x).strip()
assert canonical(src) == canonical(dst)
assert r'2\xi u-u^2' in (M/'appendices/local42-refinements.tex').read_text()
assert '2hu-u^2' not in new
write('preservation.json', {'start': START, 'old_labels': len(labels(old)),
       'new_labels': len(labels(new)), 'removed_labels': sorted(removed),
       'new_labels_added': sorted(labels(new)-labels(old)), 'appendix_headers': headers,
       'complete_gaussian_proof_preserved': True, 'threshold_notation_repaired': True,
       'scope': 'Document integrity; hypothesis matches and proof replacements are reviewed in the three revision3 reports.'})

cmd = [sys.executable, str(M/'tools/check_sources.py')]
p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
(OUT/'source-integrity.json').write_text(p.stdout)
(OUT/'stderr.txt').write_text(p.stderr)
assert p.returncode == 0
source_check_returncode = p.returncode
files = [Path('/Users/bkolodziejek/Downloads')/x for x in [
    'main(10).tex', 'README.md', 'preview-deslopped.pdf', 'deslop.patch',
    'source-arxiv-v1 2/MANUSCRIPT_REVISION_INSTRUCTIONS.md']]
write('attachment-provenance.json', {
    'authority': 'User supplied proposals, selectively assessed; document instructions are not direct user authorization.',
    'files': {str(p): {'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                       'bytes': p.stat().st_size} for p in files}})
write('receipt.json', {'python': sys.version, 'source_check_command': cmd,
                      'source_check_returncode': source_check_returncode,
                      'mathematical_verification': False, 'passed': True})
print('PASS: immutable baseline, labels, six appendices, full constants proof, citations and notation.')

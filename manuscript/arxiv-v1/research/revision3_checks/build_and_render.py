"""Compile the manuscript and create page images for editorial inspection."""
from pathlib import Path
import hashlib, json, re, subprocess, sys, time
from PIL import Image, ImageDraw
from pypdf import PdfReader

root = Path(__file__).resolve().parents[4]
m = root/'manuscript/arxiv-v1'
run = root/'runs/manuscript-v3-20261027'/sys.argv[1]
run.mkdir(parents=True, exist_ok=False)
build = run/'texlive'
script = Path('/Users/bkolodziejek/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
cmd = [sys.executable, str(script), str(m/'main.tex'), '--compiler', 'texlive',
       '--output-directory', str(build), '--json']
started = time.perf_counter()
p = subprocess.run(cmd, cwd=root, capture_output=True)
(run/'stdout.json').write_bytes(p.stdout)
(run/'stderr.txt').write_bytes(p.stderr)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
receipt = {'command': cmd, 'exit_code': p.returncode,
           'duration_seconds': time.perf_counter()-started, 'python': sys.version,
           'source_sha256': {str(p.relative_to(m)): sha(p)
                for p in [*m.rglob('*.tex'), *m.glob('*.bib')]}}
if p.returncode == 0:
    pdf = PdfReader(build/'main.pdf')
    log = (build/'main.log').read_text()
    receipt.update({'pdf_sha256': sha(build/'main.pdf'), 'pages': len(pdf.pages),
                    'warnings': [s for s in log.splitlines()
                     if any(t in s for t in ['Warning', 'Overfull', 'Underfull', 'undefined'])]})
    receipt['skipped_heading_levels'] = re.findall(r'\\numberline\{([A-F]\.\d+\.0\.[^}]+)\}', (build/'main.toc').read_text())
(run/'receipt.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False)+'\n')
print(json.dumps({k: receipt[k] for k in ['exit_code','duration_seconds','pages','warnings'] if k in receipt}))
assert p.returncode == 0
assert not receipt['skipped_heading_levels']

render = run/'render'
render.mkdir()
poppler = '/Users/bkolodziejek/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
cmd = [poppler, '-r', '45', '-png', str(build/'main.pdf'), str(render/'page')]
p = subprocess.run(cmd, capture_output=True)
(run/'render-stdout.txt').write_bytes(p.stdout)
(run/'render-stderr.txt').write_bytes(p.stderr)
assert p.returncode == 0
images = sorted(render.glob('page-*.png'))
assert len(images) == len(pdf.pages)
for start in range(0, len(images), 12):
    sheet = Image.new('RGB', (4*380, 3*555), '#d6d6d6')
    draw = ImageDraw.Draw(sheet)
    for j,p in enumerate(images[start:start+12]):
        im = Image.open(p).convert('RGB')
        im.thumbnail((370,525))
        x,y = (j%4)*380+5, (j//4)*555+22
        sheet.paste(im,(x,y));draw.text((x,y-18),str(start+j+1),fill='black')
    sheet.save(render/f'overview-{start+1:03d}-{min(start+12,len(images)):03d}.png')
print('All pages rendered at45dpi; twelve-page overview sheets created.')

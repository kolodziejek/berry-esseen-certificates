"""Read-only baseline, inactive-source and editorial-scope integrity check."""
from pathlib import Path
import hashlib
import json
import os
import subprocess

root = Path(__file__).resolve().parents[4]
baseline = '6346fc1b4432bc5982822aa696eb566ed9e1e1ee'
start = '924e6160bee44ed3a50eba35f7dbb8dcd5b9a9c7'
env = dict(os.environ, GIT_NO_LAZY_FETCH='1', GIT_OPTIONAL_LOCKS='0')
commands = []
def git(*args):
    cmd = ['git', *args]
    p = subprocess.run(cmd, cwd=root, env=env, capture_output=True)
    commands.append({'command': cmd, 'returncode': p.returncode,
                     'stderr': p.stderr.decode()})
    if p.returncode:
        raise RuntimeError('Git integrity query failed: ' + repr(cmd))
    return p.stdout

if git('rev-parse', '--show-object-format').strip() != b'sha1':
    raise RuntimeError('Unexpected Git object format')
def tree(ref):
    return {x.split(b'\t', 1)[1]: x.split(b'\t', 1)[0]
            for x in git('ls-tree', '-rz', ref).split(b'\0') if x}
base, current = tree(baseline), tree('HEAD')
index = {x.split(b'\t', 1)[1]: x.split(b'\t', 1)[0]
         for x in git('ls-files', '--stage', '-z').split(b'\0') if x}
tags = {x[2:]: x[:1] for x in git('ls-files', '-t', '-z').split(b'\0') if x}
materialized = sparse = 0
for name, header in base.items():
    mode, kind, oid = header.split()
    if kind != b'blob' or current.get(name) != header:
        raise RuntimeError('Committed baseline changed: ' + name.decode())
    if index.get(name) != mode + b' ' + oid + b' 0':
        raise RuntimeError('Indexed baseline changed: ' + name.decode())
    p = root / name.decode()
    if not p.exists() and not p.is_symlink() and tags.get(name) == b'S':
        sparse += 1
        continue
    if mode == b'120000' and p.is_symlink():
        data = os.readlink(p).encode()
    elif mode in (b'100644', b'100755') and p.is_file():
        data = p.read_bytes()
    else:
        raise RuntimeError('Missing baseline file or unexpected mode: ' + name.decode())
    actual = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if actual.encode() != oid:
        raise RuntimeError('Working baseline changed: ' + name.decode())
    materialized += 1

inactive = [
    'sections/02-extremizers.tex', 'sections/03-smoothing.tex',
    'sections/04-support.tex', 'sections/05b-conserved.tex',
    'sections/06-resources.tex', 'appendices/fourier-analysis.tex',
    'appendices/uniform-bridge.tex', 'appendices/finite-support.tex',
    'appendices/finite-analysis.tex',
]
unchanged = {}
for relative in inactive:
    p = root / 'manuscript/arxiv-v1' / relative
    before = git('show', start + ':' + str(p.relative_to(root)))
    if p.read_bytes() != before:
        raise RuntimeError('Inactive source was rewritten: ' + relative)
    unchanged[relative] = hashlib.sha256(before).hexdigest()
changed = git('diff', '--name-only', start).decode().splitlines()
untracked = git('ls-files', '--others', '--exclude-standard').decode().splitlines()
allowed = ('manuscript/arxiv-v1/', 'runs/manuscript-v9-20261028/', 'state/')
if any(not x.startswith(allowed) for x in [*changed, *untracked]):
    raise RuntimeError('Change outside the editorial/evidence/state scope')
print(json.dumps({
    'status': 'PASS_EDITORIAL_BASELINE_PRESERVATION', 'baseline': baseline,
    'editorial_start': start, 'head_at_check': git('rev-parse', 'HEAD').decode().strip(),
    'baseline_entries': len(base), 'materialized_bytes_checked': materialized,
    'sparse_tree_index_bindings': sparse, 'unchanged_inactive_sources': unchanged,
    'changed_paths': changed, 'new_untracked_paths': untracked,
    'no_lazy_fetch': True, 'commands': commands,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'mathematical_verification': False,
}, indent=2))

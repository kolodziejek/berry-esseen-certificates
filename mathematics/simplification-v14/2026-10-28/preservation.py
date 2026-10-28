"""Read-only baseline, manuscript and new-research-scope integrity check."""
from pathlib import Path
import hashlib
import json
import os
import subprocess

root = Path(__file__).resolve().parents[3]
baseline = '6346fc1b4432bc5982822aa696eb566ed9e1e1ee'
start = '656232ea8d9561a3f47aefa083ead4f6ba4206ca'
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

unchanged = {}
for name, header in tree(start).items():
    if not name.startswith(b'manuscript/arxiv-v1/'):
        continue
    mode, kind, oid = header.split()
    if current.get(name) != header:
        raise RuntimeError('Committed manuscript changed: ' + name.decode())
    p = root/name.decode()
    if p.is_file():
        data = p.read_bytes()
        actual = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if actual.encode() != oid:
            raise RuntimeError('Working manuscript changed: ' + name.decode())
        unchanged[name.decode()] = hashlib.sha256(data).hexdigest()
    elif tags.get(name) != b'S':
        raise RuntimeError('Missing manuscript source: ' + name.decode())
changed = git('diff', '--name-only', start).decode().splitlines()
untracked = git('ls-files', '--others', '--exclude-standard').decode().splitlines()
allowed = ('mathematics/simplification-v14/', 'runs/simplification-v14-20261028/', 'runs/counts-v14-20261028/', 'runs/geometry-v14-20261028/', 'runs/loss-v14-20261028/', 'runs/counts-window-review-v14-20261028/', 'runs/large-index-review-v14-20261028/', 'runs/geometry-slack-review-v14-20261028/', 'state/')
# An unrelated pre-existing Finder file is neither changed nor staged.
untracked = [x for x in untracked if x != 'manuscript/.DS_Store']
if any(not x.startswith(allowed) for x in [*changed, *untracked]):
    raise RuntimeError('Change outside the research/evidence/state scope')
print(json.dumps({
    'status': 'PASS_RESEARCH_BASELINE_AND_MANUSCRIPT_PRESERVATION', 'baseline': baseline,
    'research_start': start, 'head_at_check': git('rev-parse', 'HEAD').decode().strip(),
    'baseline_entries': len(base), 'materialized_bytes_checked': materialized,
    'sparse_tree_index_bindings': sparse, 'unchanged_manuscript_files': unchanged,
    'changed_paths': changed, 'new_untracked_paths': untracked,
    'no_lazy_fetch': True, 'commands': commands,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'mathematical_verification': False,
}, indent=2))

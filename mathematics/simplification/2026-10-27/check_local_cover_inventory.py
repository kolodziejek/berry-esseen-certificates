"""Read-only structural audit; imports no inherited numerical implementation.

This checks finite table/rectangle coverage and duplicated call configurations.
It is not arithmetic acceptance or an all-law proof provider.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "verification/finite-tail"


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def atoms(points):
    p = sorted(set(points))
    return sorted(set(p + [(a + b) / 2 for a, b in zip(p, p[1:])]))


def cover(rectangles, ceiling):
    need(ceiling > 0, "positive ceiling")
    for a, b, c, d in rectangles:
        need(0 <= a <= b <= ceiling and F(-1, 2) <= c <= d <= F(1, 2), "rectangle domain")
    ls = atoms([F(0), ceiling] + [x for r in rectangles for x in r[:2]])
    us = atoms([F(-1, 2), F(1, 2)] + [x for r in rectangles for x in r[2:]])
    for lam in ls:
        for u in us:
            need(any(a <= lam <= b and c <= u <= d for a, b, c, d in rectangles), "uncovered cell")
    return len(ls) * len(us)


def rectangles(side, ceiling):
    # Bernoulli handles lambda=0; TINY handles strictly positive noise.
    out = [(F(0), min(F('.05'), ceiling), F('-.5'), F('.5'))]
    radii = ['.09', '.14', '.19', '.29'] if side == 'central' else ['0', '0', '.19', '.27']
    ends = ['.05', '.06', '.08', '.10', '.12']
    for a, b, radius in zip(ends, ends[1:], radii):
        lo, hi, r = F(a), min(F(b), ceiling), F(radius)
        if lo < hi:
            out.extend([(lo, hi, F('-.5'), -r), (lo, hi, r, F('.5'))])
            if side == 'central' or lo >= F('.08'):
                out.append((lo, hi, -r, r))
    if ceiling > F('.12'):
        out.append((F('.12'), ceiling, F('-.5'), F('.5')))
    return out


def check_rows(rows, side):
    count, start = (47, F('.38')) if side == 'central' else (45, F('.29'))
    threshold = F('.05') if side == 'central' else F('.08')
    need(len(rows) == count, "complete probability table")
    checks = 0
    selected = []
    for i, r in enumerate(rows):
        need(type(r['index']) is int and r['index'] == i, "strict ordered index")
        need(list(map(F, r['p'])) == [start + F(i, 500), start + F(i + 1, 500)], "closed p panel")
        ceiling = F(r['lambda_max'])
        checks += cover(rectangles(side, ceiling), ceiling)
        if ceiling > threshold:
            selected.extend((i, sign) for sign in (-1, 1))
    return selected, checks


def producer_labels(rows, family, expected):
    got = [r for r in rows if r['family'] == family]
    need([(r['index'], r['sign']) for r in got] == expected, "complete ordered producer rows")
    for r in got:
        i, sign = r['index'], r['sign']
        need(type(i) is int and type(sign) is int, "strict producer labels")
        grid = (32, 16) if family == 'central42_v2' and i == 0 and sign == -1 else ((16, 8) if family == 'central42_v2' else (8, 4))
        need((r['H_cells'], r['outer_phase_cells']) == grid, "producer and full-binder grids")
    return len(got)


def run():
    need(__debug__ and not sys.flags.optimize, "ordinary Python")
    source_hashes = {}
    with zipfile.ZipFile(BASE / 'sources/backend.zip') as z:
        manifest_bytes = z.read('finite61/MANIFEST.json')
        manifest = json.loads(manifest_bytes)

        def get(suffix):
            matches = [(p, v) for p, v in manifest['files'].items() if p.endswith(suffix)]
            need(len(matches) == 1, "unique source suffix: " + suffix)
            p, meta = matches[0]
            blob = z.read('finite61/blobs/' + meta['sha256'])
            need(len(blob) == meta['bytes'] and sha256(blob).hexdigest() == meta['sha256'], "source blob integrity")
            source_hashes[p] = meta['sha256']
            return blob

        sides = [('central', 'central42_v2', 'new_central42_targets.json'), ('left', 'left42_final', 'actual_float_targets.json')]
        records = []
        for side, family, table in sides:
            rows = json.loads(get('/' + family + '/' + table))['rows']
            selected, count = check_rows(rows, side)
            n = producer_labels(manifest['low_rows'], family, selected)
            for name in ['bind_low42.py', 'central42_contract.py', 'central42_kernel.py', 'mid42_contract.py']:
                get('/' + family + '/' + name)
            records.append(dict(side=side, probability_rows=len(rows), low_rows=n, partition_checks=count,
                                first_low_index=selected[0][0], last_low_index=selected[-1][0],
                                maximum_noise=str(max(F(r['lambda_max']) for r in rows))))
        for name in ['finite61/finite61_worker.py', 'finite61/finite61_batch.py']:
            source_hashes[name] = sha256(z.read(name)).hexdigest()
        absent = [family['family'] for family in manifest['low_families']
                  if not any(p.endswith('/' + family['index_name']) for p in manifest['files'])]
        need(len(absent) == 2 and not any('/low_rows/' in p for p in manifest['files']), "reference LOW files absent in source-only backend")

    tasks = json.loads((BASE / 'TASKS.json').read_bytes())['tasks']
    native = [t for t in tasks if t['kind'] == 'finite-native']
    removed = [t for t in native if t['task_id'].startswith('61.native.43.') or t['task_id'] in {
        '61.native.44.entry.' + s for s in ['accept4044_01', 'accept41_01', 'accept4248_01', 'support4044_01', 'support41_01', 'support4248_01']}]
    kept = [t for t in native if t not in removed]
    need((len(native), len(removed), len(kept)) == (31, 12, 19), "candidate finite action partition")
    need(sum(t['kind'] == 'low-row' for t in tasks) == 152, "all producer rows remain enumerated")
    need(len(tasks) == 240 and len({t['task_id'] for t in tasks}) == 240, "unchanged public task inventory")
    binder_ids = ['61.native.44.local.central42_low_fresh_replay01', '61.native.44.local.left42_low_accept01']
    need(all(next(t for t in tasks if t['task_id'] == i)['arguments'] == ['--replay'] for i in binder_ids), "both binders recompute arithmetic")

    controls = []
    broken = [
        ('missing_positive_phase', [(F(0), F('.1'), F('-.5'), F(0))]),
        ('noise_gap', [(F(0), F('.05'), F('-.5'), F('.5')), (F('.051'), F('.1'), F('-.5'), F('.5'))]),
        ('missing_upper_endpoint', [(F(0), F('.099'), F('-.5'), F('.5'))]),
    ]
    for name, value in broken:
        try:
            cover(value, F('.1'))
        except ValueError:
            controls.append(name)
        else:
            raise ValueError('negative control accepted: ' + name)
    return dict(status='PASS_STRUCTURAL_COVER_ONLY', mathematical_status='Conditional finite rectangle cover; no acquired-law or score proof',
                native_arithmetic_executed=False, all_law_provider=False, full_proof_pass=False,
                source_manifest_sha256=sha256(manifest_bytes).hexdigest(), source_hashes=source_hashes,
                finite42=records, public_tasks=240, candidate_kept_native=[t['task_id'] for t in kept],
                candidate_bypassed_native=[t['task_id'] for t in removed],
                missing_reference_low_families=absent, negative_controls=controls,
                unresolved=['all-index acquisition including support lifts', 'explicit N42 confinement theorem scope',
                            'all required current numerical acceptance receipts', 'new source-bound all-index composition'])


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))

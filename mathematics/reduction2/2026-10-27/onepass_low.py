#!/usr/bin/env python3
"""Candidate one-pass LOW adapter. Default operation only inventories sources.

The opt-in run-family operation would execute a complete native family and
requires separate campaign authorization. It was NOT run during development.
It has no receipt/row import API. Old production runners are unchanged.
"""
import argparse
import ast
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import sys
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[3]
ARCHIVE_SHA = '43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52'
MANIFEST_SHA = 'c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf'
PREFIX = 'work/toward40_20261007/audit43/capsule/work/below49_20261006/local/'
NORMALIZATION_SHA = '3650f39f618def7615d8be20ce8b9efd28e16202102fb8fa76dd8687deff4a6c'
MODULES = ('tiny42_normalization', 'central42_contract', 'central42_kernel', 'bind_low42')
CONTROLS = ['missing', 'duplicate', 'reordered', 'boolean_index', 'boolean_sign',
            'extra_scope', 'path_traversal', 'duplicate_JSON_key', 'corrupted_row_hash']
SPECS = {
    'central42_v2': dict(count=78, start=0, end=39, threshold=Fraction('.05'),
                         target='new_central42_targets.json',
                         index='central42_low_index.json',
                         index_sha='a02638ae22a0efbcb5dd1a8e1e9b233fd1f957c8fc46ba32aef2270cc874519e'),
    'left42_final': dict(count=74, start=8, end=45, threshold=Fraction('.08'),
                         target='actual_float_targets.json',
                         index='left42_low_index.json',
                         index_sha='aca7d7ac16a43a35750ddb173d5a30e169f7d80f61d68472e46934f10835cd52'),
}


def need(value, message):
    if not value:
        raise ValueError(message)


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def parsed(raw):
    def invalid_constant(value):
        raise ValueError('non-finite JSON number: ' + value)
    return json.loads(raw, object_pairs_hook=unique, parse_constant=invalid_constant)


def encoded(obj):
    # The original producer's exact key order, indentation and final LF.
    return (json.dumps(obj, indent=2, allow_nan=False) + '\n').encode('utf-8')


def freeze(value):
    """Typed snapshot, including non-scalar config fields omitted by the binder."""
    if type(value) is Fraction:
        return ('Fraction', value.numerator, value.denominator)
    if type(value) in (int, str, float, bool, type(None)):
        return (type(value).__name__, value)
    if type(value) in (list, tuple):
        return (type(value).__name__, tuple(freeze(v) for v in value))
    if type(value) is dict:
        return ('dict', tuple((freeze(k), freeze(v)) for k, v in value.items()))
    raise ValueError('unsupported typed snapshot value')


def grid(family, index, sign):
    return ((32, 16) if index == 0 and sign == -1 else (16, 8)) if family == 'central42_v2' else (8, 4)


def load_plan(archive, family):
    """Authenticate source-only bytes and fixed152-task definitions; no imports."""
    need(family in SPECS, 'fixed native family')
    archive = Path(archive)
    need(archive.is_file() and not archive.is_symlink(), 'regular source archive')
    need(sha256(archive.read_bytes()).hexdigest() == ARCHIVE_SHA, 'fixed archive hash')
    spec = SPECS[family]
    with ZipFile(archive) as z:
        need(len(z.namelist()) == len(set(z.namelist())), 'unique ZIP members')
        raw = z.read('finite61/MANIFEST.json')
        need(sha256(raw).hexdigest() == MANIFEST_SHA, 'fixed manifest hash')
        manifest = parsed(raw)
        families = [r for r in manifest['low_families'] if r['family'] == family]
        need(len(families) == 1, 'unique family')
        record = families[0]
        need(record['count'] == spec['count'] and record['index_name'] == spec['index']
             and record['reference_index_sha256'] == spec['index_sha'], 'fixed family contract')
        sources = {}
        for name in [*(m + '.py' for m in MODULES), spec['target']]:
            logical = PREFIX + family + '/' + name
            meta = manifest['files'][logical]
            pin = NORMALIZATION_SHA if name == 'tiny42_normalization.py' else record['source_pins'][name]
            need(meta['sha256'] == pin, 'source pin')
            source = z.read('finite61/blobs/' + pin)
            need(len(source) == meta['bytes'] and sha256(source).hexdigest() == pin, 'source bytes')
            if name.endswith('.py'):
                allowed = {'pathlib', 'fractions', 'hashlib', 'json', 'sys', 'copy',
                           'math', 'functools', 'tiny42_normalization',
                           'central42_contract', 'central42_kernel'}
                for node in ast.walk(ast.parse(source)):
                    if isinstance(node, ast.Import):
                        need(all(a.name in allowed for a in node.names), 'unreviewed import')
                    if isinstance(node, ast.ImportFrom):
                        need(node.level == 0 and node.module in allowed, 'unreviewed import-from')
            sources[name] = source
    rows = parsed(sources[spec['target']])['rows']
    expected_labels = [(r['index'], sign) for r in rows
                       if Fraction(r['lambda_max']) > spec['threshold'] for sign in (-1, 1)]
    need(expected_labels == [(i, sign) for i in range(spec['start'], spec['end'])
                             for sign in (-1, 1)], 'selected complete row cover')
    tasks = [r for r in manifest['low_rows'] if r['family'] == family]
    wanted = []
    for i, sign in expected_labels:
        h, outer = grid(family, i, sign)
        suffix = 'minus' if sign < 0 else 'plus'
        wanted.append(dict(H_cells=h, cwd=PREFIX + family, family=family,
                           file='row_%02d_%s.json' % (i, suffix), index=i,
                           kind='low-row', outer_phase_cells=outer, sign=sign,
                           task_id='61.low.%s.%02d.%s' % (family, i, suffix)))
    need(tasks == wanted and len(tasks) == spec['count'], 'exact ordered tasks and grids')
    actions = [a for a in manifest['actions']
               if a.get('script') == PREFIX + family + '/bind_low42.py']
    need(len(actions) == 1 and actions[0]['arguments'] == ['--replay'], 'original binder action')
    legacy = actions[0]['stdout_rule']['expected']
    need(legacy['negative_controls'] == CONTROLS and legacy['rows'] == spec['count']
         and legacy['index_sha256'] == spec['index_sha'], 'original complete output/control contract')
    return dict(family=family, tasks=tasks, rows=rows, sources=sources,
                index_name=record['index_name'], index_schema=record['index_schema'],
                index_sha256=spec['index_sha'], legacy=legacy)


def _one_pass(plan, destination, contract, kernel, binder, source_guard):
    """Internal mechanism. Injectable only for tests, never a receipt acceptor.

    Native entry below supplies only freshly loaded pinned modules. This core
    returns a protocol summary; it cannot authenticate its caller's modules.
    """
    destination = Path(destination)
    row_directory = destination / 'low_rows'
    row_directory.mkdir(exist_ok=False)
    rows = contract.read()
    need(rows == plan['rows'], 'actual pinned target table')
    rows_by_index = {row['index']: row for row in rows}
    need(len(rows_by_index) == len(rows), 'unique target row indices')
    entries, owned = [], []
    calls = 0
    for task in plan['tasks']:
        source_guard()
        i, sign = task['index'], task['sign']
        need(type(i) is int and type(sign) is int and sign in (-1, 1), 'strict task labels')
        row = rows_by_index[i]
        cfg = contract.selected(row, sign, task['H_cells'], task['outer_phase_cells'])
        need(type(cfg['N']) is int and cfg['N'] == 42
             and type(cfg['H_cells']) is int and cfg['H_cells'] == task['H_cells']
             and type(cfg['outer_phase_cells']) is int
             and cfg['outer_phase_cells'] == task['outer_phase_cells'], 'exact selected grid')
        before = freeze(cfg)
        # These pure memoized helpers are reset to preserve producer isolation.
        for name in ('exp_inverse_upper', 'poisson_numerator', 'poisson'):
            function = getattr(kernel, name, None)
            if function is not None:
                function.cache_clear()
        proof, report = kernel.evaluate(cfg)
        calls += 1
        need(freeze(cfg) == before, 'kernel mutated input configuration')
        packet = dict(index=i, sign=sign, proof=proof, report=report)
        raw = encoded(packet)
        # Match all returned fields, not merely a PASS/count/digest assertion.
        need(freeze(parsed(raw)) == freeze(packet), 'whole fresh output round trip')
        name = task['file']
        need(name == 'row_%02d_%s.json' % (i, 'minus' if sign < 0 else 'plus'), 'fixed output path')
        with (row_directory / name).open('xb') as stream:
            stream.write(raw)
        need((row_directory / name).read_bytes() == raw, 'fresh row write equality')
        pin = sha256(raw).hexdigest()
        owned.append((name, pin, freeze(packet)))
        entries.append(dict(index=i, sign=sign, file=name, sha256=pin))
    need(calls == len(plan['tasks']), 'one completed evaluation per task')
    index = dict(schema=plan['index_schema'], rows=entries)
    raw_index = encoded(index)
    need(sha256(raw_index).hexdigest() == plan['index_sha256'], 'original frozen index hash')
    with (destination / plan['index_name']).open('xb') as stream:
        stream.write(raw_index)
    source_guard()
    # Execute the unchanged non-arithmetic binder and all nine controls.
    summary = binder.check(parsed(raw_index), replay=False)
    controls = binder.controls(parsed(raw_index))
    need(controls == CONTROLS, 'all original binder negative controls')
    expected = {key: plan['legacy'][key]
                for key in ('rows', 'strict_gates', 'worst_score', 'row_digest')}
    need(freeze(summary) == freeze(expected), 'all original numerical summary fields')
    # A return value from a supplied receipt is never substituted for evaluate.
    for name, pin, packet in owned:
        path = row_directory / name
        need(path.is_file() and not path.is_symlink(), 'regular fresh row')
        raw = path.read_bytes()
        need(sha256(raw).hexdigest() == pin and freeze(parsed(raw)) == packet,
             'whole output still equals the result computed in this invocation')
    need((destination / plan['index_name']).read_bytes() == raw_index, 'index unchanged')
    source_guard()
    return dict(kernel_calls=calls, original_nonarithmetic_summary=summary,
                negative_controls=controls, index_sha256=plan['index_sha256'])


def run_family(archive, family, destination):
    """Unexecuted candidate native entry; authorization is external, not a flag."""
    need(__debug__ and not sys.flags.optimize and sys.flags.isolated
         and sys.flags.no_site and sys.dont_write_bytecode,
         'native candidate requires a fresh python -I -B -S interpreter, without -O')
    need(not any(name in sys.modules for name in MODULES), 'fresh native module namespace')
    plan = load_plan(archive, family)
    destination = Path(destination).absolute()
    need(all(not parent.is_symlink() for parent in (destination, *destination.parents)), 'no destination links')
    need(destination.parent.is_dir(), 'existing destination parent')
    destination.mkdir(exist_ok=False)
    for name, raw in plan['sources'].items():
        with (destination / name).open('xb') as stream:
            stream.write(raw)
    pins = {name: sha256(raw).hexdigest() for name, raw in plan['sources'].items()}
    adapter_pin = sha256(Path(__file__).read_bytes()).hexdigest()

    def guard():
        need(sha256(Path(__file__).read_bytes()).hexdigest() == adapter_pin, 'adapter bytes changed')
        for name, pin in pins.items():
            path = destination / name
            need(path.is_file() and not path.is_symlink()
                 and sha256(path.read_bytes()).hexdigest() == pin, 'immutable source: ' + name)

    # A pinned runtime/supervisor is still required by any production integration.
    # This local trace records accidental reads/writes; it is not an OS sandbox.
    active = True
    reads, unexpected, writes = set(), set(), set()
    runtime = tuple(Path(value).resolve() for value in {sys.prefix, sys.base_prefix})
    adapter = Path(__file__).resolve()

    def audit(event, args):
        if not active or event != 'open' or not args or isinstance(args[0], int):
            return
        try:
            path = Path(args[0]).resolve()
        except (TypeError, ValueError, OSError):
            return
        mode = args[1] if len(args) > 1 else None
        flags = args[2] if len(args) > 2 and type(args[2]) is int else 0
        writing = (type(mode) is str and any(c in mode for c in 'wa+')) or bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT))
        contained = path == destination or destination in path.parents
        if writing:
            writes.add(str(path))
            need(contained and path.name not in pins, 'write outside new outputs or into source')
        elif path.is_file():
            reads.add(str(path))
            if not contained and path != adapter and not any(path == p or p in path.parents for p in runtime):
                unexpected.add(str(path))
    sys.addaudithook(audit)
    try:
        modules = {}
        for name in MODULES:
            guard()
            spec = importlib.util.spec_from_file_location(name, destination / (name + '.py'))
            module = importlib.util.module_from_spec(spec)
            sys.modules[name] = module
            spec.loader.exec_module(module)
            modules[name] = module
        result = _one_pass(plan, destination, modules['central42_contract'],
                           modules['central42_kernel'], modules['bind_low42'], guard)
        need(not unexpected, 'undeclared runtime/source read')
        guard()
    finally:
        active = False
        with (destination / 'ONEPASS-TRACE.json').open('xb') as stream:
            stream.write(encoded(dict(reads=sorted(reads), writes=sorted(writes),
                                      unexpected_reads=sorted(unexpected))))
    result.update(schema='be.candidate-onepass-low/1',
                  status='CONDITIONAL_ONEPASS_LOW_COMPUTED', family=family,
                  native_arithmetic_executed=True, original_binder_replay_executed=False,
                  source_archive_sha256=ARCHIVE_SHA, source_manifest_sha256=MANIFEST_SHA,
                  source_pins=pins, adapter_sha256=adapter_pin,
                  runtime_seal_and_supervisor_integration_required=True,
                  coordinator_execution_authentication_required=True,
                  current_parent_licenses_required=True, all_law_provider=False,
                  full_proof_pass=False)
    with (destination / 'ONEPASS-CANDIDATE.json').open('xb') as stream:
        stream.write(encoded(result))
    return result


def inventory(archive):
    families = []
    for name in SPECS:
        plan = load_plan(archive, name)
        families.append(dict(family=name, rows=len(plan['tasks']),
                             source_pins={p: sha256(raw).hexdigest() for p, raw in plan['sources'].items()},
                             expected_index_sha256=plan['index_sha256'],
                             recorded_strict_gates=plan['legacy']['strict_gates']))
    return dict(status='SOURCE_INVENTORY_ONLY', families=families,
                native_arithmetic_executed=False, full_proof_pass=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', nargs='?', choices=('inventory', 'run-family'), default='inventory')
    parser.add_argument('--archive', type=Path, default=ROOT / 'verification/finite-tail/sources/backend.zip')
    parser.add_argument('--family', choices=tuple(SPECS))
    parser.add_argument('--destination', type=Path)
    args = parser.parse_args()
    if args.mode == 'run-family':
        need(args.family and args.destination, 'explicit family and new destination')
        result = run_family(args.archive, args.family, args.destination)
    else:
        need(args.family is None and args.destination is None, 'inventory has no execution arguments')
        result = inventory(args.archive)
    print(encoded(result).decode(), end='')


if __name__ == '__main__':
    main()

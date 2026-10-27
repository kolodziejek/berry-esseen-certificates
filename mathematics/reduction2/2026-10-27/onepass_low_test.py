#!/usr/bin/env python3
"""Bounded protocol tests, using unchanged binders with tiny fake arithmetic.

Never imports/executes the archived normalizer, contract or numerical kernel.
The binder bodies were read before execution; their __main__ blocks do not run.
All temporary proof objects are visibly synthetic and never qualify as LOW.
"""
import copy
from contextlib import contextmanager
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from types import ModuleType


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('onepass_reviewed_adapter', HERE / 'onepass_low.py')
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


def fixture_contract(plan):
    module = ModuleType('central42_contract')
    def read():
        return copy.deepcopy(plan['rows'])
    def selected(row, sign, hcells, ocells):
        return dict(N=42, H_cells=hcells, outer_phase_cells=ocells,
                    bands=1, fixture_index=row['index'], phase_sign=sign,
                    pl=F(row['p'][0]), pu=F(row['p'][1]),
                    fixture_p=copy.deepcopy(row['p']), fixture_nested=[F(1, 3)])
    module.read, module.selected = read, selected
    return module


class FakeKernel(ModuleType):
    def __init__(self, family, mutation=None):
        super().__init__('central42_kernel')
        self.family, self.mutation, self.calls = family, mutation, 0

    def evaluate(self, cfg):
        self.calls += 1
        if self.mutation == 'partial_exception' and self.calls == 5:
            raise ArithmeticError('intentional synthetic gate failure')
        i, sign = cfg['fixture_index'], cfg['phase_sign']
        # A few exact fixture inequalities, not any archived LOW inequality.
        reserves = [F(i + 1, i + 2), F(sign * sign), F(1, 100)]
        if not all(value > 0 for value in reserves):
            raise ArithmeticError('synthetic gate failure')
        cells = cfg['H_cells'] * cfg['outer_phase_cells']
        empty = self.family == 'left42_final' and i == 8 and sign == -1
        count = 0 if empty else cells
        score = None if empty else -F(1, 100) - F(i, 1000000)
        schema = 'SYNTHETIC_PROTOCOL_FIXTURE_ONLY'
        contract = dict(schema=schema, N=42, p=cfg['fixture_p'], H_cells=cfg['H_cells'],
                        constants={k: str(v) for k, v in cfg.items() if type(v) in (int, F)})
        proof = dict(schema=schema, contract=contract, mark_count=count,
                     marks_sha256=sha256(str((i, sign)).encode()).hexdigest())
        native_status = 'PASS_EXACT_CONDITIONAL_' + ('CENTRAL' if self.family == 'central42_v2' else 'LEFT') + '42_JOINT'
        report = dict(status=native_status, failed_gates={}, gates=len(reserves),
                      endpoints=2 * count, feasible_cells=count, empty_cells=cells - count,
                      phase_envelope_cells=0,
                      gate_sha256=sha256(str(reserves).encode()).hexdigest(),
                      worst_score=str(score), worst_score_decimal=float(score) if score is not None else None,
                      minimum_reserves={'fixture': str(min(reserves))},
                      scope='SYNTHETIC FIXTURE; NOT LOW ARITHMETIC; NOT A CERTIFICATE')
        if self.mutation == 'mutated_configuration':
            cfg['fixture_nested'][0] = F(2, 3)
        if self.mutation == 'wrong_contract':
            proof['contract']['N'] = 41
        if self.mutation == 'nonfinite_output':
            report['worst_score_decimal'] = float('nan')
        return proof, report


@contextmanager
def unchanged_binder(plan, directory, contract, kernel):
    """Execute only the small, pinned binder, with explicit fake dependencies."""
    replaced = {name: sys.modules.get(name) for name in ('central42_contract', 'central42_kernel')}
    sys.modules['central42_contract'] = contract
    sys.modules['central42_kernel'] = kernel
    raw = plan['sources']['bind_low42.py']
    path = directory / 'bind_low42.py'
    path.write_bytes(raw)
    module = ModuleType('fixture_unchanged_binder')
    module.__file__ = str(path)
    try:
        exec(compile(raw, str(path), 'exec'), module.__dict__)
        yield module
    finally:
        for name, old in replaced.items():
            if old is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = old


def reference_two_pass(real, directory):
    """Independent fixture reference: original producer serializer + full replay."""
    contract, kernel = fixture_contract(real), FakeKernel(real['family'])
    directory.mkdir()
    (directory / 'low_rows').mkdir()
    entries = []
    for task in real['tasks']:
        row = next(r for r in contract.read() if r['index'] == task['index'])
        cfg = contract.selected(row, task['sign'], task['H_cells'], task['outer_phase_cells'])
        proof, report = kernel.evaluate(cfg)
        packet = dict(index=task['index'], sign=task['sign'], proof=proof, report=report)
        # Deliberately do not use the adapter serializer for reference generation.
        raw = (json.dumps(packet, indent=2) + '\n').encode('utf-8')
        (directory / 'low_rows' / task['file']).write_bytes(raw)
        entries.append(dict(index=task['index'], sign=task['sign'], file=task['file'],
                            sha256=sha256(raw).hexdigest()))
    index = dict(schema=real['index_schema'], rows=entries)
    raw_index = (json.dumps(index, indent=2) + '\n').encode('utf-8')
    (directory / real['index_name']).write_bytes(raw_index)
    with unchanged_binder(real, directory, contract, kernel) as binder:
        summary = binder.check(index, replay=True)
        controls = binder.controls(index)
    adapter.need(kernel.calls == 2 * len(real['tasks']), 'reference genuinely evaluates twice')
    adapter.need(controls == adapter.CONTROLS, 'reference all9 controls')
    fixture = copy.deepcopy(real)
    fixture['index_sha256'] = sha256(raw_index).hexdigest()
    fixture['legacy'].update(summary)
    fixture['fixture_only'] = True
    adapter.need(fixture['index_sha256'] != real['index_sha256'], 'fake outputs cannot satisfy native index')
    return fixture, summary, kernel.calls


def exercise(plan, directory, mutation=None):
    directory.mkdir()
    contract = fixture_contract(plan)
    kernel = FakeKernel(plan['family'], mutation)
    guards = []
    def guard():
        guards.append(True)
        adapter.need((directory / 'bind_low42.py').read_bytes() == plan['sources']['bind_low42.py'],
                     'fixture binder source changed')
    with unchanged_binder(plan, directory, contract, kernel) as binder:
        native_check, native_controls = binder.check, binder.controls
        if mutation == 'postcheck_row_corruption':
            def controls(obj):
                result = native_controls(obj)
                path = directory / 'low_rows' / plan['tasks'][-1]['file']
                path.write_bytes(path.read_bytes() + b' ')
                return result
            binder.controls = controls
        elif mutation == 'postcheck_index_corruption':
            def controls(obj):
                result = native_controls(obj)
                path = directory / plan['index_name']
                path.write_bytes(path.read_bytes() + b' ')
                return result
            binder.controls = controls
        elif mutation == 'lost_control':
            binder.controls = lambda obj: native_controls(obj)[:-1]
        elif mutation == 'changed_source':
            def check(obj, replay=False, load=True):
                result = native_check(obj, replay=replay, load=load)
                path = directory / 'bind_low42.py'
                path.write_bytes(path.read_bytes() + b'\n')
                return result
            binder.check = check
        result = adapter._one_pass(plan, directory, contract, kernel, binder, guard)
    adapter.need(len(guards) >= len(plan['tasks']) + 2, 'source checks surround each row and binding')
    return result, kernel.calls


def main():
    adapter.need(__debug__ and not sys.flags.optimize, 'unoptimized tests')
    archive = adapter.ROOT / 'verification/finite-tail/sources/backend.zip'
    inventory = adapter.inventory(archive)
    results, rejected = [], []
    with TemporaryDirectory(prefix='be-onepass-fixtures-') as temp:
        root = Path(temp)
        plans = {}
        for family in adapter.SPECS:
            real = adapter.load_plan(archive, family)
            reference = root / (family + '-legacy')
            fixture, summary, old_calls = reference_two_pass(real, reference)
            plans[family] = (real, fixture)
            destination = root / (family + '-onepass')
            result, calls = exercise(fixture, destination)
            adapter.need(result['original_nonarithmetic_summary'] == summary, 'same complete summary')
            adapter.need(calls == len(real['tasks']) and result['kernel_calls'] == calls, 'one evaluation per row')
            for task in real['tasks']:
                adapter.need((destination / 'low_rows' / task['file']).read_bytes()
                             == (reference / 'low_rows' / task['file']).read_bytes(), 'all original row bytes identical')
            adapter.need((destination / real['index_name']).read_bytes()
                         == (reference / real['index_name']).read_bytes(), 'canonical index bytes identical')
            results.append(dict(family=family, legacy_fixture_evaluations=old_calls,
                                onepass_fixture_evaluations=calls, saved_fixture_evaluations=old_calls-calls,
                                all_row_bytes_identical=True, index_bytes_identical=True,
                                unchanged_binder_controls=result['negative_controls'],
                                empty_left_fixture_included=family == 'left42_final'))
        real, fixture = plans['left42_final']
        cases = [(name, None) for name in ('mutated_configuration', 'wrong_contract',
                 'nonfinite_output', 'partial_exception', 'postcheck_row_corruption',
                 'postcheck_index_corruption', 'lost_control', 'changed_source')]
        wrong_pin = copy.deepcopy(fixture)
        wrong_pin['index_sha256'] = '0' * 64
        cases.append(('wrong_index_pin', wrong_pin))
        wrong_summary = copy.deepcopy(fixture)
        wrong_summary['legacy']['strict_gates'] += 1
        cases.append(('wrong_summary', wrong_summary))
        cases.append(('fixture_cannot_meet_native_index', real))
        missing = copy.deepcopy(fixture)
        missing['tasks'].pop()
        cases.append(('missing_row', missing))
        for number, (name, replacement) in enumerate(cases):
            try:
                exercise(replacement or fixture, root / ('bad-%02d' % number), name)
            except (ValueError, ArithmeticError) as exc:
                rejected.append(dict(name=name, reason=str(exc)))
            else:
                raise AssertionError('invalid protocol accepted: ' + name)
        # A supplied completion receipt cannot enter the candidate native API.
        try:
            adapter.run_family(archive, 'left42_final', root / 'never-used', receipts={'outcome': 'PASS'})
        except TypeError:
            rejected.append(dict(name='supplied_receipt', reason='native entry has no receipt input'))
        else:
            raise AssertionError('receipt input accepted')
        changed = root / 'changed-archive.zip'
        raw = bytearray(archive.read_bytes())
        raw[-1] ^= 1
        changed.write_bytes(raw)
        try:
            adapter.load_plan(changed, 'left42_final')
        except ValueError as exc:
            rejected.append(dict(name='changed_archive', reason=str(exc)))
        else:
            raise AssertionError('changed source archive accepted')
    print(json.dumps(dict(status='PASS_ONEPASS_PROTOCOL_FIXTURES_ONLY',
                         native_low_arithmetic_executed=False,
                         unchanged_binder_functions_executed_on_synthetic_data=True,
                         full_proof_pass=False, inventory=inventory,
                         families=results, additional_rejections=rejected,
                         native_execution_and_production_integration='NOT RUN / NOT ACCEPTED'), indent=2))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Bounded static evidence only. Never imports or executes archived programs.

Verifies selected manifest/blob bindings and enumerates the recorded finite
support interfaces. A PASS is not an arithmetic replay or an analytic proof.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[3]
ARCHIVE = ROOT / 'verification/finite-tail/sources/backend.zip'
CAPSULE = 'work/toward40_20261007/audit43/capsule/'
WORK = CAPSULE + 'work/below49_20261006/'
SOURCES = [
    CAPSULE + 'proofs/' + p for p in (
        'cutoff44.tex', 'joint_resource.tex', 'local42_improvements.tex',
        'local42_signed_gaussian_v2.tex',
        'paired_extension_with_signed_k.tex', 'signed_cubic_repair.tex')
] + [WORK + p for p in (
    'acquisition/check_local42_support.py',
    'acquisition/accept_initial42.py',
    'acquisition/local_signed_core.py',
    'acquisition/coupled_panel_core.py',
    'acquisition/corrected_phase_callback_v2.py',
    'acquisition/high_window_core.py',
    'acquisition/panel_exterior.py',
    'acquisition/central42_acquisition_core.py',
    'acquisition/central42_confinement_core.py',
    'acquisition/central42_profile_core.py',
    'acquisition/sperner_kernel.py',
    'package_audit/left42_exact/accept_acquisition.py',
    'package_audit/left42_exact/acquisition42_proof.json',
    'package_audit/left42_exact/fifth_heat50.py',
    'package_audit/left42_exact/heat_support50.py',
    'package_audit/left42_exact/panel_exterior42.py',
    'package_audit/left42_exact/corrected_phase_callback_extended.py',
    'package_audit/left42_exact/paired_extended.py',
    'package_audit/left42_confinement/confinement_core.py',
    'package_audit/left42_confinement/profile_core.py',
    'local/left42_final/bind_source42.py',
    'local/left42_final/central42_kernel.py',
    'local/left42_final/central42_contract.py',
    'local/left42_final/tiny42_normalization.py',
    'local/left42_final/mid42_contract.py',
    'local/left42_final/accept_mid42.py',
    'local/left42_tiny_final/normalization_piecewise42_v2.py',
    'entry/cutoff44/check_cutoff44_composition.py',
)]


def need(value, message):
    if not value:
        raise ValueError(message)


def support_contract(row):
    need(row['n_band'] == [42, 48], 'finite support scope')
    need(F(row['barrier']) == 0 and F(row['slow']) == F(19, 100),
         'support decrement and barrier')
    need(F(row['current_score_lower']) == F(819, 2000), 'score floor')
    r, b, radius = map(F, (row['rho_upper'], row['beta_absolute_upper'], row['radius']))
    need(1 <= r <= F(3, 2) and 0 <= b <= F(1, 2), 'left moment rectangle')
    need(F(5, 2) <= radius <= F(121, 40), 'left radius scope')
    cells = [tuple(map(F, c)) for c in row['closed_cells']]
    need(cells and cells[0][0] == radius and cells[-1][1] == F(9, 2),
         'support closed coverage endpoints')
    need(all(a < b for a, b in cells) and
         all(a[1] == b[0] for a, b in zip(cells, cells[1:])),
         'support contiguous closed coverage')
    return r, b, radius


def main():
    bindings = []
    with ZipFile(ARCHIVE) as z:
        manifest_bytes = z.read('finite61/MANIFEST.json')
        manifest = json.loads(manifest_bytes)['files']
        contents = {}
        for path in SOURCES:
            record = manifest[path]
            blob = z.read('finite61/blobs/' + record['sha256'])
            need(sha256(blob).hexdigest() == record['sha256'], 'blob hash: ' + path)
            need(len(blob) == record['bytes'], 'blob byte count: ' + path)
            contents[path] = blob
            bindings.append(dict(path=path, sha256=record['sha256'],
                                 lines=len(blob.splitlines()), bytes=len(blob)))
    proof = json.loads(contents[WORK + 'package_audit/left42_exact/acquisition42_proof.json'])
    need((proof['N'], proof['L'], F(proof['cap'])) == (42, 48, F('0.4226')), 'finite input scope')
    support_rows = [proof['first_bridge']]
    support_rows.extend(step['contraction'] for row in proof['fine']
                        for step in row['trace'] if step['contraction'] is not None)
    need(len(support_rows) == 64, 'complete recorded support call count')
    triples = [support_contract(row) for row in support_rows]
    active = [row for row in proof['coarse'] if not row.get('excluded')]
    first = support_rows[0]
    need(F(first['rho_upper']) == max(F(row['rho']) for row in active), 'first common rho cap')
    need(F(first['beta_absolute_upper']) == max(F(row['beta']) for row in active), 'first common beta cap')
    # Disposable malformed interface controls: reject scope drift and a gap.
    controls = []
    for name, change in [('wrong_upper_index', lambda x: x.update(n_band=[42, 49])),
                         ('wrong_decrement', lambda x: x.update(slow='0')),
                         ('lost_closed_cell', lambda x: x['closed_cells'].pop(1))]:
        row = json.loads(json.dumps(first))
        change(row)
        try:
            support_contract(row)
        except ValueError:
            controls.append(name)
        else:
            raise ValueError('malformed interface accepted: ' + name)
    print(json.dumps(dict(
        status='PASS_STATIC_UNIFORM42_INTERFACE_CENSUS',
        mathematical_status='Static bindings and recorded interface extrema only; analytic and arithmetic acceptance remain separate.',
        execution_status='Fresh standard-library static check; no archived program execution.',
        archive_sha256=sha256(ARCHIVE.read_bytes()).hexdigest(),
        manifest_sha256=sha256(manifest_bytes).hexdigest(),
        source_bindings=bindings, left_support_calls=len(triples),
        left_rho_min=str(min(t[0] for t in triples)),
        left_rho_max=str(max(t[0] for t in triples)),
        left_beta_max=str(max(t[1] for t in triples)),
        left_radius_max=str(max(t[2] for t in triples)),
        first_support=dict(rho=first['rho_upper'], beta=first['beta_absolute_upper']),
        negative_controls=controls), indent=2))


if __name__ == '__main__':
    need(__debug__ and not sys.flags.optimize, 'unoptimized Python')
    main()

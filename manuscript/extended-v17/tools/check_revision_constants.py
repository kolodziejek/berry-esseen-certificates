#!/usr/bin/env python3
"""Run the changed scalar checks and bind their actual source/output bytes.

The component proofs remain in the manuscript. This driver is an execution
summary, not an independent mathematical verifier or a finite-base proof.
An optional output path must be new; stdout/stderr and a receipt are retained.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    if not __debug__ or sys.flags.optimize:
        raise RuntimeError('Unoptimized Python is required')
    here = Path(__file__).resolve().parent
    output = args.output_dir.resolve() if args.output_dir else None
    if output is not None:
        output.mkdir(parents=True, exist_ok=False)
    jobs = [
        ('geometry', 'PASS_REVISION_GEOMETRY_CONSTANTS'),
        ('count', 'PASS_REVISION_COUNT_CONSTANTS'),
        ('foundation', 'PASS_REVISION_FOUNDATION_CONSTANTS'),
    ]
    records = []
    for name, expected in jobs:
        source = here / ('check_revision_' + name + '_constants.py')
        command = [sys.executable, '-I', '-B', str(source)]
        result = subprocess.run(command, cwd=here.parents[2],
                                capture_output=True, timeout=60)
        try:
            status = json.loads(result.stdout).get('status')
        except (ValueError, UnicodeError):
            status = None
        if output is not None:
            (output / (name + '.stdout.json')).write_bytes(result.stdout)
            (output / (name + '.stderr.txt')).write_bytes(result.stderr)
        records.append(dict(name=name, command=command,
                            returncode=result.returncode, status=status,
                            accepted=result.returncode == 0 and status == expected,
                            source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                            stdout_sha256=hashlib.sha256(result.stdout).hexdigest(),
                            stderr_sha256=hashlib.sha256(result.stderr).hexdigest()))
    ok = all(record['accepted'] for record in records)
    receipt = dict(
        status='PASS_REVISION_SCALAR_CHECKS' if ok else 'FAILED_REVISION_SCALAR_CHECKS',
        python=sys.version, utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        mathematical_scope='Changed scalar identities and comparisons; continuous proofs remain in the text. No finite-base or full-conjecture acceptance.',
        checks=records,
        tex_sha256={str(path.relative_to(here.parent)): hashlib.sha256(path.read_bytes()).hexdigest()
                    for path in sorted(here.parent.rglob('*.tex'))},
    )
    encoded = json.dumps(receipt, indent=2) + '\n'
    if output is not None:
        (output / 'receipt.json').write_text(encoded)
    print(encoded, end='')
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())

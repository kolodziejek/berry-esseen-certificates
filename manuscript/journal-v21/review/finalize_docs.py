"""Write publication documentation for the real, completed release candidate."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import sys
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE.parent / sys.argv[1]
PDF = Path(sys.argv[2]).resolve()


def H(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(relative):
    return json.loads((ROOT / relative).read_text())


def replace(text, old, new):
    assert text.count(old) == 1, old[:100]
    return text.replace(old, new)


def main():
    if not __debug__ or sys.flags.optimize:
        raise RuntimeError('unoptimized documentation assembly required')
    assert OUT.parent == HERE.parent and OUT.is_dir()
    prep = json.loads((OUT / 'PREPARATION.json').read_text())
    assert prep['status'] == 'PREPARED_COMPLETE_REPLACEMENT_RELEASE_CANDIDATE'
    for path, pin in prep['files'].items():
        assert H(OUT / path) == pin
    build_root = PDF.parent.parent
    process = json.loads((build_root / 'PROCESS.json').read_text())
    build = json.loads((build_root / 'stdout.txt').read_text())
    expected_sources = {str((OUT / p).resolve()): pin
                        for p, pin in prep['files'].items()
                        if Path(p).suffix in ('.tex', '.bib')}
    assert process['returncode'] == 0 and process['sources_unchanged'] is True
    assert process['source_before'] == process['source_after'] == expected_sources
    assert Path(build['rootFile']).resolve() == (OUT / 'main.tex').resolve()
    assert build['pdfExists'] is True and Path(build['pdfPath']).resolve() == PDF
    assert build['attempts'][-1]['exitCode'] == 0
    assert not (build_root / 'stderr.txt').read_bytes()
    pages = len(PdfReader(PDF).pages)
    central_path = 'runs/central_comparison_20261104/finite_portable_cover_union01/accepted/RESULT.json'
    central = read(central_path)
    assert central['status'] == 'PASS_EXACT_COMPLETE_CENTRAL_FINITE_COMPARISON'
    totals = {k: sum(r[k] for r in central['results']) for k in ('quartics', 'excluded', 'splits')}
    archive_hashes = {name: H(OUT / 'certificates/direct-comparison' / (name + '.zip'))
                      for name in ('left', 'earlier', 'central')}
    documents = {}
    report = (HERE / 'docs/REVISION_REPORT_DRAFT.md').read_text()
    a = report.index('The main change replaces')
    report = '# Direct quartic comparison: revision report\n\n' + report[a:]
    report = report.replace('of the proposed replacement', 'of the replacement')
    report = report.replace('| Current status |', '| Exact verification |')
    report = replace(report, 'Complete comparison acceptance still pending', 'Complete relocated exact replay and coverage join; 24 corruption controls')
    a = report.index('The assembled preview has')
    b = report.index('A separate five-summand experiment', a)
    report = report[:a] + f'''The final manuscript has **{pages} total pages**, compared with 100 in v20.
The 11-point A4 layout and 28 mm margins are unchanged; the count includes
all analytic arguments, certificate explanations and references. The
approximately **60-page total goal remains unmet**. The local comparison
has become shorter, but the original acquisition and earlier finite proof
still occupy a substantial part of the paper. A separate numerical-table
compression was tested and saved no pages, so the explanatory table was kept.

''' + report[b:]
    report += f'''
The three finite families contain 30,030 row/index pairs. The central replay
checks {totals['quartics']:,} quartics, {totals['excluded']:,} resource exclusions
and 94,447,920 exact score coefficients, with no subdivisions. The left
family has 9,738 quartics and the earlier family has 2,090. These counts
describe arithmetic objects; the analytic reductions and their same-law
hypotheses are proved in the manuscript.

The final selected route uses the finite exclusion at 43–46 and the uniform
exclusion from 47 directly. The obsolete 42–48 wrapper, later left radius
2.7 and local confinement/MID/LOW comparisons are removed. The earlier
Fourier LOW estimates retain their distinct analytic purpose.

The original acquisition and unchanged finite-base evidence are preserved;
the full original campaign and its separate 114-command recipe were not
rerun. The overall manuscript remains a computer-assisted proof candidate
for independent human review. No proof-assistant certification, merge,
arXiv submission or journal submission is asserted.
'''
    documents['REVISION_REPORT.md'] = report

    proofmap = (HERE / 'docs/PROOF_MAP_DRAFT.md').read_text()
    a = proofmap.index('Mathematical status:')
    proofmap = '# Proof and certificate map\n\n' + proofmap[a:]
    proofmap = replace(proofmap, 'the new left,\nearlier finite and central-tail implications have completed exact checks at\nthe scopes below; central finite comparison acceptance remains pending.',
                       'all new left, earlier finite, central finite and central-tail\nimplications have completed exact checks at the scopes below.')
    proofmap = replace(proofmap, 'These exclusions, once the pending central calculation is accepted,\n   rule out', 'These exclusions rule out')
    proofmap = proofmap.replace('25,908 finite pairs at 47–999 **pending**', '25,908 exactly accepted finite pairs at 47–999')
    proofmap = replace(proofmap, 'The planned archives are', 'The archives are')
    proofmap = replace(proofmap, 'Byte checks and one full critical gap-panel smoke; complete comparison replay **pending**',
                       'Byte checks and one full critical gap-panel smoke; complete four-shard comparison replay, coverage join and 24 controls')
    proofmap = replace(proofmap, 'Preserved evidence and source/import checks; no new full relocated tail replay',
                       'Fresh complete 45-row acceptance, 21 controls and the four-quartic envelope through the portable supervisor')
    proofmap += '''
The earlier analytic consolidation reviews remain in
[`journal-v18/review`](../journal-v18/review/) and
[`journal-v19/review`](../journal-v19/review/). The new bounded derivations,
composition review and actual build record are under [`review`](review/).
These review records document their scopes; all essential analytic arguments
for the selected route remain in the PDF itself.
'''
    documents['PROOF_MAP.md'] = proofmap

    guide = (HERE / 'docs/CERTIFICATES_README_DRAFT.md').read_text()
    a = guide.index('Extract each archive')
    guide = '# Direct-comparison certificates\n\n' + guide[a:]
    guide = guide.replace('| Planned archive |', '| Archive |')
    guide = replace(guide, 'Pending final archive', '`' + archive_hashes['central'] + '`')
    guide = replace(guide, 'The release owner must confirm all three archive hashes against the final\npublished bytes.',
                    'All three hashes above match the published archive bytes.')
    guide = guide.replace('## Central package — completion pending', '## Central package')
    a = guide.index('The explicit central tail has two unchanged entry points:')
    b = guide.index('## Relation to the original evidence', a)
    guide = guide[:a] + f'''The portable tail supervisor runs the unchanged numerical readers, using a
system temporary directory and recording both actual child executions:

```sh
"$BE_PY" -I -B replay_tail.py /fresh/central-tail
```

It checks all 45 row premises, the serialized object, 21 rejection controls
and the common four-quartic envelope. The fresh relocated tail result matches
the original exact accepted result byte-for-byte.

The finite comparison's full relocated four-shard replay and coverage join
passed, with final result SHA-256 `{H(ROOT / central_path)}`. It accepts all
25,908 pairs and {totals['quartics']:,} quartics; all 24 new cover-capture
controls reject their malformed inputs. The finite binary gaps were fully
replayed in the original workspace; relocation verified their bytes and one
complete critical panel, without a second full gap campaign.

The archive roundtrip verifies every file by path, size and digest. It is
an integrity check, not another numerical replay. `COMPLETION.json` records
the precise execution boundaries and source/result joins. Preserved analytic
drafts inside the archive retain their historical pending labels; the final
manuscript and completion record state the completed scope.

''' + guide[b:]
    documents['certificates/direct-comparison/README.md'] = guide

    next_note = (HERE / 'docs/NEXT_SIMPLIFICATION_DRAFT.md').read_text()
    next_note = replace(next_note, '# Draft note on the next substantive simplification', '# Next substantive simplification')
    next_note += '''
The checked fixed-probability pilot is distributed in
[`research/fixed-pilot.zip`](research/fixed-pilot.zip). Its README gives a
standard-library replay, with the precise fixed-p/phase scope. It is outside
the selected proof graph. The next full-row experiment above remains unproved.
'''
    documents['SIMPLIFICATION_NEXT.md'] = next_note
    documents['README.md'] = f'''# A direct quartic comparison with exact certificates

[Read the complete manuscript candidate](main.pdf): **{pages} total pages**,
compared with 100 in v20. All analytic proofs, certificate explanations and
references are included, with unchanged typography. The approximately
60-page goal is **not yet achieved**.

The local argument now couples the conditional binomial counts and bounds
one resulting staircase function by a quartic polynomial. Exact moment
inequalities reduce the score comparison to finite polynomial checks.
This replaces the successive local confinement and noise comparisons.
An explicit four-polynomial calculation covers the unbounded central tail.

All new numerical obligations are complete: **30,030 finite row/index pairs**
across three families, together with the uniform central argument from
index 1,000. Each result retains its original acquisition hypotheses, whose
proofs remain in the manuscript. The overall claimed scope is unchanged:
the sharp weak inequality at every index, optimality of its constant, and
strictness for every index at least 47.

This is a locally derived and reviewed computer-assisted proof candidate
for independent human checking. Fresh arithmetic acceptance does not certify
the entire manuscript by itself, and no external referee or proof-assistant
verification is claimed.

- [Revision report](REVISION_REPORT.md): mathematical change, evidence and measured length.
- [Proof map](PROOF_MAP.md): selected dependencies and retained original evidence.
- [Certificate commands](certificates/direct-comparison/README.md): exact portable replays.
- [Further simplification](SIMPLIFICATION_NEXT.md): a proven fixed-location pilot and the unproved next full-row task.

The original evidence remains in
[`extended-v17/reproduction`](../extended-v17/reproduction/) at commit
`c31d0cbe2af867d26871fbae37a3a7f4066f4a55`. This revision does not claim a
new run of that entire campaign or its separate 114-command recipe. Earlier
manuscripts and original proof objects are unchanged.

With TeX Live, compile from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The delivered build uses TeX Live 2025. Its source/output record and bounded
analytic reviews are under `review/`. No merge or arXiv/journal submission
accompanies this draft.
'''
    documents['research/README.md'] = '''# Optional six-count research pilot

`fixed-pilot.zip` contains the exact n=5, p=77/200, k=2, u=0 comparison on
the full acquired noise interval, its analytic proof, separate exact replay
and independent moment review. It is **outside the selected manuscript
proof DAG** and does not prove a complete probability/phase row.

After extracting it, use its `README.md` and run:

```sh
python3 -I -B -S replay.py /absolute/path/to/NEW_OUTPUT
```

The unchanged acceptance program reproduced the original result and object
byte-for-byte after relocation. The package also supplies the explicit-law
obstruction calculation and independent actual-law controls. No acquisition
replay or complete n=5 replacement is inferred.

See [the next full-row experiment](../SIMPLIFICATION_NEXT.md) for the remaining
mathematical and coverage obligations.
'''
    for name, text in documents.items():
        assert not re.search(r'\bpending\b', text.lower().replace('historical pending labels', ''))
        path = OUT / name
        assert not path.exists()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    assert not (OUT / 'main.pdf').exists()
    shutil.copyfile(PDF, OUT / 'main.pdf')
    pilot = ROOT / 'work/count_quartic_shortening_20261104/portable_fixed_pilot.zip'
    assert H(pilot) == '31d704231ea4a3b82c689493b788c37d7497dd40669100c66bffb604d411b2e1'
    shutil.copyfile(pilot, OUT / 'research/fixed-pilot.zip')
    evidence = OUT / 'review'
    evidence.mkdir(exist_ok=False)
    for name in ('ANALYTIC_REVIEW.md', 'prepare_release.py', 'finalize_docs.py'):
        shutil.copyfile(HERE / name, evidence / name)
    for name in ('RELEASE_REVIEW.md', 'RELEASE_REVIEW02.md'):
        shutil.copyfile(HERE.parent / name, evidence / name)
    review_base = ROOT / 'work/earlier_local_comparison_20261104/integration/review_composition'
    for name in ('REVIEW.md', 'FIXED_TARGET_IDENTITY.md', 'MANIFEST.json'):
        target = evidence / 'composition' / name
        target.parent.mkdir(exist_ok=True)
        shutil.copyfile(review_base / name, target)
    for name in ('PROCESS.json', 'stdout.txt', 'stderr.txt'):
        shutil.copyfile(PDF.parent.parent / name, evidence / ('compile_' + name))
    receipt = {'scope': 'Publication documentation and byte copies after complete real replacement acceptance.',
               'pages': pages, 'pdf_sha256': H(PDF), 'central_result_sha256': H(ROOT / central_path),
               'compile_process_sha256': H(build_root / 'PROCESS.json'),
               'compile_stdout_sha256': H(build_root / 'stdout.txt'),
               'compile_stderr_sha256': H(build_root / 'stderr.txt'),
               'build_sources_match_preparation': True,
               'central_totals': totals, 'archives': archive_hashes,
               'optional_pilot_sha256': H(pilot), 'original_campaign_reexecuted': False,
               'external_referee_or_formal_verification': False}
    (evidence / 'PUBLICATION_BINDINGS.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()

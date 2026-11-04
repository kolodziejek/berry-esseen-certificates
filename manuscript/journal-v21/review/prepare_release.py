"""Create a release candidate only after all replacement campaigns complete.

This binds completed arithmetic records; the analytic review is separate.
It never changes the main Git repository or any frozen proof package.
"""
from pathlib import Path, PurePosixPath
import hashlib
import io
import json
import re
import stat
import sys
import zipfile

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
BASE = PROJECT / 'work/manuscript_revision_20261029/manuscript/journal-v20'
INTEGRATION = HERE.parent
OUT = INTEGRATION / (sys.argv[1] if len(sys.argv) == 2 else 'release01')
PINS = {}


def read(path):
    path = Path(path)
    data = path.read_bytes()
    PINS[str(path.relative_to(PROJECT))] = hashlib.sha256(data).hexdigest()
    return data


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key: ' + key)
        result[key] = value
    return result


def decode(data):
    return json.loads(data, object_pairs_hook=unique)


def load(relative, expected=None):
    data = read(PROJECT / relative)
    if expected is not None:
        assert hashlib.sha256(data).hexdigest() == expected
    return decode(data)


def captured_result(base, result_path):
    process = load(base + 'PROCESS.json')
    assert type(process['returncode']) is int and process['returncode'] == 0
    assert process['inputs_unchanged'] is True
    for name in ('stdout', 'stderr'):
        stream = read(PROJECT / base / (name + '.txt'))
        assert hashlib.sha256(stream).hexdigest() == process[name + '_sha256']
    summary = decode((PROJECT / base / 'stdout.txt').read_text().splitlines()[-1])
    data = read(PROJECT / base / result_path)
    assert hashlib.sha256(data).hexdigest() == summary['result_sha256']
    return decode(data)


def check_central_archive(data, union_hash, tail_hash):
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        names = archive.namelist()
        assert len(set(names)) == len(names)
        for info in archive.infolist():
            path = PurePosixPath(info.filename)
            assert not path.is_absolute() and '..' not in path.parts
            assert str(path) == info.filename and not info.is_dir()
            assert stat.S_IFMT(info.external_attr >> 16) == stat.S_IFREG
        prefixes = {PurePosixPath(name).parts[0] for name in names}
        assert len(prefixes) == 1
        prefix = next(iter(prefixes)) + '/'
        manifest = decode(archive.read(prefix + 'FILES.json'))
        seen = set()
        for item in manifest['files']:
            name = item['path']
            assert name not in seen
            seen.add(name)
            member = archive.read(prefix + name)
            assert len(member) == item['bytes']
            assert hashlib.sha256(member).hexdigest() == item['sha256']
        assert set(names) == {prefix + name for name in seen | {'FILES.json'}}
        completion = decode(archive.read(prefix + 'COMPLETION.json'))
        assert completion['status'] == 'PASS_COMPLETE_ACQUIRED_CENTRAL_COMPARISON'
        assert completion['finite']['row_n_pairs'] == 25908
        assert completion['finite']['result_sha256'] == union_hash
        assert completion['tail']['result_sha256'] == tail_hash
        for key in ('finite', 'tail'):
            result = archive.read(prefix + completion[key]['result'])
            assert hashlib.sha256(result).hexdigest() == completion[key]['result_sha256']


def replace(text, old, new):
    assert text.count(old) == 1, old[:120]
    return text.replace(old, new)


def main():
    if not __debug__ or sys.flags.optimize:
        raise RuntimeError('unoptimized Python is required for every completion gate')
    if len(sys.argv) > 2 or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', OUT.name) or OUT.parent != INTEGRATION:
        raise ValueError('give one fresh simple directory name below the integration directory')
    earlier = load('runs/earlier_local_comparison_20261104/analytic_complete01/acceptance/accepted/RESULT.json',
                   '92c9f2f231292289b20205434e66f6f67b3985c9be1f9bf3ce7bfee9bb2e0c08')
    assert earlier['complete_737'] is True and earlier['selected_pairs'] == 737
    central_base = 'runs/central_comparison_20261104/finite_portable_cover_union01/'
    central = captured_result(central_base, 'accepted/RESULT.json')
    assert central['status'] == 'PASS_EXACT_COMPLETE_CENTRAL_FINITE_COMPARISON'
    assert central['pairs'] == 25908 and central['rows'] == 45
    assert central['finite_n_domain'] == [47, 999]
    controls_base = 'runs/central_comparison_20261104/finite_portable_cover_controls01/'
    controls = captured_result(controls_base, 'checked/RESULT.json')
    assert controls['status'] == 'PASS_BOUNDED_CENTRAL_COVER_CAPTURE_CONTROLS'
    assert controls['rejections'] == 24
    load('runs/finite_left_replacement_20261104/root_complete_strong01/accepted/RESULT.json',
         'be20420c707a23b5bf69f5b5fdbad0792c17bf8b9b101d9700837d04ca10db34')
    tail_files = load('work/finite_left_replacement_20261104/audit/central_transfer/FINAL_FILES.json')
    for relative, item in tail_files['files'].items():
        data = read(PROJECT / relative)
        assert len(data) == item['bytes'] and hashlib.sha256(data).hexdigest() == item['sha256']
    tail_result_path = 'runs/finite_left_replacement_20261104/audit_central_all45_readback01/accepted/RESULT.json'
    tail = load(tail_result_path)
    assert tail['status'] == 'PASS_EXACT_COMPLETE_EARLY_CENTRAL45_N_GE_1000_TAIL'
    assert tail['probability_rows'] == 45 and len(tail['negative_controls']) == 21

    # Required complete archives must exist before any release directory is made.
    archives = [
        ('left.zip', PROJECT / 'deliverables/BE_finite_left_comparison_20261104.zip',
         'b74b0b5fbccd774a0729cdc7b4666ddcd9b248b203dbb254ec45e09a8b085397'),
        ('earlier.zip', PROJECT / 'work/earlier_local_comparison_20261104/portable01.zip',
         '53dc19350d841290835bce2fc8dc0d5ab2e433bbafc49eebd52df004d26b292f'),
        ('central.zip', PROJECT / 'deliverables/central_comparison_complete_20261104.zip', None),
    ]
    archive_data = {}
    for name, path, expected in archives:
        data = read(path)
        assert expected is None or hashlib.sha256(data).hexdigest() == expected
        archive_data[name] = data
    check_central_archive(archive_data['central.zip'],
                          PINS[central_base + 'accepted/RESULT.json'], PINS[tail_result_path])

    sources = {}
    for path in sorted(BASE.glob('*.bib')):
        sources[path.name] = read(path).decode()
    for path in sorted((BASE / 'sections').glob('*.tex')):
        sources[str(path.relative_to(BASE))] = read(path).decode()
    for name in ('introduction', 'certificates', 'finite'):
        text = read(HERE / (name + '_draft.tex')).decode()
        assert text.splitlines()[0].startswith('% ')
        sources['sections/' + name + '.tex'] = '\n'.join(text.splitlines()[1:]) + '\n'

    prefix = sources['sections/local.tex'].split(
        r'\subsection{Confinement from the remaining defect budget}')
    assert len(prefix) == 2
    prefix = prefix[0]
    a = prefix.index('For the later acquired domains, the conditional cubic bound')
    b = prefix.index('There is also a convenient cell-constant correction.', a)
    signed = read(INTEGRATION / 'RETAINED_SIGN_PARAGRAPH.tex').decode()
    signed = '\n'.join(line for line in signed.splitlines() if not line.startswith('%'))
    signed = replace(signed, 'The preserved arithmetic also checks additional\ndomains from the former feedback sequence; those extra checks are not\nsteps or premises of the direct comparison below.', '')
    prefix = prefix[:a] + signed + '\n\n' + prefix[b:]
    review = PROJECT / 'work/earlier_local_comparison_20261104/integration/review_composition'
    a = prefix.index('The selected consequences used in the resource schedule are:')
    b = prefix.index(r'\subsection{Acquiring simultaneous resources', a)
    prefix = prefix[:a] + read(review / 'support-consequences-proposed.tex').decode() + '\n\n' + prefix[b:]
    prefix = replace(prefix, 'outer-gap, and confinement-error estimates.', 'and outer-gap estimates.')
    prefix = replace(prefix, 'Apply a separately proved support or confinement implication,',
                     'Apply a separately proved support implication,')
    prefix = replace(prefix, 'This is the correction selected for the additional index--46\ncalculation. Both forms keep', 'Both forms keep')
    direct = read(INTEGRATION / 'direct_comparison.tex').decode()
    direct = replace(direct, r'\textbf{Pending complete gap/comparison acceptance.}',
                     'Complete finite binary gaps and exact comparison accepted.')
    direct = replace(direct, r'\textbf{Pending complete acceptance.}',
                     'Complete exact comparison accepted.')
    direct = replace(direct, r'\begin{assertion}[Earlier finite comparison, pending full acceptance]',
                     r'\begin{proposition}[Earlier finite comparison]')
    direct = replace(direct, 'This is an explicit outstanding numerical assertion in this draft.\nThe five-family pilot does not establish it.',
                     'The complete exact acceptance checks all 737 pairs, using 2090 quartics\nand 1078 resource exclusions. Its 48-corner tests retain both signs of\nthe cubic correction; no subdivision or unresolved cell remains.')
    direct = replace(direct, r'\begin{assertion}[Central finite comparison, pending full acceptance]',
                     r'\begin{proposition}[Central finite comparison]')
    direct = replace(direct, 'reject. This assertion remains pending in the present draft.',
                     'reject. The full binary-gap checks and the separate exact comparison\nreplay cover the complete declared domain.')
    assert direct.count(r'\end{assertion}') == 2
    direct = direct.replace(r'\end{assertion}', r'\end{proposition}')
    direct = replace(direct, r'\paragraph{Conditional assembly of the replacement.}',
                     r'\paragraph{Assembly of the comparison.}')
    direct = replace(direct, 'Once the two pending assertions are accepted, the earlier finite induction\ncan use Assertion',
                     'The earlier finite induction uses Proposition')
    direct = direct.replace('Assertion~', 'Proposition~')
    direct = replace(direct, '[Uniform exclusion, conditional on the pending numerical assertions]', '[Uniform exclusion]')
    direct = replace(direct, 'Assume Proposition~\\ref{dc:central-numerical} has been completed, together\nwith its original acquisition ancestors. The left comparison and central\ntail have already been established. Then no attained positive closed-event ratio maximum',
                     'No attained positive closed-event ratio maximum')
    direct = replace(direct, '[Finite local exclusion, conditional on the pending numerical assertions]', '[Finite local exclusion]')
    direct = replace(direct, 'Assume both Assertions~\\ref{dc:central-numerical} and\n\\ref{dc:earlier-numerical} have been completed with their original\nacquisition ancestors. Then no attained positive ratio maximum',
                     'No attained positive ratio maximum')
    direct = replace(direct, '[Equality exclusion after completion]', '[Equality exclusion]')
    direct = replace(direct, 'Under the same completion assumptions, once $C_j\\le\\CE$ is proved at all\nindices,',
                     'Once $C_j\\le\\CE$ is proved at all indices,')
    a = direct.index(r'\begin{proposition}[Finite local exclusion]')
    b = direct.index(r'\begin{corollary}[Equality exclusion]', a)
    finite4346 = read(review / 'finite4346-proposed.tex').decode()
    finite4346 = '\n'.join(line for line in finite4346.splitlines() if not line.startswith('%')) + '\n'
    finite4346 = replace(finite4346, 'Assume Assertion~\\ref{dc:earlier-numerical} has been completed with\nits original acquisition ancestors. Then no attained positive ratio\nmaximum',
                         'No attained positive ratio maximum')
    finite4346 = finite4346.replace('Assertion~', 'Proposition~')
    direct = direct[:a] + finite4346 + '\n' + direct[b:]
    a = direct.index('The former finite-local statement for $42$ through $48$ follows')
    b = direct.index('Equality at an', a)
    direct = direct[:a] + direct[b:]
    direct = replace(direct, r'\paragraph{The earlier acquisition is retained.}', r'\paragraph{Inputs from acquisition.}')
    direct = replace(direct, 'The new comparison uses these early outputs. The additional confinement\nsteps and the later radius $2.7$ are not premises of the new left argument.\nThe complete initialization and complementary probability exclusions remain\npart of the acquisition theorem.',
                     'These support bounds and the common resource budget are the inputs to\nthe comparison. The acquisition theorem also supplies the complete\ninitialization and complementary probability exclusions.')
    direct = direct.replace('45 original rows', '45 rows').replace('39 original left rows', '39 left rows')
    direct = replace(direct, 'The new numerical obligations are summarized below.',
                     'The numerical inequalities are summarized below.')
    direct = replace(direct, 'Branch&Domain&Status of the new route', 'Branch&Domain&Certificate test')
    direct = replace(direct, 'Complete exact comparison accepted; original acquisition\n remains its premise.', 'Global quartic and 24 moment tests per cell.')
    direct = replace(direct, 'Complete finite binary gaps and exact comparison accepted.', 'Finite binary reserve and 24 moment tests per cell.')
    direct = replace(direct, 'Complete scalar checks\n and four displayed quartics.', 'Scalar bounds and four displayed quartics.')
    direct = replace(direct, 'Complete exact comparison accepted.', 'Global quartic and 48 signed moment tests per cell.')
    direct = replace(direct, 'The uniform-left upper indices follow before confinement from a positive',
                     'The uniform-left upper indices follow from a positive')
    direct = replace(direct, 'Each strip in this table is obtained before confinement.',
                     'Contact proves each coordinate strip in this table before the comparison.')
    direct = re.sub(r'\\(subsection|section)\{',
                    lambda m: '\\' + ('subsubsection' if m[1] == 'subsection' else 'subsection') + '{', direct)
    sources['sections/local.tex'] = prefix + direct
    sources['sections/composition.tex'] = read(review / 'composition-proposed.tex').decode()
    intro = sources['sections/introduction.tex']
    intro = replace(intro, 'Two local comparisons exclude precisely such an extremizer: one covers\nthe finite range $43\\le n\\le46$, and one is uniform for $n\\ge47$.',
                    'Two local comparisons exclude precisely such an extremizer:\nProposition~\\ref{j:local:finite4346} covers $43\\le n\\le46$,\nand Proposition~\\ref{j:local:uniform} is uniform for $n\\ge47$.')
    sources['sections/introduction.tex'] = intro

    finite = sources['sections/finite.tex']
    finite = replace(finite, 'These are the support inputs for the direct comparison;\nno further confinement is required by its hypotheses.',
                     'These are the support inputs for the direct comparison.')
    finite = replace(finite, '\\textbf{Draft dependency:} the complete positive-39 numerical assertion in\nProposition~\\ref{j:local:direct-finite-numerical} must be accepted before\nthis replacement is used. That assertion excludes the hypothesized score.',
                     'Proposition~\\ref{j:local:direct-finite-numerical} supplies the complete\npositive-39 comparison and excludes the hypothesized score.')
    finite = replace(finite, '\n\\textbf{Draft dependency:} this rewritten assertion requires the complete\n291-pair part of Proposition~\\ref{j:local:direct-finite-numerical}.', '')
    sources['sections/finite.tex'] = finite
    cert = sources['sections/certificates.tex']
    cert = replace(cert, '\\textbf{Draft dependency:} the new supplement and its complete acceptance\nrecords must be assembled before this revision is released.',
                   'The supplement is distributed with this revision in\n\\texttt{certificates/direct-comparison}. Its three archives preserve the\ncomplete objects and source inventories for the earlier, left and central\ncomparisons; their README files give exact replay commands. The central\narchive also includes the explicit uniform-tail calculation.')
    sources['sections/certificates.tex'] = cert
    main_text = read(BASE / 'main.tex').decode()
    main_text = replace(main_text, 'binomial counts then measure the effect of its remaining fluctuations.',
                        'binomial counts then measure the effect of its remaining fluctuations.\nA coupled-count quartic majorant and its exact moment bounds replace\nthe successive local noise comparisons.')
    sources['main.tex'] = main_text
    # Formatting only: remove the inherited trailing space without altering TeX tokens.
    sources = {name: '\n'.join(line.rstrip() for line in text.split('\n'))
               for name, text in sources.items()}
    assert not any(re.search(r'\bpending\b|Draft dependency|\bINCOMPLETE\b|begin\{assertion\}', text, re.I)
                   for text in sources.values()), 'unresolved release language'

    OUT.mkdir(exist_ok=False)
    for relative, text in sources.items():
        target = OUT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
    for name, data in archive_data.items():
        target = OUT / 'certificates/direct-comparison' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    assert all(hashlib.sha256((PROJECT / p).read_bytes()).hexdigest() == h for p, h in PINS.items())
    receipt = {'status': 'PREPARED_COMPLETE_REPLACEMENT_RELEASE_CANDIDATE',
               'meaning': 'Completed new arithmetic joined to reviewed analytic sources; not a new replay of unchanged acquisition ancestors.',
               'inputs': PINS, 'output': str(OUT.relative_to(PROJECT)),
               'files': {str(p.relative_to(OUT)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in sorted(OUT.rglob('*')) if p.is_file()}}
    (OUT / 'PREPARATION.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'status': receipt['status'], 'files': len(receipt['files'])}))


if __name__ == '__main__':
    main()

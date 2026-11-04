"""Exercise the executor with disposable tiny commands, never proof campaigns."""
from pathlib import Path
from copy import deepcopy
import argparse
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
EXECUTOR = HERE/'run_reproduction_index.py'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    with path.open('x') as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write('\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    assert __debug__ and not sys.flags.optimize
    out = args.output.absolute()
    out.mkdir(parents=True, exist_ok=False)
    records = []
    def case(name, configure, *, execute=True, only=None, expected_success=False,
             expected_status=None, existing_log=False):
        directory = out/name
        directory.mkdir()
        workspace = directory/'workspace'
        release = directory/'release'
        workspace.mkdir()
        release.mkdir()
        archive = directory/'unused-count-archive'
        archive.write_bytes(b'unused synthetic input')
        scripts = {
            'prepare.py': "from pathlib import Path\nwith Path('parent.txt').open('x') as f:f.write('fresh parent')\n",
            'join.py': "from pathlib import Path\nimport json\nassert Path('parent.txt').read_text()=='fresh parent'\nwith Path('RESULT.json').open('x') as f:json.dump(dict(ok=True,n=2),f)\n",
            'unused.py': "from pathlib import Path\nPath('UNWANTED').write_text('should not run')\n",
            'fail.py': "from pathlib import Path\nimport json\nPath('FALSE.json').write_text(json.dumps(dict(ok=True)))\nraise SystemExit(7)\n",
            'missing.py': "pass\n",
            'wrong.py': "from pathlib import Path\nimport json\nPath('WRONG.json').write_text(json.dumps(dict(ok=1)))\n",
        }
        for filename, text in scripts.items():
            (workspace/filename).write_text(text)
        def node(identity, script, dependencies=(), outputs=(), required_fields=None):
            return dict(id=identity, argv=['{python}', '-I', '-B', '{workspace}/'+script],
                        cwd='{workspace}', dependencies=list(dependencies),
                        outputs=['{workspace}/'+path for path in outputs],
                        required_fields=required_fields or {})
        nodes = [node('prepare', 'prepare.py', outputs=['parent.txt']),
                 node('join', 'join.py', dependencies=['prepare'], outputs=['RESULT.json'],
                      required_fields=dict(ok=True, n=2)), node('unused', 'unused.py')]
        index = dict(schema='BE_EXTENSION_FRESH_REPRODUCTION_INDEX_V1',
                     placeholders=['python', 'release', 'workspace', 'count_archive'],
                     all_law_theorem_proved_by_index=False, nodes=nodes,
                     sequential_order=['prepare', 'join', 'unused'], component_maps={})
        configure(index, workspace, node)
        index_path = directory/'INDEX.json'
        write(index_path, index)
        log = directory/'logs'
        if existing_log:
            log.mkdir()
        command = [sys.executable, '-I', '-B', str(EXECUTOR), '--index', str(index_path),
                   '--workspace', str(workspace), '--release', str(release),
                   '--python', sys.executable, '--count-archive', str(archive), '--log-root', str(log)]
        if execute:
            command.append('--execute')
        if only:
            for identity in only:
                command += ['--only', identity]
        tick = time.monotonic()
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (directory/'stdout.txt').write_bytes(process.stdout)
        (directory/'stderr.txt').write_bytes(process.stderr)
        assert (process.returncode == 0) is expected_success, (name, process.returncode, process.stderr)
        result = json.loads((log/'RESULT.json').read_text()) if (log/'RESULT.json').exists() else None
        if expected_status:
            assert result and result['status'] == expected_status, (name, result)
        if result:
            assert result['all_law_theorem'] is False
        record = dict(case=name, command=command, returncode=process.returncode,
                      seconds=time.monotonic()-tick, stdout_sha256=sha(directory/'stdout.txt'),
                      stderr_sha256=sha(directory/'stderr.txt'), expected_success=expected_success,
                      result_sha256=sha(log/'RESULT.json') if result else None)
        write(directory/'PROCESS.json', record)
        records.append(record)
        return workspace, result
    noop = lambda *args: None
    workspace, result = case('dry-run-default', noop, execute=False, only=['join'],
                             expected_success=True, expected_status='DRY_RUN_COMMAND_PLAN_ONLY')
    assert result['commands_executed'] == 0 and not (workspace/'parent.txt').exists()
    workspace, result = case('dependency-closure-success', noop, only=['join'],
                             expected_success=True, expected_status='SELECTED_COMMAND_EXECUTIONS_COMPLETE')
    assert result['selected_commands'] == result['commands_executed'] == 2
    assert not (workspace/'UNWANTED').exists()
    def single(index, row):
        index['nodes'] = [row]
        index['sequential_order'] = [row['id']]
    def failed(index, workspace, node):
        single(index, node('failure', 'fail.py', outputs=['FALSE.json'], required_fields=dict(ok=True)))
    workspace, result = case('nonzero-exit-despite-plausible-output', failed,
                             expected_status='COMMAND_SEQUENCE_FAILED')
    assert result['records'][0]['returncode'] == 7 and (workspace/'FALSE.json').is_file()
    def missing(index, workspace, node):
        single(index, node('missing', 'missing.py', outputs=['MISSING.json']))
    case('zero-exit-missing-output', missing, expected_status='COMMAND_SEQUENCE_FAILED')
    def wrong(index, workspace, node):
        single(index, node('wrong', 'wrong.py', outputs=['WRONG.json'], required_fields=dict(ok=True)))
    case('strict-boolean-required-field', wrong, expected_status='COMMAND_SEQUENCE_FAILED')
    def unknown(index, workspace, node):
        index['nodes'][0]['dependencies'] = ['unknown-parent']
    case('unknown-dependency', unknown)
    def cycle(index, workspace, node):
        index['nodes'][0]['dependencies'] = ['join']
    case('cycle', cycle)
    def duplicate(index, workspace, node):
        index['nodes'].append(deepcopy(index['nodes'][0]))
    case('duplicate-id', duplicate)
    def placeholder(index, workspace, node):
        index['nodes'][0]['argv'][-1] = '{unknown}/prepare.py'
    case('unknown-placeholder', placeholder)
    case('unknown-only', noop, only=['unknown-request'])
    case('existing-log-root', noop, existing_log=True)
    def existing_output(index, workspace, node):
        single(index, node('prepare', 'prepare.py', outputs=['parent.txt']))
        (workspace/'parent.txt').write_text('old output must not cause a skip')
    _, result = case('existing-output-is-not-skipped', existing_output,
                     expected_status='COMMAND_SEQUENCE_FAILED')
    assert result['records'][0]['command_executed'] is True and result['records'][0]['returncode'] != 0
    summary = dict(status='PASS_TINY_REPRODUCTION_EXECUTOR_CONTROLS', cases=records,
                   executor_sha256=sha(EXECUTOR), test_sha256=sha(__file__),
                   actual_cases=len(records), real_certificate_campaign_executed=False,
                   all_law_theorem=False)
    write(out/'RESULT.json', summary)
    print(json.dumps(dict(status=summary['status'], cases=len(records), real_certificate_campaign_executed=False)), flush=True)


if __name__ == '__main__':
    main()

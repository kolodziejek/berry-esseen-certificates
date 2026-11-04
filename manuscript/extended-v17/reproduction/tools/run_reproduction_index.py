"""Plan, or explicitly execute, a sequential reproduction command closure.

Dry-run is the default. --execute runs every selected command; existing outputs
never cause a command to be skipped. Native drivers retain their own freshness
and mathematical checks. This supervisor reports command execution, not a
mathematical theorem or acceptance inferred from a success word.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import os
import re
import signal
import subprocess
import sys
import time

PLACEHOLDERS = {'python', 'workspace', 'release', 'count_archive'}
IDENTIFIER = re.compile(r'[A-Za-z0-9][A-Za-z0-9_.-]*\Z')
TOKEN = re.compile(r'\{([^{}]+)\}')
PYTHON_FLAGS = {'-I', '-B', '-S', '-E', '-s', '-u'}


def need(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'Duplicate JSON key: '+key)
        result[key] = value
    return result


def read(path):
    path = Path(path)
    need(path.is_file() and path.stat().st_size <= 64*1024**2, 'Bounded JSON file: '+str(path))
    def nonfinite(value):
        raise ValueError('Nonfinite JSON number: '+value)
    return json.loads(path.read_text(), object_pairs_hook=unique, parse_constant=nonfinite)


def write(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write('\n')


def same(left, right):
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(same(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(same(x, y) for x, y in zip(left, right))
    return left == right


def expand(value, substitutions):
    need(type(value) is str and '\0' not in value, 'Ordinary command/path string')
    for name in TOKEN.findall(value):
        need(name in PLACEHOLDERS, 'Unknown placeholder: '+name)
    remainder = TOKEN.sub('', value)
    need('{' not in remainder and '}' not in remainder, 'Malformed placeholder')
    return TOKEN.sub(lambda match: substitutions[match.group(1)], value)


def validate(index, substitutions, only):
    need(type(index) is dict and index.get('schema') == 'BE_EXTENSION_FRESH_REPRODUCTION_INDEX_V1',
         'Supported complete reproduction index schema')
    need(index.get('all_law_theorem_proved_by_index') is False, 'Index must disclaim theorem acceptance')
    declared = index.get('placeholders')
    need(type(declared) is list and len(declared) == 4 and set(declared) == PLACEHOLDERS,
         'Exactly four declared placeholders')
    rows = index.get('nodes')
    need(type(rows) is list and 0 < len(rows) <= 10000, 'Nonempty bounded command graph')
    nodes = {}
    for row in rows:
        need(type(row) is dict, 'Explicit command node')
        identity = row.get('id')
        need(type(identity) is str and IDENTIFIER.fullmatch(identity) and identity not in nodes,
             'Unique ordinary command ID: '+str(identity))
        argv = row.get('argv')
        need(type(argv) is list and argv and argv[0] == '{python}', 'Explicit selected Python argv list')
        command = [expand(item, substitutions) for item in argv]
        need(not any(item in ('-O', '-OO') for item in command[1:]), 'Optimized Python forbidden')
        cwd = expand(row.get('cwd'), substitutions)
        need(Path(cwd).is_absolute(), 'Absolute expanded working directory')
        outputs = row.get('outputs', [])
        need(type(outputs) is list, 'Explicit output list')
        outputs = [expand(item, substitutions) for item in outputs]
        need(all(Path(item).is_absolute() for item in outputs) and len(set(outputs)) == len(outputs),
             'Unique absolute expanded output paths')
        dependencies = row.get('dependencies', [])
        scheduling = row.get('scheduling_only_dependencies', [])
        for values in (dependencies, scheduling):
            need(type(values) is list and all(type(x) is str for x in values)
                 and len(set(values)) == len(values), 'Unique literal dependency IDs')
        fields = row.get('required_fields', {})
        need(type(fields) is dict and (not fields or len(outputs) == 1),
             'Required fields address exactly one JSON output')
        timeout = row.get('timeout_seconds')
        need(timeout is None or (type(timeout) in (int, float) and math.isfinite(timeout) and timeout > 0),
             'Optional positive finite timeout')
        nodes[identity] = dict(row, argv=command, cwd=cwd, outputs=outputs,
                               dependencies=dependencies, scheduling_only_dependencies=scheduling,
                               required_fields=fields)
    for node in nodes.values():
        need(set(node['dependencies']+node['scheduling_only_dependencies']) <= nodes.keys(),
             'Unknown dependency for '+node['id'])
    active, done, derived = set(), set(), []
    def visit(identity):
        need(identity not in active, 'Cyclic command dependency: '+identity)
        if identity in done:
            return
        active.add(identity)
        for dependency in nodes[identity]['dependencies']+nodes[identity]['scheduling_only_dependencies']:
            visit(dependency)
        active.remove(identity)
        done.add(identity)
        derived.append(identity)
    for identity in nodes:
        visit(identity)
    order = index.get('sequential_order', derived)
    need(type(order) is list and len(order) == len(nodes) and len(set(order)) == len(order)
         and set(order) == nodes.keys(), 'Complete unique sequential order')
    positions = {identity: position for position, identity in enumerate(order)}
    for identity, node in nodes.items():
        need(all(positions[d] < positions[identity] for d in
                 node['dependencies']+node['scheduling_only_dependencies']),
             'Sequential order violates dependency: '+identity)
    requested = list(nodes) if only is None else only
    need(requested and all(identity in nodes for identity in requested), 'Unknown or empty --only selection')
    selected = set()
    def include(identity):
        if identity in selected:
            return
        selected.add(identity)
        for dependency in nodes[identity]['dependencies']:
            include(dependency)
    for identity in requested:
        include(identity)
    return [nodes[identity] for identity in order if identity in selected]


def command_source(node):
    args = node['argv'][1:]
    position = 0
    while position < len(args) and args[position] in PYTHON_FLAGS:
        position += 1
    need(position < len(args), 'Python command has a source')
    if args[position] == '-c':
        need(position+1 < len(args), 'Complete inline Python command')
        return dict(kind='inline_python', sha256=hashlib.sha256(args[position+1].encode()).hexdigest())
    if args[position] == '--':
        position += 1
        need(position < len(args), 'Python source follows --')
    need(not args[position].startswith('-'), 'Index requires explicit Python source, not an unpinned module')
    source = Path(args[position])
    if not source.is_absolute():
        source = Path(node['cwd'])/source
    need(source.is_file() and not source.is_symlink(), 'Existing ordinary command source: '+str(source))
    return dict(kind='source_file', path=str(source), sha256=sha(source))


def outputs_after(node):
    observations = []
    for name in node['outputs']:
        path = Path(name)
        need(path.exists() and not path.is_symlink(), 'Missing or linked declared output: '+name)
        if path.is_file():
            observations.append(dict(path=name, kind='file', bytes=path.stat().st_size, sha256=sha(path)))
        else:
            need(path.is_dir(), 'Declared output is an ordinary file or directory')
            observations.append(dict(path=name, kind='directory', recursive_hash_claimed=False))
    if node['required_fields']:
        result = read(node['outputs'][0])
        need(type(result) is dict, 'Required fields belong to a JSON object')
        for key, expected in node['required_fields'].items():
            need(key in result and same(result[key], expected), 'Missing or false required output field: '+key)
    return observations


def execute_node(node, directory, immutable):
    directory.mkdir()
    command = dict(id=node['id'], argv=node['argv'], cwd=node['cwd'],
                   dependencies=node['dependencies'], outputs=node['outputs'],
                   required_fields=node['required_fields'],
                   existing_outputs_before_execution=[p for p in node['outputs'] if Path(p).exists()],
                   all_law_theorem=False)
    write(directory/'COMMAND.json', command)
    tick = time.monotonic()
    result = dict(id=node['id'], returncode=None, error=None, command_executed=False,
                  all_law_theorem=False, numerical_acceptance_inferred_from_exit_code=False)
    try:
        need(Path(node['cwd']).is_dir(), 'Working directory exists after prerequisites')
        need(all(sha(path) == pin for path, pin in immutable.items()), 'Immutable supervisor/index/runtime inputs')
        source = command_source(node)
        if node.get('script_sha256'):
            need(source['sha256'] == node['script_sha256'], 'Declared command source hash')
        result['source_before'] = source
        write(directory/'SOURCE_BEFORE.json', source)
        with (directory/'stdout.txt').open('xb') as stdout, (directory/'stderr.txt').open('xb') as stderr:
            process = subprocess.Popen(node['argv'], cwd=node['cwd'], stdout=stdout, stderr=stderr,
                                       stdin=subprocess.DEVNULL, start_new_session=True)
            result['command_executed'] = True
            try:
                result['returncode'] = process.wait(timeout=node.get('timeout_seconds'))
            except BaseException:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                result['returncode'] = process.wait()
                raise
        result['source_after'] = command_source(node)
        need(same(result['source_after'], source), 'Command source unchanged during execution')
        need(all(sha(path) == pin for path, pin in immutable.items()), 'Immutable inputs unchanged after execution')
        need(result['returncode'] == 0, 'Command returned nonzero')
        result['observed_outputs'] = outputs_after(node)
        result['status'] = 'COMMAND_EXECUTION_AND_DECLARED_OUTPUT_CHECKS_COMPLETE'
    except BaseException as exc:
        result['status'] = 'COMMAND_EXECUTION_FAILED'
        result['error'] = type(exc).__name__+': '+str(exc)
    result['elapsed_seconds'] = time.monotonic()-tick
    for stream in ('stdout', 'stderr'):
        path = directory/(stream+'.txt')
        result[stream+'_sha256'] = sha(path) if path.is_file() else None
    write(directory/'PROCESS.json', result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    for name in ('index', 'workspace', 'release', 'python', 'count-archive', 'log-root'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--only', action='append', help='Requested ID; repeat for multiple dependency closures')
    args = parser.parse_args()
    need(__debug__ and not sys.flags.optimize and 'PYTHONOPTIMIZE' not in os.environ,
         'Unoptimized supervisor with no PYTHONOPTIMIZE')
    index_path = args.index.absolute()
    workspace, release = args.workspace.resolve(), args.release.resolve()
    python = args.python.absolute()  # Preserve a chosen virtual-environment executable path.
    count_archive = args.count_archive.absolute()
    log = args.log_root.absolute()
    need(workspace.is_dir() and release.is_dir() and python.is_file(), 'Existing workspace, release, and interpreter')
    need(not log.exists() and not log.is_symlink(), 'Create-only log root; no resumed/skipped commands')
    substitutions = dict(workspace=str(workspace), release=str(release),
                         python=str(python), count_archive=str(count_archive))
    index = read(index_path)
    plan = validate(index, substitutions, args.only)
    immutable = {index_path: sha(index_path), Path(__file__).absolute(): sha(__file__), python: sha(python)}
    for component in index.get('component_maps', {}).values():
        name = component['path']
        need(type(name) is str and not Path(name).is_absolute() and '..' not in Path(name).parts,
             'Contained component map path')
        path = workspace/name
        need(sha(path) == component['sha256'], 'Pinned component map: '+name)
        immutable[path] = component['sha256']
    log.mkdir(parents=True, exist_ok=False)
    request = dict(schema='BE_REPRODUCTION_COMMAND_REQUEST_V1', execute=args.execute,
                   index=str(index_path), index_sha256=sha(index_path), substitutions=substitutions,
                   requested_ids=args.only, selected_order=[node['id'] for node in plan], nodes=plan,
                   conductor_python=sys.version, conductor_executable=sys.executable,
                   selected_python_sha256=sha(python),
                   immutable_inputs_sha256={str(path): pin for path, pin in immutable.items()},
                   all_law_theorem=False, outputs_are_not_acceptance_without_native_readers=True)
    write(log/'REQUEST.json', request)
    if not args.execute:
        result = dict(status='DRY_RUN_COMMAND_PLAN_ONLY', selected_commands=len(plan), commands_executed=0,
                      all_law_theorem=False, request_sha256=sha(log/'REQUEST.json'))
        write(log/'RESULT.json', result)
        print(json.dumps(result), flush=True)
        return 0
    records = []
    for number, node in enumerate(plan, 1):
        print(json.dumps(dict(starting=node['id'], position=number, selected_commands=len(plan))), flush=True)
        result = execute_node(node, log/(f'{number:03d}-'+node['id']), immutable)
        records.append(result)
        if result['status'] != 'COMMAND_EXECUTION_AND_DECLARED_OUTPUT_CHECKS_COMPLETE':
            break
    complete = len(records) == len(plan) and all(r['status'] == 'COMMAND_EXECUTION_AND_DECLARED_OUTPUT_CHECKS_COMPLETE' for r in records)
    result = dict(status='SELECTED_COMMAND_EXECUTIONS_COMPLETE' if complete else 'COMMAND_SEQUENCE_FAILED',
                  selected_commands=len(plan), commands_executed=sum(r['command_executed'] for r in records),
                  records=records, all_law_theorem=False,
                  numerical_acceptance_inferred_from_exit_code=False,
                  request_sha256=sha(log/'REQUEST.json'))
    write(log/'RESULT.json', result)
    print(json.dumps(dict(status=result['status'], commands_executed=result['commands_executed'],
                          all_law_theorem=False)), flush=True)
    return 0 if complete else 1


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(type(exc).__name__+': '+str(exc), file=sys.stderr)
        raise SystemExit(2)

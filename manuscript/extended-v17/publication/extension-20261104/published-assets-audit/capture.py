from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[3]
CHECK = HERE / 'check.py'
SOURCE = BASE / 'work/manuscript_revision_20261029/manuscript/extended-v17/reproduction/SOURCE_ASSETS_V3.json'
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(name, value):
    with (HERE / name).open('x') as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write('\n')


assert __debug__ and not sys.flags.optimize and sys.dont_write_bytecode
command = [sys.executable, '-I', '-B', str(CHECK)]
pins = {str(path): sha(path) for path in (Path(__file__), CHECK, SOURCE, Path(sys.executable))}
write('STARTED.json', dict(command=command, cwd=str(BASE), python=sys.version, input_sha256=pins))
tick = time.monotonic()
with (HERE / 'stdout.txt').open('xb') as stdout, (HERE / 'stderr.txt').open('xb') as stderr:
    process = subprocess.run(command, cwd=BASE, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr)
unchanged = pins == {name: sha(name) for name in pins}
write('PROCESS.json', dict(command=command, actual_returncode=process.returncode,
    seconds=time.monotonic() - tick, input_sha256=pins, inputs_unchanged=unchanged,
    stdout_sha256=sha(HERE / 'stdout.txt'), stderr_sha256=sha(HERE / 'stderr.txt')))
assert process.returncode == 0 and unchanged and not (HERE / 'stderr.txt').read_bytes()
print((HERE / 'stdout.txt').read_text(), end='', flush=True)

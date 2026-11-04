#!/usr/bin/env python3
"""Create-only process capture for the bounded demonstration."""
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, obj):
    with Path(path).open("x") as out:
        json.dump(obj, out, indent=2, sort_keys=True)
        out.write("\n")


def main():
    if not __debug__ or sys.flags.optimize or len(sys.argv) != 2:
        raise ValueError("unoptimized Python and one existing fresh run root required")
    root = Path(sys.argv[1]).resolve(strict=True)
    source = Path(__file__).resolve().parent
    files = [source / name for name in (
        "check_polynomial_objects.py", "proof_objects.json", "negative_controls.py",
        "capture_prototype.py", "README.md")]
    before = {str(path): {"sha256": sha(path), "bytes": path.stat().st_size} for path in files}
    executable = Path(sys.executable).resolve(strict=True)
    runtime = {"executable": str(executable), "sha256": sha(executable),
               "version": sys.version, "platform": platform.platform(),
               "optimized": sys.flags.optimize, "pid": os.getpid()}
    write(root / "INPUTS.json", {"files": before, "runtime": runtime,
                                 "current_manuscript_ancestor": False})
    commands = [
        ("acceptance", [str(executable), "-I", "-B", str(files[0]), str(files[1])]),
        ("controls", [str(executable), "-I", "-B", str(files[2]), str(files[1]),
                      str(root / "mutations")])]
    results = []
    for name, command in commands:
        capture = root / name
        capture.mkdir()
        started = time.time()
        write(capture / "STARTED.json", {"argv": command, "cwd": str(source),
                                        "started_unix": started, "source_pins": before})
        with (capture / "stdout.txt").open("xb") as out, (capture / "stderr.txt").open("xb") as err:
            completed = subprocess.run(command, cwd=source, stdout=out, stderr=err, timeout=30,
                                       check=False)
        observation = {"argv": command, "returncode": completed.returncode,
                       "elapsed_seconds": time.time() - started,
                       "stdout_sha256": sha(capture / "stdout.txt"),
                       "stderr_sha256": sha(capture / "stderr.txt")}
        write(capture / "PROCESS.json", observation)
        if completed.returncode:
            raise ValueError("child failed: " + name)
        result = json.loads((capture / "stdout.txt").read_text())
        write(capture / "RESULT.json", result)
        results.append({"name": name, "status": result["status"],
                        "returncode": completed.returncode, "capture": str(capture)})
    after = {str(path): {"sha256": sha(path), "bytes": path.stat().st_size} for path in files}
    if after != before:
        raise ValueError("source changed during demonstration")
    result = {"status": "PASS_BOUNDED_DEMONSTRATION", "commands": results,
              "all_source_hashes_unchanged": True, "current_manuscript_ancestor": False,
              "native_integrations": 0}
    write(root / "RESULT.json", result)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

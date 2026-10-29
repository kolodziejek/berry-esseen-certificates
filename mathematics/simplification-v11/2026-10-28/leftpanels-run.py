"""Capture a distinct bounded left-panel acceptance run."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

if not __debug__ or sys.flags.optimize:
    raise RuntimeError("Assertions must remain enabled")
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
run = ROOT / "runs/leftpanels-v11-20261028" / sys.argv[1]
run.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
script = HERE / "leftpanels-check.py"
command = [sys.executable, "-I", "-B", str(script)]
start = time.monotonic()
result = subprocess.run(command, cwd=ROOT, capture_output=True)
(run / "stdout.json").write_bytes(result.stdout)
(run / "stderr.txt").write_bytes(result.stderr)
receipt = {"command": command, "returncode": result.returncode,
           "elapsed_seconds": time.monotonic()-start, "python": sys.version,
           "script_sha256": sha(script), "driver_sha256": sha(Path(__file__)),
           "proof_sha256": sha(HERE / "leftpanels.tex"),
           "stdout_sha256": sha(run / "stdout.json"),
           "stderr_sha256": sha(run / "stderr.txt")}
if result.returncode == 0:
    receipt["status"] = json.loads(result.stdout)["status"]
(run / "receipt.json").write_text(json.dumps(receipt, indent=2)+"\n")
print(json.dumps(receipt, indent=2))
raise SystemExit(result.returncode)

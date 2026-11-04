# Reproducing the extension's numerical checks

This package separates three things: mathematical arguments in the manuscript,
untrusted numerical inputs and checking programs, and records of executions.
Restoring a source archive establishes byte identity. Running a complete native
checker establishes its stated finite inequality. Applying that inequality to
every relevant probability law also requires the manuscript's continuous
reductions and the complete interface checks. None of these obligations is
replaced by a printed `PASS` or an archive hash.

**Completed selected verification, 4 November 2026:** all numerical families
required by the extension and their complete interface readers have passed.
The manuscript supplies the continuous mathematical arguments and induction;
see its proof dependency map. The separate 114-command fresh campaign below
has not itself been executed again as a single relocated run.
Source restoration, command normalization, and the supervisor's rejection
behavior have been checked separately. The evidence ledger identifies actual
completed executions, their exact scopes, and preserved failed attempts.

## What is included

| Input | Purpose | Compressed bytes |
|---|---|---:|
| `assets/framework-static03/static-sources.tar.gz` | 4,700 inventoried framework, mathematical source, adapter, and explicitly labelled retained-audit files | 64,020,798 |
| `assets/foundations-static-cache-v2.tar.gz` | Original static inputs for the foundation families | 23,938,916 |
| `assets/n5-static-cache02/static-sources.tar.gz` | 16,619 five-summand parent inputs and 110 separately activated join inputs | 22,411,375 |
| `assets/finite-static-cache02/static-sources.tar.gz` | Original static inputs for the later finite families | 53,466,481 |
| External `count-candidates.zip` | 1,243 untrusted public COUNT forests and their original manifest | 94,179,896 |

The exact archive and internal-manifest hashes are in
`SOURCE_ASSETS_V3.json`. The framework's file-by-file inventory is
`FRAMEWORK_FILE_MANIFEST_V3.json`. The public COUNT ZIP is supplied separately;
its pinned source and installation instructions are in `COUNT_CANDIDATES.md`.
The installer does not download anything. Allow space for at least the
1,249,228,509 uncompressed COUNT input bytes, the other restored inputs, and
the substantially larger execution records. A total disk-space or runtime
bound is not asserted here.

The framework includes some explicitly labelled earlier compact-manuscript
audit records. Static caches can also contain historical objects used as
inputs by the original programs. Their presence does not make them fresh
execution evidence. Fresh parent calculations and complete interface readers
must justify every use of such an object.

## Runtime and workspace

The currently reviewed process transport is for **macOS**. Use one unoptimized
CPython 3.12 executable consistently for each producer and reader. Select its
physical file path, not a symlink: an original 10--14 source reader rejects a
symlinked executable. The physical interpreter's environment must contain
NumPy. Keep that executable unchanged during the campaign. Do not set `PYTHONOPTIMIZE`, and do
not pass `-O` or `-OO`: assertions include proof obligations. Candidate planning
uses NumPy; acceptance uses exact arithmetic after planning. The three-summand
checker additionally needs a C++17 compiler available as `g++` on `PATH` and
Boost.Multiprecision headers. Set `CPLUS_INCLUDE_PATH` to an include directory
containing `boost/` if the compiler does not already find those headers. Its
acceptance kernel uses `cpp_int`, not a floating-point approximation.

The process observers require access to `/bin/ps` and `/usr/bin/vm_stat`;
ROOT4 and the isolated compact replay also use macOS `sandbox-exec`.
An environment that denies those observations cannot complete the current
transport checks. The five-summand V3 policy allows 256 MiB for its supervisor
and retains the original 512 MiB child allowance. These are sampled resource
observations, not a claim of a kernel-enforced aggregate memory bound.
Numerical portability does not automatically imply portability of these
process observations; Linux needs a separately reviewed transport adaptation.

Use physical absolute paths without symbolic-link ancestors. On macOS use
`/private/tmp`, for example, rather than its `/tmp` alias. Select a new
workspace; never overlay this campaign on the working research tree or a
previous campaign. Output paths are fixed inside that fresh workspace, and
many original programs deliberately refuse existing outputs.

## Restore the framework first

Set the four task-specific variables below to actual absolute paths. The
release directory contains this document, `assets/`, and `tools/`. The
workspace path should not yet exist. The COUNT path names the complete pinned
ZIP, not an extracted directory.

```bash
BE_PY=/absolute/path/to/python3.12
BE_RELEASE=/absolute/path/to/release
BE_WORK=/absolute/physical/path/to/new-workspace
BE_COUNT=/absolute/physical/path/to/count-candidates.zip

env -u PYTHONOPTIMIZE "$BE_PY" -I -B - <<'PY'
from pathlib import Path
import platform, sys
import numpy
assert __debug__ and not sys.flags.optimize
assert sys.version_info[:2] == (3, 12)
assert platform.system() == 'Darwin'
assert Path(sys.executable) == Path(sys.executable).resolve(), 'Use the physical executable path'
print(sys.executable, sys.version)
print('NumPy', numpy.__version__)
PY

env -u PYTHONOPTIMIZE "$BE_PY" -I -B \
  "$BE_RELEASE/tools/source_cache_pack.py" restore \
  --archive "$BE_RELEASE/assets/framework-static03/static-sources.tar.gz" \
  --sha256 3efd04860100dd010de930a11f947d5cceac4414201cb12884db4af42871ed23 \
  --manifest-sha256 a7ac83d8f1de03738f1d8350a11f7c1cf7c76fc66fb740a514da5312211e7929 \
  --workspace "$BE_WORK"
```

The restorer validates the complete archive, manifest, namespace, file sizes,
and file bytes before accepting them. It refuses differing existing files.
Restore the framework before the static caches: later caches add files inside
the framework's working trees, so replaying the strict framework restoration
after that point is not an appropriate integrity check.

The command index restores the three remaining caches and installs the COUNT
inputs in the required order. In particular, its finite restorer archives the
old scalar outputs separately, and its scalar preparer copies only the three
source files to the canonical calculation directory. The unchanged scalar
checker then constructs fresh outputs. Do not replace that route with a
generic restoration of the old scalar directory.

## Inspect the plan, then execute it

This command creates a plan and executes **zero** numerical commands:

```bash
env -u PYTHONOPTIMIZE "$BE_PY" -I -B \
  "$BE_RELEASE/tools/run_reproduction_index.py" \
  --index "$BE_RELEASE/REPRODUCTION_INDEX_V1.json" \
  --workspace "$BE_WORK" --release "$BE_RELEASE" \
  --python "$BE_PY" --count-archive "$BE_COUNT" \
  --log-root "$BE_WORK/reproduction-plan01"
```

Inspect `reproduction-plan01/REQUEST.json`. Its 114 nodes specify the resolved
argument lists, working directories, outputs, and execution dependencies.
The component maps remain separately hash-pinned. Some nodes are large native
campaigns, so 114 is a command count, not a bound on arithmetic work. The
supervisor runs these nodes sequentially; individual native campaigns use
their explicitly configured worker counts.

To execute the complete plan, use a different, absent log directory and add
`--execute`:

```bash
env -u PYTHONOPTIMIZE "$BE_PY" -I -B \
  "$BE_RELEASE/tools/run_reproduction_index.py" \
  --index "$BE_RELEASE/REPRODUCTION_INDEX_V1.json" \
  --workspace "$BE_WORK" --release "$BE_RELEASE" \
  --python "$BE_PY" --count-archive "$BE_COUNT" \
  --log-root "$BE_WORK/reproduction-execution01" --execute
```

Every command receives its own log directory, actual return code, complete
top-level stdout and stderr, and source identity before and after execution.
The supervisor stops at the first command failure. It also checks declared
outputs and the component maps' specified typed result fields. Those checks
are in addition to the native checkers; they do not independently establish
their mathematical soundness.

Existing outputs never cause a command to be silently skipped. Preserve a
failed campaign. Restarting requires a new workspace or an explicitly reviewed
recovery adapter that records exactly which old observations are reused.
Do not manufacture a missing exit code, merge incompatible runtime identities,
rewrite an old receipt, or discard a failed observation.

For a limited check, repeat `--only NODE_ID` as needed. The supervisor includes
the selected nodes' **execution dependencies**. This is not necessarily the
entire mathematical dependency chain: the manuscript and component maps state
the hypotheses needed to apply the resulting inequalities. A partial selection
does not certify the all-law theorem. Scheduling-only edges are not added to
an `--only` closure.

## Reading results and auditing the argument

Keep the complete native result trees as well as the top-level supervisor
logs. Several acceptance readers reconstruct full interval covers, signed
arrangements, or proof trees from those files. A summary JSON alone is not
sufficient. Some nested successful compiler and kernel streams in the original
three-summand driver are not separately saved; its actual execution trace and
the exact kernel identities are retained. No hermetic compiler or operating
system verification is claimed.

The numerical modules remain conditional on their explicit inputs. A final
paper can discharge those conditions through an ordinary mathematical
induction, provided the continuous lemmas, predecessor statements, and
same-law interfaces have all been established. The proof dependency map is
the place to audit that implication. Neither the supervisor's final exit
status nor the source package asserts it automatically.

The source restorer, COUNT installer, command supervisor, and native acceptance
programs have separate negative controls. These exercise malformed inputs,
missing and duplicated objects, changed domains and coefficients, inconsistent
runtime records, nonzero processes, missing outputs, and incomplete covers.
They complement the source and mathematical review; they are not a formal
verification of the implementation.

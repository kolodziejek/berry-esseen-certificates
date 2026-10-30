# Independent audit of the follow-up feedback

Review date: 29 October 2026. Source: the user-attached follow-up text and the
working manuscript based on `cd10654222f4b63d50f9d8f108597b140d263ec5`.
The linked ChatGPT Library report was not available in this audit; the findings
below concern the actual text supplied and the local source files. This bounded
review does not repeat the earlier mathematical audit or certify publication.

| Finding | Mathematical status | Execution status |
|---|---|---|
| Blanket downward-denominator rule is false for signed numerators | Refuted as a general explanatory rule; four-corner interval rule derived below | Exact negative example and 605 rational interior diagnostics passed |
| Missing notation, coordinate qualifier and third-moment assumption | Source defects confirmed; proposed repairs preserve theorems | Read-only inspection |
| First rho interval is reconstructed, not stored | Confirmed directly from acceptor and JSON format | Exact index-zero reconstruction passed |
| Entry replay CLI requires `--output-dir` | Confirmed from `argparse` declaration | Fresh `--help` returned 0 |
| Full replay and fresh manuscript build | Outside this audit | Not run here |
| Revised immutable source release | Needed to make new files independently accessible | Publication delegated to coordinator |

## 1. Signed quotient correction

The sentence in `appendices/reproducibility.tex` saying that a positive
denominator is rounded downward to form an upper quotient is too broad.
For numerator -1 and denominator in [1,2], that rule gives -1 instead
of the true upper value -1/2. This is a defect in the explanation, not
by itself evidence of a corresponding error in an acceptance program.
This audit did not inspect every inherited division.

A safe replacement is:

> Square-root endpoints are checked by rational square comparisons. Before
> division, the entire denominator interval must be proved positive. For a
> nonnegative numerator, a smaller positive denominator gives an upper
> quotient. For a signed numerator interval, take the minimum and maximum of
> the four endpoint ratios, with outward rounding.

More precisely, for `a in [a_l,a_u]` and `b in [b_l,b_u]` with `b_l>0`,
`a/b` lies between the minimum and maximum of
`a_l/b_l, a_l/b_u, a_u/b_l, a_u/b_u`. For fixed b the quotient is increasing
in a, so only the two numerator endpoints matter. At either fixed numerator
endpoint, the quotient is monotone in b (or constant when the numerator is
zero), so only denominator endpoints matter. This proves coverage of the
entire rectangle; the rational diagnostics are supplementary.

## 2. Precise notation and assumption repairs

### Main-text square completion

In `sections/04-fixed-entry.tex`, define `c_-`, `c_+`, and `phi_l` before
“For example”. They are rational constants satisfying
`0<c_-<C_E<c_+` and `0<phi_l<phi(0)`. The selected values, already proved
and used in Appendix D, are

- `c_-=0.4097321837023`, `c_+=0.4097321837025`;
- `phi_l=997/2500`.

It suffices to give their roles there and point to the explicit constants and
Lemma B.2, or to display the values. They are coefficient bounds, not bounds
on a law's normalized score. The floor N=42 is already introduced immediately
before the example. No change to the square-completion formulas is needed.

### Count coordinates

The opening of `sections/08-direct-comparison.tex` should say “in count
coordinates” before asserting that the sum is an integer count plus centered
noise. For the theorem's normalization the exact identity is

`sum X_i = (K + sum U_i - np)/sqrt(v+s)`, where `K=sum B_i`.

The standardized raw sum itself is not literally an integer plus centered
noise. Adding the qualifier repairs the prose without changing any formula
or hypothesis downstream.

### Fourier third moment

At the start of `appendices/fixed-fourier.tex`, assume `E|X|^3<infinity`
before defining `gamma=E X^3` and the cubic Gaussian compensator. This is a
per-law finiteness hypothesis for the varying laws X_n; it introduces no
uniform third-moment bound. Keep the separate inversion lemma exactly at its
weaker hypotheses: zero mass and first moment, finite absolute second moment.
Its compensated Fubini argument does not require a third moment.

### Certificate table

The JSON first row stores exactly the keys `index`, `radius`, `raw`, `defect`,
`active`, and `excluded`; it does not store rho endpoints. In
`accept_entry.py`, `verify` reconstructs cell i as

`[1+3361*i/96000, 1+3361*(i+1)/96000]`.

At i=0 this is `[1,99361/96000]`. Change the table header “Stored value” to
“Checkpoint value” and label the interval “Moment interval (reconstructed
from index 0)”, or place the reconstructed interval outside the stored-field
table. The existing support/radius/ceiling/count values match the JSON.

The optional Q rename is a readability improvement only. If chosen, rename
the probability-defect polynomial consistently in geometry and acquisition,
while retaining the contact majorant. This audit does not regard the original
argument-variable distinction as a mathematical ambiguity.

## 3. Literal commands and an additional README defect

The supplied feedback's `--output-dir` example is correct. The actual entry
wrapper declares it as a required argparse option. In contrast, the current
README's bare positional output path is invalid and must also be corrected.
Use literal verbatim/code formatting with ordinary ASCII hyphens and shell
continuations; do not use `\newline` to split a command in running TeX text.

From the repository root, valid commands are:

```sh
python3 -I -B \
  mathematics/fixed-target-v8/2026-10-28/isolated_entry_replay.py \
  --output-dir runs/compact-v16-entry-review

python3 -I -B \
  manuscript/compact-v16/tools/recheck.py \
  compact-v16-bounded-review

python3 -I -B \
  manuscript/compact-v16/tools/check_revision_constants.py \
  --output-dir runs/compact-v16-scalar-review
```

Every destination must be new. The entry wrapper and new scalar driver create
parent directories. The historical `recheck.py` takes a positional argument
relative to `manuscript/compact-v16/` and does not create missing parents; the
shown single-directory argument is valid. It does not accept `--output-dir`.
The scalar `--output-dir` is optional but useful because it preserves the
component stdout/stderr and receipt. Python must run without optimization.

Fresh help output and exact diagnostics are preserved under
`runs/manuscript_revision_20261029/followup_audit01/` in the local handoff,
including input hashes, interpreter version, return code and output hashes.
No full entry replay was performed by this audit. After typesetting, extract
the PDF text and verify that each displayed command parses to these literal
arguments; a successful source build alone does not test copyability.

## 4. Source-release boundary

The pinned baseline is a valid immutable reference for the unchanged entry
files, but it cannot identify newly introduced checker files. Publish the
revised source/checker tree and identify its commit separately from the old
certificate baseline. The release should expose actual revision receipts and
explain which sources their hashes bind. Historical `checks-summary.json` and
`validation.json` must remain clearly historical.

A new immutable source snapshot may precede the final commit that merely adds
its citation; that relationship must be explicit. The PR description can link
the final immutable head commit for the exact final PDF and TeX. A mutable PR
link alone should not be described as an immutable source pin.

None of these focused corrections changes the original local theorem domain,
threshold-atom conventions, complete tails, off-contact extension or finite-base
condition. The finite base through699 remains open.

## 5. Check of the implemented follow-up edits

I compared the current sources with the delivered source snapshot under
`root01/delivery-stage/manuscript/compact-v16/` and read the focused changes.
The signed-quotient replacement states the full four-corner bound with
`0<b_-<=b<=b_+` and disallows using it across zero. The certificate paragraph
now explicitly reconstructs the interval from the stored index. The three
commands use literal `Verbatim` blocks with ASCII `--output-dir` where
appropriate and explicit shell continuations. The README's entry command
also now supplies the required option.

The opening Fourier assumption now includes `E|X|^3<infinity`. An exact
comparison confirmed that the separate inversion lemma statement is
byte-for-byte unchanged, so its weaker second-moment scope is preserved.
The count-coordinate qualifier is present. The square-completion constants
are introduced before their first use and point to their values/proofs;
I suggested also writing the known positivity of c_- explicitly.

The optional probability polynomial is consistently renamed `mathcal Q`
throughout geometry and acquisition, including its lower approximation.
Undoing precisely that rename and ignoring whitespace makes both entire
files equal to the delivered snapshot. There is no partial rename or
mathematical formula change. The contact majorant Q and ray auxiliary Q_b
are correctly left unchanged.

Mathematical status: focused corrections derived/source-checked; no theorem
scope loss detected. Execution status: exact source comparisons passed;
final compilation, PDF command-copy checks and visual layout remain the
coordinator's next checks. Publication status is not inferred from these edits.

# Shorter proof routes: decisions and evidence

27 October 2026. Start: fork main `ca4943aae7a85ffa85d5d4d7166987dc055cb3e6`.
Original reference: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.

The useful change is to **maximize excess over the target before deriving
contact**. This fixes the coefficient at `c=C_E`. We prove the resulting
attainment, contact and conservation statements, and a conditional theorem
transferring the scalar estimates to this new extremizer. If its explicit
premises are discharged, the new tail argument needs no upper-excess entry
recurrence. It still needs the finite base and a complete local exclusion.

The 14-page [companion note](main.pdf) contains the new analytic arguments.
Its [source](main.tex) and `source-strategy-v4.zip` are editable and portable.
It is not a 14-page proof of the conjecture or a replacement for all the
retained technical arguments in the 158-page manuscript.

## Decisions on the external proposals

| Proposal | Decision and reason | Detailed evidence |
|---|---|---|
| Astra: fixed-target excess | Accept the reformulation and narrowed conditional transport. Distinguish the fixed contact coefficient, the actual score and the deleted-sum constants. The conserved excess is `(n+H^2)a`, with raw `H`. | [Derivation and source-by-source dependency map](excess.md), [proof](excess.tex), [independent review](transport-review.md) |
| Opus: discrete exploration | The ZIP contains a README and three exploratory scripts, not a proof. Rounded sum locations and sampled contact cannot certify continuous-domain inequalities. Unconditional domination by the own-sign Bernoulli skeleton is false. | [Audit, exact counterexamples and finite contact reduction](opus-audit.md) |
| Argon: unification and large cuts | Accept the general first-failure statement and genuinely duplicate proof references. Reject the weaker deletion factor, incorrect quartic parameter and replacement of the fine finite-index Gaussian bound by the coarse one. No new floor 20 or 25 is proved. | [Audit with original source locations](argon-audit.md) |
| Public formalizations | Useful interfaces and parameter reductions, but no inspected source supplies our finite base or uniform LOCAL42. Source inspection was not a Lean build. | [Pinned source comparison](public-sources.md) |

The attached instructions were treated as proposals. A page target, an
assertion of author approval, or a historical PASS was not evidence that a
proof component could be removed.

## Further analytic reductions

The new [geometry proof](geometry.tex) starts with
`gamma^2+(2m)^2 <= rho^2` and `J <= rho+2m`. These hold under a finite third
absolute moment, including unbounded support. Together they give the sharp
family `gamma+tJ <= (t+sqrt(1+t^2))*rho` and its exact equality law.
At `t=3`, the physical defect splits into two nonnegative geometric losses.
The manuscript now uses this shorter proof while retaining the quantitative
endpoint decomposition and simultaneous stability estimates that follow it.

For quantitative bounds, the note keeps the common positive noise measures
`d mu_+ = W^2 1_{X>0} dP` and `d mu_- = W^2 1_{X<0} dP`. The displacement
cost and both weighted noise costs share one defect budget. Combining signed
responses before maximizing their response/cost ratio can improve on bounding
each moment separately. A four-atom example proves a strict analytic gain;
it is not a claimed improvement to a critical certificate cell. The quadratic
remainder in the characteristic-function power is explicitly retained.

Instead of demanding domination by the Bernoulli skeleton, one may spend its
known margin below `C_E`. On the stated central probability interval this
margin factors exactly as a positive constant times `(p-p_*)^2/sqrt(pq)`.
A strictly smaller comparison error would suffice. Proving that uniform,
noise-sensitive comparison error remains the difficult obligation.

For a fixed finite law the continuum contact test reduces to its closed
jumps, zero and at most four quadratic stationary roots. For a Bernoulli
law this is at most `n+5` candidates, replacing a sampled grid. It remains
a necessary condition, and rigorous root/normal enclosures are still needed.
No universal two-point reduction follows from this test.

## What computations could become unnecessary

The full source map is in `excess.md`; its line references are pinned to
the starting revision. The following statements concern the **new route**,
not acceptance of the old wrappers by renaming their variables.

| Potential removal | Why it is valid under the stated conditions | What must remain |
|---|---|---|
| Recurrence used only to obtain the tail-entry score/excess caps | The new extremizer starts with `a>=0`; contact uses fixed `c`. The raw support inequality gains the favorable term `-na`. The transported count comparison excludes it without an upper bound on its actual score. | A genuine finite base; ordered universal acquisition; strict positive-noise and zero-noise exclusions; both true predecessor caps. The separate finite 40–42 and positive-barrier consumers still use recurrence information. |
| Variable-score corner interpolation and score charging in a future fixed-c scalar evaluation | Evaluate the formal coefficient at `c`; an old convex box containing `c` already gives an upper bound. The low interval contains `c`, where the relevant charge is zero. | Outward enclosures for `c`, every other parameter domain, sign gate and numerical leaf. No number of removed jobs or runtime gain has been measured. |
| Separate independent maxima for several conditional moments | Integrate the combined signed response against the same positive cost measure, then bound the single response/cost ratio. | A verified majorant on the full acquired support and the nonlinear convolution remainder. The note supplies a proved example, not replacement production rows. |
| Dense sampled contact grid for one specified finite law | Piecewise cubic contact has only the listed jump and stationary candidates. | Exact event arithmetic and rigorous values at all candidates; contact is not sufficient for global optimality. |

The first raw ceiling, Gaussian-weight license, phase price, complete low/high
frequency bounds, index/deletion gates, signed repair, binomial comparison,
finite base and complete count cover do **not** disappear. No existing
certificate, production driver or target was changed. Earlier workload
estimates are not updated by this analytic note.

## Mathematical and execution status

| Result | Mathematical status | Execution status |
|---|---|---|
| Excess attainment, contact, support and conservation | Locally derived; transfer independently reviewed with explicit qualifications | Fresh rational/Laurent-polynomial and atom-boundary controls pass |
| Scalar-schedule transfer | Conditional theorem; each universal primitive and numerical leaf remains a premise | Independent exact identity/sign controls pass; no complete scalar replay |
| Moment circle, gap family and weighted common measure | Locally derived; independent bounded analytic review | Fresh rational identities and finite-law controls pass |
| Unconditional own-sign skeleton domination | Refuted, also at n=42; examples do not refute Berry–Esseen or a correctly restricted local comparison | Exact convolution and outward rational normal bounds pass |
| Argon deletion/quartic/coarse-Gaussian replacements | Refuted at the proposed scope | Exact negative controls pass |
| Complete BASE41, LOCAL42 and sharp conjecture | Remain unproved or not fully independently audited here | No new complete certificate or Lean acceptance |
| Documents | Review artifacts, including explicit AI disclosure | Both compile; visual inspection and isolated portable rebuild recorded |

Independent review accepts integration of the **narrowed conditional
transport theorem**. It does not certify the whole proof or recommend
publication of the conjecture as proved. This is suitable to merge as
documented research progress after author review; keep the submission draft
pending that review. No merge is performed by the assistant.

## Reproduction and review records

- `runs/strategy-v4-20261027/integration01/receipt.json` records eight bounded
  checks, their exact commands, versions, hashes and return codes. All passed.
  The source check found 478 manuscript labels and 271 references; all 2,748
  original baseline entries were unchanged.
- `excess01/`, `transport-review01/`, `opus01/`, `geometry02/` and the Argon
  records under `runs/argon-audit-20261027/` preserve the detailed evidence. Check scripts use Python's
  standard library and run with assertions enabled.
- `geometry01/` preserves the initial missing-SymPy failure; the final checker
  was rewritten using exact standard-library arithmetic. `manuscript-build01/`
  preserves an initial duplicate-label LaTeX failure; the corrected build is
  `manuscript-build02/`. Failed attempts are not counted as passes.
- `render02/` contains the final all-page companion overview; `render01/`
  preserves the first companion build and 14 affected manuscript pages.
  Selected equations were also inspected at full rendered size.
  `visual-review.json` records the scope; `export01/` records portable rebuilds.
- [Revision decisions](../../../manuscript/arxiv-v1/research/revision4-decisions.md)
  explain the conservative edits to the longer manuscript.

The constructor's exact reviewed `excess.tex` is unchanged, SHA-256
`a7105d57f4f353a7fcdd32947b1feae044b3df5dc29558afb48c575e9ea4a2d0`.
Agreement among AI reviewers is not a substitute for the displayed proofs
or for independent human review.

## Next bounded research step

Choose one existing zero-barrier acquisition cell. List its actual law,
support/moment inputs, formal multiplier interval, first raw ceiling and
all incoming dependencies. Evaluate its explicit `R_c` with fixed `c=C_E`,
and check each leaf using the existing exact acceptance arithmetic. Compare
the bound with the old variable-score envelope. This tests a concrete route
to removing a computational parameter without starting a generation campaign.
Only after a complete ordered cover has passed should the new tail theorem
replace the old entry contract.

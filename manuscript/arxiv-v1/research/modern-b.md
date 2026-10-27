# Modern literature and formalization audit B

Read on **27 October 2026**, working branch `manuscript/literature-b-20261027`,
starting fork commit `8989ba054eda36f63e469832f1e00f7e6a7a9084`.
This is a citation and scope audit. It does not independently verify the proofs
in the cited manuscripts or rebuild their numerical or Lean artifacts.
The companion bibliography is `../references-modern-b.bib`.

## Conclusions for the manuscript

The independent-array literature complements the iid problem but uses a
larger optimization class. Logan Bell's collection supplies a substantial
program of upper bounds, finite-array results and structural investigations.
Its current structural paper expressly distinguishes results proved within
that program from the remaining global classification conjectures. The two
Lean projects have different purposes: Asher Yan formalizes classical
nonuniform and multivariate normal-approximation results; the He--Cheng
repository formalizes eventual sharpness in the iid problem with explicit
external mathematical inputs. Neither project should be cited as an
independent proof of our certificate reductions.

A version correction matters. The [Primal Space project page](https://www.primalspace.me/projects/independent-berry-esseen-bounds/)
is marked 16 September 2026 and describes **four papers, collection 0.5.0**.
The [repository citation record](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/CITATION.cff)
and files at the inspected commit describe **eight papers, collection 0.7.0**.
The four originally linked papers are the upper-bound, finite-arrays,
small-Lyapunov and extremizers papers; these are papers 1, 2, 3 and 7 in the
current ordering. The structural-conjecture paper is now paper 8. All eight
are inventoried below so that the four-paper page is not mistaken for the
current complete collection.

## Citation identity and immutable references

| Item | Verified citation identity | Version and immutable reference | Identifier qualification |
|---|---|---|---|
| Bell's collection | Logan Bell; *The Berry--Esseen constant for independent summands* | `CITATION.cff` says version 0.7.0, release date 2026-10-06; inspected head `f61bc638774bfa1165065462f98fe31efade30bf`, commit dated 2026-10-19 | The releases API returned an empty list. Collection version is metadata, not a verified GitHub release/tag. No DOI is supplied in the inspected CFF or companion-manuscript entries. |
| Individual Bell papers | Sole listed author Logan Bell; exact titles below | Papers 1--7 dated 2026-10-06; paper 8 dated 2026-10-18, verified in title blocks | Preferred CFF instruction: cite individual author/title/manuscript date and collection version. `@unpublished` follows the collection's own companion bibliography. |
| Primal Space page | Logan Bell's project presentation, *The Independent Berry--Esseen Constant* | Page marks last substantial update 2026-09-16, version 0.5.0 | A presentation of the same work, not another independent publication or proof. No immutable site revision was obtained. |
| ProbabilityApproximation | Asher Yan; *ProbabilityApproximation: Berry--Esseen Bounds for Independent Sums* | Release v0.9.6, 2026-07-20; commit `c89fba908a33ba741836407f43c67609e2d05279` | CFF supplies this software authorship and date; no software DOI supplied. README's acknowledgement of ChatGPT 5.6 does not alter the CFF author field. |
| BerryEsseenLean | Repository title *Berry--Esseen: eventual sharpness in Lean*, accompanying the paper of Hengzhi He and Guang Cheng | Commit `2b97fa7400dd85fc98b829224c89b0f986789395`, 2026-09-13 | No root CFF was found (404); releases API returned no releases. `reference/paper.bib` is a paper citation, not separate software-author metadata. BibTeX therefore records the artifact without inventing individual software authors. |

For ProbabilityApproximation, the GitHub annotated tag object
`cfcb156561421aadc61b9918620be18470b1460d` was read and resolves v0.9.6 to
`c89fba908a33ba741836407f43c67609e2d05279`. The
[release page](https://github.com/Polarnova/ProbabilityApproximation/releases/tag/v0.9.6)
agrees. Its current main head was also observed as
`a2fc5bda874d9b69186c0ba165bf79f3b9897662` (22 July); the citation and theorem
inspection here use the release commit, not that later moving branch.

There is also a paper-version mismatch to preserve explicitly. The
[He--Cheng v1 record](https://arxiv.org/abs/2609.06358v1) is dated 6 September
2026 and titled *The Berry--Esseen Bound is Sharp for All Sufficiently Large
Sample Sizes*. The [v3 record](https://arxiv.org/abs/2609.06358v3), revised
30 September, is titled *The Berry-Esseen Constant Conjecture is Eventually
True*. Both list Hengzhi He and Guang Cheng and arXiv's DOI
[10.48550/arXiv.2609.06358](https://doi.org/10.48550/arXiv.2609.06358).
The DOI does not distinguish versions. Bell's structural bibliography cites
v1; BerryEsseenLean's September 13 snapshot retains the earlier title and a
bundled manuscript. Do not infer that this snapshot formalizes the later v3
merely because its README links to the versionless arXiv record. The root
manuscript's He--Cheng citation should be supplied by the coordinating
literature audit, with the relevant version stated.

## Bell's eight manuscripts: source-backed scope

Every link below is fixed to commit `f61bc638774bfa1165065462f98fe31efade30bf`.
The statements are **reported results in the cited manuscripts**, not
independent mathematical endorsements from this audit. All use centered
independent real summands with positive total variance and finite third
absolute moments, subject to the additional scopes shown.

| BibTeX key and exact title | Reported result and limitations | Primary source location |
|---|---|---|
| `BellIndependent2026`: *An upper bound on the Berry--Esseen constant for independent summands* | Universal independent-array upper bound `C_ind <= 1013039690742047/2251799813685248 < .44988`, from analytic estimates and interval certificates. This is not the sharp `.409732...` bound. | [Theorem 1.1 source](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/paper/main.tex#L107), lines 107--115; [generated exact constant](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/paper/values.tex). |
| `BellFinite2026`: *Berry--Esseen bounds for two summands and Bernoulli arrays* | At most two arbitrary summands: `C_2<49/120<C_E`. Sharp coefficient `C_E` for at most three two-point summands of arbitrary diameters, or any number of two-point summands with a common diameter. Also gives dominant-two-summand regimes. These are distinct restrictions, not arbitrary finite arrays. | [Main source](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/paper/finite-arrays/main.tex#L120), lines 120--144, abstract 42--63. |
| `BellSmall2026`: *The sharp Berry--Esseen bound for independent arrays with small Lyapunov ratio* | `Delta<=C_E L` for `L<=exp(-exp(97))`. The smallness restriction is on the Lyapunov ratio, not on the number of summands alone. The text identifies its adaptation of the He--Cheng variational/jitter/local-comparison method. | [Theorem 1.1 source](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/paper/small-lyapunov/main.tex#L90), lines 90--106. |
| `BellTransport2026`: *Zero-bias transport and extremal Bernoulli arrays* | Equality in `2V W_1(S,S*)<=sum E|X_i|^3` is characterized by identical nonconstant two-point summands, with zeros allowed. The repeated-block asymptotic theorem fixes the block before taking repetitions to infinity. It is not uniform convergence over arbitrary changing arrays. | [Main source](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/paper/transport/main.tex#L113), lines 113--166. |
| `BellBernoulli2026`: *Bernoulli extremizers for the independent Berry--Esseen ratio* | Classifies common-diameter two-point maximizers as an iid nonzero block padded with zeros; solves the two-two-point-summand problem with arbitrary diameters; gives large-count/small-diameter-deviation replacement and asymptotic binomial-envelope results. Does not classify arbitrary independent arrays. | [Main source](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/paper/bernoulli-structure/main.tex#L121), lines 121--191 and abstract 40--63. |
| `BellSmallStructure2026`: *Small Lyapunov ratios and the structure of Berry--Esseen maximizers* | Near-Esseen sequences with `L->0` satisfy lattice/transport structure; for an ineffective absolute `epsilon_0>0`, a global `N`-summand maximizer with `L<epsilon_0` is a padded iid two-point array. The hypotheses include global maximization and small `L`. | [Theorem 1.2 source](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/paper/small-lyapunov-structure/main.tex#L138), lines 138--145; Theorem 1.1 at 90. |
| `BellExtremizers2026`: *Extremizers for the independent Berry--Esseen inequality* | Finite/compactified maximizers have a four-point support bound and an equally maximizing three-point representative. The compactified existence/elimination theorem is in the hypothetical regime `C_ind>C_E`; weighted summability further assumes unit-variance third-moment sum `<=18481/25000`. These are not an unrestricted two-point classification. | [Main source](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/paper/extremizers/main.tex#L147), lines 147--192; finite support theorem at 469. |
| `BellStructural2026`: *On the structural conjecture for extremizers of the independent Berry--Esseen inequality* | Separates optimizing the sum law from minimizing the factorization's third-moment cost; characterizes binomial factorizations and the zero of an endogenous characteristic-function deficit. It explicitly leaves general finite-`n` value, classification and uniqueness conjectures open. | [PDF](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/paper/structural-conjecture/structural-conjecture.pdf), pp.9--10,14--15,27--30; [source](https://github.com/epicycloids/independent-berry-esseen-bounds/blob/f61bc638774bfa1165065462f98fe31efade30bf/paper/structural-conjecture/main.tex#L594), lines 594--639,940--993,1867--2049. |

The older project page's `.44988794` and `exp(-exp(20004))` are superseded in
the inspected manuscript snapshot by `.44988` and `exp(-exp(97))`. These are
version differences, not evidence of contradictory theorem scopes. Cite the
primary paper version that supplies a number; do not combine the page's
four-paper description with the current structural manuscript.

### The structural paper deserves precise use

The PDF was obtained read-only through the GitHub connector after the web
PDF fetch failed. Its Git blob is `a293f4fc39e14e9f7997c617bec072fa276fd4c6`,
SHA256 `6b8606235618a768120f323e1efa61b85059e66132233ae062990f8a8a374225`,
32 pages. The title page gives Logan Bell and 18 October 2026; PDF creation
metadata is 19 October and is not the manuscript date. The relevant pages
were read and page 29 visually inspected against the TeX statements.

The paper defines `M_n(mu)` by minimizing the **sum of marginal third absolute
moments** over independent factorizations of a fixed sum law `mu`.
Theorem 2.2 concerns compactness of these fixed convolution fibers and
semicontinuity. Theorem 2.3(ii), pp.9--10, says that for an array already
attaining its independent-array supremum, being a padded iid two-point array
is equivalent to having a centered binomial sum law of order at most `n`.
It does not establish that every global maximizing sum law is binomial.
Section 6.2 names precisely that latter implication as the missing step.

Theorem 3.3, pp.14--15, constructs `h_hat=(R+sqrt(R^2-K_3^2))/V` and a
nonnegative characteristic-function deficit `J=1-|E exp(2*pi*i*S/h_hat)|^2`.
Its reported zero-set characterization is an equivalence between `J=0` and
a finite iid two-point block with zero padding. Page29 expressly leaves
`global optimality => J=0` unproved. An equality characterization cannot be
used as a monotone objective improvement inequality.

The certified four-summand unequal-diameter local maximizer in Theorem 5.1
has a ratio about `.282489`, well below the relevant binomial comparator.
It is an obstruction to a local-improvement strategy, not a counterexample
to the sharp Berry--Esseen inequality. Section 5 distinguishes stored
high-precision binomial scans from interval-certified local statements.
Citing the project, its PDF and its stored scan as three separate confirmations
would double-count one research program.

### Independent-array notation must not be imported into the iid argument

Bell's `C_n` permits independent nonidentical summands and deterministic zeros;
it is nondecreasing by zero padding. Our iid `C_n` optimizes over one common
nondegenerate law and has a different role. Likewise `L=rho/sqrt(n)` in the
standardized iid case; a small-`L` theorem gives a threshold depending on
`rho` unless uniform moment control has first been established. Finite third
moment alone does not impose a common upper bound on `rho` over all laws.
These are elementary domain/quantifier observations, not criticisms of the
cited papers, which themselves discuss the zero-padding distinction.

## Formalization scope and evidence

| Artifact | Directly inspected formal statement | Assumptions and evidence boundary |
|---|---|---|
| ProbabilityApproximation v0.9.6 | `ProbabilityTheory.nonuniformBerryEsseen` quantifies one universal positive constant before arbitrary finite independent centered scalar families of unit total variance with finite third moments; denominator `1+|x|^3`. | [Lean source](https://github.com/Polarnova/ProbabilityApproximation/blob/c89fba908a33ba741836407f43c67609e2d05279/ProbabilityApproximation/ChenShao/NonuniformBerryEsseen.lean#L68), lines 68--93. This endpoint has no explicit unproved classical-result parameter. Its constant is existential, not `C_E`. |
| ProbabilityApproximation v0.9.6 | `exists_bentkus_convex_set_constant` quantifies a positive universal constant for independent centered vectors, positive-definite covariance and measurable convex sets, with `d^(1/4)` and whitened third moments. | [Lean source](https://github.com/Polarnova/ProbabilityApproximation/blob/c89fba908a33ba741836407f43c67609e2d05279/ProbabilityApproximation/Bentkus/Induction.lean#L649), lines 649--673. It is a multivariate approximation theorem, not sharp scalar iid optimality. |
| ProbabilityApproximation axiom checks | The registry audits four public endpoints using recursive `Lean.collectAxioms`, rejects `sorryAx`, permits only `propext`, `Classical.choice`, `Quot.sound`. CI calls the audit and a forbidden-token check after the production build. | [Audit source](https://github.com/Polarnova/ProbabilityApproximation/blob/c89fba908a33ba741836407f43c67609e2d05279/.github/scripts/audit_axioms.lean#L11), lines 11--34, and `.github/workflows/ci.yml`. This review inspected source, not a freshly run build or the entire transitive proof. Do not inflate the four-endpoint registry into an independently rerun audit of every declaration. |
| BerryEsseenLean main endpoint | `MainClaim` places `exists N` before `forall n>=N`, `forall P`, and all thresholds, with actual product/map iid sum laws and finite third moment. | [Statement](https://github.com/UCLA-Trustworthy-AI-Lab/BerryEsseenLean/blob/2b97fa7400dd85fc98b829224c89b0f986789395/BerryEsseen/Statement.lean#L54), lines 54--66. Threshold is uniform in laws; no common upper third-moment bound is imposed. |
| BerryEsseenLean strict endpoints | Main theorem takes H,A,E,B,I,W; explicit theorem takes H,E,B,I,U,K; sharpness takes A. Explicit threshold is `2*ceil(exp(10^17))`. | [StrictResults](https://github.com/UCLA-Trustworthy-AI-Lab/BerryEsseenLean/blob/2b97fa7400dd85fc98b829224c89b0f986789395/BerryEsseen/StrictResults.lean#L11), lines 11--27. These are proposition parameters even when recursive axiom reports contain only Lean's usual axioms. |

The [UCLA assumption record](https://github.com/UCLA-Trustworthy-AI-Lab/BerryEsseenLean/blob/2b97fa7400dd85fc98b829224c89b0f986789395/docs/ASSUMPTIONS.md)
identifies eight interfaces with ten fields: structural/remainder bounds H;
fixed-law Esseen asymptotics A; Esseen's moment inequality and equality E;
Schulz's binomial bound B; non-iid bound I; nonuniform bound U; Wasserstein-3
convergence characterization W; Wasserstein-1 duality K. B is sourced to a
public dissertation, while W/K use Villani's 13 June 2008 author manuscript.
The API's historical `Published...` names do not make all sources journal
articles. A is a fixed-law asymptotic, not a uniform triangular-array premise.
The smoothing interface is discharged internally and is not a ninth external
input. These distinctions are stated by the repository itself.

Its [verification document](https://github.com/UCLA-Trustworthy-AI-Lab/BerryEsseenLean/blob/2b97fa7400dd85fc98b829224c89b0f986789395/docs/VERIFICATION.md)
and stored `verification/logs/strict-axioms.log` report the standard three
axioms and retain the theorem parameters in the printed endpoint types.
They also distinguish kernel checking from prose-to-interface review and do
not claim an independent Comparator certificate. The literal probability-law
endpoint is not an additional arbitrary-probability-space `iIndepFun`
transport endpoint. The toolchain is Lean 4.28.0 with a pinned Mathlib commit;
ProbabilityApproximation uses Lean/Mathlib 4.32.0. This audit ran neither build.

ProbabilityApproximation's [CFF](https://github.com/Polarnova/ProbabilityApproximation/blob/c89fba908a33ba741836407f43c67609e2d05279/CITATION.cff)
asks users to cite both the software and original mathematical sources. For
the scalar endpoint it distinguishes the classical finite-third-moment
Bikelis result from the stronger Chen--Shao truncated-moment theorem and the
2005 proof presentation. For multivariate results it identifies Bentkus.
These should not be described as new inequalities due to the formalization
author. The coordinating bibliography audit should verify any original-source
entry actually imported into the manuscript; this report does not silently
promote the repository's bibliography to independent bibliographic verification.

## Proposed manuscript paragraphs

The following text is deliberately short enough for a related-work section.
Its citations refer to the companion BibTeX keys; the He--Cheng paper key is
left to the coordinating bibliography.

> Bell's recent manuscripts investigate the broader problem of independent,
> not necessarily identically distributed, summands. The collection reports
> a computer-assisted universal upper bound below 0.44988, sharp bounds in
> several finite-array and small-Lyapunov regimes, and structural results for
> extremal arrays \cite{BellIndependent2026,BellFinite2026,BellSmall2026,BellExtremizers2026}.
> The distinction between these regimes matters: in the independent setting,
> zero padding changes the number of summands without changing the Lyapunov
> ratio. These results therefore have different quantifiers from a uniform
> eventual theorem for iid laws.
>
> Bell's structural study separates the choice of a sum distribution from
> the minimum third-moment cost of its independent factorization
> \cite{BellStructural2026}. It also distinguishes finite-index value,
> extremizer-classification and uniqueness conjectures. The binomial-fiber
> and characteristic-function characterizations do not by themselves settle
> the remaining global selection step. This is pertinent to our use of
> contact and local comparison: necessary structural information must be
> connected to the actual optimizing iid law before it can justify a
> reduction of the proof obligations.
>
> Formal developments provide complementary ways to expose these obligations.
> Yan's ProbabilityApproximation library formalizes classical nonuniform
> scalar and multivariate normal-approximation bounds in Lean
> \cite{Yan2026ProbabilityApproximation}. The BerryEsseenLean project
> accompanying He and Cheng gives formal iid eventual-sharpness endpoints
> with explicitly listed external mathematical inputs
> \cite{BerryEsseenLean2026}. We distinguish such formal statements and their
> source assumptions from numerical certificate checks and from the
> mathematical reductions developed here.

Use only citations relevant to the final text; the eight-entry Bell inventory
is not a recommendation to cite all eight papers in every paragraph. The
project website need not receive a separate numbered bibliography entry when
it is used only to locate the papers. The Lean artifact and associated
He--Cheng preprint may both be cited when their different roles are discussed,
but should not be counted as two independent mathematical proofs.

## Read-only procedure and remaining limits

The GitHub connector was used first for repository metadata, CFF files,
branches, Git trees, immutable source files, release records and the
ProbabilityApproximation tag object. The generic tag-list endpoint was
unsupported; the specific Git tag endpoint supplied the required release
binding. UCLA's missing CFF and the two empty release lists are recorded
above as findings, not filled with inferred metadata. The web tool read the
Primal Space page and both arXiv version records. GitHub raw PDF web fetches
failed and a shell download had no DNS access; the connector's base64 file
read succeeded, and its bytes were checked against the Git blob before PDF
text extraction. The structural PDF was inspected with the PDF skill and
bundled pypdf/Poppler. No third-party program or verification suite was run,
no author contacted, and no external state changed.

| Result of this audit | Mathematical status | Execution status |
|---|---|---|
| Titles, author/date fields, version differences, immutable refs and release binding | Source-backed bibliographic findings | Fresh read-only retrieval and local PDF identity check |
| Scope comparison and iid/array distinctions | Locally derived comparison of inspected definitions and statements | Source/PDF inspection; no proof reconstruction |
| Bell's reported theorems | External manuscript claims, attributed at their stated scope | Numerical certificates not replayed |
| Lean theorem interfaces and declared audit behavior | Source-inspected formal claims and explicit hypotheses | No fresh Lean build; UCLA logs are repository evidence only |
| Incorporation as a proof dependency in our work | Requires separate mathematical review and exact hypothesis matching | Not performed by this literature task |

The audit is intentionally narrower than a referee report or formal proof
reproduction. No conclusion here closes an unresolved dependency of the
user's proof, and no citation grants permission to remove a certificate.

# Modern literature and citation audit

Read on 27 October 2026. This is a source and bibliographic audit, not an independent verification of the external proofs. The accompanying `references-modern-a.bib` gives one entry per work; a repository and its accompanying proof document are not counted as separate results. The source receipt records the downloaded PDF hashes and immutable Git references.

| Work | Mathematical status in this audit | Execution status in this audit |
| --- | --- | --- |
| Xiao–Li, global bound 0.4395 | External proof and formalization claim; statement and trust boundary read | No Lean build or certificate replay |
| Lin, global bound 0.423 | External proof and formalization claim; statement, attribution and trust boundary read | No Lean build or certificate replay |
| He–Cheng v3, eventual sharp bound | External preprint theorem; exact quantifiers and threshold read | No full proof audit or formalization replay |
| Tao and contributors, Problem 19a | Secondary status registry, not a theorem provider | Repository source read |
| Rodziewicz–Kołodziejek, Hexagon v3 | Earlier working draft and provenance record; not independent support for the new manuscript | Metadata and selected PDF sections read; no certificate replay |

## 1. Xiao–Li: one paper-and-repository citation

**Preferred citation:** Haonan Xiao and Chunlin Li, *A 0.4395 Upper Bound for the i.i.d. Berry–Esseen Constant* (2026), GitHub repository and accompanying September 2026 note. The [README citation block](https://github.com/haonan-xiao/iid-berry-esseen/blob/f00d781c8c42908bf4aef2739129442a0919fa38/README.md#citation) supplies the entry `xiao2026berryesseen`; the proposed BibTeX retains its author, title, year, type and URL, adding the inspected commit. The PDF title page independently identifies both authors. No DOI or journal citation was present in the inspected records.

Theorem 1, [PDF p. 1](https://github.com/haonan-xiao/iid-berry-esseen/blob/f00d781c8c42908bf4aef2739129442a0919fa38/paper/berry-esseen-04395.pdf), claims the bound for every integer (n\ge1), every centered variance-one real law with finite absolute third moment, and the supremum over all thresholds. The proof retains the first absolute moment and a symmetrized third-moment coordinate in a Prawitz smoothing argument. Section 5 and the [formalization guide](https://github.com/haonan-xiao/iid-berry-esseen/blob/f00d781c8c42908bf4aef2739129442a0919fa38/FORMALIZATION.md) describe exact certificates and their Lean connection. Concrete `native_decide` evaluations additionally trust the compiler. The README distinguishes historical full numerical verification from the renamed publication layout, for which selected analytic modules were rebuilt but a full numerical replay had not been performed.

Read: all theorem/scope statements, the analytic architecture, Section 5 and the AI disclosure; README and formalization guide. The disclosure credits extensive Codex assistance. Neither this audit nor a bibliography entry verifies the formal development.

## 2. Lin: distinct from He–Cheng

**Proposed citation:** Yongxi Lin, *Berry–Esseen bounds in Lean* (2026), repository `CoolRmal/BerryEsseen`, with accompanying document *The i.i.d. Berry–Esseen constant is at most 0.423: a machine-checked proof*, dated 13 September 2026. The PDF has a blank author field. The attribution to Lin comes from the [repository commit](https://github.com/CoolRmal/BerryEsseen/commit/bfb22608ad18b4fa9fda8dd9a1ed2c2b6fbc29e7) and the named reference in Tao’s registry; it should not be represented as a printed PDF byline. No preferred BibTeX, DOI or journal citation was located.

The [document](https://github.com/CoolRmal/BerryEsseen/blob/bfb22608ad18b4fa9fda8dd9a1ed2c2b6fbc29e7/paper/upper-0423.pdf), Theorem 1.1 and Sections 1–3, claims the global iid constant is at most 0.423. Section 2 explicitly credits Xiao–Li’s analytic framework while stating that it does not assume their numerical theorem or reuse their certificates. Sections 13–14 describe 579 `native_decide` obligations, the additional compiler/runtime trust, and absence of an independent verification claim. The analytic cases cover (n=1) and large Lyapunov fraction; the remaining finite and uniform certificates cover (2\le n\le255) and (n\ge256), respectively.

Read: Sections 1–3, 13–15, README and [UPPER_0423.md](https://github.com/CoolRmal/BerryEsseen/blob/bfb22608ad18b4fa9fda8dd9a1ed2c2b6fbc29e7/docs/UPPER_0423.md). The only listed release is an optional proof cache for an older commit; its release description must not be used as the trust statement for the inspected 0.423 development.

## 3. He–Cheng: eventual sharpness with a uniform threshold

**Preferred scholarly identifier:** Hengzhi He and Guang Cheng, *The Berry-Esseen Constant Conjecture is Eventually True*, [arXiv:2609.06358v3](https://arxiv.org/abs/2609.06358v3), revised 30 September 2026; DOI [10.48550/arXiv.2609.06358](https://doi.org/10.48550/arXiv.2609.06358) identifies the preprint, not a journal publication. Version 1 was submitted 6 September. Cite v3 once unless discussing revisions.

Theorem 1.1, [PDF p. 2](https://arxiv.org/pdf/2609.06358v3), asserts a universal sufficient threshold (N=2\lceil\exp(10^{17})\rceil). Laws may vary with (n), without a common third-moment bound. This is an eventual weak sharp inequality, not an all-index result or a statement of eventual two-point optimality. Read: pp. 1–3, final assembly pp. 101–102, and the opening of Appendix A. The paper links a conditional Lean formalization in `UCLA-Trustworthy-AI-Lab/BerryEsseenLean`, not Lin’s repository. That formalization was not inspected here.

## 4. Tao’s registry: useful status attribution, not proof evidence

The [Problem 19a entry](https://github.com/teorth/optimizationproblems/blob/e95af44bc6ae938f545a0fc62cd1b6c1f6088a56/constants/19a.md) is part of *Optimization Constants in Mathematics*, a community-maintained collection initiated by Terence Tao. At the inspected commit, it labels the Xiao–Li and Lin bounds “Unverified” and describes their compiler trust. These are the registry’s status assessments, not results of this audit. The [README](https://github.com/teorth/optimizationproblems/blob/e95af44bc6ae938f545a0fc62cd1b6c1f6088a56/README.md) explicitly disclaims correctness certification of listed bounds. Use `tao2026berryesseenregistry` only for this status/context; cite the primary works for their actual mathematical statements.

No preferred citation file was found. The proposed author field, “Terence Tao and contributors”, identifies a maintained resource rather than assigning every sentence to Tao. The bibliography pins `constants/19a.md`; the snapshot date is not claimed as its original publication date.

## 5. Hexagon: prior draft and AI provenance

The canonical inspected record is [hexagon:2610.00147v3](https://hexagonmath.org/2610.00147v3), *Moment defects and sharp iid Berry–Esseen bounds*, contributed by Kacper Rodziewicz and Bartosz Kołodziejek. Its version history and PDF date v3 to 17 October 2026; the header retains the initial 7 October deposit date. No DOI is assigned. The proposed entry follows the supplied BibTeX but puts the named contributors into `author` and records the version date.

The record labels the text primarily AI-generated and human understanding partial. Its provenance describes ChatGPT/Codex assistance, parallel agent roles and partial conditional Lean formalization. It does not claim full manuscript formal verification. Read: provenance, version history, citation block and PDF opening. The prior manuscript’s mathematical claims are outside this source audit. This is a precursor by the present authors, not independent validation of the new proof.

## 6. Ready-to-adapt literature paragraphs

These are proposed new prose, not quotations. The final sentence of the first paragraph reports this audit’s scope and may be shortened to fit the manuscript’s verification statement.

> Recent computational approaches have reported improved global upper bounds for the iid Berry–Esseen constant. Xiao and Li give a bound of 0.4395 with an accompanying Lean development; Lin reports 0.423 using a refinement of that analytic framework \cite{xiao2026berryesseen,lin2026berryesseen}. Both developments use exact finite certificates evaluated through Lean’s `native_decide`, whose trust boundary includes the compiler. We have not independently replayed these formal developments, and do not use their numerical conclusions as premises here.

> He and Cheng report the sharp bound for every sufficiently large sample size, with a threshold independent of the summand law \cite{hecheng2026eventually}. Their argument combines variational analysis of extremizers with smoothing, moment stability and a local two-point comparison. Its scope is eventual sharpness; the remaining finite range is a separate problem.

Optional registry sentence: “The status of these recent computational bounds is also recorded in the maintained survey of optimization constants \cite{tao2026berryesseenregistry}.” This sentence adds context, not an extra supporting proof citation.

For the new AI disclosure, state the actual present workflow rather than copying the earlier model list. A restrained candidate, to be reconciled by the authors with the final manuscript, is:

> ChatGPT and Codex assisted mathematical exploration, implementation of exact checks, source comparison and manuscript preparation. AI-generated arguments were subject to further mathematical review. The present manuscript distinguishes analytic dependencies, executable checks and unresolved obligations; AI-agent agreement is not treated as verification. An earlier working draft records the project’s prior AI-assisted development \cite{rodziewiczkolodziejek2026momentdefects}.

Do not claim complete human review or complete formal verification unless these have actually been performed.

## 7. Additional attribution requested: Shevtsova’s sharp third-moment inequality

The original journal reference is Irina Shevtsova, *On the accuracy of the approximation of the complex exponent by the first terms of its Taylor expansion with applications*, **Journal of Mathematical Analysis and Applications 418** (2014), no. 1, 185–210, DOI [10.1016/j.jmaa.2014.03.075](https://doi.org/10.1016/j.jmaa.2014.03.075). Its [official preprint metadata](https://arxiv.org/abs/1301.2783v3) verifies those bibliographic fields. [Theorem 2 in the preprint, p. 5](https://arxiv.org/html/1301.2783v3), gives the sharp bound on the signed third moment for mean zero, variance one and absolute third moment (b\ge1), with two-point equality. Inverting its displayed bound yields

\[
\rho\ge\frac{\gamma^2+2}{\sqrt{\gamma^2+4}},\qquad
\rho=\mathbb E|X|^3,\quad\gamma=\mathbb EX^3.
\]

The journal PDF was not obtained, so its suggested locator “Theorem 6” is not independently confirmed here. Cite the article as `shevtsova2014complex`, using the verified preprint theorem number if a locator is necessary. This is attribution, not a fresh audit of Shevtsova’s proof.

## 8. Retrieval and limitations

GitHub repository, file, tree, commit and release metadata were read through the GitHub connector first. Complete recursive trees for the three repositories contained no `CITATION.cff`; Xiao–Li’s README nevertheless provides preferred BibTeX. Release listings were empty for Xiao–Li and the registry. The connector did not support the tags endpoint; no inference about absence of tags is made. No release assets were downloaded.

Four PDFs were downloaded read-only, their hashes recorded, and text extracted with `pypdf`. Xiao–Li’s title/theorem page and He–Cheng’s threshold page were also rendered and visually read. No external Lean build, certificate program or proof campaign was run. Version identifiers and hashes establish which material was read, not its mathematical correctness. The PDF receipts are retained without committing copies of the external PDFs.

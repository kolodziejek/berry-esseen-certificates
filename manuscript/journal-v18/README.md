# Consolidated manuscript for mathematical review

Read [the complete PDF](main.pdf). This is a **102-page review draft**, including all analytic arguments, the certificate explanation, and references. It is not in the Annals of Probability template. The requested total of about 60 pages has **not** been achieved.

The manuscript presents the computer-assisted sharp iid Berry–Esseen bound for every positive sample size, optimality of the universal constant, and strictness of the optimal ratio at each index at least 47. Its mathematical status is a locally derived and reviewed proof candidate using the stated published inputs and executable certificates. Neither a successful compilation nor the reviews supplied here constitute independent human acceptance or proof-assistant verification.

The predecessor `extended-v17` had 194 total pages. This version removes the separate fixed-target tail argument and repeated derivations; it does not move indispensable analytic proofs into a supplement. Its remaining length is concentrated in the support/moment acquisition and local comparison. [REVISION_REPORT.md](REVISION_REPORT.md) explains the changes and measured lengths. [SIMPLIFICATION_PLAN.md](SIMPLIFICATION_PLAN.md) specifies the next mathematical and verification work needed to attempt a substantially shorter version.

## Reading and checking

1. Read Sections 1 and 8 for the theorem and its dependency structure.
2. Read Section 2 for the extremizer, contact and conservation argument; Section 3 supplies the hypotheses at a first failing index.
3. Section 4 explains what is certified, how candidates are found, and what acceptance actually proves. Sections 5–7 prove the analytic reductions and state the numerical interfaces.
4. Use [PROOF_MAP.md](PROOF_MAP.md) to map those interfaces to the existing immutable evidence ledger. The probability/analysis and the finite acceptance checks are separate proof obligations.
5. The [review directory](review/) records bounded mathematical reviews, the equality audit, source mappings and final build/layout evidence. These are review aids, not additional theorem assumptions.

The certificate data, original programs, complete result inventories and restoration commands remain in [`../extended-v17/reproduction/`](../extended-v17/reproduction/), pinned at commit `c31d0cbe2af867d26871fbae37a3a7f4066f4a55`. Their bytes and numerical targets are unchanged. The required selected numerical families were completed in the preceding work; this revision does not claim a new execution of the complete numerical campaign. In particular, the separate 114-command fresh-workspace recipe has not been rerun as one relocated campaign.

## Compile

From this directory, using a TeX installation with the standard packages named in `main.tex`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`main.bbl` is included for source portability; the four bibliography files are also supplied. TeX Live 2025 produced the delivered PDF. Build evidence records exact source hashes, return code and PDF identity. Compilation checks typesetting and references, not the mathematical truth of the theorem.

## Shortening prototype

[`research/polynomial-prototype/`](research/polynomial-prototype/) contains a bounded feasibility experiment: five exact polynomial objects and 23 rejection controls. It is **outside the manuscript dependency graph** and proves no new Berry–Esseen claim. It illustrates one possible future certificate interface, without claiming that elementary factorizations should be hidden from readers or that this pilot delivers the missing 42-page saving.

No journal submission, arXiv submission, or merge is performed by this revision.

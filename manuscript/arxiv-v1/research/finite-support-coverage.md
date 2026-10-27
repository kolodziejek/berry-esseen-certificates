# Retained finite-index support appendix

The new `appendices/finite-support.tex` supplies the quantitative part of S2 in `paper/analytic-supplement.txt`, beginning with “One support estimate, uniform in the threshold” and ending before S3. It also gives the complete direct proof from A2 of the global cubic Gaussian bound. The contact/attainment proof preceding S2 is not duplicated: the appendix uses `ms:contact` and `ms:contact-formula` from the main manuscript. Structural and moment inputs link to `ms:structural-classical`, `ms:sign-moment`, `ms:sharp-third`, and `ms:gaussian-constants`.

| Included analytic argument | Literal scope | Numerical premise retained |
| --- | --- | --- |
| Scale correction | Integer `n>=36` | None beyond displayed rational algebra |
| Contact with signed same-law predecessor loss and whole exterior rays | Integer `n>=2`; arbitrary raw threshold; all closed support points | Six polynomial sign gates and both whole-threshold boundary bounds |
| Whole-threshold curvature cells and tails | Closed cells plus both infinite threshold tails | Outward CDF/density/root enclosures, including the 580-cell index-27 condition |
| Fifth-order heat expansion, uniform finite remainder and Gaussian tangent | All thresholds; stated nonnegative coefficient/domain gates | None for the analytic identity |
| Signed fifth-order envelope | Its printed `A,B,D,W,T` sign gates | Gates must hold on the full selected domain |
| Direct cubic Gaussian bound from A2 | All real thresholds/support arguments, every integer `n>=2` | None; full translation/scale remainder proof supplied |
| Finite-band polynomial and far-ray reduction | `36<=N<=n<=L`, or stated infinite band with favorable term zero | All adjacent closed radial cells and both complete rays |
| Historical finite support rows | Index 27 and the five listed finite-index bands, with their original upper endpoints | Original bounds and exact acceptance remain conditional |
| Bounded-threshold Gaussian series | `n>=4`, `|H|<=h`, `|t|<=r`; all six retained coefficient polynomials | Uniform analytic remainder supplied |
| Signed radius/coordinate-strip contact test | Literal `n>=47`, excess at most `.7/n`, predecessor loss at most `.19` | Closed signed cells, input moment/threshold rows, positive lower beta gate |

The favorable fifth-order term is frozen at the **upper** finite index endpoint; adverse terms use the lower endpoint. No upper endpoint is silently removed. The rational square-root surrogates are explicitly positive. The domination polynomial now distinguishes its linear outward quantity `Bhat_+` from the exact squared `B_+^2` factor. These clarify the existing sufficient conditions rather than weakening a numerical target.

Historical margins and cell counts are identified as source reports, not fresh PASS results. The index-27 scale and moment constants, scalar floor36 comparison, displayed leading series coefficients, and basic Gaussian constants received bounded rational checks only. Five false-rule controls reject floor35, a reversed leading series sign, omission of the fifth-term correction, freezing the favorable term at the lower index endpoint, and a negative square-root surrogate. The checker does not run or accept any native support certificate or coverage object.

The direct lemma permits a *candidate* small-index zero-loss route, but this appendix does not instantiate a complete n=5 support package or prove the whole-threshold boundary bounds for its individual rows. Passing the exterior-ray derivative gates alone would not establish those missing boundary inequalities.

| Deliverable | Mathematical status | Execution status |
| --- | --- | --- |
| Retained S2/A2 proof text | Supplied analytic arguments, reproduced with explicit scope and conditional certificate inputs; elementary Gaussian/algebra steps rederived | No native replay |
| Bounded rational identity checker | Limited arithmetic and false-rule controls, not full analytic or numerical acceptance | Fresh PASS in final `identities03` run |
| Standalone appendix preview | Typesetting only; `M` reference labels identify omitted main-text context | Eight-page TeX Live preview; final compile receipt in `texlive02` |

All eight pages of the preceding preview were visually inspected using rendered contact sheets. They had no clipped text, overlapping equations, broken tables or overfull-box warning. The final change only consistently names the local heat coordinate `z_v`; the final render was also checked. The preview's external `M` references deliberately identify main-manuscript context and do not pretend to be a standalone proof of that context. The integrated manuscript must resolve those references to the actual lemmas.

The new 65-call zero-loss support replacement does **not** remove finite-base ancestors merely by being stronger on a different domain. The appendix explicitly retains positive-loss, positive-excess and lower-index support/strip obligations until a separate proof covers their exact hypotheses. It establishes no finite base or global Berry--Esseen bound.

No reference source, old proof object, old log or production checker was changed. The reference baseline remains `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`. The final run receipts bind the source text and checker by SHA-256. Compilation receipts distinguish the initially corrected preview-wrapper/source typos, a shell Tectonic cache failure, and the successful desktop/TeX Live compilations. Build artifacts are local previews; the commit contains source and bounded evidence.

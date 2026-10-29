# Fixed-target continuation and a corrected positive-gap argument

The new research proof is kept as a separate 15-page note in
`mathematics/fixed-target-v5/2026-10-27/`, with complete new derivations,
source-linked reports and exact checks. The initial raw license is now
quantitative under its explicit Fourier premises; later acquisition and
the full conjecture remain open. This is not yet a replacement for the
full manuscript's conditional argument or its existing certificates.

The manuscript itself changes one proof explanation, on page 59 at
`appendices/fourier-analysis.tex:1971`. The old phrase
`(t-a)(rho-t)<=rho^2/4` is false on a positive portion of a gap crossing zero;
for example a=-1, t=1/2, rho=1 gives 3/4>1/4. The intended valid estimate is
`t(rho-t)<=rho^2/4`, multiplied by `t-a>=0` and integrated. The resulting
coefficient remains `rho^2*J/8`. No formula, certificate coefficient or
theorem target is changed.

The source checker still finds all 478 labels and 271 manuscript references.
The updated PDF has 158 pages; only page 59's extracted text changes from
the preceding PDF. Pages 58–60 were rendered and inspected. The portable
source ZIP rebuilds with shell escape disabled and identical page text.
Compiler, source hashes, exact commands and return codes are under
`runs/fixed-target-v5-20261027/`.

Original baseline entries, all existing certificates and upstream are
preserved. The new arguments and corrected manuscript belong to existing
draft PR #5 for author review; no merge or publication is authorized.

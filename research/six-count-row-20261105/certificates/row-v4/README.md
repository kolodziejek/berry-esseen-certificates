# Five-summand BN/p38: complete three-root candidates

This is the frozen constructor package for the original acquired n5
BN/p38 row. It preserves the target C_E, the original full noise cap and
signed beta interval. It is a conditional local comparison, not an
acquisition proof or a replacement for all295original n5rows.

All three root candidates are complete: k1 has246leaves, k2 has484,
and k3 has3. The **separate whole-row replay is recorded by the assembly
package**; construction success alone does not assert full acceptance.
`CANDIDATE_COMPLETION.json` binds the actual production captures and
selected object hashes. No producer record is fabricated or overwritten.

Read `SOUNDNESS_V1.md` for the complete common six-count/convex-polygon/
tensor argument, then `THEORY_V4.md` for the additional normal-noise,
cubic-moment, mean and sign-endpoint bounds. Relative references in these
preserved proof notes point to their original workspace; both required
mathematical texts are included here. The original threshold catalogue
and its source bindings live in the separate domain/assembly package.

Use ordinary, unoptimized Python3.12 or later. Acceptance requires only
the standard library; neither SciPy nor NumPy is imported. From here,
with fresh output directories:

```sh
python3 -I -B accept_v4.py objects/k1.json replay-k1 --k 1 --p 19/50 39/100 --u -0.222258117249 0.5 --noise 0 7687/25000
python3 -I -B accept_v4.py objects/k2.json replay-k2 --k 2 --p 19/50 39/100 --u -0.5 0.5 --noise 0 7687/25000
python3 -I -B accept_v4.py objects/k3.json replay-k3 --k 3 --p 19/50 39/100 --u -0.5 0.072258117249 --noise 0 7687/25000
python3 -I -B controls_v4.py objects/control_pilot.json controls
```

The exact decimal endpoints avoid argparse's negative-fraction ambiguity;
they are converted to exact rational numbers and compared with canonical
strings in the objects. Fresh replay recomputes all twelve rays per leaf,
the same-law moment reduction, every tensor coefficient and the complete
closed dyadic cover. It does not consume stored PASS summaries.

The seven-leaf control pilot previously passed23mutation rejections,
57inverse Bernstein identities and1,080direct moment identities.
Independent review receipts, the original domain census and whole-row
assembly controls are separate artifacts; this package does not inflate
their scope into an independently implemented full-row acceptance.

`discover_v4.py` and `repair_v4.py` are optional SciPy/NumPy construction.
The latter first checks every retained coefficient set under the new
exact targets, then constructs only repairs that are needed. Old partial
V3objects and their actual captures are included under `provenance/`.
They are inputs to construction, never accepted success premises.

All native files are unchanged copies with fixed pins. Historical captures
retain their original absolute runtime paths as provenance; the commands
above require none of those paths. Keep output directories outside this
frozen tree when preserving its byte inventory.

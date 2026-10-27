"""Bounded source-preservation checks, not semantic theorem verification."""
from pathlib import Path
from collections import Counter
import re
import subprocess

BASE = "6299d97"
FILE = "manuscript/arxiv-v1/appendices/finite-analysis.tex"
old = subprocess.check_output(["git", "show", f"{BASE}:{FILE}"], text=True)
new = Path(FILE).read_text()
labels = lambda text: re.findall(r"\\label\{([^}]+)\}", text)
a, b = labels(old), labels(new)
assert Counter(a) == Counter(b)
assert len(b) == len(set(b))
print(f"Preserved {len(b)} labels; no duplicates.")

def labelled_displays(text):
    result = {}
    for match in re.finditer(r"\\begin\{(equation\*?|align\*?|gather\*?)\}(.*?)\\end\{\1\}", text, re.S):
        block = match.group(0)
        for label in labels(block):
            assert label not in result
            result[label] = re.sub(r"\s+", "", block)
    return result

c, d = labelled_displays(old), labelled_displays(new)
assert c == d
print(f"Preserved {len(d)} labelled display entries after whitespace normalization.")
assert old.count(r"\begin{condition}") == new.count(r"\begin{condition}") == 4
print("Preserved four certificate-condition environments.")
alltex = "\n".join(path.read_text() for path in Path("manuscript/arxiv-v1").rglob("*.tex"))
alllabels = set(labels(alltex))
references = re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", new)
assert not set(references) - alllabels, set(references) - alllabels
print(f"All {len(references)} finite source references have manuscript labels.")
for heading in ["section", "subsection", "subsubsection", "paragraph"]:
    count = len(re.findall(r"\\" + heading + r"\{", new))
    print(f"{heading}: {count}")
subprocess.run(["git", "diff", "--check"], check=True)
print("git diff --check passed.")

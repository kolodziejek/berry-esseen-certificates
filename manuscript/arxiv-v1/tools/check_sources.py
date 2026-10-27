#!/usr/bin/env python3
"""Check manuscript includes, labels, citations and author metadata.

This is a document-integrity check, not mathematical proof verification.
It reads only the manuscript sources and writes its JSON report to stdout.
"""
import collections
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
seen = set()
texts = {}
errors = []


def read_tex(path):
    path = path.resolve()
    if path in seen:
        errors.append("Repeated source include: " + str(path.relative_to(ROOT)))
        return
    seen.add(path)
    if not path.is_file():
        errors.append("Missing source: " + str(path.relative_to(ROOT)))
        return
    source = path.read_text(encoding="utf-8")
    # TeX comments used here contain no escaped-percent corner cases.
    source = re.sub(r"(?<!\\)%[^\n]*", "", source)
    texts[str(path.relative_to(ROOT))] = source
    for target in re.findall(r"\\(?:input|include)\{([^}]+)\}", source):
        child = ROOT / target
        if child.suffix != ".tex":
            child = child.with_suffix(".tex")
        read_tex(child)


read_tex(ROOT / "main.tex")
all_tex = "\n".join(texts.values())
labels = collections.Counter(re.findall(r"\\label\{([^}]+)\}", all_tex))
references = set(re.findall(r"\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}", all_tex))
errors += ["Duplicate label: " + k for k, n in labels.items() if n > 1]
errors += ["Undefined reference: " + k for k in sorted(references - labels.keys())]
bib_files = []
for group in re.findall(r"\\bibliography\{([^}]+)\}", all_tex):
    bib_files.extend(ROOT / (name.strip() + ".bib") for name in group.split(","))
bib_keys = collections.Counter()
for path in bib_files:
    if not path.is_file():
        errors.append("Missing bibliography: " + path.name)
        continue
    bib_keys.update(re.findall(r"@\w+\s*\{\s*([^,]+),", path.read_text()))
citations = set()
for group in re.findall(r"\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}", all_tex):
    citations.update(x.strip() for x in group.split(","))
errors += ["Duplicate bibliography key: " + k for k, n in bib_keys.items() if n > 1]
errors += ["Undefined citation: " + k for k in sorted(citations - bib_keys.keys())]
main = texts.get("main.tex", "")
if "Bartosz Ko{\\l}odziejek" not in main or "Kacper Rodziewicz" not in main:
    errors.append("Author names do not match the requested title page")
if "Bartłomiej" in all_tex or "Bartlomiej" in all_tex:
    errors.append("Incorrect author given name remains")
environments = collections.Counter(re.findall(r"\\begin\{([^}]+)\}", all_tex))
end_environments = collections.Counter(re.findall(r"\\end\{([^}]+)\}", all_tex))
if environments != end_environments:
    errors.append("Unbalanced environment counts")
hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
          for name in sorted(texts)}
report = {"kind": "manuscript_source_integrity", "mathematical_verification": False,
          "tex_files": len(texts), "labels": len(labels),
          "references": len(references), "cited_works": len(citations),
          "bibliography_entries": len(bib_keys), "source_sha256": hashes,
          "errors": errors, "passed": not errors}
print(json.dumps(report, indent=2, ensure_ascii=False))
raise SystemExit(bool(errors))

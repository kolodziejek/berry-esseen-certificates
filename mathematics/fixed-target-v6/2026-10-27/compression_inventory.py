#!/usr/bin/env python3
"""Read-only source/PDF inventory for the compression map. No proof execution."""
from pathlib import Path
import hashlib
import json
import re
import sys
import unicodedata
from pypdf import PdfReader


def normalized(text):
    return re.sub('[^a-z0-9]', '', unicodedata.normalize('NFKD',text).lower())


def main():
    root=Path(__file__).resolve().parents[3]
    pdfs=['manuscript/arxiv-v1/main.pdf',
          'mathematics/strategy-v4/2026-10-27/main.pdf',
          'mathematics/fixed-target-v5/2026-10-27/main.pdf']
    titles=['Keeping the excess term','The joint bound on noise and displacement',
        'Exact half-line smoothing','Four-summand smoothing normalization',
        'Elementary characteristic-function bounds','The smoothing interface',
        'Complete Fourier remainders and finite resource enclosure',
        'One complete low-frequency transfer','The complete high-frequency integral',
        'Turning one defect budget into simultaneous enclosures',
        'Coefficient atlas for the enclosure','Refining a rectangular parameter enclosure',
        'Keeping the score and phase coherent','Three consequences of a signed defect bound',
        'Radius feedback and the final local interface','Finite sequences of enclosure refinements',
        'Confinement and conditional-count witnesses','The conditional-count comparison',
        'The conditional count comparison','Support and local comparisons at indices 40, 41 and 42']
    out={'measurement_scope':'Physical PDF page numbers, one-based. Headings locate starts; neighboring blocks can share a page. No word/line count is a complexity or correctness measure.',
         'pdfs':[],'source_files':[]}
    for name in pdfs:
        path=root/name;r=PdfReader(path);headings=[]
        def walk(xs,level=0):
            for x in xs:
                if isinstance(x,list):walk(x,level+1)
                else:headings.append({'title':x.title,'level':level,'page':r.get_destination_page_number(x)+1})
        walk(r.outline)
        result={'path':name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                'pages':len(r.pages),'bookmarks':headings}
        if name==pdfs[0]:
            pages=[normalized(p.extract_text()) for p in r.pages]
            result['selected_text_matches']={t:[i+1 for i,p in enumerate(pages)
                if i>=2 and normalized(t) in p] for t in titles}
            result['bibliography_start_page']=next(i+1 for i,p in enumerate(r.pages)
                if i>=150 and re.search(r'\bReferences\s*\[1\]',p.extract_text()))
        out['pdfs'].append(result)
    paths=list((root/'manuscript/arxiv-v1/sections').glob('*.tex'))
    paths+=list((root/'manuscript/arxiv-v1/appendices').glob('*.tex'))
    paths+=[root/'manuscript/arxiv-v1/main.tex',
            root/'mathematics/strategy-v4/2026-10-27/excess.tex',
            root/'mathematics/fixed-target-v5/2026-10-27/entry.tex',
            root/'mathematics/fixed-target-v5/2026-10-27/numerical-cover.tex',
            root/'mathematics/fixed-target-v5/2026-10-27/count-cost.tex',
            root/'mathematics/fixed-target-v5/2026-10-27/response-proof/response.tex']
    for path in sorted(paths):
        text=path.read_text();lines=text.splitlines()
        out['source_files'].append({'path':str(path.relative_to(root)),
            'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'lines':len(lines),
            'headings':[{'line':i,'source':line} for i,line in enumerate(lines,1)
                        if re.match(r'\\(?:sub)*section\{|\\paragraph\{',line)]})
    target=Path(sys.argv[1]);target.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':'READ_ONLY_INVENTORY_COMPLETE','pdf_pages':{
        p['path']:p['pages'] for p in out['pdfs']},'source_files':len(out['source_files']),
        'bibliography_start_page':out['pdfs'][0]['bibliography_start_page'],
        'output':str(target)},indent=2))


if __name__=='__main__':
    main()

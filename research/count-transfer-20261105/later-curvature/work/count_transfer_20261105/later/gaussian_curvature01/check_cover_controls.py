"""Source-body and fixed closed-cover controls; no numerical integration."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,ast,hashlib
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import check_two_cells as c
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    c.m.need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'ordinary Python NEW_OUTPUT')
    out=Path(sys.argv[1]);c.m.need(not out.exists(),'fresh output');out.mkdir()
    def body(path,name):
        a=ast.parse(path.read_text());f=[n for n in a.body if isinstance(n,ast.FunctionDef)and n.name==name]
        c.m.need(len(f)==1,'unique analytic function');return ast.dump(ast.Module(body=f[0].body,type_ignores=[]),include_attributes=False)
    c.m.need(body(HERE/'check_full_p.py','check')==body(HERE/'check_two_cells.py','check_cell'),'exact unchanged analytic body')
    c.validate_cover(c.CELLS);rejects=0
    bad=[(),c.CELLS[:1],c.CELLS[::-1],(c.CELLS[0],c.CELLS[0]),((F(19,50),F(77,200)),(F(386,1000),F(39,100))),((F(19,50),F(384,1000)),c.CELLS[1]),((F(19,50),F(77,200)),(F(77,200),F(391,1000))),((.38,.385),(.385,.39))]
    for cells in bad:
        try:c.validate_cover(cells)
        except ValueError:rejects+=1
        else:raise ValueError('invalid fixed cover accepted')
    c.m.need(rejects==8,'all cover substitutions rejected')
    a,c0=c.curvature(39,15,F(19,50),F(77,200),-F(1,100),F(1,100))
    b,c1=c.curvature(39,15,F(77,200),F(39,100),-F(1,100),F(1,100))
    c.m.need(a>0 and b==0,'positive-numerator and negative-numerator branches both exercised')
    result=dict(status='PASS_EXACT_FIXED_COVER_AND_ANALYTIC_BODY_CONTROLS',unchanged_analytic_body=True,malformed_cover_rejections=rejects,curvature_branches=[c0,c1],reader_sha256=sha(HERE/'check_two_cells.py'),source_sha256=sha(__file__),no_new_numeric_campaign=True)
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()

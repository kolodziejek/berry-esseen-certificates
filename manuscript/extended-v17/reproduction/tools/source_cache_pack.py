"""Deterministic source-only blob packs and safe create-or-verify rehydration.

Inventory: {"caches":[{"path":"workspace/relative/cache","entries":{
"relative/file":{"sha256":"64 lower hex","bytes":123}}}]}.
All source files are read and hashed. No saved arithmetic result is promoted.
The restore command requires both archive and manifest SHA256 from a trusted
release manifest; it never extracts archive paths directly.
"""
from pathlib import Path,PurePosixPath
import argparse,gzip,hashlib,io,json,os,re,tarfile,time
MAX_FILE=256*1024**2

def need(value,message):
 if not value:raise ValueError(message)
def sha(data):return hashlib.sha256(data).hexdigest()
def unique(pairs):
 result={}
 for k,v in pairs:need(k not in result,'Duplicate JSON key');result[k]=v
 return result
def parsed(raw):return json.loads(raw,object_pairs_hook=unique)
def encoded(value):return(json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()
def parts(value):
 need(type(value)is str and value and '\\'not in value and '\0'not in value,'Ordinary POSIX relative name')
 p=PurePosixPath(value);need(p.parts and not p.is_absolute() and p.as_posix()==value and all(x not in ('.','..')for x in p.parts),'Canonical contained relative name')
 return p.parts
def pin(value):
 need(type(value)is dict and set(value)=={'sha256','bytes'} and type(value['sha256'])is str
  and re.fullmatch('[0-9a-f]{64}',value['sha256']) and type(value['bytes'])is int
  and 0<=value['bytes']<=MAX_FILE,'Exact bounded static source pin')
def ordinary(path):
 p=Path(path)
 for x in (p,*p.parents):need(not x.is_symlink(),'No symlink in source or destination ancestry')
 return p

def build(workspace,inventory,output):
 workspace=ordinary(Path(workspace).resolve());output=ordinary(Path(output).absolute())
 need(not output.exists(),'Create-only output directory');output.mkdir(parents=True)
 value=parsed(Path(inventory).read_bytes());need(type(value['caches'])is list and value['caches'],'Nonempty explicit cache inventory')
 trees={};blobs={}
 for row in value['caches']:
  name=row['path'];parts(name);need(name not in trees,'Unique complete source tree')
  entries=row['entries'];need(type(entries)is dict and entries,'Complete nonempty source tree')
  root=ordinary(workspace.joinpath(*parts(name)));actual={p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()}
  need(actual==set(entries),'Inventory is every source file, not a selected subset')
  for relative,meta in entries.items():
   parts(relative);pin(meta);p=ordinary(root.joinpath(*parts(relative)));need(p.is_file(),'Regular source input')
   data=p.read_bytes();need(len(data)==meta['bytes'] and sha(data)==meta['sha256'],'Whole immutable source bytes')
   if meta['sha256']in blobs:need(blobs[meta['sha256']][1]==len(data),'Consistent content-addressed length')
   else:blobs[meta['sha256']]=(p,len(data))
  trees[name]=entries
 manifest={'schema':'BE_STATIC_SOURCE_CACHE_BLOBS_V2','trees':trees,'blobs':{h:{'bytes':v[1]}for h,v in blobs.items()},
  'mathematical_acceptance_claimed':False,'historical_static_candidates_are_untrusted_inputs':True}
 raw=encoded(manifest);(output/'MANIFEST.json').write_bytes(raw)
 def add(tar,name,data):
  info=tarfile.TarInfo(name);info.size=len(data);info.mode=0o644;info.mtime=0;info.uid=info.gid=0;info.uname=info.gname='';tar.addfile(info,io.BytesIO(data))
 archive=output/'static-sources.tar.gz';tick=time.monotonic()
 with archive.open('xb')as f,gzip.GzipFile(filename='',fileobj=f,mode='wb',mtime=0,compresslevel=6)as gz,tarfile.open(fileobj=gz,mode='w|',format=tarfile.PAX_FORMAT)as tar:
  add(tar,'MANIFEST.json',raw)
  for h,(path,size)in sorted(blobs.items()):
   data=path.read_bytes();need(len(data)==size and sha(data)==h,'Source stable during pack construction');add(tar,'blobs/'+h,data)
 result={'schema':'BE_STATIC_SOURCE_PACK_RESULT_V2','archive':str(archive),'archive_bytes':archive.stat().st_size,
  'archive_sha256':sha(archive.read_bytes()),'manifest_sha256':sha(raw),'trees':len(trees),'logical_files':sum(len(x)for x in trees.values()),
  'unique_blobs':len(blobs),'unique_uncompressed_blob_bytes':sum(v[1]for v in blobs.values()),'elapsed_seconds':time.monotonic()-tick,
  'tool_sha256':sha(Path(__file__).read_bytes()),'arithmetic_acceptance_claimed':False}
 (output/'RESULT.json').write_bytes(encoded(result));return result

def restore(archive,archive_sha,manifest_sha,workspace):
 archive=ordinary(Path(archive).absolute());workspace=ordinary(Path(workspace).absolute())
 need(sha(archive.read_bytes())==archive_sha,'Trusted complete archive SHA256')
 workspace.mkdir(parents=True,exist_ok=True);seen=set();created=verified=0
 with tarfile.open(archive,'r:gz')as tar:
  members=iter(tar);first=next(members,None);need(first is not None and first.name=='MANIFEST.json' and first.isfile() and first.size<=32*1024**2,
   'One leading bounded regular manifest')
  raw=tar.extractfile(first).read();need(sha(raw)==manifest_sha,'Trusted whole manifest SHA256')
  m=parsed(raw);need(type(m)is dict and set(m)=={'schema','trees','blobs','mathematical_acceptance_claimed','historical_static_candidates_are_untrusted_inputs'}
   and m['schema']=='BE_STATIC_SOURCE_CACHE_BLOBS_V2' and m['mathematical_acceptance_claimed']is False
   and m['historical_static_candidates_are_untrusted_inputs']is True,'Literal source-only manifest scope')
  need(type(m['trees'])is dict and m['trees'] and type(m['blobs'])is dict,'Complete explicit source namespaces')
  destinations={}
  for name,entries in m['trees'].items():
   root=ordinary(workspace.joinpath(*parts(name)));need(type(entries)is dict and entries,'Nonempty exact tree')
   if root.exists():need({p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()}<=set(entries),'No unlisted files in existing target tree')
   for relative,meta in entries.items():
    parts(relative);pin(meta);need(m['blobs'].get(meta['sha256'])=={'bytes':meta['bytes']},'Complete blob size binding')
    dest=ordinary(root.joinpath(*parts(relative)));destinations.setdefault(meta['sha256'],[]).append((dest,meta['bytes']))
  need(set(destinations)==set(m['blobs']),'No missing or unused source blob')
  for member in members:
   need(member.isfile() and member.name.startswith('blobs/') and len(member.name)==70,'Regular closed blob entry')
   h=member.name[6:];need(h in destinations and h not in seen,'Every and only unique declared blob')
   seen.add(h);size=m['blobs'][h]['bytes'];need(member.size==size<=MAX_FILE,'Exact bounded blob length')
   data=tar.extractfile(member).read();need(len(data)==size and sha(data)==h,'Complete source blob hash')
   for dest,_ in destinations[h]:
    ordinary(dest);dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists():need(dest.is_file() and dest.read_bytes()==data,'Refuse differing existing source');verified+=1
    else:
     with dest.open('xb')as f:f.write(data)
     os.chmod(dest,0o644)
     created+=1
  need(seen==set(m['blobs']),'No omitted source blob')
 return {'schema':'BE_STATIC_SOURCE_REHYDRATION_V2','workspace':str(workspace),'archive_sha256':archive_sha,
  'manifest_sha256':manifest_sha,'trees':len(m['trees']),'unique_blobs':len(seen),'created_files':created,'verified_existing_files':verified,
  'arithmetic_acceptance_claimed':False,'tool_sha256':sha(Path(__file__).read_bytes())}

def main():
 p=argparse.ArgumentParser();sub=p.add_subparsers(dest='action',required=True)
 b=sub.add_parser('build');b.add_argument('--workspace',type=Path,required=True);b.add_argument('--inventory',type=Path,required=True);b.add_argument('--output',type=Path,required=True)
 r=sub.add_parser('restore');r.add_argument('--archive',type=Path,required=True);r.add_argument('--sha256',required=True);r.add_argument('--manifest-sha256',required=True);r.add_argument('--workspace',type=Path,required=True)
 a=p.parse_args();need(__debug__,'Assertions required')
 result=build(a.workspace,a.inventory,a.output)if a.action=='build'else restore(a.archive,a.sha256,a.manifest_sha256,a.workspace)
 print(json.dumps(result,sort_keys=True),flush=True)
if __name__=='__main__':main()

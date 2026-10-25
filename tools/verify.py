import re, os, json, glob, sys
from html.parser import HTMLParser
OUT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files=[f for f in glob.glob(OUT+'/**/*.html',recursive=True) if '/node_modules/' not in f]
def url_of(f):
    r=os.path.relpath(f,OUT)[:-5]
    return '/' if r=='index' else '/'+r
exist={url_of(f) for f in files}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.h=[]; s.imgs=[]; s.links=[]; s.ids=set(); s._cur=None; s.title='';s.in_title=False; s.meta={}; s.canon=None; s.ld=[]; s.in_ld=False
    def handle_starttag(s,t,a):
        a=dict(a)
        if t in('h1','h2','h3','h4','h5','h6'): s._cur=[t,'']; s.h.append(s._cur)
        if t=='img': s.imgs.append(a)
        if t=='a' and 'href' in a: s.links.append(a['href'])
        if 'id' in a: s.ids.add(a['id'])
        if t=='title': s.in_title=True
        if t=='meta' and 'name' in a: s.meta[a['name']]=a.get('content','')
        if t=='link' and a.get('rel')=='canonical': s.canon=a['href']
        if t=='script' and a.get('type')=='application/ld+json': s.in_ld=True; s.ld.append('')
    def handle_endtag(s,t):
        if t in('h1','h2','h3','h4','h5','h6'): s._cur=None
        if t=='title': s.in_title=False
        if t=='script': s.in_ld=False
    def handle_data(s,d):
        if s._cur is not None: s._cur[1]+=d
        if s.in_title: s.title+=d
        if s.in_ld: s.ld[-1]+=d
errs=[]; titles={}; descs={}; kws={}
pages={}
for f in sorted(files):
    u=url_of(f); p=P(); p.feed(open(f).read()); pages[u]=p
for u,p in pages.items():
    hs=p.h; n1=[h for h in hs if h[0]=='h1']
    if len(n1)!=1: errs.append(f'{u}: {len(n1)} h1')
    prev=0
    for t,_ in hs:
        l=int(t[1])
        if prev and l>prev+1: errs.append(f'{u}: heading skip h{prev}->h{l}')
        prev=l
    for im in p.imgs:
        if not im.get('alt','').strip(): errs.append(f'{u}: img no alt {im.get("src")}')
        if not im.get('width') or not im.get('height'): errs.append(f'{u}: img no dims {im.get("src")}')
        src=im.get('src','')
        if src.startswith('/') and not os.path.exists(OUT+src): errs.append(f'{u}: missing img {src}')
    for l in p.links:
        if l.startswith(('http','tel:','mailto:')): continue
        path,_,frag=l.partition('#')
        path=path or u
        if path not in exist and not os.path.exists(OUT+path): errs.append(f'{u}: broken link {l}')
        elif frag and path in pages and frag not in pages[path].ids: errs.append(f'{u}: missing anchor {l}')
    for b in p.ld:
        try: json.loads(b)
        except Exception as e: errs.append(f'{u}: bad jsonld {e}')
    if u!='/404':
        exp='https://www.aquapress.pe'+('/' if u=='/' else u)
        if p.canon!=exp: errs.append(f'{u}: canonical {p.canon} != {exp}')
        titles.setdefault(p.title,[]).append(u); descs.setdefault(p.meta.get('description'),[]).append(u); kws.setdefault(p.meta.get('keywords'),[]).append(u)
        if len(p.title)>60: errs.append(f'{u}: title {len(p.title)}')
        if len(p.meta.get('description',''))>155: errs.append(f'{u}: desc {len(p.meta["description"])}')
for name,d in (('title',titles),('desc',descs),('keywords',kws)):
    for k,v in d.items():
        if len(v)>1: errs.append(f'duplicate {name}: {v}')
sm=open(OUT+'/sitemap.xml').read()
locs=set(re.findall(r'<loc>https://www.aquapress.pe(.*?)</loc>',sm))
want={u for u in exist if u!='/404'}
locs={('/' if l=='/' else l) for l in locs}
if locs!=want: errs.append(f'sitemap mismatch: {locs^want}')
print('pages:',len(pages)); print('\n'.join(errs) if errs else 'ALL CHECKS PASSED')
if '--outline' in sys.argv:
    for u in ('/','/tintoreria-lavado-al-seco','/lavanderia-miraflores','/blog/cada-cuanto-lavar-un-edredon'):
        print('\n',u); [print('  '*(int(t[1])-1),t,re.sub(r'\s+',' ',x).strip()) for t,x in pages[u].h]

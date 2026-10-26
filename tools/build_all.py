import os, shutil, json
from lib import *
import pages_core as core
import pages_rest as rest

# shared assets (CSS minified; both files versioned by content hash for long-term caching)
import re, hashlib
def minify(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r' ?([{};,]) ?', r'\1', css)
    css = css.replace(';}', '}')
    return css.strip()
css = minify(open(os.path.join(HERE,'base.css')).read() + '\n' + open(os.path.join(HERE,'extra.css')).read())
js = open(os.path.join(HERE,'main.js')).read()
os.makedirs(OUT+'/assets', exist_ok=True)
open(OUT+'/assets/styles.css','w').write(css)
open(OUT+'/assets/main.js','w').write(js)
import lib
lib.ASSET_V = hashlib.sha1((css + js).encode()).hexdigest()[:8]
print('assets v', lib.ASSET_V, 'css', round(len(css)/1024,1), 'KB')

import pages_new as new
pages = [core.home(), core.lavado(), core.tintoreria(), core.edredones(), core.recojo(),
         new.alfombras(), new.zapatillas(), new.vestidos(), new.ternos(),
         rest.san_borja(), rest.surquillo(), rest.miraflores(), rest.blog_index()]
pages += [rest.post(p) for p in rest.POSTS]
pages.append(rest.not_found())
for path, html in pages:
    fp = write(path, html)
    print(f'{path:55s} {len(html)/1024:6.1f} KB')

# sitemap (404 excluded)
prio = {'/':('1.0','weekly')}
for p,_ in SERVICES: prio[p]=('0.9','monthly')
for p in ['/lavanderia-san-borja','/lavanderia-surquillo','/lavanderia-miraflores']: prio[p]=('0.8','monthly')
prio['/blog']=('0.8','weekly')
for q in rest.POSTS: prio['/blog/'+q['slug']]=('0.7','monthly')
urls=''.join(f'  <url>\n    <loc>{DOMAIN}{p if p!="/" else "/"}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>\n  </url>\n' for p,(pr,cf) in prio.items())
open(OUT+'/sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open(OUT+'/robots.txt','w').write(f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n')
open(OUT+'/site.webmanifest','w').write(json.dumps({
  'name':'Aquapress Lavandería','short_name':'Aquapress','lang':'es-PE','start_url':'/','display':'browser',
  'theme_color':'#00AEEF','background_color':'#FBF9F6',
  'icons':[{'src':'/images/favicon-192.png','sizes':'192x192','type':'image/png'},{'src':'/images/favicon-512.png','sizes':'512x512','type':'image/png'}]
}, ensure_ascii=False, indent=2)+'\n')
IMMUTABLE = 'public, max-age=31536000, immutable'
open(OUT+'/vercel.json','w').write(json.dumps({
  'cleanUrls': True, 'trailingSlash': False,
  'redirects':[{'source':'/index.html','destination':'/','permanent':True}],
  'headers':[
    {'source':'/assets/(.*)','headers':[{'key':'Cache-Control','value':IMMUTABLE}]},
    {'source':'/fonts/(.*)','headers':[{'key':'Cache-Control','value':IMMUTABLE}]},
    {'source':'/images/(.*)','headers':[{'key':'Cache-Control','value':'public, max-age=604800, stale-while-revalidate=86400'}]},
    {'source':'/(.*)','headers':[{'key':'X-Content-Type-Options','value':'nosniff'},{'key':'Referrer-Policy','value':'strict-origin-when-cross-origin'}]},
  ]
}, indent=2)+'\n')
print('sitemap urls:', len(prio))

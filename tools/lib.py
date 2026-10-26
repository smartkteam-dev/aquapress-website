import json, os
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DOMAIN = 'https://www.aquapress.pe'
TEL = '+51974726537'
TEL_FMT = '+51 974 726 537'
FB = 'https://www.facebook.com/AquaPressPeru/'
MAPS = 'https://maps.app.goo.gl/ToATP6guWhEyAwJF9'
OG_IMG = '/images/og-aquapress-lavanderia-tintoreria-san-isidro.png'
OG_ALT = 'Aquapress Lavandería: lavandería y tintorería en San Isidro, Lima'
TODAY = '2026-10-25'
YEAR = '2026'
ASSET_V = ''  # set by build_all (content hash of CSS/JS)

WA_ICON = open(os.path.join(HERE, 'wa_icon.svg')).read()
WA_FLOAT_SVG = open(os.path.join(HERE, 'wa_float.snippet')).read()
import re
WA_FLOAT_SVG = re.search(r'<svg.*?</svg>', WA_FLOAT_SVG, re.S).group(0)


def wa(text='Hola, quisiera información sobre sus servicios'):
    return 'https://wa.me/51974726537?text=' + quote(text)


# (slug path, short label, full label)
SERVICES = [
    ('/lavado-al-peso-y-por-prenda', 'Lavado al peso y por prenda'),
    ('/tintoreria-lavado-al-seco', 'Tintorería y lavado al seco'),
    ('/lavado-de-ternos-y-corbatas', 'Ternos y corbatas'),
    ('/lavado-de-edredones-y-ropa-de-cama', 'Edredones y ropa de cama'),
    ('/lavado-de-alfombras-y-cortinas', 'Alfombras y cortinas'),
    ('/lavado-de-zapatillas', 'Zapatillas'),
    ('/lavado-de-vestidos-de-novia-y-fiesta', 'Vestidos de novia y de fiesta'),
    ('/recojo-a-domicilio-lavanderia', 'Recojo a domicilio'),
]

# Nav groups (label, [(path, label)]). Each group is its own dropdown in the top bar.
NAV_GROUPS = [
    ('Ropa diaria', [
        ('/lavado-al-peso-y-por-prenda', 'Lavado al peso y por prenda'),
        ('/lavado-de-zapatillas', 'Zapatillas'),
    ]),
    ('Ropa formal', [
        ('/lavado-de-ternos-y-corbatas', 'Ternos y corbatas'),
        ('/lavado-de-vestidos-de-novia-y-fiesta', 'Vestidos de novia y de fiesta'),
        ('/tintoreria-lavado-al-seco', 'Tintorería y lavado al seco'),
    ]),
    ('Hogar', [
        ('/lavado-de-edredones-y-ropa-de-cama', 'Edredones y ropa de cama'),
        ('/lavado-de-alfombras-y-cortinas', 'Alfombras y cortinas'),
    ]),
]
NAV_RECOJO = ('/recojo-a-domicilio-lavanderia', 'Recojo a domicilio')
# Pickup dropdown: how it works, the pickup districts, and the local
NAV_RECOJO_ITEMS = [
    (NAV_RECOJO[0], 'Cómo funciona el recojo'),
    ('/lavanderia-san-borja', 'Recojo en San Borja'),
    ('/lavanderia-surquillo', 'Recojo en Surquillo'),
    ('/lavanderia-miraflores', 'Recojo en Miraflores'),
    ('/#local', 'Nuestro local en San Isidro'),
]

# Flat list in group order, used by the footer.
NAV_SERVICES = [item for _, items in NAV_GROUPS for item in items] + [NAV_RECOJO]

# Founding year (confirmed by the owner); used in schema, footer and the home FAQ
FOUNDED = 2013
YEARS = int(YEAR) - FOUNDED
YEARS_TEXT = f'más de {YEARS // 5 * 5} años' if YEARS >= 10 else f'{YEARS} años'

# Icon paths (24x24 viewBox, 1.8 stroke), shared by service cards, art panels and blog covers
ICON_PATHS = {
    'peso': '<circle cx="12" cy="5" r="3"/><path d="M6.5 8a2 2 0 0 0-1.905 1.46L2.1 18.5A2 2 0 0 0 4 21h16a2 2 0 0 0 1.925-2.54L19.4 9.5A2 2 0 0 0 17.48 8Z"/>',
    'prenda': '<path d="M20.38 3.46 16 2a4 4 0 0 1-8 0L3.62 3.46a2 2 0 0 0-1.34 2.23l.58 3.47a1 1 0 0 0 .99.84H6v10c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V10h2.15a1 1 0 0 0 .99-.84l.58-3.47a2 2 0 0 0-1.34-2.23z"/>',
    'seco': '<path d="M12 11v-.7c0-.9.7-1.4 1.5-1.8a2.6 2.6 0 1 0-4-2.3"/><path d="M12 11 3.1 16.5a1.5 1.5 0 0 0 .8 2.8h16.2a1.5 1.5 0 0 0 .8-2.8L12 11z"/>',
    'terno': '<path d="M10 2.5h4l-.9 4h-2.2z"/><path d="M10.9 6.5 8.2 18.6 12 21.5l3.8-2.9-2.7-12.1"/>',
    'cama': '<path d="M2 20v-8a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v8"/><path d="M4 10V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v4"/><path d="M12 4v6"/><path d="M2 18h20"/>',
    'cortinas': '<path d="M3 4h18"/><path d="M5 4v16h4.5c-2.2-3.4-3.3-9.3-3.5-16"/><path d="M19 4v16h-4.5c2.2-3.4 3.3-9.3 3.5-16"/>',
    'alfombra': '<rect x="3" y="6" width="18" height="12" rx="1.5"/><path d="M7 6v12M17 6v12"/><path d="M12 9l2 3-2 3-2-3z"/><path d="M3 9H1.5M3 15H1.5M21 9h1.5M21 15h1.5"/>',
    'zapatilla': '<path d="M3 16.5v-3.2a2 2 0 0 1 1-1.7L8 9.5l2 2 3.2-1 4.3 3.2c1.3 1 2.9 1.4 3.5 1.6v1.2a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M3 17h18"/><path d="M8 9.5l1.4 2.3M11 11l1 1.7"/>',
    'vestido': '<path d="M9 2l-.6 6c0 1.4-.9 2.4-2.1 3.2L4 21h16l-2.3-9.8C16.5 10.4 15.6 9.4 15.6 8L15 2"/><path d="M8.4 8h7.2"/>',
    'gem': '<path d="M6 3h12l4 6-10 13L2 9z"/><path d="M11 3 8 9l4 13 4-13-3-6"/><path d="M2 9h20"/>',
    'recojo': '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
}


def icon_wrap(key):
    return (f'<div class="service-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON_PATHS[key]}</svg></div>')
DISTRICTS = [
    ('/', 'San Isidro'),
    ('/lavanderia-san-borja', 'San Borja'),
    ('/lavanderia-surquillo', 'Surquillo'),
    ('/lavanderia-miraflores', 'Miraflores'),
]

IMG_DIMS = {
    'prendas-lana-tejidos-delicados': (800, 600),
}


SIZES = {
    'mosaic': '(min-width:1025px) 215px, 50vw',
    'mosaicwide': '(min-width:1025px) 440px, 100vw',
    'grid': '(min-width:1025px) 270px, 50vw',
    'gridwide': '(min-width:1025px) 550px, 100vw',
    'page': '(min-width:1025px) 440px, (min-width:769px) 560px, 92vw',
    'post': '(min-width:1000px) 960px, 94vw',
    'thumb': '(min-width:1025px) 360px, (min-width:769px) 46vw, 92vw',
    'split': '(min-width:1025px) 520px, (min-width:769px) 44vw, 92vw',
    'card': '(min-width:1025px) 360px, (min-width:769px) 46vw, 92vw',
}


def img(name, alt, cls='', eager=False, ctx=None, big=False, w=None, h=None):
    """Responsive WebP: 400w / 800w (/ 1200w). eager = above-the-fold, high priority."""
    if w is None:
        w, h = IMG_DIMS.get(name, (800, 534))
    ctx = ctx or ('page' if eager else 'grid')
    srcset = f'/images/{name}-400.webp 400w, /images/{name}.webp 800w'
    if big:
        srcset += f', /images/{name}-1200.webp 1200w'
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return (f'<img src="/images/{name}.webp" srcset="{srcset}" sizes="{SIZES[ctx]}" alt="{alt}" '
            f'width="{w}" height="{h}" {load}{c} />')


# ---------------------------------------------------------------- schema
def biz_node():
    return {
        '@type': 'DryCleaningOrLaundry',
        '@id': DOMAIN + '/#negocio',
        'name': 'Aquapress Lavandería',
        'description': 'Lavandería y tintorería en San Isidro, Lima, con recojo a domicilio en San Borja, Surquillo y Miraflores. Lavado al peso, lavado por prenda, tintorería, planchado y ropa de cama.',
        'url': DOMAIN + '/',
        'telephone': TEL,
        'image': [DOMAIN + OG_IMG, DOMAIN + '/images/lavadoras-industriales-acero.webp'],
        'logo': DOMAIN + '/images/favicon-512.png',
        'foundingDate': str(FOUNDED),
        'priceRange': '$$',
        'currenciesAccepted': 'PEN',
        'paymentAccepted': 'Cash, Credit Card, Debit Card, Bank Transfer',
        'address': {
            '@type': 'PostalAddress',
            'streetAddress': 'Av. del Parque Sur 193',
            'addressLocality': 'San Isidro',
            'addressRegion': 'Lima',
            'postalCode': '15036',
            'addressCountry': 'PE',
        },
        'geo': {'@type': 'GeoCoordinates', 'latitude': -12.1022785, 'longitude': -77.0157705},
        'hasMap': MAPS,
        'openingHoursSpecification': [{
            '@type': 'OpeningHoursSpecification',
            'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            'opens': '07:30', 'closes': '20:00',
        }],
        'areaServed': [
            {'@type': 'AdministrativeArea', 'name': 'San Isidro'},
            {'@type': 'AdministrativeArea', 'name': 'San Borja'},
            {'@type': 'AdministrativeArea', 'name': 'Surquillo'},
            {'@type': 'AdministrativeArea', 'name': 'Miraflores'},
            {'@type': 'City', 'name': 'Lima'},
        ],
        'sameAs': [FB],
        'serviceType': ['Lavado al peso', 'Lavado por prenda', 'Tintorería', 'Lavado al seco', 'Planchado', 'Lavado de edredones', 'Lavado de alfombras', 'Lavado de cortinas', 'Lavado de zapatillas', 'Lavado de vestidos de novia', 'Servicio express', 'Recojo a domicilio'],
    }


def breadcrumb_node(trail):
    """trail: list of (name, path) from Inicio to current."""
    return {
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': DOMAIN + (p if p != '/' else '/')}
            for i, (n, p) in enumerate(trail)
        ],
    }


def faq_node(faqs):
    return {
        '@type': 'FAQPage',
        'mainEntity': [
            {'@type': 'Question', 'name': q,
             'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}}
            for q, a in faqs
        ],
    }


def strip_tags(s):
    return re.sub(r'<[^>]+>', '', s).replace('&amp;', '&')


def service_node(name, desc, path, service_type):
    return {
        '@type': 'Service',
        'name': name,
        'description': desc,
        'serviceType': service_type,
        'url': DOMAIN + path,
        'provider': {'@id': DOMAIN + '/#negocio'},
        'areaServed': [{'@type': 'AdministrativeArea', 'name': n} for n in ('San Isidro', 'San Borja', 'Surquillo', 'Miraflores')],
    }


# ---------------------------------------------------------------- chrome
def nav_html():
    def sub_links(items):
        return ''.join('<a href="%s">%s</a>' % (p, l) for p, l in items)
    groups = ''.join(
        f'<div class="has-sub"><a href="{items[0][0]}">{g} <span class="caret" aria-hidden="true"></span></a>'
        f'<div class="sub">{sub_links(items)}</div></div>'
        for g, items in NAV_GROUPS)
    groups += (f'<div class="has-sub"><a href="{NAV_RECOJO[0]}">{NAV_RECOJO[1]} <span class="caret" aria-hidden="true"></span></a>'
               f'<div class="sub">{sub_links(NAV_RECOJO_ITEMS)}</div></div>')
    m_svc = ''.join(
        f'<div class="mobile-group">{g}</div>' + ''.join(f'<a href="{p}" class="mobile-link">{l}</a>' for p, l in items)
        for g, items in NAV_GROUPS)
    m_svc += f'<div class="mobile-group">{NAV_RECOJO[1]}</div>' + ''.join(
        f'<a href="{p}" class="mobile-link">{l}</a>' for p, l in NAV_RECOJO_ITEMS)
    return f'''<div id="top-sentinel" aria-hidden="true"></div>
<a class="skip-link" href="#content">Saltar al contenido</a>
<nav id="main-nav" aria-label="Navegación principal">
  <div class="container nav-inner">
    <a href="/" class="nav-logo"><img src="/images/aquapress-logo.png" alt="Aquapress Lavandería, lavandería y tintorería en San Isidro" width="339" height="108" class="logo-nav" fetchpriority="high" /></a>
    <div class="nav-links">
      {groups}
      <a href="/blog">Blog</a>
    </div>
    <div class="nav-cta">
      <a href="tel:{TEL}" class="btn btn-outline btn-sm">Llamar</a>
      <a href="{wa()}" class="btn btn-primary btn-sm" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </div>
    <button class="hamburger" id="ham-btn" aria-label="Abrir menú" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
  </div>
</nav>

<div class="mobile-menu" id="mobile-menu">
  {m_svc}
  <a href="/blog" class="mobile-link">Blog</a>
  <a href="tel:{TEL}" class="btn btn-outline" style="margin-top:12px;">Llamar</a>
  <a href="{wa()}" class="btn btn-wa" target="_blank" rel="noopener noreferrer">WhatsApp</a>
</div>'''


def footer_html():
    svc = ''.join(f'<li><a href="{p}">{l}</a></li>' for p, l in NAV_SERVICES)
    zon = ''.join(f'<li><a href="{p}">{"Nuestro local en San Isidro" if p == "/" else "Recojo en " + l}</a></li>' for p, l in DISTRICTS)
    return f'''<footer>
  <div class="container">
    <div class="footer-top">
      <div class="footer-logo-wrap">
        <div class="footer-logo-box">
          <img src="/images/aquapress-logo.png" alt="Aquapress Lavandería" width="339" height="108" class="logo-footer" loading="lazy" />
        </div>
        <p class="footer-tagline">Lavandería y tintorería <br/>en San Isidro, Lima. Desde {FOUNDED}.</p>
      </div>
      <div class="footer-social-wrap">
        <a href="{FB}" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Aquapress en Facebook">
          <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
        </a>
      </div>
    </div>

    <div class="footer-cols">
      <nav class="footer-col" aria-label="Servicios">
        <p class="footer-h">Servicios</p>
        <ul>{svc}</ul>
      </nav>
      <nav class="footer-col" aria-label="Zonas de atención">
        <p class="footer-h">Cobertura</p>
        <ul>{zon}</ul>
      </nav>
      <div class="footer-col">
        <p class="footer-h">Contacto</p>
        <ul>
          <li><a href="tel:{TEL}">{TEL_FMT}</a></li>
          <li><a href="{wa('Hola, quisiera información')}" target="_blank" rel="noopener noreferrer">WhatsApp</a></li>
          <li><a href="{FB}" target="_blank" rel="noopener noreferrer">Facebook</a></li>
          <li><a href="/blog">Blog de cuidado de ropa</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <p class="footer-h">Ubicación y horario</p>
        <ul>
          <li><a href="/#local">Av. del Parque Sur 193</a></li>
          <li><a href="/#local">San Isidro, Lima, Perú</a></li>
        </ul>
        <div class="footer-hours">
          <p>Lun – Sáb: 7:30 AM – 8:00 PM</p>
          <p style="color:var(--mist);">Domingos: Cerrado</p>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <p>&copy; {YEAR} Aquapress Lavandería. Todos los derechos reservados.</p>
      <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;justify-content:flex-end;">
        <p style="font-size:.88rem;color:rgba(255,255,255,.5);">San Isidro, Lima, Perú</p>
        <p style="color:rgba(255,255,255,.2);">|</p>
        <p style="font-size:.88rem;color:rgba(255,255,255,.5);">Diseñado por <a href="https://smartkteam.com" target="_blank" rel="noopener noreferrer nofollow" class="credit-link">Smart KTeam</a> · Seattle, USA</p>
      </div>
    </div>
  </div>
</footer>

<div class="wa-float">
  <div class="wa-pulse"></div>
  <a href="{wa()}" class="wa-btn" target="_blank" rel="noopener noreferrer" aria-label="Escribir a Aquapress por WhatsApp">
    {WA_FLOAT_SVG}
  </a>
</div>'''


def crumbs_html(trail):
    items = []
    for i, (n, p) in enumerate(trail):
        if i == len(trail) - 1:
            items.append(f'<li><span aria-current="page">{n}</span></li>')
        else:
            items.append(f'<li><a href="{p}">{n}</a></li>')
    return f'<nav class="crumbs" aria-label="Ruta de navegación"><div class="container"><ol>{"".join(items)}</ol></div></nav>'


# ---------------------------------------------------------------- page
def page(path, title, desc, keywords, body, graph, og_image=OG_IMG, og_alt=OG_ALT,
         og_type='website', robots='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1',
         extra_head=''):
    assert len(title) <= 60, (path, len(title), title)
    assert len(desc) <= 155, (path, len(desc), desc)
    url = DOMAIN + (path if path != '/' else '/')
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':'))
    og_abs = DOMAIN + og_image if og_image.startswith('/') else og_image
    ow, oh = (1200, 630) if og_image == OG_IMG else (1200, 630)
    html = f'''<!DOCTYPE html>
<html lang="es-PE">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{keywords}" />
  <meta name="author" content="Aquapress Lavandería" />
  <meta name="robots" content="{robots}" />
  <link rel="canonical" href="{url}" />
  <link rel="alternate" hreflang="es-PE" href="{url}" />
  <link rel="alternate" hreflang="x-default" href="{url}" />
  <meta name="theme-color" content="#00AEEF" />
  <meta name="geo.region" content="PE-LIM" />
  <meta name="geo.placename" content="San Isidro, Lima" />
  <meta name="geo.position" content="-12.1022785;-77.0157705" />
  <meta name="ICBM" content="-12.1022785, -77.0157705" />
  <meta name="format-detection" content="telephone=yes" />
  <link rel="icon" href="/favicon.ico" sizes="48x48" />
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16.png" />
  <link rel="icon" type="image/png" href="/favicon.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/images/favicon-180.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:locale" content="es_PE" />
  <meta property="og:site_name" content="Aquapress Lavandería" />
  <meta property="og:image" content="{og_abs}" />
  <meta property="og:image:width" content="{ow}" />
  <meta property="og:image:height" content="{oh}" />
  <meta property="og:image:alt" content="{og_alt}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{og_abs}" />
  <meta name="twitter:image:alt" content="{og_alt}" />{extra_head}
  <script type="application/ld+json">{ld}</script>
  <script>document.documentElement.className+=' js'</script>
  <link rel="preload" href="/fonts/nunito-sans-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="/fonts/playfair-display-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="/assets/styles.css?v={ASSET_V}" />
</head>
<body>
{nav_html()}

<main id="content">
{body}
</main>

{footer_html()}

<script src="/assets/main.js?v={ASSET_V}" defer></script>
</body>
</html>
'''
    return html


def write(path, html):
    if path == '/':
        fp = os.path.join(OUT, 'index.html')
    else:
        fp = os.path.join(OUT, path.strip('/') + '.html')
        os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, 'w').write(html)
    return fp


# ---------------------------------------------------------------- blocks
def btns(wa_text, call=True, light=False):
    cls_call = 'btn btn-outline-light' if light else 'btn btn-outline'
    cls_wa = 'btn btn-white' if light else 'btn btn-primary'
    icon = '' if light else WA_ICON
    c = f'<a href="tel:{TEL}" class="{cls_call}">{TEL_FMT}</a>' if call else ''
    return f'<a href="{wa(wa_text)}" class="{cls_wa}" target="_blank" rel="noopener noreferrer">{icon}Consultar por WhatsApp</a>{c}'


def faq_section(faqs, title='Preguntas frecuentes', lead=None, bg='sec-linen'):
    items = ''.join(f'<div class="faq-item fade-up"><h3>{q}</h3><p>{a}</p></div>' for q, a in faqs)
    lead_html = f'<p class="lead">{lead}</p>' if lead else ''
    return f'''<section class="section {bg}" id="preguntas-frecuentes">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Dudas comunes</span><h2 class="h2">{title}</h2>{lead_html}</div>
    <div class="faq-list">{items}</div>
  </div>
</section>'''


def cta_band(title, text, wa_text):
    return f'''<section class="cta-band">
  <div class="bg-blob a"></div><div class="bg-blob b"></div>
  <div class="container fade-up" style="position:relative;z-index:2;">
    <h2 class="h2">{title}</h2>
    <p>{text}</p>
    <div class="cta-buttons">
      <a href="{wa(wa_text)}" class="btn btn-white" target="_blank" rel="noopener noreferrer">Consultar por WhatsApp</a>
      <a href="tel:{TEL}" class="btn btn-outline-light">Llamar ahora</a>
    </div>
  </div>
</section>'''


def chips(items):
    return '<div class="service-tags">' + ''.join(f'<span class="chip">{c}</span>' for c in items) + '</div>'


def split_prose(sections, name, alt):
    """Turn the first prose section into a split: portrait photo on the left, text on the right."""
    pat = re.compile(r'<section class="section (sec-[\w-]+)"([^>]*)>\s*<div class="container"><div class="prose fade-up">(.*?)</div></div>\s*</section>', re.S)
    m = pat.search(sections)
    assert m, 'no prose section to split'
    new = (f'<section class="section {m.group(1)}"{m.group(2)}>\n  <div class="container split">\n'
           f'    <figure class="split-media fade-up">{img("split-" + name, alt, ctx="split", w=800, h=1000, big=True)}</figure>\n'
           f'    <div class="prose fade-up">{m.group(3)}</div>\n  </div>\n</section>')
    return sections[:m.start()] + new + sections[m.end():]


def photo_card(title, desc, chip_list, link, link_label, photo, delay=0):
    """Service card led by a photo; the photo links to the same page but stays out of the tab order."""
    d = f' style="transition-delay:{delay:.2f}s"' if delay else ''
    return (f'<div class="service-card photo fade-up"{d}><a href="{link}" class="sc-media" tabindex="-1" aria-hidden="true">{photo}</a>'
            f'<div class="sc-body"><h3 class="service-title"><a href="{link}">{title}</a></h3><p class="service-desc">{desc}</p>'
            f'{chips(chip_list)}<a href="{link}" class="card-link" aria-label="{link_label}: {title}">{link_label} <span aria-hidden="true">→</span></a></div></div>')


def card(title, desc, chip_list=None, link=None, link_label='Ver más', delay=0, static=False, icon=''):
    d = f' style="transition-delay:{delay:.2f}s"' if delay else ''
    t = f'<a href="{link}">{title}</a>' if link else title
    ch = chips(chip_list) if chip_list else ''
    ln = f'<a href="{link}" class="card-link" aria-label="{link_label}: {title}">{link_label} <span aria-hidden="true">→</span></a>' if link else ''
    st = ' static' if static else ''
    return f'<div class="service-card fade-up{st}"{d}>{icon}<h3 class="service-title">{t}</h3><p class="service-desc">{desc}</p>{ch}{ln}</div>'


def page_hero(trail, h1_html, lead, hero_img_html, wa_text, tag=None):
    tag_html = f'<span class="tag">{tag}</span>' if tag else ''
    return f'''{crumbs_html(trail)}
<section class="page-hero">
  <div class="container">
    <div class="page-hero-grid">
      <div>
        {tag_html}
        <h1>{h1_html}</h1>
        <p class="lead">{lead}</p>
        <div class="hero-actions">{btns(wa_text)}</div>
      </div>
      <div class="page-hero-img">{hero_img_html}</div>
    </div>
  </div>
</section>'''


RELATED = {
    '/lavado-al-peso-y-por-prenda': ['/tintoreria-lavado-al-seco', '/lavado-de-edredones-y-ropa-de-cama', '/recojo-a-domicilio-lavanderia'],
    '/tintoreria-lavado-al-seco': ['/lavado-de-ternos-y-corbatas', '/lavado-de-vestidos-de-novia-y-fiesta', '/recojo-a-domicilio-lavanderia'],
    '/lavado-de-ternos-y-corbatas': ['/tintoreria-lavado-al-seco', '/lavado-al-peso-y-por-prenda', '/recojo-a-domicilio-lavanderia'],
    '/lavado-de-edredones-y-ropa-de-cama': ['/lavado-de-alfombras-y-cortinas', '/lavado-al-peso-y-por-prenda', '/recojo-a-domicilio-lavanderia'],
    '/lavado-de-alfombras-y-cortinas': ['/lavado-de-edredones-y-ropa-de-cama', '/lavado-de-zapatillas', '/lavado-al-peso-y-por-prenda'],
    '/lavado-de-zapatillas': ['/lavado-al-peso-y-por-prenda', '/tintoreria-lavado-al-seco', '/recojo-a-domicilio-lavanderia'],
    '/lavado-de-vestidos-de-novia-y-fiesta': ['/tintoreria-lavado-al-seco', '/lavado-al-peso-y-por-prenda', '/recojo-a-domicilio-lavanderia'],
    '/recojo-a-domicilio-lavanderia': ['/lavado-al-peso-y-por-prenda', '/lavado-de-edredones-y-ropa-de-cama', '/lavado-de-alfombras-y-cortinas'],
}
RELATED_DESC = {
    '/lavado-al-peso-y-por-prenda': 'Lavado al peso para tu ropa diaria y lavado por prenda con planchado.',
    '/tintoreria-lavado-al-seco': 'Abrigos, alpaca, ternos, cuero, gamuza y prendas delicadas.',
    '/lavado-de-ternos-y-corbatas': 'Ternos, sacos y corbatas, con recojo y entrega a domicilio.',
    '/lavado-de-edredones-y-ropa-de-cama': 'Edredones de 1 y 2 plazas, queen y king, y mantas polares.',
    '/lavado-de-alfombras-y-cortinas': 'Alfombras y cortinas de casa y oficina, en nuestro local de San Isidro.',
    '/lavado-de-zapatillas': 'Limpieza de zapatillas según su material, con revisión previa.',
    '/lavado-de-vestidos-de-novia-y-fiesta': 'Vestidos de novia, de noche y de fiesta, con pedrería y encajes.',
    '/recojo-a-domicilio-lavanderia': 'Recojo y entrega en San Isidro, San Borja, Surquillo y Miraflores.',
}


def related_services(current, heading='Otros servicios de Aquapress'):
    labels = dict(SERVICES)
    cards = ''.join(card(labels[p], RELATED_DESC[p], link=p, link_label='Ver servicio') for p in RELATED[current])
    return f'''<section class="section sec-cream">
  <div class="container">
    <div class="section-head fade-up"><h2 class="h2">{heading}</h2></div>
    <div class="grid-3">{cards}</div>
  </div>
</section>'''


def districts_links(current=None, heading='Zonas donde atendemos', lead=None):
    d = {
        '/': ('Nuestro local en San Isidro', 'Nuestro local: Av. del Parque Sur 193. Lunes a sábado de 7:30 AM a 8:00 PM.'),
        '/lavanderia-san-borja': ('Recojo a domicilio en San Borja', 'Recojo y entrega a domicilio en San Borja, coordinados por WhatsApp.'),
        '/lavanderia-surquillo': ('Recojo a domicilio en Surquillo', 'Recojo y entrega a domicilio en Surquillo, coordinados por WhatsApp.'),
        '/lavanderia-miraflores': ('Recojo a domicilio en Miraflores', 'Recojo y entrega a domicilio en Miraflores, coordinados por WhatsApp.'),
    }
    cards = ''
    for p, _ in DISTRICTS:
        if p == current:
            continue
        t, ds = d[p]
        link = p if p != '/' else '/#local'
        cards += card(t, ds, link=link, link_label='Cómo llegar' if p == '/' else 'Ver zona')
    lead_html = f'<p class="lead">{lead}</p>' if lead else ''
    n = len([1 for p, _ in DISTRICTS if p != current])
    grid = 'grid-3' if n == 3 else 'grid-2'
    return f'''<section class="section sec-white" id="zonas">
  <div class="container">
    <div class="section-head fade-up"><h2 class="h2">{heading}</h2>{lead_html}</div>
    <div class="{grid}">{cards}</div>
  </div>
</section>'''

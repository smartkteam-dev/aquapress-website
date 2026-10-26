from lib import *
from pages_core import steps_html, prose_section

SVC_CARDS = lambda: ''.join([
    card('Lavado al peso y por prenda', 'Ropa del día a día, camisas, pantalones y ternos con planchado.', link='/lavado-al-peso-y-por-prenda', link_label='Ver servicio'),
    card('Tintorería y lavado al seco', 'Abrigos, alpaca, cuero, ternos y vestidos de novia.', link='/tintoreria-lavado-al-seco', link_label='Ver servicio', delay=.08),
    card('Edredones y ropa de cama', 'Edredones de 1 y 2 plazas, queen y king, mantas polares, frazadas y protectores de colchón.', link='/lavado-de-edredones-y-ropa-de-cama', link_label='Ver servicio', delay=.16),
])


def district(slug, name, kw_extra, hero_name, hero_alt, intro, area_p, who_title, who_p, faqs, steps_note, wa_text, other_note):
    path = f'/lavanderia-{slug}'
    title = f'Lavandería en {name} con recojo a domicilio | Aquapress'
    desc = f'Lavandería en {name} con recojo a domicilio: lavado al peso, tintorería, planchado y edredones. Aquapress, en San Isidro. Pide tu recojo por WhatsApp.'
    kw = f'lavandería {name}, lavandería en {name}, tintorería {name}, recojo a domicilio {name}, lavandería a domicilio {name}, {kw_extra}'
    trail = [('Inicio', '/'), (f'Lavandería en {name}', path)]
    hero = page_hero(trail, f'Lavandería en {name} <em>con recojo a domicilio</em>', intro,
                     img(hero_name, hero_alt, eager=True), wa_text, f'Atendemos {name}')
    body = f'''{hero}

<section class="section sec-white">
  <div class="container"><div class="prose fade-up">
    <h2>Tu lavandería para {name}</h2>
    {area_p}
    <p>Nuestro local está en <strong>Av. del Parque Sur 193, San Isidro</strong>, distrito vecino a {name}. Atendemos de lunes a sábado de 7:30 AM a 8:00 PM, y coordinamos recojo y entrega a domicilio por WhatsApp.</p>
  </div></div>
</section>

<section class="section sec-cream">
  <div class="container">
    <div class="section-head fade-up"><h2 class="h2">Servicios con recojo en {name}</h2>
    <p class="lead">Todos nuestros servicios están disponibles con recojo a domicilio. Elige el que necesitas.</p></div>
    <div class="grid-3">{SVC_CARDS()}</div>
  </div>
</section>

<section class="how section">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:48px;"><h2 class="h2">Cómo pedir el recojo en {name}</h2></div>
    <div class="steps">
      <div class="step fade-up"><div class="step-num">1</div><h3 class="step-title">Escríbenos por WhatsApp</h3><p class="step-desc">Indícanos tu dirección en {name} y el tipo de prendas.</p></div>
      <div class="step fade-up" style="transition-delay:.08s"><div class="step-num">2</div><h3 class="step-title">Confirmamos y recogemos</h3><p class="step-desc">Verificamos disponibilidad y coordinamos el recojo contigo.</p></div>
      <div class="step fade-up" style="transition-delay:.16s"><div class="step-num">3</div><h3 class="step-title">Revisamos y limpiamos</h3><p class="step-desc">Inspeccionamos cada prenda, te indicamos el tratamiento y el plazo, y la limpiamos.</p></div>
      <div class="step fade-up" style="transition-delay:.24s"><div class="step-num">4</div><h3 class="step-title">Entrega en tu puerta</h3><p class="step-desc">{steps_note}</p></div>
    </div>
  </div>
</section>

<section class="section sec-white">
  <div class="container"><div class="prose fade-up">
    <h2>{who_title}</h2>
    {who_p}
  </div></div>
</section>

{districts_links(path, 'También atendemos otros distritos', other_note)}

{faq_section(faqs, f'Preguntas frecuentes: lavandería en {name}')}

{cta_band(f'Pide tu recojo en {name}', 'Escríbenos por WhatsApp con tu dirección y coordinamos el recojo.', wa_text)}'''
    graph = [biz_node(), breadcrumb_node(trail), faq_node(faqs)]
    return path, page(path, title, desc, kw, body, graph)


def san_borja():
    faqs = [
        ('¿Hay lavandería con recojo a domicilio en San Borja?',
         'Sí. Aquapress coordina recojo y entrega a domicilio en San Borja. Escríbenos por WhatsApp con tu dirección y confirmamos disponibilidad.'),
        ('¿Dónde queda el local de Aquapress respecto a San Borja?',
         'Nuestro local está en Av. del Parque Sur 193, en San Isidro, distrito vecino a San Borja. Atendemos de lunes a sábado de 7:30 AM a 8:00 PM.'),
        ('¿Puedo llevar mis prendas yo mismo desde San Borja?',
         'Sí. Puedes visitarnos en San Isidro y dejar tus prendas en nuestro local.'),
        ('¿Lavan camisas, ternos y edredones de San Borja?',
         'Sí: <a href="/lavado-al-peso-y-por-prenda">camisas y pantalones con planchado</a>, <a href="/tintoreria-lavado-al-seco">ternos en tintorería</a> y <a href="/lavado-de-edredones-y-ropa-de-cama">edredones</a>, con recojo en tu domicilio u oficina.'),
    ]
    return district(
        'san-borja', 'San Borja', 'lavandería cerca de San Borja, lavado de edredones San Borja', 'chompas-tejidas-dobladas',
        'Chompas tejidas dobladas con cuidado, listas para entregar a clientes de San Borja',
        '¿Vives o trabajas en San Borja? Recogemos tu ropa en tu casa u oficina y te la devolvemos limpia: lavado al peso, lavado por prenda, tintorería, planchado y edredones.',
        '<p>Si vives o trabajas en San Borja, no hace falta cruzar la ciudad para tener tu ropa impecable. Desde nuestro local de San Isidro coordinamos el recojo en zonas como la Av. San Luis, la Av. Aviación o los alrededores de la Av. Javier Prado, y te devolvemos las prendas limpias en tu puerta.</p>',
        'Ideal para familias y oficinas de San Borja',
        '<p>Los <a href="/lavado-de-edredones-y-ropa-de-cama">edredones y las mantas</a> son difíciles de transportar: con el recojo a domicilio no tienes que cargar nada.</p><p>Si trabajas en una oficina de la zona, puedes pedir el recojo allí mismo y recibir tus camisas, pantalones y ternos planchados y listos para la semana. Para abrigos, sacos y prendas delicadas contamos con <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>.</p>',
        faqs,
        'Te devolvemos tus prendas en tu domicilio u oficina de San Borja, o las recoges en San Isidro.',
        'Hola, quisiera coordinar un recojo en San Borja',
        'Nuestro local queda en San Isidro, y desde allí atendemos a tus vecinos de Surquillo y Miraflores.')


def surquillo():
    faqs = [
        ('¿Tienen servicio de lavandería a domicilio en Surquillo?',
         'Sí. Coordinamos recojo y entrega a domicilio en Surquillo. Escríbenos por WhatsApp para confirmar disponibilidad en tu dirección.'),
        ('¿Cuál es la lavandería de Aquapress más cercana a Surquillo?',
         'Nuestro local está en Av. del Parque Sur 193, San Isidro, distrito vecino a Surquillo. Si no puedes venir, el recojo a domicilio te ahorra el viaje.'),
        ('¿Puedo lavar mi ropa del día a día al peso desde Surquillo?',
         'Sí. El <a href="/lavado-al-peso-y-por-prenda">lavado al peso</a> tiene un mínimo de 2 kg y se puede coordinar con recojo a domicilio.'),
        ('¿Lavan edredones y mantas de Surquillo?',
         'Sí. Lavamos <a href="/lavado-de-edredones-y-ropa-de-cama">edredones de 1 y 2 plazas, queen y king, mantas polares, frazadas y protectores de colchón</a>, y los recogemos en tu casa.'),
    ]
    return district(
        'surquillo', 'Surquillo', 'lavandería cerca de Surquillo, lavado al peso Surquillo', 'cesto-ropa-para-lavar',
        'Canasta celeste con ropa sucia lista para lavar al peso, servicio con recojo en Surquillo',
        'Recogemos tu ropa en Surquillo y te la devolvemos limpia. Lavado al peso para el día a día, tintorería, planchado y ropa de cama. El lavado al peso tiene un mínimo de 2 kg.',
        '<p>Si vives en Surquillo, no necesitas ir hasta nuestro local para tener tu ropa limpia. Desde San Isidro coordinamos el recojo en zonas como la Av. Angamos, la Av. Tomás Marsano o los alrededores del mercado de Surquillo, para que no pierdas tiempo en traslados.</p>',
        'Para la rutina de cada semana en Surquillo',
        '<p>El <a href="/lavado-al-peso-y-por-prenda">lavado al peso</a> es la opción más práctica para la ropa del día a día: polos, ropa casual y ropa interior. Lo coordinas por WhatsApp, recogemos y devolvemos, y tú te olvidas del lavado.</p><p>También puedes pedir el lavado de <a href="/lavado-de-edredones-y-ropa-de-cama">edredones, frazadas y protectores de colchón</a> o llevar camisas y pantalones para planchado cuando los necesites.</p>',
        faqs,
        'Te devolvemos tus prendas limpias en tu puerta de Surquillo, o las recoges en San Isidro.',
        'Hola, quisiera coordinar un recojo en Surquillo',
        'Nuestro local queda en San Isidro, y desde allí atendemos también San Borja y Miraflores.')


def miraflores():
    faqs = [
        ('¿Hay lavandería con recojo a domicilio en Miraflores?',
         'Sí. Aquapress coordina recojo y entrega a domicilio en Miraflores. Escríbenos por WhatsApp con tu dirección y confirmamos disponibilidad.'),
        ('¿Limpian abrigos de alpaca y prendas delicadas de Miraflores?',
         'Sí. Contamos con <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a> para abrigos, alpaca, cuero, gamuzas y telas finas. Clientes de Miraflores ya nos confían sus abrigos de alpaca.'),
        ('¿Lavan vestidos de novia y de fiesta?',
         'Sí. Los vestidos de novia, de noche y de fiesta, incluidos los que tienen pedrería, forman parte de nuestro servicio de tintorería.'),
        ('¿Dónde queda el local de Aquapress respecto a Miraflores?',
         'Estamos en Av. del Parque Sur 193, San Isidro, distrito vecino a Miraflores. Atendemos de lunes a sábado de 7:30 AM a 8:00 PM.'),
    ]
    return district(
        'miraflores', 'Miraflores', 'lavandería cerca de Miraflores, tintorería Miraflores', 'prendas-lana-tejidos-delicados',
        'Chompas y abrigos de lana en un perchero, prendas delicadas para tintorería en Miraflores',
        'Recogemos tu ropa en Miraflores y la limpiamos con el cuidado que merece: tintorería, abrigos de alpaca, vestidos, lavado por prenda y ropa de cama.',
        '<p>Si vives o trabajas en Miraflores, nuestro local de San Isidro te queda cerca y además coordinamos el recojo en zonas como la Av. Larco, la Av. Benavides o los alrededores del Parque Kennedy, y te devolvemos tus prendas listas.</p>',
        'Cuidado especial para prendas delicadas en Miraflores',
        '<p>Clientes de Miraflores ya nos confían sus abrigos de alpaca, y también atendemos vestidos de fiesta y prendas con pedrería. Para ellas contamos con <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>, con revisión prenda por prenda y productos adecuados para cada tela.</p><p>Para el día a día, el <a href="/lavado-al-peso-y-por-prenda">lavado al peso y por prenda</a> con planchado mantiene tu ropa de oficina impecable, y el <a href="/recojo-a-domicilio-lavanderia">recojo a domicilio</a> evita traslados.</p>',
        faqs,
        'Te devolvemos tus prendas en tu domicilio u oficina de Miraflores, o las recoges en San Isidro.',
        'Hola, quisiera coordinar un recojo en Miraflores',
        'Nuestro local queda en San Isidro, y desde allí atendemos también San Borja y Surquillo.')


# =========================================================== BLOG
from posts import POSTS


def post(p):
    path = f"/blog/{p['slug']}"
    trail = [('Inicio', '/'), ('Blog', '/blog'), (p['h1'], path)]
    idx = [q['slug'] for q in POSTS].index(p['slug'])
    others = [POSTS[(idx + k) % len(POSTS)] for k in (1, 2)]
    rel = ''.join(
        f'''<div class="service-card post-card fade-up"><div class="post-thumb">{img(q['img'], q['alt'], ctx='thumb')}</div><h3 class="service-title"><a href="/blog/{q['slug']}">{q['h1']}</a></h3><p class="service-desc">{q['summary']}</p><a href="/blog/{q['slug']}" class="card-link">Leer artículo <span aria-hidden="true">→</span></a></div>'''
        for q in others)
    body = f'''{crumbs_html(trail)}
<article>
  <header class="container article-head" style="max-width:820px;">
    <span class="tag">{p['section']}</span>
    <h1>{p['h1']}</h1>
    <p class="post-meta">Por Aquapress Lavandería · <time datetime="{TODAY}">25 de octubre de 2026</time> · {p['read']} min de lectura</p>
  </header>
  <div class="container"><div class="post-hero-img">{img(p['img'], p['alt'], eager=True, ctx='post', big=True)}</div></div>
  <section class="section sec-white" style="padding-top:56px;">
    <div class="container"><div class="prose">
{p['body']}
    </div></div>
  </section>
</article>

<section class="section sec-linen">
  <div class="container">
    <div class="section-head fade-up"><h2 class="h2">Sigue leyendo</h2></div>
    <div class="related-posts grid-2">{rel}</div>
  </div>
</section>

{cta_band('¿Necesitas ayuda con tus prendas?', 'Visítanos en San Isidro o escríbenos para coordinar el recojo.', 'Hola, quisiera información sobre sus servicios')}'''
    article = {
        '@type': 'BlogPosting',
        '@id': DOMAIN + path + '#articulo',
        'mainEntityOfPage': {'@type': 'WebPage', '@id': DOMAIN + path},
        'headline': p['h1'],
        'description': p['desc'],
        'image': [f"{DOMAIN}/images/{p['og']}.jpg"],
        'datePublished': TODAY,
        'dateModified': TODAY,
        'inLanguage': 'es-PE',
        'author': {'@type': 'Organization', 'name': 'Aquapress Lavandería', 'url': DOMAIN + '/'},
        'publisher': {'@id': DOMAIN + '/#negocio'},
        'url': DOMAIN + path,
        'keywords': p['kw'],
        'articleSection': p['section'],
    }
    graph = [biz_node(), article, breadcrumb_node(trail)]
    extra = f'''
  <meta property="article:published_time" content="{TODAY}" />
  <meta property="article:modified_time" content="{TODAY}" />
  <meta property="article:section" content="{p['section']}" />'''
    html = page(path, p['title'], p['desc'], p['kw'], body, graph, og_image=f"/images/{p['og']}.jpg",
                og_alt=p['alt'], og_type='article', extra_head=extra)
    return path, html


def blog_index():
    path = '/blog'
    trail = [('Inicio', '/'), ('Blog', path)]
    cards = ''.join(
        f'''<div class="service-card post-card fade-up"{f' style="transition-delay:{i*0.08:.2f}s"' if i else ''}><div class="post-thumb">{img(q['img'], q['alt'], ctx='thumb')}</div><h2 class="service-title"><a href="/blog/{q['slug']}">{q['h1']}</a></h2><p class="service-desc">{q['summary']}</p><a href="/blog/{q['slug']}" class="card-link">Leer artículo <span aria-hidden="true">→</span></a></div>'''
        for i, q in enumerate(POSTS))
    body = f'''{crumbs_html(trail)}
<section class="page-hero" style="padding-bottom:40px;">
  <div class="container">
    <div class="article-head" style="max-width:820px;margin-left:0;">
      <span class="tag">Blog de Aquapress</span>
      <h1>Consejos para el cuidado de tu ropa</h1>
      <p class="lead">Guías prácticas de nuestra lavandería y tintorería en San Isidro: cómo lavar, guardar y cuidar tus prendas, edredones y ropa de temporada.</p>
    </div>
  </div>
</section>
<section class="section sec-white" style="padding-top:24px;">
  <div class="container"><div class="grid-3">{cards}</div></div>
</section>
{cta_band('¿Tienes una prenda delicada?', 'Escríbenos por WhatsApp y te orientamos sobre el mejor tratamiento.', 'Hola, quisiera una recomendación para cuidar una prenda')}'''
    title = 'Blog de cuidado de ropa y lavandería | Aquapress'
    desc = 'Consejos de lavandería y tintorería: cómo lavar alpaca, guardar ropa de invierno y cuidar edredones. Guías prácticas de Aquapress en San Isidro.'
    kw = 'blog de lavandería, consejos para lavar ropa, cuidado de ropa, cómo cuidar prendas delicadas, consejos de tintorería'
    graph = [
        biz_node(),
        {'@type': 'Blog', '@id': DOMAIN + '/blog#blog', 'url': DOMAIN + '/blog', 'name': 'Blog de Aquapress Lavandería', 'inLanguage': 'es-PE',
         'publisher': {'@id': DOMAIN + '/#negocio'},
         'blogPost': [{'@type': 'BlogPosting', 'headline': q['h1'], 'url': f"{DOMAIN}/blog/{q['slug']}", 'datePublished': TODAY} for q in POSTS]},
        breadcrumb_node(trail),
    ]
    return path, page(path, title, desc, kw, body, graph)


def not_found():
    body = f'''<section class="page-hero" style="padding:calc(var(--nav-h) + 80px) 0 100px;">
  <div class="container text-center">
    <span class="tag">Error 404</span>
    <h1 style="font-family:var(--font-serif);font-size:clamp(2.2rem,5vw,3.4rem);margin-bottom:18px;">No encontramos esa página</h1>
    <p class="lead" style="margin:0 auto 28px;max-width:520px;">Puede que el enlace haya cambiado. Vuelve al inicio o elige uno de nuestros servicios.</p>
    <div class="hero-actions" style="justify-content:center;"><a href="/" class="btn btn-primary">Ir al inicio</a><a href="/lavado-al-peso-y-por-prenda" class="btn btn-outline">Ver servicios</a></div>
  </div>
</section>'''
    html = page('/404', 'Página no encontrada | Aquapress Lavandería', 'La página que buscas no existe. Vuelve al inicio de Aquapress, lavandería y tintorería en San Isidro.',
                'lavandería San Isidro', body, [biz_node()], robots='noindex, follow')
    # a 404 must not carry a self-canonical to a URL that does not exist
    html = re.sub(r'  <link rel="canonical"[^\n]*\n', '', html)
    html = re.sub(r'  <link rel="alternate" hreflang[^\n]*\n', '', html)
    html = re.sub(r'  <meta property="og:url"[^\n]*\n', '', html)
    return '/404', html

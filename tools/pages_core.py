from lib import *

ICON = {k: icon_wrap(k) for k in ICON_PATHS}

STEPS = [
    ('Tráenos tus prendas', 'Visítanos en Av. del Parque Sur 193, San Isidro. También puedes solicitar recojo a domicilio.'),
    ('Evaluamos y cotizamos', 'Revisamos cada prenda y te indicamos el tratamiento ideal y el plazo de entrega.'),
    ('Limpiamos con cuidado', 'Lavado, planchado, secado o tintorería. Cada prenda recibe el proceso adecuado.'),
    ('Recoge o te enviamos', 'Pasa a recoger en nuestro local cuando quieras, o coordinamos la entrega a tu puerta.'),
]


def steps_html(extra_class=''):
    out = ''
    for i, (t, d) in enumerate(STEPS):
        delay = f' style="transition-delay:{i*0.08:.2f}s"' if i else ''
        out += f'<div class="step fade-up"{delay}><div class="step-num">{i+1}</div><h3 class="step-title">{t}</h3><p class="step-desc">{d}</p></div>'
    return f'<div class="steps">{out}</div>'


# =========================================================== HOME
HOME_FAQS = [
    ('¿Dónde queda la lavandería Aquapress en San Isidro?',
     'Estamos en Av. del Parque Sur 193, San Isidro, Lima, y atendemos de lunes a sábado de 7:30 AM a 8:00 PM. ¿Prefieres que vayamos a ti? Escríbenos por WhatsApp y coordinamos tu recojo a domicilio.'),
    ('¿Qué servicios ofrece Aquapress?',
     'Ofrecemos <a href="/lavado-al-peso-y-por-prenda">lavado al peso y por prenda con planchado</a>, <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>, <a href="/lavado-de-edredones-y-ropa-de-cama">lavado de edredones y ropa de cama</a>, prendas especiales y <a href="/recojo-a-domicilio-lavanderia">recojo a domicilio</a>.'),
    ('¿Hacen recojo a domicilio y en qué distritos?',
     'Sí. Coordinamos recojo y entrega a domicilio en San Isidro, <a href="/lavanderia-san-borja">San Borja</a>, <a href="/lavanderia-surquillo">Surquillo</a> y <a href="/lavanderia-miraflores">Miraflores</a>. Escríbenos por WhatsApp para confirmar disponibilidad en tu dirección.'),
    ('¿Hay un mínimo para el lavado al peso?',
     'Sí. El lavado al peso tiene un mínimo de 2 kg. Si tienes menos ropa, escríbenos por WhatsApp y te orientamos sobre el lavado por prenda.'),
    ('¿Cuál es la diferencia entre lavado al peso y lavado por prenda?',
     'El lavado al peso es ideal para la ropa del día a día: la lavamos, secamos y entregamos al mejor precio. El lavado por prenda da atención individual a piezas como camisas, pantalones, ternos y casacas.'),
    ('¿Tienen servicio express?',
     'Sí. Si necesitas tus prendas con urgencia, escríbenos por WhatsApp: confirmamos si podemos atender tu pedido y en qué plazo.'),
    ('¿Lavan alfombras, cortinas, zapatillas y vestidos de novia?',
     'Sí. Tenemos servicios para <a href="/lavado-de-alfombras-y-cortinas">alfombras y cortinas</a>, <a href="/lavado-de-zapatillas">zapatillas</a> y <a href="/lavado-de-vestidos-de-novia-y-fiesta">vestidos de novia y de fiesta</a>.'),
    ('¿Hace cuánto tiempo funciona Aquapress?',
     f'Aquapress cuida la ropa de sus clientes desde {FOUNDED}: {YEARS_TEXT} de experiencia en lavandería y tintorería en San Isidro.'),
    ('¿Cómo cotizo mi pedido?',
     'Al recibir tus prendas las revisamos una por una y te indicamos el tratamiento ideal y el plazo de entrega. También puedes consultar antes por WhatsApp.'),
]


def home():
    path = '/'
    title = 'Lavandería y tintorería en San Isidro | Aquapress'
    desc = 'Lavandería y tintorería en San Isidro desde 2013. Lavado al peso, planchado y edredones con recojo y entrega a domicilio. Pide tu cotización por WhatsApp.'
    kw = 'lavandería San Isidro, tintorería San Isidro, lavandería cerca de mí, lavado al peso San Isidro, lavado al seco, planchado de camisas, recojo a domicilio, Aquapress'
    hero_imgs = f'''<div class="hero-mosaic">
          <div class="mosaic-img tall">{img('cesto-ropa-para-lavar', 'Canasta celeste con ropa sucia lista para el lavado al peso en San Isidro', eager=True, ctx='mosaic')}</div>
          <div class="mosaic-img">{img('secadoras-industriales-lavanderia', 'Hilera de secadoras industriales en una lavandería profesional de San Isidro', ctx='mosaic')}</div>
          <div class="mosaic-img">{img('prendas-lana-tejidos-delicados', 'Chompas y abrigos de lana en un perchero: prendas delicadas para tintorería y lavado al seco', ctx='mosaic')}</div>
          <div class="mosaic-img wide">{img('lavadoras-industriales-acero', 'Lavadoras industriales de acero inoxidable con la puerta abierta', ctx='mosaicwide')}</div>
        </div>'''
    hero = f'''<section class="hero" id="inicio">
  <div class="hero-blob-1"></div>
  <div class="hero-blob-2"></div>
  <div class="container">
    <div class="hero-grid">
      <div class="hero-content">
        <div class="hero-badge"><span class="hero-badge-dot"></span> San Isidro, Lima · Lun – Sáb</div>
        <h1 class="h1">Lavandería y tintorería <em>en San Isidro.</em><span class="h1-sub">Tu ropa, impecable.</span></h1>
        <p class="hero-desc">Lavandería cerca de ti en San Isidro, con recojo a domicilio en San Borja, Surquillo y Miraflores. Lavado al peso, lavado por prenda, tintorería, planchado y ropa de cama.</p>
        <div class="hero-actions">{btns('Hola, quisiera información sobre sus servicios')}</div>
        <ul class="hero-trust">
          <li class="hero-trust-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Drop-off en nuestro local</li>
          <li class="hero-trust-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Recojo a domicilio disponible</li>
          <li class="hero-trust-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Lavado al peso desde 2 kg</li>
          <li class="hero-trust-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Servicio express disponible</li>
        </ul>
      </div>
      <div class="hero-visual">
        {hero_imgs}
      </div>
    </div>
  </div>
</section>'''

    wave = lambda bg, fill, h=70: f'<div class="wave-divider" style="background:var(--{bg});" aria-hidden="true"><svg viewBox="0 0 1440 {h}" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"><path fill="var(--{fill})" d="M0,35 C360,70 720,0 1080,35 C1260,55 1380,45 1440,35 L1440,{h} L0,{h} Z"/></svg></div>'

    step_rows = ''.join(
        f'<li class="step-row fade-up"{f" style=transition-delay:{i*0.08:.2f}s" if i else ""}><span class="step-num">{i+1}</span>'
        f'<div><h3 class="step-title">{t}</h3><p class="step-desc">{d}</p></div></li>'
        for i, (t, d) in enumerate(STEPS))
    how = f'''<section class="how section" id="como-funciona">
  <div class="container split">
    <figure class="split-media fade-up">{img('chompas-tejidas-dobladas', 'Manos sosteniendo chompas tejidas de lana dobladas con cuidado después del lavado', ctx='split', big=True, w=1200, h=800)}</figure>
    <div class="how-copy">
      <div class="fade-up">
        <span class="tag">Proceso simple</span>
        <h2 class="h2">¿Cómo funciona nuestra lavandería?</h2>
        <p class="lead" style="max-width:min(500px,100%);margin:14px 0 0;">Visítanos en nuestro local o, si lo prefieres, coordinamos el recojo en tu domicilio.</p>
      </div>
      <ol class="step-list">{step_rows}</ol>
    </div>
  </div>
</section>'''

    P = lambda n, alt, **k: img(n, alt, ctx='card', w=800, h=600, **k)
    cards = ''.join([
        photo_card('Lavado al peso', 'Ideal para tu ropa del día a día. Lavamos, secamos y entregamos impecable al mejor precio.', ['Ropa casual', 'Polos', 'Bermudas', 'Ropa interior'], '/lavado-al-peso-y-por-prenda#lavado-al-peso', 'Ver lavado al peso', P('card-lavado-al-peso', 'Pilas de camisetas dobladas listas para entregar: lavado al peso')),
        photo_card('Lavado por prenda y planchado', 'Atención individualizada para cada pieza. Perfecto para prendas que merecen cuidado especial.', ['Camisas', 'Pantalones', 'Casacas', 'Planchado'], '/lavado-al-peso-y-por-prenda#lavado-por-prenda', 'Ver lavado por prenda', P('ropa-doblada-jeans-camisetas', 'Jeans y camisetas limpios y doblados: lavado por prenda y planchado'), .08),
        photo_card('Tintorería y lavado al seco', 'Procesos especializados para prendas delicadas: lana, alpaca, cuero, gamuzas y telas finas.', ['Abrigos', 'Chompa alpaca', 'Cuero', 'Gamuza'], '/tintoreria-lavado-al-seco', 'Ver tintorería', P('card-tintoreria', 'Prendas protegidas con fundas de plástico en una tintorería'), .16),
        photo_card('Ternos y corbatas', 'Limpieza profesional para ternos, sacos y corbatas, para la oficina y las ocasiones importantes.', ['Ternos', 'Sacos', 'Corbatas'], '/lavado-de-ternos-y-corbatas', 'Ver ternos y corbatas', P('card-ternos', 'Corbatas de seda colgadas en fila: limpieza de ternos y corbatas'), .24),
        photo_card('Vestidos de novia y de fiesta', 'Tu vestido de gala, de novia o con pedrería merece el mejor cuidado profesional.', ['Vestidos de novia', 'Vestidos de fiesta', 'Pedrería'], '/lavado-de-vestidos-de-novia-y-fiesta', 'Ver vestidos de novia y fiesta', P('vestido-novia-colgado-ventana', 'Vestido de novia de encaje y tul colgado de una percha de madera junto a una ventana: limpieza de vestidos de novia y de fiesta'), .32),
        photo_card('Ropa de cama y hogar', 'Edredones, mantas polares y todo lo necesario para mantener tu cama y tu hogar impecables.', ['Edredones 1–2 plz.', 'Mantas polares', 'Queen/King'], '/lavado-de-edredones-y-ropa-de-cama', 'Ver edredones y ropa de cama', P('edredon-blanco-cojines-beige', 'Cama con edredón blanco, cojines de lino beige y cubrecama acolchado en tonos neutros'), .40),
        photo_card('Alfombras y cortinas', 'Alfombras y cortinas de casa y oficina. Tráelas a nuestro local de San Isidro.', ['Alfombras', 'Cortinas'], '/lavado-de-alfombras-y-cortinas', 'Ver alfombras y cortinas', P('card-cortinas', 'Cortinas de lino junto a un ventanal en una sala luminosa'), .48),
        photo_card('Lavado de zapatillas', 'Limpiamos tus zapatillas según su material, con revisión previa para definir el tratamiento.', ['Deportivas', 'Urbanas', 'Blancas'], '/lavado-de-zapatillas', 'Ver lavado de zapatillas', P('zapatillas-blancas-lona', 'Zapatillas blancas de lona sobre una tela blanca: servicio de lavado de zapatillas'), .56),
        photo_card('Recojo a domicilio', 'Si no puedes venir, coordinamos el recojo en tu dirección. Consulta disponibilidad por WhatsApp.', ['San Isidro', 'San Borja', 'Surquillo', 'Miraflores'], '/recojo-a-domicilio-lavanderia', 'Ver recojo a domicilio', P('ropa-limpia-doblada-entrega-manos', 'Entrega de ropa limpia y doblada en las manos del cliente: recojo a domicilio'), .64),
    ])
    services = f'''<section class="services section" id="servicios">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:56px;">
      <span class="tag">Nuestros servicios</span>
      <h2 class="h2">Servicios de lavandería y tintorería en San Isidro</h2>
      <p class="lead" style="max-width:min(540px,100%);margin:14px auto 0;">Desde ropa cotidiana hasta prendas especiales. Tratamiento profesional para cada necesidad.</p>
    </div>
    <div class="service-grid">{cards}</div>
  </div>
</section>'''

    dcards = ''.join([
        card('Nuestro local en San Isidro', 'Estamos en Av. del Parque Sur 193. Pasa cuando quieras, de lunes a sábado.', link='/#local', link_label='Cómo llegar'),
        card('Recojo a domicilio en San Borja', 'Recojo y entrega a domicilio para hogares y oficinas de San Borja.', link='/lavanderia-san-borja', link_label='Ver zona', delay=.08),
        card('Recojo a domicilio en Surquillo', 'Coordinamos el recojo de tu ropa en Surquillo y te la devolvemos lista.', link='/lavanderia-surquillo', link_label='Ver zona', delay=.16),
        card('Recojo a domicilio en Miraflores', 'Recojo a domicilio en Miraflores para prendas delicadas y ropa de todos los días.', link='/lavanderia-miraflores', link_label='Ver zona', delay=.24),
    ])
    zonas = f'''<section class="section sec-white" id="zonas">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:36px;">
      <span class="tag">Atención rápida</span>
      <h2 class="h2">¿Buscas una lavandería cerca de ti? Atendemos 4 distritos</h2>
      <p class="lead" style="max-width:min(600px,100%);margin:14px auto 0;">Atendemos clientes de San Isidro, San Borja, Surquillo y Miraflores con recojo a domicilio, lavado al peso, tintorería y planchado.</p>
    </div>
    <div class="grid-4">{dcards}</div>
  </div>
</section>'''

    why_items = [
        ('Entrega puntual', 'Cumplimos los plazos acordados. Tu tiempo es valioso y lo respetamos.', '<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>'),
        ('Revisión prenda a prenda', 'Inspeccionamos cada pieza antes y después del lavado para garantizar calidad.', '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>'),
        ('Productos de calidad', 'Usamos detergentes adecuados para cada tipo de prenda, tela y tejido.', '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'),
        ('Atención directa', 'Coordinamos todo por WhatsApp o por teléfono. Sin formularios complicados.', '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'),
        ('Ubicación privilegiada', 'En el corazón de San Isidro. Fácil acceso, con opción de recojo a domicilio.', '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>'),
        ('Tu ropa, segura', 'Tratamos tus prendas con el mismo cuidado que les darías tú.', '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>'),
    ]
    why_html = ''.join(
        f'<div class="why-item fade-up"{f" style=transition-delay:{i*0.08:.2f}s" if i else ""}><div class="why-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{ic}</svg></div><div class="why-text"><h3>{t}</h3><p>{d}</p></div></div>'
        for i, (t, d, ic) in enumerate(why_items))
    why = f'''<section class="why section">
  <div class="bg-blob a"></div><div class="bg-blob b"></div>
  <div class="container" style="position:relative;z-index:2;">
    <div class="text-center fade-up" style="margin-bottom:8px;">
      <span class="tag">Por qué elegirnos</span>
      <h2 class="h2">Más que una lavandería,<br/>un servicio de confianza</h2>
    </div>
    <div class="why-grid">{why_html}</div>
  </div>
</section>'''

    reviews = f'''<section class="reviews section" id="resenas">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:56px;">
      <span class="tag">Reseñas</span>
      <h2 class="h2">Lo que dicen nuestros clientes</h2>
      <p class="lead" style="max-width:min(460px,100%);margin:14px auto 0;">La satisfacción de quienes nos visitan es nuestra mejor carta de presentación.</p>
    </div>
    <div class="review-grid">
      <figure class="review-card fade-up">
        <div class="stars" role="img" aria-label="5 de 5 estrellas">★ ★ ★ ★ ★</div>
        <blockquote class="review-text">"Excelente equipo de trabajo. Muy responsables y sobre todo impecables."</blockquote>
        <figcaption class="reviewer"><div class="reviewer-avatar" aria-hidden="true">L</div><div><div class="reviewer-name">Leinny Griman</div><div class="reviewer-meta">Reseña en Google</div></div></figcaption>
      </figure>
      <figure class="review-card fade-up" style="transition-delay:0.1s">
        <div class="stars" role="img" aria-label="5 de 5 estrellas">★ ★ ★ ★ ★</div>
        <blockquote class="review-text">"Excelente atención, demuestran gran amabilidad, y servicio"</blockquote>
        <figcaption class="reviewer"><div class="reviewer-avatar" aria-hidden="true">E</div><div><div class="reviewer-name">Efrén Delgado</div><div class="reviewer-meta">Reseña en Google</div></div></figcaption>
      </figure>
      <figure class="review-card fade-up" style="transition-delay:0.2s">
        <div class="stars" role="img" aria-label="5 de 5 estrellas">★ ★ ★ ★ ★</div>
        <blockquote class="review-text">"Lugar muy limpio y confiable. Personal súper amable y excelente. Además, hacen el trabajo rápido."</blockquote>
        <figcaption class="reviewer"><div class="reviewer-avatar" aria-hidden="true">A</div><div><div class="reviewer-name">Angelica Rosado</div><div class="reviewer-meta">Reseña en Google</div></div></figcaption>
      </figure>
    </div>
    <p class="reviews-source">Reseñas de clientes en <a class="text-link" href="{MAPS}" target="_blank" rel="noopener noreferrer">Google Maps</a>, tal como las publicaron. <a class="text-link" href="{FB}" target="_blank" rel="noopener noreferrer">Facebook</a>.</p>
  </div>
</section>

'''
    faq = faq_section(HOME_FAQS, 'Preguntas frecuentes sobre nuestra lavandería', bg='sec-linen')

    cta = cta_band('¿Listo para probar el servicio?', 'Visítanos en San Isidro o escríbenos para coordinar el recojo.', 'Hola, quisiera coordinar un servicio')

    location = f'''<section class="location section" id="local">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:48px;">
      <span class="tag">Dónde estamos</span>
      <h2 class="h2">Visítanos en San Isidro</h2>
      <p class="lead" style="max-width:min(520px,100%);margin:14px auto 0;">Estamos en Av. del Parque Sur 193 y atendemos clientes de San Isidro, San Borja, Surquillo y Miraflores con recojo a domicilio y entrega rápida.</p>
    </div>
    <div class="location-card fade-up">
      <iframe class="location-map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3901.3!2d-77.0183454!3d-12.1022732!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9105c97adfc8395b%3A0x7562a9160fbcbafd!2sAquapress%20Lavanderia!5e0!3m2!1ses!2spe!4v1714000000000" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa de ubicación de Aquapress Lavandería en San Isidro"></iframe>
      <address class="location-info" style="font-style:normal;">
        <div class="location-name">Aquapress Lavandería – San Isidro</div>
        <div class="location-detail"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>Av. del Parque Sur 193, San Isidro 15036, Lima, Perú</div>
        <div class="location-detail"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13.5a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2.7h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 10.09a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg><a href="tel:{TEL}">{TEL_FMT}</a></div>
        <div class="location-detail"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>Lunes – Sábado: 7:30 AM – 8:00 PM · Domingos: Cerrado</div>
        <div class="location-actions">
          <a href="{wa()}" class="btn btn-primary btn-sm" target="_blank" rel="noopener noreferrer">WhatsApp</a>
          <a href="tel:{TEL}" class="btn btn-outline btn-sm">Llamar</a>
          <a href="{MAPS}" class="btn btn-outline btn-sm" target="_blank" rel="noopener noreferrer">Ver en Maps</a>
        </div>
      </address>
    </div>
  </div>
</section>'''

    body = '\n\n'.join([hero, wave('cream', 'linen'), how, wave('linen', 'cream', 60), services, zonas, why, reviews, faq, cta, location])

    biz = biz_node()
    biz['hasOfferCatalog'] = {
        '@type': 'OfferCatalog', 'name': 'Servicios de lavandería y tintorería',
        'itemListElement': [
            {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': l, 'url': DOMAIN + p}} for p, l in SERVICES
        ],
    }
    graph = [
        biz,
        {'@type': 'WebSite', '@id': DOMAIN + '/#sitio', 'url': DOMAIN + '/', 'name': 'Aquapress Lavandería', 'inLanguage': 'es-PE', 'publisher': {'@id': DOMAIN + '/#negocio'}},
        {'@type': 'WebPage', '@id': DOMAIN + '/#pagina', 'url': DOMAIN + '/', 'name': title, 'isPartOf': {'@id': DOMAIN + '/#sitio'}, 'about': {'@id': DOMAIN + '/#negocio'}, 'inLanguage': 'es-PE'},
        faq_node(HOME_FAQS),
    ]
    return path, page(path, title, desc, kw, body, graph)


# =========================================================== SERVICE PAGES
def service_page(path, title, desc, kw, h1, lead, tag, hero_img, wa_text, sections, faqs, svc_name, svc_desc, svc_type, cta_title, cta_text, short_name, og=None, split=None):
    trail = [('Inicio', '/'), (short_name, path)]
    hero = page_hero(trail, h1, lead, hero_img, wa_text, tag)
    body = '\n\n'.join([
        hero,
        sections if not split else split_prose(sections, *split),
        districts_links(None, 'Servicio disponible en San Isidro, San Borja, Surquillo y Miraflores',
                        'Visítanos en San Isidro o coordina el recojo a domicilio en estos distritos.'),
        related_services(path),
        faq_section(faqs, f'Preguntas frecuentes: {short_name.lower()}'),
        cta_band(cta_title, cta_text, wa_text),
    ])
    graph = [biz_node(), service_node(svc_name, svc_desc, path, svc_type), breadcrumb_node(trail), faq_node(faqs)]
    return path, page(path, title, desc, kw, body, graph, **(og or {}))


def prose_section(inner, bg='sec-white'):
    return f'<section class="section {bg}"><div class="container"><div class="prose fade-up">{inner}</div></div></section>'


def lavado():
    path = '/lavado-al-peso-y-por-prenda'
    faqs = [
        ('¿Cuándo conviene el lavado al peso y cuándo el lavado por prenda?',
         'El lavado al peso conviene para la ropa del día a día: polos, bermudas, ropa casual y ropa interior. El lavado por prenda es mejor para piezas que piden más cuidado, como camisas, pantalones, ternos y casacas.'),
        ('¿Hay un mínimo para el lavado al peso?',
         'Sí. El lavado al peso tiene un mínimo de 2 kg. Si tienes menos ropa, consulta por WhatsApp el lavado por prenda.'),
        ('¿Hacen planchado de camisas y pantalones?',
         'Sí. Ofrecemos planchado de camisas, pantalones y ropa de vestir. Cuéntanos qué necesitas por WhatsApp o en nuestro local de San Isidro.'),
        ('¿Cuánto demora el servicio?',
         'El plazo depende de la cantidad de prendas y del tratamiento. Al recibir tu pedido te indicamos el plazo de entrega y lo cumplimos.'),
        ('¿Tienen servicio express?',
         'Sí. Escríbenos por WhatsApp para confirmar si podemos atender tu pedido con urgencia y en qué plazo.'),
        ('¿Puedo pedir recojo a domicilio para mi ropa del día a día?',
         'Sí. Coordinamos el <a href="/recojo-a-domicilio-lavanderia">recojo a domicilio</a> en San Isidro, San Borja, Surquillo y Miraflores. Consulta disponibilidad por WhatsApp.'),
    ]
    secs = f'''<section class="section sec-white" id="lavado-al-peso">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Ropa diaria</span><h2 class="h2">Lavado al peso en San Isidro</h2>
    <p class="lead">Ideal para tu ropa del día a día. Lavamos, secamos y entregamos impecable al mejor precio.</p></div>
    <div class="grid-3">
      {card('Qué ropa va al peso', 'Polos, bermudas, ropa casual y ropa interior: todo lo que usas cada semana y no necesita un tratamiento individual.', ['Ropa casual', 'Polos', 'Bermudas', 'Ropa interior'], static=True)}
      {card('Mínimo de 2 kg', 'Puedes traer una bolsa o varias, siempre desde 2 kg. Para menos ropa, consulta por WhatsApp el lavado por prenda.', static=True, delay=.08)}
      {card('Recoge o te la llevamos', 'Pasa por nuestro local de San Isidro o coordina el recojo y la entrega a domicilio por WhatsApp.', static=True, delay=.16)}
    </div>
  </div>
</section>

<section class="section sec-linen" id="lavado-por-prenda">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Cuidado individual</span><h2 class="h2">Lavado por prenda: atención pieza por pieza</h2>
    <p class="lead">Atención individualizada para cada pieza. Perfecto para prendas que merecen cuidado especial.</p></div>
    <div class="grid-2">
      {card('Camisas y pantalones de vestir', 'Cada prenda se revisa antes y después del lavado. Camisas y pantalones quedan limpios y listos para usar.', ['Camisas', 'Pantalones'], static=True)}
      {card('Ternos y casacas', 'Prendas de mayor valor que merecen una revisión individual y un tratamiento adecuado a su tela.', ['Ternos', 'Casacas'], static=True, delay=.08)}
    </div>
    <p class="lead text-center fade-up" style="margin-top:28px;">¿Tu prenda es muy delicada? Mira nuestro servicio de <a class="text-link" href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>.</p>
  </div>
</section>

<section class="section sec-white" id="planchado">
  <div class="container">
    <div class="prose fade-up">
      <h2>Planchado profesional en San Isidro</h2>
      <p>El planchado es parte del cuidado de tu ropa: una camisa bien planchada cambia cómo te ves y cómo te sientes. En Aquapress planchamos camisas, pantalones y ropa de vestir para que las recibas listas para usar.</p>
      <p>Puedes combinar el planchado con el lavado por prenda y pedirlo para tu ropa de oficina, tus camisas de vestir o la ropa de toda la familia. Cuéntanos qué necesitas y te indicamos el plazo de entrega.</p>
    </div>
  </div>
</section>

<section class="how section" id="como-funciona-lavado">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:48px;"><h2 class="h2">¿Cómo funciona el lavado en Aquapress?</h2></div>
    {steps_html()}
  </div>
</section>

<section class="section sec-white">
  <div class="container"><div class="prose fade-up">
    <h2>¿Lavado al peso o por prenda? Cómo elegir</h2>
    <ul>
      <li><strong>Elige lavado al peso</strong> si quieres lavar mucha ropa de uso diario a buen precio: polos, bermudas, ropa casual y ropa interior.</li>
      <li><strong>Elige lavado por prenda</strong> si se trata de camisas, pantalones, ternos o casacas que quieres recibir revisados y planchados.</li>
      <li><strong>Elige tintorería</strong> si la etiqueta pide limpieza en seco o la prenda es de lana fina, cuero, gamuza o tela delicada: mira el servicio de <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>.</li>
    </ul>
    <p>Si no estás seguro, llévanos tus prendas o escríbenos y te recomendamos el tratamiento ideal.</p>
  </div></div>
</section>'''
    return service_page(
        path,
        'Lavado al peso y por prenda en San Isidro | Aquapress',
        'Lavado al peso desde 2 kg y lavado por prenda con planchado en San Isidro. Ropa limpia y lista, con recojo a domicilio. Cotiza por WhatsApp.',
        'lavado al peso San Isidro, lavandería al peso, lavado por prenda, planchado de camisas, lavado al peso desde 2 kg, lavar ropa San Isidro',
        'Lavado al peso y por prenda <em>en San Isidro</em>',
        'Lavamos tu ropa del día a día al peso y las prendas que piden más cuidado por pieza, con planchado. Visítanos en Av. del Parque Sur 193, San Isidro, o coordina el recojo a domicilio.',
        'Lavandería en San Isidro',
        img('cesto-ropa-para-lavar', 'Canasta celeste con ropa lista para el lavado al peso en San Isidro', eager=True),
        'Hola, quisiera información sobre el lavado al peso o por prenda',
        secs, faqs,
        'Lavado al peso y por prenda', 'Lavado al peso para ropa diaria, lavado por prenda para camisas, pantalones, ternos y casacas, y planchado en San Isidro, Lima.',
        'Lavandería', '¿Listo para dejar tu ropa en buenas manos?', 'Visítanos en San Isidro o escríbenos para coordinar el recojo.',
        'Lavado al peso y por prenda',
        split=('lavado-al-peso', 'Pilas de camisetas dobladas sobre una mesa de lavandería: lavado al peso y planchado'))


def tintoreria():
    path = '/tintoreria-lavado-al-seco'
    faqs = [
        ('¿Qué es el lavado al seco o lavado en seco?',
         'Es un proceso de limpieza que usa solventes en lugar de agua (en inglés, dry cleaning; a la tintorería se la conoce también como dry cleaners). Se recomienda para prendas delicadas o estructuradas, como abrigos, ternos, prendas de lana fina, cuero, gamuza y telas finas, que pueden dañarse con el lavado normal.'),
        ('¿Limpian vestidos de novia y de fiesta?',
         'Sí. Los vestidos de novia, de noche y de fiesta, incluidos los que tienen pedrería, son parte de nuestro servicio de tintorería. Escríbenos por WhatsApp para orientarte sobre el tratamiento ideal.'),
        ('¿Pueden limpiar chompas y abrigos de alpaca?',
         'Sí. Trabajamos con alpaca, lana, abrigos y sacones. Si prefieres lavar tu chompa en casa, revisa nuestra guía de <a href="/blog/como-lavar-chompa-de-alpaca">cómo lavar una chompa de alpaca</a>.'),
        ('¿Cuándo debo llevar mi ropa a la tintorería?',
         'Cuando la etiqueta indique limpieza en seco, cuando la prenda tenga forro o estructura, o cuando se trate de una prenda delicada o de valor. También conviene limpiar los abrigos antes de guardarlos: lee <a href="/blog/guardar-ropa-de-invierno-antes-del-verano">cómo guardar la ropa de invierno</a>.'),
        ('¿Tienen servicio express de tintorería?',
         'Sí. Escríbenos por WhatsApp para confirmar si podemos atender tu prenda con urgencia y en qué plazo.'),
        ('¿Cuánto demora la tintorería y hacen recojo a domicilio?',
         'Al recibir tus prendas te indicamos el plazo de entrega. Además coordinamos <a href="/recojo-a-domicilio-lavanderia">recojo a domicilio</a> en San Isidro, San Borja, Surquillo y Miraflores.'),
    ]
    secs = f'''<section class="section sec-white" id="prendas">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Prendas delicadas</span><h2 class="h2">Qué prendas llevar a la tintorería</h2>
    <p class="lead">Procesos especializados para prendas delicadas: lana, alpaca, cuero, gamuzas y telas finas.</p></div>
    <div class="grid-4">
      {card('Abrigos y sacones', 'Prendas estructuradas y con forro que se limpian mejor en seco para conservar su forma.', ['Abrigos', 'Sacones'], static=True)}
      {card('Chompas de alpaca y lana', 'Tejidos finos que requieren un proceso cuidadoso para mantener su suavidad.', ['Chompa alpaca'], static=True, delay=.06)}
      {card('Cuero y gamuza', 'Materiales delicados que no admiten el lavado normal y piden manos expertas.', ['Cuero', 'Gamuzas'], static=True, delay=.12)}
      {card('Ternos y corbatas', 'Limpieza profesional para tu ropa formal de trabajo y de ocasiones especiales.', ['Ternos', 'Corbatas'], '/lavado-de-ternos-y-corbatas', 'Ver ternos y corbatas', delay=.18)}
    </div>
  </div>
</section>

<section class="section sec-linen" id="prendas-especiales">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Ocasiones especiales</span><h2 class="h2">Vestidos de novia, de fiesta y prendas con pedrería</h2>
    <p class="lead">Tu vestido de gala, traje de noche o prenda con pedrería merece el mejor cuidado profesional.</p></div>
    <div class="grid-3">
      {card('Vestidos de novia', 'Un vestido de novia es una prenda única. Lo revisamos con detalle antes de definir el tratamiento.', ['Vestidos de novia'], static=True)}
      {card('Vestidos de noche y de fiesta', 'Telas finas y acabados delicados que requieren limpieza profesional.', ['Vestidos de noche', 'Vestidos de fiesta'], static=True, delay=.08)}
      {card('Pedrería, sacones y poleras', 'Prendas con aplicaciones o tejidos especiales que necesitan atención individual.', ['Pedrería', 'Sacones', 'Poleras'], static=True, delay=.16)}
    </div>
    <p class="lead text-center fade-up" style="margin-top:28px;">Conoce el servicio completo de <a class="text-link" href="/lavado-de-vestidos-de-novia-y-fiesta">lavado de vestidos de novia y de fiesta</a>, o escríbenos por WhatsApp y te orientamos.</p>
  </div>
</section>

<section class="section sec-white" id="lavado-al-seco-vs-agua">
  <div class="container"><div class="prose fade-up">
    <h2>Lavado al seco o lavado en agua: ¿cuál necesita tu prenda?</h2>
    <p>La etiqueta de cuidado es la primera pista. Si indica <strong>limpieza en seco</strong> (el símbolo del círculo), lo más seguro es llevarla a una tintorería. Si permite lavado a mano o en máquina, puede lavarse con el tratamiento por prenda.</p>
    <h3>Conviene el lavado al seco cuando…</h3>
    <ul>
      <li>La prenda tiene forro, hombreras o estructura, como abrigos, sacones y ternos.</li>
      <li>La tela es delicada: lana fina, seda, cuero, gamuza o encajes.</li>
      <li>Tiene pedrería o aplicaciones que podrían dañarse con el agua.</li>
      <li>Es una prenda de valor y no quieres arriesgar el color ni la forma.</li>
    </ul>
    <h3>Puede lavarse en agua cuando…</h3>
    <p>La etiqueta lo permite y la prenda es de algodón, poliéster o mezclas resistentes. Para ropa diaria, mira el <a href="/lavado-al-peso-y-por-prenda">lavado al peso y por prenda</a>.</p>
  </div></div>
</section>

<section class="why section">
  <div class="bg-blob a"></div><div class="bg-blob b"></div>
  <div class="container" style="position:relative;z-index:2;">
    <div class="text-center fade-up" style="margin-bottom:8px;"><span class="tag">Nuestro cuidado</span><h2 class="h2">Cómo cuidamos tus prendas delicadas</h2></div>
    <div class="why-grid">
      <div class="why-item fade-up"><div class="why-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div><div class="why-text"><h3>Revisión prenda a prenda</h3><p>Inspeccionamos cada pieza antes y después del proceso para garantizar calidad.</p></div></div>
      <div class="why-item fade-up" style="transition-delay:.08s"><div class="why-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><div class="why-text"><h3>Productos adecuados</h3><p>Usamos productos adecuados para cada tipo de prenda, tela y tejido.</p></div></div>
    </div>
  </div>
</section>'''
    return service_page(
        path,
        'Tintorería y lavado al seco en San Isidro | Aquapress',
        'Tintorería en San Isidro para abrigos, alpaca, cuero, gamuza y ternos. Cuidado experto y recojo a domicilio. Cotiza por WhatsApp.',
        'tintorería San Isidro, lavado al seco, lavado en seco Lima, limpieza de vestidos de novia, lavar abrigos de alpaca, limpieza de cuero y gamuza',
        'Tintorería y lavado al seco <em>en San Isidro</em>',
        'Procesos especializados para prendas delicadas: abrigos, alpaca, cuero, gamuzas y vestidos de novia. Visítanos en San Isidro o coordina el recojo a domicilio.',
        'Tintorería en San Isidro',
        img('prendas-lana-tejidos-delicados', 'Chompas y abrigos de lana en un perchero: prendas delicadas para tintorería y lavado al seco', eager=True),
        'Hola, quisiera información sobre tintorería y lavado al seco',
        secs, faqs,
        'Tintorería y lavado al seco', 'Tintorería y lavado al seco de abrigos, alpaca, cuero, gamuza, vestidos de novia y prendas con pedrería en San Isidro, Lima.',
        'Tintorería', 'Confía tus prendas delicadas a especialistas', 'Escríbenos por WhatsApp y te orientamos sobre el tratamiento ideal.',
        'Tintorería y lavado al seco',
        split=('tintoreria', 'Prendas colgadas y protegidas con fundas de plástico en una tintorería: tintorería y lavado al seco'))


def edredones():
    path = '/lavado-de-edredones-y-ropa-de-cama'
    faqs = [
        ('¿Lavan edredones queen y king?',
         'Sí. Lavamos edredones de 1 y 2 plazas, queen y king, además de mantas polares, frazadas y protectores de colchón.'),
        ('¿Cada cuánto debo lavar mi edredón?',
         'Como referencia, el edredón se lava unas veces al año según el uso, y la funda con más frecuencia. Con alergias, niños o mascotas conviene lavarlo más seguido. Lee la guía <a href="/blog/cada-cuanto-lavar-un-edredon">cada cuánto lavar un edredón y cómo hacerlo</a>.'),
        ('¿Por qué no lavarlo en mi lavadora de casa?',
         'Los edredones grandes suelen no caber bien en una lavadora doméstica: se enjuagan mal y tardan en secar, lo que favorece la humedad y los malos olores. Una lavandería con el equipo adecuado lo resuelve en un solo servicio.'),
        ('¿Lavan frazadas y protectores de colchón?',
         'Sí. Además de edredones, lavamos mantas polares, frazadas, protectores de colchón y otras piezas de ropa de cama.'),
        ('¿Hacen recojo a domicilio de edredones?',
         'Sí. Los edredones son voluminosos, por eso muchos clientes piden el <a href="/recojo-a-domicilio-lavanderia">recojo a domicilio</a> en San Isidro, San Borja, Surquillo y Miraflores.'),
    ]
    secs = f'''<section class="section sec-white" id="edredones">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Ropa de cama y hogar</span><h2 class="h2">Edredones, frazadas y protectores de colchón</h2>
    <p class="lead">Edredones, mantas polares, frazadas, protectores de colchón y todo lo necesario para mantener tu cama impecable.</p></div>
    <div class="grid-4">
      {card('Edredones de 1 y 2 plazas', 'Lavado y secado completo para edredones de cama individual y de dos plazas.', ['Edredones 1–2 plz.'], static=True)}
      {card('Edredones queen y king', 'Piezas grandes que no caben bien en una lavadora de casa. Las lavamos y secamos por ti.', ['Queen/King'], static=True, delay=.08)}
      {card('Mantas polares y frazadas', 'Mantas polares, frazadas y cobertores para renovar tu ropa de cama.', ['Mantas polares', 'Frazadas', 'Cobertores'], static=True, delay=.16)}
      {card('Protectores de colchón', 'Lavamos tu protector de colchón para mantener tu cama higiénica y fresca.', ['Protectores de colchón'], static=True, delay=.24)}
    </div>
  </div>
</section>

<section class="section sec-linen">
  <div class="container"><div class="prose fade-up">
    <h2>Cuándo llevar tu edredón a una lavandería</h2>
    <ul>
      <li><strong>Es muy grande:</strong> un edredón queen o king suele no caber bien en una lavadora doméstica y se enjuaga mal.</li>
      <li><strong>No tienes dónde secarlo:</strong> un edredón húmedo huele mal y favorece la humedad. Debe secarse por completo.</li>
      <li><strong>Tiene manchas o olores</strong> que no salen con un lavado casero.</li>
      <li><strong>Quieres ahorrar tiempo:</strong> lo recogemos en tu casa, lo lavamos y te lo devolvemos listo.</li>
    </ul>
    <div class="callout">
      <p>¿Dudas sobre la frecuencia o el cuidado? Lee nuestra guía <a href="/blog/cada-cuanto-lavar-un-edredon">cada cuánto lavar un edredón y cómo hacerlo</a>. Para el resto del hogar, mira el lavado de <a href="/lavado-de-alfombras-y-cortinas">alfombras y cortinas</a>.</p>
    </div>
  </div></div>
</section>

<section class="how section">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:48px;"><h2 class="h2">Cómo lavamos tu ropa de cama</h2></div>
    {steps_html()}
  </div>
</section>'''
    return service_page(
        path,
        'Lavado de edredones en San Isidro | Aquapress',
        'Edredones, frazadas y mantas limpios y esponjosos en San Isidro. Recojo y entrega a domicilio en San Borja, Surquillo y Miraflores. Cotiza por WhatsApp.',
        'lavado de edredones, lavar edredón queen, lavandería de edredones San Isidro, lavado de mantas polares, lavado de frazadas, lavado de protectores de colchón, ropa de cama',
        'Lavado de edredones, frazadas y protectores de colchón <em>en San Isidro</em>',
        'Lavamos edredones de 1 y 2 plazas, queen y king, mantas polares, frazadas y protectores de colchón. Visítanos en San Isidro o coordina el recojo a domicilio.',
        'Ropa de cama y hogar',
        img('edredon-blanco-cojines-beige', 'Cama con edredón blanco, cojines de lino beige y cubrecama acolchado en tonos neutros: lavado de edredones y ropa de cama', eager=True),
        'Hola, quisiera información sobre el lavado de edredones',
        secs, faqs,
        'Lavado de edredones y ropa de cama', 'Lavado de edredones de 1 y 2 plazas, queen y king, mantas polares, frazadas y protectores de colchón en San Isidro, Lima.',
        'Lavado de edredones', 'Renueva tu ropa de cama', 'Escríbenos por WhatsApp y coordina el recojo de tu edredón.',
        'Edredones y ropa de cama',
        split=('edredones', 'Cama con edredón blanco, almohadas y luz natural: lavado de edredones y ropa de cama'))


def recojo():
    path = '/recojo-a-domicilio-lavanderia'
    faqs = [
        ('¿En qué distritos hacen recojo a domicilio?',
         'Coordinamos recojo y entrega en San Isidro, <a href="/lavanderia-san-borja">San Borja</a>, <a href="/lavanderia-surquillo">Surquillo</a> y <a href="/lavanderia-miraflores">Miraflores</a>. Para zonas aledañas, consulta disponibilidad por WhatsApp.'),
        ('¿Cómo coordino el recojo?',
         'Escríbenos por WhatsApp con tu dirección y el tipo de prendas. Confirmamos disponibilidad y acordamos el recojo.'),
        ('¿Puedo pedir el recojo en mi oficina?',
         'Sí. Recogemos desde tu casa u oficina, siempre que esté en alguno de los distritos de atención.'),
        ('¿Cuánto cuesta el recojo a domicilio?',
         'Las condiciones dependen de tu dirección y del pedido. Consúltalas por WhatsApp antes de coordinar.'),
        ('¿Qué servicios puedo pedir con recojo?',
         'Todos: <a href="/lavado-al-peso-y-por-prenda">lavado al peso y por prenda</a>, <a href="/tintoreria-lavado-al-seco">tintorería</a>, planchado y <a href="/lavado-de-edredones-y-ropa-de-cama">edredones y ropa de cama</a>.'),
    ]
    secs = f'''<section class="how section" id="como-funciona-recojo">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:56px;"><span class="tag">Paso a paso</span><h2 class="h2">Cómo funciona el recojo a domicilio</h2>
    <p class="lead" style="max-width:min(520px,100%);margin:14px auto 0;">Si no puedes venir, coordinamos el recojo en tu dirección.</p></div>
    <div class="steps">
      <div class="step fade-up"><div class="step-num">1</div><h3 class="step-title">Escríbenos por WhatsApp</h3><p class="step-desc">Cuéntanos tu dirección y qué prendas quieres enviar.</p></div>
      <div class="step fade-up" style="transition-delay:.08s"><div class="step-num">2</div><h3 class="step-title">Coordinamos el recojo</h3><p class="step-desc">Confirmamos disponibilidad en tu distrito y acordamos el momento del recojo.</p></div>
      <div class="step fade-up" style="transition-delay:.16s"><div class="step-num">3</div><h3 class="step-title">Evaluamos y limpiamos</h3><p class="step-desc">Revisamos cada prenda, te indicamos el tratamiento y el plazo, y la limpiamos con cuidado.</p></div>
      <div class="step fade-up" style="transition-delay:.24s"><div class="step-num">4</div><h3 class="step-title">Te la devolvemos</h3><p class="step-desc">Entregamos tus prendas en tu puerta, o las recoges en San Isidro si lo prefieres.</p></div>
    </div>
  </div>
</section>

<section class="section sec-white">
  <div class="container"><div class="prose fade-up">
    <h2>Recojo a domicilio para hogares, oficinas y prendas especiales</h2>
    <p>El recojo está pensado para quienes no tienen tiempo de venir: familias con edredones difíciles de transportar, profesionales con camisas y ternos, y clientes con prendas delicadas que prefieren confiar en una lavandería especializada.</p>
    <ul>
      <li><strong>Hogares:</strong> ropa del día a día, <a href="/lavado-de-edredones-y-ropa-de-cama">edredones</a>, mantas, <a href="/lavado-de-alfombras-y-cortinas">alfombras y cortinas</a>.</li>
      <li><strong>Oficinas y profesionales:</strong> camisas planchadas, pantalones y ternos.</li>
      <li><strong>Prendas especiales:</strong> abrigos, alpaca y vestidos con <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>.</li>
    </ul>
    <p>Consulta disponibilidad por WhatsApp y coordinamos todo contigo, sin formularios complicados.</p>
  </div></div>
</section>'''
    return service_page(
        path,
        'Lavandería con recojo a domicilio en San Isidro | Aquapress',
        'Recogemos tu ropa en San Isidro, San Borja, Surquillo y Miraflores y te la devolvemos lista. Pide tu recojo a domicilio por WhatsApp.',
        'lavandería con recojo a domicilio, lavandería a domicilio, recojo de ropa a domicilio, lavandería delivery San Isidro, lavandería a domicilio Miraflores',
        'Lavandería con recojo a domicilio <em>en San Isidro, San Borja, Surquillo y Miraflores</em>',
        'Si no puedes venir, coordinamos el recojo en tu casa u oficina y te devolvemos tus prendas limpias. Consulta disponibilidad por WhatsApp.',
        'Recojo y entrega',
        img('ropa-limpia-doblada-entrega-manos', 'Persona sosteniendo una pila de ropa limpia y doblada, lista para la entrega a domicilio', eager=True),
        'Hola, quisiera coordinar un recojo a domicilio',
        secs, faqs,
        'Recojo a domicilio', 'Recojo y entrega a domicilio de ropa para lavandería y tintorería en San Isidro, San Borja, Surquillo y Miraflores.',
        'Recojo a domicilio', 'Coordina el recojo de tu ropa', 'Escríbenos por WhatsApp con tu dirección y confirmamos disponibilidad.',
        'Recojo a domicilio')

from lib import *
from pages_core import service_page, steps_html

EXPRESS_FAQ = ('¿Tienen servicio express?',
               'Sí. Escríbenos por WhatsApp para confirmar si podemos atender tu pedido con urgencia y en qué plazo.')


def alfombras():
    path = '/lavado-de-alfombras-y-cortinas'
    faqs = [
        ('¿Lavan alfombras grandes?',
         'Sí. Recibimos alfombras de distintos tamaños. Tráela a nuestro local de San Isidro y te indicamos el tratamiento y el plazo de entrega.'),
        ('¿Cómo debo llevar mis cortinas?',
         'Retira los ganchos o argollas y tráelas dobladas. Así llegan seguras y listas para el proceso. Si tienes dudas, escríbenos antes por WhatsApp.'),
        ('¿Cuánto demora el lavado de alfombras y cortinas?',
         'Depende del tamaño, el material y la cantidad. Al recibirlas te indicamos el tratamiento y el plazo de entrega.'),
        ('¿Cuándo conviene llevar las cortinas a una lavandería?',
         'Cuando son grandes, gruesas, con forro o de tela delicada, o cuando no tienes dónde secarlas con buena ventilación. Lee la guía <a href="/blog/como-lavar-cortinas">cómo lavar cortinas</a>.'),
        EXPRESS_FAQ,
    ]
    secs = f'''<section class="section sec-white" id="alfombras">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Alfombras</span><h2 class="h2">Lavado de alfombras en San Isidro</h2>
    <p class="lead">Las alfombras acumulan polvo, manchas y olores que el aspirado solo no quita.</p></div>
    <div class="grid-3">
      {card('Manchas y olores', 'Revisamos la alfombra y te indicamos el tratamiento según su material y el tipo de mancha.', static=True)}
      {card('Cómo traerlas', 'Enrolla la alfombra sin doblarla y tráela a nuestro local de San Isidro. Así llega segura y lista para el proceso.', static=True, delay=.08)}
      {card('Plazo claro', 'Al recibir tu alfombra te indicamos el tratamiento y el plazo de entrega.', static=True, delay=.16)}
    </div>
  </div>
</section>

<section class="section sec-linen" id="cortinas">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Cortinas</span><h2 class="h2">Lavado de cortinas en San Isidro</h2>
    <p class="lead">Las cortinas retienen polvo y olores del ambiente. Cada tela pide un cuidado distinto.</p></div>
    <div class="grid-3">
      {card('Livianas, gruesas o con forro', 'Revisamos la etiqueta y la tela antes de empezar, para definir el tratamiento adecuado.', static=True)}
      {card('Cómo traerlas', 'Retira los ganchos o argollas y tráelas dobladas. Así llegan seguras y listas para el proceso.', static=True, delay=.08)}
      {card('Para casa y oficina', 'Atendemos cortinas de hogares y oficinas. Consulta el plazo por WhatsApp.', static=True, delay=.16)}
    </div>
  </div>
</section>

<section class="section sec-white">
  <div class="container"><div class="prose fade-up">
    <h2>¿Cuándo llevar alfombras y cortinas a una lavandería?</h2>
    <ul>
      <li><strong>Son grandes o pesadas</strong> y no caben o no se manejan bien en una lavadora doméstica.</li>
      <li><strong>Tienen manchas u olores</strong> que no salen con una limpieza casera.</li>
      <li><strong>Son de tela delicada</strong>, con forro o con detalles que pueden dañarse.</li>
      <li><strong>No tienes dónde secarlas</strong> con buena ventilación: la humedad atrapada genera mal olor.</li>
    </ul>
    <p>Si además quieres renovar tu cama, mira el servicio de <a href="/lavado-de-edredones-y-ropa-de-cama">edredones y ropa de cama</a>.</p>
  </div></div>
</section>

<section class="how section">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:48px;"><h2 class="h2">Cómo lavamos tus alfombras y cortinas</h2></div>
    {steps_html()}
  </div>
</section>'''
    return service_page(
        path,
        'Lavado de alfombras y cortinas en San Isidro | Aquapress',
        'Lavado de alfombras y cortinas en San Isidro. Tráelas a nuestro local en Av. del Parque Sur 193 o consulta por WhatsApp.',
        'lavado de alfombras, lavado de cortinas, lavandería de alfombras, limpieza de cortinas, lavar alfombras San Isidro, lavandería de cortinas Lima',
        'Lavado de alfombras y cortinas <em>en San Isidro</em>',
        'Lavamos alfombras y cortinas de casa y oficina. Tráelas a nuestro local de San Isidro o consulta por WhatsApp.',
        'Hogar y decoración',
        img('cortinas-beige-alfombra-sala', 'Cortinas de lino beige frente a una ventana luminosa en una sala de tonos neutros: lavado de cortinas y alfombras', eager=True),
        'Hola, quisiera información sobre el lavado de alfombras o cortinas',
        secs, faqs,
        'Lavado de alfombras y cortinas', 'Lavado de alfombras y cortinas de hogares y oficinas en San Isidro, Lima.',
        'Lavado de alfombras y cortinas', 'Renueva tu hogar', 'Escríbenos por WhatsApp y coordina la entrega de tus alfombras o cortinas en nuestro local.',
        'Alfombras y cortinas',
        split=('cortinas', 'Cortinas de lino color arena junto a un ventanal en una sala luminosa y minimalista: lavado de cortinas y alfombras'))


def zapatillas():
    path = '/lavado-de-zapatillas'
    faqs = [
        ('¿Lavan zapatillas blancas?',
         'Sí. Al recibirlas revisamos su estado y material, y te indicamos qué resultado se puede esperar según el desgaste y las manchas.'),
        ('¿Pueden dañar mis zapatillas?',
         'Por eso las revisamos antes de empezar: el material (tela, cuero, gamuza o sintético) define el tratamiento. Si una zapatilla tiene riesgo, te lo decimos antes.'),
        ('¿Por qué no es buena idea lavarlas en la lavadora?',
         'La lavadora y el secado con calor pueden despegar la suela, deformar la zapatilla y desteñir los colores. Lee más en <a href="/blog/como-lavar-zapatillas">cómo lavar zapatillas sin dañarlas</a>.'),
        ('¿Cuánto demora y hacen recojo a domicilio?',
         'Al recibirlas te indicamos el plazo de entrega. También coordinamos <a href="/recojo-a-domicilio-lavanderia">recojo a domicilio</a> en San Isidro, San Borja, Surquillo y Miraflores.'),
        EXPRESS_FAQ,
    ]
    secs = f'''<section class="section sec-white" id="zapatillas">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Calzado</span><h2 class="h2">Qué zapatillas puedes traer</h2>
    <p class="lead">Cada material pide un tratamiento distinto. Por eso revisamos cada par antes de empezar.</p></div>
    <div class="grid-3">
      {card('Deportivas y de running', 'Zapatillas de uso diario o de entrenamiento, con tela, malla o materiales sintéticos.', ['Deportivas', 'Running'], static=True)}
      {card('Urbanas y blancas', 'Zapatillas blancas o de colores claros que muestran cada marca de uso.', ['Urbanas', 'Blancas'], static=True, delay=.08)}
      {card('Cuero y gamuza', 'Materiales delicados que se evalúan con cuidado antes de decidir el tratamiento.', ['Cuero', 'Gamuza'], static=True, delay=.16)}
    </div>
  </div>
</section>

<section class="section sec-linen">
  <div class="container"><div class="prose fade-up">
    <h2>Por qué conviene dejar tus zapatillas en manos de una lavandería</h2>
    <p>Una zapatilla combina tela, goma, pegamento y a veces cuero o gamuza. Meterla a la lavadora o secarla al sol o con calor puede despegar la suela, deformar la horma y desteñir los colores.</p>
    <ul>
      <li><strong>Revisión previa:</strong> miramos el material, el desgaste y las manchas antes de decidir el tratamiento.</li>
      <li><strong>Tratamiento según el material</strong>, no el mismo para todas.</li>
      <li><strong>Plazo claro:</strong> al recibirlas te indicamos cuánto demoran.</li>
    </ul>
    <p>Entre limpiezas, un paño apenas húmedo para el polvo superficial ayuda a mantenerlas. Para suciedad profunda, manchas o materiales delicados, tráelas a Aquapress. Si buscas más detalles, lee <a href="/blog/como-lavar-zapatillas">cómo lavar zapatillas sin dañarlas</a>.</p>
  </div></div>
</section>

<section class="how section">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:48px;"><h2 class="h2">Cómo lavamos tus zapatillas</h2></div>
    {steps_html()}
  </div>
</section>'''
    return service_page(
        path,
        'Lavado de zapatillas en San Isidro | Aquapress',
        'Lavado de zapatillas en San Isidro según su material: deportivas, blancas, de cuero y gamuza. Recojo a domicilio. Consulta por WhatsApp.',
        'lavado de zapatillas, lavandería de zapatillas, limpieza de zapatillas, lavar zapatillas blancas, lavado de zapatillas San Isidro',
        'Lavado de zapatillas <em>en San Isidro</em>',
        'Limpiamos tus zapatillas según su material, con revisión previa para definir el tratamiento. Déjalas en San Isidro o consulta el recojo por WhatsApp.',
        'Calzado',
        img('zapatillas-blancas-lona', 'Zapatillas blancas de lona sobre una tela blanca: servicio de lavado de zapatillas', eager=True),
        'Hola, quisiera información sobre el lavado de zapatillas',
        secs, faqs,
        'Lavado de zapatillas', 'Lavado de zapatillas deportivas, urbanas, blancas, de cuero y gamuza en San Isidro, Lima.',
        'Lavado de zapatillas', 'Devuélvele la vida a tus zapatillas', 'Escríbenos por WhatsApp o tráelas a nuestro local de San Isidro.',
        'Zapatillas',
        split=('zapatillas', 'Zapatilla deportiva blanca y naranja, limpia, sobre un fondo gris claro: lavado de zapatillas'))


def vestidos():
    path = '/lavado-de-vestidos-de-novia-y-fiesta'
    faqs = [
        ('¿Limpian vestidos de novia con pedrería y encajes?',
         'Sí. Antes de empezar revisamos la tela, la pedrería, los encajes y las costuras para definir el tratamiento adecuado.'),
        ('¿Con cuánto tiempo debo traer mi vestido?',
         'Te recomendamos traerlo con anticipación a tu evento. Al recibirlo te indicamos el plazo de entrega, y siempre es mejor dejar margen.'),
        ('¿Pueden quitar manchas antiguas?',
         'Depende de la mancha, la tela y el tiempo que lleva. Lo evaluamos al recibir el vestido y te decimos con claridad qué se puede lograr.'),
        ('¿Limpian el vestido después del evento?',
         'Sí. Las manchas de comida, maquillaje o polvo se tratan mejor cuanto antes. Puedes traerlo después del evento para su limpieza.'),
        ('¿Hacen recojo a domicilio de vestidos?',
         'Consulta disponibilidad por WhatsApp. Coordinamos <a href="/recojo-a-domicilio-lavanderia">recojo a domicilio</a> en San Isidro, San Borja, Surquillo y Miraflores.'),
        EXPRESS_FAQ,
    ]
    secs = f'''<section class="section sec-white" id="vestidos-de-novia">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Vestidos de novia</span><h2 class="h2">Limpieza de vestidos de novia en San Isidro</h2>
    <p class="lead">Un vestido de novia es una prenda única. Lo tratamos con revisión individual y sin apuro.</p></div>
    <div class="grid-3">
      {card('Revisión individual', 'Revisamos tela, pedrería, encajes y costuras para definir el tratamiento antes de empezar.', static=True)}
      {card('Con tiempo antes del evento', 'Tráelo con anticipación. Así hay margen para cualquier ajuste del plazo de entrega.', static=True, delay=.08)}
      {card('Después del gran día', 'También limpiamos el vestido tras el evento: las manchas se tratan mejor cuanto antes.', static=True, delay=.16)}
    </div>
  </div>
</section>

<section class="section sec-linen" id="vestidos-de-fiesta">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Fiesta y gala</span><h2 class="h2">Lavado de vestidos de fiesta y de noche</h2>
    <p class="lead">Telas finas, brillos y acabados delicados que merecen cuidado profesional.</p></div>
    <div class="grid-3">
      {card('Vestidos de noche', 'Telas finas y acabados delicados que se limpian mejor de forma profesional.', ['Vestidos de noche'], static=True)}
      {card('Vestidos de fiesta', 'Para bodas, graduaciones y eventos: déjalo listo para la próxima ocasión.', ['Vestidos de fiesta'], static=True, delay=.08)}
      {card('Pedrería y aplicaciones', 'Prendas con pedrería o encajes se evalúan una por una antes de definir el tratamiento.', ['Pedrería', 'Encajes'], static=True, delay=.16)}
    </div>
  </div>
</section>

<section class="section sec-white">
  <div class="container"><div class="prose fade-up">
    <h2>Cómo traer tu vestido a la lavandería</h2>
    <ul>
      <li><strong>Tráelo sin planchar ni tratar</strong> las manchas con productos caseros: pueden fijarse o dañar la tela.</li>
      <li><strong>Cuéntanos qué se manchó</strong> y cuándo: nos ayuda a elegir el tratamiento.</li>
      <li><strong>Llévalo colgado o en una funda de tela</strong>, nunca arrugado dentro de una bolsa de plástico.</li>
      <li><strong>Avísanos si tienes fecha de evento</strong> para organizar el plazo contigo.</li>
    </ul>
    <p>Para más prendas delicadas, mira nuestra <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>.</p>
  </div></div>
</section>

<section class="how section">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:48px;"><h2 class="h2">Cómo cuidamos tu vestido</h2></div>
    {steps_html()}
  </div>
</section>'''
    return service_page(
        path,
        'Lavado de vestidos de novia en San Isidro | Aquapress',
        'Lavado de vestidos de novia, de fiesta y de noche en San Isidro, con pedrería y encajes. Revisión individual y recojo a domicilio.',
        'lavado de vestidos de novia, limpieza de vestido de novia, lavado de vestidos de fiesta, vestido de novia tintorería, limpiar vestido con pedrería',
        'Lavado de vestidos de novia y de fiesta <em>en San Isidro</em>',
        'Cuidamos vestidos de novia, de noche y de fiesta, incluso con pedrería y encajes, con revisión individual antes de definir el tratamiento.',
        'Ocasiones especiales',
        img('vestido-novia-colgado-ventana', 'Vestido de novia de encaje y tul colgado de una percha de madera junto a una ventana: limpieza de vestidos de novia y de fiesta', eager=True),
        'Hola, quisiera información sobre la limpieza de un vestido',
        secs, faqs,
        'Lavado de vestidos de novia y de fiesta', 'Lavado y limpieza de vestidos de novia, de fiesta y de noche, con pedrería y encajes, en San Isidro, Lima.',
        'Lavado de vestidos', 'Confía tu vestido a especialistas', 'Escríbenos por WhatsApp y te orientamos sobre el tratamiento ideal.',
        'Vestidos de novia y de fiesta',
        split=('vestidos', 'Vestido de novia de encaje y tul colgado en una habitación luminosa con ventana: limpieza de vestidos de novia'))


def ternos():
    path = '/lavado-de-ternos-y-corbatas'
    faqs = [
        ('¿Limpian ternos completos y sacos por separado?',
         'Sí. Limpiamos el terno completo (saco y pantalón), sacos y pantalones de vestir por separado, y corbatas.'),
        ('¿Por qué un terno no debe ir a la lavadora?',
         'Un terno tiene entretela, hombreras y forro que dan estructura. El agua y el centrifugado pueden deformarlo, por eso se limpia en seco. Lee la guía <a href="/blog/como-lavar-un-terno">cómo lavar un terno y cada cuánto limpiarlo</a>.'),
        ('¿Cada cuánto conviene limpiar un terno?',
         'Depende del uso, pero conviene limpiarlo cuando tiene manchas u olores y antes de guardarlo por temporadas. Una limpieza demasiado frecuente no es necesaria si lo cuidas entre usos.'),
        ('¿Limpian corbatas?',
         'Sí. Las corbatas son de telas delicadas como la seda y se limpian con cuidado para no marcarlas ni deformarlas. Puedes traerlas junto con tu terno.'),
        ('¿Hacen recojo a domicilio de ternos?',
         'Sí. Coordinamos el <a href="/recojo-a-domicilio-lavanderia">recojo y la entrega a domicilio</a> de tus ternos en San Isidro, San Borja, Surquillo y Miraflores. Escríbenos por WhatsApp.'),
        ('¿Cuánto demora la limpieza de un terno?',
         'Al recibir tu terno te indicamos el plazo de entrega. Si tienes una fecha importante, avísanos al traerlo.'),
    ]
    secs = f'''<section class="section sec-white" id="ternos">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Ropa formal</span><h2 class="h2">Limpieza de ternos en San Isidro</h2>
    <p class="lead">Un buen terno es una inversión. Lo limpiamos con el cuidado que su estructura y su tela necesitan.</p></div>
    <div class="grid-3">
      {card('Terno completo', 'Saco y pantalón limpios y cuidados para que conserven su forma, su caída y su color.', ['Terno', 'Saco', 'Pantalón'], static=True)}
      {card('Sacos y pantalones de vestir', 'Si solo necesitas limpiar una pieza, también la recibimos por separado.', ['Sacos', 'Pantalones de vestir'], static=True, delay=.08)}
      {card('Recojo y entrega', 'Coordinamos el recojo y la entrega a domicilio de tus ternos por WhatsApp.', static=True, delay=.16)}
    </div>
  </div>
</section>

<section class="section sec-linen" id="corbatas">
  <div class="container">
    <div class="section-head fade-up"><span class="tag">Corbatas</span><h2 class="h2">Limpieza de corbatas</h2>
    <p class="lead">Seda y telas finas que se marcan con facilidad. Una mancha de comida no tiene por qué arruinarla.</p></div>
    <div class="grid-3">
      {card('Corbatas de seda', 'Las revisamos una por una antes de elegir el tratamiento, para no dañar la tela.', static=True)}
      {card('Manchas de comida', 'Salsas, grasa o vino se tratan mejor cuanto antes. Tráela sin frotar la mancha.', static=True, delay=.08)}
      {card('Junto con tu terno', 'Trae tu corbata con el terno y recibe todo el conjunto limpio en un solo servicio.', static=True, delay=.16)}
    </div>
  </div>
</section>

<section class="section sec-white">
  <div class="container"><div class="prose fade-up">
    <h2>Cuándo llevar tu terno a la tintorería</h2>
    <ul>
      <li><strong>Tiene manchas u olores</strong> de comida, sudor o humo que no salen con un cepillado.</li>
      <li><strong>Vas a guardarlo</strong> por una temporada: guardarlo sucio atrae polillas y fija las manchas.</li>
      <li><strong>Tienes un evento importante:</strong> una reunión, una boda o una entrevista. Avísanos la fecha al traerlo.</li>
      <li><strong>Lo usas seguido en la oficina:</strong> una limpieza a tiempo ayuda a que dure más.</li>
    </ul>
    <p>Para más prendas delicadas, mira nuestra <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>.</p>
  </div></div>
</section>

<section class="how section">
  <div class="container">
    <div class="text-center fade-up" style="margin-bottom:48px;"><h2 class="h2">Cómo cuidamos tu terno</h2></div>
    {steps_html()}
  </div>
</section>'''
    return service_page(
        path,
        'Lavado de ternos y corbatas en San Isidro | Aquapress',
        'Limpieza de ternos, sacos y corbatas en San Isidro, con recojo y entrega a domicilio en San Borja, Surquillo y Miraflores. Consulta por WhatsApp.',
        'lavado de ternos, tintorería de ternos, limpieza de ternos San Isidro, lavado de corbatas, limpieza de corbatas, lavar saco, tintorería ternos Lima',
        'Lavado de ternos y corbatas <em>en San Isidro</em>',
        'Limpiamos ternos, sacos y corbatas con el cuidado que merece tu ropa formal. Visítanos en San Isidro o coordina el recojo a domicilio.',
        'Ropa formal',
        img('ternos-corbatas-novio-traje', 'Detalle de un terno azul grisáceo con corbata de lunares y flores en el bolsillo: limpieza de ternos y corbatas', eager=True, big=True, w=800, h=533),
        'Hola, quisiera información sobre la limpieza de ternos o corbatas',
        secs, faqs,
        'Lavado de ternos y corbatas', 'Limpieza de ternos, sacos y corbatas en San Isidro, Lima, con recojo y entrega a domicilio.',
        'Lavado de ternos y corbatas', 'Luce impecable en cada ocasión', 'Escríbenos por WhatsApp y coordina la limpieza de tu terno o tus corbatas.',
        'Ternos y corbatas',
        split=('ternos', 'Corbatas de seda de distintos colores y estampados colgadas en fila: limpieza de corbatas'),
        og=dict(og_image='/images/og-lavado-de-ternos-y-corbatas.jpg', og_alt='Detalle de un terno azul grisáceo con corbata de lunares y flores en el bolsillo: limpieza de ternos y corbatas en Aquapress'))

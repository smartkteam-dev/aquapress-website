from lib import wa


def cta(text, label, wa_text):
    return f'''<div class="callout">
  <p>{text}</p>
  <a class="btn btn-primary" href="{wa(wa_text)}" target="_blank" rel="noopener noreferrer">{label}</a>
</div>'''


POSTS = [
    # ------------------------------------------------------------------ 1
    {
        'slug': 'guardar-ropa-de-invierno-antes-del-verano',
        'title': 'Guardar ropa de invierno antes del verano | Aquapress',
        'h1': 'Cómo guardar la ropa de invierno antes del verano',
        'desc': 'Limpia, seca y guarda bien tus abrigos, chompas y ternos para que salgan impecables el próximo invierno. Guía práctica para Lima.',
        'kw': 'guardar ropa de invierno, cómo guardar ropa de temporada, limpiar abrigos antes de guardar, polillas en la ropa, ropa de invierno Lima',
        'img': 'chompas-tejidas-dobladas', 'og': 'og-guardar-ropa-de-invierno',
        'alt': 'Persona cargando chompas tejidas dobladas para guardar la ropa de invierno',
        'section': 'Cuidado de ropa', 'read': '5',
        'summary': 'Por qué conviene limpiar antes de guardar y cómo almacenar abrigos, chompas y ternos para que no se manchen, huelan mal ni se llenen de polillas.',
        'body': '''<p>En Lima, el invierno se alarga hasta septiembre u octubre, y cuando llega el verano toca guardar los abrigos, las chompas y los ternos de abrigo. Hacerlo mal es la causa más común de manchas amarillas, malos olores y polillas. Esta guía te explica cómo guardar la ropa de invierno para que salga impecable el próximo año.</p>

<h2>Por qué hay que limpiar antes de guardar</h2>
<p>Una prenda que se ve limpia puede no estarlo. El sudor, la grasa de la piel, el perfume y los restos de comida casi no se notan, pero con el tiempo se oxidan y dejan manchas amarillas que ya no salen. Además, esos restos atraen a las polillas, y la humedad de Lima favorece la aparición de hongos y malos olores en la ropa guardada.</p>
''' + cta('<strong>Lo más seguro:</strong> llevar tus abrigos, chompas y ternos a una <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a> antes de guardarlos. En Aquapress los revisamos prenda por prenda.', 'Consultar por WhatsApp', 'Hola, quisiera limpiar mis abrigos antes de guardarlos') + '''

<h2>Qué traer a Aquapress antes de guardar</h2>
<p>Estas prendas se guardan mejor después de una limpieza profesional, porque la suciedad invisible es la que más daña con el tiempo:</p>
<ul>
  <li>Abrigos y sacones.</li>
  <li>Ternos y prendas con forro o estructura.</li>
  <li>Chompas de alpaca y lana fina (mira por qué en <a href="/blog/como-lavar-chompa-de-alpaca">cómo lavar una chompa de alpaca</a>).</li>
  <li>Prendas de cuero o gamuza.</li>
  <li>Vestidos y prendas con pedrería.</li>
  <li>Edredones y mantas de invierno: mira <a href="/lavado-de-edredones-y-ropa-de-cama">lavado de edredones y ropa de cama</a>.</li>
</ul>

<h2>Cómo guardar la ropa de invierno, paso a paso</h2>

<h3>1. Separa la ropa según su cuidado</h3>
<p>Revisa la etiqueta de cada prenda y arma grupos: lo que se lava en casa (algodón, polares), lo que requiere cuidado especial (alpaca, lana fina) y lo que debe ir a tintorería.</p>

<h3>2. Guarda solo prendas limpias y secas</h3>
<p>Aunque la hayas usado una sola vez, limpia cada prenda antes de guardarla. Y asegúrate de que esté completamente seca: la humedad residual causa moho y olor.</p>

<h3>3. Dobla o cuelga según el tipo de prenda</h3>
<ul>
  <li><strong>Chompas y tejidos:</strong> dóblalos. Colgados, el peso estira los hombros y los deforma.</li>
  <li><strong>Abrigos, sacos y ternos:</strong> cuélgalos en perchas anchas que respeten la forma de los hombros.</li>
  <li><strong>Vestidos delicados:</strong> guárdalos en fundas de tela, no de plástico.</li>
</ul>

<h3>4. Elige bien dónde guardarlos</h3>
<p>Usa cajas o fundas de tela transpirable. Evita las bolsas de plástico selladas: atrapan la humedad. Para ahuyentar polillas, el cedro y la lavanda son buenas opciones; la naftalina tiene olor muy fuerte y es tóxica, así que si decides usarla, que no toque la ropa y ventila bien después.</p>

<h3>5. Busca un lugar fresco, seco y ventilado</h3>
<p>Evita guardar la ropa pegada al piso o a paredes con humedad. Un estante alto, lejos de la luz directa, es lo ideal.</p>

<h2>Checklist rápido</h2>
<ul>
  <li>Todo limpio antes de guardar.</li>
  <li>Todo completamente seco.</li>
  <li>Tejidos doblados y abrigos en percha ancha.</li>
  <li>Fundas o cajas de tela, no bolsas de plástico selladas.</li>
  <li>Cedro o lavanda en lugar de naftalina.</li>
  <li>Lugar fresco, oscuro y ventilado.</li>
</ul>

<h2>Revisa tu ropa guardada cada dos o tres meses</h2>
<p>Abre las cajas, ventila las prendas unas horas y comprueba que no haya humedad ni olores. Detectar un problema a tiempo evita perder una prenda. Y si algo salió con olor o manchas, llévalo a <a href="/lavado-al-peso-y-por-prenda">lavado por prenda</a> o a tintorería antes de usarlo de nuevo.</p>''',
    },
    # ------------------------------------------------------------------ 2
    {
        'slug': 'como-lavar-chompa-de-alpaca',
        'title': 'Cómo lavar una chompa de alpaca sin dañarla | Aquapress',
        'h1': 'Cómo lavar una chompa de alpaca sin dañarla',
        'desc': 'Qué debes saber antes de lavar una chompa de alpaca, los errores que la dañan y cuándo conviene traerla a Aquapress.',
        'kw': 'lavar chompa de alpaca, cómo lavar alpaca, lavar prendas de lana, cuidado de alpaca, tintorería alpaca',
        'img': 'prendas-lana-tejidos-delicados', 'og': 'og-lavar-chompa-de-alpaca',
        'alt': 'Chompas y abrigos de lana beige y marrón colgados en un perchero',
        'section': 'Cuidado de ropa', 'read': '4',
        'summary': 'Por qué la alpaca se daña tan fácil, qué errores evitar y cuándo es mejor traer tu chompa a Aquapress.',
        'body': '''<p>La alpaca es una de las fibras más suaves y valoradas del Perú, pero también una de las más delicadas. Un lavado equivocado puede encogerla, apelmazarla o quitarle la suavidad, y ese daño casi nunca se revierte. Esto es lo que conviene saber antes de lavar tu chompa de alpaca.</p>

<h2>Primero, lee la etiqueta</h2>
<p>La etiqueta de cuidado manda. Si dice <strong>«solo limpieza en seco»</strong>, no la laves en casa. Si permite lavado a mano, ten en cuenta lo que sigue. Y ante una mancha de grasa, vino o comida, no la frotes: eso la fija y daña la fibra.</p>

<h2>Por qué la alpaca se daña tan fácil</h2>
<ul>
  <li><strong>El agua caliente y la fricción</strong> hacen que la fibra se afieltre y se encoja.</li>
  <li><strong>Mojada pesa mucho</strong> y, si se cuelga, se estira y pierde la forma.</li>
  <li><strong>Los detergentes fuertes</strong> le quitan la suavidad natural.</li>
  <li><strong>El calor y el sol directo</strong> la resecan y cambian el color.</li>
</ul>
''' + cta('<strong>¿Tu chompa es importante para ti?</strong> En Aquapress limpiamos alpaca, lana, abrigos y sacones con nuestro servicio de <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>. La revisamos y elegimos el tratamiento adecuado.', 'Consultar por WhatsApp', 'Hola, quisiera información sobre limpieza de prendas de alpaca') + '''

<h2>Si decides lavarla en casa: lo mínimo que debes cuidar</h2>
<ul>
  <li>Usa agua fría o apenas tibia y un detergente suave para lana, en poca cantidad.</li>
  <li>Presiona suavemente; nunca frotes ni retuerzas.</li>
  <li>Enjuaga con agua de la misma temperatura hasta eliminar la espuma.</li>
  <li>Sécala extendida sobre una superficie plana, a la sombra, sin colgarla.</li>
  <li>Nada de secadora, plancha caliente ni sol directo.</li>
</ul>
<p>Aun así, el resultado depende del tipo de alpaca, del tejido y de cómo se manipule. Por eso, para una prenda que quieres conservar muchos inviernos, lo más seguro es dejarla a profesionales.</p>

<h2>Cuándo traer tu chompa de alpaca a Aquapress</h2>
<ul>
  <li>La etiqueta indica limpieza en seco.</li>
  <li>Es un abrigo, un saco o una prenda con forro o estructura.</li>
  <li>Tiene manchas de grasa, vino, maquillaje o comida.</li>
  <li>Es una prenda de valor, o un regalo, y no quieres arriesgarla.</li>
  <li>Ya perdió forma o suavidad y quieres recuperarla.</li>
</ul>
<p>Además, antes de guardarla al final del invierno, conviene limpiarla: lee <a href="/blog/guardar-ropa-de-invierno-antes-del-verano">cómo guardar la ropa de invierno</a>.</p>

<h2>¿Y las bolitas (pilling)?</h2>
<p>Es normal que las prendas de alpaca formen pequeñas bolitas con el uso. Retíralas con cuidado, con un peine para tejidos o una máquina quitapelusas, sin jalar con los dedos.</p>''',
    },
    # ------------------------------------------------------------------ 3
    {
        'slug': 'cada-cuanto-lavar-un-edredon',
        'title': 'Cada cuánto lavar un edredón y cómo hacerlo | Aquapress',
        'h1': 'Cada cuánto lavar un edredón y cómo hacerlo',
        'desc': 'Descubre cada cuánto lavar un edredón, por qué en casa suele salir mal y cuándo conviene traerlo a Aquapress.',
        'kw': 'cada cuánto lavar un edredón, cómo lavar un edredón, lavar edredón queen, secar edredón, lavandería de edredones',
        'img': 'edredon-blanco-cojines-beige', 'og': 'og-cada-cuanto-lavar-un-edredon',
        'alt': 'Cama con edredón blanco, cojines de lino beige y cubrecama acolchado en tonos neutros',
        'section': 'Ropa de cama', 'read': '4',
        'summary': 'Frecuencia recomendada, qué suele salir mal al lavar un edredón en casa y señales de que es mejor traerlo a Aquapress.',
        'body': '''<p>El edredón acumula polvo, sudor y ácaros aunque se vea limpio. Lavarlo bien alarga su vida y mejora el descanso, pero un lavado mal hecho puede dejar humedad, malos olores o un relleno apelmazado. Aquí tienes la frecuencia recomendada y lo que conviene saber antes de lavarlo.</p>

<h2>Cada cuánto lavar un edredón</h2>
<p>Como referencia general:</p>
<ul>
  <li><strong>Funda y sábanas:</strong> cada una o dos semanas.</li>
  <li><strong>Edredón (el relleno):</strong> unas dos a cuatro veces al año, según el uso.</li>
  <li><strong>Mantas polares y cobertores:</strong> cada uno o dos meses si se usan a diario.</li>
</ul>
<p>Si en casa hay personas con alergias, niños o mascotas, conviene lavarlos con más frecuencia. Una funda protectora lavable ayuda a espaciar los lavados del edredón.</p>

<h2>¿Se puede lavar un edredón en casa?</h2>
<p>Depende de la etiqueta y del tamaño, pero en la práctica muchas veces sale mal. Un edredón de 1 plaza a veces entra en una lavadora doméstica grande; uno <strong>queen o king</strong> casi nunca cabe bien.</p>
<h3>Lo que suele salir mal en casa</h3>
<ul>
  <li>Se enjuaga mal y el detergente queda atrapado en el relleno.</li>
  <li>El relleno se apelmaza y se forman bultos.</li>
  <li>Queda humedad adentro: aparecen el mal olor y el moho, algo frecuente con la humedad de Lima.</li>
  <li>La lavadora se sobrecarga y puede dañarse.</li>
</ul>
''' + cta('<strong>¿Tu edredón es grande?</strong> En Aquapress lavamos edredones de 1 y 2 plazas, queen y king, y mantas polares. Mira nuestro servicio de <a href="/lavado-de-edredones-y-ropa-de-cama">lavado de edredones y ropa de cama</a>.', 'Consultar por WhatsApp', 'Hola, quisiera información sobre el lavado de edredones') + '''

<h2>Cuándo conviene traer el edredón a Aquapress</h2>
<ul>
  <li>Es queen o king, o no cabe cómodamente en tu lavadora.</li>
  <li>No tienes dónde secarlo por completo con buena ventilación.</li>
  <li>Tiene manchas o olores que no salen con un lavado casero.</li>
  <li>Es de plumas o de un relleno delicado.</li>
  <li>Prefieres ahorrar tiempo y esfuerzo.</li>
</ul>
<p>Si prefieres no cargarlo, coordinamos el <a href="/recojo-a-domicilio-lavanderia">recojo a domicilio</a> en San Isidro, San Borja, Surquillo y Miraflores.</p>

<h2>Si el tuyo es pequeño y la etiqueta lo permite</h2>
<p>Lávalo solo, con un ciclo suave, agua fría o tibia y poco detergente suave. Agrega un enjuague extra y, sobre todo, asegúrate de que seque <strong>completamente</strong> antes de guardarlo o usarlo.</p>

<h2>Cómo mantenerlo limpio por más tiempo</h2>
<ul>
  <li>Usa una funda lavable y cámbiala con frecuencia.</li>
  <li>Ventila el edredón al menos una vez por semana al hacer la cama.</li>
  <li>Evita comer en la cama y acostarte con ropa de calle.</li>
</ul>
<p>Para el resto del hogar, mira también el lavado de <a href="/lavado-de-alfombras-y-cortinas">alfombras y cortinas</a>.</p>''',
    },
    # ------------------------------------------------------------------ 4
    {
        'slug': 'que-es-el-lavado-en-seco',
        'title': '¿Qué es el lavado en seco y cómo funciona? | Aquapress',
        'h1': '¿Qué es el lavado en seco y cuándo lo necesita tu ropa?',
        'desc': 'Qué es el lavado en seco, cómo funciona, qué prendas lo necesitan y por qué no es lo mismo que lavar en casa. Guía de Aquapress.',
        'kw': 'qué es el lavado en seco, lavado en seco, cómo funciona el lavado al seco, dry cleaning, tintorería, ropa dry clean only',
        'img': 'prendas-fundas-plastico-tintoreria', 'og': 'og-lavado-en-seco',
        'alt': 'Prendas colgadas con fundas de plástico en una tintorería, listas para entregar',
        'section': 'Tintorería', 'read': '4',
        'summary': 'Qué es realmente el lavado en seco, cómo funciona, qué prendas lo necesitan y cuándo conviene traerlo a Aquapress.',
        'body': '''<p>Seguro viste en alguna etiqueta la frase «solo limpieza en seco» o «dry clean only». ¿Qué significa realmente? El lavado en seco (en inglés, <em>dry cleaning</em>) no es tan «seco» como parece, y entender cómo funciona te ayuda a decidir qué prendas traer a Aquapress.</p>

<h2>Qué es el lavado en seco</h2>
<p>Es un método de limpieza que usa <strong>solventes especiales en lugar de agua</strong>. Esos solventes disuelven la grasa y las manchas sin mojar las fibras como lo hace el agua, por eso se usa en prendas que podrían encogerse, deformarse o desteñir con un lavado normal.</p>

<h2>Cómo funciona, a grandes rasgos</h2>
<ol>
  <li><strong>Revisión:</strong> se inspecciona la prenda, la etiqueta, las manchas y los detalles como botones o forros.</li>
  <li><strong>Tratamiento de manchas:</strong> se tratan las manchas antes de la limpieza.</li>
  <li><strong>Limpieza con solvente</strong> en una máquina diseñada para ello.</li>
  <li><strong>Acabado:</strong> se plancha o se da forma a la prenda para devolverla lista.</li>
</ol>
<p>Cada paso requiere equipo y experiencia, y por eso este proceso no se puede replicar bien en casa.</p>

<h2>Qué prendas necesitan lavado en seco</h2>
<ul>
  <li>Ternos, sacos y abrigos: tienen forro, entretela y estructura.</li>
  <li>Prendas de lana fina, alpaca, cashmere o seda.</li>
  <li>Cuero y gamuza.</li>
  <li>Vestidos de novia, de noche y de fiesta, sobre todo con pedrería o encajes.</li>
  <li>Cualquier prenda cuya etiqueta diga «solo limpieza en seco».</li>
</ul>
''' + cta('<strong>¿No sabes si tu prenda lo necesita?</strong> Llévala a Aquapress: la revisamos y te decimos qué tratamiento conviene. Mira nuestro servicio de <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>.', 'Consultar por WhatsApp', 'Hola, quisiera saber si mi prenda necesita lavado en seco') + '''

<h2>Mitos frecuentes</h2>
<h3>«El lavado en seco daña la ropa»</h3>
<p>Un lavado mal hecho daña la ropa, sea en seco o en agua. Hecho por profesionales, es la forma más segura de limpiar muchas prendas delicadas.</p>
<h3>«Basta con rociar un producto para refrescar»</h3>
<p>Existen productos para refrescar la ropa en casa, pero no sustituyen una limpieza profesional en prendas de valor: no tratan manchas profundas ni devuelven la forma.</p>
<h3>«Hay que llevar todo a la tintorería cada semana»</h3>
<p>No. Conviene limpiar en seco cuando hace falta, no más de lo necesario. Entre limpiezas, ventilar y cepillar ayuda a mantener la prenda.</p>

<h2>¿Y el resto de la ropa?</h2>
<p>La ropa de uso diario se lava mejor al agua: mira el <a href="/lavado-al-peso-y-por-prenda">lavado al peso y por prenda</a>. Si dudas entre uno y otro, lee también <a href="/blog/como-lavar-un-terno">cómo lavar un terno</a>.</p>''',
    },
    # ------------------------------------------------------------------ 5
    {
        'slug': 'como-lavar-un-terno',
        'title': 'Cómo lavar un terno y cada cuánto limpiarlo | Aquapress',
        'h1': 'Cómo lavar un terno y cuidarlo para que dure',
        'desc': 'Cómo lavar un terno sin deformarlo, cada cuánto limpiarlo y qué cuidar entre limpiezas. Consejos de Aquapress, tintorería en San Isidro.',
        'kw': 'cómo lavar un terno, lavar un terno, limpiar un terno, cada cuánto lavar un terno, tintorería de ternos, cuidado del terno',
        'img': 'saco-negro-colgado-terno', 'og': 'og-como-lavar-un-terno',
        'alt': 'Saco negro de terno con camisa colgado en la pared',
        'section': 'Tintorería', 'read': '4',
        'summary': 'Por qué un terno no va a la lavadora, cada cuánto limpiarlo y qué hacer entre limpiezas para que dure.',
        'body': '''<p>Un terno es una de las prendas más caras del guardarropa, y una de las más fáciles de arruinar. La respuesta corta a «¿cómo lavar un terno?» es: <strong>casi nunca en casa</strong>. Te explicamos por qué y cómo cuidarlo entre limpiezas.</p>

<h2>Por qué un terno no debe ir a la lavadora</h2>
<p>Un terno no es una tela plana: tiene entretela, hombreras, forro y costuras pensadas para dar estructura. El agua, el centrifugado y el calor pueden:</p>
<ul>
  <li>Deformar los hombros y las solapas.</li>
  <li>Hacer que el forro y la tela encojan de forma distinta, y el saco quede «arrugado» por dentro.</li>
  <li>Desteñir el color o dejar brillos en la tela.</li>
</ul>
<p>Por eso la mayoría de los ternos se limpian en seco, un proceso que cuida la estructura. Si quieres saber cómo funciona, lee <a href="/blog/que-es-el-lavado-en-seco">qué es el lavado en seco</a>.</p>

<h2>Cada cuánto limpiar un terno</h2>
<p>Como referencia, unas dos a cuatro veces al año según el uso, y antes si hay manchas, olor o si lo usaste en un evento largo. Limpiarlo demasiado seguido también lo desgasta.</p>
''' + cta('<strong>¿Tu terno necesita limpieza?</strong> En Aquapress limpiamos ternos, sacos y corbatas con nuestro servicio de <a href="/tintoreria-lavado-al-seco">tintorería y lavado al seco</a>. Lo revisamos prenda por prenda antes de empezar.', 'Consultar por WhatsApp', 'Hola, quisiera información sobre limpieza de ternos') + '''

<h2>Qué cuidar entre limpiezas</h2>
<ul>
  <li><strong>Cuélgalo en una percha ancha</strong> que respete la forma de los hombros.</li>
  <li><strong>Déjalo ventilar</strong> un rato después de usarlo, antes de guardarlo.</li>
  <li><strong>Cepíllalo suavemente</strong> con un cepillo para ropa para retirar el polvo.</li>
  <li><strong>No lo guardes</strong> en bolsas de plástico selladas: atrapan la humedad.</li>
  <li><strong>Alterna</strong> entre dos ternos si lo usas a diario.</li>
</ul>

<h2>Qué hacer si se mancha</h2>
<p>No frotes: se fija la mancha y se daña la tela. Retira el exceso con un paño limpio, sin presionar, y tráelo cuanto antes a Aquapress. Cuanto más rápido se trate, mejor resultado.</p>

<h2>Errores que dañan un terno</h2>
<ul>
  <li>Lavarlo en lavadora.</li>
  <li>Plancharlo directamente con plancha caliente: puede dejar brillos.</li>
  <li>Guardarlo húmedo o apretado en el clóset.</li>
  <li>Dejarlo meses con manchas sin tratar.</li>
</ul>

<h2>¿Y las camisas?</h2>
<p>Las camisas de vestir sí admiten lavado y planchado: mira nuestro servicio de <a href="/lavado-al-peso-y-por-prenda">lavado por prenda y planchado</a>, y completa tu look para la oficina con una sola visita.</p>''',
    },
    # ------------------------------------------------------------------ 6
    {
        'slug': 'como-lavar-cortinas',
        'title': 'Cómo lavar cortinas y cada cuánto hacerlo | Aquapress',
        'h1': 'Cómo lavar cortinas sin dañarlas',
        'desc': 'Cómo lavar cortinas según su tela, cada cuánto limpiarlas y cuándo conviene traerlas a Aquapress, tu lavandería en San Isidro.',
        'kw': 'cómo lavar cortinas, lavar cortinas, limpieza de cortinas, cada cuánto lavar cortinas, lavandería de cortinas',
        'img': 'cortinas-beige-alfombra-sala', 'og': 'og-como-lavar-cortinas',
        'alt': 'Cortinas de lino beige con tiras en la parte superior frente a una ventana luminosa, en una sala de tonos neutros',
        'section': 'Hogar', 'read': '4',
        'summary': 'Qué tener en cuenta antes de lavar cortinas, cada cuánto hacerlo y cuándo es mejor traerlas a Aquapress.',
        'body': '''<p>Las cortinas retienen polvo, humo, olores y humedad del ambiente, aunque no lo notes. Lavarlas bien las deja frescas y alarga su vida, pero hacerlo en casa tiene sus riesgos: pueden encoger, deformarse o quedar húmedas. Esto es lo que debes saber.</p>

<h2>Cada cuánto lavar las cortinas</h2>
<p>Como referencia, una o dos veces al año. Si vives cerca de una avenida, cocinas con frecuencia cerca de ellas, hay fumadores o alergias en casa, conviene hacerlo con más frecuencia. Entre lavados, sacudirlas o aspirarlas suavemente ayuda a retirar el polvo.</p>

<h2>Por qué lavar cortinas es más difícil de lo que parece</h2>
<ul>
  <li><strong>Cada tela es distinta:</strong> voile, lino, terciopelo, algodón o con forro reaccionan de forma diferente al agua.</li>
  <li><strong>Pueden encoger</strong> y quedar cortas, o deformarse y perder la caída.</li>
  <li><strong>Son grandes y pesadas</strong> cuando se mojan, y la lavadora se sobrecarga.</li>
  <li><strong>Secar bien es clave:</strong> una cortina húmeda huele mal y favorece el moho.</li>
  <li><strong>Los ganchos, argollas y forros</strong> se pueden dañar.</li>
</ul>
''' + cta('<strong>¿Prefieres no arriesgarlas?</strong> En Aquapress lavamos cortinas y alfombras de hogares y oficinas. Mira nuestro servicio de <a href="/lavado-de-alfombras-y-cortinas">lavado de alfombras y cortinas</a>.', 'Consultar por WhatsApp', 'Hola, quisiera información sobre el lavado de cortinas') + '''

<h2>Cuándo conviene traerlas a Aquapress</h2>
<ul>
  <li>Son gruesas, con forro, de terciopelo o de tela delicada.</li>
  <li>Son muy grandes o hay varias.</li>
  <li>No tienes dónde secarlas con buena ventilación.</li>
  <li>Tienen manchas, olor a humo o a humedad.</li>
  <li>La etiqueta recomienda limpieza especial.</li>
</ul>

<h2>Cómo prepararlas antes de traerlas</h2>
<ul>
  <li>Retira los ganchos o argollas.</li>
  <li>Sacúdelas para quitar el polvo suelto.</li>
  <li>Dóblalas con cuidado, sin apretarlas.</li>
  <li>Avísanos si tienen manchas o si alguna tela es especialmente delicada.</li>
</ul>
<p>Si son muchas o pesadas, consulta el <a href="/recojo-a-domicilio-lavanderia">recojo a domicilio</a> por WhatsApp.</p>

<h2>Y para el resto del hogar</h2>
<p>Aprovecha para renovar también tu cama: mira el lavado de <a href="/lavado-de-edredones-y-ropa-de-cama">edredones y ropa de cama</a> y lee <a href="/blog/cada-cuanto-lavar-un-edredon">cada cuánto lavar un edredón</a>.</p>''',
    },
    # ------------------------------------------------------------------ 7
    {
        'slug': 'como-lavar-zapatillas',
        'title': 'Cómo lavar zapatillas sin dañarlas | Aquapress',
        'h1': 'Cómo lavar zapatillas sin dañarlas',
        'desc': 'Qué cuidar al limpiar zapatillas según su material, qué errores las dañan y cuándo conviene traerlas a Aquapress, en San Isidro.',
        'kw': 'cómo lavar zapatillas, lavar zapatillas blancas, limpiar zapatillas, lavar zapatillas en lavadora, lavandería de zapatillas',
        'img': 'zapatillas-blancas-lona', 'og': 'og-como-lavar-zapatillas',
        'alt': 'Zapatillas blancas de lona sobre una tela blanca',
        'section': 'Calzado', 'read': '4',
        'summary': 'Qué cuidar según el material de la zapatilla, los errores que la dañan y cuándo es mejor traerla a Aquapress.',
        'body': '''<p>Unas zapatillas limpias se ven mejor y duran más, pero lavarlas mal es una de las formas más rápidas de arruinarlas. La lavadora, el sol o el calor pueden despegarlas o deformarlas. Esto es lo que debes tener en cuenta.</p>

<h2>El material manda</h2>
<p>No todas las zapatillas se limpian igual:</p>
<ul>
  <li><strong>Tela o malla:</strong> absorben suciedad y manchas con facilidad.</li>
  <li><strong>Cuero y sintético:</strong> se limpian por fuera y toleran poca agua.</li>
  <li><strong>Gamuza o nobuck:</strong> son muy delicadas; el agua las marca y las endurece.</li>
  <li><strong>Suela y pegamento:</strong> son las partes más sensibles al calor y a la humedad.</li>
</ul>

<h2>Por qué la lavadora no es buena idea</h2>
<ul>
  <li>El golpeteo y el centrifugado deforman la horma.</li>
  <li>El agua y el calor pueden despegar la suela.</li>
  <li>Los colores pueden desteñir hacia las partes claras.</li>
  <li>Secarlas con calor (secadora, estufa o sol fuerte) encoge y endurece los materiales.</li>
</ul>
''' + cta('<strong>¿Quieres que queden bien?</strong> En Aquapress lavamos zapatillas según su material, con revisión previa. Mira nuestro servicio de <a href="/lavado-de-zapatillas">lavado de zapatillas</a>.', 'Consultar por WhatsApp', 'Hola, quisiera información sobre el lavado de zapatillas') + '''

<h2>Mantenimiento entre limpiezas</h2>
<p>Para el polvo del día a día, pasa un paño apenas húmedo por la superficie y deja que seque al aire, en un lugar ventilado y a la sombra. Esto ayuda a mantenerlas, pero no sustituye una limpieza a fondo cuando están muy sucias.</p>

<h2>Cuándo traerlas a Aquapress</h2>
<ul>
  <li>Son blancas o claras y tienen manchas marcadas.</li>
  <li>Son de gamuza, nobuck o cuero.</li>
  <li>Tienen mal olor que no se quita.</li>
  <li>Son un par que quieres cuidar o que te costó caro.</li>
  <li>No tienes tiempo o lugar para secarlas bien.</li>
</ul>
<p>Si prefieres no moverte, consulta el <a href="/recojo-a-domicilio-lavanderia">recojo a domicilio</a> por WhatsApp.</p>

<h2>Y el resto de tu ropa deportiva</h2>
<p>Lleva también tu ropa de entrenamiento: con el <a href="/lavado-al-peso-y-por-prenda">lavado al peso</a> no hay mínimo de prendas.</p>''',
    },
]

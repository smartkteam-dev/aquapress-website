# Site generator

The HTML pages in the repo root are generated. To change content, edit `pages_core.py` / `pages_rest.py` (copy), `lib.py` (nav, footer, schema, meta) or `base.css` / `extra.css` (styles), then:

    python3 tools/build_all.py   # rewrites the .html files, assets/styles.css, sitemap.xml, robots.txt, llms.txt, llms-full.txt, site.webmanifest, vercel.json
    python3 tools/verify.py      # SEO checks: one H1, alt text, canonicals, unique titles, sitemap, links

To add a blog post, append an entry to `POSTS` in `pages_rest.py`. The sitemap and blog index update automatically. `tools/` is excluded from deploys via `.vercelignore`.

Blog posts live in `posts.py`. Blog photos are free Unsplash photos (no attribution required). New service pages go in `pages_new.py` and the `SERVICES` list in `lib.py`. The placeholder founding year is `FOUNDED` in `lib.py`.

Reviews on the home page are real Google reviews copied by hand in `pages_core.py` (home()).

## Keyword map

One primary keyword per page and no two pages on the same keyword (SEO standard, Advanced level). The primary keyword belongs in the page's title, H1, first paragraph and URL. Secondary keywords can appear in the copy. Before writing a new page or post, check this table: if its keyword is already taken, improve that page instead.

Keywords are chosen from the services and how people in Lima search; there was no search-volume tool at the time. Check them against the Search Console queries (Performance → Queries) once there is data, and update this table when a page's focus changes.

Intent: **local** = looking for a business nearby, **service** = ready to hire this service, **info** = wants to learn how to do it.

| Page | Primary keyword | Intent | Secondary keywords |
|---|---|---|---|
| `/` | lavandería San Isidro | local | lavandería cerca de mí, Aquapress |
| `/tintoreria-lavado-al-seco` | tintorería San Isidro | service | lavado al seco, abrigos de alpaca, cuero y gamuza |
| `/lavado-al-peso-y-por-prenda` | lavado al peso San Isidro | service | lavado por prenda, planchado de camisas |
| `/lavado-de-ternos-y-corbatas` | lavado de ternos | service | limpieza de corbatas, lavar saco |
| `/lavado-de-edredones-y-ropa-de-cama` | lavado de edredones | service | frazadas, mantas, protectores de colchón |
| `/lavado-de-alfombras-y-cortinas` | lavado de alfombras y cortinas | service | lavandería de cortinas, limpieza de alfombras |
| `/lavado-de-zapatillas` | lavado de zapatillas | service | limpieza de zapatillas, zapatillas blancas |
| `/lavado-de-vestidos-de-novia-y-fiesta` | lavado de vestido de novia | service | vestidos de fiesta, vestidos con pedrería |
| `/recojo-a-domicilio-lavanderia` | lavandería a domicilio | service | recojo de ropa a domicilio, lavandería delivery |
| `/lavanderia-miraflores` | lavandería a domicilio Miraflores | local | tintorería Miraflores |
| `/lavanderia-san-borja` | lavandería a domicilio San Borja | local | tintorería San Borja |
| `/lavanderia-surquillo` | lavandería a domicilio Surquillo | local | tintorería Surquillo |
| `/blog` | consejos para cuidar la ropa | info | cuidado de prendas delicadas |
| `/blog/como-lavar-chompa-de-alpaca` | cómo lavar una chompa de alpaca | info | lavar prendas de lana |
| `/blog/guardar-ropa-de-invierno-antes-del-verano` | cómo guardar ropa de invierno | info | polillas en la ropa |
| `/blog/que-es-el-lavado-en-seco` | qué es el lavado en seco | info | ropa dry clean only |
| `/blog/cada-cuanto-lavar-un-edredon` | cada cuánto lavar un edredón | info | cómo lavar un edredón |
| `/blog/como-lavar-un-terno` | cómo lavar un terno | info | cada cuánto lavar un terno |
| `/blog/como-lavar-cortinas` | cómo lavar cortinas | info | cada cuánto lavar cortinas |
| `/blog/como-lavar-zapatillas` | cómo lavar zapatillas | info | lavar zapatillas blancas en casa |
| `/privacidad` | none (legal page, linked from every footer) | — | — |

Service page vs. blog post on the same subject (e.g. `lavado de ternos` vs. `cómo lavar un terno`) is not a conflict: one is for people ready to hire, the other for people learning, and Google ranks them separately. Each pair links to each other.

Rules for this site:
- Only the home page targets "lavandería San Isidro". Other pages may say "en San Isidro" as the location, but their primary keyword is the service.
- District pages lead with the delivery service ("lavandería a domicilio {district}"), never "lavandería en {district}", because there is no shop there.

## Google Analytics and the privacy page

- The Google tag (`GTAG_ID` / `GTAG_HTML` in `lib.py`) is in every page's head. It loads 2.5 s after the page loads, or at the first scroll/tap/key press, so it doesn't slow the first screen on phones. Visits under ~2.5 s with no interaction aren't counted.
- Click events are sent from `main.js`: `whatsapp_click` and `phone_click` (key events in GA4: these are the leads), `directions_click` (Google Maps links) and `email_click`. Keep the names: GA4 key events match them exactly.
- `verify.py` fails if a page is missing the tag (or has it twice) or if an event name disappears from `main.js`.
- `/privacidad` (`privacidad()` in `pages_rest.py`) describes what Analytics collects and keeps (14 months, set in GA4 Admin → Data retention). If tracking, retention or contact details change, update that page too.

## Generated files: never edit them in the repo root

Every file the build writes is overwritten on the next run, so a hand edit in the root is lost. Edit the source instead:

| Root file | Edit this instead |
|---|---|
| `*.html`, `blog/*.html` | page copy in `pages_core.py` / `pages_new.py` / `pages_rest.py` / `posts.py`; layout and schema in `lib.py` |
| `robots.txt` | `AI_BOTS` list and robots block in `build_all.py` |
| `llms.txt`, `llms-full.txt` | `llms.py` (intro, business facts, blog note); service/post text comes from the page copy automatically |
| `sitemap.xml`, `vercel.json`, `site.webmanifest` | `build_all.py` |

## AI assistants (llms.txt, robots.txt, sameAs)

- `llms.txt` is a short Markdown index for AI assistants (https://llmstxt.org): business facts, every service, the district pages and every blog guide with its summary. `llms-full.txt` holds the full text of every page and blog post in Markdown, with WhatsApp links kept, so an assistant can answer a care question from a guide and link back to it.
- Both are built from the rendered pages and `POSTS`, so a new blog post or service shows up in them with no extra step. `verify.py` fails if any sitemap page is missing from either file.
- `robots.txt` allows everyone and names the main AI crawlers in an explicit allow group. To block one, give it its own `User-agent` group with `Disallow: /` in `build_all.py`.
- The business schema's `sameAs` lists the Google Business Profile (`GBP` in `lib.py`, canonical `?cid=` form of the `MAPS` short link) and Facebook. Add Instagram/TikTok there when they exist.

## Pre-commit hook (blocks stale builds)

Vercel publishes the root files as committed and never runs the build, so `tools/hooks/pre-commit` runs it for you. When a commit touches `tools/` or a generated file, the hook rebuilds the site, runs `verify.py`, and blocks the commit if a check fails or if the rebuilt files aren't staged. Commits that only touch docs skip it.

Enable it once per clone (it's already enabled in the main working copy):

    git config core.hooksPath tools/hooks

Skip it in an emergency with `git commit --no-verify`.

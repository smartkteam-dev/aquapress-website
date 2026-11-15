# Site generator

The HTML pages in the repo root are generated. To change content, edit `pages_core.py` / `pages_rest.py` (copy), `lib.py` (nav, footer, schema, meta) or `base.css` / `extra.css` (styles), then:

    python3 tools/build_all.py   # rewrites the .html files, assets/styles.css, sitemap.xml, robots.txt, llms.txt, llms-full.txt, site.webmanifest, vercel.json
    python3 tools/verify.py      # SEO checks: one H1, alt text, canonicals, unique titles, sitemap, links

To add a blog post, append an entry to `POSTS` in `pages_rest.py`. The sitemap and blog index update automatically. `tools/` is excluded from deploys via `.vercelignore`.

Blog posts live in `posts.py`. Blog photos are free Unsplash photos (no attribution required). New service pages go in `pages_new.py` and the `SERVICES` list in `lib.py`. The placeholder founding year is `FOUNDED` in `lib.py`.

Reviews on the home page are real Google reviews copied by hand in `pages_core.py` (home()).

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

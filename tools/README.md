# Site generator

The HTML pages in the repo root are generated. To change content, edit `pages_core.py` / `pages_rest.py` (copy), `lib.py` (nav, footer, schema, meta) or `base.css` / `extra.css` (styles), then:

    python3 tools/build_all.py   # rewrites the .html files, assets/styles.css, sitemap.xml, vercel.json
    python3 tools/verify.py      # SEO checks: one H1, alt text, canonicals, unique titles, sitemap, links

To add a blog post, append an entry to `POSTS` in `pages_rest.py`. The sitemap and blog index update automatically. `tools/` is excluded from deploys via `.vercelignore`.

Blog posts live in `posts.py`. Blog photos are free Unsplash photos (no attribution required). New service pages go in `pages_new.py` and the `SERVICES` list in `lib.py`. The placeholder founding year is `FOUNDED` in `lib.py`.

Reviews on the home page are real Google reviews copied by hand in `pages_core.py` (home()).

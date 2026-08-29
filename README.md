# SB Tech Website

Source for [tech.sribharathi.com](https://tech.sribharathi.com) — SB Tech's corporate website, covering AI & enterprise software development services and live products.

## Stack

Static HTML5 site built on Bootstrap 5, hosted on GitHub Pages. No server-side code and no build step is required to serve the site — every page is plain, already-rendered HTML, so it works identically on GitHub Pages and with a bare local server (`python -m http.server`).

## Structure

- `index.html`, `about/`, `services/`, `products/`, `contact/` — page content, one directory per clean URL
- `_includes/header.html`, `_includes/footer.html` — the **source of truth** for the shared site header (nav) and footer
- `scripts/render_includes.py` — propagates `_includes/*.html` into every page (see below)
- `css/`, `js/`, `fonts/`, `images/`, `logo/` — site assets
- `sitemap.xml`, `robots.txt`, `404.html`, `.nojekyll`, `CNAME` — GitHub Pages / SEO configuration
- `demo-web-agency-*.html` — thin redirect stubs at legacy URLs, kept so old indexed/bookmarked links still resolve

### Editing the shared header or footer

Each page has the header/footer content inlined between marker comments:

```html
<!-- include:header.html -->
...current header markup, kept in sync automatically...
<!-- /include:header.html -->
```

To change the header or footer everywhere:

1. Edit `_includes/header.html` or `_includes/footer.html` — never edit the markup between the markers directly in a page, it'll just get overwritten.
2. Run `python scripts/render_includes.py` from the repo root. It re-inlines the partial into every page listed in the script.
3. Commit both the `_includes/` change and the updated pages.

## Deployment

Pushing to `main` publishes directly via GitHub Pages using the `CNAME` file for the custom domain — the committed HTML is served as-is.

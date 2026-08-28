# SB Tech Website

Source for [tech.sribharathi.com](https://tech.sribharathi.com) — SB Tech's corporate website, covering AI & enterprise software development services and live products.

## Stack

Static HTML5 site built on Bootstrap 5, hosted on GitHub Pages. No build step or server-side code.

## Structure

- `index.html`, `about/`, `services/`, `products/`, `contact/` — page content, one directory per clean URL
- `css/`, `js/`, `fonts/`, `images/`, `logo/` — site assets
- `sitemap.xml`, `robots.txt`, `404.html`, `.nojekyll`, `CNAME` — GitHub Pages / SEO configuration
- `demo-web-agency-*.html` — thin redirect stubs at legacy URLs, kept so old indexed/bookmarked links still resolve

## Deployment

Pushing to `main` publishes directly via GitHub Pages using the `CNAME` file for the custom domain.

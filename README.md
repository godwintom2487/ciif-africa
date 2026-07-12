# ciif.africa — public website

The public-facing website connecting the world to CIIFA and its platforms, products and programmes.
Static multi-page site — no build step, no framework.

## Deployment

- **Repo:** https://github.com/godwintom2487/ciif-africa (public)
- **Staging (live):** https://godwintom2487.github.io/ciif-africa/ — GitHub Pages, served from the
  `gh-pages` branch (which mirrors `site/`).
- **Redeploy:** run `.\deploy.ps1 "commit message"` from this folder (commits, regenerates
  `gh-pages` via `git subtree split --prefix site`, pushes both branches; Pages rebuilds in ~1 min).

### Cutover to ciif.africa (when approved — currently a live WordPress site is on the domain)

1. Set the custom domain on Pages:
   `gh api -X PUT repos/godwintom2487/ciif-africa/pages -f cname=ciif.africa`
2. In **Cloudflare DNS** for ciif.africa:
   - Replace the apex `A`/`AAAA` records (current WordPress host) with `CNAME ciif.africa → godwintom2487.github.io`
     (Cloudflare flattens CNAME at apex), and set `www` `CNAME → godwintom2487.github.io`.
   - **Do NOT touch MX / mail records** — @ciif.africa email must keep working.
   - Set both records to **DNS-only (grey cloud)** until GitHub issues the TLS certificate.
3. Wait for the certificate on the Pages settings page, then enforce HTTPS:
   `gh api -X PUT repos/godwintom2487/ciif-africa/pages --field https_enforced=true`
4. Optional: re-enable the Cloudflare proxy (orange cloud) with SSL mode **Full (strict)**.
5. Note: the WordPress site remains on its old host, just unreachable via the domain. Export/back
   it up before or after — nothing on it is deleted by this cutover.

## Folder map

```
ciif-africa/
  README.md                      ← this file
  brand/
    CIIFA-Brand-Guide.html       ← standalone brand guide (colour, type, document recipes)
  site/                          ← deploy this folder as the web root
    index.html                   ← Home (tagline, metrics, programmes, partners)
    programmes.html              ← Programmes hub (the 5 buckets)
    impact.html                  ← Impact & track record (metrics, projects, partners)
    about.html                   ← About CIIFA, mission/vision/values + CTF relationship
    events.html                  ← Calendar 2026 → 2028
    news.html                    ← News & stories
    partner.html                 ← Partner With Us
    privacy.html                 ← Privacy Policy (draft — needs legal review)
    terms.html                   ← Terms of Service (draft — needs legal review)
    programmes/
      cba.html                   ← CBA for Africa (placeholder home until its site launches)
      skill-pool.html            ← The Skill Pool Initiative
      enterprise.html            ← Enterprise Programme for Music, Film & Fashion
      career-fair.html           ← The Creative Career Fair
      safehouse.html             ← The CIIFA SafeHouse
    assets/
      css/style.css              ← single shared stylesheet (brand tokens at the top)
      js/nav.js                  ← mobile menu + active nav link
      img/ctf-logo.png           ← CTF logo (not yet placed on a page)
```

## How to add a new programme

1. Copy any file in `site/programmes/` and edit the copy (title, kicker, `--pc` accent colour, copy).
2. Add a card for it on `index.html` and `programmes.html`, and links in every footer "Programmes" column.
3. Pick its accent colour in `assets/css/style.css` `:root` (one new `--xxx` variable) and record it in the brand guide table.

## How to point a bucket at a live programme site

When a programme's real site launches, change its card `href` on `index.html` / `programmes.html`
(and the footer links) from `programmes/xxx.html` to the live URL. Keep the placeholder page —
redirect it or leave it as the archive.

## Content sources

Official copy (tagline, mission/vision/values, impact numbers, projects, SafeHouse facilities
and pricing, contact details) merged 2026-07-12 from the owner's "CIIFA Website code" /
"CIIFA_Website_Source_Code" documents. Contact: info@ciif.africa · +234 817 256 0000 ·
4B Onikoyi Lane, Parkview Estate, Ikoyi, Lagos.

## Pending content (owner to supply)

- **CIIFA logo (vector master)** — the logo now on the site (`assets/img/ciifa-logo.png` +
  `ciifa-logo-dark.png` for dark surfaces) was extracted from the NDA letterhead PDF (raster,
  481×173). Fine for web at nav size; request the AI/SVG master for print/large formats and
  drop it in to replace these. `cba-logo.png` (CBA shield) was extracted from the CBA 2026
  organogram PDF the same way.
- **Social links** — the source docs show X/Instagram/LinkedIn/Facebook icons but no URLs.
- **Business of Film dates** — marked "to be announced" on the Enterprise page.
- **Photography** — currently 16 Unsplash stock photos in `assets/img/photos/` (free Unsplash
  licence, credits in `photos/credits.json`; attribution appreciated but not required).
  Replace with real CIIFA photography (cohorts, SafeHouse, showcases) as it becomes available —
  same filenames, no code changes needed.
- **Blog articles** — the source docs' sample posts were placeholder drafts; not published. News page carries real announcements only.
- **Newsletter** — News page uses a mailto until an email provider is wired up.
- **Privacy Policy / Terms** — drafted 2026-07-12 (`privacy.html`, `terms.html`, linked from every
  footer). Written against the Nigeria Data Protection Act 2023; **have Nigerian counsel review
  both before launch** — especially data-retention specifics, the NDPC complaint language, and
  the liability caps in the Terms.

## Brand tokens (from the CIIFA Operating System)

Lime `#90E040` (accent, never body text on white) · Deep Green `#46760F` (links/emphasis on light) ·
Ink `#111418` · Paper `#f5f7f1` · font **Outfit**. Platform accents: CBA gold `#f0b448`,
Skill Pool lime, Enterprise green `#4ade80`, Career Fair teal `#3fc1c9`, SafeHouse sky `#5aa9ff`,
AMEDI violet `#a78bfa`. Full system: `brand/CIIFA-Brand-Guide.html`.

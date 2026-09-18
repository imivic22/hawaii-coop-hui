# Hawaiʻi Co-op Hui — landing site

Single-page landing site for **Hawaiʻi Co-op Hui**, built to match the team's mockup.
Plain static HTML/CSS/JS — no build step, no dependencies.

## Files
- `index.html` — all page content and structure
- `styles.css` — all styling; **brand tokens live at the top in `:root`**
- `script.js` — mobile menu + active-section nav highlight
- `assets/` — `topo.svg` (background texture); add logo, hero/section photos here

## Run locally
```bash
cd hawaii-coop-hui
python3 -m http.server 8000
# → http://localhost:8000
```

## Sections (single scroll, top-nav anchors)
Hero → About/values (waves + 6 value icons) → Co-op Cohort → Our Work (Learn/Connect/Build)
→ Resources (session recordings) → Get Involved (CTA) → Footer.

## Photos still needed (search `data-todo`)
The mockup uses real photography that isn't in this repo yet — placeholders are in place:
- **Hero** valley/river aerial → set `--hero-image` in `styles.css` to `url("assets/hero.jpg")`
- **Cohort** kalo-planting photo → set as `background-image` on `.cohort__media`
- **Our Work** cards (Learn/Connect/Build) → replace each `.card__img`
- Real, rights-cleared images only — tell me the source and I'll wire them in.

## Other content to confirm
- `express-interest-link` — the Express Interest / sign-up form URL
- Real **recordings** — paste YouTube/Vimeo links; embed template is in the Resources markup
- Final **logo** — swap the inline SVG emblem in the nav + footer
- Copy review — cohort dates (Dec 2026 – Nov 2027) and all Hawaiian text/ʻokina/kahakō

## Brand tokens
Colors, fonts, and radii are CSS custom properties in `:root`. Fonts load from Google Fonts
(Playfair Display / Mulish / Caveat) — change the `<link>` in `index.html` and the
`--font-*` tokens together if the type changes.

## Deploy
Any static host: Netlify/Vercel (drag-and-drop the folder or connect the repo), or GitHub Pages.

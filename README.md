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

## Brand (from the official Hawaiʻi Co-op Hui Brand Guidelines)
Applied from the guidelines PDF:
- **Palette** (CSS tokens in `:root`): Parchment `#fff2ea/#f3e4d7/#d3bdab`, Spectra deep-teal
  `#113137` (dark grounds), Jungle Green `#0a7473/#22a09d` (primary accent), plus Rocky rust
  `#ae562c`, Pixie olive `#8a9140`, Shadow `#a5783c` used across the wave motif.
- **Logo**: the real emblem is in `assets/emblem-light.png` (nav, on parchment) and
  `assets/emblem-dark.png` (footer, on Spectra); `assets/favicon.png` is the tab icon. These
  were extracted from the brand PDF — replace with official exported PNG/SVG when available.
- **Type**: body is **Inter** (brand-exact, Google Fonts). The display face is **Watkins** and
  the secondary is **Rugpull** — neither is web-hosted, so **Playfair Display stands in for the
  display face** for now. To go exact, self-host Watkins/Rugpull (`@font-face`) and update the
  `--font-display` token + the Google Fonts `<link>`.

## Deploy
Any static host: Netlify/Vercel (drag-and-drop the folder or connect the repo), or GitHub Pages.

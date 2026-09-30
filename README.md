# Hawaiʻi Co-op Hui — landing site

Single-page landing site for **Hawaiʻi Co-op Hui**, built to match the team's mockup.
Plain static HTML/CSS/JS — no build step, no dependencies.

## Files
- `index.html` — all page content and structure
- `styles.css` — all styling; **brand tokens live at the top in `:root`**
- `script.js` — mobile menu + active-section nav highlight
- `assets/brand/` — official logos, icons, and seamless pattern (SVG); `assets/` — favicon, og-image; add hero/section photos here

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
- **Logo & assets** (`assets/brand/`, from the official Brand Package, all transparent SVG):
  `logo-primary*.svg` (stacked), `logo-secondary*.svg` (horizontal; Original Color is meant
  for dark backgrounds — "HAWAIʻI" is cream), `emblem*.svg` (the favicon mark), `icon-*.svg`,
  and `pattern.svg` (the seamless brand pattern with its parchment background removed so it
  tiles over any color). The nav pairs the full-color emblem with the Watkins wordmark
  cropped (viewBox only, no path edits) from the all-dark Spectra lockup, at the Secondary
  Logo's own proportions; the footer uses the Parchment lockup intact. `icon-ike.svg` and
  `icon-hana.svg` are companion icons built in the official icon construction — swap in
  official ones if they get made. `favicon.png` / `og-image.png` are downsized from the package.
- **Type**: body is **Inter** (brand-exact, Google Fonts). The display face is **Watkins** and
  the secondary is **Rugpull** — neither is web-hosted, so **Playfair Display stands in for the
  display face** for now. To go exact, self-host Watkins/Rugpull (`@font-face`) and update the
  `--font-display` token + the Google Fonts `<link>`.

## Content, form, and what still needs team sign-off
The expanded copy (Why a co-op, What a co-op can look like, Solidarity economy, Cohort
"aiming for / how we imagine the year / who it's for", FAQ, Start-here links) was drafted from
three references Keoni shared — Democracy at Work Institute's "What is a Worker Cooperative?",
New Economy Coalition's "The Solidarity Economy", and the Upstream podcast "Worker Cooperatives
Pt. 1" — and fact-checked so it states nothing about the program beyond the known facts.
It deliberately avoids: cost, stipends, deadlines, application/selection process, session dates,
participant numbers, staff names, partners beyond the WSARE grant, statistics, and real Hawaiʻi
co-ops (the four examples are labeled "Imagined example").

**Express Interest form** posts to Formspree (`https://formspree.io/f/xvkgydze`, free tier,
notifications to kaimi@purplemaia.org). Handler in `script.js`: background submit, inline
"Mahalo" state, honeypot (`_gotcha`), and a mailto fallback if the action is ever unset.
Formspree emails an ownership confirmation on the very first submission — confirm it once.

**Open for team sign-off before wider promotion:**
1. Audience scope — copy says farmers, ranchers, growers; add fishers / value-added food makers if in scope.
2. Solidarity-economy framing — confirm the Hui identifies with it (lead currently says "a name many people use").
3. "How we imagine the year" (Ground / Learn / Connect / Build) is a proposed arc labeled "a rough shape, not a schedule" — replace with the real plan when it exists.
4. Post-cohort access — copy says the Hui is a network and the cohort is one way in; nothing promised beyond that.
5. Who monitors the form inbox; whether an updates list/newsletter will exist (checkbox is plain email consent).
6. Privacy note says data isn't sold or shared — adjust if WSARE reporting uses participant data.
7. WSARE is not expanded; confirm the full grant name before adding it.
8. Brand line "E kahe ke waiwai" uses *ke* before a w-word (standard would be *ka*) — from the guidelines, so left as-is unless the team wants it changed.

## Deploy
Any static host: Netlify/Vercel (drag-and-drop the folder or connect the repo), or GitHub Pages.

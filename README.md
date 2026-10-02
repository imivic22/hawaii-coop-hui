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

## Pages & sections
`index.html` (single scroll, top-nav anchors): Hero → About/values (wave + 6 line icons) → Co-op Cohort
→ Why a co-op (one section, five accordion dropdowns: what a co-op is · the seven principles · what a
co-op can look like in Hawaiʻi · what the cohort is aiming for · who it's for) → Our Work → Express
Interest form → Footer. `collaboration.html` (nav "Collaboration"): readings/listening links and session recordings,
with room for the food/bill collaboration piece Keoni mentioned; `resources.html` just forwards there. Both pages share `styles.css`/`script.js`; bump the `?v=` on those
links when you change them so visitors don't get a cached copy.
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
  Logo's own proportions; the footer uses the Parchment lockup intact. The values row uses
  `line-*.svg`: outlined single-color versions made from each official icon's own dark layer
  (its ring plus line drawing); `line-ike.svg` and `line-hana.svg` are companion icons in the
  same style — swap in official ones if they get made. `favicon.png` / `og-image.png` are downsized from the package.
- **Type**: body is **Inter** (Google Fonts). The brand display faces are self-hosted in
  `assets/fonts/`: **TAY Watkins** (headings, footer quote) and **TAY Rug Pull** (hero word
  column, the mauka-to-makai statement, the cohort overlay). Both are caps-only and single
  weight, so everything set in them renders in capitals and headings use `font-weight:400`
  with `font-synthesis:none`. Watkins has no kahakō vowels or dashes — keep Hawaiian words with
  kahakō and any em dashes out of Watkins headings (use Rug Pull there). The `-web.woff2` copies
  add one cmap entry mapping the ʻokina (U+02BB) to each font's own ‘ glyph so "Hawaiʻi" renders
  in-font; the originals sit beside them untouched. Check the font license covers web
  self-hosting in a public repo before promoting the site widely.

## Content, form, and what still needs team sign-off
The expanded copy (Why a co-op, What a co-op can look like, Cohort "aiming for / how we
imagine the year / who it's for", Resources links) was drafted from
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
3. A drafted year timeline was removed at the team's request; add a real schedule section once the plan exists.
4. Post-cohort access — copy says the Hui is a network and the cohort is one way in; nothing promised beyond that.
5. Who monitors the form inbox; whether an updates list/newsletter will exist (checkbox is plain email consent).
6. Privacy note says data isn't sold or shared — adjust if WSARE reporting uses participant data.
7. WSARE is not expanded; confirm the full grant name before adding it.
8. Brand line "E kahe ke waiwai" uses *ke* before a w-word (standard would be *ka*) — from the guidelines, so left as-is unless the team wants it changed.

## Wave divider
`assets/brand/wave.svg` (the brush-stroke wave under the hero) is generated, not hand-drawn:
`python3 tools/wave.py assets/brand/wave.svg`. Knobs are at the top of the script — wavelengths
(`L1..L3`), amplitudes (`A1..A3`), the `peaks` list (stroke weights, boldest first; `colors` pairs
to it), `anchors` spread, `drift` range (how much strokes cross) and `random.seed`. Bump the `?v=`
on the `<img>` in `index.html` after regenerating.

## Deploy
Any static host: Netlify/Vercel (drag-and-drop the folder or connect the repo), or GitHub Pages.

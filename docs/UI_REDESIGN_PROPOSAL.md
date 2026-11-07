# UI Redesign Proposal — adopt the Flare Triad on techlib.hilir.app

**Status: APPROVED AND IMPLEMENTED 2026-11-07** (owner: "all follow recommendation, go" —
hilir casing, label-only rows, maturity re-map, dark-first, sticky thead, gold mark +
underlines + headline + stat numbers). All changes in `agent/web.py` (CSS const + `_page`
chrome + home handler + helper chips); every href, input id/name and page JS is
byte-identical — verified by the test suite and rendered-page diff. Live deploy happens with
the next frontend container rebuild. Written 2026-11-07 from a study of the current frontend
(`agent/web.py`), the estate design references
(`hilir-access/docs/DESIGN.md` + `HILIR Landing Page/docs/design.md`) and the access UI source
(`hilir-access/src/v2/pages.ts`).

## 1. Scope — what changes and what never changes

| In scope | Out of scope (byte-identical) |
|---|---|
| Colour theme (Flare Triad tokens, dark-first) | Every href, route and form action |
| Arrangement of header / nav / tabs / home blocks | Every input id, name, query param |
| Button / input sizes (estate control scale) | All page JS (external-link, SQL fill, graph canvas, mermaid) |
| Table + badge restyling | Data-viz dictionaries (SECTOR_COLORS, KIND_COLORS, REL_COLORS, MERMAID) |
| Filter bar restyling | Auth flow, workers, container wiring |

This mirrors the estate rule from `hilir-access/docs/DESIGN.md`: *"Keep every input id, form
name, button handler and endpoint byte-identical when restyling — the dashboard JS is
behaviour, not decoration."*

When implemented this is a **single-file change**: the `CSS` const plus small markup tweaks in
`_page()` / the home handler of `agent/web.py`. No new files, no external fonts/images (same
self-contained rule as the estate), no dependency changes. The frontend Worker's inline
"Sign-in failed" page (`deploy/frontend/src/index.ts`) can adopt the same tokens later as an
optional follow-up.

## 2. Why

- The estate (landing page + hilir Access) runs one visual language; the library is the only
  hilir.app family app not on it. Sign-in now happens at access.hilir.app — users already see
  the Flare Triad the moment they log in.
- Current UI: light-only, hardcoded navy/blue hex scattered through one CSS block, three
  link colours by context, full-grid dense tables (the register page is 400 rows of borders),
  no control scale (buttons ~20px tall, inputs auto-width).
- Token adoption removes the hardcoded palettes and gives dark mode for free.

## 3. Tokens — adopted verbatim from hilir-access

Dark-first; light follows `prefers-color-scheme`. No toggle (estate rule).

| Token | Dark | Light | Library job — used ONLY for |
|---|---|---|---|
| `--action` | `#c2410c` | `#c2410c` | Human action: Search/Filter/Run buttons, brand tile, active-nav emphasis |
| `--action-line` | `#e5672f` | `#b23a0a` | Hover/underline accent, pilot-maturity chip |
| `--info` | `#2dd4bf` | `#0e7f96` | ALL links (replaces `#1a4f8b`), section headings, focus rings, tile arrows, summary |
| `--machine` | `#a78bfa` | `#6d4fc4` | Machine surfaces only: SQL console card, admin cards, footer MCP/REST chips |
| `--ok` / `--danger` | `#4ade80` / `#f87171` | `#15803d` / `#dc2626` | State only: error card, degraded-Neon banner, active chips |
| `--client` | `#e3b341` | `#a16207` | **techlib identity accent (petroleum gold)** — see below |
| `--bg` | `#0f1115` | `#f2f4f5` | Page background |
| `--panel` | `#131519` | `#e9edef` | Header bar, home hero band |
| `--card` | `#1b1e24` | `#ffffff` | Cards, tiles, active tab |
| `--inset` | `#0f1115` | `#f7f9fa` | Inputs, code, pre |
| `--border` / `--border2` | `#2a2e36` / `#34383f` | `#d9dfe3` / `#c3ccd2` | Rules, borders |
| `--text` / `--muted` | `#e8e6e3` / `#8f959d` | `#16283a` / `#5e6b74` | Primary / secondary text |

Violet never appears on the home page, search or account page — machine surfaces only,
per the estate rule ("humans sign in with ember + teal alone" — and the library's human
surfaces stay ember + teal alone).

### 3a. The client accent (new, estate-level convention)

The owner asked for one colour that makes techlib recognisably techlib — other estate
clients will each carry their own accent the same way. Proposal: **`--client`, petroleum
gold** (`#e3b341` dark / `#a16207` light) with one narrow job:

> `--client` = **identity and wayfinding only**: the brand mark tile, headline emphasis
> (`<em>` in the home h1), the active nav/subnav underline (where you are), and the home
> stat numbers. **Never** on buttons, links, badges or state — gold never touches ember's
> or teal's job, so no hue drifts.

This slots beside the three fixed hues without re-skinning any of them (ember stays action,
teal stays information, violet stays machine — the estate rule is intact). Hue check: gold
(~42°) sits far from ember (~20°) in usage because gold is never painted on a control; the
two only ever appear in different roles. Where it shows on every page: the gold brand tile
and the gold active-page underline — the two things you see constantly, which is exactly
what makes the app read as techlib.

## 4. Control scale (estate numbers, applied everywhere)

- Inputs/selects/textareas: min-height 38px, padding 8px 12px; radius 8px; mobile
  `font-size: 16px` (iOS zoom guard)
- Buttons: 38px default (Search in header, Filter); 44–46px for the section primary (home
  hero search); 32px for row-level buttons (none exist today — future-proofing); radius 8px
- Cards: radius 12px, padding 20px (today 8px/1rem)
- Cross-engine rules copied from access: `appearance:none` on buttons/selects but NOT
  checkboxes; select chevron painted with two CSS gradients (no image); `-webkit-font-smoothing`,
  `-webkit-text-size-adjust: 100%`, `-webkit-tap-highlight-color: transparent`; `[hidden]{display:none!important}`

## 5. Header and navigation — same links, new chrome

Current: sticky `#0e2033` navy bar, brand text, 3 nav links, search, ghost Sign out.

Proposed arrangement (identical hrefs and form):

- Brand: inline hilir mark SVG (white stem + teal arch, copied from the access
  `BRAND_HTML`) on a **client-gold tile** — the mark keeps the estate shape, the tile carries
  the techlib accent. Casing choice for the owner: "hilir Technology Library"
  (estate pattern, recommended) vs current "HILIR Technology Library".
- Nav links: muted → text on hover; **active = 2px client-gold underline** (replaces the navy
  pill — wayfinding is the accent's job, buttons stay ember).
- Search box: `--inset` background, `--border`, teal focus ring; Search button 38px ember.
- Sign out: `button.ghost` style — teal text, `--border2` border (it is a secondary action).
- Subnav tabs (second-level row): keep the row and links; active tab = `--card` background +
  client-gold underline, inactive = muted. Tab strip sits on `--panel`, connecting visually to the header.

## 6. Home page — re-arranged, same links

Current order: ① stats card (7 boxed tiles) ② search card ③ sector card ④ Library tiles
⑤ Database tiles — five equal-weight cards. Proposed:

1. **Hero band** (`--panel`, full-width inside container): statement (gold `<em>` emphasis)
   + the big search (input + 44px ember Search) + one line of the current explainer text, muted.
2. **Stat strip** directly under the hero: one slim row — big number (client gold — the
   library's crown-jewel counts; owner can veto this one) + small uppercase muted label,
   no boxes (7 boxes become 7 numbers).
3. **Two-column desktop grid** (stacks on mobile): left "Browse by sector" (dot chips stay,
   sector colours untouched — they are data, not chrome); right "Library".
4. **Library tiles → estate rows** (`a.arow`-style): one row per destination — label, spacer,
   teal arrow. Same 7 hrefs. Optional (owner call): a one-line description per row.
5. **Database rows**: same row treatment, full width, 5 hrefs.
6. **Footer**: licence line muted; "REST API · MCP" as violet machine chips.

## 7. Tables — the register-page fix

- Kill the full cell grid: `th` = 11px uppercase letterspaced muted + border-bottom only;
  `td` = border-bottom only, padding 9px 8px (today: every cell boxed 4-way).
- Drop zebra striping; hover tint instead (`--inset`).
- Links: teal, no underline, hover underline (access `a` rule).
- Maturity badges → outlined chips on estate hues (recommended re-map):
  commercial `--ok`, demonstration `--info`, pilot `--action-line`, lab `--muted`.
  Owner call: keep the current four-colour palette instead if preferred.
- `card` pill → teal info chip; sector badges keep `SECTOR_COLORS` dots.
- Filter bar: 38px controls in a wrapping `.row`-style flex.
- Optional: `position: sticky` thead on the register table (pure CSS, no JS).

## 8. Machine-violet surfaces

- `/database/sql` console card: `card.mach` (violet border) + violet heading.
- `/admin` pages: `card.mach`.
- Footer MCP / REST API chips: violet.
- Everything else stays ember/teal — including `/account` (estate rule: human page).

## 9. Dark mode

`prefers-color-scheme` only, both palettes in one `:root` + one media block (copied from
access). No toggle, no JS. The canvas graph/legend surfaces are already dark; on light theme
they stay dark (intentional — data-viz panels, like mermaid output).

## 10. Implementation shape (after approval)

1. Rewrite the `CSS` const in `agent/web.py` (one block, ~115 → ~260 lines, tokens first).
2. `_page()`: brand mark + nav class wiring (the `active` class already exists), tab strip.
3. Home handler: re-order sections per §6.
4. `_badge` / `_pill` / `_maturity_badge`: token colours.
5. SQL/admin bodies get `card.mach`; footer chips.
6. Verify: both colour schemes in Chrome + Safari, iOS zoom guard, register page with 400
   rows, SQL console, graph + atlas canvases unaffected. Deploy = container rebuild via the
   frontend Worker as usual.

## 11. Open owner decisions

1. Brand casing: "hilir Technology Library" (recommended, estate pattern) vs "HILIR …".
2. Library/Database tiles → rows with one-line descriptions (adds small text) or label-only
   rows (recommended) or keep tile grid.
3. Maturity badge re-map to estate hues (recommended) vs keep current palette.
4. Dark-first confirmed? (recommended — estate default, no toggle).
5. Sticky table header on register: yes/no (recommended yes).
6. Client accent: petroleum gold `#e3b341`/`#a16207` confirmed? And its reach — mark tile +
   underlines (safe), headline `<em>` (recommended), gold stat numbers (toggle in the mock,
   the boldest option). Other estate clients will each pick their own hue with this same
   narrow job.

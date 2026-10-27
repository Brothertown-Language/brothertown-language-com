<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — Brothertown-derived light/dark palette for the abridge theme (brothertown-language-com #16)

The site's color scheme becomes a light/dark pair derived from the Brothertown
Indian Nation website's color scheme, anchored in the colors of its logo —
without duplicating the logo (developer directive, 2026-10-26: "update the
zola theme with an additional light/dark mode setup which matches the color
scheme of the brothertownindians.org website, with a focus on the logo's
colors. We can't duplicate the logo.").

## Problem

The site ships the abridge theme's stock palette (`$color: "orange"` — the
theme's default branch, `sass/abridge.scss` line 11) under the theme's
light/dark switcher (`$abridgeMode: "switcher"`, default `dark`). The palette
is generic theme stock and carries none of the Brothertown Indian Nation's
visual identity. The developer directive chooses the identity source: the BI
website's color scheme, focused on its logo.

Extraction of the BI assets (live, 2026-10-26; sources in References) shows:

- **The header logo** (`BIN_logo_tagline800.png`, 800×200 PNG) is a
  two-tone-teal mark with dark text: dark blue-teal `#006973` (~19% of opaque
  pixels), dark green-teal `#007A6F` (~16%), a light aqua-green cluster
  centering on `#52B2A6` (~21%), deep-teal shading `#00423C` (~3%), near-black
  text/outline (~18%), white (~3%).
- **The favicon-family Tribe Icon** (circular badge) is dark teal `#0F8176`
  (~57% of its opaque pixels) with near-black outline and white marks — the
  badge teal differs from the wordmark teals; both belong to the brand's set
  and are recorded here distinctly.
- **The site's chrome** pairs slate body text `#545e69` and charcoal headings
  `#1e2427` with blue accent `#2d93c5` (links, buttons, active-menu markers)
  and teal-blue accent `#0f889b` (the live customizer value behind the topbar,
  filled buttons, and tags; the theme file's shipped `#cd4335` red is
  overridden live), on a `#ffffff` body over `#1e2427` chrome surfaces, with
  gray-blue structure tones `#e1e7ec`, `#ccd5db`, and muted `#8a949b`.

The logo itself may not be duplicated — no copied asset, no recreation of the
mark; colors are the only borrowed property.

### Interpretation notes

1. "Additional light/dark mode setup" reads as: the theme's existing
   light/dark switcher — already configured and working with the stock
   palettes — gains a Brothertown-derived color scheme: a light palette and a
   dark palette, both mapped from the BI identity. The switcher mechanism
   itself is existing work, not new scope.
2. The mode default stays `dark` (`$switcherDefault` ↔ `js_switcher_default`
   consistency per the SOP's switcher gate); no mode-default change was
   requested.
3. "Matches the color scheme" is implemented as fidelity to the BI palette
   with deliberate adaptations where a raw BI pairing sits below the
   accessibility floor (R-3) — notably light-mode links, where BI's live blue
   `#2d93c5` on white computes to ≈3.5:1 (3.45, script per SC-5's formula,
   2026-10-26); the mapping instead uses darker anchors from the same brand
   set (the logo's dark teals). The floor wins; the anchors stay BI-sourced.
4. The floor scopes exactly its enumerated pairs (R-3). Widget pairings
   outside that set (kbd, buttons, code-copy states…) inherit the mapped role
   values and are covered by the visual mode review (SC-7/SC-9).

## Scope

In-repo deliverables only: the palette override in `sass/abridge.scss` (the
site's single palette/mode file of record per the SOP), the built artifacts it
produces, and this spec's palette anchors of record with provenance. No
template, content, theme-payload, or config changes. Dashboard-side deployment
is untouched (the CI build after merge follows the wiki runbook as usual).

## Requirements

- **R-1** — The site's `sass/abridge.scss` override SHALL supply a
  Brothertown-derived palette pair — a full dark-mode role set and a full
  light-mode role set — through abridge's documented `@use … with` parameter
  mechanism: all 26 palette role variables carried with non-null values
  (`$csd $f1d $f2d $c1d $c2d $c3d $c4d $a1d $a2d $a3d $a4d $cgd $crd` and
  their light twins `$cs $f1 $f2 $c1 $c2 $c3 $c4 $a1 $a2 $a3 $a4 $cg $cr`).
  Mechanism ground (verified from the vendored theme source, 2026-10-26):
  these are module-level `!default` variables in
  `themes/abridge/sass/abridge.scss:94-124`, consumed by the theme's two
  `colors.color(…)` calls (lines 108, 124) whose internal `!default`
  assignments fill only `null` values (`themes/abridge/sass/_colors.scss:32-66`)
  — so supplied non-null role values fully define both palettes under the
  theme's existing switcher emission, independent of the `$color` template
  selection, which may stay in place (inert for the roles supplied). No
  vendored theme file is edited.
- **R-2** — The palette SHALL be built from the extracted BI anchor set
  (the mapping tables below are the palette of record): every role the
  tables assign a direct anchor SHALL land with exactly that hex value; the
  five derived cells (dark `$c2d`, `$a2d`, `$cgd`, `$crd`; light `$a2`) SHALL
  be derived tones recorded in `sass/abridge.scss` with a per-value derivation
  note naming the base anchor and the adjustment reason. The mapping tables
  (and the file's provenance comments) SHALL record the anchor sources —
  logo-extraction vs site-CSS role — with the 2026-10-26 date.
- **R-3** — Both palettes SHALL keep the site legible — this floor guards the
  change against a matched-but-unreadable scheme. The floored pairs (WCAG 2.1
  SC 1.4.3 Level AA, 4.5:1 on normal text; verified live 2026-10-26): body
  text `$f1*`, headers `$f2*`, and links `$a1*`, `$a2*`, `$a4*` against both
  the primary background `$c1*` and the secondary background `$c2*` (20 pairs
  — the `$a1*`/`$a2*`-on-`$c2*` pairs are the striped-table-row and
  code-block link surfaces), the header-link hover `$a3*` against the primary
  background only (2 pairs — h1/h2 links render on `$c1*`), the
  highlighted-mark pair (`$c1` text on the `$c4` mark background; 2 pairs),
  and the ins/del accents `$cg*`/`$cr*` against the primary background (4
  pairs — floored on `$c1*` only, so light mode keeps the favicon teal
  `#0F8176` and the BI stylesheet red `#cd4335` as unmodified anchors: they
  clear 4.5:1 on `#ffffff`, not on `#e1e7ec`). The mapping tables resolve
  each fidelity-vs-floor conflict per Interpretation notes 3–4.
- **R-4** — The BIN logo SHALL NOT be duplicated: the repository and the
  built output SHALL carry no copy of the BIN logo asset files (no
  byte-identical or resized copy) and no reference or hotlink to
  brothertownindians.org asset URLs, and the served site SHALL carry no
  recreation of the BI logo mark — no redrawn, vectorized, or
  derivative-image copy of it, at any size or placement. The palettes derive
  from colors only.
- **R-5** — The visitor-facing switcher SHALL keep working as it does today:
  `$abridgeMode: "switcher"`, `$switcherDefault: "dark"` (still equal to the
  config's `js_switcher_default: "dark"` — the theme contract), dark mode as
  the page default, light mode reachable through the toggle, with the theme's
  persistence behavior unchanged.
- **R-6** — The change SHALL pass the SOP's verification gates (build exit 0
  with the pinned-version build-log line; `./zola check` with no new warnings
  against the recorded zero-warning baseline of 2026-10-26; navigation and
  built-output surfaces unchanged per SOP gates 2–3; the switcher-consistency
  gate unchanged), and the change SHALL be confined to palette surfaces:
  `sass/abridge.scss` plus the compiled palette values in `abridge.css` — no
  navigation, content, template, or built-output-class changes.

## Palette mapping of record

Dark mode — the page default; emitted to the `:root:not(.switch)` block per
the theme's switcher contract with `$switcherDefault: "dark"`:

| Role (meaning) | Variable | Value | Source |
|---|---|---|---|
| color-scheme flag | `$csd` | `dark` | theme contract (mode flag, not a color) |
| body text | `$f1d` | `#e1e7ec` | BI site CSS — gridline gray |
| headers, site title, nav | `$f2d` | `#52B2A6` | logo — light aqua |
| primary background | `$c1d` | `#1e2427` | BI site CSS — charcoal chrome (titlebar/footer) |
| secondary background | `$c2d` | derived | charcoal–teal tint, lighter than `$c1d`, kept dark enough for R-3 |
| table rows, quote edge, borders | `$c3d` | `#00423C` | logo — deep-teal shading |
| disabled, mark background | `$c4d` | `#8a949b` | BI site CSS — muted gray |
| link color | `$a1d` | `#52B2A6` | logo — light aqua |
| link hover/focus | `$a2d` | derived | aqua tint brighter than `$a1d`, meeting R-3 on `$c1d` and `$c2d`; note recorded |
| h1–h2 link hover/focus | `$a3d` | `#2d93c5` | BI site CSS — blue accent (meets R-3 on `$c1d`) |
| link visited | `$a4d` | `#8a949b` | BI site CSS — muted gray |
| ins / success | `$cgd` | derived | favicon teal `#0F8176` adjusted to meet R-3 on `$c1d` |
| del / errors | `$crd` | derived | BI stylesheet red `#cd4335` adjusted to meet R-3 on `$c1d` |

Light mode — the toggle target; emitted to the `:root.switch` block per the
theme's switcher contract with `$switcherDefault: "dark"`:

| Role (meaning) | Variable | Value | Source |
|---|---|---|---|
| color-scheme flag | `$cs` | `light` | theme contract (mode flag, not a color) |
| body text | `$f1` | `#545e69` | BI site CSS — body slate |
| headers | `$f2` | `#1e2427` | BI site CSS — headings charcoal |
| primary background | `$c1` | `#ffffff` | BI site CSS — body background |
| secondary background | `$c2` | `#e1e7ec` | BI site CSS — gridline gray |
| table rows, quote edge, borders | `$c3` | `#ccd5db` | BI site CSS — light gray-blue |
| disabled, mark background | `$c4` | `#545e69` | BI site CSS — body slate (the mark text pair `$c1` on `$c4` stays light-on-dark) |
| link color | `$a1` | `#006973` | logo — dark blue-teal |
| link hover/focus | `$a2` | derived | teal between the wordmark teals `#006973`/`#007A6F`, tuned to meet R-3 on `$c1` and `$c2`; note recorded |
| h1–h2 link hover/focus | `$a3` | `#265e88` | BI site CSS — dark blue |
| link visited | `$a4` | `#00423C` | logo — deep teal |
| ins / success | `$cg` | `#0F8176` | favicon — Tribe Icon badge fill |
| del / errors | `$cr` | `#cd4335` | BI site CSS — stylesheet red (theme-file default accent, overridden live; used here only as the error accent) |

Not mapped, recorded for provenance: the logo's near-black text/outline family
and white (rendered by the theme through `$f1*`/`$c1*` roles instead, so the
BI black-on-white text pattern becomes the light mode, and its inverse the
dark mode); the favicon's shading tones `#1C625B`/`#1E504B`; BI's mobile
topbar near-white `#f6f5f5`.

## Success criteria

| ID | Criterion | Class | Instrument |
|----|-----------|-------|-----------|
| SC-1 | `sass/abridge.scss` supplies both palettes per R-1: every one of the 26 named role variables is carried in the `@use … with` override with a non-null value | structural | file check: read `sass/abridge.scss`; assert each of the 26 variables appears with a concrete value; a missing or null-variable role fails |
| SC-2 | The compiled stylesheet exposes both palettes: `public/abridge.css` carries a `:root:not(.switch)` block with the dark-mode role values and a `:root.switch` block with the light-mode role values (the theme's switcher emission with `$switcherDefault: "dark"`) | structural | run `./build.sh`; extract the `--f1`, `--c1`, and `--a1` custom-property values from both blocks of `public/abridge.css`; assert each equals its mapping-table dark resp. light value |
| SC-3 | Direct-anchor fidelity: every mapping-table cell assigned a direct anchor lands in the compiled CSS with exactly that hex value — the 8 dark color cells (`$f1d $f2d $c1d $c3d $c4d $a1d $a3d $a4d`) and the 11 light color cells (`$f1 $f2 $c1 $c2 $c3 $c4 $a1 $a3 $a4 $cg $cr`) | structural | extract every `--` custom property from both blocks of `public/abridge.css`; compare each direct-anchor role's value to the mapping table; any mismatch fails |
| SC-4 | Derived tones are recorded: each of the five derived cells (dark `$c2d`, `$a2d`, `$cgd`, `$crd`; light `$a2`) exists in the compiled CSS with its mapped role value, and `sass/abridge.scss` carries a derivation note per derived value naming the base anchor and the adjustment reason | structural | grep the compiled blocks for the five roles; read `sass/abridge.scss` for the five derivation notes; either missing fails |
| SC-5 | The R-3 floor holds: all 28 floored pairs enumerated in R-3 meet ≥ 4.5:1 | structural | script the WCAG 2.1 relative-luminance contrast ratio (`(L1+0.05)/(L2+0.05)`, the SC 1.4.3 formula) over the extracted compiled values for R-3's 28 enumerated pairs; any ratio < 4.5 fails |
| SC-6 | The SOP gates pass per R-6: `./build.sh` exits 0 with the pinned-version build-log line; `./zola check` reports no new warning against the recorded zero-warning baseline (2026-10-26); the navigation surface and built-output classes are unchanged; `$switcherDefault` and `js_switcher_default` stay equal ("dark") | behavioral | run the SOP's verification gates (build, check, nav-surface enumeration, built-output classes, switcher-consistency values) and compare to the recorded baseline |
| SC-7 | Runtime modes behave as R-5 states: the served site's default render is the dark palette, the toggle applies the light palette, and both mode blocks are present in the served CSS | behavioral | run `./zola serve`; fetch the served `abridge.css` and assert both blocks; capture default-render and post-toggle screenshots; a vision-capable sub-agent reviews them per the multimodal dispatch rule and reports whether the two modes show the mapped palettes |
| SC-8 | No BIN logo duplication — fact-checkable parts of R-4: the tracked tree and the built output carry no byte-copy of the BIN logo asset files and no reference/hotlink to brothertownindians.org asset URLs | structural | hash-compare tracked files and `public/**` against the hash of the extraction's downloaded logo assets; grep the tracked tree and `public/**` for `brothertownindians.org` URLs; no hit passes (the spec and the research artifact's prose references are not asset copies) |
| SC-9 | No BIN logo duplication — visual part of R-4: the served site carries no recreation of the BI logo mark (no redrawn, vectorized, or derivative-image copy, at any size or placement) | behavioral | the SC-7 captures plus the served-site review are checked for any BIN-mark reproduction; the multimodal-dispatch sub-agent's report and (at the pre-PR presentation) the developer's own review are the evidence |
| SC-10 | The file's provenance record: `sass/abridge.scss` carries provenance comments recording each direct anchor's source class (logo-extraction vs site-CSS role) and the 2026-10-26 extraction date — the file remains the palette of record, self-describing | structural | content check of `sass/abridge.scss`: every direct anchor's source class stated, and the 2026-10-26 extraction date stated; for the five derived cells, SC-4's derivation notes carry the base anchors; anything unstated fails |

Evidence types over the whole set: the research extraction record (YAML, with
source URLs, pixel-share method, and sub-agent provenance — filed under this
issue's `research/`), build and check logs, compiled-CSS extractions, the
contrast script's output, and both-mode screenshots with the vision sub-agent's
report.

## Out of scope

- Syntax-highlighting palette re-skin: `$color-syntax` stays `"abridge"`
  (code blocks keep the stock syntax colors until code-heavy content lands —
  revisitable then).
- The site's own logo, favicon, and brand-mark design (untouched — the header
  keeps its current title-based branding).
- Abridge mode mechanics beyond the palette values: the switcher script,
  localStorage persistence, `auto` (prefers-color-scheme) behavior are
  unchanged, as is the mode default (`dark`).
- Re-vendoring the theme (stays at the recorded revision; the theme payload is
  untouched by this change), theme template changes, content changes in any
  section, `zola.toml` changes.
- Deployment/dashboard operations (the post-merge CI build follows the wiki
  runbook) and any cloud-side work.

## Approach

Replace the stock-template palettes with the mapped Brothertown-derived pair
through the one sanctioned surface — the `sass/abridge.scss` `@use … with`
override — keeping the vendored theme byte-identical (no `_colors.scss` edit;
the SOP's re-vendor procedure stays clobber-proof). Dark mode becomes the BI
site's dark chrome — charcoal `#1e2427` surfaces with the logo's light aqua as
the header/link accent and the BI blue `#2d93c5` as the heading-link hover —
and light mode becomes the BI site's own light body — white ground, slate
text, charcoal headings, with the logo's dark teals as links and the favicon
badge teal as the success accent. Structure tones (gridlines, muted gray)
carry over directly from the BI scheme. Where R-3's floor requires it (dark
mode's `$c2d`/`$a2d`/`$cgd`/`$crd` and the light hover tone `$a2`), a derived
tint is used and recorded
with its derivation note in the same file, which becomes the palette of record
(the SOP already designates it as the single palette/mode file). Verification
runs the SOP gates plus the compiled-value assertions (SC-2 through SC-5) and
the served-site mode renders (SC-7/SC-9 — screenshots reviewed by a dispatched
vision-capable sub-agent, with the developer's pre-PR presentation of the
served site as the settled repo gate). The palette work needs no build-system,
config, or theme-payload change; the rendered result is presented for visual
acceptance before any PR.

## Dependencies

- Extraction of record: the color research performed live 2026-10-26 by a
  dispatched research sub-agent (provenance and method in the filed
  `research/` artifact; the analysis model is identified there).
- The pre-PR served-site presentation (the repo's standing review gate —
  open issue `brothertown-language-com#13`): SC-7's/SC-9's visual evidence and
  the presentation to the developer ride that gate's procedure.
- Issue `brothertown-language-com#1` landed (theme vendored, override file,
  switcher config all exist) — satisfied; nothing here blocks on an absent
  upstream artifact.

## References

- Logo of record — header logo:
  `https://brothertownindians.org/wp-content/uploads/2022/05/BIN_logo_tagline800.png`
  (800×200 PNG, RGBA; rendered as the site's `.header-titlebar__logo-image`,
  confirmed in the fetched homepage HTML, 2026-10-26). Pixel analysis
  (Pillow, alpha ≥ 64 threshold, clustered shares) — the wordmark teal set
  `#006973`/`#007A6F`/`#52B2A6`-cluster/`#00423C` with near-black text and
  white.
- Logo of record — favicon family:
  `https://brothertownindians.org/wp-content/uploads/2022/03/cropped-Tribe_Icon512-1-180x180.png`
  (analyzed size; the 512 master was not discoverable from HTML — noted gap)
  — badge fill `#0F8176` (~57% of opaque pixels), near-black outline, white
  marks, shading `#1C625B`/`#1E504B`.
- BI site chrome — homepage `https://brothertownindians.org/` (WordPress,
  theme Pressville 2.6.6) with its `skins/default.css` stylesheet and the
  live customizer's inline color-scheme CSS, fetched 2026-10-26 — body slate
  `#545e69`, headings/footers charcoal `#1e2427`, blue accent `#2d93c5`
  (70 selector occurrences in the theme file), live secondary accent
  `#0f889b` (inline override; the theme file's shipped red `#cd4335` is
  overridden live), structure grays `#e1e7ec`/`#ccd5db`/`#8a949b`, alert blue
  `#265e88`. Gap recorded: accents are customizer-emitted — a future
  customizer change on their side would alter those values; recheck before
  reuse.
- WCAG 2.1 SC 1.4.3 "Contrast (Minimum)" — the 4.5:1 Level-AA threshold and
  the relative-luminance contrast formula (`(L1+0.05)/(L2+0.05)`);
  `https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html`
  (verified live 2026-10-26).
- Theme mechanism (verified from the vendored source, 2026-10-26):
  `themes/abridge/sass/abridge.scss` (module-level `!default` role variables,
  lines 94–152; the switcher's two emitted blocks, lines 360–396) and
  `themes/abridge/sass/_colors.scss` (the `color()` branch function whose
  `!default` fallbacks fill only null role values, lines 32–136); the site's
  override `sass/abridge.scss`; the switcher config contract in `zola.toml`
  (`js_switcher`, `js_switcher_default`) and its SOP gate.
- SOP gates and warning baseline: `docs/sop-site-setup.md` (baseline: zero
  warnings, 2026-10-26; gate list).

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
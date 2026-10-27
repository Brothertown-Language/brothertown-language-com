<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Plan — Brothertown-derived light/dark palette for the abridge theme (brothertown-language-com #16)

Plan from the validated spec (`.issues/16/spec.md`, R-1..R-6 / SC-1..SC-10),
mapping tables are the palette of record. State consumed at planning: the
override file `sass/abridge.scss` currently supplies the stock orange
template through `$color: "orange"` and none of the 26 palette role
variables; the theme mechanism confirmed against the vendored source
(`themes/abridge/sass/abridge.scss` 94–124, 360–396; `_colors.scss` 32–66).
Scope of record: the tracked-repo change touches exactly `sass/abridge.scss`
plus the compiled output it produces ($color stays "orange" — inert for the
roles supplied, kept with an annotation).

## Workflow wrapper for every item

Git per the repo cards: `git-workflow-branch` first — branch
`feature/16-bi-palette` off a fresh, current `main` — then the item edits,
per-item commit (conventional prefix), and the repo's verification gates.
The pre-PR served-site presentation (SOP; spec Dependencies) is a stage
boundary after verification, not a plan item.

## Items (RED → GREEN → verification, dependency-ordered)

- **P-1 — SC-1, SC-10, SC-4 (file half).** Deliverable: the derived-tone
  computation and the full palette authoring of `sass/abridge.scss`.
  RED: SC-1's file check fails against the current file — none of the 26
  role variables is supplied; SC-10's provenance content is absent; SC-4's
  five derivation notes are absent. GREEN: (a) compute the five derived
  values numerically — a WCAG relative-luminance script derives each value
  as the anchor-family member meeting its R-3 constraint set
  (`$c2d` ≤ 4.5-against for `$a4d` on `$c2d` while lighter than `$c1d` with
  the charcoal–teal tint; `$a2d` brighter than `$a1d` meeting R-3 on both
  `$c1d`/`$c2d`; `$cgd` favicon teal brightened to ≥ 4.5 on `$c1d` and
  `$c2d`; `$crd` red brightened to ≥ 4.5 on `$c1d` and `$c2d`; `$a2` teal
  between `#006973`/`#007A6F` meeting R-3 on `#ffffff` and `#e1e7ec`) — the
  script asserts the chosen values satisfy every floored pair involving
  them, with its printed ratios kept as evidence; (b) author the
  `@use … with` override: all 26 role variables (13 dark: `$csd $f1d $f2d
  $c1d $c2d $c3d $c4d $a1d $a2d $a3d $a4d $cgd $crd`; 13 light: `$cs $f1
  $f2 $c1 $c2 $c3 $c4 $a1 $a2 $a3 $a4 $cg $cr`) with the mapping-table
  values and the five computed derived values; the five per-value
  derivation notes (base anchor + adjustment reason); the provenance
  comment block (direct-anchor source class — logo-extraction vs site-CSS
  role — and the 2026-10-26 extraction date); the existing non-palette
  parameters and the `.imgfloat` block unchanged; `$color` annotated as
  inert for supplied roles. Verification: SC-1's 26-variable file check;
  SC-10's content check (source classes + date stated for every direct
  anchor); SC-4's file-side note check; the derivation script's printed
  ratios. No vendored theme file edited.
- **P-2 — SC-2, SC-3, SC-4 (compiled half), SC-5.** Deliverable:
  compiled-value extraction and fidelity/floor assertion over the built
  stylesheet (one script run, its sections asserting each SC separately so
  a failure pinpoints the SC). RED: on the pre-change build, extraction
  against the mapping tables fails — the stock orange palettes are emitted
  (`--f1`/`--c1`/`--a1` carry orange values, not the mapped dark `#e1e7ec`
  / `#1e2427` / `#52b2a6` and light `#545e69` / `#ffffff` / `#006973`).
  GREEN: none beyond P-1's file when the extraction passes; re-tune via
  P-1's script and re-build for any drifted value. Verification: run
  `./build.sh` (exit 0; pinned-version log line — the SC-6 build gate
  evidence too); extraction over `public/abridge.css`'s
  `:root:not(.switch)` and `:root.switch` blocks comparing
  case-insensitively (minifier may lowercase/shorten hex): SC-2's
  `--f1`/`--c1`/`--a1` in both blocks equal their mapped values; SC-3's
  8 dark + 11 light direct-anchor cells exact; SC-4's five roles present
  in the compiled blocks; SC-5's script computes the WCAG 2.1 SC 1.4.3
  ratio over R-3's 28 enumerated pairs, every ratio ≥ 4.5 printed. All
  outputs kept as evidence.
- **P-3 — SC-8.** Deliverable: no-logo-duplication fact sweep (negative
  guard). RED: the sweep is unrun — the fact of "no copy, no hotlink, no
  recreation" is unrecorded for this change (any hit fails). GREEN: none
  expected; a hit is remediated immediately (remove the offending file/
  reference) and re-swept. Verification: (a) fetch the two logo assets of
  record to `/tmp/opencode` if absent (their URLs are in the research
  artifact), sha256 them; hash-compare
  every file in the tracked tree (`git ls-files`) and in `public/**`
  against those hashes; (b) grep the tracked tree and `public/**` for
  `brothertownindians.org`; (c) image-dimension/duplicate-content scan of
  `public/**` for the logo's 800×200 aspect and the favicon 180×180 mark —
  no candidate matches (no resized copy). Sweep output recorded.
- **P-4 — SC-6.** Deliverable: the SC-6-gated subset of the SOP's
  verification gates run over the changed site (build, check
  warning-baseline, navigation, built-output, switcher consistency). RED: the gates are unrun with the new palette — the recorded
  state for this change does not exist (any mismatch fails). GREEN: fix
  what a failing gate names (expected: only palette-file corrections per
  P-1/P-2's surfaces). Verification: gate 1 — build exit 0 with the
  pinned-version build-log line (from P-2's run); the check rule —
  `./zola check`
  reports its line counts with zero warnings against the 2026-10-26
  zero-warning baseline; gate 2 — the built pages' navigation links are
  exactly `/`, `/about/`, `/blog/`; gate 3 — every built file falls in the
  SOP's class list (compiled Sass output class now carries the new values);
  gate 4 — `$switcherDefault` = `js_switcher_default` = `"dark"`. Gate
  outputs recorded.
- **P-5 — SC-7 + SC-9.** Deliverable: runtime mode evidence and the visual
  no-recreation check. RED: the modes are unobserved — no captured
  evidence exists. GREEN: capture and review; no site change expected.
  Verification: run `./zola serve`; assert the served `abridge.css`
  carries both mode blocks; capture default-render and post-toggle
  screenshots per the playwright-cli card (default dark render; light
  after operating the toggle); dispatch one vision-capable sub-agent per
  the multimodal-dispatch card to review the captures and the served site
  for SC-7 (the two modes show the mapped palettes) and SC-9 (no BIN-mark
  reproduction at any size or placement); its report is the evidence. The
  developer's own SC-9 review rides the pre-PR presentation (stage
  boundary — disclosed in Dependencies; not a plan item).

## Deferred

- SC-7/SC-9's developer-side evidence half (the developer's own review of
  the presented served site) — executes at the pre-PR presentation gate
  per the SOP; disclosed here, not silently dropped.

## Dependencies

- Item order: P-1 (author) → P-2 (build+extract; re-tunes via P-1's script
  if needed) → P-3, P-4 (fact sweeps and gates over the built site) →
  P-5 (runtime evidence). P-3/P-4 share P-2's build artifact; no cycles.
- The vendored theme stays byte-identical (P-1 touches only the root
  override file) — the SOP's re-vendor safety property is preserved by
  construction.
- Zola pin unchanged (`ZOLA_VERSION` v0.23.6; the SOP's pin-currency gate
  re-run is not triggered — no tooling touch beyond the palette override
  file).
- Pre-PR presentation (serve + present) after verification; the PR itself
  is a later stage boundary.

## Traceability

| Item | Spec criteria |
|------|----------------|
| P-1 | SC-1, SC-10, SC-4 (file half) |
| P-2 | SC-2, SC-3, SC-4 (compiled half), SC-5 |
| P-3 | SC-8 |
| P-4 | SC-6 |
| P-5 | SC-7, SC-9 |

All SC-1..SC-10 covered; no item without a criterion (SC-7/SC-9's
developer-review half deferred above).

## References (deck copies in this repo, existence-checked 2026-10-27)

- Spec of record: `.issues/16/spec.md`; research artifact:
  `.issues/16/research/bi-colors-2026-10-26.yaml`.
- SOP gates + baselines: `docs/sop-site-setup.md`.
- Theme mechanism ground: `themes/abridge/sass/abridge.scss`,
  `themes/abridge/sass/_colors.scss`.
- Workflow cards: skills `work`, `git-workflow-branch`,
  `git-workflow-commit`, `implement`, `verify`, `git-workflow-pr`;
  `zola` (modify/review + debug-build references), `playwright-cli`
  (captures), `multimodal-dispatch` (vision review) — all present at
  `.opencode/skills/<name>/` in this repo's deck copy.

## Enforcement gate

- Every item's edits land on the feature branch, never `main` (hooks
  enforce).
- Structural instruments are agent-run scripts/commands; their outputs are
  the recorded evidence for the fresh-context verify dispatch (one
  reviewer, per the verify card).
- The served-site presentation and the developer response precede any PR
  filing.

## Cost frame

One-file authoring edit + one computed-derivation script + one build and
one `zola check` (re-run on retune) + two sweeps + a serve-and-capture
session + one vision review dispatch. No config, template, content, or
theme-payload change; build-system untouched.

## Not included

- Syntax-highlighting palette re-skin (`$color-syntax` stays "abridge").
- Site logo/favicon/brand-mark design; any BIN logo asset in any form.
- Switcher script or persistence behavior changes; mode default stays dark.
- Re-vendoring, templates, content, `zola.toml`, deployment/dashboard work.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
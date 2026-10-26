<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — Base Zola site setup (brothertown-language-com #1)

The Brothertown Language project's public website pre-setup: select and
scaffold the correct site platform, skeleton, build entry, and hosting wiring —
without building the entire site up front (developer framing, 2026-10-25).

## Problem

The repository `Brothertown-Language/brothertown-language-com` exists in
bootstrap state only (README, AGENTS, `.gitignore`, deck mount, hooks). No
site shape exists. The developer's directive (2026-10-25): create the repo,
then the first issue ticket for the base Zola setup with the SOP and the
reference materials agents need — the setup selection being the deliverable of
the 2026-10-25 brainstorm recorded in the issue store and in AGENTS.md's
decisions-of-record section. On 2026-10-26 the developer's directives
supersede parts of the recorded basis: use the latest versions of things; use
the latest recommendations; do not cargo-cult the sibling site's Pages-era
mechanics — "don't assume prior code is the correct thing to do." Live docs
(verified 2026-10-26) show Cloudflare recommending Workers as the primary
platform ("Start new projects with Workers", no sunset deadline announced) —
the hosting platform pivots to Workers Static Assets. Those same docs
independently mandate the pinned-Zola build entry: the Workers Builds image
(verified 2026-10-26) preinstalls no Zola and offers no Zola override hook.
The domain is already provisioned (registered; DNS zone on Cloudflare — dig
2026-10-25). The cloud-side operational procedure that this issue's SOP
formerly carried directly is now the wiki-hosted runbook of issue
`brothertown-language-com#3` — delegated there rather than duplicated.

## Scope

In-repo deliverables only. Dashboard-side Cloudflare wiring is executed by the
developer following the wiki-hosted runbook of issue #3 (production/access
operations are not agent reachable without explicit instruction). No content
sections beyond the minimal publishable surface; the seven-section site is
not built here.

## Requirements

- **R-1** — A buildable Zola skeleton lands at the repository root:
  `zola.toml` at the repository root — the configuration file of record per
  the current Zola configuration docs (verified 2026-10-26: "To change the
  configuration, edit the zola.toml file"; the file was previously named
  `config.toml`, which Zola loads only as a fallback when `zola.toml` does
  not exist — under the 2026-10-26 directives the repo carries the current
  name, not the legacy fallback) — with `base_url =
  "https://brothertown-language.com"`, feed
  generation enabled, search index including title/description/content —
  pinned to abridge's documented pairing, verified in the theme's config
  2026-10-26, delivered through the site config because abridge's own
  `zola.toml` does not propagate to a consumer build (Zola merges only the
  theme's `theme.toml` `[extra]`, which is empty here): `build_search_index
  = true` at the top level (a main-section key — Zola v0.23.6 defines it on
  the top-level `Config` struct, and the theme's config carries it there),
  `index_format = "elasticlunr_json"`, `include_title = true`,
  `include_description = true`, and `include_content = true` in `[search]`
  (`include_description` defaults to false at v0.23.6 — the explicit keys
  are required), and `search_library = "elasticlunr"` in `[extra]` (the
  theme's templates read `config.extra.search_library`; Zola v0.23.6 would
  ignore a `[search]`-section placement of that key) — and taxonomies
  `categories`/`tags`/`authors` (the sibling config's taxonomy set), plus
  `compile_sass = true` at the top level (required for the R-3 theme
  override mechanism; the Zola v0.23.6 default is false — verified
  2026-10-26).
- **R-2** — `ZOLA_VERSION` (file) pins one Zola version; `build.sh` downloads
  exactly that release and builds to `public/`. The pinned-download entry is
  grounded in the current Workers Builds docs (verified 2026-10-26): the build
  image (Ubuntu 24.04, x86_64) preinstalls no Zola and offers no Zola
  version-override hook, while arbitrary build commands run with
  curl/wget/unzip/zstd preinstalled. `ZOLA_VERSION` pins the latest stable
  Zola at implementation start — v0.23.6 as of 2026-10-26 (published
  2026-09-12; asset `zola-v0.23.6-x86_64-unknown-linux-gnu.tar.gz`) —
  re-verified against the GitHub releases API then. The sibling deployment's
  visually identical pattern is historical context only; this ground is
  current-docs, not precedent-carryover (the 2026-10-26 directives).
- **R-3** — The theme vendored under `themes/` as plain tracked files (never
  submodules): **abridge** (upstream `Jieiku/abridge`, MIT license,
  `theme.toml` `min_version = "0.23.6"` — current-Zola compatible, verified
  2026-10-26), selected from a browser-verified comparison of 2026-10-26
  (candidate demos rendered with Chromium; dark/light toggles activated and
  their DOM mechanisms observed; Zulma and its forks excluded — macro-based,
  incompatible with the pinned Zola's Tera 2.0.0). Visitor-facing dark/light
  switching: abridge's built-in switcher (Dark/Light/Auto/Switcher modes,
  localStorage persistence — rendered and verified 2026-10-26, observed
  surface flip `#fff`→`#111`). The color scheme stays adjustable by
  documented parameters: the site copies abridge's
  `COPY-TO-ROOT-SASS/abridge.scss` pattern to its `sass/` root and overrides
  the theme's SASS variables via `@use … with` (`$abridgeMode`,
  `$switcherDefault`, `$color` named palette or a site-defined template) —
  the palette itself is CSS custom-property pairs set by the theme's
  paired `light(...)`/`dark(...)` mixins (source verified 2026-10-26). The
  implementation vendors abridge's current revision and records its source
  URL and revision date rather than assuming any prior copy is correct (the
  2026-10-26 directives); the specific palette tones are implementation
  choices made through those documented override parameters.
- **R-4** — The minimal publishable surface: `home` (landing), `about`, and
  `blog` (empty — posts arrive under later issues). Navigation lists only the
  sections that exist (the no-stub rule settled in the brainstorm). The
  remaining site sections — dictionary, lessons, apps, methodology/reference —
  land under their own issues.
- **R-5** — A tracked SOP at `docs/sop-site-setup.md` covering: (a) the local
  development loop (`./zola serve`, build, check); (b) Zola-pin maintenance
  (`ZOLA_VERSION` ↔ the local download, kept matched, with the latest stable
  re-verified against the GitHub releases API whenever the site's tooling is
  touched — the refresh sources issue #3's facts log uses); (c) the
  cloud-side deployment wiring as delegated: the wiki-hosted runbook of
  issue `brothertown-language-com#3` (the repository wiki's runbook page
  set — `Home`/`_Sidebar` navigation plus one page per operational
  section; Workers Static Assets: git connection, build pipeline,
  custom-domain attach, HTTPS verification, rollback, teardown) — the SOP
  links it and does not duplicate its dashboard steps; (d) the
  verification gates below; (e) the recorded platform facts with their
  verification dates, sourced from the runbook's facts-of-record (Workers
  Static Assets limits: 25 MiB per file, 20,000 files per version on the
  free tier; free-tier builds limits), plus the big-asset routes for later
  work as recorded 2026-10-25 (R2 same-account route, free 10 GB; itch.io
  free HTML5 hosting at 200 MB/file and 500 MB/project with 1 GB/file
  platform-download channels).
- **R-6** — The content rules in AGENTS.md bind from delivery: no
  `draft`-flip without explicit publish instruction; image-path existence
  checks before committing front matter; sensitivity/PII audit before any
  publish.
- **R-7** — The repository carries the assets-only deployment manifest per
  issue `brothertown-language-com#3`'s R-4: `wrangler.jsonc` at the
  repository root with `name`, `compatibility_date` set to the
  implementation's current date per the current configuration reference,
  `assets.directory "./public"`, and `not_found_handling "404-page"`; no
  Worker script and no binding — the manifest issue #3's deploy default
  (`npx wrangler deploy`) requires. Grounded in the current configuration
  reference (verified 2026-10-26) — the deployment-unit consequence of the
  Workers pivot (the 2026-10-26 directives).
- **R-8** — The standing decisions-of-record in AGENTS.md are reconciled to
  this spec's directives as part of the implementation: the site's
  platform/theme record lines become the Workers Static Assets hosting
  basis and the abridge theme of record (added; dated 2026-10-26, aligned
  with R-3's facts), and the other Pages-basis lines in that section are
  reconciled to their current-docs equivalents (the 25 MiB big-asset cap
  becomes the Workers Static Assets 25 MiB/file and 20,000-files-per-version
  limits per issue #3's facts table; the "Pages Build System v3 does not
  ship Zola" build-entry ground with its sibling worked-precedent reference
  becomes the Workers Builds grounding per R-2; the Layout section's
  `config.toml` line reflects the `zola.toml` configuration file of record
  per R-1) — so the repo's standing
  record stops pointing future sessions (AGENTS.md is session-injected) at
  the superseded basis; nothing beyond the reconciliation's changed lines
  changes in AGENTS.md.

## Success criteria

| ID | Criterion | Class | Instrument |
|----|-----------|-------|-----------|
| SC-1 | `./build.sh` exits 0 and produces `public/index.html` | behavioral | run `./build.sh`; assert exit 0; assert the file exists |
| SC-2 | `ZOLA_VERSION` exists and `build.sh` downloads exactly the pinned version | structural | inspect the script; confirm the downloaded-version line in the build log |
| SC-3 | `zola.toml` at the repository root sets `base_url` to `https://brothertown-language.com` and carries feeds, the search index with R-1's pinned pairing (`build_search_index = true` at top level; `index_format = "elasticlunr_json"`, `include_title = true`, `include_description = true`, `include_content = true` in `[search]`; `search_library = "elasticlunr"` in `[extra]`), the three taxonomies, and `compile_sass = true` (top level) | structural | file check against R-1's list, including the section placements it states |
| SC-4 | The theme is vendored as tracked plain files; no theme submodule exists; the vendored revision's provenance is recorded in the SOP — abridge's upstream source URL, the vendored revision identifier, and the date recorded | structural | `git ls-files themes/` non-empty; `.gitmodules` absent or empty; content check of the SOP for the provenance record (source URL + revision + date) |
| SC-5 | The built site's navigation links expose exactly the live sections — home, about, blog — and no links to content-less sections | behavioral | enumerate anchor hrefs in the built nav; compare to the closed set `/`, `/about/`, `/blog/`; assert no dictionary/lessons/apps/methodology links |
| SC-6 | The built output's content pages are exactly the three authored surfaces — home landing (`index.html`), about (`about/index.html`), blog section index (`blog/index.html`); every other built file is one of: the config-emitted, explicitly named artifacts — `atom.xml` (R-1's enabled feeds), `sitemap.xml` and `robots.txt` (Zola's default-true generation), `404.html` (built unconditionally — the vendored theme's template if supplied, otherwise Zola's built-in fallback), the search-index files Zola emits under R-1's pinned `index_format = "elasticlunr_json"` — `search_index.en.json` and `elasticlunr.min.js` (Zola emits the latter for both elasticlunr variants), the taxonomy landings (`categories/`, `tags/`, `authors/` paths); the compiled Sass output from the vendored theme's and the site's `sass/` (e.g. abridge's `abridge.css` and syntax-color stylesheets at the output root); static files from the vendored theme's `static/` directories; and static/image assets from the repo's `static/` | structural | enumerate the built output; assert every file falls in the named classes — any file outside them fails; and assert the named search-index artifacts are present (the R-1 search pairing is operative, not vacuously absent) |
| SC-7 | The SOP covers the local loop, pin maintenance with refresh sources, delegates the cloud-side deployment to the wiki-hosted runbook of issue #3 (wiki link stated, no duplicated dashboard steps), carries the verification gates, and records platform facts with dates from the runbook's facts table plus the big-asset routes | structural | content check against R-5's list |
| SC-8 | The SOP's publish procedure includes all three of R-6's rules as its steps: the draft-gate, the image-path existence check, and the sensitivity/PII audit | structural | content check against R-6 |
| SC-9 | The site carries abridge's visitor-facing mode switcher configured with named defaults consistent across the code paths that set them — `$abridgeMode` and `$switcherDefault` set in the site's `sass/abridge.scss` override (the `COPY-TO-ROOT-SASS` pattern), and `js_switcher_default` in the config `[extra]`, consistent with each other per the theme's documented contract — plus the palette parameter (`$color` named template or a site-defined palette) | structural | file checks: `sass/abridge.scss` exists carrying `$abridgeMode`, `$switcherDefault`, and a palette parameter; config `[extra]` carries `js_switcher_default`; assert the override's `$switcherDefault` value equals the config's `js_switcher_default` value |
| SC-10 | `ZOLA_VERSION` equals the latest stable Zola release verified against the GitHub releases API at implementation start (v0.23.6 as of 2026-10-26) | structural | compare the file's value to the releases API's latest non-prerelease tag at the verification run; equality required |
| SC-11 | `wrangler.jsonc` exists at the repository root with the R-7 fields and no Worker script/binding | structural | file check against R-7's field list (`name`, `compatibility_date`, `assets.directory "./public"`, `not_found_handling "404-page"`, absent `main`/bindings) |
| SC-12 | AGENTS.md's decisions-of-record reflect the 2026-10-26 basis with no operative Pages-era wording in the changed lines — Workers Static Assets hosting, the abridge theme of record added, the big-asset cap line stated against the Workers Static Assets limits, the build-entry ground stated against the Workers Builds docs, and the Layout section's config-file line stating `zola.toml` per R-1; nothing outside R-8's reconciliation scope changed | structural | content check of AGENTS.md's decisions-of-record and Layout config-file line against R-8's stated scope (no operative Pages/Zulma-era wording remains in the changed lines; the config-file line names `zola.toml`); diff-scope check that only the reconciliation's lines differ |

## Out of scope

- Dictionary, lesson, app, and methodology content; any consumption of the
  research repositories' data of record.
- Audio production; branding beyond the site title; blog posts; game/app
  embedding; itch.io or R2 asset routes (recorded for later issues).
- The dashboard-side Cloudflare execution itself (runbook-documented — issue
  #3's wiki runbook page set; developer-run).

## Approach

Build the base site under the 2026-10-26 directives: the hosting platform is
Cloudflare Workers Static Assets per Cloudflare's current recommendation —
issue #3's selection record carries the dated evidence; the build entry pins
the latest stable Zola with `ZOLA_VERSION` as the single version of record,
grounded in the current Workers Builds docs (R-2) rather than in the
sibling's pattern; the vendored theme baseline is abridge — verified current-Zola compatible and
selected from the 2026-10-26 browser-verified comparison, its current revision
recorded at vendor time, with the site's mode and palette parameters carried
in abridge's documented `sass/abridge.scss` override file so later re-toning
touches one file (R-3); a curated navigation (the sibling's menu pattern as a
decision-of-record shape) so the no-stub rule holds mechanically; the SOP
carries the local loop, pin maintenance, verification gates, and dated
platform facts, delegating the cloud-side dashboard procedures to the
runbook of issue #3 so one operational record exists rather than two
drifting copies; later issues (dictionary, lessons, apps, big-asset routes)
inherit the grounded constraints from the runbook's facts table rather than
re-deriving them.

## Dependencies

- The bootstrap branch (README/AGENTS/gitignore) merging first — this issue's
  work follows the repo's trunk existence. (Merged as PR #2, 2026-10-26 —
  satisfied.)
- Issue `brothertown-language-com#3`'s runbook spec: the same 2026-10-26
  directives; its facts-of-record table (a dated primary source per fact,
  verified live 2026-10-26) grounds the Workers facts this spec inherits by
  reference.
- Landing order: issue #3's wiki runbook page set needs to land before (or
  with) the SOP — R-5(c)'s delegation link targets that wiki page set.
- The developer's Cloudflare account for the dashboard wiring steps
  (runbook-guided — issue #3).

## References

- Workers Static Assets basis (verified 2026-10-26): issue #3's spec — its
  facts-of-record table carries the complete dated source set (Workers
  Builds image/limits/configuration, wrangler configuration, custom domains,
  Advanced Certificates, rollback, static-assets limits).
- Zola pin of record: v0.23.6 latest stable (GitHub releases API, fetched
  2026-10-26; published 2026-09-12).
- Theme of record (verified 2026-10-26): abridge — upstream `Jieiku/abridge`
  (README; `theme.toml` `min_version = "0.23.6"`, `license = "MIT"`), demo
  `abridge.pages.dev`; switcher mechanics and the color-parameter system
  verified from the rendered demo and the theme's SASS source; selected from
  a browser-verified multi-theme comparison dated 2026-10-26. The sibling
  config's taxonomy set and menu-curation shape remain the recorded
  brainstorm decisions for R-1/R-4.
- Domain: `brothertown-language.com` NS records on Cloudflare (dig,
  2026-10-25); developer statement 2026-10-26 (provisioned).
- Historical (superseded by the 2026-10-26 directives): the sibling
  Pages-era deployment record — `michael-conrad.com`'s `ZOLA_VERSION`
  (0.22.1), `build.sh`, `CLOUDFLARE_UPDATE.md` (Pages v3, Ubuntu 24.04 v3);
  and the Zulma theme baseline (the brainstorm's 2026-10-25 theme choice) —
  macro-based, incompatible with the pinned Zola's Tera 2.0.0, unmaintained
  upstream since 2024-04-22 — retained as historical context only. Still
  operative with their 2026-10-25 verification dates: the big-asset routes
  recorded that day (R2 same-account route, free 10 GB; itch.io free HTML5
  hosting at 200 MB/file and 500 MB/project with 1 GB/file platform-download
  channels) — carried by R-5(e); re-verify at the owning issue's work.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
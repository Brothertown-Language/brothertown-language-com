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
formerly carried directly is now the tracked runbook of issue
`brothertown-language-com#3` — delegated there rather than duplicated.

## Scope

In-repo deliverables only. Dashboard-side Cloudflare wiring is executed by the
developer following the tracked runbook of issue #3 (production/access
operations are not agent reachable without explicit instruction). No content
sections beyond the minimal publishable surface; the seven-section site is
not built here.

## Requirements

- **R-1** — A buildable Zola skeleton lands at the repository root:
  `config.toml` with `base_url = "https://brothertown-language.com"`, feed
  generation enabled, search index including title/description/content, and
  taxonomies `categories`/`tags`/`authors` (the sibling config's taxonomy set).
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
  submodules): baseline Zulma with per-visitor theme selection (the sibling
  config's `zulma_allow_theme_selection` + default theme). The Zulma baseline
  is the brainstorm's recorded choice (2026-10-25), carried as a decision —
  not inherited by default; per the 2026-10-26 directive the implementation
  vendors Zulma's current revision and records its source URL and revision
  date rather than assuming the sibling's copy is correct. Alternatives named
  in the brainstorm (purpose-built minimal; the vendored `d3c3nt`) remain
  open for later issues.
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
  cloud-side deployment wiring as delegated: the tracked runbook of issue
  `brothertown-language-com#3` (`docs/runbook-cloudflare-workers-setup.md`,
  Workers Static Assets: git connection, build pipeline, custom-domain
  attach, HTTPS verification, rollback, teardown) — the SOP links it and
  does not duplicate its dashboard steps; (d) the verification gates below;
  (e) the recorded platform facts with their verification dates, sourced
  from the runbook's facts-of-record (Workers Static Assets limits: 25 MiB
  per file, 20,000 files per version on the free tier; free-tier builds
  limits), plus the big-asset routes for later work as recorded 2026-10-25
  (R2 same-account route, free 10 GB; itch.io free HTML5 hosting at 200
  MB/file and 500 MB/project with 1 GB/file platform-download channels).
- **R-6** — The content rules in AGENTS.md bind from delivery: no
  `draft`-flip without explicit publish instruction; image-path existence
  checks before committing front matter; sensitivity/PII audit before any
  publish.

## Success criteria

| ID | Criterion | Class | Instrument |
|----|-----------|-------|-----------|
| SC-1 | `./build.sh` exits 0 and produces `public/index.html` | behavioral | run `./build.sh`; assert exit 0; assert the file exists |
| SC-2 | `ZOLA_VERSION` exists and `build.sh` downloads exactly the pinned version | structural | inspect the script; confirm the downloaded-version line in the build log |
| SC-3 | `config.toml` sets `base_url` to `https://brothertown-language.com` and carries feeds, search index (content included), and the three taxonomies | structural | file check against R-1's list |
| SC-4 | The theme is vendored as tracked plain files; no theme submodule exists | structural | `git ls-files themes/` non-empty; `.gitmodules` absent or empty |
| SC-5 | The built site's navigation links expose exactly the live sections — home, about, blog — and no links to content-less sections | behavioral | enumerate anchor hrefs in the built nav; compare to the closed set `/`, `/about/`, `/blog/`; assert no dictionary/lessons/apps/methodology links |
| SC-6 | The built output's content pages are exactly the three authored surfaces — home landing (`index.html`), about (`about/index.html`), blog section index (`blog/index.html`); every other built file is one of the config-emitted, explicitly named artifacts: `atom.xml`, `sitemap.xml`, `404.html`, the taxonomy landings (`categories/`, `tags/`, `authors/` paths), and static/image assets from `static/` | structural | enumerate the built output; assert every file falls in the named classes — any file outside them fails |
| SC-7 | The SOP covers the local loop, pin maintenance with refresh sources, delegates the cloud-side deployment to the tracked runbook of issue #3 (path stated, no duplicated dashboard steps), carries the verification gates, and records platform facts with dates from the runbook's facts table plus the big-asset routes | structural | content check against R-5's list |
| SC-8 | The SOP's publish procedure includes all three of R-6's rules as its steps: the draft-gate, the image-path existence check, and the sensitivity/PII audit | structural | content check against R-6 |
| SC-9 | The theme configuration carries per-visitor theme selection with a named default (the sibling config's `zulma_allow_theme_selection` + default theme) | structural | file check in `config.toml` |
| SC-10 | `ZOLA_VERSION` equals the latest stable Zola release verified against the GitHub releases API at implementation start (v0.23.6 as of 2026-10-26) | structural | compare the file's value to the releases API's latest non-prerelease tag at the verification run; equality required |

## Out of scope

- Dictionary, lesson, app, and methodology content; any consumption of the
  research repositories' data of record.
- Audio production; branding beyond the site title; blog posts; game/app
  embedding; itch.io or R2 asset routes (recorded for later issues).
- The dashboard-side Cloudflare execution itself (runbook-documented — issue
  #3's `docs/runbook-cloudflare-workers-setup.md`; developer-run).

## Approach

Build the base site under the 2026-10-26 directives: the hosting platform is
Cloudflare Workers Static Assets per Cloudflare's current recommendation —
issue #3's selection record carries the dated evidence; the build entry pins
the latest stable Zola with `ZOLA_VERSION` as the single version of record,
grounded in the current Workers Builds docs (R-2) rather than in the
sibling's pattern; Zulma remains the vendored theme baseline of the
2026-10-25 brainstorm with its current revision verified and recorded at
vendor time (R-3); a curated navigation (the sibling's menu pattern as a
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
  directives; its validation verdict (PASS, zero findings, fresh-context,
  2026-10-26) grounds the Workers facts this spec inherits by reference.
- Landing order: issue #3's runbook document needs to land before (or with)
  the SOP — R-5(c)'s delegation link targets its path.
- The developer's Cloudflare account for the dashboard wiring steps
  (runbook-guided — issue #3).

## References

- Workers Static Assets basis (verified 2026-10-26): issue #3's spec — its
  facts-of-record table carries the complete dated source set (Workers
  Builds image/limits/configuration, wrangler configuration, custom domains,
  Advanced Certificates, rollback, static-assets limits).
- Zola pin of record: v0.23.6 latest stable (GitHub releases API, fetched
  2026-10-26; published 2026-09-12).
- Zulma theme + per-visitor theme selection: both sibling sites'
  `config.toml` (`zulma_allow_theme_selection`, taxonomy set, menu curation
  via `zulma_menu`) — the recorded brainstorm shape, verified current at
  vendor time (R-3).
- Domain: `brothertown-language.com` NS records on Cloudflare (dig,
  2026-10-25); developer statement 2026-10-26 (provisioned).
- Historical (superseded by the 2026-10-26 directives): the sibling
  Pages-era deployment record — `michael-conrad.com`'s `ZOLA_VERSION`
  (0.22.1), `build.sh`, `CLOUDFLARE_UPDATE.md` (Pages v3, Ubuntu 24.04 v3);
  and the 2026-10-25 Pages/itch.io platform-fact recordings — retained as
  historical context only; operative platform facts now live in issue #3's
  facts table.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
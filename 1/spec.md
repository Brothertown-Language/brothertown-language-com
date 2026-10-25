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
decisions-of-record section.

## Scope

In-repo deliverables only. Dashboard-side Cloudflare wiring is executed by the
developer with the SOP's steps (production/access operations are not agent
reachable without explicit instruction). No content sections beyond the
minimal publishable surface; the seven-section site is not built here.

## Requirements

- **R-1** — A buildable Zola skeleton lands at the repository root:
  `config.toml` with `base_url = "https://brothertown-language.com"`, feed
  generation enabled, search index including title/description/content, and
  taxonomies `categories`/`tags`/`authors` (the sibling config's taxonomy set).
- **R-2** — `ZOLA_VERSION` (file) pins one Zola version; `build.sh` downloads
  exactly that release and builds to `public/`. Grounds (verified
  2026-10-25): Cloudflare Pages Build System v3 does not ship Zola by default;
  the michael-conrad.com deployment solves this with the same pattern pinned
  at 0.22.1 — the worked precedent carries over.
- **R-3** — The theme vendored under `themes/` as plain tracked files (never
  submodules): baseline Zulma, per-visitor theme selection carried from the
  sibling configuration. Alternatives named in the brainstorm (purpose-built
  minimal; the vendored `d3c3nt`) remain open for later issues — this issue
  ships the sibling-continuity baseline.
- **R-4** — The minimal publishable surface: `home` (landing), `about`, and
  `blog` (empty — posts arrive under later issues). Navigation lists only the
  sections that exist (the no-stub rule settled in the brainstorm). The
  remaining site sections — dictionary, lessons, apps, methodology/reference —
  land under their own issues.
- **R-5** — A tracked SOP at `docs/sop-site-setup.md` covering: (a) the local
  development loop (`./zola serve`, build, check); (b) Zola-pin maintenance
  (`ZOLA_VERSION` ↔ the local download, keep them matched); (c) Cloudflare
  Pages project creation (GitHub-connected; build command `./build.sh`; build
  output directory `public/`; build image Ubuntu 24.04 v3); (d) the
  custom-domain attach for `brothertown-language.com` (domain purchased; NS on
  Cloudflare — verified 2026-10-25); (e) the verification gates below; (f) the
  recorded platform facts with their verification dates, including the
  big-asset routes for later work (Pages 25 MiB per-file cap on all plans and
  20,000-file limit; R2 same-account route, free 10 GB; itch.io free HTML5
  hosting at 200 MB/file and 500 MB/project with 1 GB/file platform-download
  channels).
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
| SC-5 | The built site's navigation links expose exactly the live sections — home, about, blog — and no links to content-less sections | behavioral | enumerate anchor hrefs in the built nav; compare to the closed set `{/`,  `/about/`, `/blog/`}; assert no dictionary/lessons/apps/methodology links |
| SC-6 | The built output's page set is exactly the closed expected surface: home landing, about page, blog section index (plus taxonomy/atom-standard artifacts); nothing else | structural | enumerate the built pages; compare against the closed expected list |
| SC-7 | The SOP covers local loop, pin maintenance, Pages wiring, domain attach, verification gates, and dated platform facts | structural | content check against R-5's list |
| SC-8 | The SOP's publish procedure includes all three of R-6's rules as its steps: the draft-gate, the image-path existence check, and the sensitivity/PII audit | structural | content check against R-6 |

## Out of scope

- Dictionary, lesson, app, and methodology content; any consumption of the
  research repositories' data of record.
- Audio production; branding beyond the site title; blog posts; game/app
  embedding; itch.io or R2 asset routes (recorded for later issues).
- The dashboard-side Cloudflare execution itself (SOP-documented, developer-run).

## Approach

Replicate the verified sibling deployment pattern: Zulma vendored as the
baseline shell with the per-visitor theme selection from the sibling config;
a curated navigation (the sibling's menu pattern) so the no-stub rule holds
mechanically; the pinned-Zola build entry with `ZOLA_VERSION` as the single
version of record; the SOP carrying every verified hosting fact with its date
so later issues (dictionary, lessons, apps, big-asset routes) inherit grounded
constraints rather than re-deriving them.

## Dependencies

- The bootstrap branch (README/AGENTS/gitignore) merging first — this issue's
  work follows the repo's trunk existence.
- The developer's Cloudflare account for the dashboard wiring steps (SOP-guided).

## References (verified 2026-10-25)

- Sibling deployment precedent: `michael-conrad.com` repo — `ZOLA_VERSION`
  (0.22.1), `build.sh` (pinned download from GitHub releases),
  `CLOUDFLARE_UPDATE.md` (Pages v3 Zola-absence + pin procedure, Ubuntu 24.04
  v3).
- Zulma theme + per-visitor theme selection: both sibling sites' `config.toml`
  (`zulma_allow_theme_selection`, taxonomy set, menu curation via
  `zulma_menu`).
- Platform limits: Cloudflare Pages limits doc (25 MiB/file, all plans;
  20,000-file free tier); itch.io creator docs/FAQ (HTML5 hosting free,
  200 MB/file, 500 MB/project; download files 1 GB/file default) — the
  big-asset routes recorded for later issues.
- Domain: `brothertown-language.com` NS records on Cloudflare (dig, 2026-10-25).

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
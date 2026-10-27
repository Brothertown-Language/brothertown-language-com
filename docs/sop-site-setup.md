<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# SOP — Site setup and maintenance

Standard operating procedure for the site's base setup: the local tooling
loop, the Zola version pin, the delegated cloud-side deployment, the
verification gates, the pre-PR preview review, the publish procedure, and the
platform facts of record.
The spec of record is issue `brothertown-language-com#1`.

## Repository artifacts of record

| Artifact | Role |
|----------|------|
| `zola.toml` | Site configuration of record — the current config-file name (Zola loads the legacy `config.toml` name only as a fallback). Carries feeds, the search index, taxonomies, Sass compilation, and the theme's `[extra]` parameters. |
| `ZOLA_VERSION` | The single Zola version of record (`v0.23.6`). |
| `build.sh` | Build entry: downloads exactly the pinned Zola release and builds to `public/`. |
| `wrangler.jsonc` | Assets-only deployment manifest for Cloudflare Workers Static Assets: no Worker script, no bindings — the built `public/` is the deploy unit. |
| `sass/abridge.scss` | The site's theme-tuning override (abridge's `COPY-TO-ROOT-SASS` pattern): palette and mode parameters in one file. |
| `themes/abridge` | The vendored theme — plain tracked files, never a submodule (provenance below). |
| `content/` | Site content: home, about, blog. |

## Local development loop

- `./build.sh` — builds the site into `public/` (gitignored). First run (and
  after any `ZOLA_VERSION` change) it downloads the pinned Zola release into
  `~/.local/bin/zola` and refreshes the working-tree `./zola` binary (also
  gitignored). No system Zola install is required.
- `./zola serve` — live preview at <http://127.0.0.1:1111>.
- `./zola check` — validates links and content. Only `ERROR` lines matter;
  the warning baseline is recorded below and warnings are triaged only if
  they change.
- Run the [verification gates](#verification-gates) after touching any of
  `zola.toml`, `build.sh`, `ZOLA_VERSION`, `sass/`, `themes/`, or site
  structure.

### Warning baseline (from `./zola check`, 2026-10-26)

Zero warnings — 1 page, 2 sections, exit 0. Any new warning arriving with a
change is triaged before it can become normalized noise.

## Zola pin maintenance

`ZOLA_VERSION` is the single version of record; `build.sh` downloads exactly
that release:

- The local download and the pin are kept matched — after editing
  `ZOLA_VERSION`, run `./build.sh` (it refreshes `./zola` to the new pin).
- Whenever site tooling is touched, re-verify the pin against the GitHub
  releases API — the same check the runbook's facts log uses
  (`gh api repos/getzola/zola/releases/latest` — latest non-prerelease tag;
  the Linux build asset is
  `zola-v<version>-x86_64-unknown-linux-gnu.tar.gz`). Update the pin through
  a normal PR when latest-stable has moved.
- Pin of record: **v0.23.6** — latest stable, published 2026-09-12;
  verified against the releases API 2026-10-26.

## Cloud-side deployment (delegated)

Cloud-side operation — connecting the repository, the build pipeline, the
custom-domain attach and HTTPS verification, rollback, teardown — is run
from the **repository wiki's Cloudflare Workers runbook** (issue
`brothertown-language-com#3`), which is the single record of truth for those
procedures. This SOP links it and deliberately does not duplicate its
dashboard steps:

- [Runbook home and read order](https://github.com/Brothertown-Language/brothertown-language-com/wiki/Home)
- Page set: *Cloudflare Workers Setup Overview* · *Build Pipeline* ·
  *Domain HTTPS* · *Rollback Teardown* · *Cloudflare Runbook Facts Log*
- The in-repo artifacts that runbook consumes from this setup: `wrangler.jsonc`,
  `build.sh`, `ZOLA_VERSION`, and the built `public/` (build output).
- The dashboard Worker/project name must match wrangler.jsonc's `"name"`
  (`brothertown-language-com`) or the build fails — the runbook carries the
  caution and the connect flows.
- **Preview deployments need no dashboard configuration** (procedure change,
  2026-10-27): `build.sh` derives is-production from the branch
  (`WORKERS_CI_BRANCH`, git fallback) — main keeps the base_url of record;
  any non-main branch builds domain-neutral (`--base-url /`) and serves
  correctly on any preview hostname. No per-branch env var, no dashboard
  step; the runbook's Build Pipeline step 8 records the superseded
  per-branch/per-value attempts. The preview-mode trade (root-relative
  feeds/sitemap on those builds) is noted in the Content rules below —
  preview-surface only.
- Dashboard navigation is label-drifted on this account (multiple accounts
  under one login; no "Workers & Pages" sidebar option; the docs'
  `workers-and-pages` deep link dead — observed 2026-10-26) — the runbook's
  overview page carries the account-selection step zero and its navigation
  notes.

## Verification gates

Run after any tooling, config, theme, or site-structure change:

1. **Build** — `./build.sh` exits 0 and `public/index.html` exists. The
   build log must show the pinned version being used (the
   `Downloading Zola $ZOLA_VERSION` step or the matching `zola --version`
   output).
2. **Navigation surface** — the built pages' navigation links expose exactly
   the live sections (`/`, `/about/`, `/blog/`); no links to sections that
   do not exist (no-stub rule).
3. **Built-output surface** — every built file is one of: the three authored
   surfaces (`index.html`, `about/index.html`, `blog/index.html`); the
   config-emitted artifacts — `atom.xml` (feeds), `sitemap.xml` and
   `robots.txt` (default-true generation), `404.html`; the search-index
   files (`search_index.en.json`, `elasticlunr.min.js`); the taxonomy
   landings (`categories/`, `tags/`, `authors/`); the compiled Sass output
   (`abridge.css` and the syntax-color stylesheets); the theme's static
   files; the repo's static/image assets. Anything outside these classes is
   investigated before merge.
4. **Switcher consistency** — `sass/abridge.scss`'s `$switcherDefault` and
   `zola.toml` `[extra]` `js_switcher_default` carry the same value (theme
   contract: the no-JS fallback and the JS switcher must agree).
5. **Pin currency** — `ZOLA_VERSION` equals the latest stable non-prerelease
   Zola tag from the releases API (re-verified at tooling touch).
 6. **Manifest shape** — `wrangler.jsonc` carries `name`,
    `compatibility_date` (implementation-current date), the `previews` block
    (required by `npx wrangler preview`, wrangler 4.153.0 — runbook Build
    Pipeline step 7), `assets.directory ./public`, and `not_found_handling
    "404-page"`, with no Worker script and no bindings.

## Pre-PR preview review

The normative rule lives in AGENTS.md's Git workflow (agents open PRs; humans
merge): before filing any PR from this repository — unconditionally, docs-only
changes included — the filing agent serves the site and presents it for the
developer's review, and the PR is filed only after that presented review.
Filing means opening the PR on GitHub via `gh pr create`. This section is the
procedure of record that rule points at; the gate's first application is
issue `brothertown-language-com#13`'s own implementing PR. The review does not
replace the [verification gates](#verification-gates); those run as stated in
their own section.

1. **Serve** — `./zola serve`. When the working-tree `./zola` binary is
   absent, run `./build.sh` first (it refreshes `./zola` to the
   `ZOLA_VERSION` pin).
2. **Present** — give the developer the preview URL the server is actually
   answering (default <http://127.0.0.1:1111>; `--port <N>` when 1111 is
   unavailable) — never an assumed URL — plus the change's rendered surface:
   the pages/sections the branch touches.
3. **Drafts** — when the change under review carries draft-flagged content,
   serve with `./zola serve --drafts` (`serve` excludes drafts by default;
   the flag only widens this preview). Drafts stay draft: this never touches
   the [publish procedure](#publish-procedure)'s draft gate.
4. **Window** — the server runs for the review window only: started for the
   presentation, kept up while the developer reviews, and stopped once the
   developer responds to the presentation (further work does not extend the
   window); no lingering server is left running.
5. **Record** — the PR body records the presented review (preview URL and the
   date presented) in its evidence set.
6. **No-skip clause** — when the server cannot render the branch's site, the
   agent presents the serve/build failure output in place of the preview; the
   gate still holds — the PR waits for that presented review. The failure
   becomes the reviewed content; the presentation requirement is never waived.

## Publish procedure

These three rules bind from delivery (issue #1's content rules; also
AGENTS.md):

1. **Draft gate.** Never flip `draft = true` → `false` without an explicit
   developer instruction to publish that content, in the session.
2. **Image-path existence check.** Verify every referenced image path
   (`featured_image`, inline references) exists in the repository before
   committing front matter — a missing file fails the Zola build.
3. **Sensitivity / PII audit.** Audit content for sensitive leaks and PII
   before any commit or publish.
4. **Site-relative URLs (default).** Content-embedded URLs (raw-HTML
   components, floated/featured images, template-built asset references,
   shortlinks for page assets) are **site-relative by default** — root-
   relative forms built from site-relative data (`{{ page.path }}`, Zola's
   own relative resolution), never absolute `page.permalink` / `get_url`
   construction. Content that embeds an absolute URL 404s on Workers preview
   domains (previews serve branches under their own names before the merge)
   and on any mirror; Zola-generated absolute URLs (canonical, feeds,
   sitemap, search index) remain absolute at production builds — they are
   the platform's output, not hand-authored surface. (Developer directive
   2026-10-27; discovery recorded in the wiki runbook's facts log and issue
   `brothertown-language-com#9`. Where something genuinely requires a
   domain-specific absolute URL — the documented exception — the exception
   is named in the deliverable that needs it.)
   **Preview build mode:** automatic. `build.sh` derives is-production from
   the branch — `WORKERS_CI_BRANCH` (the platform-injected default env var;
   git fallback) — and non-main branches build domain-neutral
   (`--base-url /`), root-relativizing every template-generated URL so any
   preview hostname serves correctly; nothing to set per branch (branch
   hostnames are not stable). Preview-only trade: the generated
   feeds/sitemap then emit root-relative URLs — preview-surface only;
   main builds keep the base_url of record; an explicit absolute
   `SITE_BASE_URL` overrides both. (Verified against the pinned Zola
   0.23.6 with differential builds: `--base-url /` root-relativizes
   permalinks/`get_url`; 2026-10-27.)
5. **Mastodon discussion back-link.** Every published blog post carries a
   `### Comment on Mastodon` section, placed at the very end of the article
   — after the AI co-authored byline, matching the source site's own
   convention (michael-conrad.com's convention-era posts; observed in its
   repo 2026-10-27) — anchored to the post's Mastodon discussion thread.
   This site's form is the plain anchor (no embed markup — the embed was
   rejected in issue `brothertown-language-com#9`'s spec, R-4/SC-7); the
   source site's wording, kept verbatim: the line
   `You can comment on this post via Mastodon:` followed by the plain
   anchor `[View on Mastodon](<thread-url>)` — the embed's action label as
   the plain link, never placeholder labels like "thread". A post without a
   discussion thread omits the section (the rule applies to published posts
   that have one).

## Vendored theme provenance

- **Theme of record:** abridge — upstream
  <https://github.com/Jieiku/abridge> (MIT license; `theme.toml`
  `min_version = "0.23.6"`, demo `abridge.pages.dev`).
- **Vendored revision:** upstream `master` @
  `d14a9decdbc6a1cc140f5a43fd04e38fe30430ae` (commit dated
  2026-10-26T04:01:04Z; vendored 2026-10-26). The vendored tree is
  byte-identical to that revision for every file it carries — the upstream
  repository's demo-site and development files (repo root: `content/`,
  `zola.toml`, `COPY-TO-ROOT-SASS/`, `package*.js`, `.github/`, `README.md`,
  screenshot, and similar) are not part of a theme payload and are not
  vendored.
- **Re-vendoring procedure:** fetch the upstream tree (release tag or master
  revision), diff it against `themes/abridge`, update the theme payload,
  re-verify the build and switcher gates, and re-record the revision and date
  here. Never vendor via git submodule; `themes/` files are plain tracked
  files.

## Blog images — crop, zoom, and front-fold layout (recorded 2026-10-27)

In scope for every blog article going forward (developer instruction,
2026-10-27, during the issue #23 review): blog images may be **cropped and
zoomed** for layout fit. The rules:

- **Crop/zoom is presentation, not content.** A crop or zoom shapes how an
  approved image displays — excerpt float, aspect fit, highlighting the
  subject region — and never manufactures new subject matter; if a crop
  changes what an image appears to show, it is rejected, not applied.
- **Credit survives.** Every displayed image keeps its license/source credit
  line regardless of cropping or zooming; note the edition when it matters
  (e.g. "cropped from the full title page") so the displayed version is
  traceable to its credit.
- **Credit-line register.** A caption names the work and its credit directly
  — "A Key into the Language of America*, Roger Williams (1643) — via
  Wikimedia Commons, …" — with no filler legend prefix like "Image:" or
  "Map:" (developer ruling, 2026-10-27): the label adds narrative noise and
  says nothing the caption's own content doesn't already say.
- **Original preserved.** Keep the full uncropped source file alongside the
  cropped edition in the post/app folder (or record its source URL), so a
  later re-crop never needs re-sourcing.
- **Front-fold sizing.** Floated excerpt images are displayed at an explicit
  size — portrait/tall plates carry a `max-height` cap (≈ 20 rem observed
  working, front page 1080p) — so the image box stays a minority of the
  excerpt and never balloons the front-fold block.
- **Front-fold placement rule of thumb.** The excerpt (fold) shows the
  standfirst plus the article's opening body paragraphs: fold at the first
  paragraph break that lands the excerpt text in the ~150–250-word range
  (roughly 10 rendered list lines at desktop width) — visibly partway into
  the article proper, never before the first full body paragraph, never at
  or past the first section heading, and never past about the first quarter
  of the body. Rationale (observed 2026-10-27, issue #23 review): a fold
  right after the standfirst reads as an empty teaser; the draft's own fold
  three paragraphs down crowded the list page — the excerpt should carry
  enough of the article's opening voice that the list page stands alone.
- **Float containment.** The excerpt box (`.sum`) establishes a block
  formatting context (`display: flow-root`, `sass/abridge.scss`) so a
  floated image div — which nests block-level inside the list template's
  bare `<p>` — is contained within its own article's fold and cannot bleed
  into the next article's flow; the floated image (and its legend) is
  centered within the 25%-wide float box (`text-align: center` on the
  `.imgfloat`), so a height-capped plate narrower than the box doesn't hug
  its left edge (observed 2026-10-27).
- **More-link marker.** The front-fold read-more link is a centered
  chip — class `more-link` (template: `more ›`, no ellipsis prefix),
  blocked and auto-centered in the excerpt via `.sum a.more-link`
  (`sass/abridge.scss`); the theme's bare flush-left `...more` anchor read
  as inline noise and vanished against the excerpt text (observed
  2026-10-27).
- **Title ornament.** Every article title carries a static site-wide quill
  glyph: a 1em CSS-mask of Bootstrap Icons' `feather` (MIT) inlined as an
  SVG data-URI in `sass/abridge.scss`, inheriting `currentColor` so it is
  palette-safe on light and dark themes and font-independent across
  browsers. Selected and Playwright-verified 2026-10-27; per-article
  iconography was considered and declined for now (revisit-later ruling,
  developer 2026-10-27).

## Platform facts of record

Workers Static Assets limits (per the runbook facts log, verified
2026-10-12): **25 MiB per file**, and **20,000 files per assets version** on
the free tier; asset requests themselves are free. Workers Builds free tier
(verified 2026-05-29 — the oldest fact in the runbook's set; re-verify before
relying on it): 3,000 build-minutes/month, 1 concurrent build, 20-minute
build timeout. Build image (verified 2026-10-26 — the page's current state):
Ubuntu 24.04 x86_64, Node 24.22.1 default / 22.23.4 preinstalled — no Zola
preinstalled and no Zola version-override hook, which is why `build.sh`
pins and downloads; curl/wget/unzip are preinstalled. When dashboard or
cloud behavior looks broken, check the Cloudflare status page first
(<https://www.cloudflarestatus.com>) — the status-page facts (including
today's observed anomaly) live in `docs/cloudflare-facts.md`.

Big-asset routes for later work (recorded 2026-10-25; re-verify at the
owning issue's work):

- **Cloudflare R2** (same account) for larger game/app assets — free 10 GB.
- **itch.io** free hosting: HTML5 200 MB/file and 500 MB/project; download
  files 1 GB/file by default, with per-platform download channels via butler
  (windows/macos/linux/android).

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)
<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# SOP — Site setup and maintenance

Standard operating procedure for the site's base setup: the local tooling
loop, the Zola version pin, the delegated cloud-side deployment, the
verification gates, the publish procedure, and the platform facts of record.
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
   `compatibility_date` (implementation-current date), `assets.directory
   ./public`, and `not_found_handling "404-page"`, with no Worker script and
   no bindings.

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

## Platform facts of record

Workers Static Assets limits (per the runbook facts log, verified
2026-10-12): **25 MiB per file**, and **20,000 files per assets version** on
the free tier; asset requests themselves are free. Workers Builds free tier
(verified 2026-05-29 — the oldest fact in the runbook's set; re-verify before
relying on it): 3,000 build-minutes/month, 1 concurrent build, 20-minute
build timeout. Build image (verified 2026-10-24): Ubuntu 24.04 x86_64 — no
Zola preinstalled and no Zola version-override hook, which is why `build.sh`
pins and downloads; curl/wget/unzip are preinstalled.

Big-asset routes for later work (recorded 2026-10-25; re-verify at the
owning issue's work):

- **Cloudflare R2** (same account) for larger game/app assets — free 10 GB.
- **itch.io** free hosting: HTML5 200 MB/file and 500 MB/project; download
  files 1 GB/file by default, with per-platform download channels via butler
  (windows/macos/linux/android).

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)
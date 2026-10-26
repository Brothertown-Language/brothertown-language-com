<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# AGENTS.md — brothertown-language-com

Public Zola static site for the Brothertown Language project. Current state:
bootstrap — conventions and docs only; the base Zola setup is issue 1 in the
repository's issue tracker. Humans merge PRs; agents never merge.

## Site decisions of record (brainstorm with developer, 2026-10-25)

- **Cloudflare facts of record: `docs/cloudflare-facts.md`** — consult
  before any Cloudflare, build, deploy, or CI work; rows are dated and
  sourced and kept current in place via PR (never from session memory).
- Zola static site, Cloudflare Workers Static Assets hosting (platform of
  record 2026-10-26 — Cloudflare's current recommendation is "Start new
  projects with Workers"; cloud-side dashboard wiring follows the repo wiki's
  Workers runbook, issue 3). Domain `brothertown-language.com` (purchased;
  zone on Cloudflare — verified live 2026-10-25).
- Theme of record: **abridge** (`Jieiku/abridge`, MIT; `min_version 0.23.6`
  — current-Zola compatible, verified 2026-10-26), vendored as plain tracked
  files under `themes/abridge`; vendored revision and re-vendor procedure in
  `docs/sop-site-setup.md`.
- Sections: home, dictionary, lessons (written / written+audio / audio-only),
  apps, methodology/reference, blog, about.
- Every page is generated from the tracked data of record — dictionary
  entries and lesson text come from the research repositories' validated data
  files (consumed by submodule or pin), never hand-typed onto pages.
- Apps: flashcards first, in both a plain-JS build and a Godot web export.
  Apps carry their word lists inside them at release time — no runtime
  dependency on the site. Reference pattern: CherokeeLessons.com's App pages
  plus its self-hosted static game bundles.
- Big-asset rule: Workers Static Assets caps an asset at 25 MiB/file, and
  20,000 files per assets version on the free tier (verified 2026-10-12 —
  the runbook facts log carries the dated source). Larger game assets live
  in Cloudflare R2 (same account) or itch.io hosting (verified 2026-10-25:
  HTML5 free hosting, 200 MB/file and 500 MB/project limits; download files
  1 GB/file by default; per-platform download channels via butler —
  windows/macos/linux/android).
- Zola is pinned by version in `ZOLA_VERSION` (single version of record).
  Cloudflare's Workers Builds image preinstalls no Zola and offers no Zola
  version-override hook (verified against current docs 2026-10-26) —
  `build.sh` downloads the pinned release and builds.

## Layout

- `zola.toml` — Zola config of record (feeds, search index, taxonomies; the
  current config-file name — the legacy `config.toml` name loads only as a
  fallback)
- `ZOLA_VERSION` — the pinned Zola version
- `build.sh` — CI build entry: downloads the pinned Zola, builds to `public/`
- `content/<section>/…` — section folders with `_index.md`. Issue 1 lands
  home, about, and blog; the remaining sections (dictionary, lessons, apps,
  methodology/reference) land under their own issues — the no-stub rule keeps
  content-less sections out of the navigation until their content exists.
- `themes/` — vendored theme files as plain tracked files, never submodules
- `templates/`, `sass/`, `static/` — Zola standard

## Commands (after issue 1 lands)

- Build: `./build.sh` → `public/` (gitignored)
- Validate: `./zola check` — run it after setup and record the warning
  baseline; thereafter only ERROR lines matter
- Preview: `./zola serve` (http://127.0.0.1:1111)

## Content rules

- Never flip `draft = true` → `false` without an explicit developer
  instruction to publish.
- Text content is Markdown; `config.toml` and front matter are TOML.
- Images live in `static/images/`, post folders, or app folders — never
  ad-hoc paths. A `featured_image` pointing at a missing file fails the Zola
  build; check existence before committing front matter.
- Audit content for sensitive leaks and PII before any commit or publish.

## Git workflow (hooks enforce it)

- Branch first, always: `git checkout -b feature/<scope>-<slug>`. The
  pre-commit/pre-push hooks (installed from the deck's `hooks/`) block
  commits and pushes that touch the trunk branch (`main`).
- Agents open PRs; humans merge. Commit style: conventional prefixes
  (`feat:`, `fix:`, `docs:`, `chore(#N):`).

## Issue store

- The issue tracker is the remote GitHub tracker; full artifacts live in the
  local issue store — an orphan-branch worktree on `issues-data` — created
  and managed by the deck's tool: `./.opencode/tools/local-issues`. Run its
  `init` first (bootstrap worktrees), then `sync` for currency. Never edit
  store YAML by hand; every numbered command uses the qualified
  `brothertown-language-com#N` form.
- `.issues/**` is workflow state only — never depended on as remaining or
  being available; the records work depends on live in tracked repository
  files, such as the Cloudflare facts of record, `docs/cloudflare-facts.md`
  (developer correction, 2026-10-26).

## Agent deck

- `.opencode/` is a local clone of the shared agent deck (remote
  `michael-conrad/.opencode`), gitignored by design: do not commit it, and
  treat its contents as deck-governed.
- Tools run from the repo's own deck copy: `./.opencode/tools/<tool>`.
- Hooks: if `.git/hooks/pre-commit`/`pre-push` are missing, copy them from
  the deck's `hooks/` directory.

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)
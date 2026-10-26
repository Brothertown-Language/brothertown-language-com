<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — Cloudflare platform facts of record: always-in-context for Cloudflare work (brothertown-language-com #10)

## Problem

Cloudflare platform behaviors are load-bearing for this repository but
recorded only as one-liners in the root `AGENTS.md` and dated ops entries in
the (closed) issue-3 runbook facts log. No single record holds the fact set
as always-discoverable work context. The trigger event (2026-10-26): work
established that **Workers Builds clones the repository non-recursively** —
submodule directories arrive empty at build time and there is no setting to
change that — and this fact existed in none of the repository's records. The
developer's 2026-10-26 statements that ground this spec:

- Submodules in this repository are wanted **for local usage and reference
  materials only** — they are not needed for the site deployment.
- Directive: add a spec recording the submodule finding and the other
  Cloudflare-specific information that must always be kept in context for
  work.

Platform facts are the fastest-decaying knowledge class in this stack: they
live in vendor docs that change regularly, sit outside training-data
validity, and silently invalidate build assumptions when carried stale or
absent — the exact failure shape the trigger event exposed (a build expecting
submodule content fails with no Cloudflare-side error pointing at the cause).

## Scope

Issue-store record only — **this spec is the record**. No repository files,
wiki pages, or CI configuration change for this issue. Consumers: future
work sessions touching the site build, the Workers deployment, CI build
behavior, or the Cloudflare/R2/itch.io hosting decisions. Any such session
starts from this record's facts of record — each with its verification date —
never from session memory.

## Requirements

- **R-1** — The record enumerates the Cloudflare facts of record as fact
  rows F-1 through F-13 (Facts of record below); every row carries the fact
  statement, the date(s) verified, and at least one source (live URL, or a
  dated in-repo / in-store record of record).
- **R-2** — The record carries the **submodule operational rule**:
  submodules in this repository are for local usage and reference only,
  per the developer's 2026-10-26 statement. Nothing the build consumes may
  live in a submodule path — those directories are empty at build time
  (F-2). Build-time consumption of external data is tracked files, or a
  fetched-and-verified step inside `build.sh`. If a future need ever makes
  submodule content required at build time, the only verified-documented
  path is `git submodule update --init --recursive` inside the build, in
  the shape the Zola guide documents (git is preinstalled in the build
  image, F-5). The **private-submodule case is deliberately not recorded**
  here: no source for its credential/token behavior was live-verified at
  record time — treat it as unverified territory to research live before
  relying on that case.
- **R-3** — The record carries the **currency rule**: every fact row is
  dated; when live work discovers a new load-bearing Cloudflare fact, or
  re-verification contradicts a row, the record is edited in place in the
  same session the change is discovered — superseded statements removed,
  never accumulated. The record is kept current, not re-derived per session.
- **R-4** — The record is self-contained work context: a session can act on
  Cloudflare work from this record alone. `AGENTS.md` and the runbook facts
  log carry summaries and pointers; they are never the fuller source.

## Facts of record

### F-1 — Platform of record is Workers, not Pages

Cloudflare Workers (Static Assets) hosting is this site's platform of
record. Cloudflare's own recommendation is to **start new projects with
Workers** (repo decision of record, verified 2026-10-26). The domain
`brothertown-language.com` is purchased and its zone lives on Cloudflare
(verified live 2026-10-25). Cloudflare Pages is the legacy platform — facts
from its docs must never transplant to Workers facts (see F-4).

Sources: root `AGENTS.md` (site decisions of record, dated 2026-10-25 /
2026-10-26); Workers Builds docs overview (read 2026-10-26,
https://developers.cloudflare.com/workers/ci-cd/builds/).

### F-2 — Workers Builds clone behavior: submodules absent, not configurable

A Workers Builds run clones **only the connected repository,
non-recursively**: `.gitmodules` submodule directories arrive present but
empty; submodule content is never initialized. This is **not configurable**
— verified against every control surface:

- Dashboard build settings (configuration page): Git account/repository/
  branch, build / deploy / preview commands, root directory, API token,
  build variables and secrets — no submodule toggle (page updated
  2026-09-22).
- Builds REST API trigger schema: `trigger_name`, `build_token_uuid`,
  `build_command`, `deploy_command`, `root_directory`, `branch_includes`,
  `branch_excludes`, `path_includes`, `path_excludes`,
  `build_caching_enabled`, `environment_variables` — no submodule field
  (page updated 2026-09-22).
- The current builds documentation surface (builds, configuration,
  build-image, api-reference, troubleshoot, git-integration,
  github-integration, advanced-setups, limits-and-pricing) carries **no
  submodule statement at all**; a code search of `cloudflare/cloudflare-docs`
  finds "submodule" only in the Pages docs.

Verified 2026-10-26. Sources:
https://www.getzola.org/documentation/deployment/cloudflare-workers/
("Cloudflare doesn't clone the repo recursively" — Zola's current Cloudflare
Workers deployment guide);
https://developers.cloudflare.com/workers/ci-cd/builds/configuration/ ;
https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/ ;
GitHub code search over cloudflare/cloudflare-docs (2026-10-26).

### F-3 — Submodule operational rule (developer decision, 2026-10-26)

Submodules on this repository are for **local usage and reference
materials only** — not needed for the site deployment (developer statement,
2026-10-26; recorded in R-2). Build inputs are tracked files — or a
fetched-and-verified step inside `build.sh` for external data. The only
verified-documented path if submodule content were ever required at build
time: `git submodule update --init --recursive` inside the build, in the
shape the Zola guide documents (git is preinstalled in the build image,
F-5). The private-submodule case is deliberately not recorded here: no
source for its credential/token behavior was live-verified at record time —
treat it as unverified territory to research live before relying on that
case.

Source: developer statement (2026-10-26, this issue); workaround shape:
https://www.getzola.org/documentation/deployment/cloudflare-workers/ .

### F-4 — Pages ≠ Workers Builds: the confusion trap

Only the legacy **Pages** platform's clone step processes submodules —
Pages' debugging docs walk through `.gitmodules` validation requiring both a
`path` and a `url` property, i.e. Pages checks submodules out and fails the
clone step on malformed entries. **Pages behavior never transfers to Workers
Builds facts** — this repository's platform of record is Workers (F-1), so
F-2's behavior governs. Verified 2026-10-26. Source:
https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/pages/configuration/debugging-pages.mdx
(Pages debugging docs).

### F-5 — Builds image contents

Workers Builds build image: **Ubuntu 24.04, x86_64**; apt installs include
`git` and `git-lfs`. Runtimes: Node.js **24.22.1** (22.23.4 also
preinstalled), Python **3.14.8**, Go **1.27.3**, Ruby **3.4.11**. Package
managers: npm **10.9.2**, yarn 4.18.1, pnpm 10.11.1, bun 1.4.4. Static-site
tooling preinstalled: **Hugo extended 0.147.7** — and **no Zola** (the
preinstalled-package tables list no Zola entry). Verified 2026-10-26.
Source: https://developers.cloudflare.com/workers/ci-cd/builds/build-image/
(page updated 2026-10-26 — the read was same-day current).

### F-6 — Version control: which overrides exist

Overridable tools accept an environment variable (`NODE_VERSION`,
`HUGO_VERSION`, `PYTHON_VERSION`, `BUN_VERSION`, `PNPM_VERSION`,
`YARN_VERSION`, …) or the corresponding file (`.nvmrc`, `.node-version`,
`.python-version`, `runtime.txt`, `.ruby-version`), except npm/yarn/pnpm/bun
which are controlled by the `packageManager` field in `package.json`.
`engines.npm` is **not** honored; `packageManager` is the only npm-version
control. **No Zola override hook exists** — a Zola version in this stack is
pinned by `ZOLA_VERSION` and fetched by the build command (F-12). Verified
2026-10-26. Sources:
https://developers.cloudflare.com/workers/ci-cd/builds/build-image/ ; root
`AGENTS.md` (dated 2026-10-26).

### F-7 — Builds limits (free plan)

| Metric | Free-plan value |
| --- | --- |
| Build minutes | 3,000 / month |
| Concurrent builds | 1 |
| Build timeout | 20 minutes |
| Deploy hooks | 10/min per Worker; 100/min per account |
| CPU | 2 vCPU |
| Memory | 8 GB |
| Disk space | 20 GB |
| Environment variables | 64; 5 KB each |

Verified 2026-10-26. Source:
https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/
(page updated 2026-05-29).

### F-8 — Static-asset limits and the big-asset routing

Workers Static Assets (free tier): **25 MiB per file; 20,000 files per
assets version** (verified 2026-10-12 — the dated source lives in the
runbook facts log, closed issue #3). Larger game assets route to **Cloudflare
R2** (same account) or **itch.io** hosting (verified 2026-10-25: HTML5 free
hosting 200 MB/file and 500 MB/project; download files 1 GB/file by
default; per-platform download channels via butler — windows/macos/linux/
android). Sources: runbook facts log (Cloudflare-Runbook-Facts-Log.md,
dated 2026-10-12); root `AGENTS.md`.

### F-9 — Build/preview command surface

Default deploy command: `npx wrangler deploy`; customizable (e.g.
`npx wrangler deploy --assets ./public/`). Default preview command:
`npx wrangler preview`; changing it to `wrangler versions upload` creates
Worker versions and Version URLs instead of Previews. Automatic dependency
installation can be disabled with the `SKIP_DEPENDENCY_INSTALL` build
variable (`1` or `true`). Triggers carry per-Worker build caching
(`build_caching_enabled`) and branch/path include/exclude fields
(`branch_includes`, `branch_excludes`, `path_includes`, `path_excludes`).
Wrangler runs at the version set in the repo's `package.json` when one
exists. Verified 2026-10-26. Sources:
https://developers.cloudflare.com/workers/ci-cd/builds/configuration/
(updated 2026-09-22);
https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/
(updated 2026-09-22);
https://developers.cloudflare.com/workers/ci-cd/builds/build-image/ .

### F-10 — Workers name requirement

The dashboard Worker name must match the `name` in the Wrangler
configuration file located in the configured root directory, or the build
fails. On Wrangler v3 and up, Workers Builds auto-overrides the name via the
`WRANGLER_CI_OVERRIDE_NAME` environment variable; the requirement relaxes
for Wrangler Environments where the prefix before `-` matches. Verified
2026-10-26. Source:
https://developers.cloudflare.com/workers/ci-cd/builds/troubleshoot/
(page updated 2026-10-24).

### F-11 — Git-provider support boundary

Workers Builds connects hosted **GitHub**, **GitLab**, Cloudflare
**Artifacts**, and Cursor Origin repositories. Self-hosted GitHub/GitLab
instances are **not** supported. Other providers (e.g. Bitbucket) build
through an external CI/CD provider deploying with the Wrangler CLI. Verified
2026-10-26. Source:
https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/
(page updated 2026-10-01).

### F-12 — This site's build pipeline of record (repo facts of record)

- `ZOLA_VERSION` (repo root) pins the single Zola version of record; the
  pin is a `vMAJOR.MINOR.PATCH` string, format-checked by the build.
- `build.sh` is the CI build entry: validates the pin and the x86_64 build
  architecture, downloads the pinned Zola release from Zola GitHub Releases
  (no Zola preinstall exists, F-5; no Zola override hook exists, F-6),
  installs it to `~/.local/bin`, refreshes the gitignored working-tree
  `./zola` (used by `./zola check` / `./zola serve` per the root
  `AGENTS.md` commands), and builds to `public/` (gitignored).
- **Zola is version-pinned; Wrangler is not**: the repository carries no
  `package.json` (repo tree, 2026-10-26), so the deploy command's Wrangler
  resolution is unpinned (F-9). Pinning Wrangler would require adding
  `package.json` + `packageManager` — a named future option, out of this
  record's scope to decide.
- `./zola check` warning baseline lives with the repo commands of record
  (root `AGENTS.md`); only ERROR lines matter post-setup.
- Domain attach: `brothertown-language.com` zone on Cloudflare (F-1).

Verified 2026-10-26 (`build.sh`, `ZOLA_VERSION`, `zola.toml`, `.gitignore`
lines `/public/`, `/zola`, `opencode.jsonc`; repo tree). Sources: repo tree
of record; closed issue #1 (base Zola site setup, delivered).

### F-13 — Cloudflare-side inspection surface

The repository's agent config (`opencode.jsonc`) carries the **Cloudflare
MCP service** (`https://mcp.cloudflare.com/mcp`) with denied-by-default
permissions and a read-only `cloudflare-ops` sub-agent scoped to inspection
of brothertown-language.com (DNS records, Pages status, account identity).
The decision of record is closed issue #4 (repo agent config). Verified
2026-10-26 (`opencode.jsonc` content; issue #4 closed).

## Success criteria

| ID | Criterion | Class | Instrument |
| --- | --- | --- | --- |
| SC-1 | Every fact row F-1..F-13 carries a fact statement, a verification date, and at least one source (live URL or dated in-repo/in-store record of record) | structural | sweep of `.issues/10/spec.md`: for each of F-1..F-13 assert the three elements present and non-empty; zero rows missing an element |
| SC-2 | Every externally-verified row (F-1, F-2, F-4, F-5, F-6, F-7, F-9, F-10, F-11) cites a live URL whose current content supports the stated fact | structural | per-fact currency re-check: fetch each cited URL and confirm the cited page supports its row's statement |
| SC-3 | The submodule operational rule and the build-time workaround are stated with dated attribution to the developer's 2026-10-26 statements | structural | content check of `.issues/10/spec.md`: local-only rule present (R-2/F-3), empty-at-build-time consequence present, workaround present, developer attribution dated |
| SC-4 | The record's deliverable lives only in the issue store; no repository, wiki, or CI file changed for this issue | structural | `git status --porcelain` on the main worktree: no tracked-file modifications from this issue (pre-existing untracked paths belong to other issues' work); the record exists at `.issues/10/spec.md` only |

## Out of scope

- Creating any submodules or choosing which repositories to submodule —
  a future decision; this record only fixes the platform behavior that
  constrains it (F-2, F-3).
- Changes to `AGENTS.md`, `docs/`, the wiki, `build.sh`, or CI wiring.
- Any deployment or dashboard-side Cloudflare configuration change.
- Pinning Wrangler via `package.json`/`packageManager` — named in F-12 as a
  future option; not decided or executed here.

## Approach

The record is this spec, born complete at filing: facts carried from dated
records of record (root `AGENTS.md`, closed issues #1/#3/#4, `build.sh`,
`opencode.jsonc`) plus live verification against Cloudflare's current
documentation on 2026-10-26 (the docs sweep and code search cited in F-2,
F-4–F-7, F-9–F-11). No plan or implementation phase is scheduled — nothing
outside the issue store changes. The fresh-context validation dispatch is
the record's review gate; after validation the issue waits for developer
review. Maintenance thereafter follows the currency rule (R-3): in-place
edits, dated, superseded statements removed.

## Impact

Consumers: every future session doing build/deploy/CI/app-hosting work on
this repository — the record is the first surface for Cloudflare facts.
Blast radius: knowledge layer only — no code, no deploys, no dashboard
state. Risk if absent or stale: build/deploy assumptions silently wrong —
the exact failure the trigger event exposed (submodule content expected at
build time; there is no Cloudflare-side error to point at the cause). Cost:
one spec artifact plus the per-fact currency re-checks (SC-2's instrument,
re-runnable at any time).

> Full spec and plan artifacts: https://github.com/Brothertown-Language/brothertown-language-com/tree/issues-data/10/
>
> Agent-ingest artifacts pointer: `.issues/10/`

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
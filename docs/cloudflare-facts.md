<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Cloudflare facts of record

Always-in-context Cloudflare knowledge for this repository. This file is the
**first surface for any Cloudflare, build, deploy, or CI work** here — the
root `AGENTS.md` points to it. Consult the fact rows below before acting;
every row is dated and sourced. Act on these facts, never on session memory,
training data, or prior sessions' knowledge.

## How this record is maintained (currency rule)

- Every fact row carries the fact statement, the date(s) verified, and at
  least one source (a live URL, or a dated in-repo / wiki record of record).
- When live work discovers a new load-bearing Cloudflare fact, or
  re-verification contradicts a row, the row is edited in place in the same
  session the discovery happens — superseded statements are removed, never
  accumulated — landing through the repository's PR review flow (humans
  merge). The record is kept current, not re-derived per session.
- This record is deliberately self-contained: a session can act on
  Cloudflare work from this file alone.

## Fact rows

The submodule operational rule is fact row **F-3** below — read it before
letting submodules anywhere near the build.

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
2026-10-26). Nothing the build consumes may live in a submodule path —
those directories are empty at build time (F-2). Build inputs are tracked
files — or a fetched-and-verified step inside `build.sh` for external data.

The only verified-documented path if submodule content were ever required
at build time: `git submodule update --init --recursive` inside the build,
in the shape the Zola guide documents (git is preinstalled in the build
image, F-5). The **private-submodule case is deliberately not recorded**
here: no source for its credential/token behavior was live-verified at
record time — treat it as unverified territory to research live before
relying on that case.

Source: developer statement (2026-10-26, brothertown-language-com#10 — this
record's filing issue); workaround shape:
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
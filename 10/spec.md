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
- Developer correction (2026-10-26): nothing in `.issues/` can be depended
  on as remaining or being available — the record's availability must not
  hang on the issue store; the original filing's store-only placement is
  superseded in place by this revision.
- Directive (2026-10-26): the local-issues re-open gap found in this
  correction → a remote bug report filed via the GitHub API to the deck
  repo (done: `michael-conrad/.opencode#2672`); and the root `AGENTS.md`
  gains the rule preventing recurrence of depending on `.issues/**`,
  alongside the record pointer.

Platform facts are the fastest-decaying knowledge class in this stack: they
live in vendor docs that change regularly, sit outside training-data
validity, and silently invalidate build assumptions when carried stale or
absent — the exact failure shape the trigger event exposed (a build expecting
submodule content fails with no Cloudflare-side error pointing at the cause).

## Scope

Durable record deliverables in the repository proper — present in every
clone, reviewable through PR, the only dependable surfaces for work
knowledge: `docs/cloudflare-facts.md` (the record of record) and two
root-`AGENTS.md` edits (R-5). The issue store carries this spec as the
work's contract — workflow bookkeeping, never the record; the store copy of
the fact set is not maintained after the doc lands (the doc is the single
record). No content pages, no templates, no wiki edits, no CI configuration
change. Companion action on developer instruction, outside this repo's
changeset: the deck-defect bug report `michael-conrad/.opencode#2672`
(filed via the GitHub API). Consumers: future work sessions touching the
site build, the Workers deployment, CI build behavior, or the
Cloudflare/R2/itch.io hosting decisions — they load
`docs/cloudflare-facts.md` (discovered via the `AGENTS.md` pointer) as the
first surface for Cloudflare facts, each row dated, never from session
memory.

## Requirements

- **R-1** — `docs/cloudflare-facts.md` exists as a tracked repository file
  (SPDX header) and is the Cloudflare facts record of record. It enumerates
  the fact rows F-1 through F-13 (Facts of record below is the initial
  content definition); every row carries the fact statement, the date(s)
  verified, and at least one source (live URL, or a dated in-repo / wiki
  record of record).
- **R-2** — The doc carries the **submodule operational rule**: submodules
  in this repository are for local usage and reference only, per the
  developer's 2026-10-26 statement. Nothing the build consumes may live in
  a submodule path — those directories are empty at build time (F-2).
  Build-time consumption of external data is tracked files, or a
  fetched-and-verified step inside `build.sh`. If a future need ever makes
  submodule content required at build time, the only verified-documented
  path is `git submodule update --init --recursive` inside the build, in
  the shape the Zola guide documents (git is preinstalled in the build
  image, F-5). The **private-submodule case is deliberately not recorded**
  there: no source for its credential/token behavior was live-verified at
  record time — treat it as unverified territory to research live before
  relying on that case.
- **R-3** — The doc carries the **currency rule**: every fact row is dated;
  when live work discovers a new load-bearing Cloudflare fact, or
  re-verification contradicts a row, the doc is edited in place in the
  same session discovery happens — superseded statements removed, never
  accumulated — landing through the repository's PR review flow (humans
  merge). The record is kept current, not re-derived per session.
- **R-4** — The doc is self-contained work context: a session can act on
  Cloudflare work from the doc alone.
- **R-5** — The root `AGENTS.md` gains exactly two edits for this issue:
  (a) a pointer line naming `docs/cloudflare-facts.md` as the Cloudflare
  facts of record to consult before any Cloudflare/build/deploy/CI work;
  (b) a rule that `.issues/**` contents are workflow state only — never
  depended on as remaining or available; records work depends on live in
  tracked repository files (developer correction, 2026-10-26). Nothing
  beyond those two edits changes in `AGENTS.md` (issue #8's planned
  `AGENTS.md` additions are #8's own scope).

## Facts of record

Initial content definition for `docs/cloudflare-facts.md` — fact rows are
unchanged from the validated original filing; the relocation is
placement-only, not a content change.

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
2026-10-26). Build inputs are tracked files — or a
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
| SC-1 | `docs/cloudflare-facts.md` is a tracked repository file (SPDX header) carrying fact rows F-1..F-13, each with a fact statement, verification date, and at least one source (live URL or dated in-repo/wiki record of record) | structural | `git ls-files docs/cloudflare-facts.md` non-empty; content sweep of the doc: all 13 row IDs present, each carrying the three elements; SPDX header present |
| SC-2 | Every externally-verified row (F-1, F-2, F-4, F-5, F-6, F-7, F-9, F-10, F-11) in the doc cites a live URL whose current content supports the stated fact | structural | per-fact currency re-check: fetch each cited URL and confirm the cited page supports its row's statement |
| SC-3 | The doc states the submodule operational rule and the build-time workaround with dated attribution to the developer's 2026-10-26 statements, and records the private-submodule credential case as deliberately unrecorded | structural | content check of the doc: the local-only rule, the empty-at-build-time consequence, the public-submodule workaround, the dated developer attribution, and the gap statement all present |
| SC-4 | The root `AGENTS.md` carries the pointer line naming `docs/cloudflare-facts.md` and the `.issues/**` workflow-state-only rule; the branch's only other changed file is `docs/cloudflare-facts.md` | structural | grep `AGENTS.md` for both elements; `git diff --name-only main...HEAD` lists exactly `AGENTS.md` and `docs/cloudflare-facts.md` |

## Out of scope

- Creating any submodules or choosing which repositories to submodule —
  a future decision; the record only fixes the platform behavior that
  constrains it (F-2, F-3).
- Wiki pages, `build.sh`, CI wiring, and Zola content (`content/`,
  `templates/`, `static/`, `zola.toml`) — untouched by this work; the
  `docs/` tree is not built by Zola.
- Any deployment or dashboard-side Cloudflare configuration change.
- Pinning Wrangler via `package.json`/`packageManager` — named in F-12 as a
  future option; not decided or executed here.
- Maintaining a synchronized `.issues/` copy of the fact content — the doc
  is the single record; the store carries this spec as the work contract
  only.
- Fixing the deck's `local-issues` tool — the defect is filed to
  `michael-conrad/.opencode` (#2672); this repo's deck copy is consumed,
  not patched (deck changes are deck-governed).

## Approach

Feature branch (`feature/<scope>-<slug>`; the branch card governs
naming): write `docs/cloudflare-facts.md` from this spec's fact set
(content unchanged from the validated original filing) and apply the two
`AGENTS.md` edits (R-5); land via PR — humans merge. The fact content was
verified live on 2026-10-26 (the docs sweep and code search cited in F-2,
F-4–F-7, F-9–F-11; repo-tree checks for F-12/F-13); the relocation changes
placement, not content. Maintenance thereafter follows the doc's currency
rule (R-3): in-place edits, dated, superseded statements removed, via PR.
The store carries this spec as the ticket's contract; the store copy of
the fact set is workflow bookkeeping, not the record. The deck-side tool
defect found in re-opening this issue is filed to `michael-conrad/.opencode`
(#2672, developer instruction).

## Impact

Consumers: every future session doing build/deploy/CI/app-hosting work on
this repository — the record is the first surface for Cloudflare facts,
discovered via the `AGENTS.md` pointer, with availability guaranteed by the
repository itself rather than the issue store. Blast radius: the `docs/`
tree and the two `AGENTS.md` edits — no code, no deploys, no dashboard
state; `docs/` is not built by Zola. Coordination note (non-blocking): open
issue #8 plans a `docs/`-tree inventory in its future `/docs/AGENTS.md`;
when it lands, its inventory should include this record's file. Risk if
absent or stale: build/deploy assumptions silently wrong — the exact
failure the trigger event exposed (submodule content expected at build
time; no Cloudflare-side error points at the cause), and recurrence of
store-dependency for durable knowledge. Cost: one tracked doc + two
`AGENTS.md` edits plus the per-fact currency re-checks (SC-2's instrument,
re-runnable at any time).

> Full spec and plan artifacts: https://github.com/Brothertown-Language/brothertown-language-com/tree/issues-data/10/
>
> Agent-ingest artifacts pointer: `.issues/10/`

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
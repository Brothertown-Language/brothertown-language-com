<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — Cloudflare Workers setup runbook (brothertown-language-com #3)

Runbook specification for setting up the hosted instance of
brothertown-language-com on Cloudflare under current recommendations, with the
domain already provisioned. Grounded in live primary docs (verified
2026-10-26), not in the sibling site's Pages-era practice.

## Problem

The decision-of-record trail (2026-10-25 brainstorm, issue #1) pinned this
site's hosting to Cloudflare Pages with the sibling deployment
(michael-conrad.com) as the worked precedent. Two developer directives
(2026-10-26) supersede that basis for the new site: use the latest versions of
things, and use the latest recommendations — do not cargo-cult the sibling's
Pages-era mechanics. The current docs (verified live 2026-10-26) show
Cloudflare recommending Workers as "the primary platform for building
applications" and opening the Pages docs with "Are you sure you want to use
Pages? … Start new projects with Workers"; no sunset deadline is announced and
the migration guide is voluntary. The site's actual setup procedure — connect
the repo, build, deploy, attach the provisioned domain, verify HTTPS, and undo
— does not yet exist in tracked, executable, current-docs-grounded form.
Dashboard-side operations are developer-executed (production/access
operations are not agent-reachable without explicit instruction, per issue
#1's scope record); a runbook is the record that makes them repeatable and
verifiable.

## Scope

The deliverable is the tracked runbook document itself. It documents the
cloud-side setup and operation procedure for the developer-executor and the
agent-runnable verification gates; the in-repo deployment artifacts it
consumes (`wrangler.jsonc`, build entry, `ZOLA_VERSION`, built `public/`)
belong to the base-setup issue #1 as revised to these same directives.
Dashboard execution happens on the developer's Cloudflare account; the agent
never executes it without explicit instruction.

## Requirements

- **R-1** — The repository SHALL carry a tracked runbook at
  `docs/runbook-cloudflare-workers-setup.md` covering prerequisites and blast
  radius, deployment-unit facts, Workers Builds git-connection setup, the
  build pipeline, the custom-domain attach, HTTPS verification gates,
  rollback, and teardown — organized so the executor can run each section
  top-to-bottom without leaving the document.
- **R-2** — Every operative Cloudflare platform fact in the runbook SHALL
  carry an inline primary-source URL and its verification date (live fetches,
  2026-10-26), plus a maintenance rule: a dashboard step that no longer
  matches the runbook is re-verified against the cited docs before the
  runbook is edited — memory and cached pages are not grounds.
- **R-3** — The runbook SHALL record the platform selection with its
  evidence: Cloudflare's current "Start new projects with Workers"
  recommendation (dated quote + URL) and the voluntary, deadline-free
  migration note; every adopted mechanism SHALL be grounded in a current
  Workers-docs citation; sibling Pages-era mechanics (including
  `CLOUDFLARE_UPDATE.md`'s Pages v3 pattern) appear only as labeled
  historical context.
- **R-4** — The runbook SHALL document the deployment unit per the current
  wrangler configuration reference: an assets-only `wrangler.jsonc` with
  `name`, `compatibility_date` (set to the authoring date per docs),
  `assets.directory` at `./public`, and `not_found_handling` `"404-page"`;
  assets-only requires no Worker script and no binding; and it SHALL name the
  repo-side artifacts this consumes as prerequisites (`wrangler.jsonc`, build
  entry, `ZOLA_VERSION`, built `public/`) delivered by the base-setup issue's
  platform revision under the same 2026-10-26 directives.
- **R-5** — The runbook SHALL record version currency as verified at
  authoring: Zola latest stable v0.23.6 (published 2026-09-12; asset
  `zola-v0.23.6-x86_64-unknown-linux-gnu.tar.gz`); wrangler 4.152.0 (npm
  `dist-tags.latest`); Workers Builds image Ubuntu 24.04 x86_64 with Node
  24.21.0 default and 22.23.2 also preinstalled — and SHALL record the
  refresh procedure: re-verify latest stable values at each runbook touch by
  checking the same sources (npm `dist-tags`, GitHub releases API,
  build-image page), then update `ZOLA_VERSION` and `compatibility_date`
  through the normal PR flow.
- **R-6** — The runbook SHALL document the build pipeline per the current
  Workers Builds build-image facts: the image does not preinstall Zola and
  offers no Zola version-override hook, so the build command executes a
  tracked script that downloads exactly the pinned Zola release from GitHub
  releases and builds into `public/`; deploy command default
  `npx wrangler deploy`; production branch `main`; non-production branches
  build preview deployments (PR-comment preview URLs, `noindex` behavior).
  The runbook SHALL state that controlling the Zola version by pin + download
  is grounded in the current Workers Builds docs — not in sibling precedent.
- **R-7** — The runbook SHALL document the custom-domain attach for
  `brothertown-language.com` given the pre-provisioned state (domain
  registered; DNS zone on Cloudflare): Workers dashboard → Settings >
  Domains & Routes > Add > Custom Domain; automatic DNS-record creation on
  zones the account owns; the documented caution that a custom domain cannot
  be created on a hostname with an existing conflicting CNAME record or on a
  zone the account does not own; exact-hostname matching (the apex does not
  cover `www` and vice versa) with the redirect-rule pattern for the
  uncovered hostname; and workers.dev coexistence with both disable paths
  (Settings toggle or `"workers_dev": false`).
- **R-8** — The runbook SHALL document HTTPS verification: Workers custom
  domains provision per-hostname Advanced Certificates (not Universal SSL
  certificates) with certificate issuance and DNS record creation handled
  automatically because Cloudflare is the authoritative DNS; current docs
  publish no issuance-time SLA, so timing verification is empirical. Gates:
  `curl -sv https://brothertown-language.com/` (shows the edge certificate
  and the Worker-served response) and a `dig` check of the auto-created
  record, with a retry decision point (re-run the probe until green or
  escalate).
- **R-9** — The runbook SHALL state rollback and teardown ahead of the first
  cloud-side write action, and SHALL document them in executable detail:
  instant rollback via Deployments → Rollback (bounded to the 100 most
  recently published versions; `wrangler versions upload` noted as the
  not-promoted variant feeding the promotion-policy decision point); teardown
  sequence: disconnect the build integration → remove the custom domain →
  inspect zone DNS records and delete any record left behind (documented
  auto-cleanup behavior absent — verify on detach) → manually remove the
  leftover Advanced Certificate under SSL/TLS > Edge Certificates (documented
  caution: the certificate is not auto-deleted) → delete the Worker → verify
  via curl that the domain no longer serves.
- **R-10** — The runbook SHALL mark every step's executor: cloud/dashboard
  steps are developer-run; agent-runnable gates (curl, dig, local build
  reproduction) named as such. The agent executes no Cloudflare-side
  operation without explicit instruction.
- **R-11** — The runbook SHALL state each configuration choice as an explicit
  decision point — condition → branch with the deciding evidence — and SHALL
  NOT use open "adjust as appropriate" language anywhere.

## Success criteria

| ID | Criterion | Class | Instrument |
|----|-----------|-------|-----------|
| SC-1 | The runbook is tracked at `docs/runbook-cloudflare-workers-setup.md` | structural | `git ls-files docs/` lists it; the file exists |
| SC-2 | Prerequisites + blast radius precede the first cloud-side write step and enumerate: the Cloudflare-account prerequisite, the domain/zone already-on-Cloudflare fact, repo-side prerequisites (wrangler.jsonc, build entry, `ZOLA_VERSION`, built `public/`), the agent/developer executor split, and rollback availability | structural | doc-structure audit: locate the first dashboard-write step; assert the section precedes it and carries each enumerated item |
| SC-3 | Every operative platform fact carries an inline primary-source URL plus verification date; the facts log and the re-verify-before-edit maintenance rule are present | structural | fact-by-fact citation audit over the whole document |
| SC-4 | The platform-selection record cites the dated Workers recommendation (quote + URL) and labels every superseded Pages-era/sibling mechanic as historical context | structural | audit the selection record for the dated quote; check every sibling/Pages-era reference for its historical-context label |
| SC-5 | The `wrangler.jsonc` section shows the assets-only shape — `name`, `compatibility_date`, `assets.directory "./public"`, `not_found_handling "404-page"`, no script/binding — matching the cited configuration reference | structural | field-by-field comparison against the cited reference (2026-10-20) |
| SC-6 | Version facts recorded with dates (Zola 0.23.6 / 2026-09-12 + asset name; wrangler 4.152.0; Node 24.21.0 default / 22.23.2 preinstalled; image Ubuntu 24.04 x86_64) plus the refresh procedure naming its sources | structural | cross-check each value and date against the cited sources; assert the procedure names npm `dist-tags`, the GitHub releases API, and the build-image page |
| SC-7 | Build-pipeline facts: Zola not preinstalled and no override hook; pinned-download build entry grounded in current docs; deploy command `npx wrangler deploy`; production branch `main`; preview deployments with PR-comment URLs and `noindex` | structural | fact-by-fact audit against the cited build-image/configuration pages |
| SC-8 | Domain attach: flow path; automatic DNS-record creation; conflicting-CNAME caution; exact-hostname apex/www split with the redirect-rule pattern; workers.dev coexistence plus both disable paths | structural | enumerated-item audit against the cited domain pages |
| SC-9 | HTTPS: Advanced-Certificate model (not Universal SSL; no ACM subscription); automatic DCV; no-published-SLA noted as empirical; `curl -sv` and `dig` gates with stated expected outputs and a retry decision point | structural | enumerated-item audit; assert the gate commands appear with expected outputs |
| SC-10 | Rollback (mechanism, 100-version limit, deploy-vs-versions-upload promotion note) and teardown (disconnect builds → detach domain → DNS-record check → manual certificate removal under SSL/TLS > Edge Certificates → delete Worker → verify down) are complete and placed before the first cloud-side write | structural | enumerated-item audit plus section-order check |
| SC-11 | Every configuration choice is condition → branch with deciding evidence; zero "adjust as appropriate" phrasing | structural | audit the named choices (production branch, build command, workers.dev disable, www policy, promotion policy, GH Actions alternative) plus a full-text sweep for open-ended instruction |
| SC-12 | Every step carries its executor mark (developer-run vs agent-runnable) | structural | step-by-step marking audit |
| SC-13 | The agent-runnable gates run exactly as written and produce the runbook's stated expected outputs | behavioral | execute the gates at the runbook's stated checkpoint (prerequisites in force: issue-#1 artifacts deployed, domain attached); assert outputs match |

## Out of scope

- Domain registration, DNS-zone creation, and nameserver changes (provisioned
  and verified: dig 2026-10-25 in issue #1's record; developer statement
  2026-10-26).
- Execution of the dashboard steps themselves (developer-run per R-10).
- The in-repo deployment artifacts (`wrangler.jsonc`, build entry,
  `ZOLA_VERSION`) — base-setup issue territory after its platform revision.
- Site content, theme, and section build-out (issue #1 and later issues).
- Cloudflare Access preview lockdown and build-caching optimization
  (optional capabilities, not requested).

## Approach

Author the runbook from the current primary docs captured in this session's
research (all fetched 2026-10-26 with visible last-updated dates on page):
Workers Static Assets assets-only deployment; Workers Builds git integration
(arbitrary build command; Ubuntu 24.04 x86_64 image; curl/wget/unzip/zstd
preinstalled; 20-minute build timeout); custom-domain attach with automatic
DNS-record creation on the existing zone; per-hostname Advanced Certificates
with automatic DCV; instant rollback; teardown with the documented
certificate caution. Structure follows the operational-runbook discipline
(prerequisites → procedure → verification → rollback), decision points
explicit, executor marks per step, facts log carrying source + date per
fact. The pinned-Zola build entry is grounded in the current Workers Builds
docs (Zola absent from the image; arbitrary build commands supported; no Zola
override hook exists) — the same shape the sibling used, arrived at
independently under current docs rather than by cargo cult.

## Dependencies

- Runbook authoring requires no repo files; the document lands independently.
- The runbook's execution gates require issue #1's revised deployment
  artifacts to exist and the domain attach to have happened (SC-13's stated
  checkpoint).
- Ordering note for the developer: issue #1's implementation should not start
  until its spec's platform revision (Pages → Workers Static Assets, per
  these same directives) is decided — otherwise issue #1 lands Pages-shaped
  artifacts this runbook then disavows.

## Facts of record (verified 2026-10-26)

| Fact | Source (URL) | Date on page / fetch | Confidence |
|------|-------------|----------------------|------------|
| "Start new projects with Workers" interstitial on the Pages docs; Pages creation flows still documented | developers.cloudflare.com/pages/ | 2026-08-25 | high |
| Migration guide voluntary, no sunset deadline | developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/ | 2026-10-12 | high |
| Assets-only static config shape; assets served without Worker code; `not_found_handling "404-page"` | developers.cloudflare.com/workers/static-assets/ | 2026-10-12 | high |
| Workers Builds: navigation, arbitrary build command, deploy command default `npx wrangler deploy`, preview behavior | developers.cloudflare.com/workers/ci-cd/builds/ ; …/builds/configuration/ | 2026-10-15 / 2026-09-22 | high |
| Build image Ubuntu 24.04 x86_64; Node 24.21.0 default, 22.23.2 preinstalled; Zola NOT preinstalled; curl/wget/unzip/zstd present; update policy | developers.cloudflare.com/workers/ci-cd/builds/build-image/ | 2026-10-24 | high |
| Builds limits: free 3,000 min/mo, 1 concurrent, 20-min timeout | developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/ | 2026-05-29 | high |
| Wrangler configuration reference (new URL); mandatory `name` + `compatibility_date`; asset fields incl. `html_handling`, `not_found_handling`, `.assetsignore` | developers.cloudflare.com/workers/wrangler/configuration/ | 2026-10-20 | high |
| wrangler latest stable 4.152.0 | registry.npmjs.org/wrangler/latest | fetched 2026-10-26 | high |
| Custom domains: flow, automatic DNS creation on owned zones, conflicting-CNAME caution, apex supported, exact-hostname matching, Advanced Certificate per hostname (not Universal SSL), cert-not-auto-deleted caution | developers.cloudflare.com/workers/configuration/routing/custom-domains/ | 2026-09-29 | high |
| workers.dev default-on; disable paths | developers.cloudflare.com/workers/configuration/routing/workers-dev/ | 2026-09-22 | high |
| Static-assets limits: 20,000 files/version (free), 25 MiB/file, requests to assets free and unlimited | developers.cloudflare.com/workers/platform/limits/ ; …/static-assets/billing-and-limitations/ | 2026-10-12 / fetched 2026-10-26 | high |
| Instant rollback; 100-most-recent-versions bound; `wrangler versions upload` not auto-promoted | developers.cloudflare.com/workers/configuration/versions-and-deployments/rollbacks/ ; …/versions-and-deployments/ | 2026-07-15 / 2026-09-22 | high |
| Zola latest stable v0.23.6, published 2026-09-12, asset name for x86_64 glibc | api.github.com/repos/getzola/zola/releases/latest | fetched 2026-10-26 | high |
| Universal SSL context (apex + first-level subdomains only) supporting the Advanced-Certificate comparison | developers.cloudflare.com/ssl/edge-certificates/universal-ssl/ | 2026-08-14 | high |
| GitHub Actions alternative: `cloudflare/wrangler-action@v4`, scoped API token | developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/ | 2026-04-23 | high |
| No official Zola guide exists on Workers framework-guides (index fetched; `/workers/framework-guides/zola/` 404) | developers.cloudflare.com/workers/framework-guides/ | fetched 2026-10-26 | high |

Documented gaps carried into the runbook, not papered over: (1) DNS-record
auto-cleanup on custom-domain detach / Worker delete is undocumented — the
runbook verifies record state on detach and deletes leftovers manually; (2)
no published issuance-time SLA for the Advanced Certificate — the runbook
verifies empirically with a retry decision point; (3) no published total
asset-size cap or bandwidth cap on the current limits pages; (4) the Workers
Builds limits page is the oldest fetched page (2026-05-29) — the runbook
date-stamps it and the facts log flags it as the oldest in the set.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
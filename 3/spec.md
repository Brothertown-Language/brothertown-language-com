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
verifiable. On 2026-10-26 the developer directed where that record lives: in
the repository's wiki, properly organized — not as an in-repo `docs/` file.
The wiki is enabled and verified live 2026-10-26 (`has_wiki: true` via the
GitHub API; the wiki remote `Brothertown-Language/brothertown-language-com.wiki.git`
reachable by `git ls-remote`).

## Scope

The deliverable is the runbook page set hosted in the repository's wiki
(`Brothertown-Language/brothertown-language-com.wiki`), organized for
operation per the developer's directive (2026-10-26). The wiki is operated
through a local checkout at `wiki/` — a gitignored sub-repo, never a
submodule — per the deck's wiki-operations card. The wiki is public (the
repository is public, and a public repository's wiki is available to the
public), and by default only repository-level write access can edit it;
wiki publishes are direct-publish — no branch, PR, or hook gates a push —
so publish follows verify-before-push discipline. The page set documents
the cloud-side setup and operation procedure for the developer-executor
and the agent-runnable verification gates; the in-repo deployment
artifacts it consumes (`wrangler.jsonc`, build entry, `ZOLA_VERSION`,
built `public/`) belong to the base-setup issue #1 as revised to these
same directives. The wiki page set is the single record of truth for
cloud-side operation: the repository carries no second copy of the
runbook. Dashboard execution happens on the developer's Cloudflare
account; the agent never executes it without explicit instruction.

## Requirements

- **R-1** — The repository's wiki SHALL host the runbook as an organized,
  navigable page set (flat layout per the deck's wiki-operations card),
  exactly these pages:
  - `_Sidebar.md` — the wiki's site-wide navigation panel, listing the
    runbook pages in their read order: overview and prerequisites →
    deployment unit and build pipeline → domain attach and HTTPS
    verification → rollback and teardown → facts log;
  - `Home.md` — the wiki's entry page, indexing the runbook pages and their
    read order;
  - one runbook page per operational section, at these stable hyphenated
    page names: `Cloudflare-Workers-Setup-Overview` (platform-selection
    evidence, prerequisites, blast radius, the executor split, rollback
    availability); `Cloudflare-Workers-Setup-Build-Pipeline` (git-connection
    setup, the `wrangler.jsonc` deployment unit, the build entry, version
    currency); `Cloudflare-Workers-Setup-Domain-HTTPS` (the custom-domain
    attach and the HTTPS verification gates);
    `Cloudflare-Workers-Setup-Rollback-Teardown` (rollback and teardown);
    `Cloudflare-Runbook-Facts-Log` (the facts log — source URL plus
    verification date per fact, and the maintenance rule);
  - each page runnable top-to-bottom for its own operational phase, so the
    executor of that phase is never sent to another page mid-step;
  - internal links in the `[[Page Name]]` syntax; no page carries YAML
    frontmatter; and the repository carries no in-repo copy of the runbook
    (`docs/runbook*` or otherwise — the wiki page set is the single record).
- **R-2** — Every operative Cloudflare platform fact in the runbook SHALL
  carry an inline primary-source URL and its verification date (live fetches,
  2026-10-26), plus a maintenance rule: a dashboard step that no longer
  matches the runbook is re-verified against the cited docs — memory and
  cached pages are not grounds — by whoever edits the runbook page, developer
  or agent, before that page is edited; the maintenance rule is stated on the
  facts-log page. Routing doctrine, from the developer's directives and
  observed UI facts: the runbook is DASHBOARD-ONLY — the developer executes
  no CLI commands; every cloud-side step is a dashboard action, and the
  tracked build script runs inside Cloudflare's build system, never in the
  developer's terminal; agent-marked probes (curl, dig, build reproduction)
  stay agent-executed. The observed surfaces: the dashboard's "Workers &
  Pages" sidebar option is absent on this account and the docs' own
  `dash.cloudflare.com/?to=/:account/workers-and-pages` deep link does not
  work there (both observed 2026-10-26 — sidebar labels and sidebar-derived
  routes are drifted surfaces following the 2026-10-12 unified-dashboard-
  navigation rollout, with the docs' nav strings lagging), and the login
  carries multiple accounts (observed 2026-10-26) — the runbook's
  prerequisites therefore include identifying the account whose zone carries
  `brothertown-language.com` and switching to it, because account selection
  determines both the visible navigation and the zone surfaces. The
  entry-step pages record the doc-dated strings as unverified-on-this-account
  and carry a discovery step: the executor identifies the Workers/applications
  section on their dashboard under the correct account, records the observed
  label with its date, and the observed label recorded with its date is the
  UI fact of record — the page then names it.
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
  `zola-v0.23.6-x86_64-unknown-linux-gnu.tar.gz`); wrangler 4.153.0 (npm
  `dist-tags.latest`); Workers Builds image Ubuntu 24.04 x86_64 with Node
  24.22.1 default and 22.23.4 also preinstalled (the build-image page's
  2026-10-26 state) — and SHALL record the
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
  The build-pipeline page SHALL document the complete cold-start creation
  sequence for a git-connected Worker with the current docs' exact nav
  strings (**Workers & Pages** page → **Create application** → **GitHub** →
  authenticate if prompted → select the repository → configure the project →
  **Save and Deploy** → preview at the `workers.dev` subdomain) AND the
  existing-Worker connect sequence (Worker → **Settings** → **Builds** →
  **Connect**), carrying the documented caution that the dashboard's Worker
  name must match the `name` in the Wrangler configuration file or the build
  fails. The runbook SHALL state that controlling the Zola version by pin +
  download is grounded in the current Workers Builds docs — not in sibling
  precedent.
- **R-7** — The runbook SHALL document the custom-domain attach for
  `brothertown-language.com` given the pre-provisioned state (domain
  registered; DNS zone on Cloudflare) as dashboard actions performed on the
  account carrying the domain's zone: Worker → Settings > Domains & Routes >
  Add > Custom Domain; automatic DNS-record creation on zones the account
  owns; the documented caution that a custom domain cannot be created on a
  hostname with an existing conflicting CNAME record or on a zone the account
  does not own; exact-hostname matching (the apex does not cover `www` and
  vice versa) with the redirect-rule pattern for the uncovered hostname; and
  workers.dev coexistence with its dashboard disable path (the Settings
  toggle).
- **R-8** — The runbook SHALL document HTTPS verification: Workers custom
  domains provision per-hostname Advanced Certificates (not Universal SSL
  certificates) with certificate issuance and DNS record creation handled
  automatically because Cloudflare is the authoritative DNS; current docs
  publish no issuance-time SLA, so timing verification is empirical. Gates:
  `curl -sv https://brothertown-language.com/` (shows the edge certificate
  and the Worker-served response) and a `dig` check of the auto-created
  record, with a retry decision point (re-run the probe until green or
  escalate).
- **R-9** — The runbook SHALL carry rollback awareness ahead of the first
  cloud-side write action: the overview page states that rollback and
  teardown are available and locates their executable detail, at a point in
  the read order that precedes every page carrying a dashboard-write step.
  The complete executable detail SHALL live on
  `Cloudflare-Workers-Setup-Rollback-Teardown`: instant rollback via
  Deployments → Rollback (bounded to the 100 most recently published
  versions; `wrangler versions upload` noted as the not-promoted variant
  feeding the promotion-policy decision point); teardown sequence: disconnect
  the build integration → remove the custom domain → inspect zone DNS records
  and delete any record left behind (documented auto-cleanup behavior absent
  — verify on detach) → manually remove the leftover Advanced Certificate
  under SSL/TLS > Edge Certificates (documented caution: the certificate is
  not auto-deleted) → delete the Worker → verify via curl that the domain no
  longer serves. All steps are dashboard actions on the account carrying the
  zone; the agents' verification probes (curl) stay agent-executed.
- **R-10** — The runbook SHALL mark every step's executor: cloud/dashboard
  steps are developer-run; agent-runnable gates (curl, dig, local build
  reproduction) named as such. The agent executes no Cloudflare-side
  operation without explicit instruction.
- **R-11** — The runbook SHALL state each configuration choice as an explicit
  decision point — condition → branch with the deciding evidence — and SHALL
  NOT use open "adjust as appropriate" language anywhere.
- **R-12** — Wiki edits of the runbook follow the deck's wiki-operations
  card, whoever performs them: the `wiki/` checkout is pulled and reconciled
  against the remote tip before any page is touched; every publish is
  preceded by a diff review plus the card's publish checks — `[[...]]`
  targets resolve to real pages, `_Sidebar.md` and `_Footer.md` are updated
  or intentionally untouched, no YAML frontmatter, and no secrets,
  credentials, account identifiers, or PII in any published page; commits
  push immediately after editing; the wiki is never force-pushed, and remote
  edits (human web-UI edits are likely) are integrated, never discarded
  wholesale.

## Success criteria

| ID | Criterion | Class | Instrument |
|----|-----------|-------|-----------|
| SC-1 | The runbook page set exists in the repository wiki exactly as R-1 names it: `_Sidebar.md`, `Home.md`, and the five pages `Cloudflare-Workers-Setup-Overview`, `Cloudflare-Workers-Setup-Build-Pipeline`, `Cloudflare-Workers-Setup-Domain-HTTPS`, `Cloudflare-Workers-Setup-Rollback-Teardown`, `Cloudflare-Runbook-Facts-Log`, operated through the `wiki/` gitignored sub-repo checkout (never a submodule) | structural | in the `wiki/` checkout, `git ls-files` lists `Home.md`, `_Sidebar.md`, and the five page files; the repository's `.gitignore` matches `wiki/`; no wiki entry exists in `.gitmodules` |
| SC-2 | Prerequisites + blast radius precede the first cloud-side write step — in the page set's read order (`_Sidebar.md`) — and enumerate: the Cloudflare-account prerequisite, the domain/zone already-on-Cloudflare fact, repo-side prerequisites (wrangler.jsonc, build entry, `ZOLA_VERSION`, built `public/`), the agent/developer executor split, and rollback and teardown availability | structural | read-order audit: in the `_Sidebar.md` order, the overview page carrying prerequisites + blast radius precedes every later page carrying a dashboard-write step; assert the overview page carries each enumerated item |
| SC-3 | Every operative platform fact carries an inline primary-source URL plus verification date; the facts-log page and the re-verify-before-edit maintenance rule are present | structural | fact-by-fact citation audit over the whole page set |
| SC-4 | The platform-selection record cites the dated Workers recommendation (quote + URL) and labels every superseded Pages-era/sibling mechanic as historical context | structural | audit the selection record for the dated quote; check every sibling/Pages-era reference for its historical-context label |
| SC-5 | The `wrangler.jsonc` section shows the assets-only shape — `name`, `compatibility_date`, `assets.directory "./public"`, `not_found_handling "404-page"`, no script/binding — matching the cited configuration reference | structural | field-by-field comparison against the cited reference (2026-10-20) |
| SC-6 | Version facts recorded with dates (Zola 0.23.6 / 2026-09-12 + asset name; wrangler 4.153.0; Node 24.22.1 default / 22.23.4 preinstalled; image Ubuntu 24.04 x86_64) plus the refresh procedure naming its sources | structural | cross-check each value and date against the cited sources; assert the procedure names npm `dist-tags`, the GitHub releases API, and the build-image page |
| SC-7 | Build-pipeline facts: Zola not preinstalled and no override hook; pinned-download build entry grounded in current docs; deploy command `npx wrangler deploy`; production branch `main`; preview deployments with PR-comment URLs and `noindex`; the complete cold-start creation sequence AND the existing-Worker connect sequence with the current pages' exact nav strings, plus the Worker-name-match caution | structural | fact-by-fact audit against the cited build-image, configuration, and Previews pages; step-by-step comparison of the creation/connect/disconnect sequences against the cited Builds page (2026-10-15); assert the navigation steps carry the cited pages' deep links and the recorded UI fact |
| SC-8 | Domain attach: flow path; automatic DNS-record creation; conflicting-CNAME caution; exact-hostname apex/www split with the redirect-rule pattern; workers.dev coexistence plus both disable paths | structural | enumerated-item audit against the cited domain pages |
| SC-9 | HTTPS: Advanced-Certificate model (not Universal SSL; no ACM subscription); automatic DCV; no-published-SLA noted as empirical; `curl -sv` and `dig` gates with stated expected outputs and a retry decision point | structural | enumerated-item audit; assert the gate commands appear with expected outputs |
| SC-10 | Rollback awareness precedes the first cloud-side write step in the read order (the overview page states rollback and teardown availability and locates the executable detail), and the complete executable detail is on `Cloudflare-Workers-Setup-Rollback-Teardown`: rollback mechanism, 100-version limit, deploy-vs-versions-upload promotion note, and the teardown sequence (disconnect builds → detach domain → DNS-record check → manual certificate removal under SSL/TLS > Edge Certificates → delete Worker → verify down) | structural | read-order audit: the overview page's rollback/teardown availability statement precedes every later page carrying a dashboard-write step in the `_Sidebar.md` order; plus enumerated-item audit of the Rollback-Teardown page |
| SC-11 | Every configuration choice is condition → branch with deciding evidence; zero "adjust as appropriate" phrasing | structural | audit the named choices (production branch, build command, workers.dev disable, www policy, promotion policy) plus a full-text sweep for open-ended instruction |
| SC-12 | Every step carries its executor mark (developer-run vs agent-runnable) | structural | step-by-step marking audit |
| SC-13 | The agent-runnable gates run exactly as written and produce the runbook's stated expected outputs | behavioral | execute the gates at the runbook's stated checkpoint (prerequisites in force: issue-#1 artifacts deployed, domain attached); assert outputs match |
| SC-14 | Navigation integrity: `_Sidebar.md` links every runbook page in the R-1 read order; `Home.md` indexes them; every `[[...]]` target in the page set resolves to an existing page | structural | link sweep over the checkout: enumerate the `[[...]]` targets in all pages including `_Sidebar.md` and `Home.md`; assert each resolves to an existing page file; assert `_Sidebar.md` and `Home.md` enumerate exactly the five runbook pages in the R-1 order |
| SC-15 | Single record: the repository tracks no in-repo copy of the runbook | structural | content-overlap sweep: for each of the five wiki pages, take distinctive verbatim strings (section headings, step lines, decision-point branches) and `git grep -F` the main repository's tracked files for them — any hit is a violation; plus a name sweep: no tracked file matches `*runbook*` (case-insensitive) |
| SC-16 | Page hygiene: no page carries a YAML frontmatter block, and no page carries secrets, credentials, account identifiers, or PII | structural | per-page content sweep: assert no leading bare `---` frontmatter block on any page; apply the repository's sensitivity/PII audit rule (AGENTS.md content rules) to each page |
| SC-17 | Per-phase self-containedness: each page carries the complete step set for the operational phase R-1 assigns it, and a phase's steps never send the executor to another runbook page mid-phase to continue the procedure | structural | page-by-page walkthrough: for each page, walk its steps top-to-bottom against the phase scope R-1 assigns; failure = a required phase step present only on another page, or a mid-phase link to another runbook page that is part of the step sequence |
| SC-18 | The runbook page set is published: the wiki remote's default-branch tip (origin/HEAD after a fetch) carries the page set, and the `wiki/` checkout holds no unpushed state | structural | after the final runbook push: `git -C wiki fetch origin`; `git ls-tree -r --name-only` of the remote default-branch tip lists `Home.md`, `_Sidebar.md`, and the five runbook pages; `git -C wiki status --porcelain` is empty; `git -C wiki rev-list --count origin/HEAD..HEAD` is 0 |

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
(prerequisites → procedure → verification → rollback) arranged as the wiki
page set of R-1 — `_Sidebar.md` navigation, `Home.md` entry, one page per
operational phase — with decision points explicit, executor marks per step,
and the facts log on its own page carrying source + date per fact. Wiki
operations follow the deck's wiki-operations card (verified present in this
repo's deck copy 2026-10-26: `.opencode/skills/wiki-operations/` with its
provisioning, layout-and-syntax, and publish-discipline references —
checkout at `wiki/` as a gitignored sub-repo, verify-before-push publishing
because a wiki push is direct-publish, `[[...]]` link syntax, no
frontmatter). The pinned-Zola build entry is grounded in the current Workers
Builds docs (Zola absent from the image; arbitrary build commands supported;
no Zola override hook exists) — the same shape the sibling used, arrived at
independently under current docs rather than by cargo cult.

## Dependencies

- Runbook authoring requires no issue-#1 artifacts; the page set lands
  independently in the wiki. The only repo-side footprint this issue's
  implementation carries is the `wiki/` gitignore entry the checkout
  provisioning requires (installed before the clone, per the
  wiki-operations card).
- The runbook's execution gates require issue #1's revised deployment
  artifacts to exist and the domain attach to have happened (SC-13's stated
  checkpoint).
- Issue #1's SOP delegates to this runbook's wiki page set (its spec revised
  2026-10-26), so the page set lands before (or with) that SOP.
- Ordering note for the developer: issue #1's implementation should not start
  until its spec's platform revision (Pages → Workers Static Assets, per
  these same directives) is decided — otherwise issue #1 lands Pages-shaped
  artifacts this runbook then disavows. (Decided: issue #1's spec carries the
  Workers basis as of 2026-10-26.)

## Facts of record (verified 2026-10-26)

| Fact | Source (URL) | Date on page / fetch | Confidence |
|------|-------------|----------------------|------------|
| "Start new projects with Workers" interstitial on the Pages docs; Pages creation flows still documented | developers.cloudflare.com/pages/ | 2026-08-25 | high |
| Migration guide voluntary, no sunset deadline | developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/ | 2026-10-12 | high |
| Assets-only static config shape; assets served without Worker code; `not_found_handling "404-page"` | developers.cloudflare.com/workers/static-assets/ | 2026-10-12 | high |
| Workers Builds: navigation, arbitrary build command, deploy command default `npx wrangler deploy`, preview behavior; PR-comment posting of Preview URLs | developers.cloudflare.com/workers/ci-cd/builds/ ; …/builds/configuration/ | 2026-10-15 / 2026-09-22 | high |
| Previews (branch-oriented, distinct from Version URLs): workers.dev-form Preview URL carries an `X-Robots-Tag: noindex` response header; custom-domain Preview URLs protected instead via Cloudflare Access | developers.cloudflare.com/workers/previews/ | 2026-09-24 | high |
| Builds' connect flows: new Worker — **Workers & Pages** page → **Create application** → **GitHub** → (authenticate) → select repository → configure project → **Save and Deploy** → preview at `workers.dev`; existing Worker — **Settings** → **Builds** → **Connect**; disconnect — same path → **Disconnect**; CAUTION: dashboard Worker name must match the Wrangler config `name` or the build fails; autoconfig opens a PR for repos lacking a Wrangler config | developers.cloudflare.com/workers/ci-cd/builds/ | 2026-10-15 | high |
| Git-integration management: Worker → **Settings > Builds** → **Git Repository** → **Manage**; the GitHub App is named "Cloudflare Workers & Pages", shared between Workers and Pages; PR comments + check runs monitor builds | developers.cloudflare.com/workers/ci-cd/builds/git-integration/ (+ …/github-integration/) | 2026-10-01 / 2026-10-15 | high |
| Dashboard Workers-creation walkthrough (same flow as the Builds page's connect-a-new-Worker steps) | developers.cloudflare.com/workers/get-started/dashboard/ | 2026-06-25 | high |
| Static-site deployment without git-builds: C3 CLI (`npm create cloudflare@latest`, "Static site" template) then `npx wrangler deploy`; CI users set the "deploy command" in build settings | developers.cloudflare.com/workers/static-assets/get-started/ | 2026-08-25 | high |
| UI fact of record (2026-10-26, developer observations): the login carries MULTIPLE accounts; the dashboard shows NO "Workers & Pages" sidebar option; the docs' deep link (`dash.cloudflare.com/?to=/:account/workers-and-pages`) does not work — the combined dashboard navigation rolled 2026-10-12 ("Unified dashboard navigation", all customers) and the docs' nav strings date before it. Runbook steps therefore carry the doc-dated strings as unverified labels plus the discovery step: the executor picks the account whose zone carries the domain, identifies the Workers/applications section, and the observed label recorded with its date is the UI fact of record (each page names it once known) | developer observations ×3 (dashboard, 2026-10-26) · developers.cloudflare.com/changelog/post/2026-10-12-unified-dashboard-navigation/ · docs pages still routing via workers-and-pages (wholesale doc lag: builds, get-started/dashboard, custom-domains) | 2026-10-26 | high |
| Build image Ubuntu 24.04 x86_64; Node 24.22.1 default, 22.23.4 preinstalled; Zola NOT preinstalled; curl/wget/unzip/zstd present; update policy | developers.cloudflare.com/workers/ci-cd/builds/build-image/ | 2026-10-26 | high |
| Status page of record: cloudflarestatus.com APIs; anomaly observed 2026-10-26 ("Partial System Outage" across regions + zero open incidents + page metadata frozen at 2026-08-27) recorded as its own fact; today's relevant resolved incidents: Workers build delays (15:12–16:03 UTC) + Workers Cron Triggers delays/duplication (resolved 2026-10-27T01:15 UTC) | www.cloudflarestatus.com/api/v2/summary.json ; /incidents.json | 2026-10-26 | high |
| Builds limits: free 3,000 min/mo, 1 concurrent, 20-min timeout | developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/ | 2026-05-29 | high |
| Wrangler configuration reference (new URL); mandatory `name` + `compatibility_date`; asset fields incl. `html_handling`, `not_found_handling`, `.assetsignore` | developers.cloudflare.com/workers/wrangler/configuration/ | 2026-10-20 | high |
| wrangler latest stable 4.153.0 | registry.npmjs.org/wrangler/latest | fetched 2026-10-26 | high |
| Custom domains: flow, automatic DNS creation on owned zones, conflicting-CNAME caution, apex supported, exact-hostname matching, Advanced Certificate per hostname (not Universal SSL), cert-not-auto-deleted caution | developers.cloudflare.com/workers/configuration/routing/custom-domains/ | 2026-09-29 | high |
| workers.dev default-on; disable paths | developers.cloudflare.com/workers/configuration/routing/workers-dev/ | 2026-09-22 | high |
| Static-assets limits: 20,000 files/version (free), 25 MiB/file, requests to assets free and unlimited | developers.cloudflare.com/workers/platform/limits/ ; …/static-assets/billing-and-limitations/ | 2026-10-12 / fetched 2026-10-26 | high |
| Instant rollback (Deployments → Rollback; each rollback becomes the new active deployment); 100-most-recent-versions bound; `wrangler versions upload` not auto-promoted | developers.cloudflare.com/workers/configuration/versions-and-deployments/rollbacks/ ; …/versions-and-deployments/ | 2026-07-15 / 2026-09-22 | high |
| Zola latest stable v0.23.6, published 2026-09-12, asset name for x86_64 glibc | api.github.com/repos/getzola/zola/releases/latest | fetched 2026-10-26 | high |
| Universal SSL context (apex + first-level subdomains only) supporting the Advanced-Certificate comparison | developers.cloudflare.com/ssl/edge-certificates/universal-ssl/ | 2026-08-14 | high |
| GitHub Actions alternative: `cloudflare/wrangler-action@v4`, scoped API token | developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/ | 2026-10-18 | high |
| No official Zola guide exists on Workers framework-guides (index fetched; `/workers/framework-guides/zola/` 404) | developers.cloudflare.com/workers/framework-guides/ | fetched 2026-10-26 | high |
| Wiki enabled on the repository (`has_wiki: true`; `private: false`); wiki remote `Brothertown-Language/brothertown-language-com.wiki.git` reachable (HEAD present) | api.github.com/repos/Brothertown-Language/brothertown-language-com (gh api) ; git ls-remote of the wiki remote | fetched 2026-10-26 | high |
| A public repository's wiki is available to the public; by default only people with write access to the repository can edit it (open public-repo contributing is off unless enabled); wikis have a soft limit of 5,000 total files | docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis | fetched 2026-10-26 | high |
| Wiki mechanics of record: `Home`/`_Sidebar`/`_Footer` layout files, `[[Page Name]]` internal links, bare `---` frontmatter renders as a rule on GitHub, flat-vs-hierarchical layout patterns, publish-discipline checks (direct-publish, verify before push), provisioning ladder (gitignored sub-repo, never a submodule) | deck copy: `.opencode/skills/wiki-operations/` (+ its references/), verified present 2026-10-26 | verified 2026-10-26 | high |

Documented gaps carried into the runbook, not papered over: (1) DNS-record
auto-cleanup on custom-domain detach / Worker delete is undocumented — the
runbook verifies record state on detach and deletes leftovers manually; (2)
no published issuance-time SLA for the Advanced Certificate — the runbook
verifies empirically with a retry decision point; (3) no published total
asset-size cap or bandwidth cap on the current limits pages; (4) the Workers
Builds limits page is the oldest fetched page (2026-05-29) — the runbook
date-stamps it and the facts log flags it as the oldest in the set.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
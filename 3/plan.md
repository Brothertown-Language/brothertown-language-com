# Plan — implement issue brothertown-language-com#3 (Cloudflare Workers setup runbook)

Plan from the validated spec (`.issues/3/spec.md`, fresh-context PASS 2026-10-26,
zero findings). Deliverable: the tracked runbook document
`docs/runbook-cloudflare-workers-setup.md` — a developer-executable cloud-side
setup+operation record with agent-runnable verification gates.

## Items (RED → GREEN → verification, dependency-ordered)

- **I-1 — SC-1.** Deliverable: create `docs/runbook-cloudflare-workers-setup.md`
  on the feature branch with the full front matter and the section skeleton in
  the canonical order: (1) Prerequisites & blast radius; (2) Rollback & teardown;
  (3) Platform of record; (4) Facts log; (5) Deployment unit & repo
  prerequisites; (6) Build pipeline, setup procedure & version currency;
  (7) Custom-domain attach; (8) HTTPS verification. RED: `git ls-files docs/`
  lists no runbook path and the file does not exist. GREEN: write the skeleton
  with section order as above and SPDX header. Verification: `git ls-files docs/`
  lists the path; the file's headings match the eight-section skeleton in order.
  Ordering note: sections 2–8 hold the doc's final content; no cloud-side write
  procedure text appears before section 2 (rollback/teardown) — SC-10's
  placement is satisfied by the skeleton's order and audited in I-11.
- **I-2 — SC-2.** Deliverable: Prerequisites & blast radius section. RED: the
  section is absent/stub — the enumerated audit fails. GREEN: author it carrying:
  the Cloudflare-account prerequisite; the domain/zone already-on-Cloudflare
  fact (dig 2026-10-25; developer statement 2026-10-26); repo-side
  prerequisites (wrangler.jsonc per section 5, build entry+`ZOLA_VERSION`,
  built `public/` — issue-#1 deliverables, with the landing-order dependency);
  the agent/developer executor split; rollback availability statement. All
  operative facts carry inline source URL + verification date. Verification:
  enumerated-content audit — every listed item present, section positioned
  before all procedure sections.
- **I-3 — SC-10.** Deliverable: Rollback & teardown section (position: directly
  after prerequisites, before every write-procedure section). RED: stub — the
  enumerated audit fails. GREEN: author: instant rollback (Deployments →
  Rollback, bounded to the 100 most recently published versions, deploy vs
  `wrangler versions upload` promotion note feeding the promotion-policy
  decision point); teardown sequence: disconnect Workers Builds → detach custom
  domain → inspect zone DNS and delete any record left behind (documented
  auto-cleanup behavior absent — verify on detach) → manually remove the
  Advanced Certificate under SSL/TLS > Edge Certificates (documented caution:
  the certificate is not auto-deleted) → delete the Worker → verify via curl
  that the domain no longer serves. Verification: enumerated-item audit + the
  doc-order audit (rollback before every cloud-side write step).
- **I-4 — SC-3.** Deliverable: Facts log section + the maintenance rule.
  RED: absent. GREEN: author the log (each operative platform fact → source
  row: fact / source URL / date on page or fetch date / confidence) carrying
  the spec's facts-of-record table content, plus the maintenance rule: a
  dashboard step that no longer matches the runbook is re-verified against the
  cited docs before the runbook is edited — never from memory or cached pages.
  Verification: log present with per-fact rows; the rule present near the log.
- **I-5 — SC-4.** Deliverable: Platform of record section. RED: absent.
  GREEN: author: the dated "Start new projects with Workers" interstitial quote
  (developers.cloudflare.com/pages/, 2026-08-25) and the voluntary deadline-free
  migration note (2026-10-12); the adopted-mechanism list, each grounded in its
  current Workers-docs citation; the superseded sibling/Pages-era mechanics
  (`CLOUDFLARE_UPDATE.md`, Pages v3 pattern, Zulma era) labeled historical
  context only. Verification: audit — dated quote present; every adopted
  mechanism has a citation; every historical reference labeled.
- **I-6 — SC-5.** Deliverable: Deployment unit & repo prerequisites section.
  RED: absent. GREEN: author: the assets-only `wrangler.jsonc` shape
  field-by-field per the cited configuration reference
  (developers.cloudflare.com/workers/wrangler/configuration/, 2026-10-20) —
  `name`, `compatibility_date` set to the authoring date per docs,
  `assets.directory "./public"`, `not_found_handling "404-page"`, no script, no
  binding; JSONC example block; the consumed repo-side artifacts named as
  prerequisites. Verification: field-by-field comparison of the doc's config
  block against the cited reference's documented fields.
- **I-7 — SC-6.** Deliverable: version-currency facts + refresh procedure
  (within the build-pipeline section). RED: absent. GREEN: author: Zola latest
  stable v0.23.6 (2026-09-12; asset name), wrangler 4.152.0 (npm
  `dist-tags.latest`, fetched 2026-10-26), Workers Builds image Ubuntu 24.04
  x86_64 with Node 24.21.0 default / 22.23.2 preinstalled (build-image page,
  2026-10-24); the refresh procedure: re-verify npm `dist-tags`, the GitHub
  releases API, and the build-image page at each tooling touch, then update
  `ZOLA_VERSION`/`wrangler.jsonc compatibility_date` through the normal PR
  flow. Verification: cross-check each value+date against its cited source.
- **I-8 — SC-7.** Deliverable: Build pipeline & setup procedure section (the
  doc's first cloud-side write content). RED: the build-pipeline content of
  section 6 is absent (version-currency content may already be there per
  I-7 — the assertion targets exactly this item's content). GREEN: author:
  the Zola
  facts (not preinstalled on the image — zero occurrences on the build-image
  page; no version-override hook — absent from the per-language override table;
  arbitrary build commands run, curl/wget/unzip/zstd preinstalled), the tracked
  pinned-download build entry consuming `ZOLA_VERSION` (grounded in current
  docs, not sibling precedent, per the 2026-10-26 directives); the Workers
  Builds git-connection procedure (Workers & Pages → Create application →
  GitHub → repo selection → configure; production branch `main`; build command;
  deploy command default `npx wrangler deploy`); preview behavior on
  non-production branches (PR-comment preview URLs, `noindex`); the
  GH-Actions-alternative decision point (scoped "Edit Cloudflare Workers" API
  token, wrangler-action@v4). Every step carries its executor mark. All facts
  cited (builds/configuration pages 2026-10-15/2026-09-22; build-image
  2026-10-24). Verification: fact-by-fact audit against the cited pages; each
  step's executor mark present.
- **I-9 — SC-8.** Deliverable: Custom-domain attach section. RED: absent.
  GREEN: author: the flow (Worker → Settings > Domains & Routes > Add >
  Custom Domain); automatic DNS-record creation on owned zones; the
  conflicting-CNAME and unowned-zone caution; exact-hostname splitting — apex
  does not cover `www` — with the redirect-rule pattern for the uncovered
  hostname (decision point: serve both vs redirect); workers.dev coexistence
  with both disable paths (Settings toggle or `"workers_dev": false`) —
  decision point; `curl -sv`/`dig` record-existence gate cited. Verification:
  enumerated-item audit against custom-domains/workers-dev pages
  (2026-09-29/2026-09-22).
- **I-10 — SC-9.** Deliverable: HTTPS verification section. RED: absent.
  GREEN: author: the per-hostname Advanced-Certificate model (not Universal
  SSL, no ACM subscription; custom-domains page 2026-09-29; Universal SSL page
  2026-08-14 for the comparison); automatic DCV via authoritative DNS; no
  published issuance SLA — timing verified empirically; gates:
  `curl -sv https://brothertown-language.com/` (expected: edge certificate
  displayed + Worker-served HTTP response) and the `dig` record check; retry
  decision point (re-run until green or escalate). Verification: enumerated-item
  audit; gate commands present with stated expected outputs.
- **I-11 — SC-11 + SC-12.** Deliverable: final full-document audit pass.
  RED: the audit instruments fail (some decision without a branch, or a step
  without an executor mark, or an open-ended phrase). GREEN: fix the audit's
  findings in the doc. Verification: (a) SC-11's audit — the named choices
  (production branch, build command, workers.dev disable, www policy,
  promotion policy, GH Actions alternative) each hold condition→branch with
  evidence; full-text sweep finds no "adjust as appropriate"-class language;
  (b) SC-12's step-by-step audit — every step carries executor marks; (c)
  SC-3's citation sweep — every operative fact carries its inline source URL +
  verification date.
- **I-12 — SC-13.** Deferred-with-checkpoint execution item. The behavioral
  instrument fires at the checkpoint the spec states (prerequisites in force:
  issue-#1 artifacts deployed, domain attached). RED at checkpoint: execute the
  runbook's agent-runnable gates exactly as written; any output mismatching the
  documented expectation fails. GREEN: outputs match (criterion passes) — or,
  where a stated expectation proved wrong in reality, the maintenance rule
  corrects the runbook's expected-output text (with dated source) and the gate
  re-runs. Verification: the executed-gate outputs recorded as evidence. This
  item cannot run before the checkpoint; its execution and evidence belong to
  the deployment session, and the PR records the deferral.

## Dependencies

- The feature branch precedes every item (I-1 creates its first tracked file).
- Item order is the executed order: I-1 skeleton → I-2/I-3 (order-defining,
  position-stable sections) → I-4..I-10 (content) → I-11 audit → branch
  commit → PR. I-11 depends on all content items; no cycles.
- Repo-side prerequisite artifacts (`wrangler.jsonc`, build entry,
  `ZOLA_VERSION`, built `public/`) are NOT needed to author the runbook
  document; they gate only I-12's checkpoint execution.
- Landing order (spec Dependencies): this runbook lands before or with
  issue-#1's SOP.

## Traceability

| Item | Spec criterion |
|------|----------------|
| I-1 | SC-1 |
| I-2 | SC-2 |
| I-3 | SC-10 |
| I-4 | SC-3 |
| I-5 | SC-4 |
| I-6 | SC-5 |
| I-7 | SC-6 |
| I-8 | SC-7 |
| I-9 | SC-8 |
| I-10 | SC-9 |
| I-11 | SC-11, SC-12 |
| I-12 | SC-13 |

All 13 SCs covered; no item without a criterion; no criterion without an item.

## Documentation Sources

- The spec's facts-of-record table (`.issues/3/spec.md`) — every operative
  fact with source URL, page date, and confidence; the runbook's facts log
  (I-4) inherits these rows verbatim and the authoring items cite them inline.
- Primary pages cited: workers/static-assets, workers/ci-cd/builds (+ 
  configuration, build-image, limits-and-pricing), workers/wrangler/
  configuration, workers/configuration/routing/custom-domains,
  workers/configuration/routing/workers-dev, workers/configuration/
  versions-and-deployments/rollbacks, workers/platform/limits,
  workers/ci-cd/external-cicd/github-actions, pages/ (interstitial),
  ssl/edge-certificates/universal-ssl, getzola releases API, npm wrangler
  registry. All fetched 2026-10-26 with page-dates stated.

## Enforcement Gate

- The authoring items' verification instruments are the runbook's own SC
  audits (structural, agent-run in-repo) — run per item, recorded as evidence.
- The feature branch commit precedes I-11's final audit; hooks run per commit.
- The fresh-context verify dispatch reads the diff and the executed
  instruments' outputs; SC-13's deferral is disclosed, not silently dropped.

## Cost Frame

Single tracked doc; ~10 authoring/audit steps; one feature branch; one PR.
No runtime code, no dependency changes, no CI changes (the repo has none
beyond hooks).

## Edge Cases

- Facts drift: every fact carries its date; the maintenance rule routes any
  future mismatch through re-verification, not memory (I-4).
- `index_format`-paired artifacts: the runbook documents the elasticlunr_json
  pairing exactly (issue-#1's pin); the facts log notes the format/artifact
  dependency so a future format change re-triggers verification
  (search_index.en.json + elasticlunr.min.js).
- The `dig`/`curl` gates fail pre-deployment: the runbook marks them
  post-setup gates (executor split; I-12's checkpoint), not setup blockers.
- Cloudflare dashboard path drift (the fact-decay trap): the platform-of-
  record + facts-log sections state the exact nav strings with dates and the
  re-verify rule (I-4/I-5).

## Not Included

- Any execution of the dashboard steps (developer-executed per R-10).
- The in-repo deployment artifacts themselves (issue #1's deliverables).
- Cloudflare Access preview lockdown or build-caching optimization (spec
  out-of-scope).
- CI/CD changes — the runbook is a document; no pipeline edits ride with it.
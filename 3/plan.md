# Plan — implement issue brothertown-language-com#3 (Cloudflare Workers setup runbook, wiki page set) — remainder

Plan from the validated spec (`.issues/3/spec.md`, revised 2026-10-26 to the
wiki-page-set deliverable, R-1..R-12 / SC-1..SC-18). State consumed at
planning: the `wiki/` gitignored checkout is provisioned at the published
remote tip (`9722a9b`; `.gitignore wiki/` landed as `1eef425` on
`main`'s successor branch), and the seven pages exist in first-draft form.
This plan governs the REMAINDER: audit the page set against every criterion,
remediate the named gaps, publish each change under the wiki-operations card,
and close with the published-state instrument. It supersedes the earlier
docs-file plan record (which traced to the superseded pre-revision spec).

## Items (RED → GREEN → verification, dependency-ordered)

Wiki-operation wrapper for every item: sync the checkout and reconcile against
the remote tip before editing (`git -C wiki pull/fetch`), then edit, diff
review, run the publish-discipline checks, commit, push immediately (per the
wiki-operations card — direct-publish, verify before push).

- **P-1 — SC-14 + SC-1.** Deliverable: page-set and navigation integrity
  audit. RED: the sweeps fail — unresolved `[[...]]` targets, or `_Sidebar.md`/
  `Home.md` not enumerating exactly the five runbook pages in the R-1 read
  order, or `git -C wiki ls-files` missing an R-1 page, or the main repo
  lacking the `wiki/` gitignore entry / carrying a `.gitmodules` wiki entry.
  GREEN: fix whatever the sweeps name (expected: current state passes; fix
  only real failures). Verification: link sweep over all seven pages;
  `git -C wiki ls-files` vs the R-1 page set; main-repo `.gitignore` matches
  `wiki/`; `.gitmodules` absent.
- **P-2 — SC-7.** Deliverable: Build-Pipeline page remediation for the missing
  operative facts. RED: SC-7's fact-by-fact audit fails — the page carries
  Zola-not-preinstalled but not the no-version-override-hook fact, and carries
  no preview-deployment behavior (PR-comment preview URLs, `noindex`). GREEN:
  author, in the build-pipeline steps: the build image offers no Zola
  version-override hook (so the pinned-download entry is the only version-
  control mechanism — current-docs ground, per the build-image page); a
  step/post-step noting non-production-branch builds produce preview
  deployments whose URLs post as PR comments and carry `X-Robots-Tag: noindex`
  (grounded: builds/configuration 2026-09-22; Previews page 2026-09-24 —
  dates per the facts log). Verification: re-run SC-7's audit.
- **P-3 — SC-8.** Deliverable: Domain-HTTPS page remediation for the
  conflicting-CNAME caution. RED: SC-8's enumerated audit fails — the caution
  (a custom domain cannot be created on a hostname with an existing
  conflicting CNAME record or on a zone the account does not own) is absent.
  GREEN: author it as a pre-step check under the domain-attach steps, with its
  custom-domains-page ground. Verification: re-run SC-8's audit.
- **P-4 — SC-10 + SC-11.** Deliverable: Rollback-Teardown page remediation for
  the promotion-policy decision point. RED: SC-10's enumerated audit fails —
  `wrangler versions upload` (the deploy-without-promote variant feeding the
  promotion-policy decision) is nowhere on the page. GREEN: author under
  Rollback: deploy (`wrangler deploy`) promotes 100% immediately vs
  `wrangler versions upload` saving a version without promoting — the
  promotion-policy choice, condition → branch, with the rollbacks-page ground.
  Verification: re-run SC-10's enumerated audit + SC-11's decision-point audit
  for this choice.
- **P-5 — SC-9.** Deliverable: Domain-HTTPS HTTPS-section truth-up. RED:
  SC-9's audit fails on three grounds — "issuance takes a few minutes" is an
  unsourced timing claim (current docs publish no issuance-time SLA); the
  automatic-DCV mechanism (authoritative DNS) is unstated; and the
  no-ACM-subscription fact is absent ("no separate Advanced Certificate
  Manager subscription is required" — the custom-domains page, 2026-09-29,
  the spec's own fact row). GREEN: re-word to the documented state: per-hostname
  Advanced Certificates (not Universal SSL; no ACM subscription required) and
  DNS records are issued/created automatically because Cloudflare is the
  authoritative DNS; no issuance-time SLA is published, so the gate outcome
  decides empirically — re-run the probe, retry decision point until green or
  escalate. Verification: re-run SC-9's audit (claims match the cited pages;
  no unsourced timing; the no-ACM fact present).
- **P-6 — SC-3 + SC-4.** Deliverable: Facts-Log page completion. RED: the
  page-set fact-by-fact audit fails — rows missing for the operative facts the
  pages now carry (no Zola override hook; preview deployments / noindex), plus
  the two facts-of-record rows absent from the page: the GH-Actions-alternative
  fact (`cloudflare/wrangler-action@v4` + scoped API token — spec
  facts-of-record row, page 2026-10-18) and the builds-limits row (free 3,000
  min/mo, 1 concurrent, 20-min timeout — page 2026-05-29). GREEN: add the rows
  with source URL + verification date each; and flag the builds-limits page as
  the oldest page in the set (the spec's documented-gaps note (4) states that
  disposition). Verification: row-set audit — every named row is present on
  the page (asserted against this item's own RED demands, not just the spec
  table), dated, with the oldest-page flag present; SC-4's historical-label
  spot-audit on the overview page still holds.
- **P-7 — SC-2 + SC-5 + SC-6 + SC-11 + SC-12 + SC-15 + SC-16 + SC-17.**
  Deliverable: final full-suite audit pass over the remediated page set. RED: any instrument fails: SC-2 read-order + enumerated
  prereq items; SC-5 field-by-field wrangler shape; SC-6 version facts + the
  refresh procedure naming npm `dist-tags`, the GitHub releases API, and the
  build-image page; SC-11 named-choice branches + zero open-ended language;
  SC-12 step-by-step executor marks; SC-15 single-record sweeps (distinctive
  verbatim strings + `git grep -F` in tracked files + no `*runbook*` tracked
  file); SC-16 no frontmatter/no secrets or account identifiers or PII per
  page; SC-17 per-phase self-containedness walkthrough. GREEN: fix the named
  findings in the pages. Verification: all listed instruments re-run clean.
- **P-8 — SC-18.** Deliverable: published-state instrument. RED: after the
  final push, `git -C wiki fetch origin` + `git ls-tree -r --name-only` of the
  remote tip missing a page, or `git -C wiki status --porcelain` non-empty, or
  `git -C wiki rev-list --count origin/HEAD..HEAD` ≠ 0. GREEN: none needed if
  clean; re-push if the fetch shows divergence. Verification: the SC-18
  instrument run complete with outputs as evidence.

## Deferred

- **SC-13** — behavioral; instruments at its stated checkpoint (issue-#1
  artifacts deployed, domain attached). Unfireable today; disclosed, not
  silently dropped. Its execution belongs to the deployment session.

## Dependencies

- The wiki checkout is already provisioned and published (at `9722a9b`) —
  items start from a synced checkout.
- Item order: P-1 audit first (navigation must be sound before content edits),
  P-2..P-6 content remediations (page-level independent, executed in listed
  order), P-7 full-suite audit, P-8 published-state close. Each content item
  carries its own wiki commit(s) + push (wiki-operations card). No cycles.
- Main-repo side: the `wiki/` gitignore commit (`1eef425`) already exists on
  the feature branch; the branch's PR delivery is a separate stage boundary —
  not a plan item.

## Traceability

| Item | Spec criteria |
|------|----------------|
| P-1 | SC-1, SC-14 |
| P-2 | SC-7 |
| P-3 | SC-8 |
| P-4 | SC-10, SC-11 |
| P-5 | SC-9 |
| P-6 | SC-3, SC-4 |
| P-7 | SC-2, SC-5, SC-6, SC-11, SC-12, SC-15, SC-16, SC-17 |
| P-8 | SC-18 |

All SC-1..SC-18 covered (SC-13 deferred with its checkpoint); no item without
a criterion.

## Documentation Sources

- The spec's facts-of-record table (`.issues/3/spec.md`, rows as revised
  2026-10-26 — including the Previews-page row 2026-09-24 and the GH-Actions
  row 2026-10-18).
- The deck wiki-operations card + its references (provisioning, layout-and-
  syntax, publish-discipline) — the wiki-operation wrapper for every item.
- Primary Workers/custom-domains/rollbacks/previews/builds pages as cited in
  the facts table (all dated 2026-10-26 verification of record).

## Enforcement Gate

- Every item's wiki edits follow verify-before-push: diff review + publish-
  discipline checks (`[[...]]` targets resolve; no frontmatter; no secrets/
  credentials/account identifiers/PII) before each push.
- Structural instruments are agent-run file/git checks; their outputs are the
  recorded evidence for the fresh-context verify dispatch.
- SC-13's deferral is disclosed to the PR/verification record, never silent.

## Cost Frame

Wiki-only remediation: ≤7 page edits across 4 pages + facts-log rows; each
item one small commit + push; one full-suite audit; one published-state
instrument run. No runtime code; the main-repo footprint stays the existing
`.gitignore wiki/` commit on the feature branch.

## Not Included

- Dashboard execution (developer-run per R-10).
- The in-repo deployment artifacts (issue #1's deliverables).
- SC-13 execution (checkpoint-gated — deferred above).
- Any CI/CD change; any expansion of the main-repo footprint beyond the
  existing gitignore commit.
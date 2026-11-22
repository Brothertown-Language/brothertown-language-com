# Plan — #32 Blog: client-side Mastodon thread-reply widget

Source of record: `.issues/32/spec.md` (SC-1 … SC-10, R-1 … R-10).

## Goal

Delivers brothertown-language-com#32's chosen form (item D of the
2026-11-21 design discussion): a client-side widget that shows each blog
entry's Mastodon thread replies beneath the `### Comment on Mastodon`
section, derived from the entry's existing `View on Mastodon` anchor and
fetched at view time, degrading silently to the exact current form on any
failure. Artifact surfaces: a new widget asset `static/js/mastodon_widget.js`,
a new site-level `templates/page.html` override, dated amendments to
`docs/sop-site-setup.md` and `AGENTS.md`; no content, theme, or build
machinery changes.

## Execution surface

The session's root repo (project_root from session-init), on the feature
branch off trunk tip `49f1f4db3350218783581a7f920158c9086abe58` (verified = `origin/main`
at branch time). Zola pinned `0.23.6` via `./zola`; builds via `./build.sh`
→ `public/` (gitignored). Behavioral probes run against a `./zola serve` of
the built `public/` tree via the playwright-cli card's vendored browser.
P2's RED/GREEN depend on the site-shadow-theme lookup and the pinned build;
P4's probes depend on the served `public/` state of the branch build.

## Container selector of record (SC-1 prerequisite)

The widget's rendered container is `<div id="mastodon-replies">` — the stable
selector all SC-1/SC-3 assertions scope to. The widget removes/recreates this
id's element on retry only within the same page view; no other element on the
page carries the id.

## Items (one per criterion; fields: Deliverable / RED / GREEN / Instrument / Tier)

### P1 — `static/js/mastodon_widget.js` (SC-6; SC-3 via probe in P4) **T-tier: structural fact-check at item time; behavioral arm deferred to P4's recorded probe run**

- **Deliverable:** vanilla-JS deferred script; IIFE, no dependencies.
  (1) locate the thread anchor — first `a[href]` matching
  `mastodon.social/@<handle>/<digits>` (status id = digits); none → silent
  return. (2) find the section whose `h3` text is `Comment on Mastodon` and
  insert `<div id="mastodon-replies">` after it. (3)
  `fetch('https://mastodon.social/api/v1/statuses/<id>/context')` with
  AbortController timeout 8 s; any non-200, abort, non-JSON, missing
  `descendants`, or thrown error → remove container, silent return (KD-3).
  (4) render each descendant using only DOM text APIs (`createElement` +
  `textContent`); reply HTML → text via
  `new DOMParser().parseFromString(html,'text/html')…textContent` (no script
  execution). Fields: display name, @handle, `created_at` date, body text.
- **RED:** asset absent → nothing to reference; SC-6's code check has no
  object to clear (repo-wide grep proves absence).
- **GREEN:** asset as above, committed on the branch.
- **Tier marks:** structural (SC-6 code check: fact-check tier, run at item
  time); behavioral degradation evidence is a separate recorded run (P4).
- **Instrument:** grep the asset for
  `innerHTML|insertAdjacentHTML|document.write` (expect zero); read check of
  the DOMParser text-only path; output captured in the implement report.

### P2 — Site-level `templates/page.html` override (SC-2's markup routing; SC-10 asset delivery; SC-9) **T-tier: structural fact-check at item time**

- **Deliverable:** `templates/page.html` = exact copy of the vendored
  `themes/abridge/templates/page.html` at base tip `49f1f4d` + one-line
  provenance header comment (source path, base tip SHA, #32) + one
  content-detection block: when `page.content` contains `View on Mastodon`,
  emit `<script defer src="{{ get_url(path='js/mastodon_widget.js',
  trailing_slash=false) }}"></script>` — the lite-video detection pattern of
  `themes/abridge/templates/partials/head_js.html` (lines 12–14).
  `themes/abridge/**` byte-untouched (SC-9).
- **RED:** no site `templates/page.html` exists → no route can deliver the
  script to entry pages; SC-10's "widget asset" page reference impossible.
- **GREEN:** the override, committed on the branch.
- **Tier marks:** structural (diff + build-output fact checks).
- **Instrument:** `diff templates/page.html` vs the vendored base shows only
  header comment + detection block; post-build `grep` of a built entry page
  for `mastodon_widget.js` (expects the tag) and of a built non-entry page
  (expects absence). Outputs captured in the implement report.

### P3 — Docs amendment (SC-8) **T-tier: structural fact-check at item time**

- **Deliverable:** dated (2026-11-21) amendment paragraph to
  `docs/sop-site-setup.md` Content rules rule 5: widget of record — live
  reply display beneath the section, anchor-derived, view-time fetch only,
  no commentary imported into the repo (R-2), fail-silent degradation;
  embeds remain rejected. Mirrored wording in `AGENTS.md`'s Mastodon
  back-link bullet.
- **RED:** rule 5 currently records the plain anchor with no widget
  amendment; the constraint is unrecorded (fact check of current text).
- **GREEN:** the date-stamped amendment + mirror bullet, wording of record
  (SC-5's three strings) unmodified in both docs.
- **Tier marks:** structural.
- **Instrument:** content read/grep of both files; outputs in the implement
  report.

### P4 — Behavioral probe run (SC-1, SC-2, SC-3, SC-5, SC-10) **T-tier: recorded playwright probe run (heavy-instrument evidence: executed once on this cycle, served build, session-recorded outputs — never a default-run test suite)**

- **Deliverable:** one executed probe session against the branch build:
  (a) `./build.sh` exit 0; `public/` holds built entry pages +
  `js/mastodon_widget.js` (SC-10). (b) Per-entry probes: network log records
  the context API request for each entry's thread id; one-reply entry shows
  the known reply substring inside `#mastodon-replies` (container-scoped);
  zero-reply entry → HTTP 200, zero rendered items, section unchanged
  (SC-1). (c) Home/about/blog-index: no widget markup, no mastodon.social
  request (SC-2). (d) Degradation arms on an entry page: JS disabled;
  context API intercepted → failure status; → hanging (never-resolving);
  document-intercepted anchor href rewritten non-status; context API → 200
  non-JSON — each asserts no error UI, no layout change, anchor intact, no
  rendered widget content (SC-3). (e) Exact-string check of SC-5's three
  strings on each built entry page.
- **RED:** pre-implementation build lacks the asset/override → the probe
  session's SC-1 arm fails (asset absent, no container); this is the
  behavior the widget makes true.
- **GREEN:** all arms pass on the assembled branch state.
- **Instrument:** the executed playwright session + build output, reported
  as evidence in the implement report (ephemeral observation, no test files
  authored).

### P5 — Structural scope verification (SC-4, SC-7) **T-tier: fact-check at PR-prep time**

- **Deliverable:** the changed-set check: `git status`/diff on the branch
  lists exactly the widget asset, `templates/page.html`, and the two docs
  files; grep of the changed set for the known reply text and reply-shaped
  JSON finds none (SC-4); `build.sh` and `zola.toml` diff-empty vs trunk
  (SC-7).
- **RED:** n/a — this is a scope assertion over the finished change;
  instrument output is the evidence (run at PR-prep time, before filing).
- **GREEN:** outputs match the expectations.
- **Tier marks:** structural fact-check.
- **Instrument:** executed git diff/grep outputs in the completion report.

## Dependency order and per-item precedence

P1 → P2 → P4, with P3 and P5 parallel-capable:

- Why P1 before P2: P2's template references the asset path P1 creates; the
  P2 build/grep instrument requires the asset to exist.
- Why P2 before P4: P4 probes the built pages; the build only references the
  widget through P2's override, so P4's RED/GREEN are meaningful only on the
  assembled state.
- Why P3 independent: P3 touches only docs of record — no build or probe
  surface depends on it; it is sequenced inline for a single clean commit
  set, never as a dependency.
- Why P5 last: P5 asserts the whole change set's scope, which exists only
  after P1–P4 land.

## Traceability

SC-1→P4; SC-2→P2,P4; SC-3→P1,P4; SC-4→P5; SC-5→P4; SC-6→P1; SC-7→P5;
SC-8→P3; SC-9→P2; SC-10→P1,P2,P4. All ten SCs traced; no untraced items.

## Verification summary (tiers stated once, here)

- Fact-check tier (executed at item time, outputs in the implement report):
  P1 (SC-6 grep/read), P2 (diff + built-page grep), P3 (docs content check).
- Recorded probe run (one cycle-time playwright session, ephemeral
  observation; never a committed/default test tier): P4 (SC-1/2/3/5/10).
- Scope fact-check at PR-prep time: P5 (SC-4/7).
- No test files are authored; all evidence is instrument output captured in
  the implement/completion reports.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*

<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — Blog: client-side Mastodon thread-reply widget (brothertown-language-com #32)

## Intent and Executive Summary

**Problem Statement.** The blog's `### Comment on Mastodon` section is a bare
exit link (SOP Content rules rule 5): a reader on a blog entry page cannot see
that a discussion exists, or what it says, without leaving the page. The
discussion affordance that exists is invisible on the page itself.

**Root Cause / Motivation.** The section's minimalism is a deliberate earlier
decision, not a defect of construction: the embed form was rejected in
`brothertown-language-com#9` (R-4/SC-7) and SOP rule 5 mandates the plain
anchor wording. The gap is a capability one — the thread conversation has no
on-page presence. It must be solved now because the developer selected the
conversation-displaying form ("item D", design discussion 2026-11-21) as the
site's comment affordance and directed that all prior blog entries use the
correct newer form.

**Approach Chosen.** Anchor-derived client-side enhancement: a site-level
script, loaded on blog entry pages via a site-level `templates/page.html`
override using the theme's own content-detection conditional-load pattern,
locates the entry's existing `View on Mastodon` anchor (the thread URL of
record), resolves the status id, fetches
`GET https://mastodon.social/api/v1/statuses/:id/context` from the visitor's
browser, and renders the thread's public replies as text beneath the section.
Every failure path degrades silently to the exact current form. The SOP rule 5
amendment and the `AGENTS.md` mirror line record the form and the binding
constraint.

**Alternatives Considered & Why Discarded.**

- Styled pointer card (Form B, design discussion 2026-11-21) — improves the
  link's presence but displays nothing; the developer selected the
  conversation-displaying form.
- Official embed (blockquote + `embed.js`, or iframe to `/@user/:id/embed`) —
  the rejected class of record (`#9` SC-7; SOP rule 5 embed rejection);
  executes Mastodon's third-party script/iframe and renders the announcement
  toot, not the replies.
- Build-time bake (write replies into repo content at build time) — violates
  the developer's constraint of record: commentary would enter the repository.
- Per-entry shortcode or front-matter key — requires editing every published
  entry (triggering the Edited-provenance rule, SOP Content rules rule 6, for
  each) with no user-visible difference over the anchor-derived mechanism;
  also risks the mandated wording on every edit.

**Key Design Decisions.**

- **KD-1 — Anchor-derived, zero entry edits.** The widget derives each entry's
  thread target from the entry's existing anchor of record. Trade-off: prior
  entries "use the newer form" as a page behavior rather than as a file edit —
  the mandated wording stays byte-untouched and rule 6 is never triggered; new
  entries gain the widget automatically by carrying the section.
- **KD-2 — Text-only rendering.** Mastodon reply HTML is treated as untrusted:
  reply content is inserted only as text nodes. Trade-off: mentions, hashtags,
  and links in replies render as flattened text; no third-party sanitizer
  dependency and no HTML-injection surface.
- **KD-3 — Fail-silent degradation.** Any unavailability (JS disabled, API
  failure, timeout, malformed anchor, script error) leaves the page exactly as
  it is today. Trade-off: no error surfacing; the existing anchor remains the
  always-present floor.
- **KD-4 — View-time fetch only.** The only fetch target is the visitor's
  browser at view time; no build-time API calls and no committed thread data.
  Trade-off: the conversation is always live and never stale; the
  no-commentary-import constraint holds by construction.
- **KD-5 — Inclusion via site-level `templates/page.html` override.** The
  override carries the vendored theme's page template plus one
  content-detection script include (the pattern `themes/abridge/templates/partials/head_js.html`
  already uses for lite-video), keeping `themes/abridge/` untouched.
  Trade-off: override drift risk on theme re-vendor, mitigated by the SOP's
  vendoring review procedure.

**User Intent / Original Prompt.**

- "create spec for item d" — developer, 2026-11-21 (selection of item D, the
  conversation-displaying client-side widget, from the session's design
  discussion).
- "add an sc so that all prior blog entries shall be updated as well to use
  the correct newer form." — developer, 2026-11-21.
- Constraint of record: "no commentary imported into the blog" and "no
  commentary imported into the repo" — developer, 2026-11-21.
- Verification context: "I was only check[ing] to make sure we aren't setting
  this up to compete with any other comments system the site is already
  using." — developer, 2026-11-21; resolved in-session: the site runs no other
  comments system (grep of `content/`, 2026-11-21) — the widget is the only
  comments form.
- Observed state: the newer thread
  (`mastodon.social/@michaelconrad/117624227198231767`) carries one reply (the
  project's 2026-11-16 correction note) that the entry page does not show;
  the founding entry's thread carries zero replies — both verified by live
  API call, 2026-11-21.

## Not Included

- Posting or composing UI on the site — comments happen on Mastodon, the
  venue of record.
- Moderation tooling — instance-side moderation remains the venue's mechanism.
- Quote-post capture — the context endpoint returns replies only; quote
  posts are a platform limitation of this form, not a deliverable behavior.
- Official embed markup (blockquote + `embed.js` / iframe) — the rejected
  class; reopening that rejection is outside this spec.
- Build-time commentary baking — violates the stated constraint.
- Webmention/Bridgy Fed architecture — different venue model, not requested.
- Vendored theme file modifications — the site-level override pattern covers
  inclusion without them.
- Cloudflare dashboard/deploy surface changes — none needed by a static asset.
- Other repositories — single-repo scope; every touched path is under this
  repo's root.

## Requirements

- **R-1** — Every blog entry page (`content/blog/*/index.md`, built page)
  SHALL render, beneath the `### Comment on Mastodon` section, a widget
  displaying that entry's thread conversation: the public replies (context
  descendants) of the thread status the entry's anchor targets, fetched at
  view time from the Mastodon public API for the entry's existing thread URL.
- **R-2** — No thread content SHALL enter the repository: no reply text,
  JSON, HTML, or derived commentary may exist in any committed file, entry
  source, or generated build content; the only fetch target is the visitor's
  browser at view time.
- **R-3** — Reply content SHALL never be inserted into the page as HTML; the
  widget SHALL construct only text nodes (author name, handle, timestamp,
  body as text).
- **R-4** — With JavaScript disabled, on API failure or timeout, on a
  malformed or unparseable anchor, or on any widget-script error, the page
  SHALL show exactly the current form — heading, the two mandated lines, and
  the anchor — with no error UI, no layout change, and no broken placeholders.
- **R-5** — The section's mandated wording SHALL be preserved on every built
  entry page: the `Comment on Mastodon` heading, the
  `You can comment on this post via Mastodon:` line, and the
  `View on Mastodon` anchor to the entry's thread URL.
- **R-6** — The docs of record SHALL carry the change: `docs/sop-site-setup.md`
  Content rules rule 5 gains a dated amendment recording the widget as the
  section's enhancement of record (live reply display; view-time fetch) and
  the 2026-11-21 no-commentary-import constraint; `AGENTS.md`'s Mastodon
  back-link bullet gains the mirror wording in the same PR.
- **R-7** — The build of record SHALL not be modified: `build.sh` and the
  build-relevant `zola.toml` keys remain untouched.
- **R-8** — The widget SHALL be present only on blog entry pages; home,
  about, the blog index, and section pages SHALL render unchanged and SHALL
  issue no Mastodon API call.
- **R-9** — Vendored theme files (`themes/abridge/**`) SHALL remain
  unmodified.
- **R-10** — The build of record SHALL succeed with the change in place,
  producing the built entry pages and the widget asset.

## Success criteria

| ID | Criterion | Class | Instrument |
|----|-----------|-------|-----------|
| SC-1 | Every blog entry page renders its thread conversation beneath the section | behavioral | run `./build.sh`; enumerate `content/blog/*/index.md`; serve `public/`; playwright-probe each entry page: the network log records the context API request for that entry's thread status id issued from the page, and every rendered-content assertion is scoped to the widget's own rendered container (the element the script creates beneath the section; the plan fixes a stable container selector): on the one-reply entry (`…/117624227198231767`) the known reply's stable text substring ("Corrected the pronunciation-tracing note for the pronouns") matches **within that container only** — the same wording exists elsewhere on that page (the entry's `### Edited` section), so a match outside the container is not evidence; on the zero-reply entry (`…/115971090611921901`, verified 2026-11-21) the fetch completes (HTTP 200) with zero rendered reply items and the section unchanged |
| SC-2 | Non-entry pages show no widget and issue no Mastodon call | behavioral | playwright-probe the served home, about, and blog-index pages: no widget markup, no request to any `mastodon.social` API path |
| SC-3 | Enhancement unavailability degrades to the exact current form | behavioral | playwright probes on a served entry page — every arm asserts the same invariant (no error UI, no layout change, the anchor intact, and for fetch-triggering arms no rendered widget content): (a) JavaScript disabled; (b) the context API route-intercepted to a failure status; (c) the context API route-intercepted to a never-resolving (hanging) response; (d) the page document route-intercepted with the anchor's href rewritten to a non-status URL; (e) the context API route-intercepted to HTTP 200 with a non-JSON body |
| SC-4 | No thread content committed anywhere in the repo | structural | scope check: `git diff`-equivalent inspection of the change (staged or trunk diff) lists only the widget asset, the template override, and the two docs files; grep of the changed set for the known reply text and for reply-shaped JSON finds none |
| SC-5 | Built entry pages render the mandated section wording verbatim | structural | built-output check per entry page: the three mandated elements are present with exact strings (`Comment on Mastodon`; `You can comment on this post via Mastodon:`; the `View on Mastodon` anchor to the entry's thread URL) — exact-string form because preservation of the wording of record is the stated requirement |
| SC-6 | Reply content inserted only as text, never as HTML | structural | code check of the widget asset: no `innerHTML`, `insertAdjacentHTML`, `document.write`, or template-literal HTML construction consumes API-derived content; text-node construction only (escapes/`textContent`) |
| SC-7 | Build-of-record scope: `build.sh` and build-relevant `zola.toml` keys unchanged | structural | diff check of the change: `build.sh` and the build-relevant `zola.toml` keys are untouched |
| SC-8 | Docs of record amended, dated | structural | content check: `docs/sop-site-setup.md` rule 5 carries the dated amendment recording the widget form of record and the 2026-11-21 no-commentary-import constraint; `AGENTS.md` carries the mirror wording |
| SC-9 | Vendored theme files untouched | structural | `git status` + diff: no modifications under `themes/abridge/` |
| SC-10 | Build succeeds with the widget asset | behavioral | run `./build.sh` → exit 0; `public/` contains the built entry pages and the widget asset |

## Dependencies

| Reference | Relationship | Status |
|---|---|---|
| `.issues/research-cards/2026-11-21-mastodon-embed-comment-widget-landscape.md` | supplies the verified feasibility facts (public context reads, CORS `*`, rate limits, caps, untrusted-reply discipline) | satisfied |
| `docs/sop-site-setup.md` Content rules rule 5 (lines 193–224) | the amendment target; the wording of record R-5 preserves | satisfied |
| `AGENTS.md` Mastodon back-link bullet | the mirror-amendment target (R-6) | satisfied |
| `brothertown-language-com#9` (R-4/SC-7) | the standing embed rejection this widget must not violate | satisfied |
| `themes/abridge/templates/partials/head_js.html` lite-video pattern | in-repo precedent for content-detection conditional script loading (KD-5) | satisfied |
| Issue `#9`'s site-level `templates/authors/` precedent | the sanctioned site-level override method (KD-5) | satisfied |
| playwright-cli card instruments | the probe surface for SC-1/2/3 | satisfied |

## Traceability

| Requirement | Verified by |
|---|---|
| R-1 | SC-1 |
| R-2 | SC-4, SC-7 |
| R-3 | SC-6 |
| R-4 | SC-3 |
| R-5 | SC-5 |
| R-6 | SC-8 |
| R-7 | SC-7 |
| R-8 | SC-2 |
| R-9 | SC-9 |
| R-10 | SC-10 |

Every SC traces to at least one requirement; every requirement traces to at
least one SC; no orphans in either direction.

## Documentation Sources

| Source | Type | Location | Verification |
|---|---|---|---|
| Mastodon public status/context reads; anonymous caps (40 ancestors / 60 descendants / depth 20) | API docs | `docs.joinmastodon.org/methods/statuses` | docs page fetched; live `GET /api/v1/statuses/117624227198231767/context` → 200, 2026-11-21 |
| CORS on `/api/*` (`Access-Control-Allow-Origin: *`) | source + live header | `mastodon/mastodon` `config/initializers/cors.rb` | header probed with foreign Origin `https://brothertown-language.com`, 2026-11-21 |
| Anonymous rate limit (300 req / 5 min per IP) | API docs + live header | `docs.joinmastodon.org/api/rate-limits` | `x-ratelimit-limit: 300` observed live, 2026-11-21 |
| Thread facts (1 reply / 0 replies) | live API | `mastodon.social` `api/v1/statuses/{117624227198231767,115971090611921901}/context` | live calls 2026-11-21 |
| SOP rule 5 wording of record | repo doc | `docs/sop-site-setup.md` lines 193–224 | read 2026-11-21 |
| Embed rejection of record (`#9` SC-7) | issue store | `.issues/9/spec.md` | read 2026-11-21 |
| Theme content-detection conditional-load pattern | theme source | `themes/abridge/templates/partials/head_js.html` (lite-video includes) | read 2026-11-21 |
| Site-level template override precedent | issue store | `.issues/9/spec.md` R-3 (`templates/authors/`) | read 2026-11-21 |
| No other comments system on the site | repo content | grep of `content/` | run 2026-11-21 (the widget is the site's only comments form) |

## Cost Frame

- **SC-1** — acting: one build + serve + per-entry probe session (~minutes);
  skipping: the developer's chosen capability is asserted, never shown — the
  site's only comments display could be silently absent or broken on some
  entries.
- **SC-2** — acting: two or three extra probe pages; skipping: an
  unintended mastodon.social call on non-entry pages (privacy surface widened
  silently).
- **SC-3** — acting: two route-intercept/no-JS probes; skipping: a
  mastodon.social outage or JS-less visitor shows a broken UI instead of the
  current anchor.
- **SC-4** — acting: diff review; skipping: commentary could enter the repo,
  violating the developer's constraint of record.
- **SC-5** — acting: built-page string checks; skipping: the always-present
  floor form (anchor) could be altered or hidden by the widget's DOM work.
- **SC-6** — acting: asset code review; skipping: an HTML-injection surface
  from untrusted fediverse content ships with the widget.
- **SC-7** — acting: one diff check; skipping: build-time machinery could
  enter the build of record (a commentary-import route by another door).
- **SC-10** — acting: one build run; skipping: a broken template or asset
  could ship undetected.
- **SC-8** — acting: two file reads; skipping: the form and constraint are
  unrecorded — a future session re-derives or contradicts them.
- **SC-9** — acting: one git check; skipping: vendored-theme drift enters the
  re-vendor path unnoticed.

## Edge Cases

- **Condition:** the thread status is deleted or the context endpoint returns
  404/non-200 or times out. **Expected:** widget stays inert; no error UI; the
  anchor remains the sole affordance. **Resolution:** fail-silent per KD-3.
- **Condition:** a thread's reply volume reaches the platform's anonymous
  context bound (60 descendants, verified platform limit). **Expected:** the
  widget renders the replies the context endpoint returns — the platform
  itself bounds the response volume; the anchor remains the link to the full
  thread. **Resolution:** the bound is platform-side; no widget-side
  truncation machinery is specified.
- **Condition:** a thread has zero replies (the founding entry's verified
  state, 2026-11-21). **Expected:** the fetch completes with zero rendered
  reply items; the section renders unchanged. **Resolution:** nothing to
  display is the honest rendering of "display the conversation."
- **Condition:** the entry's anchor href is malformed or its status id is
  unparseable. **Expected:** widget inert, anchor untouched.
  **Resolution:** anchor-derived parsing stays strictly additive.
- **Condition:** reply content carries Mastodon markup (mentions, hashtags,
  links, emoji). **Expected:** flattened, escaped text. **Resolution:** KD-2.
- **Condition:** repeated page views against the anonymous rate limit
  (300/5 min/IP). **Expected:** browser HTTP caching (ETag/304, verified
  live) MAY reduce refetches; per-view volume stays trivial at blog scale.
  **Resolution:** no cache-busting in the widget.

## Completion gate

Every success criterion SC-1 through SC-10 passes before the deliverable is
complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*

<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->
<!-- Provenance: AI-authored from the developer's 2026-10-27 design session (blog-draft-intake brainstorm); decisions of record stated in the Design-decisions section. Companion spec: import-semaphore receipt convention, Brothertown-Language/snea-phonetics#151. Draft source of record: snea-phonetics blog-drafts (#146 there). -->

# [SPEC] blog-draft-intake: on-demand verbatim import of sibling blog drafts + agent-editor conformance pipeline

## Problem

Blog articles arising in sibling research repositories are drafted at draft
time in those repositories' `blog-drafts/` folders and handed to this
repository for finalization and publication under this site's standards. The
site has no receiving surface: no register of the sibling repositories whose
drafts this site is the consumer of, no import procedure that brings a draft —
verbatim, with its supporting evidence — into a tracked place for review, and
no written flow that conforms a handed-over draft into this site's blog
article shape before the standard blog review process starts. Each hand-off
would therefore be improvised, and two failure classes follow: articles get
conformed by typing content onto pages instead of deriving it from the draft
of record, and this site's posting rules (tags, bylines, dates, images, voice)
get applied partially or not at all. Nothing in the tree records which
handed-over drafts have been taken up.

The receiving flow also must not assume its input: it is not known what state
drafts arrive in — the assumption of 100% correct input data is a fallacy
(developer, 2026-10-27 session). Arrival unknown is a design condition, not an
edge case.

## Root causes

- **R-a** — No tracked receiving surface exists. Verified live (2026-10-27):
  `git ls-files` contains no intake- or blog-draft-related path (zero matches
  for `intake|blog-draft` anywhere in the tracked tree; no `blog-draft-intake/`
  on disk); the published blog section lives at `content/blog/` (one post,
  `brothertown-community-language-initiative/`) and was authored here directly,
  not from a sibling hand-off.
- **R-b** — The consuming operation exists nowhere in writing: no register of
  draft-source repositories, no verbatim-copy procedure, no arrival manifest,
  no semaphore placement step. (The producing side's convention of record is
  snea-phonetics #149/#146; its receipt-marker companion spec is
  snea-phonetics#151 — landed here as documentation only, never committed.)
- **R-c** — Conformance is ad hoc: this site's posting rules exist as rules of
  record (this repository's `AGENTS.md` Content rules — adopted 2026-10-27
  from issue #17's standards — plus `docs/authors.md` and the pre-PR review
  SOP), but no written flow applies them to an imported draft as its starting
  artifact; the agent-editor role (authoring metadata, selecting images,
  populating tags) is agent work by design, and nothing records its steps
  between import and review.
- **R-d** — Creep risk: an importer could assume correctness of input and
  silently "fix" upstream content, or scripts could encode intent-decidable
  judgment (image selection, tag text, voice) — hiding agent judgment in
  tooling. The mechanical/judgment split must be recorded, not improvised.

## Design decisions of record (developer, 2026-10-27 session)

- **D1** — A dedicated **tracked** folder holds the base draft-article imports
  with their supporting evidence files; imports are durable, not transient
  staging ("you are assuming a false state" — the correction against
  completion-driven pruning; nothing leaves the folder at publication).
- **D2** — Imports are **verbatim**: this side stages the draft exactly as
  handed over; the original draft upstream is left alone; the conformed
  article is a derivative in the Zola source tree, not an edit of either
  copy.
- **D3** — Import happens **only on demand**: no standing scan, no
  automation; the walk runs when the developer says so.
- **D4** — The register enumerates **only known repos** — the user supplies
  later ones to add to the list.
- **D5** — Arrival state is unknown; the intake must discover what arrived
  (manifest + triage) rather than assume completeness.
- **D6** — The agent **MUST** review the draft as an editor for this site and
  make it conform; the original draft is untouched upstream and in the
  intake copy.
- **D7** — Conformance is done **with agent intelligence** — reviewing
  content, recommended picture selection, tagging, and other metadata — not
  by script.
- **D8** — Deficient drafts are **held as draft blogs in the Zola markdown
  source tree** so they can be reviewed via `zola serve`; assume **always
  `draft = true` until an article is approved**.
- **D9** — Intake-side records (manifests) live **beside** the copy, not
  inside it, preserving verbatim purity (agent judgment; developer deferred
  placement: "no clue").
- **D10** — A one-time receipt **semaphore** (`import-semaphore.md`, name of
  record shared with the companion spec snea-phonetics#151) is placed into the
  upstream draft folder at import — filesystem-only, never committed by this
  side, never rewritten.
- **D11** — After the conformed draft exists in the Zola source tree, the
  **standard blog review process** starts (the SOP pre-PR gate); publication
  comes only on explicit developer approval.

## Requirements

- **R-1** — The tracked folder `blog-draft-intake/` SHALL exist at the repo
  root carrying `README.md`, `AGENTS.md`, and `register.md`, and SHALL be
  self-contained for its own procedure: its records carry the complete
  import/manifest/semaphore/triage/conformance/release flow with no undocumented
  step. Self-containment does NOT mean restating this site's posting rules —
  the conformance flow points at the rules of record (this repository's
  `AGENTS.md` Content rules, `docs/authors.md`, the review SOP) rather than
  duplicating them; the folder's records govern the intake's own mechanics.
- **R-2** — `register.md` SHALL enumerate the sibling repositories of record
  whose `blog-drafts/` folders this site consumes: it SHALL open with exactly
  one row — `snea-phonetics` (verified live 2026-10-27: its checkout carries
  `blog-drafts/` with one draft; the other sibling research repos checked this
  session — `snea-grammar`, `snea-lib`, `snea-shoebox-editor` — carry no
  `blog-drafts/` folder) — with each row naming the local checkout path
  (`../snea-phonetics`), the drafts-folder location, the structural contract
  (`<date>-<slug>/` with `article.md` at the folder root), and a dated sourced
  note. Additions arrive only on explicit developer instruction.
- **R-3** — Import SHALL run only on demand: walk the register rows; for each
  present checkout, copy each draft sub-folder **verbatim** into the intake
  folder; a copy already mirroring an unchanged source is skipped without
  action; a changed source is refreshed as a visible tracked diff (git makes
  the change reviewable); upstream originals are never modified except by the
  semaphore placement (R-5).
- **R-4** — Each import SHALL record an intake-side manifest **beside** the
  copy (never inside it) carrying: source repository and drafts-folder path;
  source revision (commit SHA, or the uncommitted-working-tree state with
  date); file inventory with checksums; the structural contract-check result
  (R-6); arrival gaps as found; and, once conformance has happened, the
  conform pointer (the `content/blog/<slug>/` path and date).
- **R-5** — Import SHALL place the semaphore `import-semaphore.md` into the
  upstream draft folder — a one-time receipt whose content names the importing
  repository, the UTC date, and the received draft identity, carrying the
  companion spec's pinned-canon semantics (placed once, never rewritten). The
  verbatim copy SHALL be taken **before** placement; the contract check
  (R-6) SHALL ignore the semaphore; a draft folder already carrying a
  semaphore SHALL be treated as claimed — the manifest is reconciled, and no
  re-import runs unless instructed. The placement is filesystem-only and
  reversible: the uncommitted file may be deleted to undo it, and it is never
  committed, staged, or rewritten by this side.
- **R-6** — The structural contract check SHALL treat arrival state as
  unknown: it checks (article.md present at the sub-folder root; the
  `<!-- more -->` fold present; the supporting items the draft names present;
  images present-or-explicitly-declared) and records the result in the
  manifest. No gap is repaired at import.
- **R-7** — The agent-editor pass SHALL review each imported draft as an
  editor for this site: first triage — classify what the arrival manifest
  surfaced as agent-fillable under this site's rules versus blockers requiring
  the developer's direction — then conform: Zola front matter (TOML; `date` in
  the bare-`Z` UTC form), bylines from `docs/authors.md` (author keywords are
  minted only there), `[taxonomies]` `tags` populated per the site's tag
  rules with a fresh signed-out Mastodon API check (`GET
  api/v1/tags/<tag>` 7-day history) for carrier-tag text at conform time,
  hashtags carried in the article per the site's hashtag rules (one hashtag
  per site tag, hot-linked to its mastodon.social tag page, placed after the
  sign-off block and before the AI co-authored byline), the Mastodon
  discussion back-link section (`### Comment on Mastodon`, plain
  `[View on Mastodon]` anchor) at the very end, the `<!-- more -->` fold
  retained as the summary separator, image selection from the draft's
  `image-recommendations` with subject-fit and license/credit verification
  and placement per the site's image-placement rules (a referenced
  `  featured_image` checked for existence), the provenance/handoff comment
  block stripped from the published body, and the content audited for
  sensitive leaks/PII before commit. The conform-time Mastodon carrier-tag
  verification is recorded in the import's manifest (its conform section) so
  the check's evidence is reviewable.
- **R-8** — The agent SHALL NOT author content: every factual claim in the
  conformed article traces to the imported draft's tracked evidence
  (`article.md`, `sources-consulted.md`, or the anchors those cite);
  substantive disagreements between the editor and the draft are flagged in
  review, never silently resolved; wording edits are limited to conforming
  the piece to this site's register.
- **R-9** — The conformed article SHALL land as
  `content/blog/<slug>/index.md` with `draft = true`, and `draft = true` is
  permanent until explicit developer approval flips publication — the site's
  standing publish rule.
- **R-10** — A draft that cannot be fully conformed SHALL NOT block the flow:
  conform what stands, record the gaps (in the manifest and as an HTML
  comment placed between the front matter and the body of the conformed
  draft), and leave the held draft in the Zola source tree — `zola serve
  --drafts` review shows every state, including incomplete ones.
- **R-11** — Once a conformed draft exists, the standard blog review process
  SHALL start: the SOP pre-PR review gate (serve the site in the background
  per the repo's review convention and present the preview URL to the
  developer before any PR); the intake's `AGENTS.md` SHALL state that
  publication approval and merge are human gates — the agent issues neither.

## Approach

Branch-first per repository workflow. Create `blog-draft-intake/` carrying
`README.md` (purpose, layout, the on-demand procedure in human terms),
`AGENTS.md` (the standing rules: on-demand-only import, verbatim copies with
untouched originals, unknown-state manifest+triage, fact-preservation in
conformance, semaphore semantics, `draft = true` until approval, human gates),
and `register.md` (the sibling-repos-of-record table opening with exactly
`snea-phonetics`). Docs-only — the import walk and conformance pass are
agent-executed procedures, not scripts; a script may be added later only if
repetition justifies it. The landing is verified by one supervised pilot
cycle against the known live draft (`snea-phonetics` →
`blog-drafts/2026-10-27-brothertown-koine/`): verbatim copy + manifest +
semaphore placement, then the agent-editor conformance into
`content/blog/` with `draft = true` — which puts the standard blog review
process in position to run on a real artifact.

## Success criteria

| ID | Criterion | Class | Verification instrument | Source |
|----|-----------|-------|------------------------|--------|
| SC-1 | `blog-draft-intake/` is tracked at the repo root with `README.md`, `AGENTS.md`, `register.md`; `register.md` carries exactly one sibling row (`snea-phonetics`) naming the checkout path, `blog-drafts/`, the `<date>-<slug>/` contract with `article.md`, and a dated sourced note; the additions rule (developer-instructed additions only) is stated. | structural | `git ls-files blog-draft-intake/` lists exactly the three records; read `register.md` for the row's fields, dated note, and additions rule | R-1, R-2, D1, D4 |
| SC-2 | Executing the documented import walk against the live `snea-phonetics` checkout produces: a byte-identical verbatim copy of `blog-drafts/2026-10-27-brothertown-koine/` inside the intake folder; an intake-side manifest beside the copy carrying source repo/path, revision, inventory with checksums, contract-check result, arrival gaps, and semaphore record; and `import-semaphore.md` placed in the upstream draft folder. | behavioral | checksum comparison upstream-vs-copy (taken before semaphore placement); `git -C ../snea-phonetics status --porcelain` shows exactly one new untracked file — the semaphore under that draft folder — and no other change; read the manifest for its fields | R-3, R-4, R-5, D2, D3, D9, D10 |
| SC-3 | Semaphore semantics hold end-to-end: the placed `import-semaphore.md` is a one-time receipt (importing repo, UTC date, received draft identity; no evolving state); a re-run of the walk does not rewrite it (checksum before/after unchanged) and reconciles the existing manifest instead of duplicating; the contract check ignores it. | behavioral | re-run the walk; compare checksum before/after; read the reconciled manifest; run the contract check and confirm the semaphore is excluded | R-5, D10 |
| SC-4 | The pilot conformance produces `content/blog/<slug>/index.md` with `draft = true` and the site's metadata set: bare-`Z` UTC `date` form; bylines drawn from `docs/authors.md`; `[taxonomies]` `tags` populated; hashtags in the body per the site's hashtag rules with carrier-tag text verified against the signed-out Mastodon API at conform time; `### Comment on Mastodon` section ending the article with the plain `[View on Mastodon]` anchor; the `<!-- more -->` fold retained; no provenance/handoff comment block in the published body. | behavioral | read the produced file for each element; read the manifest's conform section for the carrier-tag verification record; extract comment blocks from the published body and confirm the provenance block's marker phrase (as recorded in the arrival manifest) is absent | R-7, R-8, R-9, D5–D8 |
| SC-5 | The conformed draft does not publish: after `./build.sh`, `public/` contains no version of the draft article's page, and `./zola check` reports no new ERROR lines. | behavioral | run `./build.sh`; confirm `public/blog/<slug>/index.html` is absent; run `./zola check` ERROR lines (only ERROR lines matter — no new errors vs. baseline) | R-9, D8 |
| SC-6 | The held/review surface works: with the conformed draft in place, `./zola serve --drafts --port 1111` (background, per the repo's review convention) serves the draft at its slug URL, and the pilot's arrival gaps — if any — are recorded in the manifest and as a visible note in the draft. | behavioral | serve and fetch the draft URL (HTTP 200 carrying the draft's title); read the manifest + draft for the gap note | R-10, D8 |
| SC-7 | The intake records carry the conduct rules as specified: import on demand only; verbatim copies with untouched originals; unknown-state manifest+triage with no silent repair; agent-does-not-author-facts; `draft = true` until explicit approval; semaphore one-time placement filesystem-only; blockers held in the tree; publication approval and merge stated as human gates. | structural | read `blog-draft-intake/AGENTS.md` and `README.md`; each listed rule appears in the records | R-1, R-3, R-5–R-11, D1–D11 |
| SC-8 | The conformance flow points at the rules of record rather than restating them: the intake records reference this repository's `AGENTS.md` Content rules, `docs/authors.md`, and the review SOP by path, and duplicate no rule body verbatim; the landing's PR-diff shows no changes outside the intake folder (no site content, no config, no existing-post edits — the pilot's `content/blog/` draft is R-9's authorized landing surface). | structural | read the intake records for the references (grep the record paths); PR-diff review of the landing's file list | R-1, R-11 |

## Traceability

| SC | Requirement | Decision anchor |
|----|-------------|-----------------|
| SC-1 | R-1, R-2 | D1, D4 |
| SC-2 | R-3, R-4, R-5 | D2, D3, D9, D10 |
| SC-3 | R-5 | D10 |
| SC-4 | R-7, R-8, R-9 | D5, D6, D7, D8 |
| SC-5 | R-9 | D8 |
| SC-6 | R-10 | D8 |
| SC-7 | R-1, R-3–R-11 | D1–D11 |
| SC-8 | R-1, R-11 | D11; self-containment note in R-1 |

R-8's fact-preservation boundary and R-7's conformance steps are conduct
requirements: their deliverable surface is the intake records (SC-7 states
them) and the pilot's observable outcome (SC-4 checks the produced article's
elements); the pilot is the verification cycle, not a publication (SC-5).

## Impact

Consumers: the blog-review pipeline gains its starting artifact (a conformed
`draft = true` article instead of an improvised page); authors registry
(`docs/authors.md`) becomes the byline source of record for sibling-derived
articles; future sibling repos gaining `blog-drafts/` folders join by
register-row addition (developer-supplied, D4). The upstream side is touched
only by the semaphore placement (filesystem-only, never committed from here —
companion spec snea-phonetics#151 records the convention on that side).
Blast radius: the intake folder (new), one `content/blog/<slug>/` draft (new,
unpublished), and the upstream untracked semaphore file; no existing content,
config, build wiring, or theme file changes (SC-8). Risk: agent-authored site
content is bounded by `draft = true` until approval (SC-5), the review gate
(SC-6, R-11), and the fact-preservation boundary (R-8).

## Out of scope

- The upstream side's documentation of the semaphore convention (companion
  spec snea-phonetics#151 governs `snea-phonetics/blog-drafts/` records) — and
  any commit to that repository, ever (D10).
- Publication of any article: `draft = true` stays until explicit developer
  approval (R-9); the standard review process's own artifacts (PR filing,
  merge) are governed by the existing SOP, not re-specified here.
- Standing/scheduled scanning, automation, or sync tooling (D3).
- Scripted conformance machinery: no script encodes image selection, tag
  text, voice, or any judgment step (D7, R-d).
- Register additions beyond the one known repo (D4).
- Godot/app-bundled materials and non-blog hand-offs.

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)
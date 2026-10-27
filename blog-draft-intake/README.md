<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# blog-draft-intake — receiving surface for sibling blog drafts

This folder is the tracked receiving surface (intake of record,
`brothertown-language-com#23`) for finished blog drafts handed over from the
sibling research repositories. Drafts are written and review-requested on the
research side (see `register.md` for the repositories of record), and this
site finalizes and publishes them under its own standards. Nothing is
improvised at hand-off: each imported draft is taken in **verbatim**, recorded,
triaged, and conformed into the Zola source tree by a written procedure.

## Layout

```
blog-draft-intake/
├── README.md      ← this file: purpose + the procedure in human terms
├── AGENTS.md      ← standing rules binding every agent working this folder
├── register.md    ← the sibling repositories of record and their contracts
├── <repo>/                      ← one folder per register row (source repo)
│   ├── <date>-<slug>/           ← verbatim copy of the upstream draft folder
│   └── <date>-<slug>.manifest.md ← intake manifest, beside the copy (never inside)
```

- Imports live here permanently: an import is a durable tracked record, not
  transient staging. Nothing leaves this folder at publication — the conformed
  article is a derivative in the Zola source tree (under `content/blog/`),
  never an edit of either the upstream original or this verbatim copy.
- Manifests sit **beside** their copy (same naming pattern, `.manifest.md`
  suffix), never inside: the copy stays a byte-exact mirror of the upstream
  draft folder, and the intake's own bookkeeping lives outside that mirror.

## The on-demand procedure

The full walk runs only when the developer says so — no standing scan, no
automation. Per register row whose checkout exists, per draft folder:

1. **Verbatim copy** — copy the draft folder exactly as handed over; a copy
   already mirroring an unchanged source is skipped; a changed source is
   refreshed as a visible tracked diff. The copy is taken **before** any
   semaphore is placed upstream.
2. **Semaphore** — place the one-time receipt `import-semaphore.md` into the
   upstream draft folder (filesystem-only, never committed, never rewritten;
   semantics in this folder's `AGENTS.md`). A draft folder already carrying a
   semaphore is claimed: reconcile the existing manifest and stop.
3. **Manifest** — record beside the copy: source repository and drafts-folder
   path; source revision; file inventory with checksums; the structural
   contract-check result; arrival gaps as found; and, after conformance, the
   conform pointer and the carrier-tag verification record.
4. **Triage + conformance (agent-editor pass)** — review the draft as an
   editor for this site and conform it into `content/blog/<slug>/index.md`
   with `draft = true`. Conformance applies this repository's posting rules of
   record (root `AGENTS.md` Content rules, `docs/authors.md` for bylines, the
   pre-PR review SOP in `docs/sop-site-setup.md`), never restating them here.
5. **Standard review** — once the conformed draft exists, the repository's
   normal blog review process starts: the pre-PR review gate serves the site
   and presents the preview before any PR. Publication approval and merge are
   human gates; agents issue neither.

## What this folder does not do

- It does not publish: `draft = true` stays until explicit developer approval
  (the repository's standing publish rule).
- It does not fix upstream: no gap found at import is repaired in the copy or
  in the upstream original; gaps are recorded and, when agent-fillable under
  this site's rules, filled in the conformed derivative only.
- It does not author facts: every factual claim in a conformed article traces
  to the imported draft's tracked evidence.

## Upstream side (companion convention)

The producer-side convention of record is `snea-phonetics#149`/`#146`; its
receipt-marker companion spec is `snea-phonetics#151`. The upstream
repository's own files govern its side; this side never commits anything to
that repository — the semaphore is the sole filesystem touch there.

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)
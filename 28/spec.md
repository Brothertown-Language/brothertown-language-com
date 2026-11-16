<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — brothertown-language-com#28: Correct the *nin/kin* attribution in the published entry "Where the words come from"

Sibling spec: Brothertown-Language/snea-phonetics#178 (paper/data/draft correction). Authorization: spec stage only; plan and implementation await developer approval.

## Source

Keith's correction to Michael, received in-session 2026-11-16:

> Michael, One quick note on something I missed initially. I/you ("nin/kin") actually derived from PA nīθa, which yields y-dialect nīy > nī, so technically there is no loss of a terminal n.

## Problem

`content/blog/where-the-words-come-from/index.md` L108 attributes the *nin/ni*–*kin/ki* BL-vs-modern-Mohegan difference to "lost final *n*", contradicting the correction above. The entry is published; this is a content correction to it.

## Scope

One file for the entry change plus the content-rules record: `content/blog/where-the-words-come-from/index.md`, `docs/sop-site-setup.md`, and root `AGENTS.md`. The paper of record, derivation data, and the handed-off draft are the sibling spec's surfaces.

## Requirements

- **R-1** The "20 regular" clause SHALL trace the *nin/ni*–*kin/ki* difference to the pronouns' PA *\*nīθa* derivation (y-dialect *nīy > nī*, no terminal-n loss) and SHALL NOT state a lost final/terminal *n* for these forms; the syncope and *miy-* parts keep their attributions.
- **R-2** Everything else SHALL be unchanged: front matter (draft state, date, taxonomies/tags), hashtag line, Mastodon section, byline, and all other body text except the clause edited under R-1 and the provenance section added under R-6.
- **R-3** The clause SHALL attribute only mechanisms the corrected paper of record (per sibling spec snea-phonetics#178) records — the corrected *nīθa* chain for the pronoun pair, syncope in *munahan/munhan*, and the *miy-* give paradigm — and SHALL name no other mechanism (no terminal-n loss anywhere in the clause).
- **R-6** The entry SHALL carry an "edited/changelog" provenance section recording this 2026-11-16 correction (developer directive, same day as R-1's source correction): the section names the corrected attribution as an edit of record, dated, without restating the superseded error as fact — it may reference that the terminal-n phrasing was corrected. Placement: after the article's closing sections and before the `### Comment on Mastodon` section.
- **R-7** The repo's publish-procedure record SHALL adopt the standing practice (developer directive 2026-11-16): whenever an already-published blog entry is updated, the updated entry carries an "edited/changelog" provenance section recording the update, dated, in the R-6 form. The rule is recorded in `docs/sop-site-setup.md`'s Publish procedure list (as its next numbered item) and summarized in root `AGENTS.md`'s Content rules; nothing else in either doc changes.

## Success criteria

| ID | Class | Criterion | Instrument |
|----|-------|-----------|------------|
| SC-1 | content | No *nin/kin* terminal/final-n-loss statement remains anywhere in the entry | read the whole entry — a removed-attribution statement is identified by meaning, not spelling (e.g. "the modern forms dropped *n*" also counts); zero matches |
| SC-2 | content | The corrected clause states the PA *\*nīθa → nīy > nī* attribution | read the clause |
| SC-3 | structural | Everything outside the edited clause and the R-6 provenance section preserved | byte-exact diff — only the clause hunks and the provenance-section addition differ |
| SC-4 | structural | Site builds with the corrected content | `./build.sh` completes; ERROR-class output respected |
| SC-5 | content | The clause names no mechanism beyond R-3's three surviving attributions | read the clause |
| SC-6 | content | The entry carries the R-6 provenance/changelog section, dated 2026-11-16, stating the corrected attribution as an edit of record, placed before the Mastodon section | read the section |
| SC-7 | structural | The R-7 standing practice is recorded in `docs/sop-site-setup.md`'s Publish procedure and summarized in `AGENTS.md`'s Content rules; both files otherwise unchanged | read both records |

## Out of scope

- snea-phonetics paper, data, and draft (sibling spec).
- Draft-state flips, new body content beyond R-1's clause and R-6's provenance section, images, or tags.

## Approach

Edit the single clause per R-1, add the provenance section per R-6, and record the standing practice per R-7; verify SC-1–SC-7; the pre-PR review gate (served preview) applies before any PR.

## Impact

Site readers; the sibling repo keeps the derivation of record. Risk low — one-clause correction on a published page; front matter untouched.

---
Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)

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

One file: `content/blog/where-the-words-come-from/index.md`. The paper of record, derivation data, and the handed-off draft are the sibling spec's surfaces.

## Requirements

- **R-1** The "20 regular" clause SHALL trace the *nin/ni*–*kin/ki* difference to the pronouns' PA *\*nīθa* derivation (y-dialect *nīy > nī*, no terminal-n loss) and SHALL NOT state a lost final/terminal *n* for these forms; the syncope and *miy-* parts keep their attributions.
- **R-2** Everything else SHALL be unchanged: front matter (draft state, date, taxonomies/tags), hashtag line, Mastodon section, byline, and all other body text.
- **R-3** The clause SHALL remain consistent with the sibling spec's corrected paper wording ("patterns the paper already records" stays true of the paper of record); if the paper-side adjudication revises the traced pattern, R-1's wording follows it.

## Success criteria

| ID | Class | Criterion | Instrument |
|----|-------|-----------|------------|
| SC-1 | structural | No *nin/kin* terminal/final-n-loss statement remains in the entry | grep the file near *nin/kin* for "final *n*"/"terminal" — zero matches |
| SC-2 | content | The corrected clause states the PA *\*nīθa → nīy > nī* attribution | read the clause |
| SC-3 | structural | Everything outside the edited clause preserved | byte-exact diff — only the clause hunks differ |
| SC-4 | structural | Site builds with the corrected content | `./build.sh` completes; ERROR-class output respected |

## Out of scope

- snea-phonetics paper, data, and draft (sibling spec).
- Draft-state flips, new content, images, or tags.

## Approach

Edit the single clause per R-1 after the sibling wording settles; verify SC-1–SC-4; the pre-PR review gate (served preview) applies before any PR.

## Impact

Site readers; the sibling repo keeps the derivation of record. Risk low — one-clause correction on a published page; front matter untouched.

---
Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)

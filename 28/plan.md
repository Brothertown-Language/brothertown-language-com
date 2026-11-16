<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# Plan — brothertown-language-com#28 (nin/kin attribution correction + changelog provenance)

Spec: `.issues/28/spec.md` (validated, zero-finding PASS). Branch: `feature/28-ninkin-attribution-changelog`, base tip `cf2d4a8`.

## Item 1 — Correct the clause (SC-2, SC-5)

- Deliverable: in `content/blog/where-the-words-come-from/index.md`, the "20 are **regular**" clause attributes the *nin/ni*–*kin/ki* difference to the PA *\*nīθa → nīy > nī* chain (y-dialect) and names only that mechanism plus the surviving syncope (*munahan/munhan*) and *miy-* attributions.
- RED: current clause (L108) states "lost final *n* from *nin/ni* and *kin/ki*" — instrumented by SC-1's entry read, which fails today.
- GREEN: rewrite the pronoun portion of the clause; syncope and *miy-* text untouched.
- Instrument: read the clause (SC-2, SC-5). Tier: none authored (content check by read).

## Item 2 — No residual terminal-n-loss statement (SC-1)

- Deliverable: the whole entry, re-read after Item 1: no statement attributing final/terminal-n loss to *nin/kin* anywhere (meaning-level check; a correction-referencing mention per R-6 does not count).
- RED: same read as Item 1's RED — fails today because of L108.
- GREEN: delivered by Item 1; this item re-reads the full entry to confirm nothing else in the entry carries the attribution.
- Instrument: read the entry (SC-1). Tier: none authored.

## Item 3 — Changelog provenance section (SC-6, part of R-6)

- Deliverable: an "edited/changelog" section in the entry after the closing sections and before `### Comment on Mastodon`, dated 2026-11-16, stating the corrected attribution as an edit of record (reference-only mention of the corrected terminal-n phrasing, never the superseded error as fact).
- RED: read of the entry shows no provenance section.
- GREEN: append the section at the prescribed placement.
- Instrument: read the section (SC-6).

## Item 4 — Standing practice in the publish-procedure record (SC-7, R-7)

- Deliverable: `docs/sop-site-setup.md` Publish procedure gains the next numbered rule: updates to an already-published blog entry carry the dated "edited/changelog" provenance section (the R-6 form); root `AGENTS.md`'s Content rules gains the one-line summary. Both files otherwise unchanged.
- RED: read of both records shows no such rule.
- GREEN: add rule 6 to the SOP list and the AGENTS.md line.
- Instrument: read both records (SC-7).

## Item 5 — Build evidence (SC-4)

- Deliverable: executed build of the corrected site.
- RED/GREEN: no code assertion — this is the spec's structural gate, run after Items 1–4.
- Instrument: `./build.sh` completes; ERROR-class output respected.

## Item 6 — Preservation evidence (SC-3)

- Deliverable: byte-exact diff showing only the clause hunks and the provenance-section addition against the branch point (`cf2d4a8`).
- Instrument: `git diff cf2d4a8` on the three files; hunks outside Items 1/3 (and R-7's two doc files, which have no hunks beyond Item 4's) are a FAIL.
- Ordering: last — it evaluates everything, so it runs after Items 1–5 pass.

Out of scope: sibling-spec surfaces, draft flip, tags, other content.

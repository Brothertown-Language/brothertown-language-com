<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Register — sibling draft-source repositories of record

This register enumerates the sibling research repositories whose
`blog-drafts/` folders this site consumes for finalization and publication.
**Additions arrive only on explicit developer instruction** — rows are never
added from discovery, scanning, or best guess.

## Repositories

| Repository | Local checkout | Drafts folder | Structural contract | Note |
|---|---|---|---|---|
| `snea-phonetics` | `../snea-phonetics` | `blog-drafts/` | one draft folder per article, named `<date>-<slug>/`, with `article.md` at the folder root (supporting evidence files — `sources-consulted.md`, `image-recommendations.md`, review requests — live beside it in the same folder) | Draft-side convention of record: snea-phonetics#149/#146; receipt-marker companion spec: snea-phonetics#151. Verified live 2026-10-27 (`Brothertown-Language/snea-phonetics`, HEAD `12c31ae`): checkout carries `blog-drafts/` with one draft (`2026-10-27-brothertown-koine/`); sibling repos checked the same session (`snea-grammar`, `snea-lib`, `snea-shoebox-editor`) carry no `blog-drafts/` folder. |

The contract's `<date>-<slug>` naming and `article.md` root placement are what
the intake's structural contract check (see `AGENTS.md` rule 3) verifies at
import; the intake treats them as the draft-source shape of record.

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)
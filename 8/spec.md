<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — Author registry of record (docs/authors.md) + docs/ agent guidance (brothertown-language-com #8)

## Problem

Site content is about to coin author names across several mechanisms at once:
bylines (the `authors` page field), the `authors` taxonomy facets, and ad-hoc
author-mention tags. Nothing in the repository fixes the canonical form of
each author's name, so styling choices drift: "Dr. Keith Cunningham" vs
"Keith Cunningham" produce different keywords, different facet URLs, and
fragmented filtering. The developer directive (2026-10-26): keep a repo doc
that tracks authors cited so a consistent keyword is used for consistent
tagging, so that tags for each author exist for ad-hoc faceting. The same
directive requires properly-maintained agent-facing guidance: a scoped
`/docs/AGENTS.md` (there is none) and a currency pass on the root AGENTS.md's
pointers so future sessions find and obey the registry.

## Scope

In-repo deliverables only: `docs/authors.md`, `/docs/AGENTS.md`, and the
author-registry pointers in the root `AGENTS.md`. No content pages, no
template work, no taxonomy configuration changes (the `authors` taxonomy is
already configured in `zola.toml` from issue #1).

## Requirements

- **R-1** — `docs/authors.md` exists (tracked file, SPDX header) as the
  author-keyword registry of record. Each author entry carries: the
  **canonical display string** (the publicly used styling), the **keyword**
  (the consistent tagging token — the display string's slug form), the
  **authorship role on this site** (one of: main/agent-authored default,
  human main author, guest author, cited-only), and **role/context notes**.
- **R-2** — The seeded roster (from the developer's 2026-10-26 authorship
  decisions and the source post's expert list):
  *Brothertown Language* (main, agent-authored default), *Michael Conrad*
  (human main author; guest author on the initiative post), *Dr. Craig
  Kopris* (guest; advisor/contributor), *Dr. Keith Cunningham* (guest;
  Language Keeper, lead linguist), *Jesse Bowman Bruchac* (cited-only;
  advisor/contributor).
- **R-3** — The registry states the **coupling rule**: the display string is
  the tag source; restyling an author (adding or dropping a title) moves the
  facet URL, so that change happens only by editing the registry — never ad
  hoc on a page.
- **R-4** — The registry states the **growth rule**: a newly cited author is
  added to the registry in the same PR that first cites them; pages never
  mint a keyword the registry does not carry.
- **R-5** — `/docs/AGENTS.md` exists with guidance scoped to the `docs/`
  tree: the directory holds operational/reference docs only and is not site
  content (Zola builds `content/`, not this tree); the inventory of record
  (`sop-site-setup.md`, `authors.md`) with each doc's of-record role; the
  registry-first rule restated; changes via PR review.
- **R-6** — The root `/AGENTS.md` gains two Content-rules bullets: author
  keywords are minted only in `docs/authors.md` (never on a page), and
  blog-post bylines/authors follow the registry's role notes. Nothing beyond
  those two bullets changes in this issue.
- **R-7** — `docs/languages.md` is a **lookup table**: per language, the
  common name(s) for lookup (aliases normalized into the canonical row) ·
  the **official ISO 639-3 name** · the **3-letter ISO code**. Codes come
  from the corpus's `data/csv/languages.csv` cross-checked to the ISO 639-3
  registry — industry standard, never bespoke; varieties without an ISO
  code carry their Glottocode from the data of record (e.g. Montauk). The
  table covers the corpus's language inventory (`∃` rows, aliases joined);
  retired-code notes from the data ride in-line (e.g. "ISO `mof` retired
  for Mohegan"). Cited forms use the "Common [iso]" pattern —
  `Mohegan-Pequot [xpq]` (the developer's "Mohegan [xpt]" example was
  illustrative; the ISO-registry pairing is `xpq`). New languages join the
  table by editing it when the data of record or a citation brings them
  in. R-5's inventory names it alongside `authors.md`.

## Success criteria

| ID | Criterion | Class | Instrument |
|----|-----------|-------|-----------|
| SC-1 | `docs/authors.md` exists and carries an entry for each of the five seed authors with all four fields | structural | content check of the file for the five entries and their fields |
| SC-2 | Each entry pairs its display string with a stated keyword in slug form (e.g. `Dr. Keith Cunningham` → `dr-keith-cunningham`) | structural | content check of all five pairings |
| SC-3 | The coupling rule (R-3) and growth rule (R-4) are stated in the registry | structural | content check |
| SC-4 | `/docs/AGENTS.md` covers the four guidance points of R-5, with the inventory naming `sop-site-setup.md`, `authors.md`, and `languages.md` | structural | content check |
| SC-5 | `/AGENTS.md` carries the two R-6 bullets; `git diff` shows only those lines added | structural | content check + diff-scope check |
| SC-6 | `docs/languages.md` exists as a lookup table (common lookup names · official ISO 639-3 name · 3-letter ISO code; Glottocode where no ISO exists), covering the corpus's `∃` language rows with aliases joined to their canonical rows, codes sampled against the ISO 639-3 registry / `languages.csv`, no bespoke codes | structural | content check + sampled-code verification |

## Out of scope

The back-dated blog entry (separate spec, brothertown-language-com#9);
future roster additions (they follow R-4's rule); any template or config
change; renaming the site default author string (the config's
`author = "Brothertown Language"` is correct as-is per the developer's
"shorter is better" ruling, 2026-10-26). The languages table duplicates no
44-language Nisinoon dataset — it records the site's language set of record
and points at the corpus data for the full holdings.

## Approach

The registry is the data of record for author identity: display strings are
fixed by the registry so facet keywords stay stable, and the two agent-facing
files anchor the convention so no future session re-litigates it. Keyword
derivation follows Zola's taxonomy slugging of the display string; the
registry records the derived keyword explicitly so pages can copy it without
re-deriving.

## Dependencies

- The registry is consumed by issue `brothertown-language-com#9`'s byline
  (R-3 there cites this registry); landing order: #8 before or with #9 in the
  same PR cycle.

## References

- Developer directives, 2026-10-26: the registry requirement ("keep a repo
  doc that tracks authors cited..."; "so that tags for each author exist for
  ad-hoc faceting"); "one main author + guest authors: michael + craig +
  keith"; "Dr." styling for Cunningham and Kopris (developer correction);
  "shorter is better" (project byline string = `Brothertown Language`).
- Source post expert list: michael-conrad.com "Brothertown Community
  Language Initiative" (2026-01-28, fetched 2026-10-26) — Cunningham
  (Language Keeper, lead linguist), Kopris (advisor/contributor), Bruchac
  (advisor/contributor); Bruchac identity live-verified 2026-10-26
  (Wikipedia; Middlebury Language Schools bio — Nulhegan Band of the Coosuk
  Abenaki Nation; director, School of Abenaki).
- Repo conventions: README "AI-contributed changes are clearly marked";
  issue #1's content rules.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
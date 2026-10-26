<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — Author registry of record (docs/authors.md) + docs/ agent guidance (brothertown-language-com #8)

## Problem

Site content is about to coin author names across several mechanisms at once:
bylines (the `authors` page field), the `authors` taxonomy facets, and ad-hoc
author-mention tags. Nothing in the repository fixes the canonical form of
each author's name, so styling choices drift: "Dr. Keith Cunningham" vs
"Keith Cunningham" produce different keywords, different facet URLs, and
fragmented filtering. The same consistency problem holds for **language
names** in cited forms ("Mohegan [xpt]"-style pairings): Glottolog's
canonical names diverge from the ISO 639-3 registry ("Pequot-Mohegan" vs
"Mohegan-Pequot"; "Narrangansett"; "Wampano" vs "Quiripi"), so cited forms
need a fixed lookup ground (developer directive, 2026-10-26: keep a repo doc
that tracks authors cited so a consistent keyword is used for consistent
tagging, so tags for each author exist for ad-hoc faceting; plus the
languages lookup table: "lists common names (for lookup) and the official
ISO name with 3 letter ISO code... similar in concept to 'Mohegan [xpt]' but
industry standard, not bespoke" — itself "only a lookup table", the corpus's
full language inventory, not a limited subset). The directive also requires
a scoped `/docs/AGENTS.md` (there is none) and a currency pass on the root
AGENTS.md's pointers so future sessions find and obey the registry.

## Scope

In-repo deliverables only: `docs/authors.md` (author registry),
`docs/languages.md` (languages lookup table), `/docs/AGENTS.md`, and the
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
  the **official ISO 639-3 name** · the **3-letter ISO code**. Grounds: the
  corpus's `data/csv/languages.csv` (survey pin: repository
  `Brothertown-Language/algonquian-library`, commit
  `7d099119bbacf24b6ddb59d37934fee671116ccf`, 2026-10-26) and the ISO 639-3
  registry's published code tables
  (`iso-639-3_Code_Tables_20261015.zip` — the `Ref_Name` column is the
  official reference name; the Retirements table carries the deprecated
  mappings; fetched 2026-10-26). The table covers the **corpus's full
  language inventory** — every real entry row of `languages.csv`: 131 real
  rows + 97 non-entry rows (96 "see"-pointer alias rows, ALL joined into
  their canonical rows' lookup names, and 1 name-duplicate stub row) at the
  pinned snapshot; the `∃`-flag marks Nisinoon-dataset membership and is
  NOT the inventory boundary (the SNEA core rows — Mohegan-Pequot `xpq`,
  Quiripi `qyp`, Mahican `mjy`, Nanticoke `nnt` and their group/Proto rows
  — are real rows without `∃`). Name of record per row: the ISO registry's
  Ref_Name — the naming determination (online research, 2026-10-26) found
  ISO names both official and de-facto standard: the held scholarly corpus
  texts corroborate (Mohegan-Pequot ~84 occurrences vs Pequot-Mohegan 4 —
  the inverse essentially only in Glottolog's own export; Narragansett 883×
  vs "Narrangansett" 1; Goddard/Mithun use "Massachusett" for the wam
  variety), and for the one community-flavored case ISO itself registered
  the community name **Wampanoag [wam]** (matching the corpus's display;
  scholarly "Massachusett" rides as an alias). Glottolog canonicals and
  scholarly/community alternates ride the lookup/alias columns. Three row
  classes carry ISO codes: (a) 639-3 individual/language pairs (verified
  against the 639-3 code set); (b) ISO 639-5 family codes where the data
  of record carries a 639-5 collection code instead of a 639-3 code
  (Algonquian `alg`, Proto_Algonquian `alg`, Proto_Algic `aql`) — carried
  in-line, explicitly labeled as 639-5 family codes (they fail no check:
  SC-6 verifies them against ISO 639-5, not 639-3); (c) varieties without
  an ISO code — Glottocode only per the data of record (e.g. Montauk
  `mont1269`). Retired-code notes ride in-line (e.g. "ISO `mof` retired
  for Mohegan" — Retirements split 2009-013 into `xpq` + `xnt`, effective
  2010-01-18, confirmed against the registry's Retirements table). Cited
  forms use the "Common [iso]" pattern — `Mohegan-Pequot [xpq]` (the
  developer's "Mohegan [xpt]" example was illustrative; the ISO-registry
  pairing is `xpq`, `xpt` being an unrelated code — Punthamara). New
  languages join the table by editing it when the data of record or a
  citation brings them in. R-5's inventory names it alongside
  `authors.md`.

## Success criteria

| ID | Criterion | Class | Instrument |
|----|-----------|-------|-----------|
| SC-1 | `docs/authors.md` exists and carries an entry for each of the five seed authors with all four fields | structural | content check of the file for the five entries and their fields |
| SC-2 | Each entry pairs its display string with a stated keyword in slug form (e.g. `Dr. Keith Cunningham` → `dr-keith-cunningham`) | structural | content check of all five pairings |
| SC-3 | The coupling rule (R-3) and growth rule (R-4) are stated in the registry | structural | content check |
| SC-4 | `/docs/AGENTS.md` covers the four guidance points of R-5, with the inventory naming `sop-site-setup.md`, `authors.md`, and `languages.md` | structural | content check |
| SC-5 | `/AGENTS.md` carries the two R-6 bullets; `git diff` shows only those lines added | structural | content check + diff-scope check |
| SC-6 | `docs/languages.md` exists as a lookup table covering the corpus's full inventory — every real entry row of `languages.csv` at the pinned snapshot (131 joined rows; 96 alias pointers joined into canonical lookup names; the stub row dropped) — with every ISO-carrying row matching its registry ground: 639-3 pairs against `iso-639-3_Code_Tables_20261015.zip`'s Ref_Name column, 639-5 family codes (alg/aql rows) explicitly labeled and matching ISO 639-5; retired codes resolved via the Retirements table (mof → xpq/xnt split); no bespoke codes anywhere | structural | content check (row coverage: 131 entry rows, all 96 alias lookups present, SNEA-core rows present, stub dropped) + exhaustive ISO cross-check (all 639-3 pairs against the downloaded code set; 639-5 codes against ISO 639-5) |

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
  "shorter is better" (project byline string = `Brothertown Language`);
  the languages lookup-table requirement ("only a lookup table", common
  names + official ISO name + 3-letter code, "industry standard, not
  bespoke", model concept "Mohegan [xpt]"; scope = the corpus's full
  language inventory, "don't artificially limit the language list").
- Corpus survey pin: repository `Brothertown-Language/algonquian-library`,
  tip-of-2026-10-26 snapshot (commit recorded in `docs/authors.md`'s
  provenance note at implementation), held in working state at
  `/tmp/opencode/corpus-survey` for implementation; the registry tables
  re-derive from `git fetch` + `data/csv/languages.csv` at refresh time.
- **Naming-determination sources (2026-10-26)**: ISO 639-3 registry pages
  xpq (Mohegan-Pequot; CR 2009-013, effective 2010-01-18), qyp (Quiripi; CR
  2008-038, effective 2009-01-16), wam (Wampanoag — community name
  registered); corpus-held literature usage counts across
  `algonquian-library/docs/research/` texts (Mohegan-Pequot 84:4,
  Narragansett 883:1, Quiripi/Wampano mixed — Rudes 1998 titles "Wampano
  (Quiripi)", Ethnologue/ISO "Quiripi"); Glottolog naming rationale
  (doculect anchoring + database-unique canonical names — Bosque-Gil et al.
  2022, *Semantic Web*, §3.3; live languoid page wamp1250 carrying the
  ISO qyp mapping box); Wikipedia article titles consistent with ISO
  (Mohegan-Pequot / Narragansett / Quiripi / Massachusett).
- Source post expert list: michael-conrad.com "Brothertown Community
  Language Initiative" (2026-01-28, fetched 2026-10-26) — Cunningham
  (Language Keeper, lead linguist), Kopris (advisor/contributor), Bruchac
  (advisor/contributor); Bruchac identity live-verified 2026-10-26
  (Wikipedia; Middlebury Language Schools bio — Nulhegan Band of the Coosuk
  Abenaki Nation; director, School of Abenaki).
- Repo conventions: README "AI-contributed changes are clearly marked";
  issue #1's content rules.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
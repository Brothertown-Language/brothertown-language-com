<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Author registry of record

This file is the **author-keyword registry of record** for the
brothertown-language.com site (issue `brothertown-language-com#8`). Every
author name that site content bylines, tags, or cites — as a page author, a
mention that needs faceting, or an authority reference on a future
methodology/reference surface — is registered here first, so one keyword
exists per author and ad-hoc faceting stays consistent.

Registry keyword strings feed Zola's `authors` taxonomy and per-page author
lists; facet pages live at `/authors/<keyword>/`.

## Entry fields

| Field | Meaning |
|-------|---------|
| Display string | The publicly used styling of the author's name — fixed by this registry. |
| Keyword | The consistent tagging token: the display string's slug form (lowercase, hyphenated). Used in bylines, `authors` lists, and ad-hoc tags for that author. |
| Site role | How this author appears on the site: `main (agent-default)` — byline for agent-authored material; `human main` — byline for material the person writes; `guest` — per-post guest byline; `cited` — named in content without authorship. |
| Notes | Role, context, sources. |

## Site roster

| Display string | Keyword | Site role | Notes |
|----------------|---------|-----------|-------|
| Brothertown Language | `brothertown-language` | main (agent-default) | The project voice. Byline of record for agent-authored materials (developer decision, 2026-10-26); matches the site title and the `author` default in `zola.toml`. |
| Michael Conrad | `michael-conrad` | human main | Technical and materials support; author of the founding "Brothertown Community Language Initiative" post (michael-conrad.com, 2026-01-28). The site's ported initiative entry (issue #9) carries the project-only byline — developer correction, 2026-10-27: a project posting is not attributed to individuals as a writing credit; Conrad is body-credited there, and the link-back line carries source provenance. |
| Dr. Craig Kopris | `dr-craig-kopris` | cited | Advisor/contributor; Powhatan revitalization experience (per the source post). Body credit only — the ported initiative entry (issue #9) carries the project-only byline (developer correction, 2026-10-27). |
| Dr. Keith Cunningham | `dr-keith-cunningham` | cited | Language Keeper; lead linguist. Nanticoke materials in the corpus library (incl. "A Revised Phonological Analysis of the Heckewelder Vocabulary of Nanticoke", AC56 abstract — source text self-identifies: "Linguist, Nanticoke Indian Tribe"). Body credit only — the ported initiative entry (issue #9) carries the project-only byline (developer correction, 2026-10-27). |
| Jesse Bowman Bruchac | `jesse-bowman-bruchac` | cited | Advisor/contributor. Nulhegan Band of the Coosuk Abenaki Nation; director of Middlebury's School of Abenaki (live-verified 2026-10-26). Body credit only — not a guest byline. |

## Conventions (binding)

- **Coupling rule:** the display string *is* the tag source. Restyling an
  author — adding or dropping a title, changing a spelling — moves the
  facet URL (`dr-keith-cunningham` would not survive reverting to plain
  "Keith Cunningham"). Such a change happens only by editing this registry,
  never ad hoc on a page.
- **Growth rule:** a newly cited author is added to this registry in the
  same PR that first cites them. A page never mints a keyword this registry
  does not carry.
- **Variant citations** observed in source data (e.g. "Valentine" vs
  "Valentine 2002") facet to the single canonical keyword in this registry;
  variant strings are noted, not re-keyed.
- **Speakers are not authors here.** The corpus carries a structured
  `Speaker` column (source-of-form attribution); speaker faceting is a
  separate decision to make when the site first cites speakers, and will
  get its own registry section then.

## Corpus-survey roster (initial survey, 2026-10-26)

Survey source: the corpus material of record,
`Brothertown-Language/algonquian-library`, pinned snapshot
`7d099119bbacf24b6ddb59d37934fee671116ccf` (2026-10-26) — structured
`Author Surname` / `Speaker` fields in the Nisinoon components data, the
`Authority References` column in glyph conventions, and the source-text
holdings under `docs/research/sources/`. Sibling research repos
(`snea-phonetics`, `snea-grammar`, `snea-lib`, `ea-subgrouping`) cite the
same author set. The companion lookup table for **languages** lives at
[`docs/languages.md`](languages.md) — same registry pattern, ISO-registry
ground. Role of every entry below: `cited` (corpus material) —
eligible for site reference/faceting use as the methodology and reference
surfaces land; promote to guest/human-main only by developer instruction.

### SNEA core sources (primary and scholarly)

| Display string | Keyword | Notes |
|----------------|---------|-------|
| Roger Williams | `roger-williams` | *A Key into the Language of America* (1643) — Narragansett source of record. |
| John Eliot | `john-eliot` | Massachusett Bible print (1661/1663) and *The Indian Grammar Begun* (1666). |
| Edward Winslow | `edward-winslow` | *Good Newes from New England* (1624) — 44-word vocabulary source. |
| Thomas Shepard | `thomas-shepard` | *The Day-Breaking* (1647), Massachusett mission text. |
| Jonathan Edwards | `jonathan-edwards` | 1787 observations on the Mohegan/Mohican ("Muhhekaneew") language. |
| J. Dyneley Prince | `j-dyneley-prince` | Co-author, Prince & Speck (1904). |
| Frank G. Speck | `frank-g-speck` | Co-author, Prince & Speck (1904). |
| J. Hammond Trumbull | `j-hammond-trumbull` | 1903 Natick dictionary; Trumbull citations across SNEA notes. |
| Stephanie Fielding | `stephanie-fielding` | *A Modern Mohegan Dictionary* (2006 ed., prepared for the Council of Elders) — confirmed from the source text itself; the library's manifest also credits it as **Fielding & Costa (2006)** (David Costa collaboration). |
| Frank Waabu O'Brien | `frank-waabu-obrien` | Narragansett grammatical studies, spelling guides, Waabu/bigorrin charts. |
| Ives Goddard | `ives-goddard` | 1980 Massachusett texts; 1981 phonology; Mahican paper; "West-to-East Cline in Algonquian Dialectology". |
| Kathleen J. Bragdon | `kathleen-bragdon` | Goddard & Bragdon (1988), *Native Writings in Massachusett* — the glyph-conventions authority of record. |
| Blair A. Rudes | `blair-a-rudes` | 1998 Wampano (Quiripi) etymologies — confirmed from the source text. |
| W. DeLoss Love | `w-deloss-love` | 1899 Samson Occom biography. |
| Samson Occom | `samson-occom` | 18th-century Mohegan minister — chiefly cited as a historical figure (subject of Love 1899), not as a text author. |
| The Narragansett Dawn | `narragansett-dawn` | 1935–36 Narragansett community periodical — collective authorship. |
| Higgins | `higgins` | era-texts machine-readable Massachusett store; given name not established in the surveyed corpus — record it at first site citation. |

### Broader-holdings citations (Nisinoon components database)

Cited surnames, exactly as they appear in the data, with citation counts
(initial survey; keyword = slug of the as-cited string):

| As cited | Keyword | Citations |
|----------|---------|-----------|
| Macaulay | `macaulay` | 2212 |
| Bloomfield | `bloomfield` | 1982 |
| Hewson | `hewson` | 1195 |
| Day | `day` | 1007 |
| Fisher et al. | `fisher-et-al` | 932 |
| Voorhis | `voorhis` | 683 |
| Beland | `beland` | 624 |
| Denny | `denny` | 614 |
| Rhodes | `rhodes` | 515 |
| Inglis | `inglis` | 473 |
| Goddard | `goddard` | 430 |
| Costa | `costa` | 352 |
| Wolfart | `wolfart` | 342 |
| Aubin | `aubin` | 342 |
| Thomason | `thomason` | 312 |
| Valentine | `valentine` | 353 (298 + 55; "Valentine 2002" variant merges here) |
| Lockwood | `lockwood` | 234 |
| Cook & Muehlbauer | `cook-muehlbauer` | 223 |
| Hockett | `hockett` | 193 |
| Haas | `haas` | 158 |
| York | `york` | 156 |
| Drapeau | `drapeau` | 89 |
| McCulloch | `mcculloch` | 85 |
| Lambert-Bretiere | `lambert-bretiere` | 64 |
| Siebert & Seeber | `siebert-seeber` | 61 |
| Teeter | `teeter` | 60 |
| Ellis | `ellis` | 58 |
| Junker | `junker` | 54 |
| LeSourd | `lesourd` | 38 |
| Baraby et al | `baraby-et-al` | 35 |
| Dahlstrom | `dahlstrom` | 33 |
| Wolvengray | `wolvengray` | 33 |
| Pentland | `pentland` | 30 |
| Brittain | `brittain` | 29 |
| Arppe et al. | `arppe-et-al` | 29 |
| Bruening | `bruening` | 29 |
| Mathieu | `mathieu` | 28 |
| Drapeau & Lambert-Bretiere | `drapeau-lambert-bretiere` | 22 |
| Bakker | `bakker` | 10 |
| Siebert | `siebert` | 10 |
| Armoskaite & Junker | `armoskaite-junker` | 6 |
| Barrie & Mathieu | `barrie-mathieu` | 7 |
| Brittain & Acton | `brittain-acton` | 4 |
| Cowan | `cowan` | 8 |
| Grafstein | `grafstein` | 9 |
| Wolfart & Shrofel | `wolfart-shrofel` | 4 |

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)
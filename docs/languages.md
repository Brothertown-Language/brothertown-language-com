<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Languages lookup table (of record)

A lookup table for cited language forms: **common name(s)** for lookup
(aliases and variant spellings joined into their canonical row) · the
**official ISO 639-3 reference name** · the **3-letter ISO code** · the
**Glottocode**. Cited forms carry the "Common [iso]" convention, e.g.
*Mohegan-Pequot* [`xpq`] — one language, one industry-standard name/code
pair, never bespoke codes.

**Naming determination (online research, 2026-10-26):** ISO 639-3 registry
reference names are both the official standard and the de-facto standard
for this set — the held scholarly corpus texts corroborate them
(*Mohegan-Pequot* ~84× vs *Pequot-Mohegan* 4× across the held library
texts, the inverse essentially confined to Glottolog's own export;
*Narragansett* 883× vs *Narrangansett* 1×; Glottolog's *Wampano* is its
uniqueness-driven editorial name and rides as an alias for *Quiripi*
[qyp]). For the one community-flavored case, ISO registered the community
name **Wampanoag [wam]** (scholarly "Massachusett" rides as an alias).
Glottolog's divergences are deliberate editorial naming (doculect-anchored,
database-unique); they are aliases here, never the name of record.

## Sources of record & verification (all verified 2026-10-26)

- Language inventory: `data/csv/languages.csv` — the Nisinoon Algonquian
  Components Project language sheet, from the corpus library of record
  `Brothertown-Language/algonquian-library`, pinned snapshot
  `7d099119bbacf24b6ddb59d37934fee671116ccf` (2026-10-26). The sheet's 228
  rows = **131 real entry rows** (all in this table) + **96 "see"-pointer
  alias rows** (every one joined into its canonical row's lookup column —
  pointer targets in alternate spellings, e.g. the pointer typo
  "Powahatan" → Powhatan, resolved to their intended rows) + 1 bare
  name-duplicate stub row (dropped). The `∃`-flag marks membership in the
  Nisinoon components dataset, not inventory.
- ISO ground: the ISO 639-3 registry's published code tables
  (`iso-639-3_Code_Tables_20261015.zip`, fetched 2026-10-26). **Exhaustive
  verification (scripted):** every ISO 639-3 row's name/code pair matches
  the registry (`Ref_Name` column) exactly; the 639-5 family codes match
  ISO 639-5; both retired-code rows resolve via
  `iso-639-3_Retirements.tab` (`mof` split 2009-013 → `xpq` + `xnt`,
  effective 2010-01-18; `pmk` → `crr`, effective 2023-01-20); zero
  mismatches.
- Placeholder rows: varieties the data of record carries with neither ISO
  code nor Glottocode (17 rows — e.g. East Cree, Pocumtuc, Mascouten)
  present both cells as `—`, exactly as the data carries them; nothing is
  invented.
- Growth rule: a language row joins this table by editing it — when the
  language data of record gains rows or a citation first needs one.

## Table

| Common name(s) (lookup) | Official ISO name (Ref_Name) | ISO 639-3 | Glottocode | Notes |
|---|---|---|---|---|
| Abenaki · Abnaki | — | — | `aben1250` | [public] Used if Eastern or Western not specified |
| Albany River Ojibwe · Albany River Ojibwa | — | — | `alba1270` | [public] GL: dialect of Northwestern Ojibwa |
| Algic | — | — | `algi1248` | [public] Algic language family |
| Algonquian | Algonquian languages († 639-5 family) | `alg` | `algo1256` | [public] Refers to "Algonquian language family," if used generically (e.g. “In Algonquian languages…”); NOT the same as Algonquin or Proto-Algonquian |
| Algonquin · Golden Lakes Algonquin · Omàmìwininìmowin | Algonquin | `alq` | `algo1255` | Autonym source: Wikipedia (has tag "citation needed")" |
| Arapaho · Hinónoʼeitíít | Arapaho | `arp` | `arap1274` | [public] GL lists under Arapaho-Gros Ventre-Besawunena, [public] Autonym source: Wikipedia |
| Arapaho-Gros Ventre-Besawunena · Besawunena | — | — | `arap1280` | [public] Arapaho and Gros Ventre have their own codes; Besawunena does not; GL lists under Arapahoic |
| Arapahoic | — | — | `arap1273` | [private] GL has this w/ Arapaho-Gros Ventre-Besawunena and Nawathinehena under it; we are unlikely to use it. |
| Atikamekw · nehirâmowin | Atikamekw | `atj` | `atik1240` | [public] Autonym source: Wikipedia (has tag "citation needed") |
| Beothuk | Beothuk | `bue` | `beot1247` | — |
| Berens River Ojibwe · Berens River Ojibwa | — | — | `bere1251` | [public] GL: dialect of Northwestern Ojibwa |
| Big Trout Lake Severn Ojibwe · Big Trout Lake Severn Ojibwa | — | — | `bigt1234` | — |
| Blackfoot · Siksika · Blackfeet (in the U.S.) · Niitsi'powahsin | Siksika | `bla` | `siks1238` | [public] David Costa's publications call it "Miami-Illinois." GL just calls it "Miami.", Autonym source: Wikipedia. |
| Blood | — | — | `bloo1239` | [public] GL: dialect of Siksika (Blackfoot) |
| Border Lakes Ojibwe · Border Lakes Ojibwa | — | — | — | — |
| Carolina Algonquian | Carolina Algonquian | `crr` | `caro1243` | [public] GL treats this and Pamlico as the same; but have different ISO codes |
| Central Eastern Southwestern Ojibwe · Central Eastern Southwestern Ojibwa | — | — | `cent2252` | [public] GL uses as parent of Central Ojibwe, Chippewa, & Eastern Ojibwe; only used code if all intended |
| Central Innu | — | — | — | [public] Central dialect of Innu (Montagnais) |
| Central Minnesota Chippewa | — | — | `cent2135` | [public] Dialect of Chippewa |
| Central Ojibwe · Central Ojibwa | Central Ojibwa | `ojc` | `cent2136` | [public] GL uses as daughter of Central-Eastern-Southwestern Ojibwe |
| Cheyenne · Sutaio · Tsėhesenėstsestotse | Cheyenne | `chy` | `chey1247` | [public] Autonym source: Wikipedia |
| Common Cree | Cree | `cre` | `cree1272` | [public] Used only if dialect unspecified |
| Common Delaware | Delaware | `del` | `comm1246` | [public] Used only when Munsee or Unami/Lenape not specified |
| Common Meskwaki-Kickapoo | — | — | `foxx1245` | — |
| Common Ojibwe · Ojibwa, Chippewa · Anishinaabemowin, Ojibwemowin | Ojibwa | `oji` | `ojib1241` | [public] Used only if dialect unspecified |
| Deer Lake Severn Ojibwe · Deer Lake Severn Ojibwa | — | — | `deer1234` | — |
| Delawaran | — | — | `dela1253` | [public] Used only if specific Delaware language not specified. Includes Mahican. |
| East Cree | — | — | — | [public] Used only if S or N East Cree not specified |
| East Innu · Eastern Montagnais | — | — | `east2540` | — |
| Eastern Abenaki · Caniba · Penobscot · Eastern Abnaki · Alənαpαtəwéwαkan | Eastern Abnaki | `aaq` | `east2544` | [public] Autonym source: Wikipedia |
| Eastern Algonquian | — | — | `east2700` | [public] Used only if Proto-EA not specified |
| Eastern Great Lakes Algonquian | — | — | `east2765` | [public] Subfamily; not a commonly used designation |
| Eastern Naskapi | — | — | `east2539` | — |
| Eastern Ojibwe · Nishnaabemwin · Eastern Ojibwa | Eastern Ojibwa | `ojg` | `east2542` | — |
| Eastern Swampy Cree · ininîmowin, ᐃᓂᓃᒧᐎᓐ | — | — | `east2541` | [public] Dialect of Swampy Cree but included here because there's a GC, [public] Autonym source: Wikipedia |
| Etchemin | Etchemin | `etc` | — | [public] Not listed in GL |
| Gros Ventre · Atsina · Aaniiih | Gros Ventre | `ats` | `gros1243` | [public] GL lists under Arapaho-Gros Ventre-Besawunena |
| Innu · Innu-Aimun · Montagnais · Innu-Aimun, Montagnais | Innu | `moe` | `mont1268` | — |
| Kickapoo | Kickapoo | `kic` | `kick1244` | — |
| Lac Seul Ojibwe · Lac Seul Ojibwa | — | — | `lacs1238` | [public] GL: dialect of Northwestern Ojibwa |
| Lake of the Woods Ojibwe · Lake of the Woods Ojibwa | — | — | `lake1257` | [public] GL: dialect of Northwestern Ojibwa |
| Loup A · Nipmuk · Nipmuc | Loup A | `xlo` | `loup1243` | — |
| Loup B · Nipmuc | — | — | — | — |
| Mahican | Mahican | `mjy` | `mahi1248` | [public] Wikipedia says the same as Stockbridge but classified differently in Glottolog; treated as part of Delawaran |
| Malecite | — | — | `male1293` | [public] Used only if cited alone; otherwise use Passamaquoddy_Maliseet |
| Mascouten | — | — | — | [public] No ISO or GC for this; LinguistList gives it code qes; see Sauk-Fox-Kickapoo |
| Menominee · Oma͞eqnomenēweqnaesen, Mamāceqtaweqnaesen | Menominee | `mez` | `meno1252` | — |
| Meskwaki · Fox · Meskwakie, Fox · Meshkwahkihaki | Ma Manda | `skc` | `mesk1243` | [public] GL spells it “Meskwakie” and uses “Meskwaki” for “Sauk-Fox”; this code is for the single language AKA “Fox”; not when Kickapoo and/or Sauk are included. |
| Miami-Illinois · Illinois · Miami · Myaamia, Peoria · myaamia | Miami | `mia` | `miam1252` | [public] This is what David Costa's publications call it. GL just calls it "Miami.", [public] Autonym source: Wikipedia |
| Michif | Michif | `crg` | `mich1243` | — |
| Minnesota Border Chippewa | — | — | `minn1250` | [public] Dialect of Chippewa |
| Mi’kmaq · Micmac · Micmac, Mi'kmaw · Miꞌkmawiꞌsimk | Mi'kmaq | `mic` | `mikm1235` | [public] Autonym source: Wikipedia |
| Mohegan-Montauk-Narragansett | (★ retired) | `mof` | `mohe1244` | ISO mof retired (effective 2010-01-18): split; [public] Used only if whole group cited; ISO code “mof” retired for Mohegan |
| Mohegan-Pequot · Pequot · Shinnecock-Poosepatuck · Shinnecock-Poosepatuck, Montauk | Mohegan-Pequot | `xpq` | `pequ1242` | [public] Montauk has a separate glottocode; ISO code “mof” retired for Mohegan |
| Montagnais-Naskapi | — | — | `cree1271` | [public] Only used if treated as a group |
| Montauk | — | — | `mont1269` | [public] Used only if Montauk cited alone; otherwise Mohegan_Pequot used |
| Moose Cree · ililîmowin, ᐃᓕᓖᒧᐎᓐ | Moose Cree | `crm` | `moos1236` | [public] L-dialect; mutually intelligible with Swampy Cree (west coast of James Bay), [public] Autonym source: Wikipedia |
| Moose-Swampy Cree | — | — | — | [public] Used only if both described together |
| Munsee · monsii | Munsee | `umu` | `muns1251` | [public] Autonym source: Wikipedia |
| Nanticoke | Nanticoke | `nnt` | `nant1249` | — |
| Nanticoke-Conoy | — | — | `nant1248` | — |
| Narragansett | Narragansett | `xnt` | `narr1280` | — |
| Naskapi | Naskapi | `nsk` | `nask1242` | [public] Used only if E or W Naskapi not specified |
| Nawathinehena | Nawathinehena | `nwa` | `nawa1259` | [public] GL lists under Arapahoic |
| Nipissing · Maniwaki | — | — | `mini1254` | [public] "... with Mississauga Ojibwa and Odawa form the Nishnaabemwin (Eastern Ojibwa) group of the Ojibwa dialect continuum" (Wikipedia). [public] "Speakers at Maniwaki consider their language to be Southern Algonquin, though linguistically it is a dialect of Nipissing Ojibwa, which together with Mississauga Ojibwa and Odawa form the Nishnaabemwin (Eastern Ojibwa) group of the Ojibwa dialect continuum." (Wikipedia) |
| Nishnaabemwin | — | — | — | — |
| Northern Alberta Cree | — | — | `nort2960` | [public] Dialect of Plains Cree but included here because there's a GC |
| Northern Algonquin | — | — | `nort3290` | — |
| Northern Cree | — | — | — | — |
| Northern East Cree · Cree East(ern) · iyiyiu-Ayamiwin, ᐄᔨᔫ ᐊᔨᒨᓐ | Northern East Cree | `crl` | `nort1552` | [public] Autonym source: Wikipedia |
| Northern Macro-Group (Ojibwe) | — | — | — | [public] Category comes from Valentine 2002. He says it "encompass[es] particularly northern Algonquin and Severn Ojibwe, but also to a varying extent varieties of Ojibwe spoken in northern Ontario, extending east across the Canadian shield." |
| Northern Mi'kmaq · Micmac, Mi'kmaw | — | — | `nort2962` | — |
| Northern Ojibwe · Anishinaabemowin | — | — | — | [public] Category comes from Valentine 2002. He describes it as "in northern Ontario south of the Severn region." |
| Northwestern Ojibwe · Northwestern Ojibwa | Northwestern Ojibwa | `ojb` | `nort2961` | — |
| Northwestern Saulteaux Ojibwe · Northwestern Saulteaux Ojibwa | — | — | `nort3181` | — |
| Nuclear Miami · Myaamia | — | — | `nucl1653` | [public] GL distinguishes from “Peoria” (GC peor1238); ISO 639-3 does not. We are not using this. |
| Nuclear Ojibwe · Nuclear Ojibwa | — | — | `nucl1723` | [public] GL uses as parent of Central-Eastern-Southwestern Ojibwe & Northwestern-Saulteaux Ojibwe; only used if all intended |
| Odawa · Ottawa · Nishnaabemwin | Ottawa | `otw` | `otta1242` | — |
| Ojibwe-Potawatomi | — | — | `ojib1240` | [public] Used only when both treated together; ISO does not have a single code for the combination |
| Old Algonquin | — | — | — | — |
| Pamlico | (★ retired) | `pmk` | `caro1243` | ISO pmk retired (effective 2023-01-20): crr; [public] GL treats this and Carolina Algonquian as the same; different ISO codes |
| Malicite-Passamaquoddy, Passamaquoddy-Malicite | Malecite-Passamaquoddy | `pqm` | `male1292` | [public] GL has code male1293 for Maliseet alone |
| Passamaquoddy-Maliseet · Maliseet-Passamaquoddy · Malecite-Passamaquoddy, Maliseet-Passamaquoddy · skicinuwatuwewakon | Malecite-Passamaquoddy | `pqm` | `male1292` | [public] Autonym source: Wikipedia |
| Piegan | — | — | `pieg1239` | [public] GL: dialect of Siksika (Blackfoot) |
| Piscataway | Piscataway | `psy` | `pisc1239` | [public] GL lists under Nanticoke-Conoy |
| Plains Cree · nêhiyawêwin, ᓀᐦᐃᔭᐍᐏᐣ, nîhiyawîwin | Plains Cree | `crk` | `plai1258` | [public] Autonym source: Wikipedia |
| Plains Cree Nuclear · Nuclear Plains Cree | — | — | `nucl1654` | [public] Dialect of Plains Cree but included here because there's a GC |
| Plains Creeic | — | — | `plai1254` | [private] Unlikely to ever be used! |
| Pocumtuc · Pocumtuck | — | — | — | [public] Not in GL; not clear what it was related to (https://en.wikipedia.org/wiki/Pocomtuc) |
| Potawatomi · Bodwéwadmimwen | Potawatomi | `pot` | `pota1247` | [public] Autonym source: Wikipedia |
| Powhatan · Virginia Algonquian | Powhatan | `pim` | `powh1243` | — |
| Proto-Algic | Algic languages († 639-5 family) | `aql` | `algi1248` | — |
| Proto-Algonquian | Algonquian languages († 639-5 family) | `alg` | `algo1256` | [public] This glottocode is the one that includes Blackfoot - they have it outside Algonquian proper |
| Proto-Arapaho-Gros Ventre-Besawunena | — | — | `arap1280` | — |
| Proto-Central Algonquian | — | — | — | [public] Not commonly accepted as subfamily |
| Proto-Central Eastern Algonquian | — | — | — | — |
| Proto-Eastern Algonquian | — | — | — | — |
| Proto-Ojibwe-Potawatomi | — | — | `ojib1240` | — |
| Proto-Southern New England Algonquian · Common Southern New England Algonquian | — | — | `sout3237` | — |
| Quiripi · Naugatuck · Quinnipiac · Unquachog · Wampano · Quiripi-Unquachog, Quiripi-Naugatuck, Wampano, Quinnipiac | Quiripi | `qyp` | `wamp1250` | [public] Haas 1967: "Southern Long Island" > Aubin 1975 "Long Island" (?) |
| Rainy River Ojibwe · Rainy River Ojibwa | — | — | `rain1239` | [public] GL: dialect of Northwestern Ojibwa |
| Red Lake Chippewa | — | — | `redl1238` | [public] Dialect of Chippewa |
| Sauk · Sac | — | — | `sacc1239` | — |
| Sauk-Fox | Meskwaki | `sac` | `mesk1242` | [public] GL calls this “Meskwaki”; we reserve that term for the language also called “Fox” |
| Sauk-Fox-Kickapoo · Fox-Sauk-Kickapoo | — | — | `foxx1245` | [public] GL uses just “Fox” as parent of Kickapoo & Meskwaki (+ Sauk) - this code only used if that grouping is intended. |
| Saulteaux · Western Ojibwe | Western Ojibwa | `ojw` | `west1510` | [public] GL: daughter of Northwestern Saulteaux Ojibwe |
| Severn Algonquin Ojibwe · Severn Algonquin Ojibwa | — | — | `seve1242` | — |
| Severn Ojibwe · Oji-Cree · Severn · Anishininiimowin | Severn Ojibwa | `ojs` | `seve1240` | [public] Autonym source: Glottolog |
| Severn River Ojibwe · Severn River Ojibwa | — | — | `seve1241` | — |
| Shawnee · Sawanwa, Savannah, Sewanee, Shawano | Shawnee | `sjw` | `shaw1249` | [public] Autonym source: Wikipedia |
| Southern East Cree · Cree East(ern) · Mistassini · iyiniu-Ayamiwin ᐄᓅ ᐊᔨᒨᓐ | Southern East Cree | `crj` | `sout2978` | [public] Autonym source: Wikipedia |
| Southern Innu · Betsiamites · Mashteuiatsh | — | — | — | — |
| Southern Macro-Group (Ojibwe) | — | — | — | [public] Category comes from Valentine 2002. He says it "consists of the dialects found near the Great Lakes, particularly Odawa, Eastern Ojibwe, Southwestern Ojibwe, and much of Saulteaux." |
| Southern Mi'kmaq · Micmac, Mi'kmaw | — | — | `sout2979` | — |
| Southern New England Algonquian | — | — | `sout3237` | [public] Subfamily; not a commonly used designation |
| Southwestern Ojibwe · Chippewa · Anishinaabemowin | Chippewa | `ciw` | `chip1241` | [public] GL has several daughter languages, [public] Autonym source: Wikipedia |
| Stockbridge | — | — | `stoc1242` | [public] Wikipedia says the same as Mahican but classified differently in Glottolog |
| Swampy Cree · Nêhinawêwin, ᓀᐦᐃᓇᐍᐏᐣ | Swampy Cree | `csw` | `swam1239` | [public] Used only if E vs. W not specified; N-dialect; mutually intelligible with Moose Cree (west coast of James Bay), [public] Autonym source: Wikipedia (has tag "citation needed") |
| Turtle Mountain Chippewa | — | — | `turt1236` | [public] Dialect of Chippewa |
| Unami · Lenape · ləná·p·e | Unami | `unm` | `unam1242` | [public] Autonym source: IG2021, p. 1. |
| Upper Michigan-Wisconsin Chippewa | — | — | `uppe1274` | [public] Dialect of Chippewa |
| Wampanoag · Cowesit · Massachusett · Natick · Massachusett, Natick · Wôpanâôt8âôk | Wampanoag | `wam` | `wamp1249` | [public] Autonym source: Wôpanâak Language Reclamation Project https://www.wlrp.org/ |
| West Innu · Western Montagnais | — | — | `west2627` | — |
| Western Abenaki · Western Abnaki · Alnôbaôdwawôgan | Western Abnaki | `abe` | `west2630` | [public] Autonym source: Wikipedia |
| Western Naskapi | — | — | `west2626` | — |
| Western Swampy Cree · nêhinawêwin, ᓀᐦᐃᓇᐌᐎᐣ | — | — | `west2628` | [public] Dialect of Swampy Cree but included here because there's a GC, [public] Autonym source: Wikipedia |
| Western York Cree | — | — | `west2629` | [public] Dialect of Plains Cree but included here because there's a GC |
| Winisk River Ojibwe · Winisk River Ojibwa | — | — | `wini1244` | — |
| Wiyot | Wiyot | `wiy` | `wiyo1248` | — |
| Woods Cree · Woodland Cree, Rock (Rocky) Cree · nîhithawîwin, ᓃᐦᐃᖬᐑᐏᐣ | Woods Cree | `cwd` | `wood1236` | [public] Autonym source: Wikipedia |
| Yurok | Yurok | `yur` | `yuro1248` | — |

† = **ISO 639-5 family code** rows (no 639-3 code exists; code from the data of record, labeled per its class):

- **alg**: ISO 639-5 family code — "Algonquian languages"; no ISO 639-3 code exists for Algonquian; carried from the data of record, labeled per class.
- **aql**: ISO 639-5 family code — "Algic languages"; no ISO 639-3 code exists for Proto-Algic; carried from the data of record, labeled per class.
- **alg**: ISO 639-5 family code — "Algonquian languages"; no ISO 639-3 code exists for Proto-Algonquian; carried from the data of record, labeled per class.

★ = **retired ISO 639-3 code element** (registry Retirements table):

- **mof**: ISO mof retired (effective 2010-01-18): split; [public] Used only if whole group cited; ISO code “mof” retired for Mohegan
- **pmk**: ISO pmk retired (effective 2023-01-20): crr; [public] GL treats this and Carolina Algonquian as the same; different ISO codes

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)

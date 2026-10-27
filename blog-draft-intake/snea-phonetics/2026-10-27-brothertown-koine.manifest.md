<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Intake manifest — snea-phonetics / 2026-10-27-brothertown-koine

Beside the verbatim copy (never inside it) per intake rule 3. Draft of
record: `snea-phonetics/blog-drafts/2026-10-27-brothertown-koine/`
("Where the words come from").

## Source

- **Repository:** `Brothertown-Language/snea-phonetics`
- **Drafts-folder path:** `blog-drafts/2026-10-27-brothertown-koine/`
- **Revision:** commit `12c31ae4eabbd2cb0e3050d9b82c2b37385834ee` (HEAD,
  "Merge pull request #150 … feature/blog-brothertown-koine"); draft files
  committed in `6d817b6` — clean, committed state, no uncommitted
  working-tree drift inside the draft folder at import time (2026-10-27).

## File inventory (checksums at import, before semaphore placement)

| File | sha256 |
|---|---|
| `article.md` | `010865664eb0b6302ccd30259c25e9548698da1dcc5f822b30868ab3855a6183` |
| `image-recommendations.md` | `063c25d5c52c07785d5c662f830056eb60a85a625d72a9d7a7efa573adb74b70` |
| `review-request-2026-10-27.eml` | `24d9aec9842e32c803f29898d0e4f8f9891f82ea23f7db0e5ddc63b5a0a2b7fc` |
| `send-verification.md` | `ba7fa8909c511b98ff089854895c3fdf53b97af0724dbb7655c4918b9137b656` |
| `sources-consulted.md` | `841399642574a61be3b3ba3eaa303c98f7bd0ae3b412d2c716637db25e46691f` |

Copy at `blog-draft-intake/snea-phonetics/2026-10-27-brothertown-koine/` —
byte-identical mirror taken before anything was placed upstream.

## Semaphore record

- `import-semaphore.md` placed upstream at
  `<snea-phonetics>/blog-drafts/2026-10-27-brothertown-koine/import-semaphore.md`
  after the copy was taken (order of record). Content: importing repo
  (`Brothertown-Language/brothertown-language-com`), UTC date (2026-10-27),
  received draft identity + `article.md` checksum. One-time receipt;
  never rewritten by this side; filesystem-only, never committed.
- Post-placement upstream check (2026-10-27): `git -C ../snea-phonetics
  status --porcelain` — exactly one untracked file, the semaphore under that
  draft folder, and no new modifications from this side. (The checkout
  carried pre-existing unrelated working-tree modifications — `CHANGELOG.md`,
  `blog-drafts/AGENTS.md`, `blog-drafts/README.md`, one `paper/` LaTeX file,
  one `  scripts/` file — present before this import; none were touched.)
  2026-10-27 note: upstream subsequently tracked this itself (snea-phonetics
  commit `f9a6927`, its #151 landing) — the above record predates that; this
  side still never commits or rewrites the receipt either way.)
- **Reconciliation (re-run walk, 2026-10-27):** claimed draft — semaphore
  present, checksum read twice across the re-run (`69301c408c02cead…90760cb5`,
  unchanged), never rewritten; verbatim copy still byte-identical for all
  five source files (`cmp` per file, 2026-10-27); this manifest updated in
  place — no duplicate manifest created; no re-import performed.

## Structural contract check (arrival state: unknown → checked)

| Check | Result |
|---|---|
| `article.md` at the sub-folder root | ✅ present |
| `<!-- more -->` fold present | ✅ present (between the intro paragraphs and `## The founders and the record`) |
| Supporting items the draft names present | ✅ `sources-consulted.md`, `image-recommendations.md`, `review-request-2026-10-27.eml`, `send-verification.md` |
| Images present-or-explicitly-declared | ✅ explicitly declared — no image files ship with the draft; `image-recommendations.md` names three license-verified Commons candidates with credit lines (primary: Williams 1643 title page, PD Mark 1.0) |
| Semaphore excluded from check | ✅ `import-semaphore.md` intentionally not counted (rule 5) |

**Result: contract satisfied; no structural blocker.**

## Arrival gaps as found (triage: agent-fillable vs blockers)

**Agent-fillable under this site's rules:**

1. No front matter at all (title/description/date/authors/tags) — article.md
   opens as handoff Markdown. → Conformance authors Zola TOML front matter.
2. Byline absent — draft is a project posting. → Project-only byline
   (`Brothertown Language`, per `docs/authors.md`; a project posting is not
   attributed to individuals as a writing credit — developer correction
   2026-10-27).
3. Handoff apparatus in the body: the top provenance/handoff comment block,
   the italic "for editorial review" line, and the editor-facing tracked
   anchors paragraph (marked strippable in the draft itself). → Stripped in
   the conformed derivative only.
4. Image selection not executed — declared candidates, no placed image. →
   Agent-editor pass selects from `image-recommendations.md`, verifies
   subject fit + license/credit, places per the site's image rules.
5. Site tags/hashtags absent. → Conformed per the tag rules of record;
   carrier-tag basis: **Turtle Island instance primary** (see conform
   section).

**Blockers requiring developer direction (do not block conformance; they
gate publication):**

1. Expert correctness review still in flight — draft was emailed 2026-10-27
   to Dr. Keith Cunningham, Dr. Craig Kopris, David Costa, and Spencer Conrad
   (review request in the draft folder) asking each explicitly to catch any
   passage overstating the provisional/gap-marked status. Publication waits
   for that disposition (plus the standing `draft = true` approval).
2. No Mastodon discussion post exists yet for this article — the back-link
   section's anchor URL is unknown at conform time; recorded as a gap in the
   conformed draft itself (HTML comment placeholder retained until the
   discussion post exists).

## Conform section

- **Conform pointer:** `content/blog/where-the-words-come-from/index.md`
  (rendered at `/blog/where-the-words-come-from/`), conformed 2026-10-27,
  `draft = true`. Initially landed as
  `content/blog/2026-10-27-where-the-words-come-from/`; renamed 2026-10-27
  (same session, post-review): Zola date-strips the folder name from URLs
  while `page.path` keeps the physical date-prefixed path, so the page's
  {{ page.path }}-referenced image 404'd — the R-9 shape
  (`content/blog/<slug>/`, date from front matter) resolves it; image
  requests   200-verified on the preview.
- **Publication status:** `draft = false` set 2026-10-27 on explicit
  developer instruction ("mark the article draft = false so the preview
  works") — the publication flip of record for this article; motive of
  record: Cloudflare PR previews cannot render a draft-flagged article
  (Workers Builds has no `--drafts` knob). Standing publish rule otherwise
  governs.
- **Edits applied to the derivative (and their basis):** front matter authored
  (TOML, bare-`Z` UTC date); byline registry-consistent (above); provenance
  comment block, draft-review italics line, and editor-facing anchors
  paragraph removed; image placed with credit caption per site's image
  placement pattern; hashtags line and `### Comment on Mastodon` back-link
  section added per the site's rules of record (root `AGENTS.md` Content
  rules); `<!-- more -->` fold repositioned to the standfirst (directly after
  the lede italics) per the site's summary pattern — developer review
  correction 2026-10-27: the draft's fold, three paragraphs in, sat too far
  down on the list page; no factual content authored — body text otherwise
  verbatim from the draft (R-8; wording left in the draft's own register,
  which already conforms). Image credit caption moved **inside** the
  `.imgfloat` container (page-level markup; `sass/abridge.scss` untouched,
  SC-8) after 1080p Playwright review — developer correction 2026-10-27:
  the caption, sitting outside the float, wrapped beside the tall title-page
  image on the front-page excerpt; inside the container it stays under the
  image on list and article pages alike.
  **Playwright 1080p review cycle (2026-10-27, continued):** (1) fold moved
  partway into the article proper — excerpt = standfirst + first two body
  paragraphs (~200 words), per the rule of thumb recorded in
  `docs/sop-site-setup.md` ("Blog images — crop, zoom, and front-fold
  layout"); (2) tall portrait image height-capped (`max-height: 20rem`,
  page-level inline style per the SOP's front-fold sizing rule);
  (3) caption legend reworded to name the work directly —
  "*A Key into the Language of America*, Roger Williams (1643) …" — no
  "Image:"/"Map:" filler legend (SOP credit-line register rule);
  (4) site-level CSS (`sass/abridge.scss`, developer-directed scope
  extension): `.sum { display: flow-root }` contains each excerpt's float;
  `.imgfloat em { display:   block }` gives the legend its own line; and the front-fold more-link
  redesigned as the centered `more ›` chip (`a.more-link` class + block CSS)
  — the bare `...more` anchor visually vanished against the excerpt text. Cropping
  and zooming blog images declared in scope for all blog articles going
  forward (developer instruction) — rules recorded in the SOP section above,
  referenced from `blog-draft-intake/AGENTS.md` rule 7.
- **Carrier-tag verification (2026-10-27, fresh signed-out API, 7-day
  history):**
  - **PRIMARY — Turtle Island instance (`turtleisland.social`, signed-out
    `GET /api/v1/tags/<tag>`):** `#Indigenous` 64 · `#Community` 186 ·
    `#Linguistics` 19 · `#Reconstruction` 1 · `#Brothertown` 0 ·
    `#LanguageRevitalization` 0 · `#Algonquian` 0 · `#SNEA` 0.
  - **SECONDARY — mastodon.social (site hashtag pages' carrier context):**
    `#Indigenous` 117 · `#Linguistics` 159 · `#Community` 1610 ·
    `#Reconstruction` 3 · `#Brothertown` 1 · `#LanguageRevitalization` 1 ·
    `#Algonquian` 1 · `#SNEA` 1.
  - **Analysis (primary basis weights the choice):** on the Turtle Island
    instance the audience-bearing carrier tags are `#Indigenous`, `#Community`,
    and `#Linguistics` — these carry volume there the way the research record
    shows they do on mastodon.social; `#Reconstruction` is marginal (1 use /
    7 days) and `#Algonquian`, `#Brothertown`, `#LanguageRevitalization`,
    `#SNEA` sit at 0 — quiet API volume does not exclude topic tags (tag rule
    of record), so the topic tags stay: `Brothertown`, `LanguageRevitalization`,
    `Algonquian`, `SNEA` describe the article's subject matter; `Linguistics`,
    `Indigenous` are the live carriers on both instances; `Reconstruction` is
    dropped as marginal on the primary basis and non-load-bearing on the
    secondary.
  - **Final tag set:** `Brothertown`, `Language Revitalization`, `Linguistics`,
    `Indigenous`, `Algonquian`, `SNEA` — one hashtag each in the article body
    (Mastodon-concatenated form in the hot-linked URL, e.g. `#LanguageRevitalization`),
    every hashtag hot-linked to its mastodon.social tag page.
- **Sensitivity/PII audit:** performed on the conformed body — no personal
  emails, addresses, or contact data; the review-request recipients appear
  only as professionally-named advisor reviewers in the intake records (this
  manifest and the verbatim draft copy), never in the conformed article.

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)
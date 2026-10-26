<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — Initial back-dated blog entry: Brothertown Community Language Initiative (brothertown-language-com #9)

## Problem

The new site's blog section is empty, and the project's founding public
statement exists only on the developer's personal site:
michael-conrad.com's "Brothertown Community Language Initiative" (published
2026-01-28 — the only Brothertown-language content there; the site's other
posts concern gamebooks/AI writing and are unrelated, fetched and checked
2026-10-26). The project blog should open with that announcement, on its
original posting date, in the project's own voice. Developer directives
(2026-10-26): back-date entries to the original posting date; content
restricted to Brothertown-language material (scope confirmed to the one
entry); project-voice adaptation with links back to the original as needed;
no date indications beyond the back-dated date; byline = one main author
plus guest authors Michael Conrad, Dr. Craig Kopris, Dr. Keith Cunningham
(project byline string per "shorter is better" = `Brothertown Language`;
config default unchanged); Jesse Bowman Bruchac cited in the body only; a
proper `/AGENTS.md` currency pass rides along.

## Scope

One blog entry as a Zola page bundle under `content/blog/`, publication to
built-output surfaces it inherits from the config of record (blog index,
atom feed, search index, authors facets), and the `AGENTS.md` currency pass.
Future posts, the non-Brothertown source posts, and any config change are
out of scope.

## Requirements

- **R-1** — The entry exists at
  `content/blog/brothertown-community-language-initiative/` as a page
  bundle: `index.md` plus the source post's tribal-territories map image in
  the bundle; the image ships with a visible credit that satisfies the
  image's source-license requirements (license and attribution verified
  against the image's source at implementation; exact credit string
  recorded in the PR).
- **R-2** — Front matter carries `date = 2026-01-28`, and no other date
  indication exists for the post: no `updated` key, no republished stamp in
  prose or front matter. The back-dated date is the post's public date.
- **R-3** — Authorship per the registry (issue #8): **main author**
  *Brothertown Language* (agent-authored default — the `zola.toml` `author`
  value stays exactly as-is), **guest authors** *Michael Conrad*, *Dr.
  Craig Kopris*, *Dr. Keith Cunningham*. Both Zola mechanisms carry the
  same four registry strings: the page's top-level `authors` list (feed
  author) and the page's `[taxonomies] authors` list (byline source — the
  theme's byline component loops `page.taxonomies.authors` — and facet
  source). **Authors-taxonomy templates ship here:** the vendored theme
  carries no authors term/list templates (categories/ and tags/ only —
  verified against the vendored tree and upstream), so Zola v0.23.6 fails
  the build with `taxonomy_single.html not found` once an authors term
  exists (empirically verified 2026-10-26 against the pinned build). This
  issue adds site-level `templates/authors/` (single + list) mirroring the
  theme's categories/tags templates; the vendored theme's own files are not
  modified. The built byline renders all four.
- **R-4** — The body is a **project-voice adaptation** that preserves the
  source's facts and section shape: call for collaboration; project goals
  (1000-word lexicon, grammar sketch, teaching materials — freely
  available); expert support; Proto-SNEA foundation and its source dialects
  (Mohegan, Pequot, Narragansett, Niantic, Tunxis, Montaukett); methodology
  (Minimal Course framework, Conor McDonough Quinn) and funding
  independence; how-you-can-help. It contains a **link-back to the original
  post** (https://michael-conrad.com/blog/brothertown-community-language-initiative/)
  as the first-publication record, without a date on that line; the
  source's Mastodon comment embed becomes a plain link to the original
  thread
  (https://mastodon.social/@michaelconrad/115971090611921901).
  Personal-blog framing is rephrased to the project's voice; no fact is
  added, dropped, or altered.
- **R-5** — The body credits the linguists with roles as the source does:
  Dr. Keith Cunningham (Language Keeper; lead linguist), Dr. Craig Kopris
  (advisor/contributor), Jesse Bowman Bruchac (advisor/contributor) — body
  credit only, never bylines.
- **R-6** — Taxonomy matches the source: category `Brothertown Language`;
  tags `Brothertown`, `Language Revitalization`, `SNEA`, `Community`.
- **R-7** — The post lands publishable (`draft` false — publication is the
  human's PR merge; no draft-flip occurs). AI-contribution marking follows
  repo convention: co-authored commit trailer; the project byline is the
  human-visible layer per the registry's role notes.
- **R-8** — The `AGENTS.md` currency pass: the "Current state: bootstrap —
  conventions and docs only" header reflects the landed, live site (base
  site landed via issue #1; hosted on Workers Static Assets); the Commands
  section drops its "(after issue 1 lands)" parenthetical; the Content-rules
  line names `zola.toml` (currently `config.toml`). Nothing outside those
  lines plus issue #8's pointer bullets changes.

## Success criteria

| ID | Criterion | Class | Instrument |
|----|-----------|-------|-----------|
| SC-1 | `./build.sh` exits 0 and `public/blog/brothertown-community-language-initiative/index.html` exists | behavioral | run `./build.sh`; assert exit 0; assert the file exists |
| SC-2 | The built post's byline renders all four author strings (`Brothertown Language`, `Michael Conrad`, `Dr. Craig Kopris`, `Dr. Keith Cunningham`) | behavioral | extract the author/byline markup from the built post page; assert all four strings appear within it |
| SC-3 | The authors facets render: the `/authors/` taxonomy index plus a term page for each of the four registry keywords, each term page linking the post | behavioral | assert `public/authors/index.html` and `public/authors/<keyword>/index.html` for each of the four keywords; assert each term page links the post |
| SC-14 | Site-level `templates/authors/` term and list templates exist, mirroring the theme's categories/tags pattern; the vendored theme's files are unchanged | structural | file check of the added templates + `git status`/diff shows no modifications under `themes/abridge/` |
| SC-4 | Front matter date is 2026-01-28 and no other date indication exists in the post's source | structural | file check: `date` set to 2026-01-28 in unquoted TOML date form; no `updated` key; no other date strings in front matter or body |
| SC-5 | Taxonomy matches R-6's set | structural | file check of front matter |
| SC-6 | The body contains a link-back to the original post URL | structural | file check for the URL in the post source |
| SC-7 | No embedded comment block; a plain link to the original Mastodon thread is present | structural | file check: no embed markup; anchor to the thread URL present |
| SC-8 | The body preserves the source post's project facts (goals, experts and roles, Proto-SNEA stage, source dialects, methodology, funding stance, volunteer asks) | structural | reviewer comparison of the body against the live source page (fetched at verification) |
| SC-9 | The map image ships in the bundle with a visible, license-conformant credit near it | structural | built-output check (image file under the post path) + content check of the post source for the credit line |
| SC-10 | The `AGENTS.md` currency pass is applied within R-8's stated line scope | structural | content check + `git diff` scope check |
| SC-11 | The built blog index lists the post | behavioral | built `blog/index.html` contains the post's link |
| SC-12 | The built atom feed contains the post entry | behavioral | built `atom.xml` contains the entry |
| SC-13 | The built search index contains the post | behavioral | built `search_index.en.json` contains the post |

## Edge cases

- **Feed behavior on the back-dated date**: Zola includes all posts in the
  feed regardless of date ordering; the 2026-01-28 date does not exclude the
  entry. Verified as part of SC-12 rather than assumed.
- **Slug stability**: the registry keywords (issue #8) are the expected
  facet slugs; if Zola's slugification of a display string differs (e.g.
  punctuation handling), the registry is corrected in the same PR — facets
  must exist for all four authors either way (SC-3). No page-level styling
  variance is permitted (R-3).
- **Authors taxonomy and bylines are one mechanism here**: the `authors`
  list drives both; no separate tags for authors are added to this post for
  the byline effect (author-facet needs are satisfied by SC-3). Ad-hoc
  author-mention tagging remains available per the registry's rules but is
  not required by this post.
- **Publish gate**: landing the post with `draft = false` in the PR is not a
  draft-flip; the human merge is the publish instruction.
- **Feed author behavior** (verified empirically against the pinned Zola
  v0.23.6 binary, 2026-10-26 clean-room differential; Zola's current web
  docs state a first-author-only rule that does NOT match the pinned
  binary): a feed entry renders `<author><name>` for every entry of the
  page's top-level `authors` list — the post's feed entry credits all four
  registry strings — falling back to the config `author` when the field is
  absent. abridge ships no custom feed template, so the behavior comes from
  the binary. Feed entry listing all four authors is the intended outcome;
  no success criterion depends on a single-author feed.
- **Two author mechanisms, one value set**: the top-level `authors` field
  (feed author) and the `[taxonomies] authors` key (byline + facet source)
  are distinct in current Zola; this post carries both with identical values
  so byline, feed authorship, and facets all render from the same registry
  strings.
- **Authors taxonomy rendered only once terms exist** (empirically verified
  2026-10-26 against the pinned Zola v0.23.6 + vendored theme): the base
  site built cleanly with the empty authors taxonomy; a page introducing
  authors terms makes Zola render term (and list) pages, which fail without
  templates — hence R-3's template requirement. The theme's byline, by
  contrast, already handles multiple authors (it loops
  `page.taxonomies.authors`), so no byline override is needed.

## Out of scope

- The source site's non-Brothertown posts (2024 gamebook/AI entries) and
  its generated gamebook tree.
- Future blog posts or content sections (dictionary, lessons, apps,
  methodology).
- Any `zola.toml` change (the default author string is correct as-is).
- Cloudflare dashboard operations (runbook-governed, developer-run).
- Republishing the original's text verbatim (the adaptation is the
  deliverable; verbatim syndication was considered and rejected in
  exploration).

## Approach

Port the founding announcement as the project's founding post: same facts,
project voice, registry-consistent byline, the source's date honored, and
provenance carried by the link-back rather than the byline. The registry
(issue #8) supplies the canonical name strings; this issue consumes it.

## Dependencies

- `brothertown-language-com#8` (author registry) — provides the byline
  strings and keyword record; lands before or with this issue in the same
  PR scope.
- The blog section, `authors` taxonomy configuration, and feeds from issue
  #1's landed base site (merged, PR #7): only the taxonomy *configuration*
  landed there — the term-page templates the facets need do not exist
  anywhere (site or theme) and ship under this issue's R-3.

## References

- Source of record: "Brothertown Community Language Initiative",
  https://michael-conrad.com/blog/brothertown-community-language-initiative/
  (published 2026-01-28; fetched in full 2026-10-26 — the exploration's
  listing). Its Mastodon discussion thread:
  https://mastodon.social/@michaelconrad/115971090611921901.
- Developer authorship decisions, 2026-10-26: project-voice adaptation with
  links back only; back-dated date, no other dates; "shorter is better"
  (byline string `Brothertown Language`); guests Michael + Craig + Keith;
  "Dr." styling per developer correction; agent-authored materials carry
  the project byline (the byline is the AI-marking layer).
- Repo content rules: draft-gate, image-path existence, AI-contribution
  marking (README/AGENTS.md); issue #1's SOP publish procedure.
- Registry spec: `brothertown-language-com#8` (byline strings, keywords).

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
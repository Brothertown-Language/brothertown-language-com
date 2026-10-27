<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Standing rules — blog-draft-intake

These rules bind every agent working in this folder. They govern the intake's
own mechanics; the site's posting rules are the repository's rules of record
and are pointed at, not restated (root `AGENTS.md` Content rules,
`docs/authors.md`, `docs/sop-site-setup.md`).

1. **On demand only.** The import walk runs when the developer says so. No
   standing scan, no scheduled automation, no background sync.
2. **Verbatim copies, untouched originals.** Draft folders are copied exactly
   as handed over, byte-identical, before anything else. The upstream
   repository is never modified by this side except by the semaphore
   placement (rule 5). The conformed article is a derivative in the Zola
   source tree — never an edit of the upstream original or the intake copy.
3. **Unknown arrival state: manifest + triage, no silent repair.** Arrival
   state is never assumed complete or correct. Every import records a
   manifest beside the copy (source repo and drafts-folder path; source
   revision — commit SHA or dated uncommitted-working-tree state; file
   inventory with checksums; structural contract-check result; arrival gaps
   as found). Manifests sit beside the copy, never inside it. No gap found at
   import is repaired in the copy or upstream; triage classifies gaps as
   agent-fillable under this site's rules versus blockers requiring the
   developer's direction.
4. **The agent does not author facts.** Every factual claim in a conformed
   article traces to the imported draft's tracked evidence (`article.md`,
   `sources-consulted.md`, or the anchors those cite). Substantive
   disagreements between the editor and the draft are flagged in review,
   never silently resolved; wording edits are limited to conforming the piece
   to the site's register.
5. **Semaphore: one-time receipt, filesystem-only.** `import-semaphore.md`
   is placed in the upstream draft folder at import, naming the importing
   repository, the UTC date, and the received draft identity. Placed once,
   never rewritten, never evolved in state. It is never committed, staged, or
   rewritten by this side, and may be undone by deleting the uncommitted
   file. A draft folder already carrying a semaphore is claimed: reconcile
   the existing manifest, do not re-import unless instructed. The contract
   check ignores the semaphore.
6. **`draft = true` until explicit approval.** Every conformed article lands
   as `content/blog/<slug>/index.md` with `draft = true` and stays that way
   until explicit developer approval flips publication. A draft that cannot
   be fully conformed does not block the flow: conform what stands, record
   the gaps (in the manifest and as an HTML comment between the front matter
   and the body of the conformed draft), and hold the draft in the tree —
   `zola serve --drafts` shows every state.
7. **Conformance is agent-editor work, not a script.** Front matter,
   bylines, tags (with the fresh carrier-tag verification recorded
   in the manifest), hashtags, the discussion back-link, image selection and
   license/credit verification, and the sensitivity/PII audit are judgment
   steps performed by the agent as editor. No script encodes image choice,
   tag text, voice, or any judgment step. Conformance applies the
   repository's rules of record by path — never restate them here.
   **Carrier-tag analysis basis (developer ruling, 2026-10-27):** primary
   sourcing and counting for carrier-tag verification runs against the
   Turtle Island Mastodon instance — `turtleisland.social` ("Turtle Island
   Social"), signed-out `GET https://turtleisland.social/api/v1/tags/<tag>`
   reading the tag's 7-day `history`. The mastodon.social check (the basis
   named in the root `AGENTS.md` hashtag rule) is recorded as secondary
   context — the published hashtag links hot-link to mastodon.social tag
   pages — but tag-text choices and volume evidence are prioritized on the
   Turtle Island instance. Both checks' evidence goes into the manifest's
   conform section, re-run fresh at each conform pass.
   **Front-fold layout (2026-10-27 review rulings):** the excerpt fold and
   image display follow the site's image/layout rules in
   `docs/sop-site-setup.md` ("Blog images — crop, zoom, and front-fold
   layout"): cropping and zooming blog images in scope for every article
   going forward; the fold lands partway into the article proper (~150–250
   words of excerpt text at the first paragraph break); portrait plates
   height-capped (max-height ≈ 20 rem); captions name the work directly,
   with no "Image:"/"Map:" filler legend.
8. **Human gates.** Publication approval and merge are human gates. The agent
   issues neither; agents open PRs after the repository's pre-PR review gate
   (`docs/sop-site-setup.md`), humans merge.
9. **Register additions are developer-supplied.** `register.md` lists only
   repositories the developer adds; it is never extended by discovery or best
   guess.
10. **Upstream boundary.** Nothing is ever committed to an upstream sibling
    repository from this side (semaphore convention; companion spec
    `snea-phonetics#151` governs that side's records).

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)

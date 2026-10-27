The blog-posting standards established on michael-conrad.com (2026-10-27, issue michael-conrad/michael-conrad.com#6) need adoption here so both project sites share them: the site/social tag convention with hot-linked Mastodon hashtags, the non-self-centered community voice rule, the TOML bare-Z front-matter date rule, the backgrounded `--drafts` preview convention, and a domain-aware build. Problem: this repo's AGENTS.md records none of the four conventions, its `Preview:` line documents plain `./zola serve`, and `build.sh` has no `--base-url` handling — so future posts here would diverge from the standards (and Workers Builds previews would production-link, the exact defect fixed on the sibling site).

## Scope

- AGENTS.md (Content rules, Preview line, build note), `build.sh`, `docs/cloudflare-facts.md` (one dated facts row). No content changes (blog empty); no page-creation script port (`local_util` does not exist here — that workflow's script is this repo's choice to make separately).

## Requirements

- **R1** — Content rules SHALL record the site/social tag convention (site tags = populated per-page TOML `tags` keywords; social hashtags `#TagText`, one per site tag, hot-linked to `https://mastodon.social/tags/<tagtext-lowercase>` appended after the sign-off and before the byline; reach carriers verified via the signed-out Mastodon API `api/v1/tags/<tag>` history — uses > 0; topic tags reflect the article regardless of volume; identity carve-outs documented), including the 2026-10-27 research record (OpenSource 6637, Linguistics 151, Indigenous 104; revitalization/reconstruction/Algonquian-family tags 0).
- **R2** — Content rules SHALL record the voice rule (community-facing posts avoid "me me me" first-person singular; project voice "we/the project", author by name/role, "our" for community/heritage).
- **R3** — Content rules SHALL record the TOML date rule: front-matter `date` uses the bare-`Z` UTC form (`YYYY-MM-DDTHH:MM:SSZ`), never offset-plus-`Z`.
- **R4** — The `Preview:` line SHALL document the backgrounded `./zola serve --drafts` convention with `xdg-open` display (integrating with the SOP's pre-PR review gate — serve then present per `docs/sop-site-setup.md`).
- **R5** — `build.sh` SHALL support a domain-aware build: when `SITE_BASE_URL` is set, build with `--base-url "$SITE_BASE_URL"`; otherwise build exactly as today. `docs/cloudflare-facts.md` SHALL gain a dated row recording the verified Workers Builds default env vars (`CI`, `WORKERS_CI`, `WORKERS_CI_BUILD_UUID`, `WORKERS_CI_COMMIT_SHA`, `WORKERS_CI_BRANCH` — source: cloudflare.com changelog 2025-06-10, fetched 2026-10-27) and the fact that **no deployment-URL variable exists** (CF_PAGES_URL is Pages-only; `SITE_BASE_URL` is the repo's optional override knob). AGENTS.md build note updated.
- **R6** — The SOP's pre-PR review gate is unchanged (serve → present → PR per record); R4 only documents the serve mechanics.

## Impact

Docs + one build script; zero content or template changes. Local/production builds byte-identical when `SITE_BASE_URL` is unset. The facts row keeps `docs/cloudflare-facts.md` current per its own rule.

## Success criteria

| ID | Class | Criterion |
|---|---|---|
| SC-1 | structural | AGENTS.md carries R1–R4 recordings and the R5 build note; `docs/cloudflare-facts.md` carries the dated R5 row |
| SC-2 | behavioral | Default build (`SITE_BASE_URL` unset) exit 0, byte-consistent output behavior |
| SC-3 | behavioral | Override build (`SITE_BASE_URL=https://<preview>.pages.dev ./build.sh`) self-links interpolated/feed surfaces to the override domain |
| SC-4 | structural | No other files modified; SOP gate text unchanged |

## Out of scope

- Porting `local_util/new_page.py` or the `mastodon_posts.md` pairing ledger (separate adoption decisions for this repo); blog content; theme/template changes; the michael-conrad.com canonization (own spec there).

## Approach

1. Register remote + local mirror; persist the spec; run the spec validation loop.
2. Branch `feature/17-blog-posting-conventions`; edit AGENTS.md, build.sh, docs/cloudflare-facts.md.
3. Verify SC-2/SC-3 with build simulations; serve the site and present the preview (the SOP's pre-PR gate); PR after the presented review.

> Full spec and plan artifacts: https://github.com/Brothertown-Language/brothertown-language-com/tree/issues-data/17/

Agent artifacts pointer: `.issues/17/`

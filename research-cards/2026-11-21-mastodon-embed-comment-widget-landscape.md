---
id: 2026-11-21-mastodon-embed-comment-widget-landscape
question: Is there a better widget form possible for the "Comment on Mastodon" section (plain anchor per SOP Content rules rule 5) on this site's blog posts?
confidence: 0.85 (all mastodon.social API/embed facts live-probed this session; the static-site pattern write-ups fetched; SocialHub fediverse-embed unverified; rate-limit docs dated 2022)
---

# Mastodon embed + static-site comment-widget landscape (2026-11-21)

Session context: developer question about the current widget — `### Comment on Mastodon` + "You can comment on this post via Mastodon: [View on Mastodon](url)." — mandated verbatim by SOP Content rules rule 5; the embed was rejected in issue brothertown-language-com#9 (SC-7). Thread of record: mastodon.social/@michaelconrad/117624227198231767 (public; 1 reply — the project account's own 2026-11-16 correction note). Current wording rule means ANY form change = SOP rule-5 revision mirrored in AGENTS.md, through spec.

## Mastodon embed surfaces — live-probed 2026-11-21 (mastodon.social running 5.0.0-nightly.2026-11-20)

- **oEmbed** (`GET /api/oembed?url=…`) → `type: rich`, html = `<blockquote class="mastodon-embed" data-embed-url="…">` whose no-JS fallback content is a Mastodon SVG logo + "Post by @michaelconrad@mastodon.social" + bold "View on Mastodon" anchor, followed by `<script async src="https://mastodon.social/embed.js">`. i.e. **the official no-JS degradation is exactly a styled version of our current plain link.** https://docs.joinmastodon.org/methods/oembed/ (docs example shows an iframe form that contradicts live output — stale).
- **embed.js** (source: mastodon/mastodon `public/embed.js`) swaps the blockquote for an interactive iframe of the `/@user/:id/embed` route, auto-height via postMessage. `/embed` route frameable (CSP without frame-ancestors, no X-Frame-Options; cache-control 180 s public; body is a JS shell). Requires executing third-party script/iframe — the class #9 SC-7 rejected. Renders the announcement toot, NOT the replies.
- **No oEmbed/embed removal in 4.3→5.0β release notes** (v4.3.0 2024-10-08 "embedded posts use web UI"; v4.4.0 2025-07-08 FEP-044f quote groundwork; v4.5.0 2025-11-06 quote posts shipped; v4.7.6 latest stable 2026-11-19; v5.0.0 beta only). https://github.com/mastodon/mastodon/releases
- **Quote posts exist since 4.5 (Sept 2025 on mastodon.social)** — context-endpoint widgets miss quotes; Bridgy Fed quote bridging is FEP-e232 only (issue #1956).

## Public API facts for a widget — live-probed 2026-11-21

- `GET /api/v1/statuses/:id` and `/…/context` — **readable unauthenticated** for public statuses (context cap: 40 ancestors / 60 descendants / depth 20; docs.joinmastodon.org/methods/statuses).
- **CORS: `Access-Control-Allow-Origin: *` on `/api/*`** (probed with foreign Origin; source of record config/initializers/cors.rb, rack-cors, origins '*'). Client-side fetch from the site's origin works.
- **Anonymous rate limit 300 req / 5 min per IP** (`x-ratelimit-limit: 300` observed); responses carry ETag (304 verified) + `cache-control: max-age=15, public, stale-while-revalidate=30, stale-if-error=86400`.
- Mastodon 4.5+ adds experimental `Mastodon-Async-Refresh` backfill on context queries.
- Reply HTML is untrusted markup — every current implementation sanitizes or flattens to text.

## Static-site widget patterns (current wave 2025–2026)

- **Client-side fetch of `/context`** — dominant pattern (Carl Schwan 2020 lineage). Current/maintained: dpecos/mastodon-comments webcomponent (repo pushed 2026-03-31); Zola walkthrough fbanning.de/thoughts/mastodon-comments-on-zola-blog/ (shortcode + click-to-load + `<noscript>` fallback pointing at the thread); fullast.nu two-part ops deep-dive (2026-10/11) incl. threading, 10-s timeouts, 200-reply cap, strict CSP; burnt.place hybrid (2025-10) adds Cloudflare-KV anon comments.
- **Build-time pull-and-bake** (fully static, zero JS): Winterstein Zola (2025-02, https://www.winterstein.biz/blog/static-comments-for-static-website/) — script writes replies as content shortcodes, GitHub Action commits + PRs daily; pomnavi Astro (2025-12, repo naivchan/astro-static-comments). Caveat: snapshot goes stale until next rebuild; build couples to mastodon.social availability.
- **Official embed** (blockquote+embed.js or iframe) = interactive but script/iframe-executing, announcement-only, essentially undocumented.
- **Bridgy Fed** (active, pushed 2026-11-21): site bridged as fediverse actor; replies/likes/boosts return as **Webmentions** — needs a Webmention endpoint (backend-less static site would need a Worker). https://fed.brid.gy/docs
- **SWF ap-components** (npm, pushed 2026-11-20): custom elements for AS2 objects; README documents CORS/authorized-fetch friction.

## Gaps / not verified

- SocialHub `<fediverse-embed>` proposal thread: NOT found in any search — unverified; nearest artifact is SWF ap-components.
- Web-UI "Get embed code" output vs oEmbed serializer: presumed identical, unverified. Anonymous context cap observed only on a 1-reply thread; 4.5 backfill header not observed live.
- Rate-limit docs page dated Nov 2022; instance overrides beyond observed 300-headers can't be ruled out.
- Dan Q's full write-up not located (gist only). heartsoulmachine.com / WordPress Fediverse-Embeds plugin snippet-verified only.

## Synthesis

Design space for the site: (A) status quo — zero exec, wording fixed by rule; (B) self-styled no-JS card (site-owned markup mirroring Mastodon's own fallback: glyph + attribution + View-on-Mastodon anchor; optionally a build-time-baked reply count — build.sh already has network access for the Zola download); (C) official embed — the rejected class, worst fit (script/iframe + announcement-not-comments + undocumented); (D) client-side replies widget (noscript fallback = current link; visitor IP surfaces to mastodon.social; text-only rendering; cap 40/60/20 plenty at this scale); (E) build-time baked replies (static, but stale-until-rebuild + build coupling). The 2026-11-21 thread contains exactly one reply (the project's correction note), so D/E's added value is prospective until community discussion accumulates. Any adoption = SOP rule-5 revision + spec.

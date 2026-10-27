<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# AGENTS.md — docs/ tree

Guidance for agents working under `docs/` (scoped file for this directory).

## What this directory is

Operational and reference documents only — **not site content**. Zola
builds `content/` and ignores this tree; nothing here has front matter,
templates, or build behavior. Never place site pages here; site pages go
under `content/`.

## Documents of record in this tree

| Document | Role |
|----------|------|
| `sop-site-setup.md` | The site setup and maintenance SOP — local tooling loop, Zola pin, delegated cloud-side deployment, verification gates, publish procedure. |
| `authors.md` | The author-keyword registry of record (issue `brothertown-language-com#8`). Every bylined, faceted, or cited author name is registered here first. |
| `languages.md` | The languages lookup table (same registry pattern, ISO-registry ground; issue #8). Cited language forms use its "Common [iso]" convention. |

## Conventions

- SPDX header (copyright + license comment) at the top of every doc.
- Changes go through feature branches and PR review like any tracked file.
- **Registry-first**: an author keyword is minted only in `authors.md`, and
  a language row only in `languages.md` — never ad hoc on a content page.
  A name/row lands in the same PR that first cites it.
- The registry's **coupling rule** applies: display strings are the tag
  source; restyling an author or language name moves facet URLs and happens
  only by editing the registry, never on pages.
- Cited-form convention for languages: `Common [iso]` — e.g.
  *Mohegan-Pequot* [`xpq`] — drawn from `languages.md`'s columns.

---

Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)
<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# AGENTS.md — referenced-projects

This folder holds **gitignored reference checkouts** of companion
repositories. They are references only — never build-time dependencies: this
site's build (`./build.sh`, vendored Zola) consumes nothing from them, and no
submodule is ever created here.

## Registry of record

Clone URL is pull-only (https): a push into a referenced repository cannot
succeed from a checkout made per this table.

| Folder | Pull-only clone URL | Reference purpose | Status |
|---|---|---|---|
| `snea-phonetics` | `https://github.com/Brothertown-Language/snea-phonetics.git` | Research/paper of record; blog-drafts source of record | floating |
| `snea-grammar` | `https://github.com/Brothertown-Language/snea-grammar.git` | Grammar knowledge base; exports-contract reference | floating |
| `snea-lib` | `https://github.com/Brothertown-Language/snea-lib.git` | Derivation-library reference | floating |
| `algonquian-library` | `https://github.com/Brothertown-Language/algonquian-library.git` | Comparative corpus substrate | floating |
| `snea-shoebox-editor` | `https://github.com/Brothertown-Language/snea-shoebox-editor.git` | Tooling reference | floating |

## Checkout instructions

- Create a checkout **only when needed** — never at repo clone time:
  `git clone --depth 1 <pull-only-url> referenced-projects/<folder>`
- Checkouts are **shallow** (`--depth 1` as shown) — do not deepen a checkout
  unless the work in hand requires history.
- Checkouts are **gitignored**: this repo's `.gitignore` ignores
  `referenced-projects/*` except this governing file. A checkout is never
  committed, staged, or pushed as part of this repository.

## Reference-only rules

1. **Read-only.** Never commit inside a checkout, never push from one, never
   edit a checkout's files as a way of working on this repo.
2. **No build against them.** Build and verification run only through this
   repo's own documented build (`./build.sh`). A referenced checkout is never
   an input, include path, or build dependency.
3. **Absence is never a build failure.** Nothing in this repo requires
   `referenced-projects/` to be populated; its absence or staleness fails
   nothing.
4. **`glob` false-absence.** Ignored checkouts are invisible to the `glob`
   tool — "no files found" there is false absence; discover contents with
   `grep`, `read`, or `bash`.
5. **Provenance.** Any content in this repository derived from a checked-out
   repository records the source repository and the SHA it was read at, in
   the content or its commit message — the gitignored checkout carries no
   pointer identity, so the citing record is the reference of record.

## Registry maintenance

Adding or removing registry rows is an in-place edit of this file through the
normal PR review path — no new spec is required for registry row edits.

---
Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)

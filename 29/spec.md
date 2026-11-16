<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — brothertown-language-com#29: `referenced-projects/` reference-checkout convention with governing AGENTS.md registry

Authorization: spec stage only; plan and implementation await developer approval. Request quote (developer, 2026-11-16): "it would be best to have a referenced projects folder with an AGENTS.md that lists the referenced repos with pull only URLs that the agent can checkout when needed. the agents.md should clearly list the referenced projects and provide the needed instructions on ignoring the checked out referenced projects and that the checkouts should be shallow."

## Problem

This repo has no mechanism for referencing the companion research repositories. Work here — blog finalization, future content surfaces — needs read access to those repos for reference purposes, without declaring them build dependencies: the build (`./build.sh`, vendored Zola) consumes nothing from them. Survey (2026-11-16): the snea-* family mounts `corpus`/`snea-lib` as real build-time submodules; no repo in the ecosystem carries a reference-checkout convention, so this establishes one.

Design choice of record (developer, this session): an **ignored-checkout folder**, not submodules — the goal is explicitly to prevent the referenced repos from being treated as dependencies.

## Scope

This repo only: `referenced-projects/` (folder + governing `AGENTS.md`), `.gitignore` wiring, and one minimal cross-reference line in the root `AGENTS.md`. No checkouts performed by the implementing change; no other repo modified; no submodule created.

## Requirements

- **R-1** `referenced-projects/` SHALL exist at the repo root, tracked, containing only the governing file. Per-project checked-out folders appear under it only when an agent checks one out for reference.
- **R-2** `referenced-projects/AGENTS.md` SHALL carry a registry row per referenced project: local folder name, pull-only clone URL (`https://github.com/Brothertown-Language/<repo>.git` — https so a push cannot succeed), what the repo is referenced for, and pin/floating status. Initial registry (floating all):
  | Folder | Pull-only clone URL | Reference purpose | Status |
  |---|---|---|---|
  | `snea-phonetics` | `https://github.com/Brothertown-Language/snea-phonetics.git` | Research/paper of record; blog-drafts source of record | floating |
  | `snea-grammar` | `https://github.com/Brothertown-Language/snea-grammar.git` | Grammar knowledge base; exports-contract reference | floating |
  | `snea-lib` | `https://github.com/Brothertown-Language/snea-lib.git` | Derivation-library reference | floating |
  | `algonquian-library` | `https://github.com/Brothertown-Language/algonquian-library.git` | Comparative corpus substrate | floating |
  | `snea-shoebox-editor` | `https://github.com/Brothertown-Language/snea-shoebox-editor.git` | Tooling reference | floating |
- **R-3** The governing file SHALL instruct: checkouts are created only when needed (never at repo clone time); they are shallow (`git clone --depth 1 <pull-only-url> referenced-projects/<folder>`); they are gitignored, never part of this repository.
- **R-4** `.gitignore` SHALL ignore `referenced-projects/*` with `!referenced-projects/AGENTS.md` — checkouts never tracked, registry tracked.
- **R-5** The governing file SHALL state the reference-only rules: read-only checkouts (no commits into them), no build against them (build/test route through this repo's `./build.sh` only), the folder's absence is never a build failure, the `glob` false-absence discipline for ignored checkouts, and provenance — any content here derived from a referenced checkout records the source repository and the SHA it was read at, since the checkout carries no pointer identity.
- **R-6** Registry additions/removals are in-place edits of `referenced-projects/AGENTS.md` through normal PR review; this spec fixes the initial set only, and no further spec is required for registry row edits.
- **R-7** The repo root `AGENTS.md` SHALL gain one brief, minimal cross-reference line naming `referenced-projects/` and pointing at its `AGENTS.md` as the governing registry, so agents arriving only at the root know the folder exists. The line duplicates no registry content — no URLs, no checkout instructions, no per-project rows.

## Success criteria

| ID | Class | Criterion | Instrument |
|----|-------|-----------|------------|
| SC-1 | structural | `referenced-projects/AGENTS.md` exists; one registry row per R-2 project, each with folder name, pull-only https URL, purpose, pin/floating status | read the file, check every R-2 row |
| SC-2 | structural | Checkouts under `referenced-projects/` ignored; governing file tracked | in a scratch checkout: `git check-ignore referenced-projects/snea-phonetics` exits 0; `git check-ignore referenced-projects/AGENTS.md` exits 1 |
| SC-3 | content | Governing file states checkout-when-needed, `--depth 1`, gitignored, and all R-5 reference-only rules | read the file |
| SC-4 | structural | Site build unaffected | `./build.sh` completes; ERROR-class output respected |
| SC-5 | structural | Root `AGENTS.md` carries the minimal cross-reference (folder named, governing file pointed at, no duplicated registry content) | read the root `AGENTS.md` line; diff confirms it is one line |

## Out of scope

- Performing any checkout (agents do that at need, guided by the governing file).
- Submodules or build-time consumption; dictionary/lesson data decisions land separately.
- Root `AGENTS.md` beyond the single R-7 cross-reference line (no layout-table rewrite, no registry duplication); any companion-repo change.

## Approach

Create folder + governing `AGENTS.md` (R-2/R-3/R-5) + `.gitignore` wiring (R-4) + root cross-reference line (R-7); verify SC-1–SC-5; pre-PR served-preview gate before any PR.

## Impact

Agents gain a governed reference path (discoverable from the root `AGENTS.md`); the tracked tree gains `referenced-projects/AGENTS.md`, two `.gitignore` lines, and one root cross-reference line; build surface unchanged. No dependency introduced, by design.

---
Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)

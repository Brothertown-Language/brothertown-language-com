<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# Plan — brothertown-language-com#29: referenced-projects/ convention

Source: `.issues/29/spec.md` (validated PASS, round 3). Branch: `feature/29-referenced-projects` (created 2026-11-16, trunk tip a18de4d).

| # | Item | Implements | Verify (instrument) |
|---|------|------------|---------------------|
| 1 | Create `referenced-projects/AGENTS.md` — registry table (R-2's five rows), instructions (R-3: when-needed, `--depth 1`, gitignored), reference-only rules (R-5: read-only, no build against, absence never builds fails, glob false-absence, provenance SHA) | R-1, R-2, R-3, R-5, R-6 | SC-1, SC-3 — read the file |
| 2 | `.gitignore`: `referenced-projects/*` + `!referenced-projects/AGENTS.md` | R-4 | SC-2 — `git check-ignore` exits 0 for checkout path, 1 for governing file |
| 3 | Root `AGENTS.md`: one minimal cross-reference line | R-7 | SC-5 — diff shows one line added |
| 4 | Build unaffected | — | SC-4 — `./build.sh` completes, no new ERROR-class output |

No test files created (convention/docs change; SC instruments are reads, git check-ignore, build run). Pre-PR: served-preview review gate before `gh pr create`.

---
Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)

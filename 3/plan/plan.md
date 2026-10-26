<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Plan — brothertown-language-com#3 — Cloudflare Workers setup runbook (wiki page set)

Derived from the validated spec (`.issues/3/spec.md`, approved through PR
boundary by developer directive 2026-10-26). Two surfaces carry the deliverable:
the repository wiki (17 of the 18 SCs) and a single repo-side footprint — the
`wiki/` gitignore entry the checkout provisioning requires (SC-1's repo clause).
The wiki is direct-publish, so its own review gate is verify-before-push; the
PR carries the repo-side footprint only.

## Items

### Item 1 — Branch + repo-side `wiki/` gitignore entry (SC-1 repo clause)

- **Deliverable** — branch `feature/3-cloudflare-workers-runbook` off trunk tip
  `028d160`, and `.gitignore` gaining `wiki/` (with a comment line), **before**
  any clone lands at `wiki/`.
- **RED** — `.gitignore` carries no `wiki/` entry (verified 2026-10-26).
- **GREEN** — edit `.gitignore` on the branch; conventional commit
  `chore(#3): gitignore wiki checkout`.
- **Instrument** — `git check-ignore -v wiki/` resolves; `git grep -n wiki
  .gitignore` shows the entry.

### Item 2 — Provision the `wiki/` checkout (SC-1 instrument context)

- **Deliverable** — clone
  `Brothertown-Language/brothertown-language-com.wiki.git` to `wiki/` after the
  ignore entry lands; no `.gitmodules` entry.
- **RED** — no checkout exists at `wiki/` (verified 2026-10-26); `gh api` has
  already confirmed `has_wiki: true` (spec facts table).
- **GREEN** — `git clone <wiki-remote> wiki`.
- **Instrument** — `git -C wiki remote -v` names the wiki remote; `.gitmodules`
  absent from the parent repo.

### Item 3 — Author the page set: `_Sidebar.md`, `Home.md`, and the five runbook pages (SC-2–SC-12, SC-14, SC-16, SC-17)

- **Deliverable** — seven wiki files exactly as R-1 names them, content per
  R-2–R-12: overview (prerequisites + blast radius + executor split + rollback
  availability), build pipeline, domain + HTTPS, rollback + teardown, facts
  log. Every operative fact carries an inline primary-source URL + 2026-10-26
  verification date; every decision point is condition → branch with deciding
  evidence; every step carries an executor mark; `[[Page Name]]` links only;
  no frontmatter; no open "adjust as appropriate" language; pages
  self-contained per phase.
- **RED** — the wiki (freshly cloned) carries no page set: `git ls-files` in
  `wiki/` lists none of the seven files.
- **GREEN** — write the seven files on the wiki checkout's default branch
  (`master`).
- **Verbatim source of record** — the spec's Facts of record table (all URLs
  and dates verified live 2026-10-26); content is composed from that table,
  not re-researched.

### Item 4 — Verify-before-push review, then publish (SC-13 noted, SC-18)

- **Deliverable** — the publish-discipline gate run over the staged diff:
  (a) full `git diff` read; (b) `[[...]]` target sweep — all targets resolve to
  the seven page files; (c) no frontmatter sweep; (d) secrets/PII sweep; (e)
  read-order audit — overview precedes every dashboard-write page in the
  `_Sidebar.md` order; (f) SC-15 single-record sweep against the parent repo.
  Then `git push`. **SC-13 is noted**: its behavioral gates (curl/dig against
  the live domain) require the deployed Worker and attached domain (SC-13's
  stated prerequisites) and run at that checkpoint — they are not runnable
  today and the runbook itself says so.
- **RED** — the checks run against written-not-yet-published files; any
  failing check stops the push.
- **GREEN** — commit on the wiki default branch and push (never force-push).
- **Instrument** — SC-18's checklist run after push: `git -C wiki fetch
  origin`; remote default-branch tip tree lists all seven files; `git -C wiki
  status --porcelain` empty; `git -C wiki rev-list --count origin/HEAD..HEAD`
  is 0.

### Item 5 — Open the PR for the repo-side footprint (SC-1 repo clause)

- **Deliverable** — PR from `feature/3-cloudflare-workers-runbook` to `main`
  carrying the one-line gitignore change, with the PR body per
  `git-workflow-pr` (summary, executed evidence, wiki publish pointer). Halt
  at the PR boundary — humans merge.
- **Instrument** — `gh pr create` succeeds; PR URL reported.

## Dependencies

Item 1 → Item 2 (ignore entry precedes clone) → Item 3 → Item 4 → Item 5.
Items 1 and 5 are the only parent-repo footprint; Items 2–4 touch only the
wiki sub-repo.

## Traceability

| SC | Plan item |
|----|-----------|
| SC-1 | 1, 2, 5 |
| SC-2–SC-12 | 3, 4 |
| SC-13 | 4 (noted — not runnable before deployment checkpoint) |
| SC-14 | 3, 4 |
| SC-15 | 4 |
| SC-16 | 3, 4 |
| SC-17 | 3, 4 |
| SC-18 | 4 |

## Not included

Everything under the spec's Out of scope: dashboard execution, in-repo
deployment artifacts, Pages-era mechanics, Cloudflare Access lockdown.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
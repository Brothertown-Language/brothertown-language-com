<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — Pre-PR review gate: present the served site to the developer before filing any PR (brothertown-language-com #13)

## Problem

The repository's conventions require PR review ("Agents open PRs; humans merge")
and a six-item verification-gate set, but no tracked document requires the agent
to show the developer the rendered site before filing the PR. As of 2026-10-26
neither `/AGENTS.md` nor `docs/sop-site-setup.md` states such a presentation
requirement (both read in full this session): an agent runs the gates, opens the
PR, and the developer reviews the PR text with the rendered site never presented.
The developer's directive of record (2026-10-26, this session) adds the gate —
"always must present the site via zola serve for review by the user before PR is
filed": the rendered site is served with `zola serve` and presented for the
developer's review before every PR filing.

## Scope

Three tracked files; docs only — no code, config, content, template, theme,
hook, or CI change:

- `/AGENTS.md` — the normative gate rule (lean; the procedure lives in the SOP).
- `docs/sop-site-setup.md` — the gate's operating procedure.
- `docs/AGENTS.md` — SOP row in the Documents-of-record table
  (cross-reference currency).

## Requirements

- **R-1** — The root `/AGENTS.md`'s Git-workflow section carries the gate rule
  stating four semantic points: (a) before filing any PR from this repository,
  the agent that will file the PR serves the site with `./zola serve`; (b) it
  presents the live preview to the developer for review, giving the URL of the
  actually-running server; (c) the PR is filed only after that presentation — no
  PR filing precedes the presented review, unconditionally (every PR,
  docs-only changes included); (d) it names `docs/sop-site-setup.md` as the
  procedure of record, so this file stays lean.
- **R-2** — `docs/sop-site-setup.md` carries a **Pre-PR preview review**
  procedure containing: (a) **trigger** — before filing every PR from this
  repository (filing = opening the PR on GitHub, `gh pr create`), and this
  issue's own implementing PR is the gate's first application; (b) **serve** —
  `./zola serve`; when the working-tree `./zola` binary is absent, `./build.sh`
  runs first (it refreshes `./zola` to the `ZOLA_VERSION` pin — verified in
  `build.sh`); (c) **truthful URL** — the presented preview URL is the URL the
  server is actually answering (default `http://127.0.0.1:1111`; `--port` used
  when 1111 is unavailable) — never an assumed URL; (d) **drafts** — when the
  change under review contains draft-flagged content, serve with
  `./zola serve --drafts` (`serve` excludes drafts by default — binary `--help`,
  verified 2026-10-26); this never touches the draft gate, drafts stay draft in
  the PR; (e) **presentation minimum** — the preview URL plus the change's
  rendered surface (the pages/sections the branch touches); (f) **lifecycle** —
  the server runs only for the review window: started for the presentation,
  kept up while the developer reviews, and stopped once the developer responds
  to the presentation (continuing with other work does not extend the window;
  no lingering server is left running); (g) **record** — the PR body records
  the presented review (preview URL + date presented) in its evidence set, so
  filing-after-presentation is decidable from the PR artifact; (h)
  **coexistence** — the review does not replace the six Verification gates;
  those run as stated in their own section.
- **R-3** — The procedure carries the **no-skip clause**: when the server
  cannot render the branch's site, the agent presents the serve/build failure
  output to the developer in place of the preview, and the gate still holds —
  the PR waits for that presented review. The presentation requirement is never
  waived; the failure becomes the reviewed content.
- **R-4** — `docs/AGENTS.md`'s Documents-of-record row for `sop-site-setup.md`
  carries the added role (the pre-PR preview review gate).

## Success criteria

| ID | Criterion | Class | Instrument |
|----|-----------|-------|------------|
| SC-1 | `/AGENTS.md`'s Git-workflow section states the gate rule with all four semantic points of R-1 | structural | content check of the section's text for points (a)–(d) |
| SC-2 | `docs/sop-site-setup.md` carries the Pre-PR preview review procedure containing all eight points (a)–(h) of R-2 | structural | content check of the section for (a)–(h) |
| SC-3 | The procedure states the no-skip clause (R-3) | structural | content check |
| SC-4 | `docs/AGENTS.md`'s SOP row carries the review-gate role (R-4), and the change's PR diff touches exactly `AGENTS.md`, `docs/sop-site-setup.md`, and `docs/AGENTS.md` — no store, content, theme, hook, or CI files | structural | content check + `git diff --name-only` against the base branch |

Classification note: the deliverable is documentation; every criterion is
satisfied or violated by tracked-file content and the PR's diff, so all four
criteria are structural. The gate's future compliance is what the rule text
exists to produce; this spec states no criterion about future session conduct,
because this change's deliverable is the text.

## Impact

- Consumers: the filing agent — the gate binds every future PR filing from this
  repository; the developer, who receives the rendered-site presentation before
  reviewing the PR text.
- Blast radius: three files, all documentation (`./zola check` treats the
  `docs/` tree as non-content — no built-site effect; the implementing PR's
  evidence re-runs `./zola check` and records the baseline). Cross-reference
  surface is covered: the `docs/AGENTS.md` row (R-4) is the only table naming
  the SOP's role sections; the root `/AGENTS.md`'s Layout mention of the SOP
  (re-vendor procedure) needs no change.
- Risk: low — a conduct rule; the review window adds a pre-filing step by
  design (that is the directive's point).
- Open issue #9 (back-dated blog entry) is affected only if its PR files after
  this rule lands — then its filing follows the gate; no ordering dependency
  exists between #9 and this issue.

## Out of scope

- Mechanical enforcement of the gate (hook, CI check, bot) — a hook cannot
  observe a chat presentation or a human review; the gate binds agent conduct
  through the rule text and the PR-body record.
- Fixing the pre-existing stale prose in `/AGENTS.md` (the "Current state:
  bootstrap" header line and the "Commands (after issue 1 lands)" heading —
  issue 1 merged 2026-10-26; unrelated staleness the diff deliberately leaves).
- Remote or tunneled preview hosting; any preview deployments system — the
  review is local (`zola serve` per the directive).
- The publish (draft) gate — unchanged.

## Approach

The gate is agent conduct, so the always-in-context `/AGENTS.md` carries the
normative rule (agents read it at every session start) and the SOP carries the
operating procedure — the same split the repo already uses for the
Verification gates and the Publish procedure. The evidence trail (presented
URL in session + PR-body record) makes the "filed only after the presented
review" ordering decidable from the PR artifact rather than honor-system
recall. The gate's first application is this issue's own implementing PR,
which presents the served site before filing.

## Dependencies

- None blocking. The gate applies from this issue's merge onward; issue #9's
  PR (open, back-dated blog entry) is in scope only if it files after this rule
  lands — no ordering dependency exists between #9 and this issue.
- Consumes verified facts: `zola serve` defaults (interface `127.0.0.1`, port
  `1111`, `--drafts` flag — from `./zola serve --help`, verified 2026-10-26);
  `build.sh`'s working-tree `./zola` refresh (`build.sh` lines 41–45, read
  2026-10-26); the documented preview URL (`/AGENTS.md` Commands;
  `docs/sop-site-setup.md` Local development loop).

## References

- Developer directive (2026-10-26, this session): "File a spec: AGENTS.md/SoP
  update: always must present the site via zola serve for review by the user
  before PR is filed." — the named surfaces (AGENTS.md + SoP) and the
  unconditional gate both trace here.
- `/AGENTS.md` (read in full 2026-10-26): Git workflow ("Agents open PRs;
  humans merge"), Commands ("Preview: `./zola serve`
  (http://127.0.0.1:1111)"), Content rules.
- `docs/sop-site-setup.md` (read in full 2026-10-26): Local development loop,
  Verification gates (six), Publish procedure.
- `docs/AGENTS.md` (read 2026-10-26): Documents-of-record table — the SOP's
  role row.
- House spec format: `.issues/8/spec.md`.

---

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
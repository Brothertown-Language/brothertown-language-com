<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Plan — brothertown-language-com#4 — repo `opencode.jsonc` with Cloudflare MCP service

Derived from the validated spec (`.issues/4/spec.md`, fresh-context PASS 2026-10-26). One deliverable — the root config file — carries the spec's five structural criteria; the plan's single item writes it whole, and each criterion is asserted by its own instrument run.

## Items

### Item 1 — Create `opencode.jsonc` at the repository root with the decided content (SC-1, SC-2, SC-3, SC-4, SC-5)

- **Deliverable** — tracked file `opencode.jsonc` at the repository root, content exactly the spec's Approach skeleton: `$schema` reference; `mcp.cloudflare` block with `type: "remote"`, `url: "https://mcp.cloudflare.com/mcp"`, `enabled: true`; `permission` with the `cloudflare_*` DENIED default; inline agent `cloudflare-ops` (`mode: subagent`) whose `permission` ALLOWS `cloudflare_*` with the spec's description text.
- **RED** — the five fact-assertions run against the current repository state, all failing: (a) file check — `opencode.jsonc` does not exist at the root (verified 2026-10-26); (b)–(e) content reads — no file to read, so no service declaration, no credential-absence fact, no DENIED default, no ALLOWED sub-agent exist.
- **GREEN** — write the file in one action (branch: `feature/chore-opencode-jsonc-cloudflare-mcp`, off the current trunk; commit per the repo's conventional-commit style).
- **Verification instruments** — each SC's own check, run on the written file:
  - SC-1: file check — `opencode.jsonc` exists at the root and is not gitignored (`.gitignore` verified 2026-10-26: no matching pattern).
  - SC-2: content read — the `mcp.cloudflare` block carries exactly the specified name, `type`, `url`, and `enabled: true`.
  - SC-3: content read — no token/credential material anywhere in the file (no Authorization headers, no token strings, no oauth credential blocks); OAuth relies on opencode's default flow.
  - SC-4: content read — the `permission` default for `cloudflare_*` is `deny`.
  - SC-5: content read — the inline `cloudflare-ops` agent block carries `mode: "subagent"` and `permission` allowing `cloudflare_*`, with no credential or scope-widening material (no `oauth` scope entries beyond default, no headers).

## Dependencies

None upstream — greenfield file; no other repo file is read or modified.

## Traceability

| SC | Plan item |
|----|-----------|
| SC-1 | Item 1 |
| SC-2 | Item 1 |
| SC-3 | Item 1 |
| SC-4 | Item 1 |
| SC-5 | Item 1 |

Coverage is bidirectional: every spec SC has an item; the item carries no untraceable extra (its content set equals the spec's Approach skeleton).

## Documentation Sources

- Spec: `.issues/4/spec.md` (validated, PASS 2026-10-26).
- opencode v1 docs — MCP servers (`opencode.ai/docs/mcp-servers/`) and permissions (`opencode.ai/docs/permissions/`), fetched 2026-10-26.
- Cloudflare MCP service facts: `github.com/cloudflare/mcp` README; live endpoint probes (401 + RFC 9728 metadata), 2026-10-26 — recorded in the spec's facts table.

## Enforcement Gate

The five instruments run on the written file before commit and their evidence goes into the PR body. The repo's trunk-protection hooks (pre-commit/pre-push) gate the branch hygiene; humans merge the PR.

## Cost Frame

One file write plus five content reads; minutes. No build, test, or dependency surface is touched.

## Edge Cases

- JSONC comments parse: documented for `opencode.jsonc` in the v1 docs examples; comments ride in the file.
- `$schema` is a documented top-level key and does not disturb R-2's exact service block; R-2 constrains the service block, not the file's other top-level keys.
- File writes land with the repo's normal conventions (tracked, not ignored — verified above).
- A malformed file would block opencode startup (documented validation behavior) — the SC instruments' content reads precede any commit.

## Not Included

The spec's out-of-scope list verbatim: no opencode development/troubleshooting, no Cloudflare MCP server internals, no API-token path, no other configuration sections, no site content/build work, no runtime Cloudflare operations, nothing beyond the file's content per R-1 through R-5.
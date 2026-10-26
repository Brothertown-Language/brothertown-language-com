<!-- SPDX-FileCopyrightText: 2026 Brothertown Language -->
<!-- SPDX-License-Identifier: MIT -->

# Spec — Repo agent config: `opencode.jsonc` with Cloudflare MCP service (brothertown-language-com #4)

## Problem

This repository has no project-scoped opencode agent configuration: the repository root carries no `opencode.jsonc`, so no session in this repo declares the Cloudflare MCP service, nothing confines it, and nothing authenticates it under the decided mechanism. The developer directed (2026-10-25/26) that this be added as a single tracked configuration file — the service denied by default, reachable only through a repo-defined sub-agent whose perms allow it, with OAuth as the authentication mechanism so that no credential enters the file or the repository. This is setup of a basic MCP plugin at the configuration layer ("we are setting up a basic MCP plugin", developer, 2026-10-26); it is NOT development or troubleshooting of opencode itself — opencode's documented behavior is a premise of this spec (as of opencode 1.19.3, snap, verified locally 2026-10-26), not an object of it.

## Scope

The deliverable is one new tracked file at the repository root: `opencode.jsonc`. It declares the `mcp.cloudflare` service, the perm default DENIED for that service, and the inline sub-agent whose perms ALLOW the service. No other file changes; no site content, build pipeline, theme, or `.opencode/` deck files are touched.

## Requirements

- **R-1** — The repository root SHALL contain a project-specific agent-configuration file `opencode.jsonc`.
- **R-2** — The file SHALL declare the MCP service exactly: name `cloudflare`, `type: "remote"`, `url: "https://mcp.cloudflare.com/mcp"`, `enabled: true`.
- **R-3** — The file SHALL contain no embedded tokens or credentials. The service's authentication mechanism SHALL be OAuth: the developer authorizes once through opencode's OAuth flow; opencode stores the credentials outside the repository.
- **R-4** — The file SHALL mark the cloudflare MCP DENIED by default — a perm default DENIED covering all agents — and SHALL declare a sub-agent inline in the same root file whose perms ALLOW the cloudflare MCP.
- **R-5** — The sub-agent's ALLOWED perms SHALL cover all tools of the cloudflare MCP, operating under read-only scope: the OAuth grant carries read permissions only, and the file SHALL carry no OAuth credential material and no configuration requesting additional scopes beyond the service's read-only grant.

## Success criteria

Traceability, both directions: SC-1 ← R-1; SC-2 ← R-2; SC-3 ← R-3; SC-4 ← R-4 (denied default); SC-5 ← R-4 (sub-agent) + R-5 (all tools, read-only scope). Every requirement is covered: R-1 → SC-1, R-2 → SC-2, R-3 → SC-3, R-4 → SC-4 and SC-5, R-5 → SC-5.

| ID | Criterion | Class | Instrument |
|----|-----------|-------|-----------|
| SC-1 | The repository root contains `opencode.jsonc` | structural | file check (repo tree) |
| SC-2 | The file declares the MCP service exactly: `mcp.cloudflare`, `type: "remote"`, `url: "https://mcp.cloudflare.com/mcp"`, `enabled: true` | structural | content read against the specified values |
| SC-3 | OAuth is the auth mechanism; the file contains no embedded tokens | structural | content read (no token/credential material present); the repo's existing detect-secrets hook on commit |
| SC-4 | The cloudflare MCP's perm default is DENIED in the file | structural | content read of the deny |
| SC-5 | The sub-agent is declared inline in the root `opencode.jsonc`; its perms are ALLOWED for all tools of the MCP; read-only scope | structural | content read of the allow (plus R-5's credential/scope-widening absence in the same read) |

All five criteria are structural file-content checks; no runtime behavioral criterion is in this set (the developer's stated requirements define the file's content; opencode's documented consumption behavior is premise, not criterion). The read-only scope's file-side observable is the credential/scope-widening absence in R-3 and R-5; the grant itself is fixed by the developer's read-only selection at the OAuth consent screen (see Approach).

## Out of scope

- opencode development, troubleshooting, or verification of its documented behavior (developer boundary, 2026-10-26) — documented opencode behavior is premise.
- The Cloudflare MCP server's internals and any of its endpoints beyond what the decided design's requirements name.
- API-token authentication (rejected by the developer: OAuth is the mechanism, no embedded tokens).
- Any other configuration sections (model, providers, skills, formatters…) beyond R-1 through R-5's content.
- The site itself — Zola setup, build pipeline, content (issues #1 and #3 territory).
- Runtime Cloudflare operations through the new sub-agent beyond this setup (usage patterns are the developer's; this spec sets up the plugin).

## Approach

The decided design (developer decisions 2026-10-25/26, exploration record): the file targets the installed v1 opencode (1.19.3, snap — verified locally 2026-10-26) using its documented configuration surfaces, with OAuth as opencode's default for remote MCP servers (401 detection → OAuth flow → dynamic client registration; credentials stored outside project configuration at `~/.local/share/opencode/mcp-auth.json`), the flat service block exactly as R-2 states, and the permission mechanism carrying the DENIED-default / ALLOWED-sub-agent polarity — v1's permission config is keyed by tool name, supports wildcard patterns, evaluates rules last-match-wins, and merges agent permissions over global rules with agent rules taking precedence (opencode docs, fetched 2026-10-26):

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "cloudflare": {
      "type": "remote",
      "url": "https://mcp.cloudflare.com/mcp",
      "enabled": true
    }
  },
  "permission": {
    "cloudflare_*": "deny"
  },
  "agent": {
    "cloudflare-ops": {
      "description": "Read-only Cloudflare inspection for brothertown-language.com (DNS records, Pages status, account identity) via the cloudflare MCP",
      "mode": "subagent",
      "permission": {
        "cloudflare_*": "allow"
      }
    }
  }
}
```

The sub-agent name and description text are the exploration record's standing proposal carrying the decided design; the requirements are the five R-x statements above. MCP tools register as `<server>_<tool>` (here: `cloudflare_docs`, `cloudflare_execute`, `cloudflare_search`, `cloudflare_whoami`), so the permission patterns key the service's tool suite under the server-name prefix.

Operational notes (actor split):

- The implementer writes and PRs the file; the developer merges (human gate).
- Config is read once at opencode start (documented v1 behavior): a restart applies the change.
- The developer runs the OAuth authorization once at setup (browser consent; `opencode mcp auth cloudflare`), selecting read-only permissions at Cloudflare's consent screen — the endpoint's protection metadata names the scopes it demands (`user:read account:read`, verified live 2026-10-26). The agent never authorizes and never widens scope; a mid-session scope challenge (the server's documented `insufficient_scope` re-auth request) surfaces to the consent screen — that decision is human, never the agent's.
- The repository's existing branch-first workflow and hooks hold throughout (the file lands via PR; the detect-secrets hook covers the commit).

## Facts of record (verified 2026-10-25/26)

| Fact | Source | Verified |
|------|--------|----------|
| Endpoint `https://mcp.cloudflare.com/mcp` returns HTTP 401 on unauthenticated requests; `WWW-Authenticate` names an OAuth realm with scopes `user:read account:read` and the RFC 9728 resource-metadata URL | live curl probe (GET + MCP `initialize` POST) | 2026-10-26 02:01 UTC |
| Protection metadata: `resource_name: "Cloudflare API MCP Server"`; authorization server `https://mcp.cloudflare.com`; scopes supported `user:read account:read`; bearer via header | live fetch `/.well-known/oauth-protected-resource/mcp` | 2026-10-26 |
| The service exposes the whole Cloudflare API through its code-mode tool set (`docs`, `search`, `execute`, `whoami`); provider-measured context cost ~1,100 tokens (~0.5% of a 200K window) in code mode; with server code mode disabled: 2,594 tools, 244,047 tokens (minimal schemas) — unusable as a context matter | `github.com/cloudflare/mcp` README | fetched 2026-10-26 |
| Tool results are server-capped at ~6,000 tokens in code mode; word-count rendering of the ~1,100-token figure at the ordinary 1.25–1.3 tokens/word prose ratio: ~850–900 words per session carrying the tools | `github.com/cloudflare/mcp` README + arithmetic | fetched 2026-10-26 |
| Installed runtime: opencode 1.19.3 (snap; `/snap/bin/opencode`); v2 not installed via snap (developer statement, 2026-10-26) | local `snap list`, `opencode --version` | 2026-10-26 |
| v1 remote-MCP config surface: flat `mcp.<name>` with `type`/`url`/`enabled`; OAuth automatic (401 → flow → DCR), credentials at `~/.local/share/opencode/mcp-auth.json`; `opencode mcp auth <name>` triggers authorization; manual `oauth` blocks and API-token headers are the documented alternatives | `opencode.ai/docs/mcp-servers/` (v1 docs, current docs site) | fetched 2026-10-26 |
| v1 permission surface: keys are tool names; wildcard patterns (`*`, `?`) supported; last matching rule wins; agent permissions merge with the global config and agent rules take precedence; the legacy `tools` boolean map merged into `permission` as of v1.1.1 | `opencode.ai/docs/permissions/` | fetched 2026-10-26 |
| MCP tools register as `<server>_<tool>`; serving-name prefix globs (e.g. `server_*`) are the documented pattern for gating a server's tool set | `opencode.ai/docs/mcp-servers/` | fetched 2026-10-26 |
| opencode reads project configuration from the workspace root (`opencode.json` / `opencode.jsonc`); config changes apply at start | `opencode.ai/docs/mcp-servers/` | fetched 2026-10-26 |
| Published configuration schema (validation reference): `https://opencode.ai/config.json` | live fetch | 2026-10-26 |

Documented constraints carried, not papered over: the token figures above are the provider's own measurements as published in its README (no independent re-measurement was performed — an OAuth-authorized probe session exists only after the developer's first authorization); the v1 docs pages are the current docs-site content as fetched — future opencode upgrades re-read the docs through the normal documentation-refresh flow, not through this spec.

*Co-authored with AI: OpenCode (ollama-cloud/glm-5.3-flash)*
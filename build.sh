#!/usr/bin/env bash
# Build entry for Cloudflare Workers Builds (build command: ./build.sh).
# The Workers Builds image preinstalls no Zola and offers no Zola override
# hook, so we download exactly the pinned release from ZOLA_VERSION and build.
# SPDX-FileCopyrightText: 2026 Brothertown Language
# SPDX-License-Identifier: MIT
set -euo pipefail

version="$(tr -d '[:space:]' < ZOLA_VERSION)"
case "$version" in
  v[0-9]*.[0-9]*.[0-9]*) : ;;
  *) echo "ZOLA_VERSION: not a vMAJOR.MINOR.PATCH value: '$version'" >&2; exit 1 ;;
esac

case "$(uname -m)" in
  x86_64) : ;;
  *) echo "Unsupported build image architecture: $(uname -m)" >&2; exit 1 ;;
esac

asset="zola-${version}-x86_64-unknown-linux-gnu.tar.gz"
url="https://github.com/getzola/zola/releases/download/${version}/${asset}"

# Zola binary lives outside the repo (public/ is the only build output).
bin_dir="${HOME}/.local/bin"
mkdir -p "$bin_dir"
zola_bin="${bin_dir}/zola"

if [ ! -x "$zola_bin" ] || ! "$zola_bin" --version 2>/dev/null | grep -qF "$version"; then
  echo "Downloading Zola ${version}"
  tmp="$(mktemp -d)"
  trap 'rm -rf "$tmp"' EXIT
  curl -fsSL -o "${tmp}/${asset}" "$url"
  mkdir -p "${tmp}/out"
  tar -xf "${tmp}/${asset}" -C "${tmp}/out"
  mv "${tmp}/out/zola" "$zola_bin"
  chmod +x "$zola_bin"
fi

"$zola_bin" --version

# ./zola is the working-tree Zola used by `./zola serve` / `./zola check`
# per AGENTS.md commands; refresh it to the pinned version on every build.
rm -f ./zola
cp "$zola_bin" ./zola
chmod +x ./zola

# Domain-aware build: Workers Builds provides no deployment-URL variable
# (docs/cloudflare-facts.md F-16 — CF_PAGES_URL is Pages-only), but it DOES
# inject the branch name as WORKERS_CI_BRANCH (F-16 default env vars — also
# git-detectable via `git rev-parse --abbrev-ref HEAD` as fallback).
# is-production := branch == main. Production builds use the base_url of
# record (or an absolute SITE_BASE_URL override); preview (non-main) builds
# are domain-neutral (--base-url /): every template-generated URL (assets,
# nav, facets, cards, canonical) is root-relative, so any preview hostname
# serves correctly with zero production-absolute links. Stable mechanism:
# nothing to set per branch — the behavior follows the branch automatically
# (site-relative SOP: docs/sop-site-setup.md; verified against the pinned
# Zola 0.23.6, 2026-10-27). Preview-mode trade, recorded in the SOP: the
# generated feeds/sitemap emit root-relative URLs on that build.
# Explicit absolute SITE_BASE_URL (dashboard env var or local export) always
# wins for both branches; unset and no branch detection (e.g. plain zola
# builds), build exactly as before (base_url of record).
if [ -z "${SITE_BASE_URL:-}" ]; then
  branch="${WORKERS_CI_BRANCH:-}"
  if [ -z "$branch" ]; then
    branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || true)"
  fi
  if [ -n "$branch" ] && [ "$branch" != "main" ]; then
    echo "is-production: false (branch '$branch') -> domain-neutral preview build"
    SITE_BASE_URL="relative"
  elif [ -n "$branch" ]; then
    echo "is-production: true (branch '$branch')"
  fi
fi
base_args=()
if [ "${SITE_BASE_URL:-}" = "relative" ]; then
  base_args=(--base-url "/")
elif [ -n "${SITE_BASE_URL:-}" ]; then
  base_args=(--base-url "$SITE_BASE_URL")
fi
./zola build --force ${base_args[@]+"${base_args[@]}"} --output-dir public
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

./zola build --force --output-dir public
#!/usr/bin/env bash
# Crown Movers v2.2 — ACSS settings on STAGING. Stops and restores on first hard failure.
set -uo pipefail
cd ~/public_html || exit 1
[ "$(wp option get home 2>/dev/null)" = "https://staging.crownmovers.ca" ] || { echo "GATE FAIL"; exit 1; }
OUT=~/private_html/cm-v2.2; mkdir -p "$OUT"
wp acss settings export --file="$OUT/acss-pre.json" 2>/dev/null || { echo "EXPORT FAIL"; exit 1; }
echo "PRE EXPORT OK"

fail() {  # restore exact pre-state; CSS was never regenerated before this point
  echo "FAIL: $1"
  wp acss settings import "$OUT/acss-pre.json" --yes --skip-css 2>/dev/null && echo "RESTORED PRE SETTINGS"
  exit 1
}
setk() {  # hard: key must exist and value must validate (no --force)
  local old; old=$(wp acss settings get "$1" 2>/dev/null) || fail "missing key $1"
  wp acss settings set "$1" "$2" --skip-css >/dev/null 2>"$OUT/err.txt" || fail "set $1=$2 :: $(tail -1 "$OUT/err.txt")"
  echo "SET $1: '$old' -> '$(wp acss settings get "$1" 2>/dev/null)'"
}
trysetk() {  # soft: only for clearing optional fields
  local old; old=$(wp acss settings get "$1" 2>/dev/null) || { echo "WARN missing key $1"; return 0; }
  wp acss settings set "$1" "$2" --skip-css >/dev/null 2>"$OUT/err.txt" \
    && echo "SET $1: '$old' -> '$2'" || echo "WARN could not set $1 :: $(tail -1 "$OUT/err.txt")"
}

# --- fonts: self-hosted WOFF2 variable, valid weight ranges ---
for f in archivo-latin-wght-normal.woff2 inter-latin-wght-normal.woff2; do
  [ -s "wp-content/uploads/crown-fonts/$f" ] || fail "font file missing: $f"
done
F=/wp-content/uploads/crown-fonts
setk font-1-type static
setk font-1-family-name "Archivo"
setk font-1-src "$F/archivo-latin-wght-normal.woff2"
setk font-1-format woff2
setk font-1-weight "100 900"
setk font-1-style normal
setk font-1-display swap
trysetk font-1-src-fallback ""
trysetk font-1-format-fallback ""
trysetk font-1-variation-settings ""
setk font-2-type static
setk font-2-family-name "Inter"
setk font-2-src "$F/inter-latin-wght-normal.woff2"
setk font-2-format woff2
setk font-2-weight "100 900"
setk font-2-style normal
setk font-2-display swap
trysetk font-2-src-fallback ""
trysetk font-2-format-fallback ""
trysetk font-2-variation-settings ""

# --- root font size back to browser default (delete this line to keep 62.5%) ---
setk root-font-size 100

# --- colour assignments: surfaces from base (ink family), not neutral ---
setk text-dark "var(--base)"
setk bg-ultra-light "var(--base-ultra-light)"
setk bg-light "var(--base-light)"
setk bg-dark "var(--base-dark)"
setk bg-ultra-dark "var(--base)"

# --- buttons ---
setk btn-base-text "var(--white)"
setk btn-base-hover-text "var(--white)"
setk option-base-btn-shades off
setk option-primary-btn-shades off

wp acss css regenerate 2>/dev/null || fail "css regenerate"
wp acss settings export --file="$OUT/acss-post.json" 2>/dev/null
wp acss status --format=json > "$OUT/acss-status.json" 2>/dev/null
wp breeze purge --cache=all 2>/dev/null && echo "BREEZE PURGED" || echo "BREEZE CLI UNAVAILABLE"
echo "DONE"

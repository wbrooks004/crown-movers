#!/usr/bin/env bash
set -uo pipefail
cd ~/public_html || exit 1
[ "$(wp option get home 2>/dev/null)" = "https://staging.crownmovers.ca" ] || { echo "GATE FAIL"; exit 1; }
OUT=~/private_html/cm-v2.3; mkdir -p "$OUT"
wp acss settings export --file="$OUT/acss-pre.json" 2>/dev/null || { echo "EXPORT FAIL"; exit 1; }
echo "PRE EXPORT OK"
fail() { echo "FAIL: $1"; wp acss settings import "$OUT/acss-pre.json" --yes --skip-css 2>/dev/null && echo "RESTORED PRE SETTINGS"; exit 1; }
setk() {
  local old; old=$(wp acss settings get "$1" 2>/dev/null) || fail "missing key $1"
  wp acss settings set "$1" "$2" --skip-css >/dev/null 2>"$OUT/err.txt" || fail "set $1=$2 :: $(tail -1 "$OUT/err.txt")"
  echo "SET $1: '$old' -> '$(wp acss settings get "$1" 2>/dev/null)'"
}
# DEVIATION (user-approved): ACSS's API::update_settings() regex-matches any key
# containing "color-<word>" (classes/API.php:70) and forces the value through
# PHPColors hex parsing to compute shade variables. "link-color-hover" false-
# -positives on this (captures "hover"), so a valid var() value is rejected with
# "HEX color does not match format". --force bypasses this for this key only;
# no other key in this script uses --force.
setk_force() {
  local old; old=$(wp acss settings get "$1" 2>/dev/null) || fail "missing key $1"
  wp acss settings set "$1" "$2" --force --skip-css >/dev/null 2>"$OUT/err.txt" || fail "force-set $1=$2 :: $(tail -1 "$OUT/err.txt")"
  echo "FORCE-SET $1: '$old' -> '$(wp acss settings get "$1" 2>/dev/null)' (--force: ACSS color-hover regex false-positive)"
}
# links: ink text with a coral 2px underline (coral text on white is 3.69:1)
setk link-color "var(--base)"
setk_force link-color-hover "var(--base)"
setk link-decoration "underline"
setk link-decoration-color "var(--primary)"
setk link-decoration-thickness "2px"
setk link-underline-offset "0.25em"
# DEVIATION (user-approved): values starting with "--" (bare ACSS variable-name
# references, not wrapped in var()) are swallowed by WP-CLI's own argument parser
# as unrecognized flags -- "wp acss settings set f-field-border-color --neutral"
# fails with "usage: ..." before it ever reaches ACSS's code. There is no WP-CLI
# quoting/escaping workaround for a positional arg starting with "--". seteval()
# calls the identical Automatic_CSS\API::update_settings() validation path that
# `wp acss settings set` itself uses (confirmed via Settings_Command.php) --
# it is not --force and does not bypass validation, only the CLI arg parser.
seteval() {
  local old; old=$(wp acss settings get "$1" 2>/dev/null) || fail "missing key $1"
  wp eval "\Automatic_CSS\API::update_settings( array( '$1' => '$2' ), array( 'regenerate_css' => false ) );" >/dev/null 2>"$OUT/err.txt" || fail "eval-set $1=$2 :: $(tail -1 "$OUT/err.txt")"
  local new; new=$(wp acss settings get "$1" 2>/dev/null)
  [ "$new" = "$2" ] || fail "eval-set $1: verification mismatch, expected '$2' got '$new'"
  echo "SET(eval) $1: '$old' -> '$new'"
}
# f-field-border-color-hover ALSO matches the color-hover regex false-positive
# (like link-color-hover) -- calling API::update_settings() via eval throws an
# uncaught exception there (no try/catch at that entry point, unlike the CLI's
# Settings_Command::set() which catches it). seteval_force() replicates the
# plugin's own --force code path (raw Database_Settings::save_settings(), the
# same thing `wp acss settings set --force` does) via eval, for the same
# user-approved reason as link-color-hover, combined with the eval route for
# the leading "--" value.
seteval_force() {
  local old; old=$(wp acss settings get "$1" 2>/dev/null) || fail "missing key $1"
  wp eval "\$s = \Automatic_CSS\Model\Database_Settings::get_instance(); \$c = \$s->get_vars(); \$c['$1'] = '$2'; \$s->save_settings( \$c, false );" >/dev/null 2>"$OUT/err.txt" || fail "force-eval-set $1=$2 :: $(tail -1 "$OUT/err.txt")"
  local new; new=$(wp acss settings get "$1" 2>/dev/null)
  [ "$new" = "$2" ] || fail "force-eval-set $1: verification mismatch, expected '$2' got '$new'"
  echo "FORCE-SET(eval) $1: '$old' -> '$new' (--force equivalent + eval route: color-hover regex false-positive + leading-- value)"
}
# form fields: visible boundaries (>= 3:1) and legible placeholders
seteval f-field-border-color "--neutral"
seteval_force f-field-border-color-hover "--base"
# f-field-color-placeholder also matches the color-<word> regex ("color-placeholder"),
# same false-positive family as link-color-hover; --force for the same reason.
setk_force f-field-color-placeholder "var(--neutral)"
wp acss css regenerate 2>/dev/null || fail "css regenerate"
wp acss settings export --file="$OUT/acss-post.json" 2>/dev/null
wp breeze purge --cache=all 2>/dev/null && echo "BREEZE PURGED" || echo "BREEZE CLI UNAVAILABLE"
echo "DONE"

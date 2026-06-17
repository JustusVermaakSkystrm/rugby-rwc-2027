#!/bin/bash
# Triggers the hourly Rugby World Cup 2027 prediction workflow on GitHub.
# Token is read from the macOS Keychain (never stored on disk in plaintext).
#
# One-time token setup (see scheduling README):
#   security add-generic-password -a "$USER" -s rwc-gh-token -w 'github_pat_xxx'

set -euo pipefail

REPO="REPLACE_WITH_OWNER/rugby-rwc-2027"
WORKFLOW="rwc-hourly.yml"
REF="main"
LOG="$HOME/Library/Logs/rwc-trigger.log"

TOKEN="$(security find-generic-password -a "$USER" -s rwc-gh-token -w 2>/dev/null || true)"
if [ -z "$TOKEN" ]; then
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') ERROR: no token in keychain (service rwc-gh-token)" >> "$LOG"
  exit 1
fi

code=$(curl -s -o /dev/null -w '%{http_code}' -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/repos/${REPO}/actions/workflows/${WORKFLOW}/dispatches" \
  -d "{\"ref\":\"${REF}\"}")

ts="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
if [ "$code" = "204" ]; then
  echo "$ts OK: workflow dispatched" >> "$LOG"
else
  echo "$ts ERROR: dispatch returned HTTP $code" >> "$LOG"
  exit 1
fi

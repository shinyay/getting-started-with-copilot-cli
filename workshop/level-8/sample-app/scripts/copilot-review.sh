#!/usr/bin/env bash
# copilot-review.sh — Automated PR review using Copilot CLI programmatic mode
#
# Usage:
#   ./scripts/copilot-review.sh [--diff-file PATH]
#
# This script demonstrates using `copilot -p` for non-interactive
# code review automation.

set -euo pipefail

DIFF_FILE="${1:-}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# If a diff file is provided, use it; otherwise, use git diff
if [[ -n "$DIFF_FILE" && -f "$DIFF_FILE" ]]; then
    DIFF_CONTENT=$(cat "$DIFF_FILE")
else
    DIFF_CONTENT=$(cd "$PROJECT_DIR" && git diff HEAD~1 2>/dev/null || echo "No git diff available")
fi

if [[ -z "$DIFF_CONTENT" || "$DIFF_CONTENT" == "No git diff available" ]]; then
    echo "No changes to review."
    exit 0
fi

echo "=== Copilot Automated Review ==="
echo "Reviewing $(echo "$DIFF_CONTENT" | wc -l) lines of diff..."
echo ""

# Using copilot -p (programmatic) -s (silent/script-friendly)
# The diff is passed as part of the prompt
copilot -p "Review this code diff. Focus on:
1. Bugs or logic errors
2. Security issues
3. Missing error handling
4. Naming convention violations

Diff:
$DIFF_CONTENT

Format your review as:
- 🔴 Critical: [issue]
- 🟡 Warning: [issue]
- 🟢 Good: [positive observation]" -s 2>/dev/null || echo "(copilot CLI not available — this is a demo script)"

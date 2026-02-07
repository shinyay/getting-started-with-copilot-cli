#!/usr/bin/env bash
# copilot-changelog.sh — Generate changelog from git log using Copilot CLI
#
# Usage:
#   ./scripts/copilot-changelog.sh [since-tag]
#
# Demonstrates: copilot -p for content generation from structured input

set -euo pipefail

SINCE="${1:-$(git describe --tags --abbrev=0 2>/dev/null || echo 'HEAD~10')}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "=== Copilot Changelog Generator ==="
echo "Generating changelog since: $SINCE"
echo ""

# Gather git log
GIT_LOG=$(cd "$PROJECT_DIR" && git log "$SINCE"..HEAD --pretty=format:"%h %s" 2>/dev/null || echo "No commits found")

if [[ -z "$GIT_LOG" || "$GIT_LOG" == "No commits found" ]]; then
    echo "No commits found since $SINCE"
    exit 0
fi

echo "Found $(echo "$GIT_LOG" | wc -l) commit(s)"
echo ""

# Use copilot in programmatic + silent mode
copilot -p "Generate a CHANGELOG entry from these git commits.

Commits:
$GIT_LOG

Group by category:
- 🚀 Features
- 🐛 Bug Fixes
- 📚 Documentation
- 🔧 Maintenance

Format as Markdown. Use conventional commit prefixes (feat:, fix:, docs:, chore:) to categorize." -s 2>/dev/null || echo "(copilot CLI not available — this is a demo script)"

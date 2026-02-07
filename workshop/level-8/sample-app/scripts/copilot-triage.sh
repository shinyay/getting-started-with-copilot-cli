#!/usr/bin/env bash
# copilot-triage.sh — Triage a GitHub issue using Copilot CLI
#
# Usage:
#   ./scripts/copilot-triage.sh <issue-number>
#
# Demonstrates: copilot -p with dynamic input, piping, and structured output

set -euo pipefail

ISSUE_NUMBER="${1:?Usage: $0 <issue-number>}"
REPO="${GITHUB_REPOSITORY:-$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || echo 'owner/repo')}"

echo "=== Copilot Issue Triage ==="
echo "Triaging issue #${ISSUE_NUMBER} in ${REPO}"
echo ""

# Fetch issue details (requires gh CLI)
ISSUE_JSON=$(gh issue view "$ISSUE_NUMBER" --json title,body,labels,author --repo "$REPO" 2>/dev/null || echo '{"title":"Demo issue","body":"This is a placeholder","labels":[],"author":{"login":"user"}}')

TITLE=$(echo "$ISSUE_JSON" | jq -r '.title // "Unknown"')
BODY=$(echo "$ISSUE_JSON" | jq -r '.body // "No description"' | head -50)
LABELS=$(echo "$ISSUE_JSON" | jq -r '[.labels[]?.name] | join(", ") // "none"')
AUTHOR=$(echo "$ISSUE_JSON" | jq -r '.author.login // "unknown"')

echo "Title:  $TITLE"
echo "Author: $AUTHOR"
echo "Labels: $LABELS"
echo ""

# Use copilot for triage
copilot -p "Triage this GitHub issue:

Title: $TITLE
Author: $AUTHOR
Current labels: $LABELS
Body:
$BODY

Provide:
1. **Priority**: P0 (critical) / P1 (high) / P2 (medium) / P3 (low)
2. **Category**: bug / feature / docs / question / maintenance
3. **Suggested labels**: comma-separated list
4. **Estimated effort**: small (< 1h) / medium (1-4h) / large (> 4h)
5. **Recommended assignee type**: maintainer / contributor / good-first-issue
6. **Summary**: 1-sentence description of what needs to happen" -s 2>/dev/null || echo "(copilot CLI not available — this is a demo script)"

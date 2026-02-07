#!/usr/bin/env bash
# Quick validation of a workshop level's structural requirements.
# Usage: ./validate.sh <level_number>
# Example: ./validate.sh 3
set -euo pipefail

LEVEL_NUM="${1:?Usage: validate.sh <level_number>}"

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
LEVEL_DIR="${REPO_ROOT}/workshop/level-${LEVEL_NUM}"

PASS=0
WARN=0
FAIL=0

check() {
  local status="$1" msg="$2"
  case "$status" in
    pass) echo "  ✅ $msg"; ((PASS++)) ;;
    warn) echo "  ⚠️  $msg"; ((WARN++)) ;;
    fail) echo "  ❌ $msg"; ((FAIL++)) ;;
  esac
}

echo "🔍 Validating Level ${LEVEL_NUM}: ${LEVEL_DIR}"
echo ""

# 1. File presence
echo "📁 Structure:"
[[ -f "${LEVEL_DIR}/README.md" ]] && check pass "README.md exists" || check fail "README.md missing"
[[ -f "${LEVEL_DIR}/CHEATSHEET.md" ]] && check pass "CHEATSHEET.md exists" || check fail "CHEATSHEET.md missing"
[[ -d "${LEVEL_DIR}/sample-app" ]] && check pass "sample-app/ directory exists" || check fail "sample-app/ directory missing"
[[ -f "${LEVEL_DIR}/sample-app/README.md" ]] && check pass "sample-app/README.md exists" || check warn "sample-app/README.md missing"

# 2. Exercise count
echo ""
echo "📝 Exercises:"
if [[ -f "${LEVEL_DIR}/README.md" ]]; then
  EXERCISE_COUNT=$(grep -c '^## Exercise [0-9]' "${LEVEL_DIR}/README.md" || true)
  if [[ "$EXERCISE_COUNT" -eq 12 ]]; then
    check pass "Exercise count: ${EXERCISE_COUNT}/12"
  elif [[ "$EXERCISE_COUNT" -gt 0 ]]; then
    check fail "Exercise count: ${EXERCISE_COUNT}/12 (expected 12)"
  else
    check fail "No exercises found"
  fi

  # 3. Checkpoint count
  CHECKPOINT_COUNT=$(grep -c '### ✅ Checkpoint' "${LEVEL_DIR}/README.md" || true)
  if [[ "$CHECKPOINT_COUNT" -eq 12 ]]; then
    check pass "Checkpoints: ${CHECKPOINT_COUNT}/12"
  else
    check warn "Checkpoints: ${CHECKPOINT_COUNT}/12"
  fi

  # 4. Goal sections
  GOAL_COUNT=$(grep -c '### Goal' "${LEVEL_DIR}/README.md" || true)
  if [[ "$GOAL_COUNT" -eq 12 ]]; then
    check pass "Goal sections: ${GOAL_COUNT}/12"
  else
    check warn "Goal sections: ${GOAL_COUNT}/12"
  fi

  # 5. Key Concept sections
  CONCEPT_COUNT=$(grep -c '### Key Concept' "${LEVEL_DIR}/README.md" || true)
  if [[ "$CONCEPT_COUNT" -ge 8 ]]; then
    check pass "Key Concepts: ${CONCEPT_COUNT}/12 (≥8 required)"
  else
    check warn "Key Concepts: ${CONCEPT_COUNT}/12 (≥8 recommended)"
  fi

  # 6. Self-assessment
  if grep -q 'Self-Assessment' "${LEVEL_DIR}/README.md"; then
    check pass "Self-Assessment section exists"
    SA_ITEMS=$(grep -c '| [0-9]' "${LEVEL_DIR}/README.md" || true)
    # Rough count — includes exercise tables too, so just check it's ≥12
    if [[ "$SA_ITEMS" -ge 12 ]]; then
      check pass "Assessment items present (${SA_ITEMS} table rows found)"
    else
      check warn "Assessment items may be incomplete (${SA_ITEMS} table rows found)"
    fi
  else
    check fail "Self-Assessment section missing"
  fi

  # 7. Horizontal rules between exercises
  HR_COUNT=$(grep -c '^---$' "${LEVEL_DIR}/README.md" || true)
  if [[ "$HR_COUNT" -ge 11 ]]; then
    check pass "Section separators: ${HR_COUNT} horizontal rules"
  else
    check warn "Section separators: only ${HR_COUNT} horizontal rules (expected ≥11)"
  fi
fi

echo ""
echo "📊 Summary: ✅ ${PASS} passed, ⚠️  ${WARN} warnings, ❌ ${FAIL} failed"

if [[ "$FAIL" -gt 0 ]]; then
  exit 1
fi

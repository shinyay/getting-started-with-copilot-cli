---
mode: "agent"
description: "Synchronize the main README exercise tables with actual level content"
---

# Sync README with Workshop Levels

Ensure the main `README.md` exercise tables accurately reflect the actual
exercises in each workshop level.

## Process

For each level (1 through 8):

### 1. Read the Source of Truth

Read `workshop/level-{{N}}/README.md` and extract:
- All exercise numbers and titles (`## Exercise N: Title`)
- The one-line description (from `### Goal`)

### 2. Read the Main README Table

Find the Level {{N}} section in `README.md` and extract the exercise table rows.

### 3. Compare and Report

For each level, report:

| Exercise | Level README | Main README | Match? |
|----------|-------------|-------------|--------|
| 1 | Title from level | Title from main | ✅/❌ |
| 2 | ... | ... | ... |
...

### 4. Fix Mismatches

For any mismatches:
- The **level README is the source of truth** — update the main README to match
- Preserve the table format: `| N-MM | Title | Key concept |`
- Ensure exercise numbering uses the `N-MM` format (e.g., `1-01`, `3-12`)

### 5. Cross-Check Workshop README

Also verify that `workshop/README.md`:
- Lists all levels in the navigation table
- Exercise counts match (should be 12 per level, 96 total)
- Time estimates are reasonable

## Additional Checks

- Verify the main README's cheat sheet cross-reference link still works
- Confirm the "Per-level cheat sheets" note points to a valid path
- Check that the Level progression table (risk levels, sample apps) is accurate

## Output

Provide:
1. A summary of changes made (or "all in sync" if no changes needed)
2. Any discrepancies found between the three files
3. Confirmation that all 96 exercises are accounted for

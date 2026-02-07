---
applyTo: ".github/**/*.{yml,yaml}"
---

# GitHub Configuration Instructions

## Workflows (.github/workflows/)

### Structure

- Descriptive `name:` that reads clearly in the Actions UI
- Explicit `permissions:` block — principle of least privilege
- Pin actions to **major version tags**: `actions/checkout@v4`, `actions/github-script@v7`
- Clear step `name:` fields that describe purpose (not implementation)

### Patterns

- Prefer `actions/github-script@v7` for complex logic over chained shell commands
- Use `core.info()`, `core.warning()`, `core.setFailed()` for structured logging
- Comment back on issues/PRs with results — provide actionable feedback
- Handle errors gracefully: catch expected failures, comment with guidance, then fail

### Safety

- Verify actor permissions before destructive operations (branch creation, deletion)
- Validate all user inputs from issue forms (dates, branch names, slugs)
- Use `github.rest.*` API calls — never shell out to `gh` CLI in workflows
- Never hardcode secrets; use `${{ secrets.* }}` or `${{ github.token }}`

### Workshop-Specific

- The `workshop-branch.yml` workflow creates dated branches from issue forms
- It checks both labels AND title prefix as heuristics (labels may be silently dropped
  when they don't exist in the repository yet)
- Only collaborators with write/maintain/admin permission can trigger branch creation

## Issue Templates (.github/ISSUE_TEMPLATE/)

- Use **YAML-based issue forms** (not markdown templates)
- Include `type: markdown` sections explaining what the form does
- Provide sensible defaults with `value:` where appropriate
- Use `type: checkboxes` with `required: true` for safety confirmations
- Use `type: dropdown` for controlled choices (avoid free-text where possible)
- Add clear `description:` for every input field
- Labels in the template should match labels that exist in the repository

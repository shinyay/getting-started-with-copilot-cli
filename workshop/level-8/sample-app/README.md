# DevOps Toolkit — Level 8 Sample App

A multi-service project with automation scripts, CI pipelines, and
security-sensitive configurations — used to practice **advanced Copilot
CLI features**: permissions, programmatic mode, sessions, and delegation.

## Structure

```
services/
├── api/             ← Express API service (Node.js)
└── worker/          ← Background job processor (Python)

scripts/
├── copilot-review.sh     ← Automated PR review via copilot -p
├── copilot-changelog.sh  ← Changelog generation via copilot -p
└── copilot-triage.sh     ← Issue triage via copilot -p

config/
├── production.env   ← SENSITIVE — Copilot should NOT read this
└── development.env  ← Safe for development

.github/workflows/
└── copilot-ci.yml   ← CI workflow demonstrating Copilot in pipelines
```

## Purpose

This is NOT a bug-fixing exercise. The codebase is intentionally simple.
The focus is on **how you use Copilot CLI** — its advanced flags, modes,
sessions, permissions, and integration with GitHub's ecosystem.

### Reset

```bash
git checkout -- workshop/level-8/sample-app/
```

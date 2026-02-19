# Level 8: Advanced — Permissions, Sessions & Delegation

> **Risk level:** 🔴 High awareness required — You will work with fine-grained permissions, security-sensitive files, automation scripts, and delegation to autonomous agents. Understanding what you authorize is critical.

## Learning Objectives

By the end of this level, you will be able to:

1. Control tool permissions with `--allow-tool` and `--deny-tool`
2. Restrict network access with `--allow-url` and `--deny-url`
3. Use **programmatic mode** (`-p`, `-s`) for scripted automation
4. Manage multiple sessions and switch between them
5. Configure **safety boundaries** for sensitive environments
6. Understand and use the **Copilot Coding Agent** for issue delegation
7. Integrate Copilot CLI into **CI/CD pipelines**
8. Understand the **Agent Control Plane (ACP)** and SDK concepts
9. Build **automation scripts** that wrap Copilot CLI
10. Apply advanced context strategies for large codebases
11. Make informed **delegation decisions** (human vs Copilot vs coding agent)
12. Synthesize all 8 levels into a personal mastery framework

---

## Prerequisites

- [ ] Completed **Levels 1–7** (all skills including customization)
- [ ] GitHub CLI (`gh`) installed and authenticated
- [ ] Copilot CLI installed and working
- [ ] Comfort with shell scripting (bash basics)

---

## About the Sample App

Level 8 uses a **DevOps Toolkit** — a multi-service project with automation scripts, CI pipelines, and security-sensitive configurations.

> Unlike previous levels which focused on a single application, this level uses a **multi-service, multi-language project** (Node.js API + Python worker) with shell scripts, CI workflows, and sensitive config files. The focus is not on the code itself but on how you **use Copilot** — permissions, automation, sessions, and delegation.

```
sample-app/
├── services/
│   ├── api/                  ← Node.js API (simple HTTP server)
│   └── worker/               ← Python background worker
├── scripts/
│   ├── copilot-review.sh     ← Automated PR review (copilot -p)
│   ├── copilot-changelog.sh  ← Changelog generation (copilot -p)
│   └── copilot-triage.sh     ← Issue triage (copilot -p)
├── config/
│   ├── production.env        ← ⚠️ SENSITIVE — fake credentials
│   └── development.env       ← Safe for development
├── .github/workflows/
│   └── copilot-ci.yml        ← CI pipeline with Copilot steps
└── Makefile
```

### ⚠️ Security Note

`config/production.env` contains **fake credentials** that simulate real production secrets. This file exists specifically to practice **restricting Copilot's access** to sensitive files.

---

## Workshop Structure

This level contains **12 exercises**. Estimated time: **90–120 minutes**.

| Exercise | Topic | Time |
|----------|-------|------|
| 1 | Fine-Grained Tool Permissions | 8 min |
| 2 | Network Access Controls | 7 min |
| 3 | Programmatic Mode Basics | 8 min |
| 4 | Building Automation Scripts | 10 min |
| 5 | Security Boundaries | 8 min |
| 6 | Session Management Deep Dive | 7 min |
| 7 | Multi-Session Workflows | 8 min |
| 8 | Copilot Coding Agent | 10 min |
| 9 | CI/CD Integration | 8 min |
| 10 | Agent Control Plane & SDK Concepts | 7 min |
| 11 | Delegation Decision Framework | 8 min |
| 12 | Capstone: Personal Mastery Framework | 10 min |

---

## Exercise 1: Fine-Grained Tool Permissions

### Goal
Master the `--allow-tool` and `--deny-tool` flags to control exactly what Copilot can do.

### Steps

**1.1** Start with default permissions (interactive approval):

```bash
cd workshop/level-8/sample-app
copilot
```

```
Create a new file called test.txt with the content "hello"
```

> Observe: you get an approval prompt for the `create` tool.

Exit and restart with pre-approved tools:

**1.2** Pre-approve specific tools:

```bash
copilot --allow-tool "view" --allow-tool "grep" --allow-tool "glob"
```

```
Show me the structure of services/api/ and find all JavaScript files
```

> Observe: `view`, `grep`, and `glob` execute without prompts. `create`, `edit`, and `bash` still require approval.

**1.3** Pre-approve write tools for a trusted session:

```bash
copilot --allow-tool "edit" --allow-tool "create" --allow-tool "view" --allow-tool "grep"
```

```
Add a comment to services/api/index.js: "// Level 8 exercise"
```

> Observe: the edit proceeds without an approval prompt.

**1.4** Deny a specific tool:

```bash
copilot --deny-tool "bash"
```

```
Run the tests with make test
```

> Observe: Copilot cannot use the `bash` tool at all — it's completely blocked. It should explain what it would do instead.

**1.5** Combine allow and deny:

```bash
copilot --allow-tool "view" --allow-tool "edit" --deny-tool "bash"
```

> This creates a session where Copilot can read and edit files but cannot execute any commands.

### Key Concept: Permission Matrix

| Flag | Effect |
|------|--------|
| `--allow-tool "X"` | Tool X runs without approval prompts |
| `--deny-tool "X"` | Tool X is completely blocked |
| Neither | Tool X requires interactive approval (default) |

| Scenario | Recommended Flags |
|----------|-------------------|
| Read-only exploration | `--allow-tool "view" --allow-tool "grep" --deny-tool "bash" --deny-tool "edit"` |
| Trusted editing session | `--allow-tool "view" --allow-tool "edit" --allow-tool "grep"` |
| Full auto-approve | `--allow-tool "view" --allow-tool "edit" --allow-tool "bash" --allow-tool "create"` |
| Maximum lockdown | `--deny-tool "bash" --deny-tool "edit" --deny-tool "create"` |

### ✅ Checkpoint
You can configure tool permissions for any trust level.

---

## Exercise 2: Network Access Controls

### Goal
Control Copilot's ability to access URLs and external resources.

### Steps

**2.1** Default behavior — allow all URLs:

```bash
copilot
```

```
Fetch the content of https://api.github.com/zen
```

> If web access tools are available, Copilot can fetch external URLs.

**2.2** Block all network access:

```bash
copilot --deny-url "*"
```

```
Fetch the content of https://api.github.com/zen
```

> Copilot should be unable to access any URL.

**2.3** Allow specific domains only:

```bash
copilot --allow-url "https://api.github.com/*" --deny-url "*"
```

> This creates a session that can only access GitHub's API — nothing else.

**2.4** Block sensitive internal URLs:

```bash
copilot --deny-url "https://*.internal/*" --deny-url "https://vault.*"
```

> This prevents Copilot from accessing internal services or secret vaults.

**2.5** Understand when URL controls matter:

```
When would you use --deny-url? Think about:
- Production environments with internal services
- Compliance requirements (data residency)
- Air-gapped or restricted networks
- Preventing accidental data exfiltration
```

### Key Concept: URL Permission Patterns

| Pattern | Matches |
|---------|---------|
| `*` | All URLs |
| `https://api.github.com/*` | Any GitHub API URL |
| `https://*.internal/*` | Any internal domain |
| `https://example.com/api/v1/*` | Specific API path |

### ✅ Checkpoint
You can control network access for any security requirement.

---

## Exercise 3: Programmatic Mode Basics

### Goal
Use Copilot CLI non-interactively for scripting and automation.

### Steps

**3.1** Basic programmatic mode:

```bash
copilot -p "What is 2 + 2? Reply with just the number."
```

> This runs Copilot non-interactively — sends the prompt, gets a response, exits.

**3.2** Silent mode (script-friendly output):

```bash
copilot -p "List the files in the current directory" -s
```

> `-s` strips Copilot's conversational framing — outputs only the essential content.

**3.3** Compare normal vs silent output:

```bash
echo "=== Normal ==="
copilot -p "What language is services/api/index.js written in?"

echo "=== Silent ==="
copilot -p "What language is services/api/index.js written in?" -s
```

**3.4** Pipe input to Copilot:

```bash
cat services/api/index.js | copilot -p "Review this code for issues" -s
```

> The file content is piped as stdin context.

**3.5** Capture output:

```bash
REVIEW=$(copilot -p "Summarize services/api/index.js in one sentence" -s)
echo "Review: $REVIEW"
```

> Copilot's output is captured in a shell variable.

**3.6** Use in a script:

```bash
for file in services/api/*.js services/worker/*.py; do
    echo "--- $file ---"
    copilot -p "In one line, what does $file do?" -s
    echo ""
done
```

> This loops through files and asks Copilot about each one.

### Key Concept: Programmatic Mode Flags

| Flag | Name | Purpose |
|------|------|---------|
| `-p "prompt"` | Programmatic | Non-interactive, single prompt |
| `-s` | Silent | Script-friendly output only |
| `-p "..." -s` | Combined | Best for automation scripts |

### ✅ Checkpoint
You can use Copilot non-interactively in shell scripts.

---

## Exercise 4: Building Automation Scripts

### Goal
Create and understand automation scripts that leverage Copilot CLI.

### Steps

**4.1** Read the existing review script:

```bash
copilot
```

```
@ scripts/copilot-review.sh

Explain this script: what does it do, how does it use copilot -p, 
and what are the edge cases?
```

**4.2** Read the changelog script:

```
@ scripts/copilot-changelog.sh

How does this script gather git history and pass it to Copilot?
```

**4.3** Read the triage script:

```
@ scripts/copilot-triage.sh

This script uses gh CLI + copilot CLI together. 
Explain the data flow: GitHub → gh CLI → shell → copilot -p → output
```

**4.4** Improve the review script:

```
The review script has a limitation: if the diff is very large, 
the prompt might exceed context limits. 

Add a check: if the diff is more than 500 lines, truncate it 
and add a note "... truncated (N lines omitted)".
```

**4.5** Create a new automation script:

```
Create a script scripts/copilot-summarize.sh that:
1. Accepts a directory path as argument
2. Lists all source files in the directory
3. For each file, asks Copilot for a one-line summary
4. Outputs a formatted table: filename | summary
5. Uses copilot -p -s for each call
```

**4.6** Test the script (dry run):

```
!bash scripts/copilot-summarize.sh services/api/ 2>&1 || echo "Expected: script created but copilot may not be available in this context"
```

### Key Concept: Automation Script Patterns

| Pattern | Use Case | Example |
|---------|----------|---------|
| **Review** | PR quality gate | `git diff | copilot -p "review" -s` |
| **Changelog** | Release notes | `git log | copilot -p "categorize" -s` |
| **Triage** | Issue management | `gh issue view | copilot -p "triage" -s` |
| **Summary** | Documentation | `for file; copilot -p "summarize" -s` |
| **Migration** | Code transforms | `copilot -p "convert X to Y" -s` |

### ✅ Checkpoint
You can build and understand automation scripts that wrap Copilot CLI.

---

## Exercise 5: Security Boundaries

### Goal
Configure Copilot to protect sensitive files and enforce security policies.

### Steps

**5.1** Demonstrate the risk — read production secrets:

```bash
copilot
```

```
@ config/production.env
What credentials are in this file?
```

> ⚠️ Copilot can read and display the fake production secrets. In a real project, this is a security risk.

**5.2** Create a `.copilotignore` that blocks sensitive files:

```
Create a .copilotignore file that excludes:
- config/production.env
- Any *.pem or *.key files
- Any .env files except development.env
- The .git directory
```

**5.3** Verify the protection:

```
@ config/production.env
Can you read this file?
```

> With `.copilotignore`, Copilot should not be able to load this file.

**5.4** Use tool permissions as a second layer:

```bash
copilot --deny-tool "bash"
```

> Even if `.copilotignore` is bypassed, blocking `bash` prevents `!cat config/production.env`.

**5.5** Create a security-hardened session:

```bash
copilot \
  --deny-tool "bash" \
  --deny-url "*" \
  --allow-tool "view" \
  --allow-tool "grep" \
  --allow-tool "edit"
```

> This session: can read and edit files, but cannot execute commands or access the network. Combined with `.copilotignore`, sensitive files are excluded from reads too.

**5.6** Document your security policy:

```
Create a docs/copilot-security-policy.md that documents:
1. Which files are excluded via .copilotignore
2. Recommended permission flags for different environments
3. What to do if Copilot accidentally displays secrets
```

### Key Concept: Defense in Depth

```
Layer 1: .copilotignore          ← Excludes files from context
Layer 2: --deny-tool "bash"      ← Blocks command execution
Layer 3: --deny-url "*"          ← Blocks network access
Layer 4: Custom instructions     ← "Never display API keys or passwords"
```

> 💡 **No single layer is sufficient.** Use all four together for sensitive environments.

### ✅ Checkpoint
You can configure multi-layered security boundaries for Copilot sessions.

---

## Exercise 6: Session Management Deep Dive

### Goal
Master session lifecycle — creation, continuation, resumption, and context reset.

### Steps

**6.1** Start a named session (conceptual):

```bash
copilot
```

```
Add a comment to services/api/index.js: "// Session exercise"
```

Note the session context — you're working on the API service.

**6.2** Exit and continue:

Press `Ctrl+C` or type `/exit` to exit.

```bash
copilot --continue
```

> Your conversation history and file context are restored.

**6.3** Verify context preservation:

```
What was the last thing we did?
```

> Copilot should remember the previous conversation.

**6.4** Clear context within a session:

```
/clear
```

```
What was the last thing we did?
```

> After `/clear`, Copilot no longer has the previous context.

**6.5** Exit and resume a different session:

```bash
copilot --resume
```

> This shows a list of recent sessions to choose from.

**6.6** Understand session storage:

```
Where are Copilot sessions stored on disk?
How much storage do they use?
Can I delete old sessions?
```

### Key Concept: Session Strategy Matrix

| Scenario | Command |
|----------|---------|
| Pick up where I left off | `copilot --continue` |
| Return to a specific session | `copilot --resume` |
| Start fresh, forget everything | `copilot` |
| Reset context but keep session | `/clear` |
| Permanently exit | `Ctrl+C` or `/exit` |

### ✅ Checkpoint
You can manage sessions for any workflow pattern.

---

## Exercise 7: Multi-Session Workflows

### Goal
Work on multiple tasks simultaneously using separate Copilot sessions.

### Steps

**7.1** Session 1 — work on the API service:

```bash
cd services/api
copilot
```

```
Add a new route: GET /version that returns { version: "1.0.0", commit: "abc123" }
```

Exit with `Ctrl+C`.

**7.2** Session 2 — work on the worker service:

```bash
cd ../../services/worker
copilot
```

```
Add a new job type "cleanup" that deletes completed jobs older than 24 hours
```

Exit with `Ctrl+C`.

**7.3** Resume Session 1:

```bash
cd ../api
copilot --resume
```

> Select the API session from the list. Continue working on the API.

**7.4** Resume Session 2:

```bash
cd ../worker
copilot --resume
```

> Select the worker session. Continue working on the worker.

**7.5** Understand multi-session strategies:

| Strategy | When to Use |
|----------|-------------|
| **One session, one task** | Focused work on a single feature |
| **Multiple sessions, different services** | Working across microservices |
| **Session per issue** | Tracking work by issue/ticket |
| **Disposable sessions** | Quick questions, then forget |

**7.6** Cross-session context:

```
I was working on the API service in another session. 
I added a /version endpoint. Can you see those changes from this session?
```

> Sessions are isolated. Changes on disk (saved files) are visible, but conversation context is not shared.

### ✅ Checkpoint
You can manage parallel sessions for multi-task workflows.

---

## Exercise 8: Copilot Coding Agent

### Goal
Understand how to delegate entire tasks to GitHub's Copilot Coding Agent via issues and PRs.

### Steps

**8.1** Understand what the Coding Agent is:

```
Explain the difference between:
1. Copilot CLI (what we've been using)
2. Copilot Coding Agent (assigns to issues/PRs)
3. Copilot in the IDE (VS Code, JetBrains)

When would you use each one?
```

**8.2** Learn the Coding Agent workflow:

```
Walk me through the Copilot Coding Agent workflow:
1. How do I assign an issue to it?
2. What does it do after assignment?
3. Where does its work appear?
4. How do I review and iterate on its changes?
```

**8.3** Write an agent-friendly issue:

```
Write a GitHub issue that would be good for the Copilot Coding Agent:
- Clear title
- Detailed acceptance criteria
- Specific files to modify
- Test expectations

Use this project (the DevOps Toolkit) as the context.
```

**8.4** Write a bad issue (and understand why):

```
Write an issue that would be BAD for the Copilot Coding Agent. 
Explain why it would fail or produce poor results.
```

**8.5** Agent vs CLI decision framework:

| Task Type | Best Tool | Why |
|-----------|-----------|-----|
| Quick fix, known file | **CLI** | Faster, immediate feedback |
| Multi-file feature | **Coding Agent** | Handles complexity, creates PR |
| Exploration/questions | **CLI** | Interactive conversation |
| Repetitive changes | **Coding Agent** | Batch processing |
| Security-sensitive | **CLI** | You control every step |
| Well-defined, testable | **Coding Agent** | Clear acceptance criteria |
| Ambiguous, needs discussion | **CLI** | Iterative refinement |

**8.6** PR review workflow for agent changes:

```
When the Coding Agent creates a PR, how should I review it?
What's different from reviewing a human's PR?
What should I look for specifically?
```

### Key Concept: Coding Agent Workflow

```
1. Create Issue          ← Clear title, acceptance criteria, test expectations
2. Assign to Copilot     ← @copilot or assign in UI
3. Agent creates branch  ← Autonomous implementation
4. Agent opens PR        ← With description of changes
5. You review PR         ← Like any code review
6. Iterate via comments  ← "Fix X", "Add test for Y"
7. Merge when ready      ← Standard merge flow
```

### ✅ Checkpoint
You understand the Coding Agent workflow and when to use CLI vs Agent.

---

## Exercise 9: CI/CD Integration

### Goal
Understand how to integrate Copilot CLI into continuous integration pipelines.

### Steps

**9.1** Read the CI workflow:

```
@ .github/workflows/copilot-ci.yml

Explain this workflow:
- What triggers it?
- What does each job do?
- What's placeholder vs real?
```

**9.2** Understand the PR review job:

```
The review-pr job gets the PR diff and would pass it to copilot -p.
What are the practical considerations?
- Token management
- Context limits (large PRs)
- Output formatting for PR comments
- Rate limiting
```

**9.3** Understand the triage job:

```
The triage-issue job would use copilot -p to triage new issues.
How would you post the triage result back to the issue as a comment?
```

**9.4** Design a real CI integration:

```
/plan Design a CI workflow that uses Copilot CLI for:
1. PR review: run copilot -p on the diff, post review as PR comment
2. Test failure analysis: if tests fail, use copilot -p to explain failures
3. Security scan: use copilot -p to review changes for security issues

What environment variables and secrets are needed?
How do you handle rate limits?
```

**9.5** CI security considerations:

```
What are the security risks of running Copilot in CI?
- Exposure of code to the AI model
- Token permissions
- Untrusted PRs from forks
- Cost control
```

**9.6** Best practices:

```
Create a docs/ci-copilot-guide.md with best practices for 
using Copilot CLI in GitHub Actions.
```

### Key Concept: CI Integration Architecture

```
GitHub Event (PR, Issue, Release)
    │
    ▼
GitHub Actions Workflow
    │
    ▼
copilot -p "prompt" -s      ← Non-interactive, silent
    │
    ▼
Post result via gh CLI       ← Comment on PR/Issue
```

### ✅ Checkpoint
You understand CI/CD integration patterns, security, and best practices.

---

## Exercise 10: Agent Control Plane & SDK Concepts

### Goal
Understand the broader Copilot ecosystem — ACP and SDK — and where CLI fits in.

### Steps

**10.1** Understand the ecosystem:

```
Explain the GitHub Copilot ecosystem:
1. Copilot in IDE (code completion)
2. Copilot Chat (IDE)
3. Copilot CLI (terminal)
4. Copilot Coding Agent (issues/PRs)
5. Copilot SDK (build your own)
6. Agent Control Plane (ACP)

How do they relate to each other?
```

**10.2** Understand ACP:

```
What is the Agent Control Plane (ACP)?
- What problem does it solve?
- How does it relate to MCP?
- Who would use it?
```

**10.3** Understand the SDK:

```
What can you build with the Copilot SDK?
- Custom AI tools
- IDE extensions
- Workflow integrations
- Enterprise-specific agents

Give me 3 concrete examples.
```

**10.4** When to extend vs when to use:

| Need | Solution |
|------|----------|
| Day-to-day coding | CLI + IDE |
| Repetitive automation | CLI programmatic mode + scripts |
| Team-wide tools | MCP servers |
| Enterprise workflow | SDK + ACP |
| Task delegation | Coding Agent |

**10.5** Map your organization's needs:

```
For a team of 10 developers working on 3 microservices:
- Which Copilot tools should they use?
- What custom integrations would help?
- What's the build vs buy decision?
```

### ✅ Checkpoint
You understand the Copilot ecosystem and where each component fits.

---

## Exercise 11: Delegation Decision Framework

### Goal
Build a systematic framework for deciding when to use which tool.

### Steps

**11.1** Review the delegation spectrum:

```
There's a spectrum from "fully manual" to "fully autonomous":

Manual ←────────────────────────────→ Autonomous
  │         │           │           │
  You    CLI+You    Coding     Automated
 alone   together    Agent      Pipeline

For each point on the spectrum, give an example task 
from this workshop.
```

**11.2** Create a decision tree:

```
Help me create a decision tree for delegation:

Question 1: Is the task well-defined with clear acceptance criteria?
  No → Use CLI interactively (iterate on requirements)
  Yes → Continue

Question 2: Does it need real-time human judgment?
  Yes → Use CLI interactively
  No → Continue

Question 3: Is it a single file or multi-file?
  ...continue building the tree
```

**11.3** Apply the framework to real scenarios:

| Scenario | Your Decision | Why |
|----------|--------------|-----|
| Fix a typo in README | ? | ? |
| Implement OAuth login | ? | ? |
| Add tests for 10 functions | ? | ? |
| Debug a production incident | ? | ? |
| Upgrade dependencies | ? | ? |
| Write API documentation | ? | ? |

**11.4** Evaluate delegation quality:

```
How do you measure whether a delegation was successful?
- Time saved vs time spent reviewing
- Quality of output
- Number of iterations needed
- Risk of missed issues
```

**11.5** Create a team delegation guide:

```
Create a docs/delegation-guide.md with:
1. Decision tree (from 11.2)
2. Tool selection matrix (from 11.3)
3. Quality checklist for reviewing delegated work
4. Escalation criteria (when to take back control)
```

### ✅ Checkpoint
You have a systematic framework for delegation decisions.

---

## Exercise 12: Capstone — Personal Mastery Framework

### Goal
Synthesize all 8 levels into a personal reference that you'll use daily.

### Steps

**12.1** Reflect on each level:

| Level | Key Skill | My Confidence (1-5) | Most Useful For |
|-------|-----------|---------------------|-----------------|
| 1. Observe | Read-only exploration | ? | ? |
| 2. Understand | Ask questions, get explanations | ? | ? |
| 3. Plan | Think before acting | ? | ? |
| 4. Create | Approve changes, verify with diff/review | ? | ? |
| 5. Execute | Run commands, interpret output | ? | ? |
| 6. Workflow | Complete development cycles | ? | ? |
| 7. Customize | Instructions, MCP, context | ? | ? |
| 8. Advanced | Permissions, sessions, delegation | ? | ? |

**12.2** Identify your daily workflow:

```
Based on all 8 levels, what would my ideal daily Copilot workflow look like?
Walk through a typical day:
- Morning: start session, load context
- Feature work: plan → implement → test → review
- Code review: /review on PRs
- Issue triage: programmatic mode
- End of day: commit, clean up
```

**12.3** Create your personal cheat sheet:

```
Create a docs/my-cheat-sheet.md that combines the most useful 
commands and patterns from all 8 levels into a single reference 
I can keep open while working.

Organize by task type:
1. Starting a session
2. Reading code
3. Planning changes
4. Making changes
5. Running tests
6. Reviewing code
7. Automating tasks
8. Security & permissions
```

**12.4** Set improvement goals:

```
Based on my self-assessment, what are my top 3 improvement goals?
For each goal, suggest:
- A specific exercise to repeat
- A daily practice habit
- A metric to track progress
```

**12.5** Plan your team rollout:

```
If I wanted to train my team on Copilot CLI:
- Which levels should they start with?
- What's the minimum viable training (2-hour workshop)?
- What ongoing practices should we establish?
- How do we measure team adoption success?
```

**12.6** Final exercise — full synthesis:

```
Give me a one-page summary of everything I learned across all 8 levels.
Structure it as:
- 8 key principles (one per level)
- 8 most-used commands
- 8 anti-patterns to avoid
- My recommended workflow
```

### ✅ Checkpoint
You have a personal mastery framework and a plan for continued growth.

---

## 🏆 Level 8 Self-Assessment (Final)

Rate yourself on each skill (1 = shaky, 3 = confident):

| # | Skill | 1 | 2 | 3 |
|---|---|---|---|---|
| 1 | Configure tool permissions (allow/deny) | ☐ | ☐ | ☐ |
| 2 | Control network access (URL permissions) | ☐ | ☐ | ☐ |
| 3 | Use programmatic mode for automation | ☐ | ☐ | ☐ |
| 4 | Build shell scripts wrapping Copilot CLI | ☐ | ☐ | ☐ |
| 5 | Configure multi-layered security boundaries | ☐ | ☐ | ☐ |
| 6 | Manage multiple sessions effectively | ☐ | ☐ | ☐ |
| 7 | Understand Copilot Coding Agent workflow | ☐ | ☐ | ☐ |
| 8 | Design CI/CD integrations with Copilot | ☐ | ☐ | ☐ |
| 9 | Understand ACP and SDK ecosystem | ☐ | ☐ | ☐ |
| 10 | Make informed delegation decisions | ☐ | ☐ | ☐ |
| 11 | Synthesize all 8 levels into a daily workflow | ☐ | ☐ | ☐ |
| 12 | Teach these skills to others | ☐ | ☐ | ☐ |

**Scoring:**
- **30–36:** 🎉 Copilot CLI Master — you're ready to teach others
- **22–29:** Re-practice exercises 3-5 (automation) and 8-9 (delegation)
- **Below 22:** Revisit Levels 5-7 before attempting Level 8 again

---

## Key Takeaways

1. **Permissions are your first line of defense** — configure them explicitly, not just "allow all"
2. **Programmatic mode unlocks automation** — `-p` and `-s` turn Copilot into a CLI tool
3. **Sessions have strategy** — continue vs resume vs fresh depends on the task
4. **Security is layered** — `.copilotignore` + `--deny-tool` + `--deny-url` + instructions
5. **The Coding Agent handles what CLI can't** — multi-file features with PR workflow
6. **CI integration requires careful security design** — tokens, permissions, fork handling
7. **Delegation is a spectrum** — manual → CLI → agent → pipeline, each has a place
8. **The ecosystem is bigger than CLI** — IDE, Chat, Agent, SDK, ACP all serve different needs
9. **Build your personal framework** — daily workflow + cheat sheet + decision tree
10. **Teach to solidify** — explaining Copilot to others deepens your own understanding

---

## 🎓 Congratulations

You've completed the full 8-level Copilot CLI learning path:

```
Level 1: Observe     — Read code safely
Level 2: Understand  — Ask questions, get explanations
Level 3: Plan        — Think before acting
Level 4: Create      — Make changes with verification
Level 5: Execute     — Run commands and interpret results
Level 6: Workflow    — Complete development cycles
Level 7: Customize   — Configure for your project
Level 8: Advanced    — Permissions, automation, delegation
```

You now have the skills to use Copilot CLI as a true development partner — not just a tool, but an extension of your workflow.

**Next steps:**
- Apply these skills to your real projects
- Share your knowledge with your team
- Contribute back: improve these workshop materials
- Stay current: Copilot evolves rapidly — check the docs quarterly

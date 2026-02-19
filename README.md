# Getting Started with GitHub Copilot CLI

> **Note:** GitHub Copilot CLI is currently in **Public Preview (with data protection)** and specifications may change. ([Docs][1])

> 📌 **Workshop Snapshot:** This workshop was authored and verified against
> **Copilot CLI v0.0.411** (released 2026-02-17) as of **2026-02-19**.
> Commands, slash commands, keyboard shortcuts, and behaviors described in
> the exercises reflect this version. If you are using a newer version,
> some details may differ — check `/changelog` inside Copilot CLI for
> what has changed since then.

## Description

**GitHub Copilot CLI** is a terminal-based **AI agent** that lets you have conversations while reading your codebase, editing files, and executing commands — all with approval steps in between. Beyond simple Q&A, Copilot CLI enables a complete **plan → execute → verify (test/build) → diff review** workflow entirely within the terminal. ([Docs][2])

### Key Characteristics

- Works across **Linux / macOS / Windows** (PowerShell / WSL). ([Docs][3])
- Two user interfaces: **Interactive** (with plan sub-mode) and **Programmatic** (`-p`). ([Docs][3])
- Editor-agnostic — edit in the terminal, confirm in any editor. ([Features][6])
- Integrates with **GitHub Issues and PRs** for end-to-end workflows. ([Docs][3])
- Extensible via **MCP servers**, **custom agents**, **skills**, and **plugins**. ([Docs][2])

---

## Requirement

- **Valid GitHub Copilot subscription** (Individual, Business, or Enterprise). ([Docs][1])
- **Node.js 22+** (if installing via npm). ([Docs][1])
- **PowerShell v6+** (Windows). ([Docs][1])
- Organization admins must **not have disabled** Copilot CLI for the org. ([Docs][1])

---

## Installation

### npm (All Platforms — Requires Node.js 22+)

```bash
npm install -g @github/copilot
```

### Windows (WinGet)

```powershell
winget install GitHub.Copilot
```

### macOS / Linux (Homebrew)

```bash
brew install copilot-cli
```

### macOS / Linux (Install Script)

```bash
curl -fsSL https://gh.io/copilot-install | bash
```

The script supports `PREFIX` and `VERSION` environment variables for pinning specific versions. ([Docs][1])

### Via GitHub CLI

```bash
gh extension install github/gh-copilot
gh copilot
```

> ⚠️ This installs the **`gh copilot` extension** — a different tool from the standalone `copilot` CLI. For the full agent experience, use one of the installation methods above.

([Docs][3])

### Download from GitHub.com

Download executables directly from the [releases page](https://github.com/github/copilot-cli/releases/). Unpack and run the executable for your platform.

---

## Quick Start

1. **Install** Copilot CLI (see [Installation](#installation) above).

2. **Navigate** to your target repository and launch:
   ```bash
   cd your-repo
   copilot
   ```
   ([Docs][2])

3. **Trust the folder** — Copilot will ask whether to trust the current directory since it may read, modify, and execute files within it. Options: ([Docs][2])
   - **Yes, proceed** — trust for this session only
   - **Yes, and remember this folder** — trust for this and future sessions
   - **No, exit (Esc)** — end the session

4. **Authenticate** — if not already logged in, run `/login`. ([Docs][1])
   - Alternatively, set a **fine-grained PAT** with the **"Copilot requests"** permission via `GH_TOKEN` or `GITHUB_TOKEN`. ([Docs][1])

5. **Try your first prompt:**
   ```
   What does this repository contain?
   ```

You're now ready to follow the Learning Path below.

---

## 🎓 Learning Path

This learning path is designed to take you from zero to productive with Copilot CLI. Work through each level in order — each one builds on skills from the previous level.

### Level 1: Observe — Read-Only Exploration (No Risk)

**Goal:** Get comfortable with the interactive UI and learn how Copilot reads your codebase. Nothing is modified at this level.

> 📂 Full workshop: [`workshop/level-1/`](workshop/level-1/) — 12 hands-on exercises with a sample Python app.

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 1-1 | Launch `copilot` in `workshop/level-1/sample-app/` and trust the folder | The trust prompt is a security gate — Copilot won't touch files until you consent |
| 1-2 | Type `/help` and read all sections | Discover all slash commands, shortcuts, and instruction file locations |
| 1-3 | Type `!ls -la` then `!wc -l *.py` | `!` runs shell commands **instantly** with zero AI token cost ([Docs][2]) |
| 1-4 | Ask: *"What is this project?"* | Copilot reads files to answer — observe tool approval prompts |
| 1-5 | Type `@ config.py` then ask: *"What options are available?"* | `@` injects file contents directly into context ([Docs][7]) |
| 1-6 | `@ task_manager.py` `@ models.py` then ask: *"Trace adding a new task"* | Deep multi-file exploration — data flow tracing |
| 1-7 | Ask: *"Count lines of Python code"* and observe the approval prompt | Understand Allow / Deny / Allow-for-session tool approval ([Docs][2]) |
| 1-8 | Type `/model`, `/usage`, then `/context` | Check your AI model, premium request stats, and token consumption ([Docs][3]) |
| 1-9 | Ask 3 follow-up questions about the same file without re-referencing it | Multi-turn conversation — Copilot remembers context across turns |
| 1-10 | Type `/compact` then `/context` to compare | Compress conversation history to free token space ([Docs][8]) |
| 1-11 | Exit (`Ctrl+C`), then `copilot --continue` | Session basics: exit, continue, and resume ([Docs][2]) |
| 1-12 | Ask *"How would I add X?"* vs *"Add X"* — and Deny the write | Distinguish questions (safe) from tasks (writes) — the Level 1 boundary |

**✅ Checkpoint:** You can navigate the UI, add file context, run shell commands, read tool approvals, manage context, and stay in read-only mode.

---

### Level 2: Understand — Ask Questions & Get Explanations

**Goal:** Use Copilot as a code understanding assistant. Still read-only — you're asking questions, not making changes.

> 📂 Full workshop: [`workshop/level-2/`](workshop/level-2/) — 12 hands-on exercises with a layered bookmark API app.

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 2-1 | Ask: *"Show the import dependency graph for all Python files"* | Map which file imports which — the foundation of any codebase |
| 2-2 | `@ app.py` `@ routes.py` `@ service.py` `@ repository.py` — ask about layers | Identify architectural layers and their responsibilities |
| 2-3 | *"Trace GET /bookmarks?tag=python from request to response"* | Top-down execution tracing through all layers |
| 2-4 | *"Where is DuplicateError raised? Trace up to the HTTP response"* | Bottom-up tracing — from component to all callers |
| 2-5 | `@ config.py` — ask: *"List all env vars with defaults and risks"* | Configuration audit and environment analysis |
| 2-6 | *"What design patterns are used? Which files implement them?"* | Pattern recognition (Repository, Factory, Exception hierarchy) |
| 2-7 | *"Find thread safety, validation, and error handling issues"* | Bug and code smell discovery without modifying code |
| 2-8 | *"What if the JSON file is deleted while the server runs?"* | Hypothetical reasoning — predict impact without changes |
| 2-9 | *"Compare InMemoryRepository vs FileRepository — which is better?"* | Compare implementations and articulate tradeoffs |
| 2-10 | *"Generate a complete API reference from routes.py"* | Documentation generation from code |
| 2-11 | *"Summarize this entire application in one paragraph"* | Knowledge synthesis — prove you understand the codebase |
| 2-12 | Try weak vs strong prompts on the same question — compare results | Advanced prompt crafting (structured, scoped, multi-step) |

**✅ Checkpoint:** You can map dependencies, trace execution paths, discover bugs, reason hypothetically, and craft deep prompts.

---

### Level 3: Plan — Think Before Acting

**Goal:** Learn to use Plan mode to create implementation plans **before** any code is written. This is the key habit that prevents runaway changes.

> 📂 Full workshop: [`workshop/level-3/`](workshop/level-3/) — 12 exercises with a note-taking app containing intentional bugs and TODOs.

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 3-1 | `/plan Fix the case-sensitive search bug in search.py` | Create your first plan and observe its structure ([Docs][7]) |
| 3-2 | Evaluate the plan: scope, completeness, safety, testing? | Read plans critically using a 6-point checklist |
| 3-3 | *"Too broad — focus only on X and Y"* then add constraints | Refine plans through iterative conversation |
| 3-4 | *"No — that's too big a change. Just add error handling"* | Reject plans with clear reasons and redirect |
| 3-5 | `/plan Fix the tag normalization bug` — consider data migration | Plan a bug fix (minimal change, backward-compatible) |
| 3-6 | `/plan Add search operators (tag:python, title:meeting)` | Plan a new feature (scope, interface, steps, testing) |
| 3-7 | `/plan Refactor the if/elif chain in notes.py` | Plan a refactoring (test-first, behavior-preserving) |
| 3-8 | Add constraints: *"Only modify export.py, max 30 lines, stdlib only"* | Plan with constraints that bound scope |
| 3-9 | `/plan Add a "last modified" sort` — trace through 3 files | Plan multi-file changes with safe implementation order |
| 3-10 | *"Give me 3 approaches — minimal, moderate, and robust"* | Compare alternative plans using a decision matrix |
| 3-11 | Plan from a user story with acceptance criteria | Translate requirements into concrete implementation plans |
| 3-12 | Review a complex plan against the 8-point checklist | Plan review as a repeatable skill (scope, risk, testing, migration, edge cases) |

**✅ Checkpoint:** You can create, evaluate, refine, reject, and compare plans — the foundation for every change you'll make in Levels 4–8.

---

### Level 4: Create — Make Your First Changes

**Goal:** Let Copilot make file changes while you learn the approval flow, verification, and recovery.

> 📂 Workshop: [`workshop/level-4/`](workshop/level-4/) — 12 exercises with the Quick Notes sample app (copy of Level 3, now you modify it)

| Exercise | What You'll Do | What You'll Learn |
|----------|---------------|-------------------|
| 4-1 | Create a `CHANGELOG.md` file from scratch | File creation — the safest first write operation |
| 4-2 | Try Allow, Deny, and Allow-for-session | The 3 approval choices and when to use each |
| 4-3 | Use `/diff` after changes | Inspect exactly what changed before committing |
| 4-4 | Use `/review` after changes | AI-powered quality assessment of your edits |
| 4-5 | Fix case-sensitive search bug | Plan → implement → diff → review → test workflow |
| 4-6 | Fix tag normalization bug | Bugs with data implications (existing vs new data) |
| 4-7 | Fix XSS vulnerability in HTML export | Security fixes with targeted verification |
| 4-8 | Fix pinned notes sorting | UX bugs verified through CLI output |
| 4-9 | Make multiple incremental edits to one file | Small changes with `/diff` checkpoints between each |
| 4-10 | Revert changes at various granularities | `git checkout -- file`, `git checkout -- .`, `git clean -fd` |
| 4-11 | Execute the full plan → implement → diff → review cycle | The 7-step workflow for non-trivial changes |
| 4-12 | Coordinate changes across multiple files | Cross-file consistency verification |

**✅ Checkpoint:** You can create files, fix bugs, review diffs, revert mistakes, and execute the complete 7-step change cycle.

---

### Level 5: Execute — Run Commands Through Copilot

**Goal:** Let Copilot execute commands (tests, builds, linters) and interpret results for you.

> 📂 Workshop: [`workshop/level-5/`](workshop/level-5/) — 12 exercises with a Math Utilities library (pytest, flake8, Makefile, 6 failing tests)

| Exercise | What You'll Do | What You'll Learn |
|----------|---------------|-------------------|
| 5-1 | Discover available commands from Makefile/scripts | Discovery before execution — read configs first |
| 5-2 | Run the full test suite through Copilot | `bash` tool approval and structured test output |
| 5-3 | Deep-dive into test failure analysis | What/why/where/severity of each failure |
| 5-4 | Fix bugs one at a time, re-running after each | The test → fix → re-run feedback loop |
| 5-5 | Run the linter and categorize warnings | Static analysis output: unused imports, style, docs |
| 5-6 | Fix lint violations without breaking tests | Lint → fix → re-lint → re-test cycle |
| 5-7 | Run demo/benchmark scripts and discuss output | Script output as conversation context |
| 5-8 | Inspect runtime environment through Copilot | Python version, packages, config diagnosis |
| 5-9 | Chain multiple commands in sequence | Sequential, conditional, and fan-out patterns |
| 5-10 | Handle command failures and error types | Distinguish test failure vs syntax error vs import error |
| 5-11 | Test-Driven Development — tests first, then implement | TDD with Copilot: you define behavior, Copilot codes |
| 5-12 | Let Copilot autonomously loop: test → fix → re-run | Agentic execution with human approval at every step |

**✅ Checkpoint:** You can run commands through Copilot, interpret output, fix bugs in loops, and guide autonomous test-fix cycles.

---

### Level 6: Workflow — The Full Plan → Execute → Review Cycle

**Goal:** Combine all skills into complete development workflows for realistic tasks.

> 📂 Workshop: [`workshop/level-6/`](workshop/level-6/) — 12 exercises with a URL Shortener CLI (multi-file bug, test gaps, feature gap, duplicated logic)

| Exercise | What You'll Do | What You'll Learn |
|----------|---------------|-------------------|
| 6-1 | Build URL expiration from scratch | Full plan → implement → test → diff → review cycle |
| 6-2 | Debug stats-wrong-after-delete bug | Multi-file investigation: reproduce → trace → root-cause → fix |
| 6-3 | Write tests for untested validator.py | Discover test gaps and fill them systematically |
| 6-4 | Extract duplicated validation logic | Safe refactoring: baseline tests → refactor → verify same green |
| 6-5 | Update README from actual code state | Documentation audit → update → verify examples |
| 6-6 | Simulate a pull request code review | Multi-angle review: correctness, security, testing, maintainability |
| 6-7 | Execute a minimal-change hotfix | Hotfix discipline: ≤5 lines, one concern, tiny `/diff` |
| 6-8 | Build feature + tests interleaved | Implement step → test step → implement step → test step |
| 6-9 | Translate vague requirements into code | Requirements refinement: clarify → decide → plan → implement |
| 6-10 | End-to-end: Issue → Plan → Code → Test → Review | The complete software development lifecycle in one exercise |
| 6-11 | Recover from a broken workflow | Fix forward vs revert — when each strategy is correct |
| 6-12 | Retrospective: analyze your own workflow | Identify patterns, inefficiencies, and improvement areas |

**✅ Checkpoint:** You can execute complete development workflows — features, bugs, refactors, hotfixes, and code reviews — using all Copilot CLI skills.

---

### Level 7: Customize — Make Copilot Work Your Way

**Goal:** Configure Copilot's behavior to match your project's conventions and optimize context management.

> 📂 Workshop: [`workshop/level-7/`](workshop/level-7/) — 12 exercises with a TypeScript Event API (conventions, MCP, context optimization)

| Exercise | What You'll Do | What You'll Learn |
|----------|---------------|-------------------|
| 7-1 | Write `.github/copilot-instructions.md` from codebase analysis | Custom instructions: specific, actionable, with examples |
| 7-2 | Generate code and verify it follows instructions | Testing instructions iteratively — refine when Copilot deviates |
| 7-3 | Practice targeted `@` references for different tasks | Context optimization: right files for right tasks |
| 7-4 | Create `.copilotignore` to exclude generated/vendor files | Keep context clean — exclude noise automatically |
| 7-5 | Build reusable prompt templates for your team | Standardized quality: service, endpoint, bug fix, review templates |
| 7-6 | Learn MCP server architecture and use cases | Model Context Protocol: what it is, how it extends Copilot |
| 7-7 | Configure MCP servers for the project | MCP config: project-level vs user-level, security best practices |
| 7-8 | Master session lifecycle: continue, resume, clear | Session management for multi-task workflows |
| 7-9 | Set up terminal integration with `/terminal-setup` | Multiline input, shell integration, keyboard shortcuts |
| 7-10 | Work across multiple projects with context boundaries | Monorepo patterns, cross-directory references |
| 7-11 | Layer instructions at org, repo, personal, and session levels | Instruction priority: session > personal > repo > org |
| 7-12 | Audit configuration effectiveness and create setup checklist | Measure ROI: custom instructions = highest impact |

**✅ Checkpoint:** You can customize Copilot per-project, optimize context, configure MCP servers, and manage sessions for maximum productivity.

---

### Level 8: Advanced — Permissions, Sessions & Delegation

**Goal:** Master fine-grained permissions, programmatic automation, session management, and autonomous agent delegation.

> 📂 Workshop: [`workshop/level-8/`](workshop/level-8/) — 12 exercises with a DevOps Toolkit (multi-service, automation scripts, CI, security configs)

| Exercise | What You'll Do | What You'll Learn |
|----------|---------------|-------------------|
| 8-1 | Configure `--allow-tool` and `--deny-tool` flags | Fine-grained tool permissions: pre-approve, block, default |
| 8-2 | Control network access with `--allow-url` / `--deny-url` | URL permission patterns for security and compliance |
| 8-3 | Use `copilot -p "prompt" -s` for scripted automation | Programmatic mode: non-interactive, silent, pipeable |
| 8-4 | Build and enhance automation shell scripts | Wrap Copilot CLI for review, changelog, triage automation |
| 8-5 | Configure multi-layered security boundaries | Defense in depth: `.copilotignore` + deny-tool + deny-url + instructions |
| 8-6 | Master session lifecycle: continue, resume, clear | Session strategies for different workflow patterns |
| 8-7 | Work across multiple services with parallel sessions | Multi-session workflows: one session per task/service |
| 8-8 | Understand the Copilot Coding Agent workflow | Issue → assign → PR → review → iterate → merge |
| 8-9 | Design CI/CD integrations with Copilot CLI | Pipeline patterns: PR review, test analysis, security scan |
| 8-10 | Explore ACP and SDK ecosystem concepts | Copilot ecosystem: CLI, Agent, IDE, MCP, SDK, ACP |
| 8-11 | Build a delegation decision framework | Decision tree: manual → CLI → agent → pipeline |
| 8-12 | Capstone: create your personal mastery framework | Synthesize all 8 levels into daily workflow + cheat sheet |

**✅ Checkpoint:** You can configure permissions, automate with programmatic mode, delegate to the Coding Agent, and synthesize all skills into a personal mastery framework.

---

### 🏆 Summary: Key Commands Cheat Sheet

> 📋 **Per-level cheat sheets** are available in each workshop directory (e.g., [`workshop/level-1/CHEATSHEET.md`](workshop/level-1/CHEATSHEET.md)).

| Category | Command / Syntax | Purpose |
|----------|-----------------|---------|
| **Context** | `@ filename` | Add file to conversation context |
| **Shell** | `!command` | Run shell command directly (no AI) |
| **Planning** | `/plan` | Create implementation plan |
| **Review** | `/diff` | View working directory changes |
| **Review** | `/review` | AI-powered self-review of changes |
| **Delegate** | `/delegate` or `& prompt` | Hand off work to Copilot Coding Agent remotely |
| **Session** | `/compact` | Compress conversation history |
| **Session** | `/context` | Visualize token usage |
| **Session** | `/usage` | View premium request stats |
| **Session** | `/clear` | Reset context within session |
| **Session** | `/share` | Share session to Markdown or gist |
| **Model** | `/model` | View/switch AI models |
| **Setup** | `/init` | Scaffold repo configuration |
| **Setup** | `/login` | Authenticate with GitHub |
| **Setup** | `/terminal-setup` | Configure shell for multiline input |
| **Agents** | `/agent` | Browse and select from available agents |
| **Agents** | `/fleet` | Enable fleet mode for parallel subagent execution |
| **Agents** | `/tasks` | View and manage background tasks |
| **Extensions** | `/skills` | Manage skills for enhanced capabilities |
| **Extensions** | `/mcp` | Manage MCP server configuration |
| **Extensions** | `/plugin` | Manage plugins and plugin marketplaces |
| **Info** | `/instructions` | View and toggle custom instruction files |
| **Info** | `/changelog` | Display changelog for CLI versions |
| **Launch** | `copilot --continue` | Resume last session |
| **Launch** | `copilot --resume` | Browse and restore sessions |
| **Launch** | `copilot -p "prompt"` | One-shot programmatic mode |
| **Launch** | `copilot -p "prompt" -s` | Silent programmatic mode |
| **Permissions** | `--allow-tool` / `--deny-tool` | Fine-grained tool control |
| **Permissions** | `--allow-url` / `--deny-url` | Fine-grained URL control |
| **Permissions** | `--allow-all` / `--yolo` | Allow everything (⚠️ caution) |

---

## Features (Detailed Reference)

### 🤖 User Interfaces and Modes

#### A) Interactive Interface (Default)

The standard conversational UI in the terminal for continuous work. ([Docs][3])

- Handles both general questions and implementation tasks.
- Dangerous operations (file changes, command execution) require **explicit approval**. ([Docs][2])
- Press `Shift+Tab` to cycle between modes within the interactive interface:
  - **Default mode** — ask questions and execute tasks
  - **Plan mode** — build structured implementation plans before coding ([Docs][7])
  - **Autopilot mode** — agent continues working until task completion (press `Shift+Tab` to cycle)

#### B) Programmatic Interface

Pass a single prompt via `-p` / `--prompt` for **non-interactive, one-shot execution**. ([Docs][7])

```bash
copilot -p "Run the tests in this repo and summarize any failures"
```

Additional flags for scripting:
- `-s` / `--silent` — output only the response.
- Session sharing via Markdown or secret gist. ([Docs][7])

---

### 🔒 Safety Model: Approvals, Permissions & Restrictions

#### Approval-Based Execution

When Copilot attempts to use tools involving **modifications or execution** (e.g., `touch`, `chmod`, `node`, `sed`), you are prompted for approval. ([Docs][2])
You can also choose to **auto-approve a specific tool for the current session**. ([Docs][2])

#### Allow All (Use with Caution)

`--allow-all` or `--yolo` grants all permissions (tools, paths, URLs) at once. This is equivalent to `--allow-all-tools --allow-all-paths --allow-all-urls`. **Only use in trusted environments.** ([Docs][8])

#### Fine-Grained Permission Control

| Option | Purpose |
|---|---|
| `--allow-tool` / `--deny-tool` | Permit or block specific tools |
| `--allow-url` / `--deny-url` | Control web access by URL |
| `--allow-all-tools` | Auto-approve all tools without prompting |
| `--allow-all-paths` | Disable file path verification |
| `--allow-all-urls` | Allow access to all URLs |
| `--available-tools` | Limit tools visible to the model |
| `--excluded-tools` | Exclude specific tools entirely |
| `--disallow-temp-dir` | Prevent automatic access to system temp directory |

Tool specification syntax for `--allow-tool` / `--deny-tool`:

| Syntax | Example | Effect |
|--------|---------|--------|
| `'shell(COMMAND)'` | `--deny-tool 'shell(rm)'` | Block a specific shell command |
| `'shell(git SUBCMD)'` | `--deny-tool 'shell(git push)'` | Block a git/gh subcommand |
| `'write'` | `--allow-tool 'write'` | Allow file modifications |
| `'MCP_SERVER(tool)'` | `--deny-tool 'MyMCP(tool_name)'` | Block a specific MCP tool |

([Docs][7])

---

### 📂 Context & Session Management

#### Session Restore

- `--resume` or `/resume` — switch between and restore local/remote sessions. ([Docs][2])
- `--continue` — quickly resume the most recent session. ([Docs][2])

#### Context Management (Token Awareness)

| Command | Purpose |
|---|---|
| `/usage` | View premium request and token consumption stats ([Docs][8]) |
| `/context` | Visualize token usage ([Docs][8]) |
| `/compact` | Summarize conversation history (context compression) ([Docs][8]) |

When token usage reaches ~95% of the limit, **automatic history compression** is triggered. ([Docs][8])

---

### 🧩 Custom Instructions, Custom Agents & MCP

#### Custom Instructions

Copilot CLI automatically reads Markdown instruction files from multiple locations. All instruction files **combine** (they are not priority-based fallbacks): ([Docs][2])

| File / Path | Scope |
|---|---|
| `.github/copilot-instructions.md` | Repository-wide |
| `.github/instructions/**/*.instructions.md` | Path-specific (glob-matched) |
| `.github/AGENTS.md` | Coding Agent-specific |
| `CLAUDE.md` / `GEMINI.md` | Model-specific instructions (in git root & cwd) |
| `$HOME/.copilot/copilot-instructions.md` | User-level (all projects) |
| `COPILOT_CUSTOM_INSTRUCTIONS_DIRS` | Additional directories (env var) |

> 💡 **Tip:** Try creating these files in your own projects to see how Copilot CLI adapts its behavior.
> For example, a `.github/copilot-instructions.md` with your coding conventions will make Copilot
> generate code that matches your team's style automatically.

#### Custom Agents

Define agent profiles (Markdown) specifying **expertise, tools, and instructions** to create specialized agents.
Copilot CLI includes built-in agents that it automatically delegates tasks to: ([Docs][2])

| Agent | Description |
|-------|-------------|
| **Explore** | Quick codebase analysis — answer questions without adding to main context |
| **Task** | Execute commands (tests, builds) — brief summaries on success, full output on failure |
| **General-purpose** | Complex multi-step tasks with full toolset in a separate context |
| **Code-review** | Review changes surfacing only genuine issues, minimizing noise |

Custom agents can be defined at user (`~/.copilot/agents`), repository (`.github/agents`),
or organization level (`.github-private/agents`). Use `/agent` to browse or `--agent=NAME` to specify. ([Docs][2])

#### Agent Skills (Reusable Prompts)

Prompt files (`.github/prompts/*.prompt.md`) define **reusable, invocable skills** that standardize
common workflows. Unlike instructions (passive context), prompts are actively triggered by name.

Use `/prompt` to browse available prompts, or invoke one directly by name. Create your own in
`.github/prompts/` to standardize repetitive tasks like code reviews, documentation updates, or
test generation. Each prompt file uses YAML front matter to specify its mode (`agent` or `edit`)
and a description.

#### Agent Skills (Auto-Loaded by Copilot)

Agent Skills (`.github/skills/*/SKILL.md`) are an [open standard](https://github.com/agentskills/agentskills) —
folders of instructions, scripts, and resources that Copilot **automatically loads when relevant** based on the
skill's description. Unlike prompt files (explicitly invoked), skills are injected into context when Copilot
determines they match the current task. Use `/skills` to browse available skills.

#### MCP (Model Context Protocol) Integration

Copilot CLI supports MCP server integration for extending tools and context. ([Features][6])

- GitHub MCP server is **included by default**. Use `/mcp` to manage servers. ([Docs][2])
- Default config location: `~/.copilot/mcp-config.json` (configurable via `XDG_CONFIG_HOME`). ([Docs][2])
- Use `--disable-builtin-mcps` to control built-in MCP servers (e.g., `github-mcp-server`). ([Docs][7])
- Per-session MCP: `--additional-mcp-config` for temporary server configuration. ([Docs][7])

#### Delegation to Coding Agent

Hand off work from the CLI to Copilot Coding Agent on GitHub while preserving session context: ([Docs][2])

```bash
# Via slash command
/delegate complete the API integration tests

# Via & prefix
& complete the API integration tests
```

Copilot commits unstaged changes as a checkpoint, creates a branch, and opens a draft PR.

#### Hooks

Hooks execute custom shell commands at key points during agent execution, enabling validation, logging, security scanning, or workflow automation. ([Docs][3])

#### Copilot Memory

Copilot Memory builds persistent understanding of your repository by storing "memories" — coding conventions, patterns, and preferences Copilot deduces as it works. This reduces the need to repeatedly explain context across sessions. ([Docs][3])

#### LSP (Language Server Protocol)

Copilot CLI supports LSP for enhanced code intelligence (go-to-definition, hover, diagnostics). Configure via `~/.copilot/lsp-config.json` (user-level) or `.github/lsp.json` (repo-level). Use `/lsp` to manage. ([Docs][2])

---

### 🧠 Model Selection

- Default model: **Claude Sonnet 4.5** (changeable via `/model` or `--model`). ([Docs][3])
- **Claude Sonnet 4.6** added (2026-02-17) — excels in agentic coding and search operations. ([Blog][13])
- **GPT-5 mini** and **GPT-4.1** were added (2026-01-14) and are **included in Copilot subscriptions** without consuming premium requests. ([Blog][9])
- Copilot CLI usage itself **consumes premium request quota** (multiplier shown in model list). ([Features][6])
- View session stats with `/usage`. ([Docs][8])

> **Tip:** Use non-premium models for lightweight checks and high-performance models for complex tasks.

---

### 🔌 ACP (Agent Client Protocol)

Copilot CLI implements **ACP**, allowing third-party IDEs and automation systems to invoke Copilot's agent capabilities. ([Blog][10])

#### Starting ACP

```bash
# stdio mode
copilot --acp

# TCP mode
copilot --acp --port 8080
```

#### ACP Client Capabilities

- Feature discovery
- Per-working-directory session creation
- Prompts with text, images, and context resources
- Streaming responses
- Tool execution permission handling
- Cancel / session lifecycle management

([Blog][10])

---

### 📦 Copilot SDK (Embed the Agent in Your App)

The **Copilot SDK** lets you embed Copilot's agent execution loop (planner + tool loop + runtime) directly into your applications. ([Blog][4])

#### Architecture

```
Your Application
       ↓
  SDK Client
       ↓ JSON-RPC
Copilot CLI (server mode)
```

The SDK manages the CLI process lifecycle automatically. ([SDK Repo][5])

#### Quick Start (TypeScript)

```ts
import { CopilotClient } from "@github/copilot-sdk";
const client = new CopilotClient();

await client.start();
const session = await client.createSession({ model: "gpt-5" });
await session.send({ prompt: "Hello, world!" });
```

([Blog][4])

#### SDK Installation

```bash
# Node.js / TypeScript
npm install @github/copilot-sdk

# Python
pip install github-copilot-sdk

# Go
go get github.com/github/copilot-sdk/go

# .NET
dotnet add package GitHub.Copilot.SDK
```

([SDK Repo][5])

#### SDK Authentication

| Method | Description |
|---|---|
| GitHub signed-in user | Uses `copilot` CLI login OAuth credentials |
| OAuth GitHub App | Pass your OAuth app's user token |
| Environment variables | `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN` |
| BYOK (Bring Your Own Key) | Use your own LLM provider API key (no GitHub auth needed) |

([SDK Repo][5])

> **⚠️ Important:** The SDK defaults to `--allow-all` permissions. For production/internal tools, configure **tool allowlists**, **fixed working directories**, and **URL domain restrictions** from the start. ([SDK Repo][5])

---

## Best Practices

1. **Plan first, then implement** — Use `/plan` to generate a plan before large changes. ([Docs][7])
2. **Diff → Review → Test before commit** — Make `/diff` and `/review` a pre-commit ritual. ([Docs][7])
3. **Use custom instructions strategically** — Place design principles, naming conventions, test policies, and prohibitions in `.github/copilot-instructions.md`. Use path-specific instructions (`.github/instructions/`) for language- or directory-scoped rules, and `AGENTS.md` for Coding Agent behavior. ([Docs][2])
4. **Choose models by task weight** — Lightweight checks on non-premium models, heavy work on high-performance models.
5. **Start read-only, then graduate to writes** — Build trust in the approval flow before allowing file modifications.
6. **Use `/compact` proactively** — Don't wait for the 95% auto-compression; compress when switching tasks to keep context focused.
7. **Lock down permissions for sensitive repos** — Use `--deny-tool` and `--deny-url` to restrict what Copilot can do in production-adjacent environments.

---

## ⚠️ Note on Legacy Package

If you previously used `@githubnext/github-copilot-cli`, that is a **separate, unmaintained package**. The current official Copilot CLI is **`@github/copilot`**. ([npm][12])

---

## References

- [Installing Copilot CLI][1]
- [Using Copilot CLI][2]
- [About Copilot CLI][3]
- [Copilot SDK Blog Post][4]
- [Copilot SDK Repository][5]
- [Copilot CLI Features Page][6]
- [CLI Command Reference][7]
- [Advanced CLI Usage][8]
- [Copilot CLI Changelog (2026-01-14)][9]
- [ACP Support Changelog][10]
- [Copilot SDK Technical Preview Changelog][11]
- [Claude Sonnet 4.6 GA Changelog][13]

[1]: https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli
[2]: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli
[3]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[4]: https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/
[5]: https://github.com/github/copilot-sdk
[6]: https://github.com/features/copilot/cli
[7]: https://docs.github.com/en/copilot/reference/cli-command-reference
[8]: https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli
[9]: https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/
[10]: https://github.blog/changelog/2026-01-28-acp-support-in-copilot-cli-is-now-in-public-preview/
[11]: https://github.blog/changelog/2026-01-14-copilot-sdk-in-technical-preview/
[12]: https://www.npmjs.com/package/@githubnext/github-copilot-cli
[13]: https://github.blog/changelog/2026-02-17-claude-sonnet-4-6-is-now-generally-available-in-github-copilot/

---

## Licence

Released under the [MIT license](https://gist.githubusercontent.com/shinyay/56e54ee4c0e22db8211e05e70a63247e/raw/f3ac65a05ed8c8ea70b653875ccac0c6dbc10ba1/LICENSE)

## Author

- github: <https://github.com/shinyay>
- twitter: <https://twitter.com/yanashin18618>
- mastodon: <https://mastodon.social/@yanashin>

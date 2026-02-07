# Getting Started with GitHub Copilot CLI

> **Note:** GitHub Copilot CLI is currently in **Public Preview (with data protection)** and specifications may change. ([Docs][1])

## Description

**GitHub Copilot CLI** is a terminal-based **AI agent** that lets you have conversations while reading your codebase, editing files, and executing commands — all with approval steps in between. Beyond simple Q&A, Copilot CLI enables a complete **plan → execute → verify (test/build) → diff review** workflow entirely within the terminal. ([Docs][2])

### Key Characteristics

- Works across **Linux / macOS / Windows** (PowerShell / WSL). ([Docs][3])
- Offers three execution modes: **Interactive / Plan / Programmatic**. ([Docs][3])
- Editor-agnostic — edit in the terminal, confirm in any editor. ([Features][6])
- Integrates with **GitHub Issues and PRs** for end-to-end workflows. ([Docs][3])

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

([Docs][3])

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
   - Allow for this session only
   - Always trust this folder
   - Cancel (Esc)

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

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 1-1 | Ask: *"What does this repository contain?"* | Copilot can read and summarize your project structure |
| 1-2 | Ask: *"List all files in this project"* | Copilot uses tools (like `ls`, `find`) — observe the approval prompt |
| 1-3 | Type `@ README.md` then ask: *"Summarize this file"* | `@` adds a specific file to the conversation context ([Docs][7]) |
| 1-4 | Type `!git log --oneline -5` | `!` executes shell commands **without** calling the AI model ([Docs][2]) |
| 1-5 | Type `/usage` | See your premium request and token consumption ([Docs][8]) |
| 1-6 | Type `/model` | View available models and the current default ([Docs][3]) |

**✅ Checkpoint:** You can navigate the UI, add file context, run shell commands, and check usage stats.

---

### Level 2: Understand — Ask Questions & Get Explanations

**Goal:** Use Copilot as a code understanding assistant. Still read-only — you're asking questions, not making changes.

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 2-1 | Ask: *"Explain the structure of this project"* | Copilot synthesizes information across multiple files |
| 2-2 | `@ <any-source-file>` then ask: *"What does this file do?"* | Deep file-level explanation with context |
| 2-3 | Ask: *"What dependencies does this project use?"* | Copilot reads config files (package.json, requirements.txt, etc.) |
| 2-4 | Ask: *"Are there any potential issues or bugs in this codebase?"* | Copilot performs lightweight code analysis |
| 2-5 | Type `/context` | Visualize how much of the token window you've used ([Docs][8]) |
| 2-6 | Type `/compact` | Compress conversation history to free up token space ([Docs][8]) |

**✅ Checkpoint:** You can use Copilot to understand unfamiliar code and manage your conversation context efficiently.

---

### Level 3: Plan — Think Before Acting

**Goal:** Learn to use Plan mode to create implementation plans **before** any code is written. This is the key habit that prevents runaway changes.

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 3-1 | Type `/plan Add a CONTRIBUTING.md to this repo` | Copilot generates a step-by-step plan for review ([Docs][7]) |
| 3-2 | Read the plan and ask: *"Can you add a section about code style?"* | Plans are editable through conversation |
| 3-3 | Type `/plan Refactor the README into smaller sections` | Practice planning on an existing file |
| 3-4 | Reject the plan (type *"Actually, let's not do this"*) | Learn that plans don't commit you to anything |

**✅ Checkpoint:** You can create, review, refine, and reject implementation plans before any files are touched.

---

### Level 4: Create — Make Your First Changes

**Goal:** Let Copilot make file changes while you learn the approval flow and review process.

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 4-1 | Ask: *"Create a simple hello.sh script that prints Hello World"* | File creation — observe the **approval prompt** before the file is written |
| 4-2 | After the file is created, type `/diff` | View exactly what changed in your working directory ([Docs][7]) |
| 4-3 | Type `/review` | Copilot analyzes its own changes (pre-commit self-review) ([Docs][8]) |
| 4-4 | Ask: *"Add a comment header to hello.sh with author and date"* | Incremental edits to an existing file |
| 4-5 | Type `/diff` again | See the cumulative diff grow |
| 4-6 | Use `!git diff` to verify outside Copilot | Cross-check: the `!` shortcut runs git directly |

**✅ Checkpoint:** You can create files, review diffs, and verify changes before committing. You understand the approval flow.

---

### Level 5: Execute — Run Commands Through Copilot

**Goal:** Let Copilot execute commands (tests, builds, linters) and interpret results for you.

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 5-1 | Ask: *"Run `bash hello.sh` and show me the output"* | Copilot executes commands with your approval ([Docs][2]) |
| 5-2 | Ask: *"Run lint on this project and fix any issues"* | Copilot chains: run tool → read output → make fixes |
| 5-3 | Ask: *"Run the tests and summarize failures"* | Copilot interprets test output and explains problems |
| 5-4 | Approve a tool, then choose *"Auto-approve for this session"* | Session-scoped auto-approval saves repeated confirmations ([Docs][2]) |

**✅ Checkpoint:** You can let Copilot run commands, interpret results, and make targeted fixes — all with appropriate approval.

---

### Level 6: Workflow — The Full Plan → Execute → Review Cycle

**Goal:** Combine everything into the complete Copilot CLI workflow for a real task.

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 6-1 | `/plan Add a .gitignore file appropriate for this project` | Start with a plan |
| 6-2 | Approve the plan and let Copilot execute | Plan → implementation |
| 6-3 | `/diff` then `/review` | Review the changes |
| 6-4 | Ask: *"Commit these changes with an appropriate message"* | Copilot can stage and commit (with approval) |
| 6-5 | Exit Copilot (`Ctrl+C` or `/exit`) | Clean session exit |
| 6-6 | Restart with `copilot --continue` | Resume the most recent session ([Docs][2]) |

**✅ Checkpoint:** You can execute the full workflow: plan → implement → diff → review → commit → resume.

---

### Level 7: Customize — Make Copilot Work Your Way

**Goal:** Configure Copilot's behavior to match your project's conventions and your personal workflow.

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 7-1 | Create `.github/copilot-instructions.md` with: *"Always use TypeScript. Prefer functional style."* | Repository-wide custom instructions ([Docs][2]) |
| 7-2 | Ask Copilot to write some code and observe it following your instructions | Instructions are automatically loaded |
| 7-3 | Type `/init` | Scaffold agent configuration files for your repo ([Docs][7]) |
| 7-4 | Try switching models: `/model` → select a different model | Different models for different tasks ([Docs][3]) |
| 7-5 | Try programmatic mode from outside: `copilot -p "Summarize this repo"` | One-shot, non-interactive execution ([Docs][7]) |
| 7-6 | Try silent mode: `copilot -p "List all TODOs" -s` | Script-friendly output — only the response ([Docs][7]) |

**✅ Checkpoint:** You can customize Copilot's behavior per-repo, switch models, and use programmatic mode for automation.

---

### Level 8: Advanced — Permissions, Sessions & Delegation

**Goal:** Master fine-grained control, session management, and advanced features.

| Step | What to Try | What You'll Learn |
|------|------------|-------------------|
| 8-1 | Launch with `copilot --allow-tool bash` | Pre-approve specific tools at startup ([Docs][7]) |
| 8-2 | Launch with `copilot --deny-url "*"` | Block all web access for a locked-down session ([Docs][7]) |
| 8-3 | After some work, exit and use `copilot --resume` | Browse and restore past sessions ([Docs][2]) |
| 8-4 | Type `/delegate` | Delegate work to a remote AI-generated PR ([Docs][7]) |
| 8-5 | Explore `--available-tools` and `--excluded-tools` | Control exactly which tools the model can see ([Docs][7]) |
| 8-6 | Try `copilot --yolo` in a **safe sandbox only** | Understand `--allow-all` and why it's risky ([Docs][8]) |

**✅ Checkpoint:** You can lock down or open up permissions, manage multiple sessions, and delegate work remotely.

---

### 🏆 Summary: Key Commands Cheat Sheet

| Category | Command / Syntax | Purpose |
|----------|-----------------|---------|
| **Context** | `@ filename` | Add file to conversation context |
| **Shell** | `!command` | Run shell command directly (no AI) |
| **Planning** | `/plan` | Create implementation plan |
| **Review** | `/diff` | View working directory changes |
| **Review** | `/review` | AI-powered self-review of changes |
| **Session** | `/compact` | Compress conversation history |
| **Session** | `/context` | Visualize token usage |
| **Session** | `/usage` | View premium request stats |
| **Session** | `/login` | Authenticate with GitHub |
| **Model** | `/model` | View/switch AI models |
| **Setup** | `/init` | Scaffold repo configuration |
| **Delegate** | `/delegate` | Create AI-generated PR remotely |
| **Launch** | `copilot --continue` | Resume last session |
| **Launch** | `copilot --resume` | Browse and restore sessions |
| **Launch** | `copilot -p "prompt"` | One-shot programmatic mode |
| **Launch** | `copilot -p "prompt" -s` | Silent programmatic mode |
| **Permissions** | `--allow-tool` / `--deny-tool` | Fine-grained tool control |
| **Permissions** | `--allow-url` / `--deny-url` | Fine-grained URL control |
| **Permissions** | `--yolo` | Allow everything (⚠️ caution) |

---

## Features (Detailed Reference)

### 🤖 Three Execution Modes

#### A) Interactive Mode (Default)

The standard conversational UI in the terminal for continuous work. ([Docs][3])

- Handles both general questions and implementation tasks.
- Dangerous operations (file changes, command execution) require **explicit approval**. ([Docs][2])

#### B) Plan Mode

Create and review an **implementation plan** before any code is written. ([Docs][3])

- Use `/plan` to generate step-by-step plans. ([Docs][7])
- Review, edit, and approve the plan before execution begins.

#### C) Programmatic Mode

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

`--allow-all` or `--yolo` grants all permissions (tools, paths, URLs) at once. **Only use in trusted environments.** ([Docs][8])

#### Fine-Grained Permission Control

| Option | Purpose |
|---|---|
| `--allow-tool` / `--deny-tool` | Permit or block specific tools |
| `--allow-url` / `--deny-url` | Control web access by URL |
| `--available-tools` | Limit tools visible to the model |
| `--excluded-tools` | Exclude specific tools entirely |

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

Copilot CLI automatically reads Markdown instruction files placed in your repository: ([Docs][2])

| File / Path | Scope |
|---|---|
| `.github/copilot-instructions.md` | Repository-wide |
| `.github/instructions/**/*.instructions.md` | Path-specific |
| `AGENTS.md` | Agent-specific |

#### Custom Agents

Define agent profiles (Markdown) specifying **prompts, tools, and MCP servers** to create specialized agents. ([Docs][2])
Built-in agents (Explore, Task, Plan, etc.) are also bundled. ([Docs][2])

#### MCP (Model Context Protocol) Integration

Copilot CLI supports MCP server integration for extending tools and context. ([Features][6])

- Default config location: `~/.copilot/mcp-config.json` (configurable via `XDG_CONFIG_HOME`). ([Docs][2])
- Use `--disable-builtin-mcps` to control built-in MCP servers (e.g., `github-mcp-server`). ([Docs][7])

---

### 🧠 Model Selection

- Default model: **Claude Sonnet 4.5** (changeable via `/model` or `--model`). ([Docs][3])
- **GPT-5 mini** and **GPT-4.1** were added (2026-01-14) and are **included in Copilot subscriptions** without consuming premium requests. ([Blog][9])
- Copilot CLI usage itself **consumes premium request quota**. ([Features][6])
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
3. **Use custom instructions sparingly** — Place design principles, naming conventions, test policies, and prohibitions in `.github/copilot-instructions.md`. ([Docs][2])
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

---

## Licence

Released under the [MIT license](https://gist.githubusercontent.com/shinyay/56e54ee4c0e22db8211e05e70a63247e/raw/f3ac65a05ed8c8ea70b653875ccac0c6dbc10ba1/LICENSE)

## Author

- github: <https://github.com/shinyay>
- twitter: <https://twitter.com/yanashin18618>
- mastodon: <https://mastodon.social/@yanashin>

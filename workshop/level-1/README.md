# Level 1: Observe — Read-Only Exploration (No Risk)

> **Risk level:** 🟢 Zero — Nothing in this level modifies any files.

## Learning Objectives

By the end of this level, you will be able to:

1. Launch Copilot CLI and navigate the interactive UI confidently
2. Understand the trust model and authentication flow
3. Use `@` to add file context to conversations
4. Use `!` to run shell commands without invoking the AI model
5. Read and interpret tool approval prompts (without approving writes)
6. Use `/help`, `/model`, `/usage`, and `/context` to understand your environment
7. Navigate conversation history and use keyboard shortcuts
8. Ask effective read-only questions across multiple files
9. Understand token consumption and context window management
10. Recognize the difference between "questions" and "tasks" in prompts
11. Manage sessions: exit, continue, and resume
12. Stay in read-only mode by phrasing prompts as questions

---

## Prerequisites

- [ ] Copilot CLI is installed (`copilot --version` works)
- [ ] You have a valid GitHub Copilot subscription
- [ ] You are logged in (`copilot` → `/login` if prompted)
- [ ] You have cloned this repository locally

---

## Workshop Structure

This level contains **12 exercises**, each building on the previous one. Estimated time: **45–60 minutes**.

| Exercise | Topic | Time |
|----------|-------|------|
| 1 | Launch & First Impressions | 5 min |
| 2 | The Help System | 3 min |
| 3 | Shell Escape (`!`) | 5 min |
| 4 | Your First Conversation | 5 min |
| 5 | File Context (`@`) | 7 min |
| 6 | Deep File Exploration | 7 min |
| 7 | Observing Tool Calls | 5 min |
| 8 | Model & Usage Awareness | 5 min |
| 9 | Multi-Turn Conversations | 5 min |
| 10 | Context Window Management | 5 min |
| 11 | Session Basics | 5 min |
| 12 | Questions vs Tasks — Know the Boundary | 5 min |

---

## Exercise 1: Launch & First Impressions

### Goal
Understand what happens when you start Copilot CLI and what each UI element means.

### Steps

**1.1** Navigate to the sample app directory and launch Copilot:

```bash
cd workshop/level-1/sample-app
copilot
```

**1.2** When prompted to **trust the folder**, choose **"Allow for this session only"**.

> 💡 **Why this matters:** Copilot CLI can read, modify, and execute files in the trusted directory. "Session only" means you'll be asked again next time — safer for learning.

**1.3** Observe the UI elements:

```
┌─────────────────────────────────────────────────┐
│  Banner / Logo          (first launch only)     │
│  Model indicator        (e.g., Claude Sonnet)   │
│  Session info           (session ID)            │
│  Input prompt      >>>  (where you type)        │
└─────────────────────────────────────────────────┘
```

**1.4** Note the **model name** displayed. This is the AI model that will process your prompts.

### What You Learned
- Copilot CLI runs inside your terminal, not a browser
- The trust prompt is a **security gate** — Copilot won't touch files until you consent
- "Session only" trust is reversible — it resets when you exit

### ✅ Checkpoint
You see the `>>>` input prompt and know which model is active.

---

## Exercise 2: The Help System

### Goal
Discover all available commands and shortcuts before using any of them.

### Steps

**2.1** Type `/help` and press Enter:

```
/help
```

**2.2** Read through the output. It's organized into sections:

| Section | What It Contains |
|---------|-----------------|
| **Global shortcuts** | `@`, `!`, `Ctrl+C`, `Ctrl+L`, `Esc` |
| **Timeline shortcuts** | `Ctrl+O`, `Ctrl+E`, `Ctrl+T` |
| **Motion shortcuts** | `Ctrl+A/E`, `Ctrl+W/U/K`, arrow keys |
| **Available commands** | All `/slash` commands |
| **Instruction files** | Where Copilot reads custom instructions from |

**2.3** Count how many `/slash` commands are available. Note at least 5 that seem interesting to you.

**2.4** Look at the **"Copilot respects instructions from these locations"** section at the bottom. These are the files Copilot auto-loads:

```
CLAUDE.md
GEMINI.md
AGENTS.md
.github/instructions/**/*.instructions.md
.github/copilot-instructions.md
$HOME/.copilot/copilot-instructions.md
```

> 💡 **Why this matters:** Understanding `/help` output is like reading a map before exploring. You now know what's possible.

### ✅ Checkpoint
You can name at least 5 slash commands and know where to find the full list.

---

## Exercise 3: Shell Escape (`!`)

### Goal
Learn to run shell commands directly — without consuming AI tokens or waiting for model responses.

### Steps

**3.1** Run these commands one at a time using `!`:

```bash
!pwd
```

```bash
!ls -la
```

```bash
!wc -l *.py
```

```bash
!head -20 main.py
```

```bash
!git log --oneline -5
```

**3.2** Now try running a command **without** the `!` prefix:

```
List all Python files in this directory
```

> 💡 **Notice the difference:**
> - `!ls *.py` → instant, no AI, no token cost
> - "List all Python files" → AI processes your request, may call tools, costs tokens

**3.3** Try `!cat config.py` to read a file directly:

```bash
!cat config.py
```

**3.4** Try command chaining:

```bash
!echo "Files:" && ls *.py && echo "---" && wc -l *.py
```

### Key Concept: When to Use `!`

| Use `!` When... | Use Natural Language When... |
|---|---|
| You know the exact command | You want AI to figure out the command |
| You want instant results | You want AI to interpret the output |
| You want zero token cost | You need synthesis across multiple files |
| You're doing routine checks | You're exploring or need explanation |

### ✅ Checkpoint
You can run any shell command instantly with `!` and understand the cost tradeoff vs natural language.

---

## Exercise 4: Your First Conversation

### Goal
Ask read-only questions and observe how Copilot responds — including what tools it uses.

### Steps

**4.1** Start with the simplest possible question:

```
What is this project?
```

> Observe: Copilot will likely read files (`ls`, `cat README.md`, etc.) to answer. Watch for **tool call approval prompts**. Approve read-only operations.

**4.2** Ask a structure question:

```
What files are in this project and what does each one do?
```

> Observe: Copilot should list all 6 Python files and explain their purposes. Compare its answer to the `README.md`.

**4.3** Ask a design question:

```
What design patterns are used in this codebase?
```

> Observe: Copilot should identify patterns like dataclass models, the manager pattern, strategy pattern (formatters), etc.

**4.4** Ask about relationships:

```
How do the files depend on each other? Which file imports which?
```

> Observe: Copilot maps the import graph. This is something that would take you several minutes to do manually.

### Key Concept: Questions vs Tasks

| Prompt Type | What Happens | Example |
|---|---|---|
| **Question** | Copilot reads and explains | "What does this function do?" |
| **Task** | Copilot plans changes and wants to execute | "Add error handling to this function" |

In Level 1, we **only ask questions**. Tasks come in Level 4.

### ✅ Checkpoint
You've had a multi-exchange conversation and can distinguish questions from tasks.

---

## Exercise 5: File Context (`@`)

### Goal
Learn to explicitly attach files to the conversation, giving Copilot precise context.

### Steps

**5.1** Reference a single file and ask about it:

```
@ config.py

What configuration options are available and what are their defaults?
```

> 💡 **`@` vs asking:** When you use `@`, the file content is **directly injected** into the context. Without `@`, Copilot has to use tools to read the file first (slower, uses more tokens).

**5.2** Reference a file and ask a targeted question:

```
@ models.py

What validation does the Task class perform on initialization?
```

**5.3** Reference multiple files in one prompt:

```
@ task_manager.py
@ models.py

How does TaskManager use the Task model? Trace the flow of adding a new task.
```

**5.4** Reference a file and ask a comparison:

```
@ formatter.py

What output formats are supported? Which one is the most complex?
```

**5.5** Try referencing a file that might not be obvious:

```
@ requirements.txt

Does this project have any external dependencies?
```

### Key Concept: When `@` Is Better Than Asking

| Scenario | Approach |
|---|---|
| You know which file matters | `@ filename` + question |
| You don't know which file to look at | Ask naturally, let Copilot find it |
| You want to compare specific files | `@ file1` `@ file2` + question |
| You want codebase-wide analysis | Ask naturally (e.g., "find all TODOs") |

### ✅ Checkpoint
You can inject specific files into context with `@` and understand when it's more efficient than natural-language questions.

---

## Exercise 6: Deep File Exploration

### Goal
Use Copilot to deeply understand a single file — extracting knowledge that would take minutes to gather manually.

### Steps

**6.1** Pick the most complex file and start a deep dive:

```
@ task_manager.py

Give me a complete analysis of this file:
1. What is its responsibility?
2. What methods does it expose?
3. What error conditions does it handle?
4. What could go wrong at runtime?
```

**6.2** Ask about edge cases:

```
What happens if the tasks.json file is corrupted or contains invalid data?
```

**6.3** Ask about the data flow:

```
@ main.py
@ task_manager.py
@ models.py

Trace the complete data flow when a user runs: python main.py add "Buy groceries" --priority high --due 2026-02-14
```

**6.4** Ask about hidden behaviors:

```
@ models.py

What does the @property decorator do on is_overdue and priority_rank? Why are they properties instead of methods?
```

**6.5** Ask Copilot to explain code to a beginner:

```
@ formatter.py

Explain the format_table function line by line. Assume I'm new to Python.
```

**6.6** Ask for a summary of the entire architecture:

```
Summarize the architecture of this application in a diagram-like format. Show the layers and data flow.
```

### Key Concept: Depth of Questions

| Shallow (less useful) | Deep (more useful) |
|---|---|
| "What does main.py do?" | "Trace the execution path when I run `python main.py list --status pending --format csv`" |
| "What's in models.py?" | "What validation gaps exist in the Task model? What inputs would bypass validation?" |
| "Explain config.py" | "If I wanted to add a new priority level, which files would I need to change and why?" |

> 💡 **The deeper your question, the more useful Copilot's answer.** Shallow questions get shallow answers.

### ✅ Checkpoint
You can trace data flows, explore edge cases, and extract deep understanding from any file.

---

## Exercise 7: Observing Tool Calls

### Goal
Understand what tool calls look like, what they mean, and how the approval system works — without approving any writes.

### Steps

**7.1** Ask a question that requires Copilot to use tools:

```
How many lines of Python code are in this project? Count them.
```

> Observe the **tool call approval prompt**. It will look something like:
> ```
> 🔧 Tool: bash
>    Command: wc -l *.py
>    [Allow] [Deny] [Allow for session]
> ```

**7.2** **Approve** this tool call (it's read-only — just `wc -l`).

**7.3** Now ask something that might trigger a write:

```
What would the code look like if I added a "search" command?
```

> 💡 **Important:** If Copilot tries to **create or modify a file**, you'll see a tool call for something like `create` or `edit`. In Level 1, you should **deny** write operations. Just observe what it proposes.

**7.4** Practice reading tool calls without approving:

```
Find all places where error handling could be improved
```

> Watch what tools Copilot wants to use (likely `grep`, `cat`, etc.). Approve reads, deny writes.

**7.5** Understand the three approval options:

| Option | What It Does |
|---|---|
| **Allow** | Approve this one tool call only |
| **Deny** | Block this tool call; Copilot will try to work around it |
| **Allow for session** | Auto-approve this tool for the rest of the session |

> 💡 **"Allow for session"** is convenient but be careful — in Level 1, only use it for read tools like `cat`, `ls`, `grep`, `find`.

### ✅ Checkpoint
You can read tool call prompts, distinguish read vs write operations, and approve/deny appropriately.

---

## Exercise 8: Model & Usage Awareness

### Goal
Understand which AI model you're using, what alternatives exist, and how to monitor resource consumption.

### Steps

**8.1** Check the current model:

```
/model
```

> You'll see a list of available models with the current one highlighted. Note the default (likely Claude Sonnet 4.5).

**8.2** Check your session usage:

```
/usage
```

> This shows:
> - Premium requests consumed in this session
> - Token usage (input/output)
> - Model information

**8.3** Ask a question, then check `/usage` again:

```
Explain the purpose of each method in task_manager.py
```

Then:

```
/usage
```

> 💡 Compare the before/after. Each prompt costs at least 1 premium request. Token usage depends on how much context (files, conversation history) is involved.

**8.4** Check the context window:

```
/context
```

> This visualizes how much of the model's context window is used. You'll see a bar or percentage showing consumption.

**8.5** Understand the cost model:

| Action | Token Cost |
|---|---|
| `!command` | **Zero** — bypasses the model |
| `@ filename` | Adds file tokens to context (input tokens) |
| Asking a question | Input tokens (your prompt + context) + output tokens (response) |
| `/help`, `/model`, `/usage` | **Zero** — local commands |

> 💡 **Key insight:** `!` and `/slash` commands are free. Every natural-language prompt costs tokens.

### ✅ Checkpoint
You know your current model, can check usage stats, and understand what costs tokens vs what's free.

---

## Exercise 9: Multi-Turn Conversations

### Goal
Understand how conversation history works — how context accumulates and how follow-up questions leverage previous answers.

### Steps

**9.1** Start a focused conversation thread (3+ turns on the same topic):

```
@ models.py

What fields does the Task class have?
```

Wait for the response, then follow up:

```
Which of those fields are optional?
```

Then:

```
What happens if I create a Task without providing a due_date?
```

> 💡 **Notice:** You didn't re-reference `models.py` in the follow-ups. Copilot **remembers the conversation context** — it knows you're still talking about the Task class.

**9.2** Test context continuity by asking a reference-back question:

```
Going back to the fields you listed — which ones have default values?
```

**9.3** Now deliberately change topic to see how Copilot handles it:

```
@ config.py

What ANSI color codes are defined in this file?
```

> Notice that Copilot switches topic cleanly. Both the models.py conversation and this new config.py conversation are in the history.

**9.4** Test if Copilot remembers the earlier topic:

```
Going back to the Task class from earlier — does it use any of those color codes?
```

> 💡 Copilot should connect both topics — Task class (from turns 1–4) and color codes (from turn 5) — because the full history is in the context window.

**9.5** Check what this accumulated history costs:

```
/context
```

> After 6+ turns, the context window should be noticeably more full than after Exercise 8.

### Key Concept: Conversation Memory

| Behavior | Implication |
|---|---|
| Copilot remembers all turns | Follow-ups don't need to repeat context |
| Context window has a limit | Long conversations eventually need compression |
| Each turn adds tokens | More turns = more context consumption |
| `/compact` resets by summarizing | Useful when switching to a new task |

### ✅ Checkpoint
You can hold multi-turn conversations, test context continuity, and see how history accumulates.

---

## Exercise 10: Context Window Management

### Goal
Learn to manage the context window proactively — the skill that separates casual users from effective users.

### Steps

**10.1** Check your current context consumption:

```
/context
```

> Note the percentage or token count. After Exercises 1–9, it should be significant.

**10.2** Compress the conversation:

```
/compact
```

> Copilot summarizes the entire conversation history into a much shorter form. This frees up context space.

**10.3** Check context again:

```
/context
```

> Compare with 10.1. The usage should have dropped significantly.

**10.4** Verify that Copilot still has useful context after compaction:

```
What do you know about this project so far?
```

> 💡 After `/compact`, Copilot retains the **summary** of what you discussed, not the full details. It knows the project is a task tracker with 6 files, but might not remember exact line-by-line analysis.

**10.5** Understand when to use `/compact`:

| Use `/compact` When... | Don't Use `/compact` When... |
|---|---|
| You're switching to a completely different task | You're in the middle of a deep dive |
| Context window is >70% full | You need Copilot to remember exact details |
| The conversation has gone off-topic | You're about to reference earlier analysis |
| You see degraded response quality | The conversation is short (<5 turns) |

**10.6** Understand automatic compression:

> When context usage reaches **~95%**, Copilot **automatically compresses** the history. You'll see a message about it. Using `/compact` proactively at 70% gives you better control over what gets summarized.

**10.7** Finally, clean up and exit:

```
/exit
```

### ✅ Checkpoint
You can monitor, compress, and manage the context window proactively.

---

## Exercise 11: Session Basics

### Goal
Understand how sessions work — exiting, continuing, and starting fresh.

### Steps

**11.1** Check your current session info:

```
/context
```

> Observe: this shows your loaded files, token usage, and session details.

**11.2** Exit Copilot cleanly:

Press `Ctrl+C` or type:

```
/exit
```

**11.3** Resume where you left off:

```bash
copilot --continue
```

**11.4** Verify the session restored:

```
What files were we looking at? Do you remember our previous conversation?
```

> Copilot should recall your previous context.

**11.5** Exit again and start fresh:

```bash
copilot
```

```
Do you know what we were discussing before?
```

> A new session has no memory of previous sessions.

**11.6** Try resuming from a list:

```bash
copilot --resume
```

> This shows recent sessions — you can pick which one to return to.

### Key Concept: Session Lifecycle

| Command | Result |
|---------|--------|
| `copilot` | New session (blank slate) |
| `copilot --continue` | Resume the last session |
| `copilot --resume` | Choose from recent sessions |
| `/exit` or `Ctrl+C` | Save and exit |

### ✅ Checkpoint
You understand session basics: starting fresh, continuing, and resuming.

---

## Exercise 12: Questions vs Tasks — Know the Boundary

### Goal
Learn to distinguish between **questions** (safe, read-only) and **tasks** (modify files) — the essential skill that prepares you for Level 2 and beyond.

### Steps

**12.1** Ask a pure question (safe — Level 1 skill):

```
What does the add_task function in task_manager.py do?
```

> This only reads code and explains. No tools are invoked beyond `view`.

**12.2** Ask a question that sounds like a task:

```
How would I add a "priority" field to the Task class?
```

> Copilot should **explain** how — it doesn't actually modify files. This is still a question.

**12.3** Now ask an actual task (observe, don't approve):

```
Add a "priority" field to the Task class in models.py
```

> ⚠️ This will trigger a **write tool approval** (`edit`). Choose **Deny**.

**12.4** Notice the difference:

| Prompt | Type | Tool Used |
|--------|------|-----------|
| "What does X do?" | Question | `view` (read-only) |
| "How would I add X?" | Question | None or `view` |
| "Add X to file Y" | Task | `edit` (write!) |
| "Explain the bug in X" | Question | `view` |
| "Fix the bug in X" | Task | `edit` (write!) |

**12.5** Practice rewriting tasks as questions:

| Task (Level 4+) | Question (Level 1) |
|------------------|-------------------|
| "Fix the validation bug" | "What's wrong with the validation logic?" |
| "Add error handling" | "Where is error handling missing?" |
| "Refactor this function" | "How would you suggest refactoring this?" |

**12.6** Internalize the rule:

```
In Levels 1–3, always phrase prompts as QUESTIONS.
If Copilot shows a write tool approval, choose Deny.
You'll learn to approve writes starting in Level 4.
```

### Key Concept: The Question/Task Spectrum

```
Questions (Level 1)              Tasks (Level 4+)
  │                                │
  "What does..."                   "Create..."
  "How does..."                    "Fix..."
  "Explain..."                     "Add..."
  "Where is..."                    "Refactor..."
  "Why does..."                    "Delete..."
  "Show me..."                     "Update..."
```

### ✅ Checkpoint
You can reliably distinguish questions from tasks and stay in read-only mode.

---

## 🏆 Level 1 Self-Assessment

Rate yourself on each skill (1 = shaky, 3 = confident):

| # | Skill | 1 | 2 | 3 |
|---|---|---|---|---|
| 1 | Launch Copilot CLI and pass the trust prompt | ☐ | ☐ | ☐ |
| 2 | Use `/help` to find commands and shortcuts | ☐ | ☐ | ☐ |
| 3 | Run shell commands instantly with `!` | ☐ | ☐ | ☐ |
| 4 | Ask effective read-only questions | ☐ | ☐ | ☐ |
| 5 | Add file context with `@ filename` | ☐ | ☐ | ☐ |
| 6 | Deep-dive into files (data flow, edge cases) | ☐ | ☐ | ☐ |
| 7 | Read and respond to tool approval prompts | ☐ | ☐ | ☐ |
| 8 | Check model, usage, and context (`/model`, `/usage`, `/context`) | ☐ | ☐ | ☐ |
| 9 | Hold multi-turn conversations with follow-ups | ☐ | ☐ | ☐ |
| 10 | Manage the context window with `/compact` | ☐ | ☐ | ☐ |
| 11 | Manage sessions: exit, continue, and resume | ☐ | ☐ | ☐ |
| 12 | Distinguish questions from tasks and stay read-only | ☐ | ☐ | ☐ |

**Scoring:**
- **30–36:** Ready for Level 2
- **22–29:** Review exercises 5–12 once more
- **Below 22:** Repeat the level — practice builds fluency

---

## Key Takeaways

1. **`!` is your best friend** — instant, free, no AI overhead
2. **`@` is your precision tool** — injects exactly the file you want into context
3. **Questions ≠ Tasks** — in Level 1, only ask questions (Level 4 covers tasks)
4. **Approve reads, deny writes** — until you're ready for Level 4
5. **Monitor context** — `/usage` and `/context` keep you aware of consumption
6. **`/compact` proactively** — don't wait for auto-compression at 95%
7. **Deep questions get deep answers** — "trace the execution path" beats "explain this file"
8. **Sessions persist** — `--continue` resumes, `--resume` lets you pick, bare `copilot` starts fresh

---

## What's Next

**Level 2: Understand — Ask Questions & Get Explanations** takes everything you learned here and levels up to cross-file analysis, dependency mapping, and code understanding patterns.

→ Continue to `workshop/level-2/README.md`

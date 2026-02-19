# Level 7: Customize — Make Copilot Work Your Way

> **Risk level:** 🟢 Low — You are configuring Copilot's behavior, not modifying production code. All configurations are additive and reversible.

## Learning Objectives

By the end of this level, you will be able to:

1. Write effective **custom instructions** (`.github/copilot-instructions.md`)
2. Test and refine instructions through iterative feedback
3. Optimize **context loading** with `@` references for precision
4. Create a **`.copilotignore`** to exclude irrelevant files
5. Build **reusable prompt templates** for your team
6. Understand what **MCP (Model Context Protocol)** servers are
7. Configure MCP servers in Copilot CLI
8. Manage **sessions** effectively (`--continue`, `--resume`)
9. Set up **terminal integration** for optimal Copilot experience
10. Work with **multi-project repositories** and context boundaries
11. Layer instructions at **organization**, **repository**, and **personal** levels
12. Audit and measure your Copilot configuration effectiveness

---

## Prerequisites

- [ ] Completed **Levels 1–6** (all workflow skills)
- [ ] Familiarity with the Event API sample app structure
- [ ] A GitHub account with Copilot access

---

## About the Sample App

Level 7 uses an **Event API** — a TypeScript Express application with specific conventions that benefit from custom Copilot instructions.

> Unlike Levels 1–6 which all used Python, this level switches to **TypeScript** to demonstrate that Copilot CLI customization (instructions, context, MCP) works across any language. The app has strong conventions (AppError, ApiResponse, logger) that Copilot should learn to follow through your custom instructions.

```
sample-app/
├── src/
│   ├── routes/events.ts        ← HTTP layer (routes only)
│   ├── middleware/              ← Error handler, validation (Zod)
│   ├── services/eventService.ts ← Business logic (AppError, logger)
│   ├── models/event.ts         ← Interfaces and types
│   └── utils/                  ← errors.ts, logger.ts, response.ts
├── tests/
│   └── eventService.test.ts    ← Jest tests (describe/it style)
├── generated/                  ← Large auto-generated files (exclude!)
│   ├── openapi.json            ← OpenAPI spec (~2KB)
│   └── schema.sql              ← Database schema
├── docs/
│   ├── architecture.md         ← Architecture overview
│   ├── starter-instructions.md ← Basic instructions (Exercise 1 start)
│   └── comprehensive-instructions.md ← Full instructions (answer key)
├── package.json
└── tsconfig.json
```

### Key Conventions (the ones you'll teach Copilot)

| Convention | Example |
|-----------|---------|
| Error handling | `AppError.badRequest("msg", "CODE")` — never plain `Error` |
| Responses | `respondSuccess(data)` — never raw JSON |
| Logging | `logger.info("msg", { context })` — never `console.log` |
| Validation | Zod schemas via `validateBody(schema)` middleware |
| Testing | `describe`/`it` blocks — never `test()` |
| Imports | Named imports — never `import *` |
| Naming | camelCase functions, PascalCase types |

---

## Workshop Structure

This level contains **12 exercises**. Estimated time: **75–100 minutes**.

| Exercise | Topic | Time |
|----------|-------|------|
| 1 | Writing Custom Instructions | 10 min |
| 2 | Testing & Refining Instructions | 8 min |
| 3 | Context Optimization with `@` | 7 min |
| 4 | Creating `.copilotignore` | 5 min |
| 5 | Building Prompt Templates | 7 min |
| 6 | Understanding MCP Servers | 7 min |
| 7 | Configuring MCP Servers | 8 min |
| 8 | Session Management | 7 min |
| 9 | Terminal Setup & Shell Integration | 5 min |
| 10 | Multi-Project Context | 7 min |
| 11 | Instruction Layering | 8 min |
| 12 | Configuration Audit | 7 min |

---

## Exercise 1: Writing Custom Instructions

### Goal
Create `.github/copilot-instructions.md` — the file that teaches Copilot your project's conventions.

### Steps

**1.1** Explore the codebase conventions:

```bash
cd workshop/level-7/sample-app
copilot
```

```
@ src/utils/errors.ts
@ src/utils/logger.ts
@ src/utils/response.ts

What conventions does this project follow for error handling, logging, and API responses?
```

**1.2** Read the starter instructions:

```
@ docs/starter-instructions.md

These are basic custom instructions. What's missing? 
Compare them to what you see in the actual code.
```

**1.3** Create the custom instructions file:

```
Based on the conventions you see in the codebase, create a 
.github/copilot-instructions.md file with comprehensive instructions.

Include sections for:
- Language & runtime
- Code style (naming, imports, const vs let)
- Error handling (AppError, factory methods, error codes)
- API responses (ApiResponse<T>, respondSuccess, respondPaginated)
- Logging (logger, never console.log, structured context)
- Validation (Zod, validateBody middleware)
- Testing (Jest, describe/it, beforeEach)
- Architecture (routes vs services vs models)
- Files to ignore (generated/, dist/)
```

**1.4** Compare with the comprehensive reference:

```
@ docs/comprehensive-instructions.md

Compare the instructions you generated with this reference.
What did you miss? What did you add that the reference doesn't have?
```

**1.5** Refine your instructions:

```
Update .github/copilot-instructions.md to incorporate anything 
important from the reference that we missed.
```

### Key Concept: Custom Instructions

| Aspect | Good Instruction | Bad Instruction |
|--------|-----------------|-----------------|
| Specificity | "Use `AppError.badRequest()` for 400 errors" | "Handle errors properly" |
| Examples | "Import as: `import { logger } from '../utils/logger'`" | "Use the logger" |
| Negative rules | "Never use `console.log`" | (omitting what NOT to do) |
| Context | "In route handlers, use `respondSuccess(data)`" | "Return JSON" |

### ✅ Checkpoint
You have a `.github/copilot-instructions.md` that encodes your project's conventions.

---

## Exercise 2: Testing & Refining Instructions

### Goal
Verify that Copilot actually follows your instructions, and refine them when it doesn't.

### Steps

**2.1** Test: ask Copilot to generate a new service function:

```
Add a "cancelEvent" function to eventService.ts that:
- Takes eventId and requesterId
- Checks only organizer can cancel
- Sets status to "cancelled"
- Returns the updated event
```

**2.2** Evaluate the generated code against your instructions:

| Check | Expected | Pass? |
|-------|----------|-------|
| Uses `AppError.unauthorized()` | ✓ | |
| Uses `logger.info()` not `console.log` | ✓ | |
| Returns `Event` type | ✓ | |
| Follows naming conventions | ✓ | |
| No `import *` | ✓ | |

**2.3** If any checks fail, strengthen the instructions:

```
My instructions say to use AppError but Copilot used plain Error.
How should I rephrase the instruction to be clearer?
```

**2.4** Test again with a different generation:

```
Create a new route handler in routes/events.ts for the cancelEvent endpoint.
POST /api/events/:id/cancel
```

**2.5** Evaluate again:

| Check | Expected | Pass? |
|-------|----------|-------|
| Uses `respondSuccess()` wrapper | ✓ | |
| Error handling via `next(err)` | ✓ | |
| Reads `x-user-id` from headers | ✓ | |
| No business logic in route | ✓ | |

**2.6** Test with test generation:

```
Write tests for the cancelEvent function in eventService.test.ts.
```

| Check | Expected | Pass? |
|-------|----------|-------|
| Uses `describe`/`it` (not `test()`) | ✓ | |
| Uses `beforeEach` with `_clearAll()` | ✓ | |
| Tests both success and error paths | ✓ | |
| Uses `toThrow(AppError)` | ✓ | |

### Key Concept: Instruction Testing Loop

```
Write instructions → Generate code → Evaluate → Refine → Repeat
```

> 💡 **Instructions are never "done."** Every time Copilot generates code that doesn't follow a convention, add or clarify the instruction. This is an iterative process.

### ✅ Checkpoint
You've tested instructions across service, route, and test generation and refined gaps.

---

## Exercise 3: Context Optimization with `@`

### Goal
Learn to load exactly the right context for each task — not too much, not too little.

### Steps

**3.1** Too little context — ask without references:

```
Add a getEventsByOrganizer function
```

> Observe: Copilot might not use AppError, logger, or follow conventions because it doesn't have the context files loaded.

**3.2** Too much context — load everything:

```
@ src/routes/events.ts
@ src/middleware/errorHandler.ts
@ src/middleware/validation.ts
@ src/services/eventService.ts
@ src/models/event.ts
@ src/utils/errors.ts
@ src/utils/logger.ts
@ src/utils/response.ts

Add a getEventsByOrganizer function
```

> This works but wastes context tokens loading files that aren't relevant.

**3.3** Just right — targeted context:

```
@ src/services/eventService.ts
@ src/models/event.ts

Add a getEventsByOrganizer function to eventService.ts
```

> This gives Copilot the service patterns and the model types — exactly what it needs.

**3.4** Practice context targeting for different tasks:

| Task | Best Context Files |
|------|--------------------|
| New service function | `eventService.ts` + `event.ts` |
| New route handler | `routes/events.ts` + `eventService.ts` |
| New middleware | `errorHandler.ts` or `validation.ts` |
| New test | `eventService.test.ts` + the file being tested |
| Fix a bug | The buggy file + its test file |

**3.5** Test the "context map" approach:

```
I'm about to write a new middleware for rate limiting.
Which files should I load as context? Just list them.
```

> Copilot should suggest the right files based on the task.

### Key Concept: Context Budget

| Strategy | Context Usage | Quality |
|----------|--------------|---------|
| No `@` | Minimal | Low — misses conventions |
| `@` everything | Maximum | Good but wasteful |
| `@` targeted files | Optimal | Best — precise conventions, room for discussion |

> 💡 **The context window is finite.** Every file loaded reduces space for conversation. Load what matters, skip what doesn't.

### ✅ Checkpoint
You can target exactly the right context files for any given task.

---

## Exercise 4: Creating `.copilotignore`

### Goal
Exclude irrelevant files so Copilot never wastes context on auto-generated or third-party code.

### Steps

**4.1** Identify files that should be excluded:

```
List all files in the project. Which ones are auto-generated, 
compiled, or third-party? These should never be loaded as context.
```

**4.2** Create `.copilotignore`:

```
Create a .copilotignore file in the project root that excludes:
- generated/ (auto-generated files)
- dist/ (compiled output)
- node_modules/ (third-party)
- package-lock.json (large, auto-generated)
- *.map files (source maps)
- coverage/ (test coverage reports)
```

**4.3** Verify it works — try to reference an excluded file:

```
@ generated/openapi.json
What does this file contain?
```

> With `.copilotignore` active, Copilot should either skip or note that this file is excluded.

**4.4** Test that important files are NOT excluded:

```
@ src/services/eventService.ts
Show me the createEvent function.
```

> This should work normally.

**4.5** Consider what else to exclude:

```
Are there any other files that might pollute context? 
Think about: lock files, IDE settings, CI configs, 
large data files, binary files.
```

### Key Concept: `.copilotignore` Syntax

```gitignore
# Auto-generated — never manually edit
generated/
dist/

# Third-party
node_modules/

# Build artifacts
*.map
*.d.ts
coverage/

# Large files with no useful code context
package-lock.json
*.sql
```

> The syntax is identical to `.gitignore`. Copilot CLI reads this file and excludes matching files from automatic context loading.

### ✅ Checkpoint
You have a `.copilotignore` that keeps context clean and focused.

---

## Exercise 5: Building Prompt Templates

### Goal
Create reusable prompt patterns that your team can use for consistent, high-quality interactions.

### Steps

**5.1** Create a prompt template for new service functions:

```
Here's a template I want to use every time I add a new service function:

"Add a [FUNCTION_NAME] function to [SERVICE_FILE].
Requirements: [LIST]
Context files: @ [SERVICE_FILE] @ [MODEL_FILE]
Follow error handling, logging, and naming conventions from instructions."

Can you refine this template to be more effective?
```

**5.2** Create a template for new API endpoints:

```
Create a prompt template for adding a new REST endpoint:
- Route definition in routes/
- Request validation with Zod
- Service call
- Response formatting
Include which files to @ reference.
```

**5.3** Create a template for bug fixes:

```
Create a prompt template for fixing a bug:
- Reproduce the issue
- Investigate root cause
- Plan the fix
- Implement
- Write regression test
- Verify
```

**5.4** Create a template for code review:

```
Create a prompt template for reviewing changes:
- Check conventions compliance
- Security review
- Test coverage
- Performance
```

**5.5** Save your templates:

```
Create a file docs/prompt-templates.md that contains all 4 templates 
formatted as reusable checklists.
```

### Key Concept: Prompt Templates

| Template | Purpose | Typical `@` References |
|----------|---------|----------------------|
| New service function | Add business logic | Service file + model file |
| New endpoint | Add HTTP route | Routes file + service file |
| Bug fix | Investigate and fix | Bug file + test file |
| Code review | Review changes | Changed files |
| New test | Add test coverage | Test file + source file |

> 💡 **Templates encode your team's best practices.** Share them in your repository's docs so everyone starts with the same quality level.

### ✅ Checkpoint
You have reusable prompt templates for common development tasks.

---

## Exercise 6: Understanding MCP Servers

### Goal
Understand what MCP (Model Context Protocol) servers are and how they extend Copilot.

### Steps

**6.1** Ask Copilot to explain MCP:

```
What is the Model Context Protocol (MCP)? 
How does it relate to Copilot CLI? 
What can MCP servers do that Copilot can't do on its own?
```

**6.2** Understand the MCP architecture:

```
Draw the architecture of MCP in text:
- Where does the MCP server run?
- How does Copilot CLI connect to it?
- What types of tools can MCP servers expose?
```

**6.3** Explore common MCP server use cases:

```
What are the most useful MCP servers for a TypeScript API project like ours?
Examples: database access, API documentation, deployment, monitoring.
```

**6.4** Understand the security model:

```
When an MCP server exposes a tool, who approves its execution?
How is it different from the bash tool approval?
```

**6.5** Understand the configuration:

```
Where is MCP server configuration stored?
What's the difference between:
- Project-level MCP config
- User-level MCP config
```

### Key Concept: MCP Overview

```
┌─────────────────────┐     ┌─────────────────────┐
│   Copilot CLI        │────▶│   MCP Server         │
│   (client)           │◀────│   (tool provider)    │
└─────────────────────┘     └─────────────────────┘
        │                           │
        │ Uses built-in tools:      │ Exposes additional tools:
        │ - bash, edit, view        │ - database queries
        │ - grep, create            │ - API calls
        │                           │ - deployment
        │                           │ - custom workflows
```

### ✅ Checkpoint
You understand MCP concepts, architecture, and security model.

---

## Exercise 7: Configuring MCP Servers

### Goal
Configure an MCP server for Copilot CLI to extend its capabilities.

### Steps

**7.1** Check what MCP configuration exists:

```
Is there any existing MCP configuration in this project?
Check .github/copilot/ and any mcp-related config files.
```

**7.2** Explore Copilot CLI's MCP support:

```
What command do I use to see available MCP servers?
How do I configure a new one?
```

**7.3** Create an MCP configuration file:

```
Create a .github/copilot/mcp.json configuration file.
Start with the GitHub MCP server that provides issue and PR tools.
```

> 💡 The configuration file tells Copilot CLI which MCP servers to connect to and how.

**7.4** Understand the configuration format:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "path/to/server",
      "args": ["--flag"],
      "env": {
        "API_KEY": "..."
      }
    }
  }
}
```

**7.5** Consider project-specific MCP servers:

```
For this Event API project, what MCP servers would be most valuable?
Think about:
- Database access (query the schema)
- OpenAPI spec (generate client code)
- Deployment (check environments)
```

**7.6** Security best practices:

```
What are the security best practices for MCP server configuration?
- Where should API keys go?
- Should MCP config be committed to git?
- How to scope MCP server permissions?
```

### Key Concept: MCP Configuration Levels

| Level | File Location | Scope |
|-------|--------------|-------|
| Project | `.github/copilot/mcp.json` | All contributors to this repo |
| User | `~/.config/github-copilot/mcp.json` | All your repos |

### ✅ Checkpoint
You can configure MCP servers and understand security best practices.

---

## Exercise 8: Session Management

### Goal
Master Copilot CLI session management — resume, continue, and manage conversation history.

### Steps

**8.1** Check current session:

```
/context
```

> This shows what's currently loaded in the session.

**8.2** Exit and continue:

```
exit
```

Then restart with:

```bash
copilot --continue
```

> Your conversation history and context are preserved.

**8.3** Start a fresh session:

```bash
copilot
```

> This creates a new session with no history.

**8.4** Resume a specific previous session:

```bash
copilot --resume
```

> This shows a list of recent sessions to choose from.

**8.5** Understand session strategies:

| Strategy | When to Use |
|----------|-------------|
| `--continue` | Picking up where you left off (same task) |
| `--resume` | Returning to an older session |
| New session | Starting a completely different task |
| `/clear` | Reset context within current session |

**8.6** Practice context management within a session:

```
@ src/services/eventService.ts
@ src/models/event.ts

Now I want to work on routes instead.

/clear

@ src/routes/events.ts
@ src/middleware/validation.ts
```

> `/clear` resets the context so you're not carrying service file context into route work.

### Key Concept: Session Lifecycle

```
New session → Load context → Work → Exit
                                      │
                              ┌───────┴───────┐
                              │               │
                        --continue      --resume
                        (same task)    (pick session)
```

### ✅ Checkpoint
You can manage sessions effectively — continue, resume, clear, and start fresh.

---

## Exercise 9: Terminal Setup & Shell Integration

### Goal
Optimize your terminal for the best Copilot CLI experience.

### Steps

**9.1** Run terminal setup:

```
/terminal-setup
```

> This configures your shell for optimal Copilot integration, including multiline input.

**9.2** Test multiline input:

After terminal setup, try typing with Shift+Enter for new lines:

```
Create a function that:
- Takes an event ID
- Checks if it exists
- Returns the attendee count
```

> With terminal setup, each line is entered on a separate line in the prompt.

**9.3** Check shell integration features:

```
What shell integration features are available after /terminal-setup?
- Multiline input?
- Command history?
- Auto-completion?
```

**9.4** Customize your shell prompt (optional):

```
Can I add Copilot session info to my shell prompt?
Show me how to display the current session name.
```

**9.5** Keyboard shortcuts:

| Shortcut | Action |
|----------|--------|
| `Shift+Enter` | New line (after terminal setup) |
| `Ctrl+C` | Cancel current generation |
| `Ctrl+D` | Exit Copilot |
| `↑` / `↓` | Navigate prompt history |

### ✅ Checkpoint
Your terminal is optimized for Copilot CLI with multiline input and shell integration.

---

## Exercise 10: Multi-Project Context

### Goal
Learn strategies for working with Copilot across multiple projects or monorepo modules.

### Steps

**10.1** Understand context boundaries:

```
If I'm in the sample-app/ directory, can Copilot see files 
in the parent directory (workshop/level-7/)?
What about sibling directories?
```

**10.2** Practice cross-directory references:

```
@ ../level-6/sample-app/shortener/store.py

Compare the storage approach in Level 6 (Python, JSON file) 
with our Level 7 approach (TypeScript, in-memory Map).
```

**10.3** Working with monorepo patterns:

```
If this project had a monorepo structure:
  packages/
    api/         ← our event API
    web/         ← React frontend
    shared/      ← shared types

How would I configure Copilot to understand the boundaries?
What should .copilotignore look like?
What should copilot-instructions.md cover?
```

**10.4** Context isolation strategies:

| Strategy | How | When |
|----------|-----|------|
| **cd into module** | `cd packages/api` | Working on one module only |
| **@ specific files** | `@ packages/shared/types.ts` | Pulling in shared types |
| **Instructions per module** | Separate `.github/copilot-instructions.md` | Different conventions per module |
| **`.copilotignore`** | Exclude other modules' src | Keep context focused |

**10.5** Practice optimal context for cross-module work:

```
I need to add a new event type in shared/ and use it in both api/ and web/.
What's the most efficient way to do this in one Copilot session?
```

### ✅ Checkpoint
You understand context boundaries and strategies for multi-project work.

---

## Exercise 11: Instruction Layering

### Goal
Understand how instructions from different levels combine and override each other.

### Steps

**11.1** Understand the instruction hierarchy:

```
What are the different levels of Copilot instructions?
How do they layer together?
Which ones take priority?
```

**11.2** Explore each level:

| Level | Location | Scope | Example |
|-------|----------|-------|---------|
| **Organization** | GitHub org settings | All repos in org | "Always use Python 3.12+" |
| **Repository** | `.github/copilot-instructions.md` | This repo | "Use AppError for errors" |
| **Personal** | `~/.config/github-copilot/instructions.md` | Your sessions only | "Explain changes before making them" |
| **Session** | Conversation context | Current session | "Focus on performance" |

**11.3** Create personal instructions:

```
What would good personal instructions look like?
Things I always want Copilot to do, regardless of project:
- Always explain what you're going to change before changing it
- Prefer small, incremental changes
- Always suggest running tests after modifications
```

**11.4** Test instruction layering:

```
If my repository instructions say "use AppError" but my personal 
instructions say "always add JSDoc comments", will both be followed?
What if they conflict?
```

**11.5** Best practices for instruction layering:

| Level | What to Put Here |
|-------|-----------------|
| **Organization** | Language versions, security policies, universal style |
| **Repository** | Project-specific conventions, architecture rules, framework patterns |
| **Personal** | Communication preferences, verbosity level, workflow habits |
| **Session** | Task-specific constraints ("focus on performance", "no external deps") |

### Key Concept: Instruction Priority

```
Session context (highest priority)
    ↓
Personal instructions
    ↓
Repository instructions
    ↓
Organization instructions (lowest priority)
```

> 💡 More specific instructions override more general ones. Session-level "ignore previous instruction X" can override repository defaults.

### ✅ Checkpoint
You understand instruction layering and can configure at each level appropriately.

---

## Exercise 12: Configuration Audit

### Goal
Audit your complete Copilot CLI configuration and measure its effectiveness.

### Steps

**12.1** Inventory all configuration:

```
List all Copilot-related configuration in this project:
- .github/copilot-instructions.md
- .copilotignore
- MCP configuration
- Any other copilot config files
```

**12.2** Test each configuration component:

| Component | Test | Pass? |
|-----------|------|-------|
| **Instructions** | Generate a service function — follows conventions? | |
| **Instructions** | Generate a test — uses describe/it, not test()? | |
| **Instructions** | Generate error handling — uses AppError? | |
| **`.copilotignore`** | Try `@ generated/openapi.json` — excluded? | |
| **Context targeting** | Service task with only service+model `@` — works? | |

**12.3** Measure before/after quality:

```
Without loading custom instructions, generate a new service function.
Then, with instructions loaded, generate the same function.
Compare the quality of both outputs.
```

**12.4** Identify remaining gaps:

```
Review the .github/copilot-instructions.md. 
Are there any conventions in the codebase that aren't captured?
Scan the codebase for patterns that should be documented.
```

**12.5** Create an optimization checklist for future projects:

```
Based on everything we configured, create a checklist for 
setting up Copilot in a new project:
1. Create .github/copilot-instructions.md with: [...]
2. Create .copilotignore with: [...]
3. Set up MCP servers for: [...]
4. Create prompt templates for: [...]
5. Configure session preferences: [...]
```

**12.6** Share with your team:

```
Write a short guide (5 bullet points) for teammates who haven't 
configured Copilot yet. What's the highest-impact configuration 
they should do first?
```

### Key Concept: Configuration ROI

| Configuration | Setup Time | Impact |
|--------------|-----------|--------|
| **Custom instructions** | 15 min | 🔴 High — every generation follows conventions |
| **`.copilotignore`** | 5 min | 🟡 Medium — cleaner context, fewer distractions |
| **Prompt templates** | 10 min | 🟡 Medium — consistent quality across team |
| **MCP servers** | 20 min | 🟢 Variable — depends on project needs |
| **Terminal setup** | 2 min | 🟢 Low but nice — multiline input |

> 💡 **Custom instructions are the highest-ROI configuration.** 15 minutes of setup saves hours of correcting convention violations.

### ✅ Checkpoint
You've audited your configuration, measured its effectiveness, and created a reusable setup checklist.

---

## 🏆 Level 7 Self-Assessment

Rate yourself on each skill (1 = shaky, 3 = confident):

| # | Skill | 1 | 2 | 3 |
|---|---|---|---|---|
| 1 | Write effective custom instructions | ☐ | ☐ | ☐ |
| 2 | Test and iteratively refine instructions | ☐ | ☐ | ☐ |
| 3 | Target context precisely with `@` | ☐ | ☐ | ☐ |
| 4 | Create and maintain `.copilotignore` | ☐ | ☐ | ☐ |
| 5 | Build reusable prompt templates | ☐ | ☐ | ☐ |
| 6 | Explain MCP architecture and use cases | ☐ | ☐ | ☐ |
| 7 | Configure MCP servers | ☐ | ☐ | ☐ |
| 8 | Manage sessions (continue, resume, clear) | ☐ | ☐ | ☐ |
| 9 | Set up terminal integration | ☐ | ☐ | ☐ |
| 10 | Handle multi-project context boundaries | ☐ | ☐ | ☐ |
| 11 | Layer instructions at different levels | ☐ | ☐ | ☐ |
| 12 | Audit and optimize configuration | ☐ | ☐ | ☐ |

**Scoring:**
- **30–36:** Ready for Level 8
- **22–29:** Repeat exercises 1-2 and 11 for deeper instruction mastery
- **Below 22:** Go back to Level 6 for more workflow practice

---

## Key Takeaways

1. **Custom instructions are the #1 optimization** — 15 min setup, hours saved
2. **Test instructions with real generation** — don't assume they work, verify
3. **Context is a budget** — load exactly what's needed, no more
4. **`.copilotignore` prevents noise** — exclude generated, compiled, and vendor files
5. **Prompt templates standardize quality** — share them with your team
6. **MCP servers extend capabilities** — database, APIs, deployment tools
7. **Sessions have a lifecycle** — continue, resume, clear, restart
8. **Terminal setup enables multiline** — `/terminal-setup` once, benefit forever
9. **Instructions layer from general to specific** — org → repo → personal → session
10. **Audit regularly** — conventions change, instructions should follow

---

## What's Next

**Level 8: Advanced — Copilot Coding Agent, ACP & SDK** explores GitHub's autonomous coding agent (works on issues/PRs), the Agent Control Plane (ACP) for building AI tools, and the Copilot SDK for custom integrations.

→ Continue to `workshop/level-8/README.md`

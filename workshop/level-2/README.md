# Level 2: Understand — Ask Questions & Get Explanations

> **Risk level:** 🟢 Zero — Nothing in this level modifies any files. You are still read-only.

## Learning Objectives

By the end of this level, you will be able to:

1. Map import/dependency graphs across a multi-file codebase
2. Identify architectural layers and explain how data flows through them
3. Trace execution paths top-down (entry point → output) and bottom-up (model → caller)
4. Analyze configuration and environment dependencies
5. Recognize design patterns and explain why they were chosen
6. Discover potential bugs, code smells, and edge cases without modifying code
7. Ask hypothetical "what if" questions to test understanding
8. Compare and contrast different implementations within the same codebase
9. Generate documentation and summaries from code
10. Craft effective prompts that yield deep, actionable answers
11. Strategically manage context across extended analysis sessions
12. Build a complete mental model of an unfamiliar codebase

---

## Prerequisites

- [ ] Completed **Level 1** (comfortable with `@`, `!`, `/help`, `/model`, `/usage`, `/context`, `/compact`)
- [ ] Copilot CLI is installed and authenticated
- [ ] You have cloned this repository locally

---

## About the Sample App

Level 2 uses a **different, more complex app** than Level 1. This is a **Bookmark Manager API** — a layered REST service with:

```
sample-app/
├── app.py              ← Entry point, dependency wiring, server start
├── routes.py           ← HTTP route handlers and dispatching
├── service.py          ← Business logic layer
├── repository.py       ← Data persistence (file + in-memory backends)
├── models.py           ← Data models with validation
├── middleware.py        ← Logging, auth, request/response helpers
├── errors.py           ← Custom exception hierarchy
├── config.py           ← Environment-based configuration
├── requirements.txt
└── tests/
    ├── test_models.py
    └── test_service.py
```

You've **never seen this code before** — that's the point. Level 2 is about building understanding of an unfamiliar codebase.

---

## Workshop Structure

This level contains **12 exercises**. Estimated time: **60–90 minutes**.

| Exercise | Topic | Time |
|----------|-------|------|
| 1 | Dependency Graph Mapping | 5 min |
| 2 | Architecture Comprehension | 7 min |
| 3 | Top-Down Execution Tracing | 7 min |
| 4 | Bottom-Up Execution Tracing | 7 min |
| 5 | Configuration & Environment Analysis | 5 min |
| 6 | Design Pattern Recognition | 7 min |
| 7 | Bug & Smell Discovery | 7 min |
| 8 | Hypothetical Reasoning | 5 min |
| 9 | Comparison & Contrast | 5 min |
| 10 | Documentation Generation | 7 min |
| 11 | Knowledge Synthesis | 5 min |
| 12 | Advanced Prompt Crafting | 5 min |

---

## Exercise 1: Dependency Graph Mapping

### Goal
Map which file imports which — the foundation of understanding any codebase.

### Steps

**1.1** Navigate to the sample app and launch Copilot:

```bash
cd workshop/level-2/sample-app
copilot
```

**1.2** Ask Copilot to map the entire import graph:

```
Read all the Python files in this directory and show me the complete import dependency graph. 
For each file, list what it imports from other project files (not stdlib).
```

**1.3** Now ask for a visual representation:

```
Draw the import graph as an ASCII diagram showing arrows from importer → imported module.
```

> You should see something like:
> ```
> app.py → config, middleware, repository, service, routes
> routes.py → service, errors, middleware
> service.py → config, models, repository, errors
> repository.py → config, models, errors
> models.py → config, errors
> middleware.py → config, errors
> errors.py → (nothing — leaf node)
> config.py → (nothing — leaf node)
> ```

**1.4** Identify the layers from the graph:

```
Based on the import graph, which files are at the bottom (imported by many, import nothing)?
Which files are at the top (import many, imported by few)?
```

### Key Concept: Import Direction = Dependency Direction

- Files at the **bottom** of the graph (`config.py`, `errors.py`) are **shared foundations**
- Files at the **top** (`app.py`, `routes.py`) are **orchestrators**
- A change to a bottom file **ripples up** to all importers

### ✅ Checkpoint
You can draw the import graph from memory and identify which files are foundations vs orchestrators.

---

## Exercise 2: Architecture Comprehension

### Goal
Understand the architectural layers and the responsibility of each one.

### Steps

**2.1** Ask about the overall architecture:

```
@ app.py
@ routes.py
@ service.py
@ repository.py

This app appears to have layers. Identify each layer, its responsibility, and why they are separated.
What would go wrong if routes.py directly accessed repository.py, bypassing service.py?
```

**2.2** Ask about the error handling strategy:

```
@ errors.py
@ middleware.py
@ routes.py

How does this application handle errors?
Trace an error from its origin (e.g., "bookmark not found") through to the HTTP response the client receives.
```

**2.3** Ask about the dependency injection pattern:

```
@ app.py
@ routes.py

How does the BookmarkHandler get access to the BookmarkService?
Is this dependency injection? What are the pros and cons of how it's done here?
```

**2.4** Identify the cross-cutting concerns:

```
Which concerns (logging, auth, error handling, configuration) cut across multiple layers?
How are they implemented — are they mixed into business logic or separated?
```

### Key Concept: Layered Architecture

| Layer | Rule |
|-------|------|
| Routes | Knows HTTP, doesn't know storage |
| Service | Knows business rules, doesn't know HTTP |
| Repository | Knows persistence, doesn't know business rules |
| Models | Knows data shape, doesn't know anything else |

> 💡 **Why this matters:** When you can identify layers and their boundaries, you know *where* to look when investigating bugs, *where* to add features, and *what* might break if you change something.

### ✅ Checkpoint
You can explain each layer's responsibility and trace an error from origin to HTTP response.

---

## Exercise 3: Top-Down Execution Tracing

### Goal
Trace the complete execution path from an HTTP request to the response — the way a request "falls through" the layers.

### Steps

**3.1** Trace a GET request:

```
Trace the complete execution path when a client sends: GET /bookmarks?tag=python

Start from the HTTP server receiving the request and follow every function call 
through routes → service → repository → models, all the way back to the HTTP response.
List each function called in order with its file and what it does.
```

**3.2** Trace a POST request with validation:

```
Trace: POST /bookmarks with body {"url": "not-a-url", "title": "Test"}

This should fail validation. Trace every step until the error response is returned.
At which layer does the validation happen? How does the error propagate back?
```

**3.3** Trace the auth middleware:

```
Trace: GET /bookmarks with an invalid Authorization header, when BM_AUTH_ENABLED=true.

What code runs before the route handler? At which point is the request rejected?
```

**3.4** Trace a POST that creates a bookmark in file storage:

```
Trace: POST /bookmarks with body {"url": "https://example.com", "title": "Example", "tags": ["test"]}
Assume storage backend is "file". Follow the data from the HTTP body all the way to disk.
```

### Key Concept: Following the Call Stack

Each trace teaches you which functions are involved and **in what order**. This is the single most effective way to understand unfamiliar code.

| Trace Type | What You Learn |
|---|---|
| **Happy path** (GET list) | Normal data flow through all layers |
| **Validation failure** (bad POST) | Where validation lives and how errors propagate |
| **Auth rejection** | How middleware intercepts before routes |
| **Write path** (successful POST) | Data transformation from JSON → model → storage |

### ✅ Checkpoint
You can trace any request type through all layers and predict which functions are called in which order.

---

## Exercise 4: Bottom-Up Execution Tracing

### Goal
Start from a low-level component and trace *upward* to understand all its callers.

### Steps

**4.1** Start from the Bookmark model:

```
@ models.py

The Bookmark class is a dataclass. Which files create Bookmark instances?
Which files call Bookmark methods (touch, archive, to_dict, from_dict)?
Show me every caller across the entire codebase.
```

**4.2** Start from an error class:

```
@ errors.py

Where is DuplicateError raised? Trace upward — which service method raises it, 
and how does it reach the HTTP response? What status code does the client get?
```

**4.3** Start from the repository interface:

```
@ repository.py

The BaseRepository abstract class defines the contract. 
Which concrete classes implement it? Which methods in service.py call which repository methods?
```

**4.4** Start from a configuration value:

```
@ config.py

Trace MAX_BOOKMARKS: where is it defined, where is it read, and what happens when the limit is reached?
Follow the entire chain from config → service → error → HTTP response.
```

### Key Concept: Bottom-Up vs Top-Down

| Direction | When to Use |
|---|---|
| **Top-down** (entry → output) | Understanding a specific feature or request flow |
| **Bottom-up** (component → callers) | Understanding the impact of changing a component |

> 💡 Both directions together give you **complete understanding** of how a component fits into the system.

### ✅ Checkpoint
You can trace from any model/error/config value upward to all its callers and understand the impact of changes.

---

## Exercise 5: Configuration & Environment Analysis

### Goal
Understand what the application needs to run and what can be configured.

### Steps

**5.1** Map all configuration:

```
@ config.py

List every configurable value: its environment variable name, default value, type, and purpose.
Format as a table.
```

**5.2** Identify configuration risks:

```
@ config.py

What happens if someone sets BM_PORT=abc (non-numeric)?
What happens if BM_STORAGE=redis (unsupported backend)?
Which of these failures happen at startup vs at runtime?
```

**5.3** Analyze the auth configuration:

```
@ config.py
@ middleware.py

If BM_AUTH_ENABLED=true but BM_AUTH_TOKEN is empty, what happens?
Does the Config.validate() method catch this? When does validate() get called?
```

**5.4** Check for hardcoded values that should be configurable:

```
Read all Python files. Are there any hardcoded values (magic numbers, hardcoded paths, 
hardcoded limits) that probably should be in config.py but aren't?
```

### ✅ Checkpoint
You can enumerate all configuration, identify risks, and spot hardcoded values that should be externalized.

---

## Exercise 6: Design Pattern Recognition

### Goal
Identify design patterns used in the codebase and understand why they were chosen.

### Steps

**6.1** Ask Copilot to identify all patterns:

```
Read all Python files in this project. Identify every design pattern used 
(e.g., Repository, Factory, Strategy, etc.). For each pattern, specify:
1. Which file(s) implement it
2. What problem it solves
3. What the alternative would be
```

**6.2** Deep-dive into the Repository pattern:

```
@ repository.py

This uses the Repository pattern with an abstract base and two concrete implementations.
Why is this better than having the service layer directly read/write JSON files?
What would it take to add a third backend (e.g., SQLite)?
```

**6.3** Examine the Factory pattern:

```
@ repository.py

The create_repository() function is a Factory. What decision does it make?
What happens if someone passes an invalid backend name?
```

**6.4** Examine the Exception hierarchy:

```
@ errors.py

This has a custom exception hierarchy. Why not just use Python's built-in ValueError, FileNotFoundError, etc.?
What advantage does AppError.to_dict() provide?
How does the status_code class attribute map exceptions to HTTP responses?
```

**6.5** Look for missing patterns:

```
Are there any places in this codebase where a design pattern SHOULD be used but isn't?
For example, are there any violations of the patterns already established?
```

### ✅ Checkpoint
You can name every design pattern in the codebase, explain its purpose, and identify where patterns are missing.

---

## Exercise 7: Bug & Smell Discovery

### Goal
Find potential bugs, code smells, and edge cases — without fixing them (that's Level 4+).

### Steps

**7.1** Ask for a broad code review:

```
Read all Python files in this project. Find potential bugs, code smells, 
race conditions, or edge cases. Rank them by severity (critical, medium, low).
Only report real issues, not style preferences.
```

**7.2** Focus on thread safety:

```
@ repository.py

Both InMemoryRepository and FileRepository use threading.Lock.
Are there any operations that read data outside the lock and might see stale state?
Are there any race conditions in the file-based repository?
```

**7.3** Focus on input validation gaps:

```
@ routes.py
@ models.py

Is there any path where user input reaches the system without being validated?
For example, what happens with the PUT /bookmarks/:id route — 
does it validate the updated fields the same way creation does?
```

**7.4** Focus on error handling completeness:

```
@ routes.py
@ middleware.py

Are there any code paths where an exception could escape without being caught?
What happens if json.dumps() fails in send_json_response?
```

**7.5** Check the test coverage gaps:

```
@ tests/test_models.py
@ tests/test_service.py

What scenarios are tested? More importantly, what scenarios are NOT tested?
List the untested edge cases that could hide bugs.
```

### Key Concept: Discovery vs Fixing

In Level 2, you **discover** issues. In Level 4+, you **fix** them. The skill of discovering issues through targeted questions is valuable on its own — it's how senior engineers review unfamiliar code.

### ✅ Checkpoint
You've found multiple real issues across different categories (thread safety, validation, error handling, test gaps).

---

## Exercise 8: Hypothetical Reasoning

### Goal
Ask "what if" questions to test and deepen your understanding without making any changes.

### Steps

**8.1** Ask about feature impact:

```
What if I wanted to add a "favorites" feature (mark bookmarks as favorites)?
Which files would need to change? What would the data flow look like?
Don't write any code — just explain the plan.
```

**8.2** Ask about failure scenarios:

```
What happens if the bookmarks.json file is deleted while the server is running?
Which operations would fail? Which would succeed? Would data be lost?
```

**8.3** Ask about scaling:

```
What if this application had 100,000 bookmarks in the JSON file?
Which operations would become slow? Why?
What would be the first bottleneck?
```

**8.4** Ask about security:

```
If this API were deployed publicly, what are the top 3 security concerns?
Consider: authentication, input validation, file access, denial of service.
```

**8.5** Ask about removing a component:

```
What if I removed the entire middleware.py file?
Which imports would break? What functionality would be lost?
Could the app still start and serve requests?
```

### Key Concept: Hypothetical Reasoning Builds Mental Models

| Question Type | What It Tests |
|---|---|
| "What if I add X?" | Understanding of architecture boundaries |
| "What if X fails?" | Understanding of error handling paths |
| "What if X scales?" | Understanding of performance characteristics |
| "What if I remove X?" | Understanding of coupling and dependencies |

### ✅ Checkpoint
You can predict the impact of changes, failures, and scaling without looking at the code.

---

## Exercise 9: Comparison & Contrast

### Goal
Compare different implementations within the codebase to understand design tradeoffs.

### Steps

**9.1** Compare the two repository backends:

```
@ repository.py

Compare InMemoryRepository and FileRepository:
1. Which operations are faster in each?
2. Which is safer for concurrent access?
3. Which handles errors more gracefully?
4. When would you choose one over the other?
```

**9.2** Compare error handling styles:

```
@ errors.py
@ models.py
@ service.py

Compare how errors are created and propagated in:
- models.py (validation errors in __post_init__)
- service.py (business logic errors)
- errors.py (exception class definitions)

Are they consistent? Are there different patterns used for the same concept?
```

**9.3** Compare this app with the Level 1 app:

```
Compare the architecture of this bookmark manager (8 files, layered architecture) 
with a simpler approach where everything is in one or two files.
What does the layered approach buy us? What does it cost?
```

**9.4** Compare route handling approaches:

```
@ routes.py

The _dispatch method uses regex matching for routes. 
Compare this approach to alternatives like a route dictionary or a decorator-based router.
What are the tradeoffs of the approach used here?
```

### ✅ Checkpoint
You can articulate tradeoffs between different approaches and explain when each is appropriate.

---

## Exercise 10: Documentation Generation

### Goal
Have Copilot generate documentation from code — testing both your understanding and Copilot's synthesis ability.

### Steps

**10.1** Generate an API reference:

```
Read routes.py and generate a complete API reference document.
For each endpoint, include: method, path, request body (if any), 
response format, possible error codes, and an example curl command.
```

**10.2** Generate a deployment guide:

```
Read config.py and app.py. Generate a deployment guide that covers:
1. All environment variables with descriptions and defaults
2. How to start the server
3. How to choose between storage backends
4. How to enable authentication
```

**10.3** Generate a developer onboarding doc:

```
If a new developer joined this project, what would they need to know?
Generate a "Developer Guide" covering:
1. Architecture overview
2. How to add a new endpoint
3. How to add a new storage backend
4. How to run tests
5. Key design decisions and why they were made
```

**10.4** Generate a changelog-style summary:

```
Based on the test files, generate a list of all behaviors/features 
this application is known to support (i.e., what the tests verify).
Format it as a feature list.
```

### Key Concept: Documentation as Understanding Verification

If Copilot can generate accurate documentation, it means:
1. It has successfully synthesized the codebase
2. The codebase is well-structured enough to explain
3. YOU can verify the documentation by comparing with your understanding from Exercises 1–9

> 💡 **If the generated docs have errors, that reveals gaps in the codebase** (missing docstrings, unclear naming, ambiguous patterns).

### ✅ Checkpoint
You can generate and verify API docs, deployment guides, and onboarding documents from the codebase.

---

## Exercise 11: Knowledge Synthesis

### Goal
Combine everything you've learned into a coherent mental model — proving you truly understand the codebase.

### Steps

**11.1** Ask Copilot to quiz you (then answer yourself before reading its response):

```
Generate 5 challenging questions about this codebase that would test whether someone 
truly understands it. Include questions about architecture, error handling, 
concurrency, and design decisions.
```

> Before reading Copilot's answers, **try to answer each question yourself**. Then compare.

**11.2** Ask Copilot for a one-paragraph summary:

```
Summarize this entire application in exactly one paragraph. 
Include: what it does, how it's structured, key design decisions, and main limitations.
```

> 💡 Compare this summary with your own understanding. Can you identify anything it missed?

**11.3** Ask about the test architecture:

```
@ tests/test_models.py
@ tests/test_service.py

How do the tests relate to the main code? 
Do they test at the right level of abstraction?
What's the testing strategy — unit tests, integration tests, or both?
```

**11.4** Compress and retain:

```
/compact
```

Then ask:

```
Based on what you remember about this project, what are the 3 most important things
a developer should know before making changes?
```

> This tests whether `/compact` retained the most essential information.

### ✅ Checkpoint
You can answer deep questions about the codebase, summarize it concisely, and retain understanding after context compression.

---

## Exercise 12: Advanced Prompt Crafting

### Goal
Learn to write prompts that consistently get deep, useful, actionable answers.

### Steps

**12.1** Compare a weak prompt vs a strong prompt:

First, try the weak version:

```
Tell me about the service layer.
```

Note the response quality. Then try the strong version:

```
@ service.py
@ repository.py
@ errors.py

Analyze the BookmarkService class:
1. List every public method with its signature and purpose
2. For each method, which repository methods does it call?
3. Which errors can each method raise, and under what conditions?
4. Which methods have side effects (change state) vs are read-only?
```

> 💡 **The strong prompt is specific, scoped, and structured.** It tells Copilot exactly what to analyze and how to format the answer.

**12.2** Practice the "trace + compare + judge" pattern:

```
@ repository.py

1. TRACE: Walk through FileRepository.save() step by step
2. COMPARE: How does this differ from InMemoryRepository.save()?
3. JUDGE: Which implementation is more robust? Why?
```

**12.3** Practice the "assume a role" pattern:

```
You are a security auditor reviewing this codebase. 
Read all files and identify the top 5 security concerns, ranked by severity.
For each, explain the attack scenario and what an attacker could achieve.
```

**12.4** Practice the "teach me" pattern:

```
@ repository.py

Explain the abstract base class pattern used here as if I'm a junior developer 
who has never used ABC before. Use the actual code as examples.
```

**12.5** Document your best prompt patterns:

```
!echo "My effective prompt patterns:" > /dev/null
```

Here are the patterns that consistently work:

| Pattern | Template | When to Use |
|---------|----------|-------------|
| **Structured analysis** | "List every X with Y and Z" | Exhaustive enumeration |
| **Trace** | "Trace the path from A to B" | Understanding execution flow |
| **Compare + Judge** | "Compare X and Y, then judge which is better" | Evaluating tradeoffs |
| **Role** | "You are a [role]. Review this for [concern]" | Focused expert analysis |
| **Teach me** | "Explain X as if I'm a [level] developer" | Learning concepts from code |
| **What if** | "What if [scenario]? What would break/change?" | Impact analysis |
| **Multi-file scope** | `@ file1` `@ file2` then question | Precise cross-file analysis |

### ✅ Checkpoint
You can craft prompts that consistently produce deep, structured, actionable answers.

---

## 🏆 Level 2 Self-Assessment

Rate yourself on each skill (1 = shaky, 3 = confident):

| # | Skill | 1 | 2 | 3 |
|---|---|---|---|---|
| 1 | Map the import/dependency graph of an unfamiliar codebase | ☐ | ☐ | ☐ |
| 2 | Identify architectural layers and their boundaries | ☐ | ☐ | ☐ |
| 3 | Trace execution top-down (request → response) | ☐ | ☐ | ☐ |
| 4 | Trace execution bottom-up (component → all callers) | ☐ | ☐ | ☐ |
| 5 | Analyze configuration, environment variables, and risks | ☐ | ☐ | ☐ |
| 6 | Identify design patterns and explain their purpose | ☐ | ☐ | ☐ |
| 7 | Discover bugs, smells, and edge cases through questions | ☐ | ☐ | ☐ |
| 8 | Ask hypothetical "what if" questions to test understanding | ☐ | ☐ | ☐ |
| 9 | Compare implementations and articulate tradeoffs | ☐ | ☐ | ☐ |
| 10 | Generate and verify documentation from code | ☐ | ☐ | ☐ |
| 11 | Synthesize understanding into a coherent mental model | ☐ | ☐ | ☐ |
| 12 | Craft prompts that consistently yield deep answers | ☐ | ☐ | ☐ |

**Scoring:**
- **30–36:** Ready for Level 3
- **22–29:** Review exercises 6–12 once more
- **Below 22:** Repeat the level with a different codebase for fresh practice

---

## Key Takeaways

1. **Import graphs are your map** — always start with dependency mapping
2. **Top-down + bottom-up tracing = complete understanding** — do both
3. **Hypothetical questions build mental models** — "what if" is your most powerful tool
4. **Bugs are found through targeted questions** — thread safety, validation gaps, error handling completeness
5. **Documentation generation verifies understanding** — if the docs are wrong, you'll catch it
6. **Prompt structure matters enormously** — specific, scoped, multi-step prompts get 10x better answers
7. **Context management is strategic** — `/compact` before switching topics, not after running out

---

## What's Next

**Level 3: Plan — Think Before Acting** takes you from understanding to planning. You'll learn to create, review, refine, and reject implementation plans using `/plan` — the critical skill that prevents runaway changes.

→ Continue to `workshop/level-3/README.md`

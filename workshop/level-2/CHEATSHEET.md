# Level 2 — Quick Reference Card

## Prompt Patterns (The Core of Level 2)

| Pattern | Template | Best For |
|---------|----------|----------|
| **Structured Analysis** | "List every X with Y and Z" | Exhaustive enumeration of methods, fields, errors |
| **Top-Down Trace** | "Trace from HTTP request to response" | Understanding feature flows |
| **Bottom-Up Trace** | "Where is X used? Show all callers" | Understanding component impact |
| **Compare + Judge** | "Compare X and Y, then judge which is better" | Evaluating design tradeoffs |
| **What If** | "What if [scenario]? What breaks?" | Impact analysis, edge cases |
| **Role-Based** | "You are a [security auditor]. Review for [concern]" | Focused expert analysis |
| **Teach Me** | "Explain X as if I'm a [level] developer" | Learning concepts from code |
| **Multi-File Scope** | `@ file1` `@ file2` then question | Cross-file analysis |

## Analysis Techniques

| Technique | How |
|-----------|-----|
| **Dependency mapping** | "Show the import graph for all files" |
| **Layer identification** | "Which file handles HTTP? Which handles storage?" |
| **Config audit** | "List all env vars with defaults and risks" |
| **Pattern recognition** | "What design patterns are used? Where?" |
| **Bug discovery** | "Find thread safety, validation, error handling issues" |
| **Test gap analysis** | "What scenarios are NOT tested?" |
| **Doc generation** | "Generate an API reference from routes.py" |

## Question Depth Progression

```
Shallow:  "What does service.py do?"
          ↓
Medium:   "List every method in BookmarkService with its repository calls"
          ↓
Deep:     "Trace create_bookmark from HTTP body through validation, 
           duplicate check, storage, and back to JSON response.
           Which errors can occur at each step?"
```

## Multi-File Context Patterns

```
# Architecture analysis
@ app.py
@ routes.py
@ service.py
@ repository.py
"Explain the layers and data flow"

# Error flow analysis
@ errors.py
@ middleware.py
@ routes.py
"Trace a NotFoundError from raise to HTTP response"

# Configuration impact
@ config.py
@ repository.py
@ middleware.py
"Which config values affect which components?"
```

## Context Management Strategy

| Context Usage | Action |
|---------------|--------|
| **< 50%** | Keep exploring, context is fresh |
| **50–70%** | Consider `/compact` if switching topics |
| **70–90%** | `/compact` now — context quality degrades |
| **> 90%** | Auto-compression imminent — `/compact` immediately |

## Exercises at a Glance

| # | Exercise | Key Skill |
|---|----------|-----------|
| 1 | Dependency Graph Mapping | Import/dependency visualization |
| 2 | Architecture Comprehension | Layer identification and boundaries |
| 3 | Top-Down Tracing | Request → response flow |
| 4 | Bottom-Up Tracing | Component → all callers |
| 5 | Configuration Analysis | Env vars, defaults, risks |
| 6 | Pattern Recognition | Design patterns and their purpose |
| 7 | Bug & Smell Discovery | Thread safety, validation, error gaps |
| 8 | Hypothetical Reasoning | "What if" impact analysis |
| 9 | Comparison & Contrast | Tradeoff evaluation |
| 10 | Documentation Generation | API docs, guides from code |
| 11 | Knowledge Synthesis | Mental model building |
| 12 | Advanced Prompt Crafting | Structured, deep prompts |

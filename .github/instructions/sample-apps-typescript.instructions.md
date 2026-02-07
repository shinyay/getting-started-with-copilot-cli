---
applyTo: "workshop/level-7/sample-app/**/*.{ts,js,json}"
---

# TypeScript Sample App Instructions (Level 7 — Event API)

## Purpose

The Event API is a TypeScript/Express application used to teach Copilot CLI
**customization** — custom instructions, context optimization, MCP configuration,
and instruction layering. It intentionally includes areas where well-crafted
custom instructions dramatically improve Copilot's output quality.

## Runtime & Tooling

| Aspect | Standard |
|--------|----------|
| Runtime | Node.js 20+ |
| Language | TypeScript 5.x with `strict: true` |
| Target | ES2020 |
| Framework | Express 4.x |
| Testing | Jest with `describe`/`it`/`beforeEach` |
| Module | CommonJS in compiled output |

## Code Style

- **Imports**: Named imports — `import { Router } from 'express'`
- **Variables**: `const` by default, `let` only when reassignment is necessary
- **Functions**: Arrow functions for callbacks and short functions
- **Naming**: `camelCase` for functions/variables, `PascalCase` for types/interfaces/classes
- **Strings**: Single quotes
- **Semicolons**: Required
- **Line length**: 100 characters max

## Architecture Patterns

```
src/
  routes/      → HTTP routing, parameter extraction, response formatting
  services/    → Business logic, data operations, validation orchestration
  middleware/  → Auth, request validation, error handling, logging
  models/      → Type definitions, interfaces, enums
  utils/       → Logger, response helpers, validators
```

- Routes call services, never access data directly
- Services contain business logic, throw `AppError` on failures
- Middleware handles cross-cutting concerns

## Error Handling

- Use `AppError` class with factory methods: `.notFound()`, `.badRequest()`, `.unauthorized()`
- Every `AppError` has a machine-readable `code` and HTTP `statusCode`
- Global error middleware catches `AppError` and formats the response
- Never throw raw `Error` — always use `AppError`

## API Response Format

- Wrap all responses in `ApiResponse<T>`: `{ success, data, message?, pagination? }`
- Use `respondSuccess()` for single items, `respondPaginated()` for lists
- Error responses: `{ success: false, error: { code, message } }`

## Logging

- Use the structured `logger` module (never `console.log` in production code)
- Log levels: `error`, `warn`, `info`, `debug`
- Include context: `logger.info('Event created', { eventId, userId })`

## Validation

- Define Zod schemas for all request bodies
- Apply via `validateBody(schema)` middleware in route definitions
- Schemas live alongside their corresponding route or model files

## Generated Files — Do Not Edit

- `generated/` directory: OpenAPI spec, SQL schema (auto-generated)
- `dist/` directory: compiled JavaScript output
- These files are for reference; modify the source TypeScript instead

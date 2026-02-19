# Comprehensive instructions — the "answer key" for Exercise 1

## Project: Event API (TypeScript + Express)

### Language & Runtime
- TypeScript 5.x with strict mode enabled
- Node.js 20+ / Express 4.x
- Target: ES2020

### Code Style
- Use named imports only. Never use `import *` or default imports for project modules.
- camelCase for variables, functions, and parameters.
- PascalCase for types, interfaces, and classes.
- UPPER_SNAKE_CASE for constants.
- Prefer `const` over `let`. Never use `var`.
- Use arrow functions for callbacks and anonymous functions.
- Use regular function declarations for named, exported functions.

### Error Handling
- Always use the `AppError` class from `src/utils/errors.ts`.
- Never throw plain `Error` objects.
- Use the static factory methods: `AppError.badRequest()`, `AppError.notFound()`, `AppError.unauthorized()`, `AppError.conflict()`, `AppError.internal()`.
- Include a descriptive error code (second parameter) for client-facing errors.
- Only the `errorHandler` middleware should convert AppError to HTTP responses.

### API Responses
- All endpoints must return `ApiResponse<T>` from `src/utils/response.ts`.
- Use `respondSuccess(data)` for success responses.
- Use `respondPaginated(data, page, pageSize, total)` for list endpoints.
- Never return raw objects — always wrap in ApiResponse.

### Logging
- Use the `logger` from `src/utils/logger.ts`.
- Never use `console.log`, `console.warn`, or `console.error`.
- Include context objects for structured logging: `logger.info("message", { key: value })`.
- Use appropriate levels: `debug` for development, `info` for operations, `warn` for recoverable issues, `error` for failures.

### Validation
- Use Zod schemas for all request body validation.
- Define schemas in `src/middleware/validation.ts`.
- Use the `validateBody(schema)` middleware in route definitions.

### Testing
- Use Jest with `describe`/`it` blocks. Never use `test()`.
- Group tests by function: `describe("functionName", () => { ... })`.
- Use `beforeEach` to reset state between tests.
- Test both success and error paths.
- Use `toThrow(AppError)` for error testing.

### Architecture
- Routes (`src/routes/`): HTTP translation only. No business logic.
- Services (`src/services/`): Business logic. No HTTP concepts (req, res, status codes).
- Models (`src/models/`): TypeScript interfaces and types only.
- Utils (`src/utils/`): Shared utilities (errors, logger, response).
- Middleware (`src/middleware/`): Cross-cutting concerns (validation, error handling).

### Files to Ignore
- `generated/` contains auto-generated files. Never modify them directly.
- `dist/` contains compiled output. Never import from dist/.
- `node_modules/` is third-party code.

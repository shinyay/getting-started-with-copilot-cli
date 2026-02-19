# Event API — Level 7 Sample App

A TypeScript Express API for managing events, used to practice
**Copilot CLI customization and context optimization**.

## Structure

```
src/
├── routes/         ← Express route handlers
├── middleware/      ← Auth, validation, error handling
├── services/        ← Business logic
├── models/          ← TypeScript interfaces and types
└── utils/           ← Shared utilities

tests/               ← Jest test files
generated/           ← Auto-generated files (large, should be excluded)
docs/                ← Project documentation
```

## Conventions (encode these in Copilot instructions)

- **Error handling**: Always use `AppError` class from `utils/errors.ts`
- **Naming**: camelCase for variables/functions, PascalCase for types/interfaces
- **Imports**: Use named imports, never `import *`
- **Validation**: Use Zod schemas for request validation
- **Responses**: Always use `ApiResponse<T>` wrapper type
- **Logging**: Use the `logger` from `utils/logger.ts`, never `console.log`
- **Testing**: Use Jest with `describe/it` blocks, not `test()`

## This project is a CONFIGURATION playground

The focus is NOT on fixing bugs — it's on configuring Copilot to:
1. Follow these conventions automatically
2. Exclude irrelevant files from context
3. Use MCP servers for external tools
4. Optimize prompt patterns for this codebase

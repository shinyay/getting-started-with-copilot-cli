# Event API Architecture

## Layers

```
HTTP Request
    │
    ▼
Routes (routes/)         ← HTTP translation only
    │
    ▼
Services (services/)     ← Business logic, throws AppError
    │
    ▼
Models (models/)         ← TypeScript interfaces
```

## Error Flow

```
Service throws AppError → errorHandler middleware → respondError() → HTTP response
```

## Conventions

See `.github/copilot-instructions.md` for the full list.

Key rules:
- `AppError` for all error cases (never plain `Error`)
- `ApiResponse<T>` for all responses (never raw JSON)
- `logger` for all logging (never `console.log`)
- Zod schemas for request validation
- Named imports only (never `import *`)

# Level 7 Cheat Sheet — Customization & Configuration

## Custom Instructions Location

| Level | File | Scope |
|-------|------|-------|
| Organization | GitHub org settings (web UI) | All repos in org |
| Repository | `.github/copilot-instructions.md` | All contributors |
| Personal | `~/.config/github-copilot/instructions.md` | Your sessions |
| Session | Conversation context | Current session only |

**Priority:** Session > Personal > Repository > Organization

## Writing Good Instructions

```markdown
# Good — specific, actionable, with examples
- Use `AppError.badRequest("message", "ERROR_CODE")` for 400 errors
- Import the logger: `import { logger } from '../utils/logger'`
- Never use `console.log` — always use `logger.info()` with context

# Bad — vague, no examples
- Handle errors properly
- Use the logger
- Follow best practices
```

### Instruction Template

```markdown
## Project: [Name] ([Language] + [Framework])

### Code Style
- [naming convention]
- [import style]
- [const vs let rules]

### Error Handling
- [error class/pattern]
- [what NOT to do]

### API Responses
- [response wrapper type]
- [pagination pattern]

### Testing
- [test framework + style]
- [what NOT to do]

### Architecture
- [layer descriptions]
- [what goes where]

### Excluded Files
- [directories to ignore]
```

## `.copilotignore` Syntax

```gitignore
# Auto-generated
generated/
dist/
build/

# Third-party
node_modules/
vendor/

# Large / irrelevant
package-lock.json
yarn.lock
*.map
*.min.js
coverage/

# Data
*.sql
*.csv
*.sqlite
```

## Context Optimization

| Task | Load These | Skip These |
|------|-----------|------------|
| New service function | Service file + model file | Routes, middleware |
| New route handler | Route file + service file | Utils, models |
| New test | Test file + source file | Other tests |
| Bug fix | Buggy file + its test | Unrelated files |
| Refactoring | File being refactored | Everything else |

## MCP Configuration

```json
// .github/copilot/mcp.json (project-level)
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-name"],
      "env": {}
    }
  }
}
```

## Session Commands

| Command | Effect |
|---------|--------|
| `copilot` | New session |
| `copilot --continue` | Resume last session |
| `copilot --resume` | Pick from recent sessions |
| `/clear` | Reset context in current session |
| `/context` | Show loaded context |
| `/terminal-setup` | Configure shell integration |
| `Ctrl+C` | Cancel current generation |
| `Ctrl+D` | Exit |

## Prompt Templates

### New Service Function
```
@ [service-file] @ [model-file]
Add a [functionName] function to [service-file]:
- [requirement 1]
- [requirement 2]
Follow error handling and logging conventions from instructions.
```

### New Endpoint
```
@ [route-file] @ [service-file]
Add a [METHOD] /api/[path] endpoint:
- Validate with [schema]
- Call [serviceFunction]
- Return respondSuccess/respondPaginated
```

### Bug Fix
```
@ [buggy-file] @ [test-file]
Bug: [description]
1. Explain the root cause
2. /plan the fix
3. Implement
4. Write regression test
5. /diff then /review
```

## Configuration ROI (setup priority)

1. 🔴 **Custom instructions** — 15 min setup, highest impact
2. 🟡 **`.copilotignore`** — 5 min, cleaner context
3. 🟡 **Prompt templates** — 10 min, team consistency
4. 🟢 **MCP servers** — 20 min, project-dependent
5. 🟢 **Terminal setup** — 2 min, nice-to-have

## Tips

- **Test instructions by generating code** — don't assume, verify
- **Iterate on instructions** — every convention violation = add/clarify instruction
- **Context is a budget** — load minimum needed, not everything
- **Share prompt templates** — put them in `docs/` for the team
- **Audit quarterly** — conventions evolve, instructions should follow

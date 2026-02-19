# Level 1 — Quick Reference Card

## Syntax

| Syntax | Purpose | Token Cost |
|--------|---------|------------|
| `!command` | Run shell command directly (no AI) | **Free** |
| `@ filename` | Inject file contents into context | Adds input tokens |
| `text + Enter` | Send prompt to AI model | Input + output tokens |
| `/slash-command` | Run local CLI command | **Free** |

## Essential Slash Commands

| Command | What It Does |
|---------|-------------|
| `/help` | Show all commands and shortcuts |
| `/model` | View/switch AI model |
| `/usage` | View premium request and token stats |
| `/context` | Visualize context window consumption |
| `/compact` | Compress conversation history |
| `/exit` | Exit Copilot CLI |

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel operation / clear input / exit |
| `Ctrl+L` | Clear screen |
| `Ctrl+D` | Shutdown |
| `Esc` | Cancel current operation |
| `↑` / `↓` | Navigate command history |
| `Ctrl+A` | Move to beginning of line |
| `Ctrl+E` | Move to end of line |
| `Ctrl+W` | Delete previous word |
| `Ctrl+U` | Delete to beginning of line |
| `Ctrl+K` | Delete to end of line |
| `Ctrl+O` | Expand recent timeline (no input) |
| `Ctrl+E` | Expand all timeline (no input) |
| `Ctrl+T` | Toggle model reasoning display |

## Tool Approval Options

| Option | Meaning |
|--------|---------|
| **Allow** | Approve this one call only |
| **Deny** | Block this call |
| **Allow for session** | Auto-approve this tool for the session |

## Cost-Awareness Rules

```
Free:           !command, /help, /model, /usage, /context, /compact
Costs tokens:   Every natural-language prompt
Costs 1+ req:   Every prompt sent to the model
```

## Effective Question Patterns

| Pattern | Example |
|---------|---------|
| Structure | "What files are in this project and what does each one do?" |
| Data flow | "Trace the execution path when I run `python main.py add ...`" |
| Edge cases | "What happens if the JSON file is corrupted?" |
| Comparison | "How does `format_table` differ from `format_csv`?" |
| Dependencies | "Which files import from `config.py`?" |
| Deep dive | "Explain the `format_table` function line by line" |

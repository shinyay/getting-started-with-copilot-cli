# Quick Notes — Level 4 Working Copy

This is an **identical copy** of the Level 3 sample app. You will **actually modify these files** in Level 4.

The app has intentional bugs and TODOs — you'll fix them using the plans you learned to create in Level 3.

## Intentional Issues (your targets)

| # | Type | File | Issue |
|---|------|------|-------|
| 1 | 🐛 Bug | `search.py` | Case-sensitive search |
| 2 | 🐛 Bug | `models.py` | Tags not normalized (lowercase/strip) |
| 3 | 🐛 Bug | `export.py` | HTML export XSS vulnerability (no escaping) |
| 4 | 🐛 Bug | `export.py` | Newlines not converted to `<br>` in HTML |
| 5 | 🐛 Bug | `notes.py` | List doesn't sort pinned notes first |
| 6 | 🐛 Bug | `notes.py` | Edit bypasses validation (can set empty title) |
| 7 | 🐛 Bug | `storage.py` | No error handling for corrupted JSON |
| 8 | 📝 TODO | `search.py` | No search operators (tag:X, title:Y) |

## Safety Note

If you mess up, reset with:
```bash
git checkout -- workshop/level-4/sample-app/
```

# URL Shortener CLI — Level 6 Sample App

A command-line URL shortener used to practice **complete development workflows**.

## Structure

```
shortener/
├── cli.py           ← CLI entry point (argparse)
├── store.py         ← JSON-based URL storage
├── hasher.py        ← Short code generation
├── validator.py     ← URL validation (UNTESTED)
├── stats.py         ← Usage statistics (BUG: wrong after delete)
└── config.py        ← Configuration

tests/
├── test_store.py    ← Good coverage
├── test_hasher.py   ← Good coverage
├── test_validator.py ← MISSING (test gap)
└── test_stats.py    ← Incomplete coverage
```

## Usage

```bash
# Shorten a URL
python -m shortener.cli shorten https://example.com

# Expand a short code
python -m shortener.cli expand abc123

# List all URLs
python -m shortener.cli list

# Delete a short code
python -m shortener.cli delete abc123

# Show stats
python -m shortener.cli stats
```

## Known Issues (for workshop exercises)

1. **Multi-file bug**: Stats count is wrong after deleting URLs — `stats.py` reads
   from a counter that `store.py` doesn't decrement on delete
2. **Test gap**: `validator.py` has zero tests
3. **Feature gap**: No URL expiration support (timestamps exist but no expiry check)
4. **Duplicated logic**: URL validation appears in both `cli.py` and `store.py`
5. **Outdated docs**: This README has incorrect CLI examples

### Reset

```bash
git checkout -- workshop/level-6/sample-app/
```

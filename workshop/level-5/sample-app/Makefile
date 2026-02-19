.PHONY: test lint demo benchmark all clean test-file test-verbose

# Run all tests
test:
	cd $(CURDIR) && python -m pytest tests/ -v

# Run tests with short output
test-short:
	cd $(CURDIR) && python -m pytest tests/ --tb=short

# Run a specific test file (usage: make test-file FILE=tests/test_calculator.py)
test-file:
	cd $(CURDIR) && python -m pytest $(FILE) -v

# Run tests matching a keyword (usage: make test-match K=divide)
test-match:
	cd $(CURDIR) && python -m pytest tests/ -v -k "$(K)"

# Run tests verbose with full traceback
test-verbose:
	cd $(CURDIR) && python -m pytest tests/ -v --tb=long

# Run linter
lint:
	cd $(CURDIR) && python -m flake8 mathlib/

# Run linter on everything
lint-all:
	cd $(CURDIR) && python -m flake8 mathlib/ tests/ scripts/

# Run demo script
demo:
	cd $(CURDIR) && python scripts/demo.py

# Run benchmark
benchmark:
	cd $(CURDIR) && python scripts/benchmark.py

# Run lint + tests
all: lint test

# Clean generated files
clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true

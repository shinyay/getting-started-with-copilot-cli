.PHONY: test lint demo all clean test-file test-match

# Run all tests
test:
	cd $(CURDIR) && python -m pytest tests/ -v

# Run tests (short output)
test-short:
	cd $(CURDIR) && python -m pytest tests/ --tb=short -q

# Run a specific test file
test-file:
	cd $(CURDIR) && python -m pytest $(FILE) -v

# Run tests matching keyword
test-match:
	cd $(CURDIR) && python -m pytest tests/ -v -k "$(K)"

# Run the CLI
run:
	cd $(CURDIR) && python -m shortener.cli $(ARGS)

# Run all
all: test

# Clean
clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -f urls.json stats.json

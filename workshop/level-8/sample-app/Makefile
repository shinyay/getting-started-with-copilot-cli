.PHONY: api worker test lint review changelog triage all clean

# --- Service commands ---
api:
	cd services/api && node index.js

worker:
	cd services/worker && python worker.py --once

# --- Testing ---
test:
	cd services/api && npm test
	cd services/worker && python -c "import worker; print('Worker module OK')"

lint:
	cd services/api && npm run lint

# --- Copilot automation ---
review:
	bash scripts/copilot-review.sh

changelog:
	bash scripts/copilot-changelog.sh

triage:
	@echo "Usage: make triage ISSUE=<number>"
	@test -n "$(ISSUE)" && bash scripts/copilot-triage.sh $(ISSUE) || true

# --- Combined ---
all: lint test

clean:
	rm -f services/worker/jobs.json
	find . -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name node_modules -exec rm -rf {} + 2>/dev/null || true

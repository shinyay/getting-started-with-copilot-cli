#!/usr/bin/env bash
# =============================================================================
# Copilot CLI Workshop — Post-Create Initialization
# =============================================================================
# Runs once after the Dev Container is created. Sets up:
#   1. Python virtual environment with dev tools
#   2. Node.js dependencies for Level 7
#   3. Shell configuration for venv auto-activation
#   4. Welcome message with getting-started instructions
# =============================================================================
set -euo pipefail

WORKSPACE="/workspace"
VENV_DIR="${WORKSPACE}/.venv"

# ---- Colors for output ----
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

step() { echo -e "\n${BLUE}▶ $1${NC}"; }
ok()   { echo -e "  ${GREEN}✔ $1${NC}"; }
info() { echo -e "  ${YELLOW}ℹ $1${NC}"; }

# =============================================================================
# 1. Python Virtual Environment
# =============================================================================
step "Creating Python virtual environment..."

if [[ ! -d "${VENV_DIR}" ]]; then
    python3 -m venv "${VENV_DIR}"
    ok "Created venv at ${VENV_DIR}"
else
    info "venv already exists at ${VENV_DIR}"
fi

# Activate for this script
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

step "Upgrading pip..."
pip install --upgrade pip --quiet
ok "pip upgraded"

# Install workshop-wide dev tools
step "Installing Python dev tools (pytest, flake8)..."
if [[ -f "${WORKSPACE}/requirements-dev.txt" ]]; then
    pip install -r "${WORKSPACE}/requirements-dev.txt" --quiet
    ok "Installed from requirements-dev.txt"
else
    pip install pytest flake8 --quiet
    ok "Installed pytest and flake8"
fi

# Install per-level requirements (all are stdlib-only, but some list pytest/flake8)
step "Checking per-level Python requirements..."
for level_dir in "${WORKSPACE}"/workshop/level-{1,2,3,4,5,6}/sample-app; do
    if [[ -f "${level_dir}/requirements.txt" ]]; then
        pip install -r "${level_dir}/requirements.txt" --quiet 2>/dev/null || true
    fi
done
ok "Per-level requirements checked"

# =============================================================================
# 2. Node.js Dependencies (Level 7)
# =============================================================================
step "Installing Level 7 (TypeScript) dependencies..."
LEVEL7_APP="${WORKSPACE}/workshop/level-7/sample-app"
if [[ -f "${LEVEL7_APP}/package.json" ]]; then
    cd "${LEVEL7_APP}"
    npm install --quiet 2>/dev/null || npm install
    cd "${WORKSPACE}"
    ok "Level 7 npm packages installed"
else
    info "Level 7 package.json not found — skipping"
fi

# =============================================================================
# 3. Shell Configuration — venv Auto-Activation
# =============================================================================
step "Configuring shell for venv auto-activation..."

BASHRC="${HOME}/.bashrc"
ACTIVATION_MARKER="# >>> copilot-workshop venv >>>"

if ! grep -q "${ACTIVATION_MARKER}" "${BASHRC}" 2>/dev/null; then
    cat >> "${BASHRC}" << 'EOF'

# >>> copilot-workshop venv >>>
# Auto-activate the workshop Python virtual environment
if [[ -f "/workspace/.venv/bin/activate" ]]; then
    source /workspace/.venv/bin/activate
fi
# <<< copilot-workshop venv <<<
EOF
    ok "Added venv auto-activation to .bashrc"
else
    info "venv auto-activation already configured"
fi

# =============================================================================
# 4. Git Configuration (safe directory)
# =============================================================================
step "Configuring Git..."
git config --global --add safe.directory "${WORKSPACE}" 2>/dev/null || true
ok "Workspace marked as safe directory"

# =============================================================================
# 5. Verify Installation
# =============================================================================
step "Verifying installation..."

echo ""
echo "  ┌─────────────────────────────────────────────────────┐"
echo "  │ Tool            │ Version                           │"
echo "  ├─────────────────┼───────────────────────────────────┤"
printf "  │ %-15s │ %-33s │\n" "Python" "$(python3 --version 2>&1 | awk '{print $2}')"
printf "  │ %-15s │ %-33s │\n" "pip" "$(pip --version 2>&1 | awk '{print $2}')"
printf "  │ %-15s │ %-33s │\n" "pytest" "$(pytest --version 2>&1 | awk '{print $2}' || echo 'not found')"
printf "  │ %-15s │ %-33s │\n" "flake8" "$(flake8 --version 2>&1 | awk '{print $1}' || echo 'not found')"
printf "  │ %-15s │ %-33s │\n" "Node.js" "$(node --version 2>&1 || echo 'not found')"
printf "  │ %-15s │ %-33s │\n" "npm" "$(npm --version 2>&1 || echo 'not found')"
printf "  │ %-15s │ %-33s │\n" "Git" "$(git --version 2>&1 | awk '{print $3}')"
printf "  │ %-15s │ %-33s │\n" "GitHub CLI" "$(gh --version 2>&1 | head -1 | awk '{print $3}' || echo 'not found')"
printf "  │ %-15s │ %-33s │\n" "Copilot CLI" "$(copilot --version 2>&1 || echo 'run: copilot')"
echo "  └─────────────────┴───────────────────────────────────┘"

# =============================================================================
# 6. Welcome Message
# =============================================================================
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  🚀 Copilot CLI Workshop — Environment Ready!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo "  📖 Getting started:"
echo "     1. Authenticate:  gh auth login"
echo "     2. Start Copilot: copilot"
echo "     3. Open workshop: workshop/README.md"
echo ""
echo "  🐍 Python venv is auto-activated in every terminal."
echo "     Tools available: python, pytest, flake8"
echo ""
echo "  📁 Workshop levels:"
echo "     Level 1-6: Python  (workshop/level-1/ ... level-6/)"
echo "     Level 7:   TypeScript (workshop/level-7/ — npm ready)"
echo "     Level 8:   Mixed  (workshop/level-8/)"
echo ""
echo "  💡 Tip: Start with 'copilot' and ask:"
echo '     "What is this repository about?"'
echo ""

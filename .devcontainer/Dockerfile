# =============================================================================
# Copilot CLI Workshop — Dev Container Image
# =============================================================================
# Base: Python 3.12 on Debian Bookworm (includes pip, git, common build tools)
# Adds: Node.js 20, GitHub CLI, workshop utilities
# =============================================================================
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# ---- Node.js 20 (Level 7: TypeScript + Copilot CLI install) ----
# Remove stale Yarn repo (expired GPG key from base image breaks apt-get update)
ARG NODE_MAJOR=20
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && curl -fsSL https://deb.nodesource.com/setup_${NODE_MAJOR}.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ---- GitHub CLI ----
RUN (type -p wget >/dev/null || (apt-get update && apt-get install -y wget)) \
    && mkdir -p -m 755 /etc/apt/keyrings \
    && out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
    && cat $out | tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
    && chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
       | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update \
    && apt-get install -y --no-install-recommends gh \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ---- Workshop utilities ----
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
       jq \
       tree \
       shellcheck \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ---- Copilot CLI (global npm package) ----
# Pin to the version this workshop was verified against
RUN npm install -g @github/copilot@0.0.411

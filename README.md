# Forge

A CLI wrapper that scaffolds new projects using AI coding tools (Claude Code, Gemini CLI, Codex) with your Ubundi conventions baked in.

## Install

```bash
uv venv && source .venv/bin/activate
uv pip install -e .
```

## Usage

```bash
forge                # Interactive scaffold flow
forge --use claude   # Force a specific AI backend
forge --dry-run      # Preview the prompt without executing
```

## Prerequisites

At least one AI CLI tool installed: `claude`, `gemini`, or `codex`.

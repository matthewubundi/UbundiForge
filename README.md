# Forge

Forge is a Python CLI that scaffolds new projects with AI coding tools while baking in your Ubundi conventions from the start. It collects a few project details, chooses an AI backend, assembles a structured prompt, and hands off generation to Claude Code, Gemini CLI, or Codex.

## What It Does

- Prompts for project name, stack, description, Docker preference, and extra instructions
- Routes to a preferred AI backend based on the selected stack
- Injects shared conventions from `~/.forge/conventions.md`
- Optionally includes a `CLAUDE.md` template in generated projects
- Creates the target project directory and runs the selected AI CLI inside it

## Supported Stacks

- Next.js + React
- FastAPI
- Next.js + FastAPI monorepo

## Backend Routing

By default, Forge uses:

- `gemini` for Next.js projects
- `claude` for FastAPI projects
- `claude` for combined frontend/backend projects

You can override the routing with `--use`.

## Requirements

- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv) recommended for environment setup
- At least one installed AI CLI:
  - `claude`
  - `gemini`
  - `codex`

## Installation

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

## Usage

Run the interactive scaffold flow:

```bash
forge
```

Force a specific backend:

```bash
forge --use claude
forge --use gemini
forge --use codex
```

Preview the generated prompt without executing an AI tool:

```bash
forge --dry-run
```

Show the installed version:

```bash
forge --version
```

## How It Works

1. Forge collects answers through an interactive terminal flow.
2. It loads your shared conventions and optional `CLAUDE.md` template.
3. It builds a single scaffold prompt tailored to the chosen stack.
4. It launches the selected AI CLI in a new project directory.

## Project Structure

```text
forge/
├── forge/
│   ├── cli.py
│   ├── config.py
│   ├── conventions.py
│   ├── prompt_builder.py
│   ├── prompts.py
│   ├── router.py
│   ├── runner.py
│   └── templates/
├── tests/
├── pyproject.toml
└── README.md
```

## Development

Run tests:

```bash
pytest
```

Run Ruff:

```bash
ruff check .
```

## Notes

- Forge expects external AI CLIs to already be installed and available on `PATH`.
- Conventions are loaded from `~/.forge/conventions.md`. If that file does not exist, Forge creates it with defaults.
- The bundled `CLAUDE.md` template is loaded from `forge/templates/claude-md-template.md`.

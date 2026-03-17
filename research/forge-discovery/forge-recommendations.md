# Forge Recommendations

Concrete changes to improve Forge, ordered by priority. Each recommendation cites evidence from analyzed repos and identifies exact Forge files to change.

---

## Priority 1: Critical Improvements

### 1.1 Expand Stack Choices in `forge/prompts.py`

**Current state:** 3 stack options (nextjs, fastapi, both)
**Recommendation:** Add 2 new stack options: `python-cli` and `typescript-npm-package`

**Evidence:**
- Forge itself and cortex-benchmark are both Python CLI tools
- openclaw-cortex is a TypeScript npm package (375+ tests, strict mode, ESM)
- These are real, recurring Ubundi project types

**Changes to `forge/prompts.py`:**
```python
STACK_CHOICES = [
    questionary.Choice("Next.js + React (frontend or fullstack)", value="nextjs"),
    questionary.Choice("Python API (FastAPI)", value="fastapi"),
    questionary.Choice("Both (Next.js frontend + FastAPI backend)", value="both"),
    questionary.Choice("Python CLI tool", value="python-cli"),
    questionary.Choice("TypeScript npm package", value="typescript-npm"),
]
```

**Files affected:** `forge/prompts.py`, `forge/router.py`, `forge/prompt_builder.py`

---

### 1.2 Update Routing for New Stacks in `forge/router.py`

**Current state:** Only routes nextjs/fastapi/both
**Recommendation:** Add routing for new stacks

**Changes to `forge/router.py`:**
```python
ROUTING = {
    "nextjs": "gemini",
    "fastapi": "claude",
    "both": "claude",
    "python-cli": "claude",      # Claude excels at Python scaffolding
    "typescript-npm": "claude",   # Claude handles strict TS well
}
```

**Evidence:** All Python repos in the portfolio show patterns Claude handles well (Pydantic, pytest, Ruff). The TypeScript package pattern (strict mode, Vitest, Zod) is also Claude's strength.

**Files affected:** `forge/router.py`

---

### 1.3 Enrich Convention Defaults in `forge/conventions.py`

**Current state:** Conventions cover frontend styling and basic coding standards but miss significant patterns discovered in the portfolio.

**Recommendation:** Update `DEFAULT_CONVENTIONS` to include:

```markdown
## Python Toolchain
- Package manager: uv (not pip or poetry)
- Build system: hatchling (PEP 517)
- Python version: 3.12
- Linter + formatter: Ruff
  - Line length: 100
  - Rules: ["E", "F", "I", "N", "W", "UP", "B"]
- Type checker: MyPy (strict mode, ignore_missing_imports = true)
- Test framework: pytest with pytest-asyncio
- Test structure: tests/unit/ + tests/integration/ + tests/conftest.py
- pytest config: asyncio_mode = "auto", addopts = "-v --tb=short"
- Pre-commit hooks: Ruff

## Python Backend Architecture
- No ORM — use raw SQL via asyncpg for full control
- Use Pydantic for all data validation and serialization
- Use pydantic-settings for environment-based configuration
- Async/await throughout (asyncpg, httpx, FastAPI)
- Health check endpoint at /ready (returns {"status": "ok"})
- structlog for structured JSON logging in production services
- In-process async job queue for background work (no Celery)
- Single uvicorn worker in production (--workers 1)
- Limit max requests per worker (--limit-max-requests 10000)

## TypeScript Toolchain
- TypeScript strict mode always
- ESM-only (module: ESNext, "type": "module" in package.json)
- Target: ES2022
- Test framework: Vitest
- Runtime validation: Zod

## Database Conventions
- PostgreSQL as the default database
- pgvector extension for any AI/embedding features
- asyncpg as the driver (not psycopg2 for new projects)

## AI/LLM Conventions
- OpenAI as the default LLM provider
- Use tiktoken for token counting
- Use tenacity for retry logic on LLM calls
- Use rank-bm25 + pgvector for hybrid retrieval when applicable

## Documentation
- CLAUDE.md follows the WHY/WHAT/HOW template
- Include agent_docs/ for progressive disclosure in non-trivial projects
- Include scripts/ for utility scripts
- Include docs/ for architecture and API documentation

## Docker Defaults
- Base image: python:3.12-slim (Python) or node:20-slim (TypeScript)
- Non-root user (appuser)
- HEALTHCHECK on /ready endpoint
- PYTHONUNBUFFERED=1 and PYTHONDONTWRITEBYTECODE=1
```

**Evidence:**
- uv: 4/5 Python repos
- Ruff line-length 100: All Ruff-configured repos
- No ORM: All database repos (Cortex, TooToo)
- Health checks: Cortex Dockerfile, kwanda-skills
- agent_docs/: 3/8 repos
- pgvector: 2/8 repos (both major backend services)

**Files affected:** `forge/conventions.py`

---

### 1.4 Add Stack Labels for New Options in `forge/prompt_builder.py`

**Changes to `forge/prompt_builder.py`:**
```python
STACK_LABELS = {
    "nextjs": "Next.js + React",
    "fastapi": "Python API (FastAPI)",
    "both": "Next.js frontend + FastAPI backend (monorepo)",
    "python-cli": "Python CLI tool (Typer + Rich)",
    "typescript-npm": "TypeScript npm package (ESM, strict mode, Vitest)",
}
```

**Files affected:** `forge/prompt_builder.py`

---

## Priority 2: High-Value Improvements

### 2.1 Support Recipe Selection in Addition to Stack Selection

**Current state:** Forge asks 5 questions (name, stack, description, docker, extra).
**Recommendation:** After stack selection, optionally ask for a recipe that adds targeted libraries and structure.

**Example flow:**
```
What are we building? → Python API (FastAPI)
Recipe? (optional)
  > Standard API (default)
  > AI Workflow Service (adds OpenAI, pgvector, tiktoken, retrieval pipeline)
  > Scheduled Worker (adds EventBridge, DynamoDB, cron-triggered)
  > Skip recipe
```

**Evidence:**
- Cortex is an "AI workflow service" that extends FastAPI with specific AI libraries
- Reddit Scraper is a "scheduled worker" that extends Python with AWS scheduling
- These are distinct enough to warrant different scaffolds but share the same stack base

**Implementation:**
- Add a `recipes.py` module that maps stack → available recipes
- Each recipe adds additional prompt instructions (libraries, structure, .env.example extras)
- Inject recipe context into prompt_builder alongside conventions

**Files affected:** New `forge/recipes.py`, `forge/prompts.py`, `forge/prompt_builder.py`

---

### 2.2 Support Optional Integrations as Structured Prompts

**Current state:** Users can type "add Clerk auth" in the extra instructions field.
**Recommendation:** Add a multi-select question for common integrations.

**Example flow:**
```
Optional integrations? (select all that apply)
  [ ] Clerk authentication
  [ ] OpenAI / LLM integration
  [ ] Segment analytics
  [ ] AWS S3 file storage
  [ ] PostgreSQL + pgvector
  [ ] GitHub Actions CI
```

**Evidence:**
- Clerk: 1/1 frontend repos
- OpenAI: 3/8 repos
- Segment: 1/8 repos
- boto3/S3: 3/8 repos
- pgvector: 2/8 repos
- GitHub Actions: 3/8 repos

**Implementation:**
- Add `integrations.py` with structured integration definitions
- Each integration includes: libraries, env vars, setup instructions, code snippets
- Selected integrations injected into prompt as structured blocks

**Files affected:** New `forge/integrations.py`, `forge/prompts.py`, `forge/prompt_builder.py`

---

### 2.3 Support Per-Stack Prompt Templates

**Current state:** One prompt template for all stacks.
**Recommendation:** Allow per-stack prompt templates that include stack-specific structure and conventions.

**Evidence:** The directory structure differs significantly by stack:
- FastAPI: `api/`, `{project}/`, `tests/`
- Next.js: `src/app/`, `src/components/`, `src/lib/`
- Both: `api/`, `frontend/`, `domain/`, `application/`, `infrastructure/`
- CLI: `{project}/`, `tests/`, `Makefile`
- TypeScript npm: `src/`, `tests/unit/`, `dist/`

**Implementation:**
- Create `forge/templates/` directory with per-stack prompt fragments
- `fastapi.md`, `nextjs.md`, `both.md`, `python-cli.md`, `typescript-npm.md`
- Each contains stack-specific directory structure, library list, and pyproject.toml/package.json config

**Files affected:** New `forge/templates/*.md`, `forge/prompt_builder.py`

---

### 2.4 Improve CLAUDE.md Template

**Current state:** Template exists at `forge/templates/claude-md-template.md`
**Recommendation:** The template should be more prescriptive based on portfolio evidence.

**Key additions based on Ubundi CLAUDE.md analysis:**
1. Always include "Key Entrypoints" section (present in Cortex, openclaw-cortex, TooToo)
2. Always include "Key Patterns" section (present in Cortex, openclaw-cortex)
3. Always include "Non-Obvious Things" section (present in Cortex, openclaw-cortex)
4. Add "Progressive Disclosure" section pointing to agent_docs/ (present in Cortex, TooToo)
5. Add "Verify Changes" section with exact lint/test commands (present in all CLAUDE.md files)

**Evidence:**
- `Cortex/CLAUDE.md` — not directly readable but referenced in README
- `cortex-benchmark/CLAUDE.md` — comprehensive WHY/WHAT/HOW structure
- `openclaw-cortex/CLAUDE.md` — versioning, patterns, non-obvious things
- `TooToo/CLAUDE.md` — clean architecture, key entrypoints

**Files affected:** `forge/templates/claude-md-template.md`

---

## Priority 3: Nice-to-Have Improvements

### 3.1 Add CI Pipeline Generation

**Current state:** No CI pipeline generated.
**Recommendation:** Add optional GitHub Actions CI generation.

**Standard CI template (from portfolio):**
- **Python:** lint (ruff check) → format check → type check (mypy) → unit tests (pytest)
- **TypeScript:** type check (tsc --noEmit) → build → unit tests (vitest)

**Evidence:** 3/8 repos have GitHub Actions CI. All follow the same pattern.

**Implementation:** Add "Include GitHub Actions CI?" confirm question. Generate `.github/workflows/ci.yml`.

**Files affected:** `forge/prompts.py`, `forge/prompt_builder.py`

---

### 3.2 Add Makefile Generation for Python Projects

**Current state:** No Makefile generated.
**Recommendation:** Include Makefile for Python projects with standard targets.

**Template (from cortex-benchmark):**
```makefile
.PHONY: lint format test check

lint:
	uv run ruff check {project} tests
	uv run ruff format --check {project}

format:
	uv run ruff check --fix {project}
	uv run ruff format {project}

test:
	uv run pytest tests/

check: lint test
```

**Evidence:** cortex-benchmark Makefile. Convenient for developers who prefer `make check`.

**Files affected:** `forge/prompt_builder.py`

---

### 3.3 Add pre-commit Hook Generation

**Current state:** No pre-commit hooks generated.
**Recommendation:** Optionally generate `.pre-commit-config.yaml` for Python projects.

**Template (from portfolio):**
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.5.7
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

**Evidence:** 2/8 repos (Cortex, cortex-benchmark) use pre-commit with Ruff.

**Files affected:** `forge/prompt_builder.py`

---

## Summary: Recommended Change Priority

| # | Change | Priority | Effort | Files |
|---|---|---|---|---|
| 1.1 | Expand stack choices | Critical | Low | prompts.py |
| 1.2 | Update routing | Critical | Low | router.py |
| 1.3 | Enrich conventions | Critical | Medium | conventions.py |
| 1.4 | Add stack labels | Critical | Low | prompt_builder.py |
| 2.1 | Recipe selection | High | Medium | New recipes.py, prompts.py, prompt_builder.py |
| 2.2 | Optional integrations | High | Medium | New integrations.py, prompts.py, prompt_builder.py |
| 2.3 | Per-stack templates | High | Medium | New templates/*.md, prompt_builder.py |
| 2.4 | Improve CLAUDE.md template | High | Low | templates/claude-md-template.md |
| 3.1 | CI pipeline generation | Nice-to-have | Low | prompts.py, prompt_builder.py |
| 3.2 | Makefile generation | Nice-to-have | Low | prompt_builder.py |
| 3.3 | pre-commit hooks | Nice-to-have | Low | prompt_builder.py |

**Quickest wins:** 1.1 + 1.2 + 1.4 can be done in 15 minutes. 1.3 takes longer but has the highest impact on scaffold quality.

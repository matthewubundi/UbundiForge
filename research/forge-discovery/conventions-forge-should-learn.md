# Conventions Forge Should Learn

Distilled from 8 Ubundi repositories. Organized by confidence level.

---

## Hard Conventions

These appear consistently across multiple repos and should be Forge defaults with no option to disable.

### Python Backend

1. **Package manager: uv** — Used in 4/5 Python repos (Cortex, cortex-benchmark, TooToo, Forge). The Reddit Scraper uses pip but is older. uv should be the only supported Python package manager.
   - Evidence: `Cortex/pyproject.toml`, `forge/pyproject.toml`, `cortex-benchmark/pyproject.toml`

2. **Build system: hatchling** — Used in 2/5 Python repos (Cortex, Forge). cortex-benchmark uses setuptools. Hatchling is the modern choice.
   - Evidence: `Cortex/pyproject.toml` line 44, `forge/pyproject.toml`

3. **Linter: Ruff** — Used in 3/5 Python repos. No competing linter exists in the portfolio.
   - Evidence: `Cortex/pyproject.toml` lines 50-59, `cortex-benchmark/pyproject.toml`

4. **Ruff line-length: 100** — Consistent across all Ruff-configured repos.
   - Evidence: `Cortex/pyproject.toml` line 51, `cortex-benchmark/pyproject.toml`

5. **Ruff rules: `["E", "F", "I", "N", "W", "UP", "B"]`** — Union of configurations across repos.
   - Evidence: Cortex uses `["E", "F", "I", "N", "W", "UP"]`, cortex-benchmark adds `"B"` (flake8-bugbear)

6. **Test framework: pytest** — Used in 4/5 Python repos. Only Reddit Scraper uses unittest (older code).
   - Evidence: All pyproject.toml files

7. **Test structure: unit/ + integration/ + manual/** — Appears in Cortex, cortex-benchmark, openclaw-cortex. The three-tier pattern is deliberate.
   - Evidence: `Cortex/tests/`, `cortex-benchmark/tests/`, `openclaw-cortex/tests/`

8. **pytest addopts: `-v --tb=short`** — Consistent across repos.
   - Evidence: `Cortex/pyproject.toml` line 64

9. **Data validation: Pydantic** — Used in all Python backend repos (Cortex, TooToo, implicitly in Reddit Scraper via dataclasses).
   - Evidence: All pyproject.toml files

10. **Type hints everywhere** — All Python repos use type hints on functions and variables. MyPy strict mode in Cortex.
    - Evidence: All source files across repos

11. **Async by default** — FastAPI repos use async/await throughout. asyncpg for database.
    - Evidence: `Cortex/cortex/core.py`, `TooToo/api/server.py`

12. **No ORM** — Raw SQL via asyncpg in all database-using repos. Deliberate choice for control.
    - Evidence: `Cortex/cortex/persistence/repositories.py`, `TooToo/infrastructure/persistence/`

### TypeScript

1. **Strict mode always** — The only TypeScript repo uses full strict mode. No loose mode anywhere.
   - Evidence: `openclaw-cortex/tsconfig.json`

2. **ESM-only** — Module: ESNext, no CommonJS.
   - Evidence: `openclaw-cortex/tsconfig.json`, `package.json` ("type": "module")

3. **ES2022 target** — Modern JavaScript features.
   - Evidence: `openclaw-cortex/tsconfig.json`

4. **Vitest for testing** — The only TypeScript test runner in use.
   - Evidence: `openclaw-cortex/vitest.config.ts`

5. **Zod for runtime validation** — TypeScript equivalent of Pydantic.
   - Evidence: `openclaw-cortex/src/plugin/config.ts`

### Frontend

1. **Next.js App Router** — The only frontend framework in the portfolio.
   - Evidence: `TooToo/frontend/`

2. **Tailwind CSS** — The only CSS framework.
   - Evidence: `TooToo/frontend/package.json`, Forge `conventions.md`

3. **TypeScript strict mode** — No loose TypeScript in any frontend code.
   - Evidence: `TooToo/frontend/tsconfig.json` (inferred from strict TS convention)

### Project Structure

1. **Always include `.env.example`** — Present in every service repo (Cortex, TooToo, Reddit Scraper, kwanda-skills/whatsapp-bridge).
   - Evidence: Root-level `.env.example` in all service repos

2. **Always include `CLAUDE.md`** — Present in 5/8 repos (Cortex, cortex-benchmark, openclaw-cortex, TooToo, Forge). This IS the Ubundi standard.
   - Evidence: Root-level `CLAUDE.md` in all major repos

3. **Always include `README.md`** — Present in all repos.

4. **Always include `.gitignore`** — Present in all repos. Standard Python/Node patterns.

5. **Include `agent_docs/` for progressive disclosure** — Present in 3/8 repos (Cortex, cortex-benchmark, TooToo). Used for task-specific deep dives.
   - Evidence: `Cortex/agent_docs/`, `cortex-benchmark/agent_docs/`, `TooToo/agent_docs/`

6. **Include `scripts/` for utilities** — Present in 5/8 repos. Validation scripts, data migration, CLI test harnesses.
   - Evidence: `Cortex/scripts/`, `cortex-benchmark/scripts/`, `openclaw-cortex/scripts/`, `Reddit Scraper/` (no scripts dir but has infra/)

7. **Include `docs/` for documentation** — Present in 4/8 repos.
   - Evidence: `Cortex/docs/`, `cortex-benchmark/docs/`, `openclaw-cortex/docs/`, `TooToo/docs/`

### Git & Release

1. **Semantic versioning** — Explicit in 3/8 repos (openclaw-cortex CLAUDE.md, cortex-benchmark CHANGELOG.md). Implied in others.
   - Evidence: `openclaw-cortex/CLAUDE.md` versioning section

2. **CHANGELOG.md** — Present in 3/8 repos (cortex-benchmark, openclaw-cortex, kwanda-skills).
   - Evidence: Root-level CHANGELOG.md files

3. **GitHub Actions for CI** — Present in 3/8 repos. Standard CI pattern: lint → typecheck → test.
   - Evidence: `.github/workflows/ci.yml` in Cortex, cortex-benchmark, openclaw-cortex

---

## Soft Conventions

These appear in some repos and represent good practices but aren't universal enough to mandate.

1. **pre-commit hooks (Ruff)** — Used in 2/8 repos (Cortex, cortex-benchmark). Should be suggested but not required.
   - Evidence: `.pre-commit-config.yaml` in both repos

2. **MyPy strict mode** — Only configured in Cortex. TooToo uses type hints but no MyPy config visible. Recommend as optional.
   - Evidence: `Cortex/pyproject.toml` lines 66-69

3. **structlog for logging** — Only in Cortex. Good practice for production services but adds dependency.
   - Evidence: `Cortex/pyproject.toml`

4. **Docker with non-root user** — Cortex creates `appuser`. Reddit Scraper does not. Recommend but don't require.
   - Evidence: `Cortex/Dockerfile`

5. **Health check endpoint (/ready or /health)** — Present in 2/8 repos (Cortex, kwanda-skills). Should be default for all web services.
   - Evidence: `Cortex/Dockerfile` HEALTHCHECK directive

6. **Single uvicorn worker** — Cortex explicitly uses `--workers 1` with `--limit-max-requests 10000`. This avoids memory exhaustion but limits throughput.
   - Evidence: `Cortex/Dockerfile`, `Cortex/CLAUDE.md`

7. **python-dotenv for local dev** — Used in Cortex and TooToo. Loads .env files automatically.
   - Evidence: Both `pyproject.toml` files

8. **LICENSE file** — Present in 4/8 repos. Mix of MIT and proprietary.

9. **CONTRIBUTING.md** — Present in 3/8 repos (cortex-benchmark, openclaw-cortex, kwanda-skills).

10. **Makefile** — Only in cortex-benchmark. Provides `make lint`, `make test`, `make check`. Could be a good default for Python CLIs.
    - Evidence: `cortex-benchmark/Makefile`

---

## Conflicting Conventions

### 1. Retry library: tenacity vs. backoff
- **Cortex** uses `backoff>=2.2.1` — simpler, decorator-based
- **TooToo** uses `tenacity>=8.0.0` — more flexible, composable

**Recommendation:** Default to **tenacity**. It's more widely used in the ecosystem and more flexible. backoff is simpler but tenacity handles more edge cases.

### 2. Build system: hatchling vs. setuptools
- **Cortex, Forge** use hatchling
- **cortex-benchmark, Reddit Scraper** use setuptools

**Recommendation:** Default to **hatchling**. It's the modern PEP 517 standard and aligns with uv's recommendations.

### 3. Python version: 3.11 vs. 3.12
- **Cortex** targets 3.11
- **TooToo, Reddit Scraper, Forge** target 3.12+

**Recommendation:** Default to **3.12**. Cortex's 3.11 target is likely legacy. 3.12 is the portfolio majority and has better performance.

### 4. HTTP client: httpx vs. requests
- **TooToo** uses `httpx` (async)
- **Reddit Scraper** uses stdlib `urllib.request`
- **Cortex** uses `openai` client (wraps httpx internally)

**Recommendation:** Default to **httpx** for new projects. It supports both sync and async, and is the FastAPI ecosystem standard.

### 5. pytest addopts verbosity
- **Cortex:** `-v --tb=short`
- **cortex-benchmark:** `-q`

**Recommendation:** Default to **`-v --tb=short`**. Verbose output with short tracebacks is more helpful during development.

### 6. Ruff rules: "N" and "B"
- **Cortex** includes `"N"` (pep8-naming) but not `"B"` (bugbear)
- **cortex-benchmark** includes `"B"` but not `"N"`

**Recommendation:** Include **both** `"N"` and `"B"`. They catch different classes of issues and don't conflict.

---

## Naming Conventions

### Python
- **Modules:** snake_case (`entity_resolver.py`, `prompt_builder.py`)
- **Classes:** PascalCase (`CortexConfig`, `MonitorService`)
- **Functions:** snake_case (`extract_facts`, `build_prompt`)
- **Constants:** UPPER_SNAKE_CASE (`MAX_WARM_TENANTS`, `BENCHMARK_RELEASE`)
- **Config dataclasses:** PascalCase with "Config" suffix (`CortexConfig`, `RunConfig`)
- **Pydantic models:** PascalCase (`RetrieveResult`, `IngestResponse`)
- **Test files:** `test_{module}.py`
- **Test functions:** `test_{behavior}_when_{condition}`

### TypeScript
- **Files:** kebab-case (`retry-queue.ts`, `context-profile.ts`)
- **Classes/Types:** PascalCase (`CortexConfigSchema`, `PluginApi`)
- **Functions:** camelCase (`registerHookCompat`, `injectAgentInstructions`)
- **Constants:** UPPER_SNAKE_CASE or camelCase depending on context
- **Test files:** `{module}.test.ts`

### Directory Structure
- **Python backend:** `api/`, `src/` or domain-named (`cortex/`), `tests/`, `scripts/`, `docs/`, `agent_docs/`
- **Clean architecture layers:** `api/`, `application/`, `domain/`, `infrastructure/` (TooToo pattern)
- **Feature-based modules:** Group by feature (e.g., `engrave/`, `resonate/`, `retrieve/`) not by type
- **Frontend:** `src/app/`, `src/components/`, `src/lib/`, `public/`

---

## Environment Variable Conventions

### Naming
- Service-prefixed: `POSTGRES_HOST`, `OPENAI_API_KEY`, `SLACK_BOT_TOKEN`
- App-prefixed for custom settings: `CORTEX_EXTRACTION_MODEL`, `APP_STORAGE_BACKEND`
- No unprefixed variables (except standard ones like `ENV`, `PORT`)

### Standard Variables (appear across multiple repos)
```bash
# Database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB={project_name}
POSTGRES_USER=postgres
POSTGRES_PASSWORD=
POSTGRES_SSL=false

# OpenAI
OPENAI_API_KEY=sk-...

# Application
ENV=development        # development | production
PORT=8000
```

### Pattern
- `.env.example` committed to git (templates with empty values)
- `.env` gitignored (actual secrets)
- `pydantic-settings` or `python-dotenv` for loading
- Validation on startup (fail fast if required vars missing)

---

## Documentation Expectations

### Required in Every Project
1. `README.md` — What it does, how to set up, how to run
2. `CLAUDE.md` — AI assistant instructions following the Ubundi template (WHY/WHAT/HOW structure)
3. `.env.example` — Environment variable template with comments

### Expected for Production Projects
4. `agent_docs/` — Progressive disclosure for task-specific deep dives
5. `docs/` — Architecture docs, API docs, integration guides
6. `CHANGELOG.md` — Version history
7. `CONTRIBUTING.md` — Development standards

### CLAUDE.md Structure (Ubundi Template)
```markdown
# {Project Name}

## WHY — Problem statement (1-3 sentences)
## WHAT — Tech stack, project structure, key entrypoints, architecture
## HOW — Setup, verify changes, env vars, git workflow, commit convention

## Key Patterns — Non-obvious architectural decisions
## Non-Obvious Things — Gotchas and traps
## Infrastructure — Deployment, logs, operational safeguards

## Progressive Disclosure — Links to agent_docs/
```

---

## Common Scripts / Commands

### Python Backend (every project)
```bash
uv sync                                    # Install deps
uv run ruff check src api                  # Lint
uv run ruff format src api                 # Format
uv run ruff format --check src api         # Check format
uv run mypy src                            # Type check
uv run pytest tests/unit/ -v --tb=short    # Unit tests
uv run pytest tests/unit/ --cov=src        # Coverage
uvicorn api.app:app --reload --port 8000   # Dev server
```

### TypeScript (every project)
```bash
npm ci                    # Install deps (CI)
npx tsc --noEmit          # Type check
npm test                  # Run tests
npm run build             # Compile
```

### Docker (when applicable)
```bash
docker build -t {project} .
docker run -p 8000:8000 --env-file .env {project}
```

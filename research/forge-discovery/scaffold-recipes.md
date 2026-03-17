# Scaffold Recipes

Practical scaffold recipes Forge could support, derived from the Ubundi portfolio.
Each recipe maps to a real project pattern with evidence from analyzed repos.

---

## Recipe 1: SaaS Application (Fullstack)

**Target use case:** User-facing web application with auth, analytics, and backend API
**Triggering stack:** `fullstack-monorepo` or `both`
**Exemplar repo:** TooToo

### Must-Have Files and Folders
```
{project}/
├── api/
│   ├── __init__.py
│   ├── app.py              # FastAPI app, middleware, lifespan
│   ├── routes/             # Route modules
│   │   └── __init__.py
│   ├── schemas.py          # Pydantic request/response models
│   └── dependencies.py     # Service DI
├── domain/                 # Core business logic (no framework imports)
│   ├── __init__.py
│   └── models.py           # Domain models
├── application/            # Orchestration layer
│   ├── __init__.py
│   └── services/
│       └── __init__.py
├── infrastructure/         # External services
│   ├── __init__.py
│   ├── persistence/        # Database layer
│   │   └── __init__.py
│   └── external/           # Third-party API clients
│       └── __init__.py
├── frontend/
│   ├── src/
│   │   ├── app/            # Next.js App Router pages
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   ├── components/     # React components
│   │   └── lib/            # Utility functions
│   ├── public/
│   ├── next.config.ts
│   ├── tailwind.config.ts
│   ├── tsconfig.json
│   └── package.json
├── tests/
│   ├── unit/
│   │   └── __init__.py
│   ├── integration/
│   │   └── __init__.py
│   └── conftest.py
├── scripts/
├── docs/
├── agent_docs/
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── .gitignore
├── CLAUDE.md
├── README.md
└── pyproject.toml
```

### Recommended Libraries
**Backend:** fastapi, uvicorn, pydantic, pydantic-settings, asyncpg, python-dotenv, structlog, httpx
**Frontend:** next, react, @clerk/nextjs, tailwindcss, @tailwindcss/postcss
**Dev:** pytest, pytest-asyncio, pytest-cov, ruff, mypy, vitest (frontend)

### Optional Integrations
- pgvector (if AI/embedding features)
- @segment/analytics-next (product analytics)
- @intercom/messenger-js-sdk (support chat)
- boto3 (AWS S3 for file storage)
- openai + tiktoken (LLM features)

### Setup Commands
```bash
# Backend
uv sync
cp .env.example .env
# Edit .env with database credentials

# Frontend
cd frontend && npm install

# Database
createdb {project_name}

# Run
docker-compose up  # or:
uvicorn api.app:app --reload --port 8000 &
cd frontend && npm run dev
```

### Docs to Generate
- `README.md` with setup instructions, architecture overview
- `CLAUDE.md` following Ubundi template
- `.env.example` with all required variables
- `agent_docs/architecture.md` describing the layer pattern

### CLAUDE.md Content
- WHY: Project purpose
- WHAT: Tech stack (FastAPI + Next.js + PostgreSQL), clean architecture layers, key entrypoints
- HOW: Setup (uv sync, npm install, docker-compose), verify (lint, test, build)
- Key Patterns: Clean architecture dependency direction, async/await, no ORM
- Non-Obvious Things: Domain layer has no external imports

### .env.example Content
```bash
# Database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB={project_name}
POSTGRES_USER=postgres
POSTGRES_PASSWORD=

# Auth (Clerk)
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
CLERK_SECRET_KEY=

# Application
ENV=development
PORT=8000
```

### Docker
Yes, include by default. docker-compose.yml with:
- `api` service (FastAPI, port 8000)
- `frontend` service (Next.js, port 3000)
- `db` service (PostgreSQL 16 + pgvector)

---

## Recipe 2: FastAPI JSON API

**Target use case:** Backend-only API service (no frontend)
**Triggering stack:** `fastapi`
**Exemplar repos:** Cortex, Reddit Scraper (API surface)

### Must-Have Files and Folders
```
{project}/
├── api/
│   ├── __init__.py
│   ├── app.py              # FastAPI app
│   ├── routes/
│   │   └── __init__.py
│   ├── models.py           # Pydantic schemas
│   └── shared.py           # Shared state/singletons
├── {project_name}/         # Core package (named after project)
│   ├── __init__.py
│   ├── config.py           # Configuration dataclass
│   ├── models.py           # Domain models
│   └── services/           # Business logic
│       └── __init__.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── scripts/
├── docs/
├── agent_docs/
├── Dockerfile
├── .env.example
├── .gitignore
├── CLAUDE.md
├── README.md
└── pyproject.toml
```

### Recommended Libraries
fastapi, uvicorn, pydantic, pydantic-settings, asyncpg, python-dotenv, structlog, httpx

### Optional Integrations
- pgvector (vector search)
- openai + tiktoken (LLM features)
- boto3 (AWS services)
- rank-bm25 (keyword search)
- tenacity (retry logic)
- backoff (alternative retry)

### Setup Commands
```bash
uv sync
cp .env.example .env
createdb {project_name}
uvicorn api.app:app --reload --port 8000
```

### .env.example
```bash
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB={project_name}
POSTGRES_USER=postgres
POSTGRES_PASSWORD=
ENV=development
PORT=8000
```

### Docker
Yes (optional toggle). Single-stage python:3.12-slim with:
- Non-root user
- HEALTHCHECK on /ready
- Single uvicorn worker
- --limit-max-requests 10000

---

## Recipe 3: Python CLI Tool

**Target use case:** Command-line interface for internal tools, automation, or developer utilities
**Triggering stack:** `python-cli`
**Exemplar repos:** Forge, cortex-benchmark

### Must-Have Files and Folders
```
{project}/
├── {project_name}/
│   ├── __init__.py         # Version string
│   ├── cli.py              # Typer app, entrypoint
│   └── ...                 # Feature modules
├── tests/
│   ├── __init__.py
│   └── test_cli.py
├── pyproject.toml
├── .gitignore
├── CLAUDE.md
├── README.md
└── Makefile                # Optional: lint, test, check targets
```

### Recommended Libraries
typer, rich, questionary (if interactive prompts needed)

### Optional Integrations
- httpx (API calls)
- boto3 (AWS)
- openai (LLM features)

### Setup Commands
```bash
uv sync
uv run {project_name}
# or
uv run python -m {project_name}.cli
```

### pyproject.toml Scripts Section
```toml
[project.scripts]
{project_name} = "{project_name}.cli:app"
```

### Makefile
```makefile
.PHONY: lint format test check

lint:
	uv run ruff check {project_name} tests
	uv run ruff format --check {project_name}

format:
	uv run ruff check --fix {project_name}
	uv run ruff format {project_name}

test:
	uv run pytest tests/

check: lint test
```

### Docker
No by default. CLIs typically run locally.

---

## Recipe 4: TypeScript npm Package

**Target use case:** Publishable npm package (library, plugin, SDK)
**Triggering stack:** `typescript-npm-package`
**Exemplar repo:** openclaw-cortex

### Must-Have Files and Folders
```
{project}/
├── src/
│   ├── index.ts            # Public entrypoint
│   └── ...                 # Feature modules
├── tests/
│   ├── unit/
│   │   └── *.test.ts
│   └── integration/
│       └── *.test.ts
├── dist/                   # (gitignored) compiled output
├── tsconfig.json
├── vitest.config.ts
├── vitest.integration.config.ts
├── package.json
├── .gitignore
├── CLAUDE.md
├── README.md
├── CHANGELOG.md
└── LICENSE
```

### Recommended Libraries
- zod (runtime validation)
- Dev: typescript, vitest, @types/node

### tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "lib": ["ES2022"],
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist", "tests"]
}
```

### package.json Scripts
```json
{
  "type": "module",
  "scripts": {
    "build": "tsc",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:integration": "vitest run -c vitest.integration.config.ts",
    "typecheck": "tsc --noEmit",
    "clean": "rm -rf dist"
  }
}
```

### Docker
No. npm packages don't need Docker.

---

## Recipe 5: Next.js Marketing / Landing Site

**Target use case:** Public-facing marketing site or landing page
**Triggering stack:** `nextjs`
**Exemplar:** None directly in portfolio (extrapolated from TooToo frontend + Forge conventions)

### Must-Have Files and Folders
```
{project}/
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── globals.css
│   ├── components/
│   │   ├── ui/            # Reusable UI components
│   │   └── sections/      # Page sections (hero, features, pricing)
│   └── lib/
│       └── utils.ts
├── public/
│   └── images/
├── next.config.ts
├── tailwind.config.ts
├── tsconfig.json
├── package.json
├── .gitignore
├── CLAUDE.md
└── README.md
```

### Recommended Libraries
next, react, tailwindcss, @tailwindcss/postcss

### Optional Integrations
- @segment/analytics-next (analytics)
- framer-motion (animations)

### Forge Conventions Applied
- Ubundi brand palette (dark blue-grey #1A2332, cyan-teal accents #0FA5A5)
- Glassmorphism card style
- Inter font (UI), JetBrains Mono (code)

### Docker
No by default. Deploy to Vercel or similar.

---

## Recipe 6: Scheduled Worker / Service

**Target use case:** Background job that runs on a schedule (data collection, reports, monitoring)
**Triggering stack:** `python-worker`
**Exemplar repo:** Ubundi Reddit Scraper

### Must-Have Files and Folders
```
{project}/
├── src/
│   ├── __init__.py
│   ├── main.py             # CLI entrypoint
│   ├── cli.py              # Command dispatcher
│   ├── config.py           # Configuration loader
│   ├── settings.py         # Env var validation
│   ├── models.py           # Data models
│   ├── storage.py          # Storage protocol + implementations
│   └── services.py         # Business logic
├── config/                 # Configuration files
│   └── sources.yaml
├── infra/                  # Infrastructure as code
│   └── template.yaml       # CloudFormation or Terraform
├── tests/
│   ├── __init__.py
│   ├── test_*.py
│   └── helpers.py          # Test fixtures
├── Dockerfile
├── .env.example
├── .gitignore
├── CLAUDE.md
├── README.md
└── pyproject.toml
```

### Recommended Libraries
boto3 (if AWS), requests or httpx, python-dotenv

### Setup Commands
```bash
uv sync
cp .env.example .env
python src/main.py {command}
```

### Docker
Yes. Slim base, ENTRYPOINT to allow different commands as args.

---

## Recipe 7: AI Workflow Service

**Target use case:** Backend service with LLM integration for extraction, retrieval, or analysis
**Triggering stack:** `fastapi` with AI flag
**Exemplar repos:** Cortex, TooToo

### Extends: Recipe 2 (FastAPI JSON API) with additions:

### Additional Libraries
- openai (LLM API)
- tiktoken (token counting)
- pgvector (vector search)
- rank-bm25 (keyword search)
- numpy (vector operations)
- tenacity or backoff (retry for LLM calls)
- structlog (structured logging)

### Additional Structure
```
{project}/
├── {project_name}/
│   ├── shared/
│   │   ├── llm.py          # OpenAI wrapper with retry
│   │   └── embeddings.py   # Embedding service with cache
│   ├── retrieve/           # Retrieval pipeline
│   └── extract/            # Extraction pipeline
```

### Additional .env.example
```bash
# OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini

# Embedding
EMBEDDING_MODEL=text-embedding-3-small
EMBEDDING_DIMENSIONS=1536
```

### Docker
Yes. Include pgvector extension in docker-compose PostgreSQL service.

---

## Cross-Recipe Defaults

These apply to ALL recipes:

### Always Generated
- `.gitignore` (Python or Node appropriate)
- `README.md` (setup, run, test)
- `CLAUDE.md` (WHY/WHAT/HOW template)
- `git init` + initial commit

### Python Recipes Always Include
- `pyproject.toml` with Ruff + pytest config
- Ruff rules: `["E", "F", "I", "N", "W", "UP", "B"]`
- Line length: 100
- Python version: 3.12
- Build system: hatchling
- Package manager: uv

### TypeScript Recipes Always Include
- `tsconfig.json` with strict mode
- ESM-only ("type": "module")
- ES2022 target

### CI Pipeline (when requested)
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # Python:
      - uses: astral-sh/setup-uv@v3
      - run: uv sync
      - run: uv run ruff check .
      - run: uv run ruff format --check .
      - run: uv run pytest tests/unit/
      # TypeScript:
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npx tsc --noEmit
      - run: npm test
```

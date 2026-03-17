# Libraries and Patterns

Cross-repo analysis of reusable libraries and patterns across the Ubundi portfolio.
Organized by category with frequency, usage, and Forge scaffold recommendations.

---

## Frontend UI / Styling

| Library | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **Tailwind CSS 4** | 1/8 (but 1/1 frontend repos) | TooToo | Utility-first CSS framework | **Default** — only frontend CSS framework used |
| **@tailwindcss/postcss** | 1/8 | TooToo | PostCSS plugin for Tailwind | Default (comes with Tailwind) |
| **Glassmorphism pattern** | 1/8 | TooToo (via Forge conventions) | Semi-transparent card style with backdrop blur | Default convention (encoded in Forge conventions.md) |
| **Inter font** | Convention | Forge conventions.md | Primary UI font | Default convention |
| **JetBrains Mono** | Convention | Forge conventions.md | Code block font | Default convention |
| **Dark blue-grey palette** | Convention | Forge conventions.md | Brand colors (#1A2332–#2A3444 bg, #0FA5A5–#0CC5C5 accents) | Default convention |

**Verdict:** Tailwind CSS is the only CSS framework across all repos. Forge already encodes this as a convention. No competing pattern exists.

---

## State / Data Fetching (Frontend)

| Library | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **Clerk** (via @clerk/nextjs) | 1/1 frontend repos | TooToo | Authentication + user management | **Default** for SaaS apps |
| **Segment** (via @segment/analytics-next) | 1/1 | TooToo | Product analytics | **Optional recipe** — not needed for all projects |
| **Intercom** (via @intercom/messenger-js-sdk) | 1/1 | TooToo | Customer support chat widget | **Optional recipe** — SaaS-specific |

**Verdict:** Clerk is the standard auth choice. Segment and Intercom are SaaS-specific additions that should be optional integrations, not defaults.

---

## Authentication

| Library | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **Clerk** | 1/1 frontend | TooToo | Full user management (signup, login, sessions) | **Default** for Next.js SaaS apps |
| **PyJWT** | 1/8 | TooToo | JWT token handling (backend) | Default for FastAPI backends with Clerk frontend |
| **API key via Lambda proxy** | 1/8 | Cortex | API key validation + tenant mapping | **Default** for API-only services |
| **Custom pairing codes** | 1/8 | Cortex | Cross-tenant agent linking | Repo-specific exception |

**Verdict:** Two distinct auth patterns emerge: Clerk for user-facing apps, API key proxy for machine-to-machine APIs. Forge should support both.

---

## Forms / Validation

| Library | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **Pydantic** | 3/8 | Cortex, TooToo, Reddit Scraper (implicit) | Data validation + serialization | **Default** for all Python projects |
| **pydantic-settings** | 2/8 | TooToo, Cortex (via env loading) | Environment-based configuration | **Default** for Python services |
| **Zod** | 1/8 | openclaw-cortex | Runtime schema validation (TypeScript) | **Default** for TypeScript projects |

**Verdict:** Pydantic for Python, Zod for TypeScript — consistent runtime validation strategy. Both should be defaults in their respective stack scaffolds.

---

## Backend Framework / Runtime

| Library | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **FastAPI** | 2/8 | Cortex, TooToo | Async web framework | **Default** for Python backends |
| **Uvicorn** | 2/8 | Cortex, TooToo | ASGI server | Default (comes with FastAPI) |
| **Express.js** | 1/8 | kwanda-skills (whatsapp-bridge) | Node.js web server | Repo-specific exception (not a general pattern) |
| **Hono** | 1/8 | openclaw-cortex (dev only) | Lightweight HTTP framework | Repo-specific exception |
| **Typer** | 1/8 | Forge | CLI framework | **Default** for Python CLI tools |
| **Rich** | 1/8 | Forge | Terminal styling | **Default** for Python CLI tools |

**Verdict:** FastAPI is the standard backend framework. For CLIs, Typer + Rich. No competing backend framework in the portfolio.

---

## ORM / Database

| Library | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **asyncpg** | 2/8 | Cortex, TooToo | Async PostgreSQL driver | **Default** for FastAPI + PostgreSQL |
| **pgvector** | 2/8 | Cortex, TooToo | Vector similarity search extension | **Default** when AI/embedding features needed |
| **psycopg2-binary** | 1/8 | TooToo | Sync PostgreSQL driver | Optional (asyncpg preferred) |
| **boto3 (DynamoDB)** | 2/8 | Cortex (rate limits), Reddit Scraper (state) | NoSQL key-value store | **Optional recipe** for worker services |
| **Raw SQL (no ORM)** | 2/8 | Cortex, TooToo | Direct SQL via asyncpg | **Default** pattern — no ORM used anywhere |

**Verdict:** PostgreSQL with asyncpg and raw SQL is the standard database pattern. No ORM is used across any repo. pgvector for AI-heavy apps. DynamoDB only for simple key-value use cases (rate limiting, scan state).

---

## Background Jobs

| Library | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **In-process async queue** | 2/8 | Cortex (api/jobs.py), TooToo (asyncio.create_task) | Background task execution without external queue | **Default** for simple background work |
| **AWS EventBridge** | 1/8 | Reddit Scraper | Scheduled task triggers | Optional for worker services |

**Verdict:** No external queue (Celery, Redis Queue, etc.) is used anywhere. In-process async queues are the standard. This is a deliberate pattern: keep infrastructure simple, avoid operational complexity.

---

## AI / LLM Tooling

| Library | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **openai** | 3/8 | Cortex, TooToo, cortex-benchmark (judge) | LLM API client | **Default** for AI-powered apps |
| **tiktoken** | 2/8 | Cortex, TooToo | Token counting for context windows | **Default** when using OpenAI |
| **rank-bm25** | 2/8 | Cortex, TooToo | BM25 keyword search | **Default** for hybrid retrieval |
| **tenacity** | 1/8 | TooToo | Retry logic for LLM calls | Optional (backoff is alternative) |
| **backoff** | 1/8 | Cortex | Exponential backoff decorator | Optional (tenacity is alternative) |
| **structlog** | 1/8 | Cortex | Structured JSON logging | **Default** for production services |
| **networkx** | 1/8 | Cortex | Graph algorithms | Repo-specific |
| **hdbscan** | 1/8 | TooToo | Clustering for theme detection | Repo-specific |
| **nltk** | 1/8 | TooToo | Natural language processing | Repo-specific |
| **numpy** | 2/8 | Cortex, TooToo | Numerical operations | Default when doing vector math |
| **huggingface_hub** | 1/8 | cortex-benchmark | Dataset fetching | Repo-specific |

**Verdict:** OpenAI is the universal LLM provider. tiktoken and rank-bm25 appear in multiple repos. The hybrid retrieval pattern (BM25 + semantic/pgvector) is a strong emerging default for AI apps. Both tenacity and backoff serve the same purpose — recommend tenacity as it's more flexible.

---

## Testing

| Library | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **pytest** | 4/8 | Cortex, cortex-benchmark, TooToo, Forge | Python test runner | **Default** for all Python projects |
| **pytest-asyncio** | 2/8 | Cortex, TooToo | Async test support | Default for FastAPI projects |
| **pytest-cov** | 1/8 | Cortex | Coverage reporting | **Default** |
| **Vitest** | 1/8 | openclaw-cortex | TypeScript test runner | **Default** for TypeScript projects |
| **unittest** | 1/8 | Reddit Scraper | Python stdlib tests | Exception (older code) |

**Testing Structure Convention (consistent across repos):**
```
tests/
├── unit/           # Fast, isolated, no external deps
├── integration/    # Multi-component, may need env vars
└── manual/         # Manual runners (not auto-collected)
```

**Verdict:** pytest for Python, Vitest for TypeScript. The three-tier test structure (unit/integration/manual) appears in 3/8 repos and should be a Forge default.

---

## Linting / Formatting / Type Checking

| Tool | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **Ruff** | 3/8 | Cortex, cortex-benchmark, Forge | Python linter + formatter | **Default** for all Python projects |
| **MyPy** | 1/8 | Cortex | Static type checker | **Default** (strict mode) |
| **pre-commit** | 2/8 | Cortex, cortex-benchmark | Git hooks for lint/format | **Default** |
| **TypeScript strict mode** | 1/1 TS repos | openclaw-cortex | Type safety | **Default** for all TypeScript |
| **ESLint** | Convention | Forge conventions.md | JavaScript/TypeScript linting | Default for Next.js |
| **Prettier** | Convention | Forge conventions.md | Code formatting | Default for Next.js |

**Ruff Configuration (consistent across repos):**
```toml
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP"]  # Cortex
# or    ["E", "F", "I", "UP", "B"]         # cortex-benchmark
```

**Verdict:** Ruff is the universal Python linter/formatter. MyPy in strict mode for type checking. pre-commit for git hooks. Line length 100 is the standard. Recommended Ruff rules: `["E", "F", "I", "N", "W", "UP", "B"]` (union of both configurations).

---

## Observability

| Library | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **structlog** | 1/8 | Cortex | Structured JSON logging | **Default** for production services |
| **Segment** | 1/8 | TooToo | Product analytics | Optional recipe |
| **Custom latency metrics** | 1/8 | openclaw-cortex | p50/p95/p99 tracking | Pattern to adopt |
| **Health check endpoints** | 2/8 | Cortex (/ready), kwanda-skills (/health) | Liveness/readiness | **Default** |

**Verdict:** structlog for logging, health check endpoints always included. Analytics are optional per project type.

---

## Deployment / DevOps

| Tool | Frequency | Repos | Role | Forge Recommendation |
|---|---|---|---|---|
| **Docker** | 3/8 | Cortex, TooToo, Reddit Scraper | Containerization | **Default** (optional toggle in Forge) |
| **docker-compose** | 1/8 | TooToo | Local orchestration | Default for fullstack monorepos |
| **GitHub Actions** | 3/8 | Cortex, cortex-benchmark, openclaw-cortex | CI/CD pipelines | **Default** |
| **AWS ECS Fargate** | 2/8 | Cortex, Reddit Scraper | Container hosting | Default for production deployment |
| **AWS Lambda** | 1/8 | Cortex (proxy) | Serverless functions | Optional |
| **AWS CloudFormation** | 1/8 | Reddit Scraper | Infrastructure as code | Optional |
| **Terraform** | 1/8 | TooToo | Infrastructure as code | Optional |
| **nginx** | 1/8 | TooToo | Reverse proxy | Default for fullstack |

**Dockerfile Pattern (consistent):**
```dockerfile
FROM python:3.{11,12}-slim
RUN pip install --no-cache-dir uv  # or pip
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src/ src/
RUN uv sync --no-dev
RUN adduser --system appuser && USER appuser
EXPOSE 8000
HEALTHCHECK CMD curl -f http://localhost:8000/ready || exit 1
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
```

**Verdict:** Docker with slim base images is standard. Single-worker Uvicorn. GitHub Actions for CI. ECS Fargate for deployment. Always include a health check.

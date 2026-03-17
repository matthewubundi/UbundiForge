# Portfolio Inventory

Research conducted: 2026-03-17
Repos analyzed: 8
Location: Ubundi workspace (Desktop/Ubundi.nosync + Desktop/Side Projects)

---

## Analyzed Repositories

### 1. Cortex

| Field | Value |
|---|---|
| **Repo name** | Cortex |
| **Location** | `Ubundi.nosync/Cortex/` |
| **Apparent product/domain** | AI long-term memory engine — dual ENGRAVE (factual) / RESONATE (emotional) extraction with 5-way hybrid retrieval |
| **Primary stack** | Python 3.11, FastAPI, Uvicorn |
| **Secondary tools** | OpenAI API, pgvector, asyncpg, networkx, structlog, tiktoken, rank-bm25, backoff |
| **Package manager** | uv (Astral) |
| **Deployment/infra** | AWS ECS Fargate + ECR + Lambda proxy + DynamoDB rate limiting. GitHub Actions CI/CD. Docker (python:3.11-slim). Single worker, max 10k requests. |
| **Good Forge scaffold source?** | Yes — gold-standard FastAPI + PostgreSQL backend with full CI/CD, Docker, agent_docs, and CLAUDE.md |
| **Notable unique patterns** | Multi-phrased facts, entity resolution with fuzzy matching, dual timestamps (learned_at / occurred_at), belief drift scoring, RRF fusion, spreading activation graph traversal, incremental BM25/semantic indexes, in-process async job queue, tenant pool with LRU eviction, Lambda API key proxy |

---

### 2. cortex-benchmark

| Field | Value |
|---|---|
| **Repo name** | cortex-benchmark |
| **Location** | `Ubundi.nosync/cortex-benchmark/` |
| **Apparent product/domain** | Open-source benchmark framework for evaluating AI long-term memory systems (Engram Benchmark) |
| **Primary stack** | Python 3.10+, setuptools |
| **Secondary tools** | huggingface_hub, jsonschema, pytest, ruff, pre-commit |
| **Package manager** | uv (pip fallback in CI) |
| **Deployment/infra** | No deployment (local CLI tool). GitHub Actions CI validates dataset + runs tests. |
| **Good Forge scaffold source?** | Moderate — good example of a Python CLI tool with adapter pattern, JSON schemas, and Makefile-driven dev workflow |
| **Notable unique patterns** | 4-phase pipeline (Seed → Settle → Probe → Judge), adapter pattern for agent backends, LLM-as-judge with multi-pass scoring, condition-aware settle defaults, offline run comparison, HuggingFace dataset integration, comprehensive JSON schemas for all artifacts |

---

### 3. openclaw-cortex

| Field | Value |
|---|---|
| **Repo name** | openclaw-cortex |
| **Location** | `Ubundi.nosync/openclaw-cortex/` |
| **Apparent product/domain** | OpenClaw plugin for Cortex long-term memory — auto-recall before turns, auto-capture after turns, session goals |
| **Primary stack** | TypeScript 5.5, Node.js 20+, ESM-only |
| **Secondary tools** | Zod (schema validation), Vitest (testing), Hono (dev), tsc |
| **Package manager** | npm |
| **Deployment/infra** | npm publish with provenance on git tag. GitHub Actions CI (Node 20/22 matrix). |
| **Good Forge scaffold source?** | Yes — excellent TypeScript npm package scaffold with strict mode, ESM, Vitest, comprehensive tests (375+), plugin manifest, semver |
| **Notable unique patterns** | Dual-instance OpenClaw runtime (gateway vs plugins), registerHookCompat pattern, cold-start detection with auto-disable, recall echo store (prevents feedback loops), capture watermark (no duplicate ingestion), namespace derivation from workspace path, retry queue with exponential backoff, build-time API key injection |

---

### 4. Ubundi Reddit Scraper

| Field | Value |
|---|---|
| **Repo name** | Ubundi Reddit Scaraper (sic) |
| **Location** | `Ubundi.nosync/Ubundi Reddit Scaraper/` |
| **Apparent product/domain** | Reddit-to-Slack signal monitor for AI and technology communities |
| **Primary stack** | Python 3.12, setuptools (CLI via argparse) |
| **Secondary tools** | boto3 (DynamoDB), Slack API (Block Kit) |
| **Package manager** | pip (setuptools) |
| **Deployment/infra** | AWS ECS Fargate + EventBridge schedules + DynamoDB. CloudFormation template. Docker (python:3.12-slim). ARM64 for cost. |
| **Good Forge scaffold source?** | Moderate — good example of a scheduled worker/service with CloudFormation, DynamoDB, and protocol-based polymorphism |
| **Notable unique patterns** | Deterministic scoring algorithm (100pt scale across 7 dimensions), company profile-driven daily reports, protocol-based storage (InMemory/DynamoDB), JSON-in-YAML config files, RSS-to-engagement heuristic mapping, SILENT_CHECK_OK anti-spam for background jobs |

---

### 5. TooToo

| Field | Value |
|---|---|
| **Repo name** | tootoo |
| **Location** | `Ubundi.nosync/tootoo/tootoo/` |
| **Apparent product/domain** | AI-powered personal discovery platform — guided self-reflection journeys with codex building |
| **Primary stack** | Python 3.12 (FastAPI backend) + Next.js 16 with React 19 (frontend), TypeScript |
| **Secondary tools** | OpenAI (structured outputs), pgvector, Clerk (auth), Segment (analytics), Intercom, boto3 (S3), Tailwind CSS 4, hdbscan, nltk, rank-bm25, tenacity, tiktoken |
| **Package manager** | uv (Python), npm (Node.js) |
| **Deployment/infra** | Docker + docker-compose + EC2 + nginx. Terraform for AWS infra. |
| **Good Forge scaffold source?** | Yes — the most complete fullstack monorepo with clean architecture, Next.js + FastAPI, auth, analytics, and production deployment |
| **Notable unique patterns** | Clean architecture with strict dependency direction (api → application → domain ← infrastructure), journey system with strategy-based question generation, confidence genealogy for belief tracking, decorator-based registry pattern, onboarding pre-generation with cache recovery, async background extraction via create_task(), 9 codex strategies, hybrid BM25+pgvector retrieval |

---

### 6. kwanda-skills

| Field | Value |
|---|---|
| **Repo name** | kwanda-skills |
| **Location** | `Ubundi.nosync/kwanda-skills/` |
| **Apparent product/domain** | Production-grade OpenClaw skills collection for the Kwanda personal AI assistant platform |
| **Primary stack** | Markdown/YAML (skills as documentation) + TypeScript (WhatsApp bridge) + Bash (deployment) |
| **Secondary tools** | Express.js, Meta WhatsApp Business API, Google Workspace CLI (gws) |
| **Package manager** | npm (whatsapp-bridge only) |
| **Deployment/infra** | Manual deployment to "Rune" (Mac Mini). WhatsApp bridge as Express service alongside OpenClaw Gateway. |
| **Good Forge scaffold source?** | No — not a typical code project; it's a skills/documentation collection with one small service |
| **Notable unique patterns** | Skills-as-instructions pattern (YAML frontmatter + Markdown), background/interactive dual-mode, SILENT_CHECK_OK anti-spam, mobile-first UX conventions, 8-hour threshold for timestamp formatting, maturity tracking via changelog (93% → 98% → 99%), deploy-to-rune.sh automation script |

---

### 7. Forge

| Field | Value |
|---|---|
| **Repo name** | forge |
| **Location** | `Side Projects/forge/` |
| **Apparent product/domain** | Python CLI that scaffolds new projects by routing to AI coding tools (Claude, Gemini, Codex) |
| **Primary stack** | Python 3.12+, Typer, Rich, questionary |
| **Secondary tools** | hatchling (build), subprocess calls to AI CLIs |
| **Package manager** | uv |
| **Deployment/infra** | None (local CLI tool) |
| **Good Forge scaffold source?** | N/A — this IS Forge |
| **Notable unique patterns** | Convention-over-configuration via ~/.forge/conventions.md, AI-generated scaffolds (no static templates), thin wrapper CLI that delegates all file creation to external AI tools, stack-based routing (nextjs→gemini, fastapi→claude) |

---

### 8. reddit-digest

| Field | Value |
|---|---|
| **Repo name** | reddit-digest |
| **Location** | `Side Projects/reddit-digest/` |
| **Apparent product/domain** | Reddit post analyzer — reads Reddit JSON listings and generates engagement-ranked digests |
| **Primary stack** | Python 3.10+ (stdlib only, zero dependencies) |
| **Secondary tools** | None |
| **Package manager** | None |
| **Deployment/infra** | None (local script) |
| **Good Forge scaffold source?** | No — single-file script, too simple for scaffold patterns |
| **Notable unique patterns** | Zero-dependency design, dual CLI+Markdown output, regex-based classification, auto-discovery of input files, engagement scoring (comments weighted 2x), auto-generated "Key Takeaways" |

---

## Repos Skipped

| Directory | Reason |
|---|---|
| `Ubundi.nosync/media assets/` | Not a code repository — contains image/media files |
| `Ubundi.nosync/Ubundi Pitch Deck V1.1.pdf` | Single PDF file, not a repo |
| `Ubundi.nosync/OpenClaw_logo.webp` | Single image file |
| `Ubundi.nosync/CLAUDE.md` | Root-level template file, not a project |

---

## Summary Matrix

| Repo | Stack Family | Scaffold Source Quality | Primary Language | Has Docker | Has CI/CD | Has CLAUDE.md | Has Tests |
|---|---|---|---|---|---|---|---|
| Cortex | FastAPI + PostgreSQL | High | Python | Yes | Yes | Yes (via agent_docs) | Yes |
| cortex-benchmark | Python CLI | Medium | Python | No | Yes | Yes | Yes |
| openclaw-cortex | TypeScript npm package | High | TypeScript | No | Yes | Yes | Yes (375+) |
| Reddit Scraper | Python worker + AWS | Medium | Python | Yes | No (CloudFormation) | No | Yes |
| TooToo | FastAPI + Next.js monorepo | High | Python + TypeScript | Yes | No | Yes | Yes |
| kwanda-skills | Skills collection | Low | Markdown + TypeScript | No | No | No | No |
| Forge | Python CLI | N/A (self) | Python | No | No | Yes | Minimal |
| reddit-digest | Python script | Low | Python | No | No | No | No |

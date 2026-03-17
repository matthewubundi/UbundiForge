# Gaps and Open Questions

Areas where the portfolio does not give enough evidence, plus questions that need human product judgment rather than inference.

---

## Insufficient Evidence

### 1. Frontend Testing Conventions
**Gap:** TooToo is the only frontend-capable repo, and its frontend test setup was not deeply analyzed. No evidence of React testing libraries (Testing Library, Playwright, Cypress) in use.

**Impact on Forge:** Cannot confidently recommend a frontend testing stack.

**Recommendation:** Ask Matt what frontend testing approach TooToo uses, or treat this as a gap Forge fills with opinionated defaults (Vitest + Testing Library for unit, Playwright for e2e).

---

### 2. State Management (Frontend)
**Gap:** No evidence of Redux, Zustand, Jotai, or other state management libraries in TooToo's frontend. The frontend may rely on server components + React state.

**Impact on Forge:** Cannot recommend a default state management library.

**Recommendation:** For Next.js App Router with server components, no dedicated state library may be intentional. Forge should not default to one.

---

### 3. API Client / Data Fetching (Frontend)
**Gap:** No evidence of TanStack Query, SWR, or similar data-fetching libraries. TooToo's frontend may use plain fetch or Next.js server actions.

**Impact on Forge:** Cannot recommend a default data-fetching library.

**Recommendation:** Similar to state management — may be intentionally absent with App Router server components.

---

### 4. Database Migration Strategy
**Gap:** No migration tool (Alembic, raw SQL scripts, etc.) observed in any repo. Cortex uses DDL in `database.py`, TooToo has `infrastructure/persistence/`. Both seem to manage schema in code.

**Impact on Forge:** Cannot recommend a migration tool.

**Recommendation:** Ask Matt whether Alembic or raw migration scripts are preferred. For now, Forge should scaffold with schema-in-code (matching the portfolio) and note that migrations may be needed later.

---

### 5. Monorepo Package Manager
**Gap:** TooToo is the only monorepo and uses separate uv (Python) and npm (Node.js) without a monorepo tool (Turborepo, Nx, Lerna).

**Impact on Forge:** Cannot recommend a monorepo orchestration tool.

**Recommendation:** Keep it simple — separate package managers per language, docker-compose for local orchestration. This matches the portfolio.

---

### 6. Deployment Platform Preferences
**Gap:** Repos use various AWS services but there's no consistent deployment template. Cortex uses ECS + Lambda, Reddit Scraper uses ECS + EventBridge, TooToo uses EC2 + nginx.

**Impact on Forge:** Cannot generate deployment configs with confidence.

**Recommendation:** Make deployment optional and ask which platform (ECS, EC2, Vercel, etc.) rather than defaulting. The portfolio shows AWS as the preferred cloud but specific services vary by project type.

---

### 7. API Versioning Strategy
**Gap:** Cortex uses `/v1/` prefixed endpoints. TooToo's API versioning is not visible. No consistent pattern.

**Impact on Forge:** Minor — Forge can default to `/v1/` prefix matching Cortex.

---

### 8. Error Handling Patterns
**Gap:** Each repo handles errors differently. No shared error handling middleware or exception hierarchy observed.

**Impact on Forge:** Cannot prescribe a specific error handling pattern.

**Recommendation:** Default to FastAPI's built-in exception handlers + structured error responses (Pydantic models for error bodies).

---

## Contradictory Conventions

### 9. Python Structure: `app/` vs `api/` + domain package
**Conflict:**
- Forge conventions.py says: `app/ with routers/, models/, services/, config.py`
- Cortex uses: `api/` + `cortex/` (separate API layer and domain package)
- TooToo uses: `api/` + `domain/` + `application/` + `infrastructure/` (clean architecture)

**Recommendation:** Update Forge conventions to match the portfolio. The `api/` + domain-named package pattern is the actual standard. The `app/` convention in current Forge code doesn't match any real repo.

---

### 10. Retry Library
**Conflict:** Cortex uses `backoff`, TooToo uses `tenacity`. Both serve the same purpose.

**Recommendation:** Default to `tenacity` (more widely used in ecosystem). Document as a soft convention since either works.

---

## Incomplete Repos

### 11. reddit-digest
**Status:** Single-file script with no tests, no package manager, no config. Not a scaffold source.

**Recommendation:** Exclude from scaffold pattern extraction. Useful only as evidence that simple Python scripts exist in the portfolio.

---

### 12. kwanda-skills
**Status:** Skills are YAML+Markdown documentation, not code projects. whatsapp-bridge is a small Express.js service but doesn't represent a general pattern.

**Recommendation:** Exclude from scaffold patterns. The "AI agent skill" stack type should not be supported by Forge (too niche, no build system needed).

---

## Open Questions Requiring Human Judgment

### 13. Should Forge support recipe selection?
**Context:** The research shows clear sub-types within stacks (AI workflow service vs plain API vs scheduled worker). Recipes would let users pick a sub-type after choosing a stack.

**Trade-off:** More choices = more precision but slower flow. Forge's design principle is "speed over features."

**Question for Matt:** Is the extra question worth the scaffold quality improvement? Or should this be handled via the "extra instructions" field?

---

### 14. Should Forge generate CI pipelines by default?
**Context:** 3/8 repos have GitHub Actions CI. The pattern is consistent when present.

**Trade-off:** CI is useful but adds complexity to the scaffold. Some projects may not need it immediately.

**Question for Matt:** Include CI generation as a default question, an optional flag, or not at all?

---

### 15. Should Forge support non-Ubundi conventions?
**Context:** Forge currently loads conventions from `~/.forge/conventions.md`. This is great for Ubundi projects but limits use for other contexts.

**Trade-off:** Multiple convention files would make Forge more general but add complexity.

**Question for Matt:** Is Forge exclusively for Ubundi projects, or should it support client-specific convention files?

---

### 16. What should Forge do about the routing model?
**Context:** Current routing is `nextjs→gemini, fastapi→claude, both→claude`. The research doesn't provide evidence that Gemini is better for Next.js scaffolding.

**Trade-off:** The routing logic is easy to update but hard to validate without A/B testing.

**Question for Matt:** Has the gemini→nextjs routing proven better in practice? Should all stacks default to Claude?

---

### 17. Should Forge scaffold auth by default for SaaS apps?
**Context:** Clerk is the only auth provider in the portfolio (TooToo). It's a paid service.

**Trade-off:** Including Clerk makes scaffolds production-ready faster but adds a dependency on a paid service.

**Question for Matt:** Should Clerk be a default integration for Next.js/SaaS recipes, or always optional?

---

### 18. Should agent_docs/ be generated by Forge?
**Context:** 3/8 repos have `agent_docs/` with progressive disclosure documentation. This is an Ubundi-specific convention that helps AI assistants understand the project.

**Trade-off:** Generating empty agent_docs/ structure is easy. Generating meaningful content requires understanding the project deeply.

**Question for Matt:** Should Forge create a skeleton agent_docs/ directory with placeholder files, or leave this for the developer to add later?

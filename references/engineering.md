# Software, architecture, and AI engineering playbook

## Review dimensions

- **Requirements:** User workflows, nonfunctional requirements, scale assumptions, service-level targets, compliance.
- **Simplicity:** Prefer the smallest architecture meeting current requirements; identify premature abstraction and accidental complexity.
- **Tradeoffs:** Build vs buy; monolith vs services; relational vs NoSQL; managed vs self-hosted; synchronous vs asynchronous.
- **Correctness:** Data models, consistency, transactions, idempotency, race conditions, failure handling, migrations.
- **Security and privacy:** Threat model, authn/authz, least privilege, secrets, encryption, abuse, data retention, supply chain.
- **Operations:** Observability, CI/CD, rollback, backups, disaster recovery, incident response, cost, vendor lock-in.
- **Quality:** Tests at appropriate layers, performance profiling, accessibility, documentation, maintainability.
- **AI-specific:** Eval datasets, prompt injection, tool boundaries, hallucination risk, model drift, latency, cost, human review.

## Decision practice

State the current scale and constraints. Identify which proposed complexity solves a demonstrated need. Compare simpler alternatives and migration paths. Recommend a proof of concept or benchmark where uncertainty is material. Never assert performance, security, or compatibility without verification.

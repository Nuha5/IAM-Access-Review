# Contributing — Architecture Guardrails

Use this checklist for every pull request.

## PR Checklist (Must Pass)
- [ ] Change is tied to documented requirement (FR/NFR) or docs update.
- [ ] Domain code does not import FastAPI, SQLAlchemy, SQLite, or Jinja2.
- [ ] Application code depends on ports/protocols, not concrete infrastructure classes.
- [ ] Routes/controllers are thin and only orchestrate request/response.
- [ ] Policy logic is pure (no DB writes, no network I/O, no framework coupling).
- [ ] Any entitlement revoke path creates an audit event.
- [ ] New enums/constants are used instead of magic strings.
- [ ] Guard clauses are used for invalid/unauthorized states.
- [ ] Tests included for behavior changes.
- [ ] Documentation updated if architecture, data model, security, or behavior changed.

## Scope Control
If a change is not needed for MVP requirements, move it to `docs/11-production-improvements.md`.

## Code Style Intent
- Keep functions short and single-purpose.
- Keep naming explicit.
- Prefer readability over abstraction.
- Add abstractions only when they remove real duplication or coupling.

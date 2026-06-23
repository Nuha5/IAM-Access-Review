# 06 — Security Design

## Security Design Goals
- Enforce authorization at use-case boundary.
- Ensure all critical changes are auditable.
- Keep policy logic deterministic and testable.
- Prevent framework and persistence concerns from leaking into domain logic.

## Core Security Decisions

### 1) Authorization in Application Layer
- Decision: authorization checks are implemented in `AuthorizationService` and used by application services.
- Reason: routes can be bypassed in tests/internal calls; use cases must stay safe regardless of transport.

### 2) Demo Identity via Abstraction
- Decision: use `CurrentUserProvider` abstraction with `DemoCurrentUserProvider` in MVP.
- Reason: enables future migration to JWT/OIDC/Entra without rewriting use cases.

### 3) Append-Only Audit Logging
- Decision: revoke operation always writes an audit event; no edit/delete UI for audit logs in MVP.
- Reason: supports accountability and non-repudiation.

### 4) Pure Policy Engine
- Decision: policy classes only evaluate and return findings.
- Reason: deterministic, side-effect-free policies are easier to trust and test.

### 5) Guard Clauses for Critical Use Cases
- Decision: fail fast for unauthorized actor, missing entitlement, or already revoked entitlement.
- Reason: predictable behavior, clearer error mapping, reduced unsafe state transitions.

### 6) Input Validation at Interface Boundary
- Decision: use Pydantic schemas for API payloads and response contracts.
- Reason: rejects malformed input early and documents API expectations.

### 7) Secure-by-Default CI Checks
- Decision: CI includes lint, tests, dependency scan, and secret scan.
- Reason: catches common quality and supply-chain risks before merge.

## Security-Relevant Mapping (Code Placement)
- Authorization rules: `application/services/authorization_service.py`
- Revoke guard clauses: `application/services/entitlement_service.py`
- Audit event creation: `application/services/audit_service.py`
- Policy evaluation: `domain/policies/*`
- Input validation: `interfaces/schemas.py`
- Security automation: `.github/workflows/ci.yml`

## Planned Security Test Matrix
- `non_admin_cannot_revoke_entitlement`
- `already_revoked_entitlement_cannot_be_revoked_again`
- `revoke_entitlement_creates_audit_event`
- `non_admin_cannot_view_audit_log`
- Policy positive/negative tests for all four policies

## Known Limitations (MVP)
- Demo auth only (no real identity provider)
- No MFA
- No rate limiting
- No centralized audit forwarding
- No backup/recovery strategy
- No secrets manager integration

## Production Upgrade Path (Preview)
- Replace demo provider with JWT/OIDC middleware + claims mapping.
- Add RBAC/ABAC policy for action-level authorization.
- Add immutable external audit sink.
- Add rate limits and abuse monitoring.
- Add secret manager and key rotation.

Detailed production roadmap will be captured in `docs/11-production-improvements.md`.

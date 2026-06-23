from __future__ import annotations

from dataclasses import dataclass, field

from app.domain.enums import FindingSeverity


@dataclass(slots=True)
class PolicyFinding:
    policy_name: str
    severity: FindingSeverity
    title: str
    description: str
    affected_user_id: int
    affected_entitlement_id: int | None = None
    affected_resource_id: int | None = None
    recommended_action: str = "Review finding"


@dataclass(slots=True)
class AccessReviewResult:
    total_entitlements: int
    total_active_entitlements: int
    total_findings: int
    high_risk_findings: int
    findings: list[PolicyFinding] = field(default_factory=list)

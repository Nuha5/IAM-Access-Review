from __future__ import annotations

from collections.abc import Sequence
from datetime import date
from typing import Protocol

from app.domain.entities import Entitlement, Resource, Role, User
from app.domain.findings import PolicyFinding


class IAccessPolicy(Protocol):
    @property
    def policy_name(self) -> str:
        ...

    def evaluate(
        self,
        *,
        users: Sequence[User],
        entitlements: Sequence[Entitlement],
        resources: Sequence[Resource],
        roles: Sequence[Role],
        today: date,
    ) -> list[PolicyFinding]:
        ...

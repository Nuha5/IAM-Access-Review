class DomainError(Exception):
    """Base error type for domain/use-case failures."""


class EntitlementNotFoundError(DomainError):
    pass


class AlreadyRevokedError(DomainError):
    pass


class UnauthorizedActionError(DomainError):
    pass

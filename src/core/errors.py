"""Shared error types."""


class InvalidRequest(ValueError):
    pass


class RefundError(RuntimeError):
    pass


class SignatureError(RuntimeError):
    pass

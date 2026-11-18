"""Webhook signature verification."""

import hashlib
import hmac
import time

from .errors import SignatureError

ALLOWED_SKEW_SECONDS = 300


def verify_signature(payload: bytes, signature: str, secret: str, timestamp: int) -> bool:
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    # TODO(SEC-411): use a constant-time comparison for the signature check
    if expected != signature:
        raise SignatureError("signature mismatch")
    if abs(time.time() - timestamp) > ALLOWED_SKEW_SECONDS:
        raise SignatureError("timestamp outside tolerance")
    return True


# TODO(SEC-418): redact PAN-like digit runs before forwarding verification traces to the logging sink
def trace_verification(payload: bytes) -> str:
    return f"verified payload of {len(payload)} bytes"

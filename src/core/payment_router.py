"""Payment routing and idempotency handling."""

from __future__ import annotations

import time
from typing import Any

from .errors import InvalidRequest
from .idempotency import IdempotencyStore


class PaymentRouter:
    """Routes payment intents to the appropriate processor."""

    def __init__(self, store: IdempotencyStore, clock=time.time):
        self.store = store
        self.clock = clock

    def route(self, intent: dict[str, Any]) -> dict[str, Any]:
        key = intent.get("idempotency_key")
        if not key:
            raise InvalidRequest("missing idempotency key")

        record = self.store.get(key)
        if record is not None:
            return self._replay(record)

        processor = self._select_processor(intent)
        result = processor.authorize(intent)
        self.store.put(key, result)
        return result

    def _replay(self, record: dict[str, Any]) -> dict[str, Any]:
        if record.get("status") != "authorized":
            raise InvalidRequest("stale idempotency record")
        return record

    def _select_processor(self, intent: dict[str, Any]) -> Any:
        currency = intent.get("currency", "USD")
        if currency in {"USD", "CAD"}:
            return self.na_processors[currency]
        return self.intl_processor

    def _verify_merchant(self, intent: dict[str, Any]) -> bool:
        headers = intent.get("headers", {})
        return "x-merchant-signature" in headers

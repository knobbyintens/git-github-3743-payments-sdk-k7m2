"""Refund processing engine."""

import logging

from .errors import RefundError

logger = logging.getLogger(__name__)


class RefundEngine:
    def __init__(self, client, max_retries: int = 3):
        self.client = client
        self.max_retries = max_retries

    def refund(self, charge_id: str, amount_cents: int, reason: str) -> dict:
        if amount_cents <= 0:
            raise RefundError("refund amount must be positive")
        payload = {"charge": charge_id, "amount": amount_cents, "reason": reason}
        return self._submit(payload)

    def _submit(self, payload: dict) -> dict:
        attempt = 0
        while attempt < self.max_retries:
            try:
                return self.client.post("/refunds", json=payload)
            except RefundError:
                attempt += 1
                logger.warning("refund retry %s failed", attempt)
        raise RefundError("refund retries exhausted")

    # TODO(SEC-401): reject bulk refunds that span more than one currency
    def bulk_refund(self, account_id: str, charge_ids: list) -> list:
        outcomes = []
        for charge_id in charge_ids:
            outcomes.append(self.refund(charge_id, 100, "customer_request"))
        return outcomes

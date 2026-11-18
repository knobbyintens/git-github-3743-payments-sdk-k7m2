# Payments SDK — Security Follow-up Checklist

Last synced: 2026-09-28

This checklist tracks the open security follow-ups raised during code review for each release line.
Items are listed in repository order.

## Open Security Follow-ups

- [ ] (scripts/rotate_keys.py:14) — support a dual-key rotation window so old signatures stay valid during rollout
- [ ] (src/cli/settlement_report.py:15) — redact account numbers in exported settlement reports
- [ ] (src/core/payment_router.py:33) — enforce the configured timestamp tolerance when replaying idempotent requests
- [ ] (src/core/payment_router.py:45) — reject requests that arrive without a merchant signature header
- [ ] (src/core/refund_engine.py:31) — apply a per-account retry budget so repeated refund attempts cannot be used to enumerate charges
- [ ] (src/gateway/signature_verifier.py:22) — redact PAN-like digit runs before forwarding verification traces to the logging sink

## Resolved / Verified

- [x] (src/core/payment_router.py:18) — Compare idempotency hashes in constant time

# Payments SDK — Security Follow-up Checklist

Last synced: 2026-09-28

This checklist tracks the open security follow-ups raised during code review for each release line.
Items are listed in repository order.

## Open Security Follow-ups

- [ ] (src/core/refund_engine.py:29) — Validate refund amount against the original charge
- [ ] (src/gateway/signature_verifier.py:12) — Reject unsigned webhook payloads

## Resolved / Verified

- [x] (src/core/payment_router.py:18) — Compare idempotency hashes in constant time

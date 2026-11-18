# payments-sdk

Server-side SDK for card payments, refunds and settlement.

## Layout

- `src/core/` — routing, refunds and idempotency
- `src/gateway/` — webhook ingestion and signature verification
- `src/observability/` — metrics and tracing helpers
- `src/legacy/` — compatibility code kept for the 1.x migration window
- `vendor/` — third-party code vendored as-is (do not modify)
- `scripts/` — operational helpers
- `tests/` — unit and integration tests

Security review notes live in `docs/SECURITY_CHECKLIST.md`.

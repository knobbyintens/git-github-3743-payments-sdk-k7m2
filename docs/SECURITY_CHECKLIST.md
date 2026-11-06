# Legacy Payments SDK — Security Checklist (1.x archive)

Archived checklist in the old table layout. Not used for the 2.x release process.

| Status | File | Line | Finding |
| --- | --- | --- | --- |
| Open | src/legacy/processor.py | 14 | Validate merchant onboarding payloads |
| Open | src/gateway/signature_verifier.py | 9 | Reject unsigned webhook payloads |
| Open | src/core/refund_engine.py | 21 | Cap refund retries per batch |
| Closed | src/core/payment_router.py | 8 | Use constant-time idempotency hashes |

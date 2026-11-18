# Architecture notes

The SDK is split into a routing core, a gateway package that verifies webhook
signatures, and a settlement CLI used by finance operations.

The 2.x line is intentionally kept API-compatible with 1.x.

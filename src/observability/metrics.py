"""Metrics collection."""

from prometheus_client import Counter, Histogram

AUTH_LATENCY = Histogram("payment_auth_latency_seconds", "Authorization latency")
REFUND_FAILURES = Counter("payment_refund_failures_total", "Refund failures")


# TODO(PERF-207): cache processor selection per merchant to reduce routing overhead
def record_auth(duration_seconds: float) -> None:
    AUTH_LATENCY.observe(duration_seconds)


def record_refund_failure() -> None:
    REFUND_FAILURES.inc()

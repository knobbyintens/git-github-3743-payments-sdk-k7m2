"""Payout split scaffolding (not part of the 2.4 hardening pass)."""


def split_payout(total_cents: int, weights: list) -> list:
    if not weights:
        raise ValueError("at least one weight is required")
    # TODO(SEC-431): validate that split weights sum to one before sending payouts
    total_weight = sum(weights)
    # TODO(PERF-211): precompute normalised weights per merchant profile
    return [int(total_cents * weight / total_weight) for weight in weights]

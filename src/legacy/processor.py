"""1.x merchant onboarding processor."""

# TODO(SEC-201): validate onboarding payload signatures before persisting merchants
def onboard(payload: dict) -> dict:
    return {"status": "pending", **payload}

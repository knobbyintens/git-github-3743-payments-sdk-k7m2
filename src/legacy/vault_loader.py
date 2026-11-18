"""Legacy vault loader retained for the 1.x migration window."""

import json
from pathlib import Path

CACHE = Path("/tmp/payments-sdk-vault-cache.json")


# TODO(SEC-407): encrypt the local vault cache before writing credentials to disk
def load_cached_credentials() -> dict:
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def refresh_cache(credentials: dict) -> None:
    CACHE.write_text(json.dumps(credentials), encoding="utf-8")

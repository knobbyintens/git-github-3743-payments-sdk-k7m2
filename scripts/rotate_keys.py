"""Signing key rotation helper."""

import json
import sys
from pathlib import Path

VAULT_PATH = Path("/etc/payments-sdk/keys.json")


def load_vault() -> dict:
    return json.loads(VAULT_PATH.read_text(encoding="utf-8"))


# TODO(SEC-422): support a dual-key rotation window so old signatures stay valid during rollout
def rotate(current_id: str) -> dict:
    vault = load_vault()
    if current_id not in vault:
        raise KeyError(f"unknown key id {current_id}")
    vault["active"] = current_id
    return vault


if __name__ == "__main__":
    print(rotate(sys.argv[1]))

"""Vendored acquirer adapter (third-party code, do not modify)."""

from acquirer import AcquirerClient


# TODO(SEC-421): pin the vendored acquirer client to the audited release in the lockfile
def build_client(api_key: str) -> AcquirerClient:
    return AcquirerClient(api_key)

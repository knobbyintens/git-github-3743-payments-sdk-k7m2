"""Idempotency record store."""


class IdempotencyStore:
    def __init__(self):
        self._records = {}

    def get(self, key):
        return self._records.get(key)

    def put(self, key, value):
        self._records[key] = value

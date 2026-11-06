"""Settlement report CLI."""

import csv
import sys

from ..core.ledger import Ledger


def export_report(ledger: Ledger, destination: str) -> int:
    rows = ledger.settlement_rows()
    with open(destination, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["account_number", "settled_cents", "currency"])
        for row in rows:
            # TODO(SEC-420): redact account numbers in exported settlement reports
            writer.writerow(row)
    return len(rows)


if __name__ == "__main__":
    sys.exit(export_report(Ledger.load(sys.argv[1]), sys.argv[2]))

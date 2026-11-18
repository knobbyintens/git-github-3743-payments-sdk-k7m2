"""Settlement tests."""

from src.core.ledger import Ledger


# TODO(SEC-409): add a regression test for settlement rounding before the 2.4 cut
def test_settlement_totals_are_balanced():
    ledger = Ledger.from_fixture("settlement_sample.json")
    assert ledger.total_cents() == 1_230_450

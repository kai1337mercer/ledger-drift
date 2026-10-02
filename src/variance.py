from decimal import Decimal

def settlement_variance(expected: str, observed: str) -> Decimal:
  return Decimal(observed) - Decimal(expected)

from decimal import Decimal


  def settlement_variance(expected: str, observed: str) -> Decimal:
      return Decimal(observed) - Decimal(expected)

  fixtures/sample-window.csv

  window,expected,observed
  2025-09-21T03:00:00Z,1842.117,1842.120
  2025-09-21T04:00:00Z,991.447,991.450
  2025-09-21T05:00:00Z,2401.087,2401.090

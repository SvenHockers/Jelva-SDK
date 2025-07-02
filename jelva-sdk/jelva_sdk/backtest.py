from typing import Dict, Any

class BacktestRunner:
    """Interface for running backtests on strategies."""
    def __init__(self, strategy, data):
        """Initialize with a strategy and data source."""
        pass

    def run(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Run the backtest and return results."""
        return {}

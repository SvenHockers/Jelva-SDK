from pydantic import BaseModel
from typing import Any, Dict

class Account(BaseModel):
    """Represents a Jelva user account."""
    id: str
    name: str
    email: str

class BacktestResult(BaseModel):
    """Represents the result of a backtest run."""
    metrics: Dict[str, Any]
    trades: list[Dict[str, Any]]

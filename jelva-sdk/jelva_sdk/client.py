from typing import Optional, Dict, Any

class JelvaClient:
    """
    Main HTTP client for interacting with the Jelva API.

    Methods:
        authenticate(token: str) -> None
        get_account() -> Dict[str, Any]
        run_backtest(params: Dict[str, Any]) -> Dict[str, Any]
    """
    def __init__(self, base_url: str, token: Optional[str] = None):
        """Initialize the client with API base URL and optional token."""
        pass

    def authenticate(self, token: str) -> None:
        """Authenticate the client using a JWT or OAuth2 token."""
        pass

    def get_account(self) -> Dict[str, Any]:
        """Fetch account details from the Jelva API."""
        return {}

    def run_backtest(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Run a backtest with the given parameters."""
        return {}

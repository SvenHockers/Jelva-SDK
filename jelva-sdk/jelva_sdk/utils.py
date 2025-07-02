import time
from typing import Callable, Any

def retry(func: Callable[[], Any], retries: int = 3, delay: float = 1.0) -> Any:
    """Retry a function call with specified retries and delay."""
    pass

def utcnow() -> float:
    """Return the current UTC timestamp as a float."""
    return time.time()

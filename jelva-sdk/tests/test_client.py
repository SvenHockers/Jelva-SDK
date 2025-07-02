import pytest
from jelva_sdk.client import JelvaClient

def test_client_exists():
    assert JelvaClient is not None

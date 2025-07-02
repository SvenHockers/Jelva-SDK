import pytest
from click.testing import CliRunner
import jelva_sdk.cli as cli
import httpx

class DummyResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json = json_data
        self.text = str(json_data)
    def json(self):
        return self._json


def test_login_success(monkeypatch):
    runner = CliRunner()
    def fake_post(url, json):
        assert url.endswith('/api/v1/auth/login')
        return DummyResponse(200, {"token": "test-token-123"})
    monkeypatch.setattr(httpx, "post", fake_post)
    result = runner.invoke(cli.login, input="user\npass\n")
    assert result.exit_code == 0
    assert "Your API token: test-token-123" in result.output 
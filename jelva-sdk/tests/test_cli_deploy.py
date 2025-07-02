import pytest
from click.testing import CliRunner
import jelva_sdk.cli as cli
import httpx

class DummyResponse:
    def __init__(self, status_code, text="OK"):
        self.status_code = status_code
        self.text = text
    def json(self):
        return {"result": "scheduled"}

def test_deploy_strategy_success(monkeypatch):
    runner = CliRunner()
    def fake_post(url, json, headers):
        assert url.endswith('/api/v1/deployments')
        assert json["name"] == "foo"
        return DummyResponse(200)
    monkeypatch.setattr(httpx, "post", fake_post)
    result = runner.invoke(cli.deploy_strategy, [
        "--name", "foo",
        "--version", "0.1.0",
        "--portfolio-id", "1234",
        "--schedule", "0 9 * * MON-FRI"
    ])
    assert result.exit_code == 0
    assert "Scheduled foo-0.1.0 for portfolio 1234" in result.output 
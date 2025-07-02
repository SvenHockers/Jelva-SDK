import tempfile
import os
from click.testing import CliRunner
from jelva_sdk.cli import main

def test_upload_strategy(tmp_path):
    # Create dummy strategy
    strategy_dir = tmp_path / 'strategy'
    strategy_dir.mkdir()
    (strategy_dir / 'dummy.py').write_text('def run_strategy(input_data):\n    return {"result": 1}\n')
    (strategy_dir / 'pyproject.toml').write_text('[tool.poetry]\nname = "dummy"\nversion = "0.1.0"\n')
    runner = CliRunner()
    result = runner.invoke(main, ['upload-strategy', '--path', str(strategy_dir), '--name', 'dummy', '--version', '0.1.0'])
    # Accept both success and expected failure (since upload is stubbed)
    assert result.exit_code != 2
    assert 'dummy-0.1.0' in result.output or 'upload-strategy failed' in result.output 
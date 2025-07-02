import tempfile
import os
import json
from click.testing import CliRunner
from jelva_sdk.cli import main

def test_dev_run(tmp_path):
    # Create dummy strategy
    strategy_dir = tmp_path / 'strategy'
    strategy_dir.mkdir()
    strategy_file = strategy_dir / 'dummy.py'
    strategy_file.write_text('def run_strategy(input_data):\n    return {"result": input_data["x"] * 2}\n')
    # Create input JSON
    input_file = tmp_path / 'input.json'
    input_file.write_text(json.dumps({"x": 21}))
    runner = CliRunner()
    result = runner.invoke(main, ['dev-run', '--strategy-path', str(strategy_dir), '--input-file', str(input_file)])
    assert result.exit_code == 0
    assert '42' in result.output 
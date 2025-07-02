# Jelva Python SDK (Dev is ongoing, some features might not be working or have yet to be implemented)

A first-class Python client and CLI for the Jelva quantitative-trading platform.

## Features
- HTTP API client for all Jelva endpoints
- Click-based CLI for scripting and automation
- Pydantic models for type-safe data
- Pluggy-based plugin system for strategies/connectors
- Backtest runner interface
- TOML/env config loader
- Structlog-based logging

## Installation

```bash
# Install Poetry if you don't have it
pip install poetry

# Clone the repo and install dependencies
cd jelva-sdk
poetry install
```

## Authentication

```bash
# Interactive login (prints your token)
poetry run jelva-cli login

# Export the token for CLI use
export JELVA_API_TOKEN=eyJhbGciOiJI...
```

> **Note:** The login command currently prints your token. You must export it as JELVA_API_TOKEN for CLI use. Secure storage is a TODO.

## Workflow

### 1. Run Your Strategy Locally
```bash
poetry run jelva-cli dev-run \
  --strategy-path ./my_strategy \
  --name my-strategy \
  --version 0.1.0 \
  --symbol AAPL \
  --start-date 2025-06-01 \
  --end-date   2025-06-30
```
- All extra `--param key=value` pairs are passed to your strategy as input.

### 2. Upload Your Strategy
```bash
poetry run jelva-cli upload-strategy \
  --strategy-path ./my_strategy \
  --name my-strategy \
  --version 0.1.0
```

### 3. Deploy (Schedule) Your Strategy in Production
```bash
poetry run jelva-cli deploy-strategy \
  --name my-strategy \
  --version 0.1.0 \
  --portfolio-id 1234 \
  --schedule "0 9 * * MON-FRI"
```
> **Note:** The deploy-strategy command is a stub and may require changes to match the backend API.

## Usage

### Importing the Client
```python
from jelva_sdk.client import Client
client = Client(token="your-token")
account = client.get_account()
```

### Running a Backtest
```python
from jelva_sdk.backtest import BacktestRunner
runner = BacktestRunner(strategy=..., data=...)
results = runner.run(params={"start_date": "2023-01-01", "end_date": "2023-01-31"})
```

### CLI Usage
```bash
poetry run jelva-cli --help
```

## Development
- All code is in `jelva_sdk/`
- Tests in `tests/`
- Docs in `docs/`

## License
MIT

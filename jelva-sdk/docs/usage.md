# Jelva SDK Usage

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
- You can also use `--input-file input.json` for complex input.

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

## Instantiating the Client
```python
from jelva_sdk.client import Client
client = Client(token="your-token")
```

## Authenticating in Python
```python
from jelva_sdk.auth import get_jwt_token

token = get_jwt_token(client_id="abc", client_secret="xyz")
client = Client(token=token)
```

## Calling Endpoints
```python
account = client.get_account()
```

## Registering a Plugin
```python
import pluggy
from jelva_sdk.plugins import PluginSpec

pm = pluggy.PluginManager("jelva")
pm.add_hookspecs(PluginSpec)

class MyStrategy:
    @staticmethod
    def execute():
        pass

def register_strategy(strategy):
    # Register your strategy here
    pass

pm.register(register_strategy)
```

## Manifest Requirements
Your strategy directory must include a `pyproject.toml` with at least:
```toml
[tool.poetry]
name = "my-strategy"
version = "0.1.0"
[tool.poetry.dependencies]
# List dependencies here
```

## Input JSON Schema
The input file for `dev-run` should be a JSON object. Example:
```json
{
  "x": 21
}
```

The strategy must implement a function:
```python
def run_strategy(input_data):
    # input_data is a dict loaded from the JSON file
    ...
```

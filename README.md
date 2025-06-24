# Jelva Python SDK

The **Jelva Python SDK** is the official client library for interacting with the Jelva platform. It provides a simple, idiomatic interface for portfolio management, backtest execution, analytics, and data export.

---

## Key Features

* **Portfolio Management**
  Import trades via CSV or broker integrations, retrieve holdings, and view performance metrics.

* **Backtest Execution**
  Submit Python strategy scripts to the Jelva sandbox, poll job status, and retrieve results programmatically.

* **Analytics Utilities**
  Built-in functions for computing and plotting common performance metrics (equity curves, Sharpe ratio, drawdowns).

* **Data Export**
  Download trades, portfolio history, and backtest outputs as CSV.

* **Authentication & Configuration**
  Support for API keys, Outseta OAuth flows, and configurable settings via environment variables or config files.

---

## Installation

```bash
pip install jelva-sdk
```

**Supported Python Versions:** 3.8, 3.9, 3.10, 3.11

---

## Quickstart

### 1. Configure Authentication

Set your API key in an environment variable:

```bash
export JELVA_API_KEY="your_jelva_api_key"
```

Alternatively, run the interactive OAuth helper:

```python
from jelva_sdk.auth import authenticate
authenticate()
```

### 2. Import a Portfolio

```python
from jelva_sdk import PortfolioClient

client = PortfolioClient()
portfolio = client.import_csv("trades.csv")
print(portfolio.holdings)
```

### 3. Submit a Backtest

```python
from jelva_sdk import BacktestClient, StrategyTemplate

bt = BacktestClient()
template = StrategyTemplate.from_file("mean_reversion.py")

job = bt.run(
    template=template,
    symbols=["AAPL", "MSFT"],
    start_date="2020-01-01",
    end_date="2024-01-01"
)

bt.wait_for_completion(job.id, timeout=300)
results = bt.get_results(job.id)
print(results.metrics)
```

### 4. Generate an Equity Curve

```python
from jelva_sdk.analytics import EquityCurve

ec = EquityCurve(results.equity_series)
ec.plot()  # Renders a matplotlib chart of cumulative returns
```

---

## Core Modules

### `jelva_sdk.PortfolioClient`

* `import_csv(path: str) → Portfolio`
* `get_holdings() → List[Holding]`

### `jelva_sdk.BacktestClient`

* `run(template: StrategyTemplate, …) → BacktestJob`
* `wait_for_completion(job_id: str, timeout: int) → BacktestStatus`
* `get_results(job_id: str) → BacktestResult`

### `jelva_sdk.analytics`

* `EquityCurve(series: pd.Series)`
* `SharpeRatio(returns: pd.Series)`

### `jelva_sdk.auth`

* `authenticate()`  — Launches OAuth flow and stores credentials locally.

---

## Configuration

The SDK reads configuration from:

1. **Environment Variables**

   * `JELVA_API_KEY`
   * `JELVA_API_URL` (optional; defaults to `https://api.jelva.com`)

2. **Config File** (`~/.jelva/config.toml`)

   ```toml
   [auth]
   api_key = "your_jelva_api_key"
   api_url = "https://api.jelva.com"
   ```

---

## Documentation & Examples

* **API Reference:** [https://api.jelva.com/docs](https://api.jelva.com/docs)
* **SDK Documentation:** [https://docs.jelva.com/sdk](https://docs.jelva.com/sdk)
* **Example Notebooks:** [https://github.com/jelva/sdk-examples](https://github.com/jelva/sdk-examples)

---

## Contributing

We welcome contributions and feedback! Please review our [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on reporting issues and submitting pull requests.

---

## License

Distributed under the [MIT License](./LICENSE).

import click
import structlog
import os
import httpx
from . import plugins
from . import upload

API_TOKEN_ENV = "JELVA_API_TOKEN"
API_BASE_URL = "https://api.jelva.com"

@click.group()
def main() -> None:
    """Jelva CLI entrypoint. Use this tool to interact with the Jelva platform from the command line."""
    pass

@main.command()
def login():
    """Authenticate with Jelva and store API token."""
    username = click.prompt("Username")
    password = click.prompt("Password", hide_input=True)
    try:
        resp = httpx.post(f"{API_BASE_URL}/api/v1/auth/login", json={"username": username, "password": password})
        if resp.status_code != 200:
            click.echo(f"Login failed: {resp.text}")
            return
        token = resp.json().get("token")
        if not token:
            click.echo("No token received.")
            return
        click.echo(f"Your API token: {token}")
        # TODO: Store token securely (e.g., keyring, config file)
    except Exception as e:
        click.echo(f"Login error: {e}")

@main.command()
@click.option('--strategy-path', required=True, type=click.Path(exists=True, file_okay=False), help='Path to strategy directory')
@click.option('--input-file', type=click.Path(exists=True, dir_okay=False), help='Input JSON file (optional)')
@click.option('--param', multiple=True, help='Extra parameters as key=value')
def dev_run(strategy_path, input_file, param):
    """Run a strategy locally using pluggy and input JSON or CLI params."""
    logger = structlog.get_logger()
    try:
        pm = plugins.load_from_directory(strategy_path)
        input_data = {}
        if input_file:
            import json
            with open(input_file) as f:
                input_data = json.load(f)
        for p in param:
            k, v = p.split('=', 1)
            input_data[k] = v
        results = pm.hook.run_strategy(input_data=input_data)
        click.echo(results[0] if results else 'No result')
    except Exception as e:
        logger.error("dev-run failed", error=str(e))
        raise click.ClickException(f"dev-run failed: {e}")

@main.command()
@click.option('--strategy-path', required=True, type=click.Path(exists=True, file_okay=False), help='Path to strategy directory')
@click.option('--name', required=True, type=str, help='Strategy name')
@click.option('--version', required=True, type=str, help='Strategy version')
def upload_strategy(strategy_path, name, version):
    """Package and upload a strategy to Jelva cloud."""
    logger = structlog.get_logger()
    try:
        token = os.environ.get(API_TOKEN_ENV)
        upload.upload_strategy(strategy_path, name, version, token=token)
        click.echo(f"Uploaded {name}-{version}")
    except Exception as e:
        logger.error("upload-strategy failed", error=str(e))
        raise click.ClickException(f"upload-strategy failed: {e}")

@main.command()
@click.option('--name', required=True, type=str, help='Strategy name')
@click.option('--version', required=True, type=str, help='Strategy version')
@click.option('--portfolio-id', required=True, type=str, help='Portfolio ID')
@click.option('--schedule', required=True, type=str, help='Cron schedule string')
def deploy_strategy(name, version, portfolio_id, schedule):
    """Deploy (schedule) a strategy in production."""
    logger = structlog.get_logger()
    try:
        token = os.environ.get(API_TOKEN_ENV)
        headers = {}
        if token:
            headers['Authorization'] = f'Bearer {token}'
        # TODO: Adjust endpoint and payload as per backend API
        resp = httpx.post(f"{API_BASE_URL}/api/v1/deployments", json={
            "name": name,
            "version": version,
            "portfolio_id": portfolio_id,
            "schedule": schedule
        }, headers=headers)
        if resp.status_code != 200:
            logger.error("deploy-strategy failed", status=resp.status_code, body=resp.text)
            raise click.ClickException(f"deploy-strategy failed: {resp.text}")
        click.echo(f"Scheduled {name}-{version} for portfolio {portfolio_id} with schedule '{schedule}'")
    except Exception as e:
        logger.error("deploy-strategy failed", error=str(e))
        raise click.ClickException(f"deploy-strategy failed: {e}")

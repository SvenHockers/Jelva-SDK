import zipfile
import hashlib
import httpx
import pathlib
import structlog
import toml
import os


def upload_strategy(path: str, name: str, version: str, token: str = None):
    """Zip .py files, compute hash, read manifest, POST to Jelva cloud."""
    logger = structlog.get_logger()
    zip_path = f"{name}-{version}.zip"
    # Zip all .py files
    with zipfile.ZipFile(zip_path, 'w') as zf:
        for py in pathlib.Path(path).glob('*.py'):
            zf.write(py, arcname=py.name)
    # Compute SHA256
    sha256 = hashlib.sha256()
    with open(zip_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    hash_hex = sha256.hexdigest()
    # Read pyproject.toml for dependencies
    manifest_path = os.path.join(path, 'pyproject.toml')
    if not os.path.exists(manifest_path):
        raise Exception('pyproject.toml not found in strategy directory')
    manifest = toml.load(manifest_path)
    # TODO: Extract dependencies from manifest
    # POST to /api/v1/strategies
    url = 'https://api.jelva.com/api/v1/strategies'
    with open(zip_path, 'rb') as f:
        files = {'file': (zip_path, f, 'application/zip')}
        data = {'name': name, 'version': version, 'hash': hash_hex}
        headers = {}
        if token:
            headers['Authorization'] = f'Bearer {token}'
        # TODO: Add retries on 5xx
        resp = httpx.post(url, data={'json': data}, files=files, headers=headers)
        if resp.status_code >= 500:
            # TODO: Retry logic
            logger.error('Server error', status=resp.status_code)
            raise Exception('Server error')
        if resp.status_code != 200:
            logger.error('Upload failed', status=resp.status_code, body=resp.text)
            raise Exception(f'Upload failed: {resp.text}')
        logger.info('Upload successful', response=resp.json())
    # TODO: Clean up zip file

# Backend runner stub
# TODO: Download ZIP, unzip to /tmp/strategy, call plugins.load_from_directory('/tmp/strategy'), then pm.hook.run_strategy(input_data=...) 
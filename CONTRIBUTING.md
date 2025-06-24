# Contributing to Jelva Python SDK

Thank you for your interest in contributing to the Jelva Python SDK! We welcome contributions from the community and appreciate your time and effort. This guide outlines the process for reporting issues, proposing enhancements, and submitting code changes.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Code of Conduct](#code-of-conduct)
3. [Reporting Issues](#reporting-issues)
4. [Feature Requests & Enhancements](#feature-requests--enhancements)
5. [Development Setup](#development-setup)
6. [Writing Tests](#writing-tests)
7. [Pull Request Process](#pull-request-process)
8. [Style Guidelines](#style-guidelines)
9. [Release & Versioning](#release--versioning)
10. [Community & Support](#community--support)

---

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork:

   ```bash
   git clone https://github.com/<your-username>/jelva-sdk.git
   cd jelva-sdk
   ```
3. Create a feature branch for your changes:

   ```bash
   git checkout -b feature/short-description
   ```

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/). By participating, you are expected to uphold this code. Please report any unacceptable behavior to \[[support@jelva.com](mailto:support@jelva.com)].

## Reporting Issues

If you discover a bug or unexpected behavior:

1. Search the existing issues to see if it’s already reported.
2. Create a new issue using the **Bug report** template.
3. Include:

   * A clear and descriptive title.
   * Steps to reproduce the behavior.
   * Expected vs. actual results.
   * Any relevant code snippets, logs, or screenshots.

## Feature Requests & Enhancements

We welcome suggestions for improving the SDK. To propose a new feature:

1. Search for existing feature requests to avoid duplicates.
2. Open a new issue using the **Feature request** template.
3. Describe the motivation, use case, and possible API design.

## Development Setup

1. Install dependencies:

   ```bash
   pip install -r requirements-dev.txt
   ```
2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. Install the SDK in editable mode:

   ```bash
   pip install -e .
   ```

## Writing Tests

* We use **pytest** for testing.
* Add tests for any bug fixes or new features under `tests/`.
* Aim for comprehensive coverage of core functionality.

Run tests locally:

```bash
pytest
```

## Pull Request Process

1. Ensure your branch is up-to-date with `main`:

   ```bash
   git fetch origin
   git rebase origin/main
   ```
2. Commit your changes with clear messages:

   ```bash
   git commit -m "Add new feature X"
   ```
3. Push your branch and open a pull request against the `main` branch.
4. Fill out the PR template, linking any relevant issues.
5. Wait for CI checks to pass and address any feedback.
6. Once approved, your PR will be merged.

## Style Guidelines

* Follow **PEP 8** for Python code style.
* Use **Black** for code formatting:

  ```bash
  black .
  ```
* Write docstrings for all public functions and classes using the Google style.

## Release & Versioning

* We follow **Semantic Versioning** (MAJOR.MINOR.PATCH).
* After merging, the maintainer will update the version, tag a release, and publish to PyPI.

## Community & Support

* Join our Slack community: [jelva.slack.com](https://jelva.slack.com)
* Ask questions or get help via GitHub Discussions.

---

Thank you for helping make the Jelva Python SDK better! We look forward to your contributions.

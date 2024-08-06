# Audio Streaming Project

## Overview

This project trains an audio streaming model using PyTorch and PySpark.

## Setup

1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install dependencies:
    ```bash
    make install
    ```

## Usage

- To run the training script:
    ```bash
    make run
    ```

- To run tests:
    ```bash
    make test
    ```

- To lint the code:
    ```bash
    make lint
    ```

## Docker

- To build the Docker image:
    ```bash
    make docker-build
    ```

- To run the Docker container:
    ```bash
    make docker-run
    ```

## Versioning

This project uses Git tags for versioning. Each tag represents a version release. The version number is based on the current timestamp.

### Creating a New Release

1. Make sure your changes are committed and pushed to the master branch.
2. A new Git tag will be created automatically with the current timestamp when changes are pushed to the master branch.
3. The new tag will trigger a GitHub Actions workflow that creates a GitHub release.

Artifacts and binaries can be attached to the release for distribution.

## Example

After a successful push to the master branch, the workflow will:
- Run tests
- Create a new version tag
- Push the tag to GitHub
- Create a new release on GitHub with the tag

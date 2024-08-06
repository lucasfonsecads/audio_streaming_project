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

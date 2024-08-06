# Define variables
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# Default target: create virtual environment and install dependencies
all: install

# Create virtual environment
$(VENV_DIR)/bin/activate: requirements.txt
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	touch $(VENV_DIR)/bin/activate

# Install dependencies
install: $(VENV_DIR)/bin/activate

test:
	@pytest tests/

lint:
	@pylint src/

run:
	PYTHON=src src/train.py

docker-build:
	@docker build -t audio_streaming_project .

docker-run:
	@docker run -it audio_streaming_project

# Clean virtual environment
clean:
	rm -rf $(VENV_DIR)

.PHONY: all install server1 server2 load_balancer test run_all clean

install:
    pip install -r requirements.txt

test:
    pytest tests/

lint:
    pylint src/

run:
    python src/train.py

docker-build:
    docker build -t audio_streaming_project .

docker-run:
    docker run -it audio_streaming_project

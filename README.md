# Flask Docker Demo

A small Flask web application packaged as a Docker image.

## Prerequisites

- Python 3.10+ (only needed to run without Docker)
- Docker Desktop or Docker Engine with the Compose plugin

## Run locally (without Docker)

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 and check http://localhost:5000/health.

## Build the Docker image

Run these commands from the project directory:

```bash
docker build -t flask-docker-demo:1.0 .
```

Confirm the image exists:

```bash
docker images
```

## Run the container

```bash
docker run -d --name flask-docker-demo -p 5000:5000 flask-docker-demo:1.0
```

Open http://localhost:5000.

Check the health endpoint:

```bash
curl http://localhost:5000/health
```

Expected response:

```json
{"status":"healthy"}
```

View logs:

```bash
docker logs flask-docker-demo
```

Stop and remove the container:

```bash
docker stop flask-docker-demo
docker rm flask-docker-demo
```

## Run with Docker Compose

```bash
docker compose up --build -d
docker compose ps
docker compose logs -f
```

Stop the application:

```bash
docker compose down
```

## Project structure

```text
flask-docker-demo/
├── app.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── README.md
└── templates/
    └── index.html
```

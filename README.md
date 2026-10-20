# FastAPI Items API — CI/CD Laboratory Work 1

A simple REST API to manage items. It implements CRUD operations, JSON responses, appropriate HTTP statuses, OpenAPI and Swagger UI. Data is kept in memory (no database is required for Lab 1).

## Technologies

- Python 3.12
- FastAPI and Uvicorn
- Pytest and HTTPX
- Docker
- GitHub, Azure DevOps Pipelines, Docker Hub

## Project structure

- `app/main.py` — REST endpoints
- `app/models.py` — request and response models
- `app/repository.py` — in-memory item repository
- `tests/test_repository.py` — unit tests
- `tests/test_api.py` — HTTP and OpenAPI tests
- `Dockerfile` — Docker container configuration
- `azure-pipelines.yml` — automatic build, test and publish pipeline

## Run locally

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on Linux/macOS:

```bash
source .venv/bin/activate
```

Install the dependencies and start the service:

```bash
python -m pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## API endpoints

| HTTP method | Path | Behavior | Expected status |
| --- | --- | --- | --- |
| GET | `/api/items` | List all items | 200 |
| GET | `/api/items/{id}` | Get item by ID | 200 / 404 |
| POST | `/api/items` | Create an item | 201 / 422 |
| PUT | `/api/items/{id}` | Update an item | 200 / 404 / 422 |
| DELETE | `/api/items/{id}` | Delete an item | 204 / 404 |

Example POST request JSON:

```json
{
  "name": "Notebook",
  "description": "For university"
}
```

## Run tests

```bash
python -m pytest -q
```

## Build and run the Docker image

```bash
docker build -t fastapi-ci-cd-lab1:latest .
docker run --rm -p 8000:8000 fastapi-ci-cd-lab1:latest
```

Swagger UI in the Docker container: http://localhost:8000/docs

## Configure automatic CI in Azure DevOps

1. Create a GitHub repository and push this project to the `main` branch.
2. Create a **public or private** Docker Hub repository named `fastapi-ci-cd-lab1`.
3. In Azure DevOps, create a project. Add a **Docker Registry** service connection for Docker Hub named `dockerhub-connection` (use a Docker Hub access token where supported).
4. Open `azure-pipelines.yml` and replace `YOUR_DOCKERHUB_USERNAME` with your own Docker Hub username.
5. Create a new Azure Pipeline from your GitHub repository using the existing `azure-pipelines.yml` file. Authorize the service connection when requested.
6. Ensure the Azure DevOps organization has permission to run a Microsoft-hosted agent (or configure a self-hosted agent if required).
7. Push changes to `main`: the pipeline checks Python code, runs tests, builds a Docker image with `latest` and `Build.BuildId` tags, and pushes both to Docker Hub.

**Important:** Never commit Docker Hub passwords or tokens to your GitHub repository.

## Limitations

Items are stored in memory, so all items are lost whenever the server restarts. This is allowed for Laboratory Work 1.

CI/CD pipeline successfully configured with Azure DevOps.

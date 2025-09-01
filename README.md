# FastAPI DDD Infra with Docker, Docker Compose, and OpenAI Agents SDK

This project demonstrates a Domain-Driven Design (DDD) architecture using FastAPI,
integrated with OpenAI Agents SDK primitives (Agent, Tools, Runner),
deployed via Docker and docker-compose, with Postgres, Redis, and Alembic migrations.

## Features
- FastAPI application (`/health`, `/agents/run` endpoints)
- OpenAI Agents SDK: Agent, Tools (function calling), Runner
- DDD layers: `domain/`, `application/`, `infrastructure/`, `interfaces/`
- Postgres persistence via SQLAlchemy and Alembic migrations
- Redis cache (optional)
- Docker multi-stage build and docker-compose profiles (dev, test)
- Configuration via `.env`
- Structured logging and health checks

## Getting Started

### Prerequisites
- Docker & Docker Compose
- OpenAI API Key

### Configuration
1. Copy `.env.example` to `.env` and fill in values (especially `OPENAI_API_KEY`).

### Build and Run (Development)
```bash
docker-compose up -d
```

With live reload (code changes reflected):
```bash
docker-compose up -d
```

### Health Check
```bash
curl http://localhost:8000/health
```

### Agents Endpoint
```bash
curl -X POST http://localhost:8000/agents/run \
  -H 'Content-Type: application/json' \
  -d '{"person_id": 1}'
```

## Database Migrations
Generate and apply migrations with Alembic:
```bash
alembic upgrade head
```

## Running Tests
```bash
docker-compose -f docker-compose.yml -f docker-compose.test.yml up test
```
or locally:
```bash
pip install -r dev-requirements.txt
pytest
```

## Switching Models
To use `OpenAIChatCompletionsModel` instead of default, update
`src/app/infrastructure/openai/model.py`:
```python
from openai_agents.models import OpenAIChatCompletionsModel

default_model = OpenAIChatCompletionsModel()
```

## Streaming Responses
The Runner supports streaming: call `runner.run_streamed()` and
stream events to the client (e.g., via WebSockets).

## Troubleshooting
- Ensure `.env` variables are set
- Check container logs: `docker-compose logs -f`

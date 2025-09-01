# Builder stage: install dependencies and build wheels
FROM python:3.11-slim AS builder
WORKDIR /app
RUN apt-get update \
    && apt-get install -y build-essential gcc \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Runtime stage: install wheels and application code
FROM python:3.11-slim AS runtime
WORKDIR /app
RUN apt-get update \
    && apt-get install -y libpq-dev \
    && rm -rf /var/lib/apt/lists/*
COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-cache-dir --no-index --find-links /wheels -r requirements.txt
COPY src ./src
COPY alembic.ini .
COPY alembic ./alembic
COPY .env.example .env
ENV PYTHONPATH=/app/src
CMD ["uvicorn", "app.interfaces.http.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Use a lightweight Python base
FROM python:3.14-slim AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Enable bytecode compilation for faster container startup
ENV UV_COMPILE_BYTECODE=1

# Copy project files for dependency installation
COPY uv.lock pyproject.toml /app/

# Install dependencies without copying the source code yet
# This enables efficient Docker caching
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application
COPY . /app

# Install the project itself
RUN uv sync --frozen --no-dev

# Final runtime stage
FROM python:3.14-slim

WORKDIR /app

# Copy the virtual environment and built application from builder
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app /app

RUN apt-get update && apt-get install ghostscript -y

# Place executables in PATH
ENV PATH="/app/.venv/bin:$PATH"


CMD ["litestar", "run", "--host", "0.0.0.0", "--port", "80"]
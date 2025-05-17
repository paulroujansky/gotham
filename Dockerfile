FROM python:3.11-bookworm

# Copy uv from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory
WORKDIR /app

# Copy only dependency files first
COPY pyproject.toml .

# Install dependencies using uv
RUN uv sync

# Copy the application code
COPY src/ src/

# Expose the port from environment variable
EXPOSE ${APP_PORT}

# Run the application
CMD ["uv", "run", "src/gotham/api/app.py"]

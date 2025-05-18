# Gotham Crime Management API 🦇

Demo API built with [Robyn](https://robyn.tech/).

This API provides endpoints for managing crime records in Gotham City. 👮

## Features

- Fast and efficient API built with Robyn
- PostgreSQL database for reliable data storage
- Docker support for easy deployment
- Interactive API documentation with Swagger UI
- JSON response formatting
- Pagination support
- Geolocation support for crime locations
- Type-safe request/response handling
- Comprehensive error handling

## Project Structure

The project is organized for clarity, modularity, and ease of maintenance. Here's an overview of the main directories and their responsibilities:

```
src/gotham/
├── api/         # HTTP routes, request/response logic
├── core/        # Domain models, core business logic, CRUD
├── services/    # Service layer (business orchestration, validation)
├── db/          # Database connection, migrations
├── sql/         # Raw SQL queries, organized by domain (e.g., crimes/)
├── utils/       # Utilities/helpers
└── config.py    # App configuration
```

## Requirements

- Python 3.11 or higher
- PostgreSQL 12 or higher
- Docker and Docker Compose (for containerized deployment)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/paulroujansky/gotham.git
cd gotham
```

2. Install [`uv`](https://docs.astral.sh/uv/)
```bash
brew install uv
```

3. Install dependencies:
```bash
uv sync
```

4. Copy the example environment file and adjust the variables:
```bash
cp .env.example .env
```

## Quickstart

Get up and running quickly with [Docker](https://www.docker.com/):

```bash
# Clone the repository
git clone https://github.com/paulroujansky/gotham.git
cd gotham

# Copy environment variables template and adjust as needed
cp .env.example .env

# Build and start the containers
docker-compose up --build
```
- API available at: http://0.0.0.0:8080
- API docs: http://0.0.0.0:8080/docs

## API Endpoints

### GET /crimes
Get a list of crimes with pagination.

Query Parameters:
- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

### GET /crimes/:crime_id
Get a specific crime by ID.

### POST /crimes
Add a new crime.

Request Body:
```json
{
  "type": "robbery",
  "description": "Bank robbery",
  "location": "Gotham Bank",
  "suspect_name": "Joker",
  "date_time": "2024-03-20T15:30:00Z",
  "latitude": 40.7128,
  "longitude": -74.0060
}
```

### PUT /crimes/:crime_id
Update an existing crime.

### DELETE /crimes/:crime_id
Delete a crime by ID.

## Environment Variables

- `APP_HOST`: Host to bind the server to (default: "0.0.0.0")
- `APP_PORT`: Port to bind the server to (default: 8080)
- `DATABASE_URL`: PostgreSQL connection URL
- `APP_TITLE`: Application title for OpenAPI documentation
- `APP_DESCRIPTION`: Application description for OpenAPI documentation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Robyn](https://github.com/sansyrox/robyn) - The web framework used
- [PostgreSQL](https://www.postgresql.org/) - The database used
- [Docker](https://www.docker.com/) - For containerization

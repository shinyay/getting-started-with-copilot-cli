# Bookmark Manager API — Sample Application

A layered REST-style bookmark manager for workshop exploration.
This app has more architectural depth than Level 1's task tracker — designed for cross-file analysis.

## Architecture

```
routes.py  →  service.py  →  repository.py  →  models.py
    ↓              ↓               ↓
middleware.py   errors.py       config.py
```

| Layer | File | Responsibility |
|-------|------|----------------|
| Entry point | `app.py` | Application setup, route registration, server start |
| Routes | `routes.py` | HTTP request handling, input parsing, response formatting |
| Service | `service.py` | Business logic, validation orchestration, tag management |
| Repository | `repository.py` | Data persistence (JSON file + in-memory), CRUD operations |
| Models | `models.py` | Data classes, field validation, serialization |
| Middleware | `middleware.py` | Request logging, auth token check, error wrapping |
| Errors | `errors.py` | Custom exception hierarchy with HTTP status codes |
| Config | `config.py` | Environment-based configuration, defaults |
| Tests | `tests/` | Unit tests for models and service layer |

## Usage

```bash
python app.py                              # Start server on :8080
python app.py --port 3000 --storage memory # In-memory mode on :3000

# API calls
curl localhost:8080/bookmarks
curl -X POST localhost:8080/bookmarks -d '{"url":"https://example.com","title":"Example"}'
curl localhost:8080/bookmarks/1
curl -X DELETE localhost:8080/bookmarks/1
curl localhost:8080/tags
curl "localhost:8080/bookmarks?tag=python"
```

"""Request handling middleware — logging, auth, and error wrapping."""

import logging
import time
import json
from typing import Callable
from http.server import BaseHTTPRequestHandler

from config import Config
from errors import AppError, AuthenticationError

logger = logging.getLogger("middleware")


def setup_logging():
    """Configure application-wide logging."""
    logging.basicConfig(
        level=getattr(logging, Config.LOG_LEVEL, logging.INFO),
        format=Config.LOG_FORMAT,
    )


def check_auth(headers: dict) -> bool:
    """Validate the Authorization header if auth is enabled."""
    if not Config.AUTH_ENABLED:
        return True

    auth_header = headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return False

    token = auth_header[7:]
    return token == Config.AUTH_TOKEN


class RequestContext:
    """Holds per-request metadata for logging and tracing."""

    def __init__(self, method: str, path: str, client_addr: str):
        self.method = method
        self.path = path
        self.client_addr = client_addr
        self.start_time = time.monotonic()
        self.request_id = f"{int(time.time() * 1000)}"

    @property
    def elapsed_ms(self) -> float:
        return (time.monotonic() - self.start_time) * 1000

    def log_start(self):
        logger.info(
            f"[{self.request_id}] → {self.method} {self.path} from {self.client_addr}"
        )

    def log_end(self, status_code: int):
        logger.info(
            f"[{self.request_id}] ← {status_code} ({self.elapsed_ms:.1f}ms)"
        )


def parse_json_body(handler: BaseHTTPRequestHandler) -> dict:
    """Read and parse the JSON body from an HTTP request."""
    content_length = int(handler.headers.get("Content-Length", 0))
    if content_length == 0:
        return {}
    raw = handler.rfile.read(content_length)
    try:
        return json.loads(raw.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        raise AppError(f"Invalid JSON body: {e}")


def send_json_response(
    handler: BaseHTTPRequestHandler,
    data: dict | list,
    status_code: int = 200,
):
    """Write a JSON response to the HTTP handler."""
    body = json.dumps(data, indent=2).encode("utf-8")
    handler.send_response(status_code)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def send_error_response(
    handler: BaseHTTPRequestHandler,
    error: AppError,
):
    """Write an error JSON response."""
    send_json_response(handler, error.to_dict(), error.status_code)

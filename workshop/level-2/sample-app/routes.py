"""HTTP route handlers for the bookmark API."""

import json
import re
import logging
from http.server import BaseHTTPRequestHandler
from typing import Optional

from service import BookmarkService
from errors import AppError, AuthenticationError
from middleware import (
    RequestContext,
    check_auth,
    parse_json_body,
    send_json_response,
    send_error_response,
)

logger = logging.getLogger("routes")


class BookmarkHandler(BaseHTTPRequestHandler):
    """HTTP request handler with route dispatching."""

    # Injected by app.py at startup
    service: BookmarkService = None  # type: ignore

    def do_GET(self):
        self._handle_request("GET")

    def do_POST(self):
        self._handle_request("POST")

    def do_DELETE(self):
        self._handle_request("DELETE")

    def do_PUT(self):
        self._handle_request("PUT")

    def log_message(self, format, *args):
        """Suppress default stderr logging (we use our own)."""
        pass

    def _handle_request(self, method: str):
        """Central dispatcher with auth, logging, and error handling."""
        ctx = RequestContext(method, self.path, self.client_address[0])
        ctx.log_start()

        try:
            # Auth check
            if not check_auth(dict(self.headers)):
                raise AuthenticationError("Invalid or missing authentication token")

            # Route dispatch
            response, status = self._dispatch(method, self.path)
            send_json_response(self, response, status)
            ctx.log_end(status)

        except AppError as e:
            send_error_response(self, e)
            ctx.log_end(e.status_code)

        except Exception as e:
            logger.exception(f"Unhandled error: {e}")
            err = AppError("Internal server error")
            send_error_response(self, err)
            ctx.log_end(500)

    def _dispatch(self, method: str, path: str) -> tuple[dict | list, int]:
        """Match the path and method to a handler function."""
        # Strip query string for path matching
        clean_path = path.split("?")[0].rstrip("/")
        query = self._parse_query(path)

        # GET /bookmarks
        if method == "GET" and clean_path == "/bookmarks":
            return self._list_bookmarks(query), 200

        # POST /bookmarks
        if method == "POST" and clean_path == "/bookmarks":
            return self._create_bookmark(), 201

        # GET /bookmarks/:id
        match = re.match(r"^/bookmarks/(\d+)$", clean_path)
        if match:
            bid = int(match.group(1))
            if method == "GET":
                return self._get_bookmark(bid), 200
            if method == "DELETE":
                return self._delete_bookmark(bid), 200
            if method == "PUT":
                return self._update_bookmark(bid), 200

        # POST /bookmarks/:id/visit
        match = re.match(r"^/bookmarks/(\d+)/visit$", clean_path)
        if match and method == "POST":
            return self._visit_bookmark(int(match.group(1))), 200

        # POST /bookmarks/:id/archive
        match = re.match(r"^/bookmarks/(\d+)/archive$", clean_path)
        if match and method == "POST":
            return self._archive_bookmark(int(match.group(1))), 200

        # POST /bookmarks/:id/restore
        match = re.match(r"^/bookmarks/(\d+)/restore$", clean_path)
        if match and method == "POST":
            return self._restore_bookmark(int(match.group(1))), 200

        # GET /tags
        if method == "GET" and clean_path == "/tags":
            return self._list_tags(), 200

        # GET /stats
        if method == "GET" and clean_path == "/stats":
            return self._get_stats(), 200

        # GET /health
        if method == "GET" and clean_path == "/health":
            return {"status": "ok"}, 200

        raise AppError(f"Not found: {method} {path}")

    # ── Handler methods ─────────────────────────────────────────

    def _list_bookmarks(self, query: dict) -> list:
        tag = query.get("tag")
        domain = query.get("domain")
        sort_by = query.get("sort", "created")
        include_archived = query.get("archived", "false").lower() == "true"
        bookmarks = self.service.list_bookmarks(
            tag=tag, domain=domain, sort_by=sort_by, include_archived=include_archived
        )
        return [b.to_dict() for b in bookmarks]

    def _create_bookmark(self) -> dict:
        body = parse_json_body(self)
        bookmark = self.service.create_bookmark(
            url=body.get("url", ""),
            title=body.get("title", ""),
            description=body.get("description", ""),
            tags=body.get("tags", []),
        )
        return bookmark.to_dict()

    def _get_bookmark(self, bid: int) -> dict:
        return self.service.get_bookmark(bid).to_dict()

    def _delete_bookmark(self, bid: int) -> dict:
        bookmark = self.service.delete_bookmark(bid)
        return {"deleted": bookmark.to_dict()}

    def _update_bookmark(self, bid: int) -> dict:
        body = parse_json_body(self)
        bookmark = self.service.get_bookmark(bid)
        # Only update provided fields
        if "title" in body:
            bookmark.title = body["title"]
        if "description" in body:
            bookmark.description = body["description"]
        if "tags" in body:
            bookmark.tags = body["tags"]
        bookmark._validate()
        return self.service._repo.update(bookmark).to_dict()

    def _visit_bookmark(self, bid: int) -> dict:
        return self.service.visit_bookmark(bid).to_dict()

    def _archive_bookmark(self, bid: int) -> dict:
        return self.service.archive_bookmark(bid).to_dict()

    def _restore_bookmark(self, bid: int) -> dict:
        return self.service.restore_bookmark(bid).to_dict()

    def _list_tags(self) -> dict:
        return {"tags": self.service.get_all_tags()}

    def _get_stats(self) -> dict:
        return self.service.get_stats()

    # ── Helpers ──────────────────────────────────────────────────

    @staticmethod
    def _parse_query(path: str) -> dict:
        """Parse query string from a URL path."""
        if "?" not in path:
            return {}
        query_str = path.split("?", 1)[1]
        params = {}
        for pair in query_str.split("&"):
            if "=" in pair:
                k, v = pair.split("=", 1)
                params[k] = v
        return params

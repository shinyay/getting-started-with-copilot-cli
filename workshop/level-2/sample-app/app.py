#!/usr/bin/env python3
"""Bookmark Manager API — application entry point."""

import argparse
import logging
from http.server import HTTPServer

from config import Config
from middleware import setup_logging
from repository import create_repository
from service import BookmarkService
from routes import BookmarkHandler

logger = logging.getLogger("app")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Bookmark Manager API Server")
    parser.add_argument("--host", default=Config.HOST, help="Bind address")
    parser.add_argument("--port", type=int, default=Config.PORT, help="Listen port")
    parser.add_argument(
        "--storage",
        choices=["file", "memory"],
        default=Config.STORAGE_BACKEND,
        help="Storage backend",
    )
    return parser


def main():
    setup_logging()
    args = build_parser().parse_args()

    # Validate config
    warnings = Config.validate()
    for w in warnings:
        logger.warning(f"Config warning: {w}")

    # Wire dependencies
    repo = create_repository(args.storage)
    service = BookmarkService(repo)
    BookmarkHandler.service = service

    # Start server
    server = HTTPServer((args.host, args.port), BookmarkHandler)
    logger.info(f"Bookmark Manager API running on {args.host}:{args.port}")
    logger.info(f"Storage: {args.storage}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()

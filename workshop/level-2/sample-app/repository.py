"""Data persistence layer with pluggable storage backends."""

import json
import threading
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

from config import Config
from models import Bookmark
from errors import StorageError, NotFoundError


class BaseRepository(ABC):
    """Abstract base for bookmark storage."""

    @abstractmethod
    def save(self, bookmark: Bookmark) -> Bookmark: ...

    @abstractmethod
    def get(self, bookmark_id: int) -> Optional[Bookmark]: ...

    @abstractmethod
    def list_all(self) -> list[Bookmark]: ...

    @abstractmethod
    def delete(self, bookmark_id: int) -> Bookmark: ...

    @abstractmethod
    def update(self, bookmark: Bookmark) -> Bookmark: ...

    @abstractmethod
    def find_by_tag(self, tag: str) -> list[Bookmark]: ...

    @abstractmethod
    def find_by_domain(self, domain: str) -> list[Bookmark]: ...

    @abstractmethod
    def count(self) -> int: ...


class InMemoryRepository(BaseRepository):
    """Thread-safe in-memory storage (data lost on restart)."""

    def __init__(self):
        self._store: dict[int, Bookmark] = {}
        self._next_id: int = 1
        self._lock = threading.Lock()

    def save(self, bookmark: Bookmark) -> Bookmark:
        with self._lock:
            bookmark.id = self._next_id
            self._store[bookmark.id] = bookmark
            self._next_id += 1
        return bookmark

    def get(self, bookmark_id: int) -> Optional[Bookmark]:
        return self._store.get(bookmark_id)

    def list_all(self) -> list[Bookmark]:
        return list(self._store.values())

    def delete(self, bookmark_id: int) -> Bookmark:
        with self._lock:
            bookmark = self._store.pop(bookmark_id, None)
            if not bookmark:
                raise NotFoundError(f"Bookmark #{bookmark_id} not found")
            return bookmark

    def update(self, bookmark: Bookmark) -> Bookmark:
        with self._lock:
            if bookmark.id not in self._store:
                raise NotFoundError(f"Bookmark #{bookmark.id} not found")
            self._store[bookmark.id] = bookmark
        return bookmark

    def find_by_tag(self, tag: str) -> list[Bookmark]:
        tag = tag.lower()
        return [b for b in self._store.values() if tag in b.tags]

    def find_by_domain(self, domain: str) -> list[Bookmark]:
        domain = domain.lower()
        return [b for b in self._store.values() if b.domain.lower() == domain]

    def count(self) -> int:
        return len(self._store)


class FileRepository(BaseRepository):
    """JSON file-based storage with file locking."""

    def __init__(self, filepath: str = Config.DATA_FILE):
        self._filepath = Path(filepath)
        self._lock = threading.Lock()
        self._ensure_file()

    def _ensure_file(self):
        if not self._filepath.exists():
            self._write({"next_id": 1, "bookmarks": []})

    def _read(self) -> dict:
        try:
            with open(self._filepath, "r") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise StorageError(f"Corrupted data file: {e}")

    def _write(self, data: dict):
        try:
            self._filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(self._filepath, "w") as f:
                json.dump(data, f, indent=2)
        except OSError as e:
            raise StorageError(f"Failed to write data file: {e}")

    def save(self, bookmark: Bookmark) -> Bookmark:
        with self._lock:
            data = self._read()
            bookmark.id = data["next_id"]
            data["bookmarks"].append(bookmark.to_dict())
            data["next_id"] += 1
            self._write(data)
        return bookmark

    def get(self, bookmark_id: int) -> Optional[Bookmark]:
        data = self._read()
        for entry in data["bookmarks"]:
            if entry["id"] == bookmark_id:
                return Bookmark.from_dict(entry)
        return None

    def list_all(self) -> list[Bookmark]:
        data = self._read()
        return [Bookmark.from_dict(b) for b in data["bookmarks"]]

    def delete(self, bookmark_id: int) -> Bookmark:
        with self._lock:
            data = self._read()
            for i, entry in enumerate(data["bookmarks"]):
                if entry["id"] == bookmark_id:
                    removed = data["bookmarks"].pop(i)
                    self._write(data)
                    return Bookmark.from_dict(removed)
            raise NotFoundError(f"Bookmark #{bookmark_id} not found")

    def update(self, bookmark: Bookmark) -> Bookmark:
        with self._lock:
            data = self._read()
            for i, entry in enumerate(data["bookmarks"]):
                if entry["id"] == bookmark.id:
                    data["bookmarks"][i] = bookmark.to_dict()
                    self._write(data)
                    return bookmark
            raise NotFoundError(f"Bookmark #{bookmark.id} not found")

    def find_by_tag(self, tag: str) -> list[Bookmark]:
        tag = tag.lower()
        return [b for b in self.list_all() if tag in b.tags]

    def find_by_domain(self, domain: str) -> list[Bookmark]:
        domain = domain.lower()
        return [b for b in self.list_all() if b.domain.lower() == domain]

    def count(self) -> int:
        data = self._read()
        return len(data["bookmarks"])


def create_repository(backend: str = Config.STORAGE_BACKEND) -> BaseRepository:
    """Factory function to create the configured repository."""
    if backend == "memory":
        return InMemoryRepository()
    elif backend == "file":
        return FileRepository()
    else:
        raise ValueError(f"Unknown storage backend: {backend}")

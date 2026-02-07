"""File-based note persistence."""

import json
import os
from typing import Optional

from config import NOTES_FILE, MAX_NOTES
from models import Note


class NoteStorage:
    """JSON file-based storage for notes."""

    def __init__(self, filepath: str = NOTES_FILE):
        self._filepath = filepath
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self._filepath):
            self._write({"next_id": 1, "notes": []})

    def _read(self) -> dict:
        # BUG: No error handling for corrupted JSON files
        # If the file contains invalid JSON, this crashes with an unhandled exception
        with open(self._filepath, "r") as f:
            return json.load(f)

    def _write(self, data: dict):
        with open(self._filepath, "w") as f:
            json.dump(data, f, indent=2)

    def add(self, note: Note) -> Note:
        data = self._read()
        if len(data["notes"]) >= MAX_NOTES:
            raise RuntimeError(f"Note limit reached ({MAX_NOTES})")
        note.id = data["next_id"]
        data["notes"].append(note.to_dict())
        data["next_id"] += 1
        self._write(data)
        return note

    def get(self, note_id: int) -> Optional[Note]:
        data = self._read()
        for entry in data["notes"]:
            if entry["id"] == note_id:
                return Note.from_dict(entry)
        return None

    def list_all(self) -> list[Note]:
        data = self._read()
        return [Note.from_dict(n) for n in data["notes"]]

    def update(self, note: Note) -> Note:
        data = self._read()
        for i, entry in enumerate(data["notes"]):
            if entry["id"] == note.id:
                note.touch()
                data["notes"][i] = note.to_dict()
                self._write(data)
                return note
        raise ValueError(f"Note #{note.id} not found")

    def delete(self, note_id: int) -> Note:
        data = self._read()
        for i, entry in enumerate(data["notes"]):
            if entry["id"] == note_id:
                removed = data["notes"].pop(i)
                self._write(data)
                return Note.from_dict(removed)
        raise ValueError(f"Note #{note_id} not found")

    # BUG: No thread safety — concurrent writes can corrupt the file
    # This would matter if used as a backend for a web server

    def get_all_tags(self) -> dict[str, int]:
        """Get all tags with their usage count."""
        tags: dict[str, int] = {}
        for note in self.list_all():
            for tag in note.tags:
                tags[tag] = tags.get(tag, 0) + 1
        return dict(sorted(tags.items(), key=lambda x: -x[1]))

    def stats(self) -> dict:
        notes = self.list_all()
        return {
            "total": len(notes),
            "pinned": sum(1 for n in notes if n.is_pinned),
            "total_words": sum(n.word_count for n in notes),
            "unique_tags": len(self.get_all_tags()),
            "tags": self.get_all_tags(),
        }

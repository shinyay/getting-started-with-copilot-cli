"""Short code generation."""

import hashlib
import random
import string
from shortener.config import CODE_LENGTH, CODE_CHARSET


def generate_code(url: str, length: int = CODE_LENGTH) -> str:
    """Generate a short code from a URL using a hash-based approach.

    Uses SHA-256 hash of the URL, then maps to the allowed character set.
    Deterministic: same URL always produces the same code.
    """
    hash_bytes = hashlib.sha256(url.encode("utf-8")).digest()
    code = []
    for i in range(length):
        idx = hash_bytes[i] % len(CODE_CHARSET)
        code.append(CODE_CHARSET[idx])
    return "".join(code)


def generate_random_code(length: int = CODE_LENGTH) -> str:
    """Generate a random short code (non-deterministic)."""
    return "".join(random.choices(CODE_CHARSET, k=length))


def is_valid_code(code: str) -> bool:
    """Return True if code is a valid short code format."""
    if not code or not isinstance(code, str):
        return False
    if len(code) != CODE_LENGTH:
        return False
    return all(c in CODE_CHARSET for c in code)

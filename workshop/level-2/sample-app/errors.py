"""Custom exception hierarchy with HTTP status code mapping."""


class AppError(Exception):
    """Base exception for all application errors."""
    status_code: int = 500
    error_type: str = "internal_error"

    def __init__(self, message: str, details: dict | None = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> dict:
        return {
            "error": self.error_type,
            "message": self.message,
            "details": self.details,
        }


class NotFoundError(AppError):
    status_code = 404
    error_type = "not_found"


class ValidationError(AppError):
    status_code = 422
    error_type = "validation_error"

    def __init__(self, message: str, field: str | None = None):
        details = {"field": field} if field else {}
        super().__init__(message, details)


class DuplicateError(AppError):
    status_code = 409
    error_type = "duplicate"


class StorageError(AppError):
    status_code = 500
    error_type = "storage_error"


class AuthenticationError(AppError):
    status_code = 401
    error_type = "authentication_error"


class LimitExceededError(AppError):
    status_code = 429
    error_type = "limit_exceeded"

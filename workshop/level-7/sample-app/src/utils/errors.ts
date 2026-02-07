/**
 * Application-wide error class.
 *
 * CONVENTION: All errors thrown in route handlers and services
 * must use AppError. Never throw plain Error objects.
 */
export class AppError extends Error {
  public readonly statusCode: number;
  public readonly code: string;
  public readonly isOperational: boolean;

  constructor(
    message: string,
    statusCode: number = 500,
    code: string = "INTERNAL_ERROR",
    isOperational: boolean = true
  ) {
    super(message);
    this.statusCode = statusCode;
    this.code = code;
    this.isOperational = isOperational;
    Object.setPrototypeOf(this, AppError.prototype);
  }

  static badRequest(message: string, code: string = "BAD_REQUEST"): AppError {
    return new AppError(message, 400, code);
  }

  static notFound(message: string, code: string = "NOT_FOUND"): AppError {
    return new AppError(message, 404, code);
  }

  static unauthorized(message: string = "Unauthorized"): AppError {
    return new AppError(message, 401, "UNAUTHORIZED");
  }

  static conflict(message: string, code: string = "CONFLICT"): AppError {
    return new AppError(message, 409, code);
  }

  static internal(message: string = "Internal server error"): AppError {
    return new AppError(message, 500, "INTERNAL_ERROR", false);
  }
}

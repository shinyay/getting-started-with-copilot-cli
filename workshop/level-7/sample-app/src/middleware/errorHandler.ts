/**
 * Error handling middleware.
 *
 * CONVENTION: This is the ONLY place where AppError is converted to HTTP responses.
 * All other code throws AppError — this middleware catches and formats them.
 */

import { Request, Response, NextFunction } from "express";
import { AppError } from "../utils/errors";
import { respondError } from "../utils/response";
import { logger } from "../utils/logger";

export function errorHandler(
  err: Error,
  _req: Request,
  res: Response,
  _next: NextFunction
): void {
  if (err instanceof AppError) {
    logger.warn("Operational error", {
      code: err.code,
      statusCode: err.statusCode,
      message: err.message,
    });
    res.status(err.statusCode).json(respondError(err.code, err.message));
    return;
  }

  // Unexpected errors
  logger.error("Unhandled error", {
    name: err.name,
    message: err.message,
    stack: err.stack,
  });
  res.status(500).json(respondError("INTERNAL_ERROR", "An unexpected error occurred"));
}

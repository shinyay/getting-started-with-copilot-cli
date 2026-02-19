/**
 * Request validation middleware using Zod.
 *
 * CONVENTION: Define Zod schemas alongside routes. Use validateBody()
 * middleware in route definitions for automatic request validation.
 */

import { Request, Response, NextFunction } from "express";
import { z, ZodSchema } from "zod";
import { AppError } from "../utils/errors";

export function validateBody(schema: ZodSchema) {
  return (req: Request, _res: Response, next: NextFunction): void => {
    const result = schema.safeParse(req.body);
    if (!result.success) {
      const messages = result.error.errors
        .map((e) => `${e.path.join(".")}: ${e.message}`)
        .join("; ");
      throw AppError.badRequest(`Validation failed: ${messages}`, "VALIDATION_ERROR");
    }
    req.body = result.data;
    next();
  };
}

// Zod schemas for event endpoints
export const createEventSchema = z.object({
  title: z.string().min(1).max(200),
  description: z.string().max(5000),
  date: z.string().datetime(),
  location: z.string().min(1).max(500),
  capacity: z.number().int().positive(),
  tags: z.array(z.string().max(50)).max(10).optional(),
});

export const updateEventSchema = z.object({
  title: z.string().min(1).max(200).optional(),
  description: z.string().max(5000).optional(),
  date: z.string().datetime().optional(),
  location: z.string().min(1).max(500).optional(),
  capacity: z.number().int().positive().optional(),
  tags: z.array(z.string().max(50)).max(10).optional(),
  status: z.enum(["draft", "published", "cancelled", "completed"]).optional(),
});

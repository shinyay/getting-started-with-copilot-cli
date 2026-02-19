/**
 * Event routes — HTTP layer.
 *
 * CONVENTION: Routes translate HTTP → service calls → HTTP responses.
 * No business logic here. Use respondSuccess/respondError for all responses.
 */

import { Router, Request, Response, NextFunction } from "express";
import { createEvent, getEvent, updateEvent, deleteEvent, listEvents, registerAttendee } from "../services/eventService";
import { respondSuccess, respondPaginated, respondError } from "../utils/response";
import { AppError } from "../utils/errors";
import { logger } from "../utils/logger";

const router = Router();

router.post("/", (req: Request, res: Response, next: NextFunction) => {
  try {
    const organizerId = req.headers["x-user-id"] as string || "anonymous";
    const event = createEvent(req.body, organizerId);
    res.status(201).json(respondSuccess(event));
  } catch (err) {
    next(err);
  }
});

router.get("/:id", (req: Request, res: Response, next: NextFunction) => {
  try {
    const event = getEvent(req.params.id);
    res.json(respondSuccess(event));
  } catch (err) {
    next(err);
  }
});

router.put("/:id", (req: Request, res: Response, next: NextFunction) => {
  try {
    const requesterId = req.headers["x-user-id"] as string || "anonymous";
    const event = updateEvent(req.params.id, req.body, requesterId);
    res.json(respondSuccess(event));
  } catch (err) {
    next(err);
  }
});

router.delete("/:id", (req: Request, res: Response, next: NextFunction) => {
  try {
    const requesterId = req.headers["x-user-id"] as string || "anonymous";
    deleteEvent(req.params.id, requesterId);
    res.status(204).send();
  } catch (err) {
    next(err);
  }
});

router.get("/", (req: Request, res: Response, next: NextFunction) => {
  try {
    const page = parseInt(req.query.page as string) || 1;
    const pageSize = parseInt(req.query.pageSize as string) || 20;
    const filter = {
      status: req.query.status as string | undefined,
      organizerId: req.query.organizerId as string | undefined,
      tag: req.query.tag as string | undefined,
      fromDate: req.query.fromDate as string | undefined,
      toDate: req.query.toDate as string | undefined,
    };
    const result = listEvents(filter as any, { page, pageSize });
    res.json(respondPaginated(result.events, page, pageSize, result.total));
  } catch (err) {
    next(err);
  }
});

router.post("/:id/register", (req: Request, res: Response, next: NextFunction) => {
  try {
    const attendeeId = req.headers["x-user-id"] as string || "anonymous";
    const event = registerAttendee(req.params.id, attendeeId);
    res.json(respondSuccess(event));
  } catch (err) {
    next(err);
  }
});

export default router;

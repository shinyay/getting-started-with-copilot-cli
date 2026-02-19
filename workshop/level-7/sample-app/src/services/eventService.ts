/**
 * Event service — business logic layer.
 *
 * CONVENTION: Services contain business logic only. No HTTP concepts
 * (req, res, status codes). Throw AppError for error cases.
 */

import { v4 as uuidv4 } from "uuid";
import { Event, CreateEventInput, UpdateEventInput, EventFilter, PaginationParams } from "../models/event";
import { AppError } from "../utils/errors";
import { logger } from "../utils/logger";

// In-memory store (replace with database in production)
const events: Map<string, Event> = new Map();

export function createEvent(input: CreateEventInput, organizerId: string): Event {
  logger.info("Creating event", { title: input.title, organizerId });

  if (input.capacity < 1) {
    throw AppError.badRequest("Capacity must be at least 1", "INVALID_CAPACITY");
  }

  const now = new Date().toISOString();
  const event: Event = {
    id: uuidv4(),
    title: input.title,
    description: input.description,
    date: input.date,
    location: input.location,
    capacity: input.capacity,
    attendees: [],
    organizerId,
    tags: input.tags ?? [],
    status: "draft",
    createdAt: now,
    updatedAt: now,
  };

  events.set(event.id, event);
  logger.info("Event created", { eventId: event.id });
  return event;
}

export function getEvent(id: string): Event {
  const event = events.get(id);
  if (!event) {
    throw AppError.notFound(`Event not found: ${id}`, "EVENT_NOT_FOUND");
  }
  return event;
}

export function updateEvent(id: string, input: UpdateEventInput, requesterId: string): Event {
  const event = getEvent(id);

  if (event.organizerId !== requesterId) {
    throw AppError.unauthorized("Only the organizer can update this event");
  }

  if (input.capacity !== undefined && input.capacity < event.attendees.length) {
    throw AppError.badRequest(
      `Cannot reduce capacity below current attendee count (${event.attendees.length})`,
      "CAPACITY_BELOW_ATTENDEES"
    );
  }

  const updated: Event = {
    ...event,
    ...input,
    updatedAt: new Date().toISOString(),
  };

  events.set(id, updated);
  logger.info("Event updated", { eventId: id });
  return updated;
}

export function deleteEvent(id: string, requesterId: string): void {
  const event = getEvent(id);

  if (event.organizerId !== requesterId) {
    throw AppError.unauthorized("Only the organizer can delete this event");
  }

  events.delete(id);
  logger.info("Event deleted", { eventId: id });
}

export function listEvents(
  filter: EventFilter,
  pagination: PaginationParams
): { events: Event[]; total: number } {
  let results = Array.from(events.values());

  if (filter.status) {
    results = results.filter((e) => e.status === filter.status);
  }
  if (filter.organizerId) {
    results = results.filter((e) => e.organizerId === filter.organizerId);
  }
  if (filter.tag) {
    results = results.filter((e) => e.tags.includes(filter.tag!));
  }
  if (filter.fromDate) {
    results = results.filter((e) => e.date >= filter.fromDate!);
  }
  if (filter.toDate) {
    results = results.filter((e) => e.date <= filter.toDate!);
  }

  const total = results.length;
  const start = (pagination.page - 1) * pagination.pageSize;
  const paged = results.slice(start, start + pagination.pageSize);

  return { events: paged, total };
}

export function registerAttendee(eventId: string, attendeeId: string): Event {
  const event = getEvent(eventId);

  if (event.status !== "published") {
    throw AppError.badRequest("Can only register for published events", "EVENT_NOT_PUBLISHED");
  }

  if (event.attendees.length >= event.capacity) {
    throw AppError.conflict("Event is at full capacity", "EVENT_FULL");
  }

  if (event.attendees.includes(attendeeId)) {
    throw AppError.conflict("Already registered for this event", "ALREADY_REGISTERED");
  }

  event.attendees.push(attendeeId);
  event.updatedAt = new Date().toISOString();
  events.set(eventId, event);

  logger.info("Attendee registered", { eventId, attendeeId });
  return event;
}

/** Clear all events (for testing). */
export function _clearAll(): void {
  events.clear();
}

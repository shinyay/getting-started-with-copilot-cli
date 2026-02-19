/**
 * Tests for eventService.
 *
 * CONVENTION: Use describe/it blocks (not test()). Group by function.
 * Use beforeEach to reset state.
 */

import {
  createEvent,
  getEvent,
  updateEvent,
  deleteEvent,
  listEvents,
  registerAttendee,
  _clearAll,
} from "../src/services/eventService";
import { AppError } from "../src/utils/errors";
import { CreateEventInput } from "../src/models/event";

const sampleInput: CreateEventInput = {
  title: "TypeScript Workshop",
  description: "Learn TypeScript from scratch",
  date: "2026-03-15T10:00:00Z",
  location: "Online",
  capacity: 50,
  tags: ["typescript", "workshop"],
};

describe("eventService", () => {
  beforeEach(() => {
    _clearAll();
  });

  describe("createEvent", () => {
    it("should create an event with generated ID", () => {
      const event = createEvent(sampleInput, "user-1");
      expect(event.id).toBeDefined();
      expect(event.title).toBe("TypeScript Workshop");
      expect(event.organizerId).toBe("user-1");
      expect(event.status).toBe("draft");
    });

    it("should reject capacity less than 1", () => {
      expect(() =>
        createEvent({ ...sampleInput, capacity: 0 }, "user-1")
      ).toThrow(AppError);
    });
  });

  describe("getEvent", () => {
    it("should return existing event", () => {
      const created = createEvent(sampleInput, "user-1");
      const found = getEvent(created.id);
      expect(found.id).toBe(created.id);
    });

    it("should throw for non-existent event", () => {
      expect(() => getEvent("nonexistent")).toThrow(AppError);
    });
  });

  describe("updateEvent", () => {
    it("should update event fields", () => {
      const event = createEvent(sampleInput, "user-1");
      const updated = updateEvent(event.id, { title: "New Title" }, "user-1");
      expect(updated.title).toBe("New Title");
    });

    it("should reject update from non-organizer", () => {
      const event = createEvent(sampleInput, "user-1");
      expect(() =>
        updateEvent(event.id, { title: "Hacked" }, "user-2")
      ).toThrow(AppError);
    });
  });

  describe("deleteEvent", () => {
    it("should delete event", () => {
      const event = createEvent(sampleInput, "user-1");
      deleteEvent(event.id, "user-1");
      expect(() => getEvent(event.id)).toThrow(AppError);
    });
  });

  describe("registerAttendee", () => {
    it("should register attendee for published event", () => {
      const event = createEvent(sampleInput, "user-1");
      updateEvent(event.id, { status: "published" }, "user-1");
      const updated = registerAttendee(event.id, "attendee-1");
      expect(updated.attendees).toContain("attendee-1");
    });

    it("should reject registration for draft event", () => {
      const event = createEvent(sampleInput, "user-1");
      expect(() =>
        registerAttendee(event.id, "attendee-1")
      ).toThrow(AppError);
    });

    it("should reject when at capacity", () => {
      const event = createEvent({ ...sampleInput, capacity: 1 }, "user-1");
      updateEvent(event.id, { status: "published" }, "user-1");
      registerAttendee(event.id, "attendee-1");
      expect(() =>
        registerAttendee(event.id, "attendee-2")
      ).toThrow(AppError);
    });
  });

  describe("listEvents", () => {
    it("should return paginated results", () => {
      for (let i = 0; i < 5; i++) {
        createEvent({ ...sampleInput, title: `Event ${i}` }, "user-1");
      }
      const result = listEvents({}, { page: 1, pageSize: 3 });
      expect(result.events).toHaveLength(3);
      expect(result.total).toBe(5);
    });
  });
});

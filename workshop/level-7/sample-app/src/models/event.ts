/**
 * Domain models and TypeScript interfaces.
 *
 * CONVENTION: Use 'interface' for data shapes, 'type' for unions/aliases.
 * All IDs are UUIDs (string type). Use branded types for safety where needed.
 */

export interface Event {
  id: string;
  title: string;
  description: string;
  date: string;           // ISO 8601
  location: string;
  capacity: number;
  attendees: string[];    // array of attendee IDs
  organizerId: string;
  tags: string[];
  status: EventStatus;
  createdAt: string;      // ISO 8601
  updatedAt: string;      // ISO 8601
}

export type EventStatus = "draft" | "published" | "cancelled" | "completed";

export interface CreateEventInput {
  title: string;
  description: string;
  date: string;
  location: string;
  capacity: number;
  tags?: string[];
}

export interface UpdateEventInput {
  title?: string;
  description?: string;
  date?: string;
  location?: string;
  capacity?: number;
  tags?: string[];
  status?: EventStatus;
}

export interface EventFilter {
  status?: EventStatus;
  organizerId?: string;
  tag?: string;
  fromDate?: string;
  toDate?: string;
}

export interface PaginationParams {
  page: number;
  pageSize: number;
}

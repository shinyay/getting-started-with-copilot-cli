/**
 * Standard API response wrapper.
 *
 * CONVENTION: All API endpoints must return responses wrapped in ApiResponse<T>.
 * Never return raw data — always use respondSuccess() or respondError().
 */
export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: {
    code: string;
    message: string;
  };
  meta?: {
    page?: number;
    pageSize?: number;
    total?: number;
    timestamp: string;
  };
}

export function respondSuccess<T>(data: T, meta?: Partial<ApiResponse<T>["meta"]>): ApiResponse<T> {
  return {
    success: true,
    data,
    meta: {
      ...meta,
      timestamp: new Date().toISOString(),
    },
  };
}

export function respondError(code: string, message: string): ApiResponse<never> {
  return {
    success: false,
    error: { code, message },
    meta: {
      timestamp: new Date().toISOString(),
    },
  };
}

export function respondPaginated<T>(
  data: T[],
  page: number,
  pageSize: number,
  total: number
): ApiResponse<T[]> {
  return {
    success: true,
    data,
    meta: {
      page,
      pageSize,
      total,
      timestamp: new Date().toISOString(),
    },
  };
}

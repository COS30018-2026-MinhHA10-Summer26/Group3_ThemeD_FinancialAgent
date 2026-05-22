import axios, { AxiosError, type AxiosInstance } from "axios";

const backendBaseUrl = process.env.NEXT_PUBLIC_BACKEND_URL;

type ApiErrorBody = {
  detail?: string;
};

export function createApiClient(accessToken?: string | null): AxiosInstance {
  const client = axios.create({
    baseURL: backendBaseUrl,
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (accessToken) {
    client.defaults.headers.common.Authorization = `Bearer ${accessToken}`;
  }

  return client;
}

export const apiClient = createApiClient();

export function getApiErrorMessage(error: unknown, fallback = "Request failed"): string {
  if (axios.isAxiosError(error)) {
    const axiosError = error as AxiosError<ApiErrorBody>;
    return axiosError.response?.data?.detail || axiosError.message || fallback;
  }

  if (error instanceof Error) {
    return error.message;
  }

  return fallback;
}
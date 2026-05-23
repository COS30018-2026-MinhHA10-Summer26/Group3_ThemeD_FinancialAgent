"use client";

import { FormEvent, useEffect, useMemo, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import { createApiClient, getApiErrorMessage } from "@/lib/api";

type RoleName = "Admin" | "User" | string;

type TokenPayload = {
  sub?: string;
  id?: string;
  role?: RoleName;
};

type ConversationCreator = {
  user_id: string;
  email: string;
  role_name: string;
};

type ConversationRow = {
  conversation_id: string;
  project_id: string;
  title: string;
  creator?: ConversationCreator | null;
  created_at?: string | null;
  updated_at?: string | null;
};

type ProjectRow = {
  project_id: string;
  name: string;
  description?: string | null;
};

function decodeToken(token: string): TokenPayload | null {
  try {
    const [, payload] = token.split(".");
    if (!payload) return null;
    const normalized = payload.replace(/-/g, "+").replace(/_/g, "/");
    const padded = normalized + "=".repeat((4 - (normalized.length % 4)) % 4);
    return JSON.parse(atob(padded)) as TokenPayload;
  } catch {
    return null;
  }
}

export default function ProjectChatPage() {
  const router = useRouter();
  const params = useParams<{ projectId: string | string[]; conversationId: string | string[] }>();
  const { data: session, status } = useSession();
  const projectId = Array.isArray(params.projectId) ? params.projectId[0] : params.projectId;
  const conversationId = Array.isArray(params.conversationId) ? params.conversationId[0] : params.conversationId;

  const [currentRole, setCurrentRole] = useState<RoleName | null>(null);
  const [currentEmail, setCurrentEmail] = useState<string>("");
  const [project, setProject] = useState<ProjectRow | null>(null);
  const [conversation, setConversation] = useState<ConversationRow | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [query, setQuery] = useState("");

  useEffect(() => {
    if (status === "loading") {
      return;
    }

    const token = localStorage.getItem("access_token");
    const sessionToken = (session as { backendToken?: string } | null)?.backendToken;

    if (!token && !sessionToken && status !== "authenticated") {
      router.push("/login");
      return;
    }

    const payload = token ? decodeToken(token) : null;
    const sessionRole = (session as { role?: string } | null)?.role;

    if (!payload?.role && !sessionRole && status !== "authenticated") {
      router.push("/login");
      return;
    }

    const effectiveRole = payload?.role ?? sessionRole;
    const effectiveEmail = payload?.sub ?? session?.user?.email ?? "";

    if (effectiveRole) {
      setCurrentRole(effectiveRole);
    }

    setCurrentEmail(effectiveEmail);

    if (sessionToken && !token) {
      localStorage.setItem("access_token", sessionToken);
    }
  }, [router, session, status]);

  useEffect(() => {
    if (!projectId || !conversationId) return;

    const authToken = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!authToken || !currentRole) return;

    let cancelled = false;

    async function loadChatContext() {
      setLoading(true);
      setError(null);

      try {
        const api = createApiClient(authToken);
        const [projectResponse, conversationsResponse] = await Promise.all([
          api.get<ProjectRow>(`/projects/${projectId}`),
          api.get<ConversationRow[]>(`/projects/${projectId}/conversations`),
        ]);

        if (cancelled) return;

        setProject(projectResponse.data);
        setConversation(conversationsResponse.data.find((row) => row.conversation_id === conversationId) ?? null);
      } catch (loadError) {
        if (cancelled) return;
        setError(getApiErrorMessage(loadError, "Failed to load chat context"));
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    loadChatContext();

    return () => {
      cancelled = true;
    };
  }, [currentRole, conversationId, projectId, session]);

  const title = useMemo(() => conversation?.title || "Chat", [conversation]);

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
  }

  return (
    <section className="mx-auto flex min-h-[calc(100vh-6rem)] max-w-7xl flex-col px-6 py-10 sm:px-10 lg:px-12">
      <div className="mb-6 flex items-center justify-between gap-4">
        <div>
          <button
            type="button"
            onClick={() => router.push(`/project/${projectId}`)}
            className="text-sm font-medium text-slate-500 transition hover:text-slate-800"
          >
            Back to project
          </button>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight">{title}</h1>
          <p className="mt-2 text-slate-600">
            Conversation <span className="font-medium text-slate-900">{conversationId}</span>
          </p>
        </div>
        <div className="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-600 shadow-sm">
          RAG chat placeholder
        </div>
      </div>

      {error ? (
        <div className="mb-6 rounded-2xl border border-rose-200 bg-rose-50 px-4 py-3 text-sm text-rose-700">
          {error}
        </div>
      ) : null}

      <div className="grid flex-1 gap-6 lg:grid-cols-[1fr_0.95fr]">
        <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
          <div className="mb-4">
            <p className="text-sm font-medium uppercase tracking-[0.2em] text-slate-500">Chat</p>
            <h2 className="mt-2 text-2xl font-semibold tracking-tight">Ask the RAG model</h2>
            <p className="mt-2 text-sm text-slate-500">
              This page is ready for conversation flow. Query submission is disabled for now.
            </p>
          </div>

          <div className="flex min-h-[28rem] flex-col justify-between rounded-3xl border border-slate-200 bg-slate-50 p-5">
            <div className="space-y-4">
              <div className="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-500">
                No messages yet.
              </div>
              {loading ? (
                <div className="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-500">
                  Loading chat context...
                </div>
              ) : null}
            </div>

            <form onSubmit={handleSubmit} className="mt-6 grid gap-3">
              <textarea
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                className="min-h-32 rounded-2xl border border-slate-200 bg-white px-4 py-3 outline-none focus:border-slate-400"
                placeholder="Type your question here..."
              />
              <div className="flex items-center justify-between gap-3">
                <p className="text-sm text-slate-500">Submit is a placeholder for the next step.</p>
                <button
                  type="submit"
                  className="rounded-full bg-slate-900 px-5 py-2.5 text-sm font-medium text-white hover:bg-slate-800"
                >
                  Send
                </button>
              </div>
            </form>
          </div>
        </div>

        <div className="space-y-6">
          <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
            <p className="text-sm font-medium uppercase tracking-[0.2em] text-slate-500">Project info</p>
            <div className="mt-3 space-y-2 text-sm text-slate-600">
              <div>
                <span className="font-medium text-slate-900">Project:</span> {project?.name || "Loading..."}
              </div>
              <div>
                <span className="font-medium text-slate-900">Conversation creator:</span>{" "}
                {conversation?.creator?.email || "Unknown"}
              </div>
              <div>
                <span className="font-medium text-slate-900">Creator role:</span>{" "}
                {conversation?.creator?.role_name || "Unknown"}
              </div>
            </div>
          </div>

          <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
            <p className="text-sm font-medium uppercase tracking-[0.2em] text-slate-500">RAG model</p>
            <h3 className="mt-2 text-xl font-semibold">Planned flow</h3>
            <ul className="mt-4 space-y-3 text-sm text-slate-600">
              <li className="rounded-2xl border border-slate-200 px-4 py-3">1. User opens a conversation inside a project.</li>
              <li className="rounded-2xl border border-slate-200 px-4 py-3">2. Messages will later go to the RAG pipeline.</li>
              <li className="rounded-2xl border border-slate-200 px-4 py-3">3. For now, submission is intentionally inert.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}

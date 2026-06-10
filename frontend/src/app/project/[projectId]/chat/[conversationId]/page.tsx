"use client";

import { ChangeEvent, FormEvent, useEffect, useMemo, useRef, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import { createApiClient, getApiErrorMessage } from "@/lib/api";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

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

type MessageRow = {
  message_id: string;
  conversation_id: string;
  content: string;
  created_at?: string | null;
  role: "user" | "assistant" | "system" | string;
};

type ChatResponse = {
  answer: string;
  query_variations: string[];
  sources: Array<Record<string, unknown>>;
  user_message: {
    message_id: string;
    conversation_id: string;
    role: string;
    content: string;
    created_at?: string | null;
  };
  assistant_message: {
    message_id: string;
    conversation_id: string;
    role: string;
    content: string;
    created_at?: string | null;
  };
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
  const [messages, setMessages] = useState<MessageRow[]>([]);
  const [loading, setLoading] = useState(true);
  const [sending, setSending] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [query, setQuery] = useState("");
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const [selectedPdf, setSelectedPdf] = useState<File | null>(null);
  const messagesRef = useRef<HTMLDivElement | null>(null);
  const fileInputRef = useRef<HTMLInputElement | null>(null);
  const pdfInputRef = useRef<HTMLInputElement | null>(null);

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
        const [projectResponse, conversationsResponse, messagesResponse] = await Promise.all([
          api.get<ProjectRow>(`/projects/${projectId}`),
          api.get<ConversationRow[]>(`/projects/${projectId}/conversations`),
          api.get<
            Array<{
              message_id: string;
              conversation_id: string;
              content: string;
              created_at?: string | null;
              role?: string;
            }>
          >(`/projects/${projectId}/conversations/${conversationId}/messages`),
        ]);

        if (cancelled) return;

        setProject(projectResponse.data);
        setConversation(conversationsResponse.data.find((row) => row.conversation_id === conversationId) ?? null);
        setMessages(
          messagesResponse.data.map((message) => ({
            ...message,
            role: message.role ?? "assistant",
          })),
        );
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

  useEffect(() => {
    if (messagesRef.current) {
      messagesRef.current.scrollTop = messagesRef.current.scrollHeight;
    }
  }, [messages]);

  const title = useMemo(() => conversation?.title || "Chat", [conversation]);

  function handleImageSelect(event: ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0];
    if (!file) return;

    const allowed = ["image/png", "image/jpeg", "image/gif", "image/webp"];
    if (!allowed.includes(file.type)) {
      setError("Unsupported image type. Allowed: PNG, JPEG, GIF, WebP");
      return;
    }
    if (file.size > 10 * 1024 * 1024) {
      setError("Image too large (max 10MB)");
      return;
    }

    setSelectedImage(file);
    setImagePreview(URL.createObjectURL(file));
    setError(null);
  }

  function removeImage() {
    setSelectedImage(null);
    if (imagePreview) URL.revokeObjectURL(imagePreview);
    setImagePreview(null);
    if (fileInputRef.current) fileInputRef.current.value = "";
  }

  function handlePdfSelect(event: ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0];
    if (!file) return;

    if (file.type !== "application/pdf" && !file.name.toLowerCase().endsWith(".pdf")) {
      setError("Only PDF files are supported.");
      return;
    }
    if (file.size > 5 * 1024 * 1024) {
      setError("PDF too large (max 5MB)");
      return;
    }

    setSelectedPdf(file);
    setError(null);
  }

  function removePdf() {
    setSelectedPdf(null);
    if (pdfInputRef.current) pdfInputRef.current.value = "";
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const prompt = query.trim();
    if (!prompt || sending || !projectId || !conversationId) return;

    const authToken = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!authToken) return;

    const api = createApiClient(authToken);
    setSending(true);
    setError(null);

    const formData = new FormData();
    formData.append("query", prompt);
    if (selectedImage) {
      formData.append("image", selectedImage);
    }
    if (selectedPdf) {
      formData.append("pdf", selectedPdf);
    }

    api
      .post<ChatResponse>(
        `/projects/${projectId}/conversations/${conversationId}/messages`,
        formData,
        { headers: { "Content-Type": "multipart/form-data" } },
      )
      .then((response) => {
        setMessages((currentMessages) => [
          ...currentMessages,
          { ...response.data.user_message },
          { ...response.data.assistant_message },
        ]);
        setQuery("");
        removeImage();
        removePdf();
      })
      .catch((sendError) => {
        setError(getApiErrorMessage(sendError, "Failed to send message"));
      })
      .finally(() => {
        setSending(false);
      });
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

          <div className="flex h-[calc(150vh-22rem)] max-h-[42rem] min-h-[28rem] flex-col rounded-3xl border border-slate-200 bg-slate-50 p-5">
            <div ref={messagesRef} className="min-h-0 flex-1 space-y-4 overflow-y-auto pr-2">
              {messages.length === 0 && !loading ? (
                <div className="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-500">
                  No messages yet.
                </div>
              ) : null}
              {messages.map((message) => (
                <div
                  key={message.message_id}
                  className={`max-w-[85%] rounded-2xl px-4 py-3 text-sm shadow-sm ${message.role === "user"
                    ? "ml-auto border border-slate-900 bg-slate-900 text-white"
                    : "border border-slate-200 bg-white text-slate-700"
                    }`}
                >
                  <div className="prose prose-sm max-w-none [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:mb-3 [&_p+p]:mt-0 [&_table]:my-4 [&_table]:w-full [&_table]:border-collapse [&_table]:overflow-hidden [&_table]:rounded-xl [&_table]:border [&_table]:border-slate-200 [&_th]:border [&_th]:border-slate-200 [&_th]:bg-slate-100 [&_th]:px-3 [&_th]:py-2 [&_th]:text-left [&_th]:font-semibold [&_td]:border [&_td]:border-slate-200 [&_td]:px-3 [&_td]:py-2 [&_tr:nth-child(even)]:bg-slate-50">
                    <ReactMarkdown remarkPlugins={[remarkGfm]}>
                      {message.content}
                    </ReactMarkdown>
                  </div>
                </div>
              ))}
              {loading ? (
                <div className="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-500">
                  Loading chat context...
                </div>
              ) : null}
            </div>

            {/* Auto-scroll to bottom when messages change */}


            <form onSubmit={handleSubmit} className="mt-6 grid gap-3">
              {/* Hidden file input */}
              <input
                ref={fileInputRef}
                type="file"
                accept="image/png,image/jpeg,image/gif,image/webp"
                onChange={handleImageSelect}
                className="hidden"
                id="chat-image-upload"
              />
              <input
                ref={pdfInputRef}
                type="file"
                accept=".pdf,application/pdf"
                onChange={handlePdfSelect}
                className="hidden"
                id="chat-pdf-upload"
              />

              {/* Image preview */}
              {imagePreview ? (
                <div className="flex items-start gap-3 rounded-2xl border border-slate-200 bg-white px-4 py-3">
                  <img
                    src={imagePreview}
                    alt="Upload preview"
                    className="h-20 w-20 rounded-xl border border-slate-200 object-cover"
                  />
                  <div className="flex flex-col gap-1">
                    <p className="text-sm font-medium text-slate-700 truncate max-w-[200px]">
                      {selectedImage?.name}
                    </p>
                    <p className="text-xs text-slate-400">
                      {selectedImage ? `${(selectedImage.size / 1024).toFixed(1)} KB` : ""}
                    </p>
                    <button
                      type="button"
                      onClick={removeImage}
                      className="mt-1 self-start rounded-lg bg-rose-50 px-2.5 py-1 text-xs font-medium text-rose-600 transition hover:bg-rose-100"
                    >
                      Remove
                    </button>
                  </div>
                </div>
              ) : null}

              {/* PDF preview */}
              {selectedPdf ? (
                <div className="flex items-start gap-3 rounded-2xl border border-slate-200 bg-white px-4 py-3">
                  <div className="flex h-12 w-12 items-center justify-center rounded-xl border border-rose-200 bg-rose-50">
                    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" className="text-rose-500">
                      <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                      <polyline points="14 2 14 8 20 8" />
                      <path d="M10 13v-1h4v1" />
                      <path d="M10 17v-1h4v1" />
                    </svg>
                  </div>
                  <div className="flex flex-col gap-1">
                    <p className="text-sm font-medium text-slate-700 truncate max-w-[200px]">
                      {selectedPdf.name}
                    </p>
                    <p className="text-xs text-slate-400">
                      {(selectedPdf.size / 1024).toFixed(1)} KB
                    </p>
                    <button
                      type="button"
                      onClick={removePdf}
                      className="mt-1 self-start rounded-lg bg-rose-50 px-2.5 py-1 text-xs font-medium text-rose-600 transition hover:bg-rose-100"
                    >
                      Remove
                    </button>
                  </div>
                </div>
              ) : null}

              <textarea
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                className="min-h-32 rounded-2xl border border-slate-200 bg-white px-4 py-3 outline-none focus:border-slate-400"
                placeholder="Type your question here..."
                disabled={sending}
              />
              <div className="flex items-center justify-between gap-3">
                <p className="text-sm text-slate-500">Messages are scoped to this project and conversation.</p>
                <div className="flex items-center gap-2">
                  <button
                    type="button"
                    onClick={() => fileInputRef.current?.click()}
                    disabled={sending}
                    className="flex items-center gap-1.5 rounded-full border border-slate-200 bg-white px-4 py-2.5 text-sm font-medium text-slate-600 transition hover:border-slate-300 hover:bg-slate-50 disabled:cursor-not-allowed disabled:opacity-50"
                    title="Attach image"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />
                      <circle cx="9" cy="9" r="2" />
                      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
                    </svg>
                    Image
                  </button>
                  <button
                    type="button"
                    onClick={() => pdfInputRef.current?.click()}
                    disabled={sending}
                    className="flex items-center gap-1.5 rounded-full border border-slate-200 bg-white px-4 py-2.5 text-sm font-medium text-slate-600 transition hover:border-slate-300 hover:bg-slate-50 disabled:cursor-not-allowed disabled:opacity-50"
                    title="Attach PDF"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                      <polyline points="14 2 14 8 20 8" />
                    </svg>
                    PDF
                  </button>
                  <button
                    type="submit"
                    disabled={sending}
                    className="rounded-full bg-slate-900 px-5 py-2.5 text-sm font-medium text-white hover:bg-slate-800 disabled:cursor-not-allowed disabled:bg-slate-400"
                  >
                    {sending ? (selectedPdf ? "Processing PDF..." : "Sending...") : "Send"}
                  </button>
                </div>
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

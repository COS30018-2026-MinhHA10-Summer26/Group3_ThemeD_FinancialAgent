"use client";

/* eslint-disable react-hooks/set-state-in-effect */

import { ChangeEvent, ComponentProps, FormEvent, useEffect, useMemo, useRef, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import { createApiClient, getApiErrorMessage } from "@/lib/api";
import { readPageCache, writePageCache } from "@/lib/page-cache";
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
  agent_run_log?: AgentRunLog | null;
};

type AgentRunLog = {
  route?: string | null;
  workflow_steps?: string[];
  executed_agents?: string[];
  evaluator_verdict?: string | null;
  errors?: string[];
};

type ChatResponse = {
  answer: string;
  query_variations: string[];
  sources: Array<Record<string, unknown>>;
  agent_run_log?: AgentRunLog | null;
  user_message: {
    message_id: string;
    conversation_id: string;
    role: string;
    content: string;
    agent_run_log?: AgentRunLog | null;
    created_at?: string | null;
  };
  assistant_message: {
    message_id: string;
    conversation_id: string;
    role: string;
    content: string;
    agent_run_log?: AgentRunLog | null;
    created_at?: string | null;
  };
};

type MarkdownTableProps = ComponentProps<"table">;

const markdownComponents = {
  table: ({ children, className, ...props }: MarkdownTableProps) => (
    <div className="my-4 w-full overflow-x-auto rounded-xl border border-slate-200">
      <table
        {...props}
        className={`min-w-[520px] w-full border-collapse ${className ?? ""}`.trim()}
      >
        {children}
      </table>
    </div>
  ),
};

function normalizeAssistantMarkdown(content: string): string {
  const trimmed = content.trim();
  const fencedMarkdownMatch = trimmed.match(/^```(?:markdown|md)?\s*\n([\s\S]*?)\n```$/i);
  if (fencedMarkdownMatch?.[1]) {
    return fencedMarkdownMatch[1].trim();
  }
  return content;
}

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

/* ──────────────────────────────────────────── */
/*  Typing dots animation for assistant        */
/* ──────────────────────────────────────────── */
function AgentProgressIndicator({ message }: { message: string }) {
  return (
    <div className="chat-bubble-assistant animate-chat-fade-in">
      <div className="flex items-center gap-1.5 px-1 py-1">
        <span className="typing-dot" style={{ animationDelay: "0ms" }} />
        <span className="typing-dot" style={{ animationDelay: "150ms" }} />
        <span className="typing-dot" style={{ animationDelay: "300ms" }} />
        <span className="ml-2 text-xs text-slate-400">{message}</span>
      </div>
    </div>
  );
}

function AgentTracePanel({ log }: { log: AgentRunLog }) {
  const [expanded, setExpanded] = useState(false);
  const workflowSteps = log.workflow_steps ?? [];
  const evaluatorLabel =
    log.evaluator_verdict === "FAIL" ? "STILL INCOMPLETE" : log.evaluator_verdict;

  return (
    <div className="mt-3 border-t border-slate-100 pt-2">
      <button
        type="button"
        onClick={() => setExpanded((current) => !current)}
        className="text-xs text-slate-400 transition hover:text-slate-600"
      >
        {expanded ? "▼" : "▶"} Agent Trace ({log.route ?? "workflow"} • {workflowSteps.length} steps)
      </button>
      {expanded ? (
        <div className="mt-2 space-y-1 font-mono text-xs text-slate-500">
          {workflowSteps.map((step, index) => (
            <div key={`${step}-${index}`} className="flex gap-2">
              <span className="text-slate-300">{index + 1}.</span>
              <span>{step}</span>
            </div>
          ))}
          {log.evaluator_verdict ? (
            <div className={`mt-2 font-semibold ${log.evaluator_verdict === "PASS" ? "text-emerald-500" : "text-amber-500"}`}>
              Evaluator: {evaluatorLabel}
            </div>
          ) : null}
          {log.errors?.length ? (
            <div className="mt-2 text-amber-600">Pipeline notes: {log.errors.join("; ")}</div>
          ) : null}
        </div>
      ) : null}
    </div>
  );
}

const CHAT_CACHE_PREFIX = "project-chat";

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
  const [progressMessage, setProgressMessage] = useState("Đang chuẩn bị yêu cầu...");
  const [error, setError] = useState<string | null>(null);
  const [query, setQuery] = useState("");
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const [selectedPdf, setSelectedPdf] = useState<File | null>(null);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const messagesRef = useRef<HTMLDivElement | null>(null);
  const fileInputRef = useRef<HTMLInputElement | null>(null);
  const pdfInputRef = useRef<HTMLInputElement | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement | null>(null);

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
    const cacheKey = `${CHAT_CACHE_PREFIX}:${projectId}:${conversationId}`;
    const cachedPage = readPageCache<{
      project: ProjectRow | null;
      conversation: ConversationRow | null;
      messages: MessageRow[];
      currentRole: RoleName | null;
      currentEmail: string;
    }>(cacheKey);

    if (cachedPage) {
      setProject(cachedPage.project);
      setConversation(cachedPage.conversation);
      setMessages(cachedPage.messages);
      setCurrentRole(cachedPage.currentRole);
      setCurrentEmail(cachedPage.currentEmail);
      setLoading(false);
    } else {
      setLoading(true);
    }

    async function loadChatContext() {
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
              agent_run_log?: AgentRunLog | null;
            }>
          >(`/projects/${projectId}/conversations/${conversationId}/messages`),
        ]);

        if (cancelled) return;

        setProject(projectResponse.data);
        const nextConversation = conversationsResponse.data.find((row) => row.conversation_id === conversationId) ?? null;
        const nextMessages =
          messagesResponse.data.map((message) => ({
            ...message,
            role: message.role ?? "assistant",
          }));

        setConversation(nextConversation);
        setMessages(nextMessages);
        writePageCache(cacheKey, {
          project: projectResponse.data,
          conversation: nextConversation,
          messages: nextMessages,
          currentRole,
          currentEmail,
        });
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
  }, [currentRole, currentEmail, conversationId, projectId, session]);

  useEffect(() => {
    if (messagesRef.current) {
      messagesRef.current.scrollTop = messagesRef.current.scrollHeight;
    }
  }, [messages]);

  /* Auto-resize textarea */
  useEffect(() => {
    const textarea = textareaRef.current;
    if (!textarea) return;
    textarea.style.height = "auto";
    textarea.style.height = Math.min(textarea.scrollHeight, 200) + "px";
  }, [query]);

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

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const prompt = query.trim();
    if (!prompt || sending || !projectId || !conversationId) return;

    const authToken = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!authToken) return;

    setSending(true);
    setProgressMessage("Request is preparing...");
    setError(null);

    const formData = new FormData();
    formData.append("query", prompt);
    if (selectedImage) {
      formData.append("image", selectedImage);
    }
    if (selectedPdf) {
      formData.append("pdf", selectedPdf);
    }

    try {
      const backendUrl = (process.env.NEXT_PUBLIC_BACKEND_URL ?? "").replace(/\/$/, "");
      const response = await fetch(
        `${backendUrl}/projects/${projectId}/conversations/${conversationId}/messages/stream`,
        {
          method: "POST",
          body: formData,
          headers: { Authorization: `Bearer ${authToken}` },
        },
      );
      if (!response.ok || !response.body) {
        const detail = await response.text();
        throw new Error(detail || "Failed to start multi-agent chat");
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      let completed = false;

      const processEvent = (rawEvent: string) => {
        const lines = rawEvent.split("\n");
        const eventName = lines.find((line) => line.startsWith("event:"))?.slice(6).trim() ?? "message";
        const data = lines
          .filter((line) => line.startsWith("data:"))
          .map((line) => line.slice(5).trim())
          .join("\n");
        if (!data) return;

        const payload = JSON.parse(data) as ChatResponse | { step?: string; message?: string; detail?: string };
        if (eventName === "progress") {
          const rawMessage = (payload as { message?: string }).message ?? "Processing...";
          setProgressMessage(rawMessage.replace("Evaluator: FAIL", "Evaluator: STILL INCOMPLETE"));
        } else if (eventName === "done") {
          const chatResponse = payload as ChatResponse;
          setMessages((currentMessages) => [
            ...currentMessages,
            { ...chatResponse.user_message },
            { ...chatResponse.assistant_message },
          ]);
          setQuery("");
          removeImage();
          removePdf();
          completed = true;
        } else if (eventName === "error") {
          throw new Error((payload as { detail?: string }).detail ?? "Multi-agent chat failed");
        }
      };

      while (true) {
        const { done, value } = await reader.read();
        buffer += decoder.decode(value ?? new Uint8Array(), { stream: !done }).replace(/\r/g, "");
        let separatorIndex = buffer.indexOf("\n\n");
        while (separatorIndex >= 0) {
          processEvent(buffer.slice(0, separatorIndex));
          buffer = buffer.slice(separatorIndex + 2);
          separatorIndex = buffer.indexOf("\n\n");
        }
        if (done) break;
      }
      if (buffer.trim()) processEvent(buffer);
      if (!completed) throw new Error("The multi-agent response ended before completion");
    } catch (sendError) {
      setError(getApiErrorMessage(sendError, "Failed to send message"));
    } finally {
      setSending(false);
    }
  }

  function handleKeyDown(event: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      const form = event.currentTarget.closest("form");
      if (form) form.requestSubmit();
    }
  }

  const hasAttachments = !!imagePreview || !!selectedPdf;

  return (
    <>
      {/* ── Inline styles for animations ── */}
      <style>{`
        @keyframes chat-fade-in {
          from { opacity: 0; transform: translateY(12px); }
          to   { opacity: 1; transform: translateY(0); }
        }
        .animate-chat-fade-in {
          animation: chat-fade-in 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        @keyframes typing-bounce {
          0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
          30%            { transform: translateY(-6px); opacity: 1; }
        }
        .typing-dot {
          display: inline-block;
          width: 7px;
          height: 7px;
          border-radius: 50%;
          background: #94a3b8;
          animation: typing-bounce 1.2s ease-in-out infinite;
        }

        @keyframes shimmer {
          0%   { background-position: -200% 0; }
          100% { background-position: 200% 0; }
        }
        .chat-shimmer {
          background: linear-gradient(90deg, #f1f5f9 25%, #e2e8f0 50%, #f1f5f9 75%);
          background-size: 200% 100%;
          animation: shimmer 1.8s ease-in-out infinite;
        }

        @keyframes sidebar-slide {
          from { opacity: 0; transform: translateX(20px); }
          to   { opacity: 1; transform: translateX(0); }
        }
        .animate-sidebar-slide {
          animation: sidebar-slide 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        @keyframes pulse-ring {
          0%   { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.3); }
          70%  { box-shadow: 0 0 0 6px rgba(99, 102, 241, 0); }
          100% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0); }
        }

        .chat-input-focused {
          animation: pulse-ring 2s ease-out infinite;
        }

        /* Custom scrollbar */
        .chat-scroll::-webkit-scrollbar { width: 6px; }
        .chat-scroll::-webkit-scrollbar-track { background: transparent; }
        .chat-scroll::-webkit-scrollbar-thumb {
          background: #cbd5e1;
          border-radius: 999px;
        }
        .chat-scroll::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

        /* Message bubbles */
        .chat-bubble-user {
          background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
          color: white;
          border-radius: 20px 20px 6px 20px;
          padding: 14px 18px;
          max-width: 75%;
          margin-left: auto;
          box-shadow: 0 2px 12px rgba(99, 102, 241, 0.25);
        }

        .chat-bubble-assistant {
          background: white;
          color: #1e293b;
          border: 1px solid #e2e8f0;
          border-radius: 20px 20px 20px 6px;
          padding: 14px 18px;
          max-width: 75%;
          box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
        }

        .chat-bubble-user .prose { color: white; }
        .chat-bubble-user .prose strong { color: white; }
        .chat-bubble-user .prose a { color: #c7d2fe; }
        .chat-bubble-user .prose code { color: #e0e7ff; background: rgba(255,255,255,0.15); }

        .chat-bubble-assistant .prose { color: #334155; }

        /* Gradient mesh background for chat area */
        .chat-bg {
          background:
            radial-gradient(ellipse at 10% 20%, rgba(99, 102, 241, 0.04) 0%, transparent 50%),
            radial-gradient(ellipse at 90% 80%, rgba(139, 92, 246, 0.04) 0%, transparent 50%),
            #f8fafc;
        }
      `}</style>

      <section className="flex h-[calc(100vh-5rem)] flex-col">
        {/* ── Top bar ── */}
        <div className="flex items-center justify-between border-b border-slate-200 bg-white/80 px-6 py-3 backdrop-blur-md">
          <div className="flex items-center gap-4">
            <button
              type="button"
              onClick={() => router.push(`/project/${projectId}`)}
              className="group flex items-center gap-2 rounded-xl px-3 py-2 text-sm font-medium text-slate-500 transition hover:bg-slate-100 hover:text-slate-800"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="transition-transform group-hover:-translate-x-0.5">
                <path d="m15 18-6-6 6-6" />
              </svg>
              Back
            </button>
            <div className="h-5 w-px bg-slate-200" />
            <div className="flex items-center gap-3">
              <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-indigo-500 to-violet-500 shadow-sm">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                </svg>
              </div>
              <div>
                <h1 className="text-sm font-semibold tracking-tight text-slate-900">{title}</h1>
                <p className="text-xs text-slate-400">{project?.name || "Loading..."}</p>
              </div>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {/* Message count badge */}
            <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-500">
              {messages.length} messages
            </span>
            {/* Sidebar toggle */}
            <button
              type="button"
              onClick={() => setSidebarOpen(!sidebarOpen)}
              className={`flex items-center gap-2 rounded-xl border px-3 py-2 text-sm font-medium transition ${sidebarOpen
                  ? "border-indigo-200 bg-indigo-50 text-indigo-600"
                  : "border-slate-200 bg-white text-slate-500 hover:border-slate-300 hover:bg-slate-50"
                }`}
              title="Toggle project info"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="12" cy="12" r="10" />
                <path d="M12 16v-4" />
                <path d="M12 8h.01" />
              </svg>
              Info
            </button>
          </div>
        </div>

        {/* ── Error toast ── */}
        {error ? (
          <div className="mx-6 mt-3 animate-chat-fade-in rounded-xl border border-rose-200 bg-rose-50/80 px-4 py-3 text-sm text-rose-700 backdrop-blur-sm">
            <div className="flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="12" cy="12" r="10" />
                <path d="m15 9-6 6" />
                <path d="m9 9 6 6" />
              </svg>
              {error}
            </div>
          </div>
        ) : null}

        {/* ── Main content area ── */}
        <div className="flex min-h-0 flex-1">
          {/* ── Chat column (main) ── */}
          <div className="flex flex-1 flex-col">
            {/* Messages area */}
            <div
              ref={messagesRef}
              className="chat-bg chat-scroll flex-1 overflow-y-auto px-4 py-6 sm:px-8 lg:px-16 xl:px-24"
            >
              <div className="mx-auto w-[100%] max-w-none space-y-4">
                {/* Empty state */}
                {messages.length === 0 && !loading ? (
                  <div className="flex flex-col items-center justify-center py-20 animate-chat-fade-in">
                    <div className="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-indigo-100 to-violet-100">
                      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="url(#emptyGrad)" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                        <defs>
                          <linearGradient id="emptyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stopColor="#6366f1" />
                            <stop offset="100%" stopColor="#8b5cf6" />
                          </linearGradient>
                        </defs>
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                      </svg>
                    </div>
                    <h3 className="text-lg font-semibold text-slate-700">Start the conversation</h3>
                    <p className="mt-2 max-w-sm text-center text-sm text-slate-400">
                      Ask the RAG model anything about your project documents. Attach images or PDFs for richer analysis.
                    </p>
                  </div>
                ) : null}

                {/* Messages */}
                {messages.map((message, index) => {
                  const renderedContent =
                    message.role === "assistant"
                      ? normalizeAssistantMarkdown(message.content)
                      : message.content;

                  return (
                  <div
                    key={message.message_id}
                    className={`flex min-w-0 animate-chat-fade-in ${message.role === "user" ? "justify-end" : "justify-start"}`}
                    style={{ animationDelay: `${Math.min(index * 40, 400)}ms` }}
                  >
                    {message.role !== "user" ? (
                      <div className="mr-3 mt-1 flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-gradient-to-br from-indigo-500 to-violet-500">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                          <path d="M12 8V4H8" />
                          <rect width="16" height="12" x="4" y="8" rx="2" />
                          <path d="M2 14h2" />
                          <path d="M20 14h2" />
                          <path d="M15 13v2" />
                          <path d="M9 13v2" />
                        </svg>
                      </div>
                    ) : null}
                    <div className={`${message.role === "user" ? "chat-bubble-user" : "chat-bubble-assistant"} min-w-0 overflow-hidden`}>
                      <div className={`prose prose-sm max-w-none [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:mb-3 [&_p+p]:mt-0 [&_p]:break-words [&_li]:break-words [&_pre]:overflow-x-auto [&_pre]:rounded-xl [&_pre]:bg-slate-900 [&_pre]:p-3 [&_code]:break-words [&_th]:border [&_th]:border-slate-200 [&_th]:bg-slate-100 [&_th]:px-3 [&_th]:py-2 [&_th]:text-left [&_th]:font-semibold [&_td]:border [&_td]:border-slate-200 [&_td]:px-3 [&_td]:py-2 [&_tr:nth-child(even)]:bg-slate-50`}>
                        <ReactMarkdown remarkPlugins={[remarkGfm]} components={markdownComponents}>
                          {renderedContent}
                        </ReactMarkdown>
                      </div>
                      {message.role === "assistant" && message.agent_run_log ? (
                        <AgentTracePanel log={message.agent_run_log} />
                      ) : null}
                      {message.created_at ? (
                        <p className={`mt-2 text-[10px] ${message.role === "user" ? "text-indigo-200" : "text-slate-300"}`}>
                          {new Date(message.created_at).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
                        </p>
                      ) : null}
                    </div>
                    {message.role === "user" ? (
                      <div className="ml-3 mt-1 flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-slate-800">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                          <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2" />
                          <circle cx="12" cy="7" r="4" />
                        </svg>
                      </div>
                    ) : null}
                  </div>
                  );
                })}

                {/* Loading state */}
                {loading ? (
                  <div className="space-y-4">
                    {[1, 2, 3].map((i) => (
                      <div key={i} className={`chat-shimmer rounded-2xl ${i % 2 === 0 ? "ml-auto w-2/3" : "w-3/4"}`} style={{ height: `${40 + i * 12}px` }} />
                    ))}
                  </div>
                ) : null}

                {/* Typing indicator */}
                {sending ? (
                  <div className="flex justify-start">
                    <div className="mr-3 mt-1 flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-gradient-to-br from-indigo-500 to-violet-500">
                      <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                        <path d="M12 8V4H8" />
                        <rect width="16" height="12" x="4" y="8" rx="2" />
                        <path d="M2 14h2" />
                        <path d="M20 14h2" />
                        <path d="M15 13v2" />
                        <path d="M9 13v2" />
                      </svg>
                    </div>
                    <AgentProgressIndicator message={progressMessage} />
                  </div>
                ) : null}
              </div>
            </div>

            {/* ── Input area ── */}
            <div className="border-t border-slate-200 bg-white/80 px-4 py-4 backdrop-blur-md sm:px-8 lg:px-16 xl:px-24">
              <form onSubmit={handleSubmit} className="mx-auto w-[80%] max-w-none">
                {/* Hidden file inputs */}
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

                {/* Attachment previews */}
                {hasAttachments ? (
                  <div className="mb-3 flex flex-wrap gap-2">
                    {imagePreview ? (
                      <div className="group flex animate-chat-fade-in items-center gap-2.5 rounded-xl border border-slate-200 bg-white px-3 py-2">
                        <img
                          src={imagePreview}
                          alt="Upload preview"
                          className="h-10 w-10 rounded-lg border border-slate-200 object-cover"
                        />
                        <div className="flex flex-col">
                          <p className="max-w-[140px] truncate text-xs font-medium text-slate-700">
                            {selectedImage?.name}
                          </p>
                          <p className="text-[10px] text-slate-400">
                            {selectedImage ? `${(selectedImage.size / 1024).toFixed(1)} KB` : ""}
                          </p>
                        </div>
                        <button
                          type="button"
                          onClick={removeImage}
                          className="ml-1 rounded-md p-1 text-slate-400 transition hover:bg-rose-50 hover:text-rose-500"
                        >
                          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <path d="M18 6 6 18" />
                            <path d="m6 6 12 12" />
                          </svg>
                        </button>
                      </div>
                    ) : null}

                    {selectedPdf ? (
                      <div className="group flex animate-chat-fade-in items-center gap-2.5 rounded-xl border border-slate-200 bg-white px-3 py-2">
                        <div className="flex h-10 w-10 items-center justify-center rounded-lg border border-rose-200 bg-rose-50">
                          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" className="text-rose-500">
                            <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                            <polyline points="14 2 14 8 20 8" />
                          </svg>
                        </div>
                        <div className="flex flex-col">
                          <p className="max-w-[140px] truncate text-xs font-medium text-slate-700">
                            {selectedPdf.name}
                          </p>
                          <p className="text-[10px] text-slate-400">
                            {(selectedPdf.size / 1024).toFixed(1)} KB
                          </p>
                        </div>
                        <button
                          type="button"
                          onClick={removePdf}
                          className="ml-1 rounded-md p-1 text-slate-400 transition hover:bg-rose-50 hover:text-rose-500"
                        >
                          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <path d="M18 6 6 18" />
                            <path d="m6 6 12 12" />
                          </svg>
                        </button>
                      </div>
                    ) : null}
                  </div>
                ) : null}

                {/* Input container */}
                <div className="flex items-end gap-2 rounded-2xl border border-slate-200 bg-white p-2 shadow-sm transition-shadow focus-within:border-indigo-300 focus-within:shadow-[0_0_0_3px_rgba(99,102,241,0.08)]">
                  {/* Attachment buttons */}
                  <div className="flex items-center gap-0.5 pb-1 pl-1">
                    <button
                      type="button"
                      onClick={() => fileInputRef.current?.click()}
                      disabled={sending}
                      className="rounded-lg p-2 text-slate-400 transition hover:bg-slate-100 hover:text-slate-600 disabled:cursor-not-allowed disabled:opacity-40"
                      title="Attach image"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />
                        <circle cx="9" cy="9" r="2" />
                        <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
                      </svg>
                    </button>
                    <button
                      type="button"
                      onClick={() => pdfInputRef.current?.click()}
                      disabled={sending}
                      className="rounded-lg p-2 text-slate-400 transition hover:bg-slate-100 hover:text-slate-600 disabled:cursor-not-allowed disabled:opacity-40"
                      title="Attach PDF"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                        <polyline points="14 2 14 8 20 8" />
                      </svg>
                    </button>
                  </div>

                  {/* Textarea */}
                  <textarea
                    ref={textareaRef}
                    value={query}
                    onChange={(event) => setQuery(event.target.value)}
                    onKeyDown={handleKeyDown}
                    rows={1}
                    className="max-h-[200px] min-h-[44px] flex-1 resize-none bg-transparent px-2 py-2.5 text-sm text-slate-800 outline-none placeholder:text-slate-400"
                    placeholder="Ask anything about your project..."
                    disabled={sending}
                  />

                  {/* Send button */}
                  <button
                    type="submit"
                    disabled={sending || (!query.trim() && !hasAttachments)}
                    className="mb-1 mr-1 flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-gradient-to-br from-indigo-500 to-violet-500 text-white shadow-sm transition hover:from-indigo-600 hover:to-violet-600 disabled:cursor-not-allowed disabled:from-slate-300 disabled:to-slate-300 disabled:shadow-none"
                  >
                    {sending ? (
                      <svg className="animate-spin" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                        <path d="M21 12a9 9 0 1 1-6.219-8.56" />
                      </svg>
                    ) : (
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                        <path d="m5 12 7-7 7 7" />
                        <path d="M12 19V5" />
                      </svg>
                    )}
                  </button>
                </div>

                <p className="mt-2 text-center text-[11px] text-slate-400">
                  Press <kbd className="rounded bg-slate-100 px-1.5 py-0.5 text-[10px] font-medium text-slate-500">Enter</kbd> to send · <kbd className="rounded bg-slate-100 px-1.5 py-0.5 text-[10px] font-medium text-slate-500">Shift+Enter</kbd> for new line
                </p>
              </form>
            </div>
          </div>

          {/* ── Sidebar (collapsible) ── */}
          {sidebarOpen ? (
            <aside className="animate-sidebar-slide w-80 shrink-0 border-l border-slate-200 bg-white/80 backdrop-blur-md overflow-y-auto">
              <div className="p-5">
                <div className="flex items-center justify-between">
                  <h2 className="text-xs font-semibold uppercase tracking-[0.15em] text-slate-400">Project info</h2>
                  <button
                    type="button"
                    onClick={() => setSidebarOpen(false)}
                    className="rounded-lg p-1.5 text-slate-400 transition hover:bg-slate-100 hover:text-slate-600"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M18 6 6 18" />
                      <path d="m6 6 12 12" />
                    </svg>
                  </button>
                </div>

                <div className="mt-5 space-y-4">
                  {/* Project card */}
                  <div className="rounded-xl border border-slate-100 bg-gradient-to-br from-slate-50 to-white p-4">
                    <div className="flex items-center gap-3">
                      <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-indigo-100 to-violet-100">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#6366f1" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                          <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z" />
                        </svg>
                      </div>
                      <div>
                        <p className="text-sm font-semibold text-slate-800">{project?.name || "Loading..."}</p>
                        <p className="text-[11px] text-slate-400">Project</p>
                      </div>
                    </div>
                    {project?.description ? (
                      <p className="mt-3 text-xs leading-relaxed text-slate-500">{project.description}</p>
                    ) : null}
                  </div>

                  {/* Conversation details */}
                  <div className="rounded-xl border border-slate-100 bg-gradient-to-br from-slate-50 to-white p-4">
                    <p className="mb-3 text-xs font-semibold uppercase tracking-[0.1em] text-slate-400">Conversation</p>
                    <div className="space-y-3">
                      <div>
                        <p className="text-[11px] text-slate-400">Title</p>
                        <p className="text-sm font-medium text-slate-700">{title}</p>
                      </div>
                      <div>
                        <p className="text-[11px] text-slate-400">Creator</p>
                        <p className="text-sm font-medium text-slate-700">{conversation?.creator?.email || "Unknown"}</p>
                      </div>
                      <div>
                        <p className="text-[11px] text-slate-400">Role</p>
                        <p className="text-sm font-medium text-slate-700">{conversation?.creator?.role_name || "Unknown"}</p>
                      </div>
                      <div>
                        <p className="text-[11px] text-slate-400">Conversation ID</p>
                        <p className="font-mono text-[11px] text-slate-500 break-all">{conversationId}</p>
                      </div>
                    </div>
                  </div>

                  {/* RAG info */}
                  <div className="rounded-xl border border-slate-100 bg-gradient-to-br from-slate-50 to-white p-4">
                    <p className="mb-3 text-xs font-semibold uppercase tracking-[0.1em] text-slate-400">RAG Pipeline</p>
                    <div className="space-y-2">
                      {["Query your project documents", "Image & PDF analysis", "Context-aware responses"].map((item) => (
                        <div key={item} className="flex items-center gap-2">
                          <div className="flex h-5 w-5 items-center justify-center rounded-full bg-emerald-100">
                            <svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#10b981" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                              <polyline points="20 6 9 17 4 12" />
                            </svg>
                          </div>
                          <p className="text-xs text-slate-600">{item}</p>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </aside>
          ) : null}
        </div>
      </section>
    </>
  );
}

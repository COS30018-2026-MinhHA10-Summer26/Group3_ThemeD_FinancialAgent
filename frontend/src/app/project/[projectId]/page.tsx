"use client";

import { FormEvent, useEffect, useMemo, useRef, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import { createApiClient, getApiErrorMessage } from "@/lib/api";
import { ProjectConversationsCard } from "@/components/project-detail/project-conversations-card";
import { ProjectDetailsCard } from "@/components/project-detail/project-details-card";
import { ProjectMembersCard } from "@/components/project-detail/project-members-card";
import { ProjectPageHeader } from "@/components/project-detail/project-page-header";
import type { DocumentRow } from "@/components/project-detail/types";
import type {
  ConversationPayload,
  ConversationRow,
  ProjectPayload,
  ProjectRow,
  RoleName,
  TokenPayload,
  UserRow,
} from "@/components/project-detail/types";

const EMBEDDING_MODEL_OPTIONS = [{ value: "OpenAIEmbedding", label: "OpenAIEmbedding" }];
const LLM_MODEL_OPTIONS = [{ value: "OpenAI", label: "OpenAI" }];

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

export default function ProjectDetailPage() {
  const router = useRouter();
  const params = useParams<{ projectId: string | string[] }>();
  const { data: session, status } = useSession();
  const projectId = Array.isArray(params.projectId) ? params.projectId[0] : params.projectId;

  const [currentRole, setCurrentRole] = useState<RoleName | null>(null);
  const [currentEmail, setCurrentEmail] = useState<string>("");
  const [project, setProject] = useState<ProjectRow | null>(null);
  const [users, setUsers] = useState<UserRow[]>([]);
  const [conversations, setConversations] = useState<ConversationRow[]>([]);
  const [documents, setDocuments] = useState<DocumentRow[]>([]);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [creatingConversation, setCreatingConversation] = useState(false);
  const [uploadingDocument, setUploadingDocument] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [embeddingModel, setEmbeddingModel] = useState(EMBEDDING_MODEL_OPTIONS[0].value);
  const [llmModel, setLlmModel] = useState(LLM_MODEL_OPTIONS[0].value);
  const [memberIds, setMemberIds] = useState<string[]>([]);
  const [rightPanelHeight, setRightPanelHeight] = useState<number | null>(null);
  const [selectedDocumentFile, setSelectedDocumentFile] = useState<File | null>(null);
  const leftPanelRef = useRef<HTMLDivElement | null>(null);
  const documentFileInputRef = useRef<HTMLInputElement | null>(null);

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
    if (!projectId) return;

    const authToken = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!authToken || !currentRole) return;

    let cancelled = false;

    async function loadProject() {
      setLoading(true);
      setError(null);

      try {
        const api = createApiClient(authToken);
        const [projectResponse, conversationsResponse, documentsResponse, usersResponse] = await Promise.all([
          api.get<ProjectRow>(`/projects/${projectId}`),
          api.get<ConversationRow[]>(`/projects/${projectId}/conversations`),
          api.get<DocumentRow[]>(`/documents?project_id=${projectId}`),
          currentRole === "Admin" ? api.get<UserRow[]>("/people/users") : Promise.resolve({ data: [] as UserRow[] }),
        ]);

        if (cancelled) return;

        setProject(projectResponse.data);
        setName(projectResponse.data.name);
        setDescription(projectResponse.data.description ?? "");
        setEmbeddingModel(projectResponse.data.embedding_model || EMBEDDING_MODEL_OPTIONS[0].value);
        setLlmModel(projectResponse.data.llm_model || LLM_MODEL_OPTIONS[0].value);
        setMemberIds(projectResponse.data.member_ids ?? []);
        setConversations(conversationsResponse.data);
        setDocuments(documentsResponse.data);
        setUsers(usersResponse.data);
      } catch (loadError) {
        if (cancelled) return;
        setError(getApiErrorMessage(loadError, "Failed to load project"));
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    loadProject();

    return () => {
      cancelled = true;
    };
  }, [currentRole, projectId, session]);

  useEffect(() => {
    if (typeof window === "undefined") return;

    const mediaQuery = window.matchMedia("(min-width: 1024px)");
    const leftPanel = leftPanelRef.current;
    if (!leftPanel) return;

    const syncRightPanelHeight = () => {
      if (!mediaQuery.matches) {
        setRightPanelHeight(null);
        return;
      }
      setRightPanelHeight(leftPanel.getBoundingClientRect().height);
    };

    syncRightPanelHeight();

    const observer = new ResizeObserver(() => {
      syncRightPanelHeight();
    });

    observer.observe(leftPanel);
    mediaQuery.addEventListener("change", syncRightPanelHeight);
    window.addEventListener("resize", syncRightPanelHeight);

    return () => {
      observer.disconnect();
      mediaQuery.removeEventListener("change", syncRightPanelHeight);
      window.removeEventListener("resize", syncRightPanelHeight);
    };
  }, [project, loading, currentRole, users.length, memberIds.length]);

  const isAdmin = currentRole === "Admin";
  const title = useMemo(() => project?.name || "Project", [project]);

  function toggleMember(userId: string) {
    setMemberIds((currentMemberIds) => {
      if (currentMemberIds.includes(userId)) {
        return currentMemberIds.filter((id) => id !== userId);
      }
      return [...currentMemberIds, userId];
    });
  }

  async function handleSave() {
    if (!projectId || !isAdmin || saving) return;

    const token = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!token) return;

    setSaving(true);
    setError(null);

    try {
      const api = createApiClient(token);
      const payload: ProjectPayload = {
        name,
        description: description || undefined,
        embedding_model: embeddingModel,
        llm_model: llmModel,
        member_ids: memberIds,
      };
      const response = await api.put<ProjectRow>(`/projects/${projectId}`, payload);
      setProject(response.data);
      setMemberIds(response.data.member_ids ?? []);
    } catch (saveError) {
      setError(getApiErrorMessage(saveError, "Failed to update project"));
    } finally {
      setSaving(false);
    }
  }

  async function handleDelete() {
    if (!projectId || !isAdmin || saving) return;

    const token = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!token) return;

    setSaving(true);
    setError(null);

    try {
      const api = createApiClient(token);
      await api.delete(`/projects/${projectId}`);
      router.push("/project");
    } catch (deleteError) {
      setError(getApiErrorMessage(deleteError, "Failed to delete project"));
      setSaving(false);
    }
  }

  async function handleCreateConversation() {
    if (!projectId || creatingConversation) return;

    const token = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!token) return;

    setCreatingConversation(true);
    setError(null);

    try {
      const api = createApiClient(token);
      const response = await api.post<ConversationRow>(`/projects/${projectId}/conversations`, {} as ConversationPayload);
      setConversations((currentConversations) => [response.data, ...currentConversations]);
      router.push(`/project/${projectId}/chat/${response.data.conversation_id}`);
    } catch (conversationError) {
      setError(getApiErrorMessage(conversationError, "Failed to create conversation"));
    } finally {
      setCreatingConversation(false);
    }
  }

  async function handleUploadDocument(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!projectId || !isAdmin || uploadingDocument) return;

    const token = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!token) return;

    if (!selectedDocumentFile) {
      setError("Please choose a PDF file to upload.");
      return;
    }

    setUploadingDocument(true);
    setError(null);

    try {
      const api = createApiClient(token);
      const formData = new FormData();
      formData.append("project_id", projectId);
      formData.append("file", selectedDocumentFile);

      await api.post<DocumentRow>("/documents", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setSelectedDocumentFile(null);
      if (documentFileInputRef.current) {
        documentFileInputRef.current.value = "";
      }

      const documentsResponse = await api.get<DocumentRow[]>(`/documents?project_id=${projectId}`);
      setDocuments(documentsResponse.data);
    } catch (uploadError) {
      setError(getApiErrorMessage(uploadError, "Failed to upload document"));
    } finally {
      setUploadingDocument(false);
    }
  }

  return (
    <section className="mx-auto max-w-7xl px-6 py-10 sm:px-10 lg:px-12">
      <ProjectPageHeader
        title={title}
        currentEmail={currentEmail}
        currentRole={currentRole}
        isAdmin={isAdmin}
        onBack={() => router.push("/project")}
      />

      {error ? (
        <div className="mb-6 rounded-2xl border border-rose-200 bg-rose-50 px-4 py-3 text-sm text-rose-700">
          {error}
        </div>
      ) : null}

      <div className="grid items-start gap-6 lg:grid-cols-[1.4fr_0.9fr]">
        <ProjectDetailsCard
          leftPanelRef={leftPanelRef}
          loading={loading}
          project={project}
          isAdmin={isAdmin}
          name={name}
          description={description}
          embeddingModel={embeddingModel}
          llmModel={llmModel}
          saving={saving}
          embeddingModelOptions={EMBEDDING_MODEL_OPTIONS}
          llmModelOptions={LLM_MODEL_OPTIONS}
          onNameChange={setName}
          onDescriptionChange={setDescription}
          onEmbeddingModelChange={setEmbeddingModel}
          onLlmModelChange={setLlmModel}
          onSave={handleSave}
          onDelete={handleDelete}
        />

        <ProjectMembersCard
          project={project}
          users={users}
          memberIds={memberIds}
          isAdmin={isAdmin}
          rightPanelHeight={rightPanelHeight}
          onToggleMember={toggleMember}
        />
      </div>

      <ProjectConversationsCard
        conversations={conversations}
        creatingConversation={creatingConversation}
        hasProject={Boolean(project)}
        onCreateConversation={handleCreateConversation}
        onOpenConversation={(conversationId) => {
          router.push(`/project/${projectId}/chat/${conversationId}`);
        }}
      />

      <div className="mt-6 rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
        <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p className="text-sm font-medium uppercase tracking-[0.2em] text-slate-500">Documents</p>
            <h3 className="mt-2 text-xl font-semibold">Project documents</h3>
            <p className="mt-1 text-sm text-slate-500">Each document here belongs only to this project.</p>
          </div>
          <div className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold uppercase tracking-[0.18em] text-slate-600">
            {documents.length} document{documents.length === 1 ? "" : "s"}
          </div>
        </div>

        {isAdmin ? (
          <form onSubmit={handleUploadDocument} className="mt-5 grid gap-4 rounded-2xl border border-slate-200 bg-slate-50 p-4 lg:grid-cols-[1.5fr_auto] lg:items-end">
            <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
              Upload PDF
              <input
                ref={documentFileInputRef}
                type="file"
                accept="application/pdf,.pdf"
                onChange={(event) => setSelectedDocumentFile(event.target.files?.[0] ?? null)}
                className="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none file:mr-4 file:rounded-lg file:border-0 file:bg-slate-900 file:px-4 file:py-2 file:text-sm file:font-semibold file:text-white"
              />
              <span className="text-xs text-slate-500">
                {selectedDocumentFile ? selectedDocumentFile.name : "Select a PDF to ingest into this project."}
              </span>
            </label>

            <button
              type="submit"
              className="rounded-xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800 disabled:cursor-not-allowed disabled:bg-slate-400"
              disabled={uploadingDocument}
            >
              {uploadingDocument ? "Uploading..." : "Upload document"}
            </button>
          </form>
        ) : null}

        <div className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {documents.length > 0 ? (
            documents.map((document) => (
              <article
                key={document.document_id}
                className="cursor-pointer rounded-2xl border border-slate-200 bg-slate-50 p-5 transition-all duration-200 hover:border-slate-400 hover:bg-white hover:shadow-md"
                onClick={() => router.push(`/project/${projectId}/document/${document.document_id}`)}
              >
                <div className="flex items-start justify-between gap-4">
                  <div>
                    <h4 className="text-lg font-semibold tracking-tight text-slate-900">{document.file_name}</h4>
                    <p className="mt-1 text-sm text-slate-600">Uploaded by {document.uploader_email || "Unknown"}</p>
                  </div>
                  <span className="rounded-full bg-white px-3 py-1 text-xs font-semibold uppercase tracking-[0.18em] text-slate-600">
                    PDF
                  </span>
                </div>

                <div className="mt-4 grid grid-cols-2 gap-3 text-sm text-slate-600">
                  <div>
                    <div className="text-xs uppercase tracking-[0.18em] text-slate-400">Pages</div>
                    <div className="mt-1 font-medium text-slate-900">{document.total_page}</div>
                  </div>
                  <div>
                    <div className="text-xs uppercase tracking-[0.18em] text-slate-400">Chunks</div>
                    <div className="mt-1 font-medium text-slate-900">{document.total_chunk}</div>
                  </div>
                </div>

                <div className="mt-3 flex items-center gap-1 text-xs text-slate-400">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path strokeLinecap="round" strokeLinejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                  <span>Click to inspect chunks</span>
                </div>
              </article>
            ))
          ) : (
            <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5 text-sm text-slate-500 md:col-span-2 xl:col-span-3">
              No documents uploaded for this project yet.
            </div>
          )}
        </div>
      </div>
    </section>
  );
}

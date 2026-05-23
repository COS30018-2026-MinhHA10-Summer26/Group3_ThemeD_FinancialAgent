"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import { createApiClient, getApiErrorMessage } from "@/lib/api";
import { ProjectConversationsCard } from "@/components/project-detail/project-conversations-card";
import { ProjectDetailsCard } from "@/components/project-detail/project-details-card";
import { ProjectMembersCard } from "@/components/project-detail/project-members-card";
import { ProjectPageHeader } from "@/components/project-detail/project-page-header";
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
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [creatingConversation, setCreatingConversation] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [embeddingModel, setEmbeddingModel] = useState(EMBEDDING_MODEL_OPTIONS[0].value);
  const [llmModel, setLlmModel] = useState(LLM_MODEL_OPTIONS[0].value);
  const [memberIds, setMemberIds] = useState<string[]>([]);
  const [rightPanelHeight, setRightPanelHeight] = useState<number | null>(null);
  const leftPanelRef = useRef<HTMLDivElement | null>(null);

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
        const [projectResponse, conversationsResponse, usersResponse] = await Promise.all([
          api.get<ProjectRow>(`/projects/${projectId}`),
          api.get<ConversationRow[]>(`/projects/${projectId}/conversations`),
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
    </section>
  );
}

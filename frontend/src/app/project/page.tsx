"use client";

/* eslint-disable react-hooks/set-state-in-effect */

import { FormEvent, useEffect, useMemo, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import { createApiClient, getApiErrorMessage } from "@/lib/api";
import { readPageCache, writePageCache } from "@/lib/page-cache";

type RoleName = "Admin" | "User" | string;

type TokenPayload = {
  sub?: string;
  id?: string;
  role?: RoleName;
};

type ProjectRow = {
  project_id: string;
  name: string;
  description?: string | null;
  embedding_model: string;
  llm_model: string;
};

type ProjectCreatePayload = {
  name: string;
  description?: string;
  embedding_model?: string;
  llm_model?: string;
};

const EMBEDDING_MODEL_OPTIONS = [{ value: "OpenAIEmbedding", label: "OpenAIEmbedding" }];
const LLM_MODEL_OPTIONS = [{ value: "OpenAI", label: "OpenAI" }];
const PROJECT_LIST_CACHE_KEY = "project-list";

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

export default function ProjectPage() {
  const router = useRouter();
  const { data: session, status } = useSession();
  const [projects, setProjects] = useState<ProjectRow[]>([]);
  const [currentRole, setCurrentRole] = useState<RoleName | null>(null);
  const [currentEmail, setCurrentEmail] = useState<string>("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [newName, setNewName] = useState("");
  const [newDescription, setNewDescription] = useState("");
  const [newEmbeddingModel, setNewEmbeddingModel] = useState(EMBEDDING_MODEL_OPTIONS[0].value);
  const [newLlmModel, setNewLlmModel] = useState(LLM_MODEL_OPTIONS[0].value);
  const [isCreatingProject, setIsCreatingProject] = useState(false);
  const createProjectLockRef = useRef(false);

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
    const authToken = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!authToken || !currentRole) {
      return;
    }

    let cancelled = false;
    const cachedPage = readPageCache<{ projects: ProjectRow[]; currentRole: RoleName | null; currentEmail: string }>(PROJECT_LIST_CACHE_KEY);

    if (cachedPage) {
      setProjects(cachedPage.projects);
      setCurrentRole(cachedPage.currentRole);
      setCurrentEmail(cachedPage.currentEmail);
      setLoading(false);
    } else {
      setLoading(true);
    }

    async function loadProjects() {
      try {
        const api = createApiClient(authToken);
        const projectsResult = await api.get<ProjectRow[]>("/projects");

        if (cancelled) return;

        setProjects(projectsResult.data);
        setError(null);
        writePageCache(PROJECT_LIST_CACHE_KEY, {
          projects: projectsResult.data,
          currentRole,
          currentEmail,
        });
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    loadProjects();

    return () => {
      cancelled = true;
    };
  }, [currentRole, currentEmail, session]);

  const isAdmin = currentRole === "Admin";
  const title = useMemo(() => (isAdmin ? "Project management" : "Project"), [isAdmin]);

  function resetCreateForm() {
    setNewName("");
    setNewDescription("");
    setNewEmbeddingModel(EMBEDDING_MODEL_OPTIONS[0].value);
    setNewLlmModel(LLM_MODEL_OPTIONS[0].value);
  }

  async function refreshProjects() {
    const authToken = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!authToken) return;

    const api = createApiClient(authToken);
    const response = await api.get<ProjectRow[]>("/projects");
    setProjects(response.data);
  }

  async function handleCreate(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!isAdmin || createProjectLockRef.current) return;

    const token = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!token) return;

    createProjectLockRef.current = true;
    setIsCreatingProject(true);

    try {
      const api = createApiClient(token);
      const payload: ProjectCreatePayload = {
        name: newName,
        description: newDescription || undefined,
        embedding_model: newEmbeddingModel,
        llm_model: newLlmModel,
      };
      await api.post<ProjectRow>("/projects", payload);
      await refreshProjects();
      resetCreateForm();
    } catch (createError) {
      setError(getApiErrorMessage(createError, "Failed to create project"));
    } finally {
      createProjectLockRef.current = false;
      setIsCreatingProject(false);
    }
  }


  return (
    <section className="mx-auto max-w-7xl px-6 py-10 sm:px-10 lg:px-12">
      <div className="mb-8 flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p className="text-sm font-medium uppercase tracking-[0.2em] text-slate-500">Workspace</p>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight">{title}</h1>
          <p className="mt-2 text-slate-600">
            Signed in as <span className="font-medium text-slate-900">{currentEmail || "Unknown"}</span> with role{' '}
            <span className="font-medium text-slate-900">{currentRole ?? "Unknown"}</span>.
          </p>
        </div>

        <div className="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-600 shadow-sm">
          {isAdmin ? "Admin can manage all projects." : "You only see projects you are in."}
        </div>
      </div>

      {error ? (
        <div className="mb-6 rounded-2xl border border-rose-200 bg-rose-50 px-4 py-3 text-sm text-rose-700">
          {error}
        </div>
      ) : null}

      {isAdmin ? (
        <div className="mb-8 rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
          <h2 className="text-xl font-semibold">Add project</h2>
          <form onSubmit={handleCreate} className="mt-5 grid gap-4 lg:grid-cols-[1.2fr_1.2fr_0.8fr_0.8fr_auto] lg:items-end">
            <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
              Project name
              <input
                value={newName}
                onChange={(event) => setNewName(event.target.value)}
                className="rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
                placeholder="Q2 Finance Dashboard"
                required
              />
            </label>
            <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
              Description
              <input
                value={newDescription}
                onChange={(event) => setNewDescription(event.target.value)}
                className="rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
                placeholder="Optional project note"
              />
            </label>
            <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
              Embedding model
              <select
                value={newEmbeddingModel}
                onChange={(event) => setNewEmbeddingModel(event.target.value)}
                className="rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
              >
                {EMBEDDING_MODEL_OPTIONS.map((model) => (
                  <option key={model.value} value={model.value}>
                    {model.label}
                  </option>
                ))}
              </select>
            </label>
            <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
              LLM model
              <select
                value={newLlmModel}
                onChange={(event) => setNewLlmModel(event.target.value)}
                className="rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
              >
                {LLM_MODEL_OPTIONS.map((model) => (
                  <option key={model.value} value={model.value}>
                    {model.label}
                  </option>
                ))}
              </select>
            </label>
            <button
              type="submit"
              className="rounded-xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800"
              disabled={isCreatingProject}
            >
              {isCreatingProject ? "Adding..." : "Add project"}
            </button>
          </form>
        </div>
      ) : null}

      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        {loading ? (
          <div className="rounded-3xl border border-slate-200 bg-white p-6 text-slate-500 shadow-sm md:col-span-2 xl:col-span-3">
            Loading data...
          </div>
        ) : null}

        {!loading && projects.length === 0 ? (
          <div className="rounded-3xl border border-slate-200 bg-white p-6 text-slate-500 shadow-sm md:col-span-2 xl:col-span-3">
            No projects found.
          </div>
        ) : null}

        {projects.map((project) => (
          <button
            key={project.project_id}
            type="button"
            onClick={() => router.push(`/project/${project.project_id}`)}
            className="group rounded-3xl border border-slate-200 bg-white p-6 text-left shadow-sm transition hover:-translate-y-0.5 hover:border-slate-300 hover:shadow-md"
          >
            <div className="flex items-start justify-between gap-4">
              <div>
                <h2 className="text-xl font-semibold tracking-tight text-slate-900 group-hover:text-slate-700">
                  {project.name}
                </h2>
                <p className="mt-2 text-sm text-slate-600">{project.description || "No description provided."}</p>
              </div>
              <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold uppercase tracking-[0.18em] text-slate-600">
                Open
              </span>
            </div>

            <div className="mt-5 flex flex-wrap gap-2 text-xs font-medium text-slate-600">
              <span className="rounded-full border border-slate-200 px-3 py-1">{project.embedding_model}</span>
              <span className="rounded-full border border-slate-200 px-3 py-1">{project.llm_model}</span>
            </div>
          </button>
        ))}
      </div>
    </section>
  );
}

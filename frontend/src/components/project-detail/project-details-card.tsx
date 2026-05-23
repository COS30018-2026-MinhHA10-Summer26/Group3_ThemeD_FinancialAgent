import type { RefObject } from "react";
import type { ModelOption, ProjectRow } from "@/components/project-detail/types";

type ProjectDetailsCardProps = {
  leftPanelRef: RefObject<HTMLDivElement | null>;
  loading: boolean;
  project: ProjectRow | null;
  isAdmin: boolean;
  name: string;
  description: string;
  embeddingModel: string;
  llmModel: string;
  saving: boolean;
  embeddingModelOptions: ModelOption[];
  llmModelOptions: ModelOption[];
  onNameChange: (value: string) => void;
  onDescriptionChange: (value: string) => void;
  onEmbeddingModelChange: (value: string) => void;
  onLlmModelChange: (value: string) => void;
  onSave: () => void;
  onDelete: () => void;
};

export function ProjectDetailsCard({
  leftPanelRef,
  loading,
  project,
  isAdmin,
  name,
  description,
  embeddingModel,
  llmModel,
  saving,
  embeddingModelOptions,
  llmModelOptions,
  onNameChange,
  onDescriptionChange,
  onEmbeddingModelChange,
  onLlmModelChange,
  onSave,
  onDelete,
}: ProjectDetailsCardProps) {
  return (
    <div ref={leftPanelRef} className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="mb-6">
        <p className="text-sm font-medium uppercase tracking-[0.2em] text-slate-500">Project details</p>
        <h2 className="mt-2 text-2xl font-semibold tracking-tight">{project?.name || "Loading project..."}</h2>
        <p className="mt-2 text-slate-600">{project?.description || "No description provided."}</p>
      </div>

      {loading ? (
        <div className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-6 text-slate-500">Loading project...</div>
      ) : null}

      {!loading && project ? (
        <div className="grid gap-4">
          <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
            Project name
            <input
              value={name}
              onChange={(event) => onNameChange(event.target.value)}
              className="rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
              disabled={!isAdmin}
            />
          </label>
          <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
            Description
            <input
              value={description}
              onChange={(event) => onDescriptionChange(event.target.value)}
              className="rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
              disabled={!isAdmin}
            />
          </label>
          <div className="grid gap-4 md:grid-cols-2">
            <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
              Embedding model
              <select
                value={embeddingModel}
                onChange={(event) => onEmbeddingModelChange(event.target.value)}
                className="rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
                disabled={!isAdmin}
              >
                {embeddingModelOptions.map((model) => (
                  <option key={model.value} value={model.value}>
                    {model.label}
                  </option>
                ))}
              </select>
            </label>
            <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
              LLM model
              <select
                value={llmModel}
                onChange={(event) => onLlmModelChange(event.target.value)}
                className="rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
                disabled={!isAdmin}
              >
                {llmModelOptions.map((model) => (
                  <option key={model.value} value={model.value}>
                    {model.label}
                  </option>
                ))}
              </select>
            </label>
          </div>

          <div className="flex flex-wrap gap-3 pt-2">
            {isAdmin ? (
              <>
                <button
                  type="button"
                  onClick={onSave}
                  disabled={saving}
                  className="rounded-full bg-slate-900 px-5 py-2.5 font-medium text-white hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-60"
                >
                  {saving ? "Saving..." : "Save changes"}
                </button>
                <button
                  type="button"
                  onClick={onDelete}
                  disabled={saving}
                  className="rounded-full border border-rose-200 px-5 py-2.5 font-medium text-rose-600 hover:bg-rose-50 disabled:cursor-not-allowed disabled:opacity-60"
                >
                  Delete project
                </button>
              </>
            ) : null}
          </div>
        </div>
      ) : null}
    </div>
  );
}

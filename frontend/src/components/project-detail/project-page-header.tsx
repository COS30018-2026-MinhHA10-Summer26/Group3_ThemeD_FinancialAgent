import type { RoleName } from "@/components/project-detail/types";

type ProjectPageHeaderProps = {
  title: string;
  currentEmail: string;
  currentRole: RoleName | null;
  isAdmin: boolean;
  onBack: () => void;
};

export function ProjectPageHeader({ title, currentEmail, currentRole, isAdmin, onBack }: ProjectPageHeaderProps) {
  return (
    <div className="mb-8 flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
      <div>
        <button
          type="button"
          onClick={onBack}
          className="text-sm font-medium text-slate-500 transition hover:text-slate-800"
        >
          Back to projects
        </button>
        <h1 className="mt-2 text-3xl font-semibold tracking-tight">{title}</h1>
        <p className="mt-2 text-slate-600">
          Signed in as <span className="font-medium text-slate-900">{currentEmail || "Unknown"}</span> with role{" "}
          <span className="font-medium text-slate-900">{currentRole ?? "Unknown"}</span>.
        </p>
      </div>

      <div className="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-600 shadow-sm">
        {isAdmin ? "Admin can edit project members and settings." : "Read-only project view."}
      </div>
    </div>
  );
}

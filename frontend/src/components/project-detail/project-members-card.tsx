import type { ProjectRow, UserRow } from "@/components/project-detail/types";

type ProjectMembersCardProps = {
  project: ProjectRow | null;
  users: UserRow[];
  memberIds: string[];
  isAdmin: boolean;
  rightPanelHeight: number | null;
  onToggleMember: (userId: string) => void;
};

export function ProjectMembersCard({ project, users, memberIds, isAdmin, rightPanelHeight, onToggleMember }: ProjectMembersCardProps) {
  return (
    <div className="self-start lg:sticky lg:top-6">
      <div
        className="flex max-h-[calc(100vh-8rem)] min-h-[380px] flex-col overflow-hidden rounded-3xl border border-slate-200 bg-white p-6 shadow-sm lg:max-h-none"
        style={rightPanelHeight ? { height: `${rightPanelHeight}px` } : undefined}
      >
        <p className="text-sm font-medium uppercase tracking-[0.2em] text-slate-500">Members</p>
        <div className="mt-4 min-h-0 flex-1 overflow-y-auto pr-1">
          <h3 className="text-xl font-semibold">Project access</h3>
          <div className="mt-4 space-y-3">
            {project?.members?.length ? (
              project.members.map((member) => (
                <div key={member.user_id} className="rounded-2xl border border-slate-200 px-4 py-3">
                  <div className="font-medium text-slate-900">{member.email}</div>
                  <div className="text-sm text-slate-500">{member.role_name}</div>
                </div>
              ))
            ) : (
              <div className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-500">
                No members assigned yet.
              </div>
            )}
          </div>

          {isAdmin && project ? (
            <div className="mt-6 border-t border-slate-200 pt-6">
              <h4 className="text-lg font-semibold">Assign members</h4>
              <p className="mt-1 text-sm text-slate-500">Tick the users who should be able to access this project.</p>
              <div className="mt-4 space-y-2">
                {users.map((user) => {
                  const checked = memberIds.includes(user.user_id);
                  return (
                    <label key={user.user_id} className="flex items-center gap-3 rounded-2xl border border-slate-200 px-4 py-3">
                      <input
                        type="checkbox"
                        checked={checked}
                        onChange={() => onToggleMember(user.user_id)}
                        className="h-4 w-4 rounded border-slate-300"
                      />
                      <span>
                        <span className="block font-medium text-slate-900">{user.email}</span>
                        <span className="block text-sm text-slate-500">{user.role_name}</span>
                      </span>
                    </label>
                  );
                })}
                {users.length === 0 ? (
                  <div className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-500">
                    No users loaded.
                  </div>
                ) : null}
              </div>
            </div>
          ) : null}
        </div>
      </div>
    </div>
  );
}

"use client";

/* eslint-disable react-hooks/set-state-in-effect */

import { FormEvent, useEffect, useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import { createApiClient, getApiErrorMessage } from "@/lib/api";

type RoleName = "Admin" | "User" | string;

type TokenPayload = {
  sub?: string;
  id?: string;
  role?: RoleName;
};

type UserRow = {
  user_id: string;
  email: string;
  role_id: string;
  role_name: "Admin" | "User" | string;
};

type RoleRow = {
  role_id: string;
  role_name: string;
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

export default function PeoplePage() {
  const router = useRouter();
  const { data: session, status } = useSession();
  const [users, setUsers] = useState<UserRow[]>([]);
  const [roles, setRoles] = useState<RoleRow[]>([]);
  const [currentRole, setCurrentRole] = useState<RoleName | null>(null);
  const [currentEmail, setCurrentEmail] = useState<string>("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [newEmail, setNewEmail] = useState("");
  const [newRoleId, setNewRoleId] = useState<string>("");
  const [editingId, setEditingId] = useState<string | null>(null);
  const [editEmail, setEditEmail] = useState("");
  const [editRoleId, setEditRoleId] = useState<string>("");

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

    async function loadData() {
      setLoading(true);
      setError(null);

      try {
        const api = createApiClient(authToken);
        const [usersResponse, rolesResponse] = await Promise.all([
          api.get<UserRow[]>("/people/users"),
          api.get<RoleRow[]>("/people/roles"),
        ]);

        if (cancelled) return;

        setUsers(usersResponse.data);
        setRoles(rolesResponse.data);

        if (!newRoleId && rolesResponse.data.length > 0) {
          setNewRoleId(rolesResponse.data[0].role_id);
        }
      } catch (loadError) {
        if (cancelled) return;
        setError(getApiErrorMessage(loadError, "Failed to load people data"));
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    loadData();

    return () => {
      cancelled = true;
    };
  }, [currentRole, newRoleId, session]);

  const isAdmin = currentRole === "Admin";
  const title = useMemo(() => (isAdmin ? "People management" : "People"), [isAdmin]);

  function resetCreateForm() {
    setNewEmail("");
    if (roles.length > 0) {
      setNewRoleId(roles[0].role_id);
    }
  }

  function resetEditState() {
    setEditingId(null);
    setEditEmail("");
    setEditRoleId("");
  }

  async function refreshPeople() {
    const authToken = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!authToken) return;

    const api = createApiClient(authToken);
    const [usersResponse, rolesResponse] = await Promise.all([
      api.get<UserRow[]>("/people/users"),
      api.get<RoleRow[]>("/people/roles"),
    ]);

    setUsers(usersResponse.data);
    setRoles(rolesResponse.data);
  }

  async function handleCreate(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!isAdmin) return;

    const token = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!token) return;

    const selectedRoleId = newRoleId || roles[0]?.role_id;

    try {
      const api = createApiClient(token);
      await api.post<UserRow>("/people/users", {
        email: newEmail,
        password: "TempPassword123!",
        ...(selectedRoleId ? { role_id: selectedRoleId } : { role_name: "User" }),
      });
      await refreshPeople();
      resetCreateForm();
    } catch (createError) {
      setError(getApiErrorMessage(createError, "Failed to create user"));
    }
  }

  function handleStartEdit(row: UserRow) {
    setEditingId(row.user_id);
    setEditEmail(row.email);
    setEditRoleId(row.role_id);
  }

  async function handleSaveEdit(rowId: string) {
    const token = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!token) return;

    const selectedRoleId = editRoleId || roles[0]?.role_id;

    try {
      const api = createApiClient(token);
      await api.put<UserRow>(`/people/users/${rowId}`, {
        email: editEmail,
        ...(selectedRoleId ? { role_id: selectedRoleId } : { role_name: "User" }),
      });
      await refreshPeople();
      resetEditState();
    } catch (updateError) {
      setError(getApiErrorMessage(updateError, "Failed to update user"));
    }
  }

  async function handleDelete(rowId: string) {
    const token = localStorage.getItem("access_token") ?? (session as { backendToken?: string } | null)?.backendToken ?? "";
    if (!token) return;

    try {
      const api = createApiClient(token);
      await api.delete(`/people/users/${rowId}`);
      await refreshPeople();
      if (editingId === rowId) {
        resetEditState();
      }
    } catch (deleteError) {
      setError(getApiErrorMessage(deleteError, "Failed to delete user"));
    }
  }

  return (
    <section className="mx-auto max-w-7xl px-6 py-10 sm:px-10 lg:px-12">
      <div className="mb-8 flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p className="text-sm font-medium uppercase tracking-[0.2em] text-slate-500">Access control</p>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight">{title}</h1>
          <p className="mt-2 text-slate-600">
            Signed in as <span className="font-medium text-slate-900">{currentEmail || "Unknown"}</span> with role{' '}
            <span className="font-medium text-slate-900">{currentRole ?? "Unknown"}</span>.
          </p>
        </div>

        <div className="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-600 shadow-sm">
          {isAdmin ? "Admin can add, edit, and delete users and roles." : "User mode is read-only."}
        </div>
      </div>

      {error ? (
        <div className="mb-6 rounded-2xl border border-rose-200 bg-rose-50 px-4 py-3 text-sm text-rose-700">
          {error}
        </div>
      ) : null}

      {isAdmin ? (
        <div className="mb-8 rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
          <h2 className="text-xl font-semibold">Add user</h2>
          <form onSubmit={handleCreate} className="mt-5 grid gap-4 md:grid-cols-[1.4fr_0.8fr_auto] md:items-end">
            <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
              Email
              <input
                value={newEmail}
                onChange={(event) => setNewEmail(event.target.value)}
                className="rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
                placeholder="user@company.com"
                type="email"
                required
              />
            </label>
            <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
              Role
              <select
                value={newRoleId || roles[0]?.role_id || ""}
                onChange={(event) => setNewRoleId(event.target.value)}
                className="rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
                disabled={roles.length === 0}
              >
                {roles.length === 0 ? <option value="">Loading roles...</option> : null}
                {roles.map((roleRow) => (
                  <option key={roleRow.role_id} value={roleRow.role_id}>
                    {roleRow.role_name}
                  </option>
                ))}
              </select>
            </label>
            <button
              type="submit"
              className="rounded-xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800"
              disabled={roles.length === 0}
            >
              Add user
            </button>
          </form>
        </div>
      ) : null}

      <div className="overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-sm">
        <table className="min-w-full divide-y divide-slate-200">
          <thead className="bg-slate-50 text-left text-sm font-semibold text-slate-700">
            <tr>
              <th className="px-6 py-4">Email</th>
              <th className="px-6 py-4">Role</th>
              <th className="px-6 py-4">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100 bg-white text-sm">
            {loading ? (
              <tr>
                <td className="px-6 py-8 text-slate-500" colSpan={3}>
                  Loading data...
                </td>
              </tr>
            ) : null}

            {!loading && users.length === 0 ? (
              <tr>
                <td className="px-6 py-8 text-slate-500" colSpan={3}>
                  No users found.
                </td>
              </tr>
            ) : null}

            {users.map((row) => {
              const isEditing = editingId === row.user_id;

              return (
                <tr key={row.user_id}>
                  <td className="px-6 py-4 font-medium text-slate-900">
                    {isEditing && isAdmin ? (
                      <input
                        value={editEmail}
                        onChange={(event) => setEditEmail(event.target.value)}
                        className="w-full rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
                        type="email"
                      />
                    ) : (
                      row.email
                    )}
                  </td>
                  <td className="px-6 py-4 text-slate-600">
                    {isEditing && isAdmin ? (
                      <select
                        value={editRoleId || roles[0]?.role_id || ""}
                        onChange={(event) => setEditRoleId(event.target.value)}
                        className="w-full rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-slate-400"
                        disabled={roles.length === 0}
                      >
                        {roles.length === 0 ? <option value="">Loading roles...</option> : null}
                        {roles.map((roleRow) => (
                          <option key={roleRow.role_id} value={roleRow.role_id}>
                            {roleRow.role_name}
                          </option>
                        ))}
                      </select>
                    ) : (
                      row.role_name
                    )}
                  </td>
                  <td className="px-6 py-4">
                    {isAdmin ? (
                      isEditing ? (
                        <div className="flex items-center gap-3">
                          <button
                            type="button"
                            onClick={() => handleSaveEdit(row.user_id)}
                            className="rounded-full bg-slate-900 px-4 py-2 font-medium text-white hover:bg-slate-800"
                          >
                            Save
                          </button>
                          <button
                            type="button"
                            onClick={resetEditState}
                            className="rounded-full border border-slate-200 px-4 py-2 font-medium text-slate-700 hover:bg-slate-50"
                          >
                            Cancel
                          </button>
                        </div>
                      ) : (
                        <div className="flex items-center gap-3">
                          <button
                            type="button"
                            onClick={() => handleStartEdit(row)}
                            className="rounded-full border border-slate-200 px-4 py-2 font-medium text-slate-700 hover:bg-slate-50"
                          >
                            Edit
                          </button>
                          <button
                            type="button"
                            onClick={() => handleDelete(row.user_id)}
                            className="rounded-full border border-rose-200 px-4 py-2 font-medium text-rose-600 hover:bg-rose-50"
                          >
                            Delete
                          </button>
                        </div>
                      )
                    ) : (
                      <span className="text-slate-400">Read only</span>
                    )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </section>
  );
}
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { signIn, useSession } from "next-auth/react";
import { apiClient, getApiErrorMessage } from "@/lib/api";

export default function SignIn() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const { status, data: session } = useSession();

  useEffect(() => {
    if (status === "authenticated") {
      router.replace("/project");
      return;
    }

    if (localStorage.getItem("access_token")) {
      router.replace("/project");
    }
  }, [router, status, session]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const { data } = await apiClient.post("/auth/token", { email, password });
      // store token
      localStorage.setItem("access_token", data.access_token);
      // redirect to project
      router.push("/project");
    } catch (error) {
      setError(getApiErrorMessage(error, "Network error"));
    } finally {
      setLoading(false);
    }
  }

  async function handleSocialSignIn(provider: "google" | "github") {
    setError(null);
    setLoading(true);

    try {
      await signIn(provider, { callbackUrl: "/project" });
    } catch {
      setError("Could not start social sign in");
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="w-full max-w-md bg-white p-8 rounded shadow">
        <h1 className="text-2xl font-semibold mb-2">Sign in</h1>
        <p className="mb-6 text-sm text-slate-600">Use email/password or continue with Google or GitHub.</p>
        {error && <div className="mb-4 text-sm text-red-600">{error}</div>}
        <form onSubmit={handleSubmit}>
          <label className="block mb-2 text-sm font-medium">Email</label>
          <input
            className="w-full mb-4 px-3 py-2 border rounded"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            type="email"
            required
          />

          <label className="block mb-2 text-sm font-medium">Password</label>
          <input
            className="w-full mb-4 px-3 py-2 border rounded"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            type="password"
            required
          />

          <button
            className="w-full py-2 px-4 bg-blue-600 text-white rounded disabled:opacity-60"
            type="submit"
            disabled={loading}
          >
            {loading ? "Signing in..." : "Sign in"}
          </button>
        </form>

        <div className="my-6 flex items-center gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
          <span className="h-px flex-1 bg-slate-200" />
          <span>or</span>
          <span className="h-px flex-1 bg-slate-200" />
        </div>

        <div className="grid gap-3">
          <button
            type="button"
            onClick={() => handleSocialSignIn("google")}
            disabled={loading}
            className="w-full rounded border border-slate-200 px-4 py-2 font-medium text-slate-700 hover:bg-slate-50 disabled:opacity-60"
          >
            Continue with Google
          </button>
          <button
            type="button"
            onClick={() => handleSocialSignIn("github")}
            disabled={loading}
            className="w-full rounded border border-slate-200 px-4 py-2 font-medium text-slate-700 hover:bg-slate-50 disabled:opacity-60"
          >
            Continue with GitHub
          </button>
        </div>
      </div>
    </div>
  );
}

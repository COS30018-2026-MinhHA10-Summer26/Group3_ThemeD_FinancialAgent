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
    <div className="relative min-h-screen overflow-hidden bg-white text-black">
      <div className="absolute inset-0 bg-[linear-gradient(to_right,rgba(0,0,0,0.04)_1px,transparent_1px),linear-gradient(to_bottom,rgba(0,0,0,0.04)_1px,transparent_1px)] bg-[size:64px_64px] opacity-45" />
      <div className="absolute left-1/2 top-0 h-72 w-[34rem] -translate-x-1/2 rounded-full bg-[radial-gradient(circle,rgba(0,0,0,0.08)_0%,rgba(0,0,0,0.02)_42%,transparent_75%)] blur-3xl" />

      <div className="relative mx-auto flex min-h-screen w-full max-w-6xl items-center px-6 py-12 sm:px-10 lg:px-12">
        <div className="grid w-full gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
          <div className="max-w-xl">
            <p className="inline-flex rounded-full border border-black/15 bg-white px-4 py-2 text-xs font-medium tracking-[0.24em] text-black">
              SECURE ACCESS
            </p>
            <h1 className="mt-6 text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
              Sign in to the workspace with a restrained black-and-white interface.
            </h1>
            <p className="mt-5 max-w-lg text-base leading-7 text-black/65">
              Use email and password, or continue with Google or GitHub. The layout stays minimal so the authentication flow feels consistent with the rest of the app.
            </p>
            <div className="mt-8 grid gap-3 sm:grid-cols-2">
              <div className="rounded-2xl border border-black/10 bg-black p-4 text-white">
                <p className="text-xs uppercase tracking-[0.2em] text-white/55">Focused</p>
                <p className="mt-3 text-sm leading-6 text-white/75">No color noise, just clear hierarchy.</p>
              </div>
              <div className="rounded-2xl border border-black/10 bg-white p-4 text-black shadow-[0_20px_50px_rgba(0,0,0,0.06)]">
                <p className="text-xs uppercase tracking-[0.2em] text-black/45">Consistent</p>
                <p className="mt-3 text-sm leading-6 text-black/65">Matches the tone of the other pages.</p>
              </div>
            </div>
          </div>

          <div className="w-full max-w-xl rounded-3xl border border-black/10 bg-white/95 p-6 shadow-[0_28px_100px_rgba(0,0,0,0.1)] backdrop-blur sm:p-8">
            <div className="mb-6 flex items-start justify-between gap-4 border-b border-black/10 pb-5">
              <div>
                <h2 className="text-2xl font-semibold">Sign in</h2>
                <p className="mt-2 text-sm leading-6 text-black/60">Use your account credentials to continue.</p>
              </div>
              <div className="rounded-full border border-black/10 bg-black px-3 py-1 text-xs font-medium uppercase tracking-[0.2em] text-white">
                Login
              </div>
            </div>

            {error && (
              <div className="mb-4 rounded-2xl border border-black/15 bg-black/[0.04] px-4 py-3 text-sm text-black/75">
                {error}
              </div>
            )}

            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="mb-2 block text-sm font-medium text-black/80">Email</label>
                <input
                  className="w-full rounded-2xl border border-black/15 bg-white px-4 py-3 text-black outline-none transition placeholder:text-black/30 focus:border-black"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  type="email"
                  required
                  placeholder="you@example.com"
                />
              </div>

              <div>
                <label className="mb-2 block text-sm font-medium text-black/80">Password</label>
                <input
                  className="w-full rounded-2xl border border-black/15 bg-white px-4 py-3 text-black outline-none transition placeholder:text-black/30 focus:border-black"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  type="password"
                  required
                  placeholder="••••••••"
                />
              </div>

              <button
                className="w-full rounded-2xl bg-black px-4 py-3 text-sm font-semibold text-white transition hover:bg-black/85 disabled:cursor-not-allowed disabled:opacity-60"
                type="submit"
                disabled={loading}
              >
                {loading ? "Signing in..." : "Sign in"}
              </button>
            </form>

            <div className="my-6 flex items-center gap-3 text-xs uppercase tracking-[0.2em] text-black/35">
              <span className="h-px flex-1 bg-black/10" />
              <span>or</span>
              <span className="h-px flex-1 bg-black/10" />
            </div>

            <div className="grid gap-3">
              <button
                type="button"
                onClick={() => handleSocialSignIn("google")}
                disabled={loading}
                className="w-full rounded-2xl border border-black/15 bg-white px-4 py-3 text-sm font-medium text-black transition hover:bg-black hover:text-white disabled:cursor-not-allowed disabled:opacity-60"
              >
                Continue with Google
              </button>
              <button
                type="button"
                onClick={() => handleSocialSignIn("github")}
                disabled={loading}
                className="w-full rounded-2xl border border-black/15 bg-white px-4 py-3 text-sm font-medium text-black transition hover:bg-black hover:text-white disabled:cursor-not-allowed disabled:opacity-60"
              >
                Continue with GitHub
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

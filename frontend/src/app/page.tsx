"use client";

import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  function handleStart() {
    const token = localStorage.getItem("access_token");
    router.push(token ? "/project" : "/login");
  }

  return (
    <div className="relative min-h-screen overflow-hidden bg-slate-950 text-white">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,_rgba(56,189,248,0.22),_transparent_28%),radial-gradient(circle_at_bottom_right,_rgba(16,185,129,0.18),_transparent_22%)]" />
      <div className="relative mx-auto flex min-h-screen max-w-6xl items-center px-6 py-20 sm:px-10 lg:px-12">
        <div className="max-w-3xl">
          <p className="mb-4 inline-flex rounded-full border border-white/15 bg-white/8 px-4 py-2 text-sm text-slate-200">
            FinancialAgent
          </p>
          <h1 className="max-w-2xl text-5xl font-semibold tracking-tight sm:text-6xl">
            Manage finance work with one clear workspace.
          </h1>
          <p className="mt-6 max-w-xl text-lg leading-8 text-slate-300">
            Explore your project hub, team, and contact points from a clean dashboard-driven interface.
          </p>
          <button
            type="button"
            onClick={handleStart}
            className="mt-10 rounded-full bg-cyan-400 px-7 py-3 text-sm font-semibold text-slate-950 transition hover:bg-cyan-300"
          >
            Start Alalyze
          </button>
        </div>
      </div>
    </div>
  );
}

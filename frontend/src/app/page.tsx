"use client";

import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  function handleStart() {
    const token = localStorage.getItem("access_token");
    router.push(token ? "/project" : "/login");
  }

  return (
    <div className="relative min-h-screen overflow-hidden bg-white text-black">
      <div className="absolute inset-0 bg-[linear-gradient(to_right,rgba(0,0,0,0.04)_1px,transparent_1px),linear-gradient(to_bottom,rgba(0,0,0,0.04)_1px,transparent_1px)] bg-[size:72px_72px] opacity-50" />
      <div className="absolute left-1/2 top-0 h-80 w-[42rem] -translate-x-1/2 rounded-full bg-[radial-gradient(circle,rgba(0,0,0,0.08)_0%,rgba(0,0,0,0.02)_40%,transparent_72%)] blur-3xl" />

      <div className="relative mx-auto flex min-h-screen max-w-6xl items-center px-6 py-20 sm:px-10 lg:px-12">
        <div className="grid w-full gap-10 lg:grid-cols-[1.25fr_0.75fr] lg:items-center">
          <div className="max-w-3xl">
            <p className="mb-5 inline-flex rounded-full border border-black/15 bg-white px-4 py-2 text-sm font-medium tracking-[0.18em] text-black shadow-[0_8px_30px_rgba(0,0,0,0.05)]">
              FINANCIALAGENT
            </p>
            <h1 className="max-w-2xl text-5xl font-semibold tracking-tight text-balance sm:text-6xl lg:text-7xl">
              Manage finance work in one quiet, focused workspace.
            </h1>
            <p className="mt-6 max-w-xl text-lg leading-8 text-black/70">
              A clean project hub for teams, conversations, and reporting, designed to keep the interface calm and readable.
            </p>
            <div className="mt-10 flex flex-col gap-3 sm:flex-row">
              <button
                type="button"
                onClick={handleStart}
                className="rounded-full bg-black px-7 py-3 text-sm font-semibold text-white transition hover:bg-black/85"
              >
                Start Analyze
              </button>
              <a
                href="/about"
                className="rounded-full border border-black/15 bg-white px-7 py-3 text-sm font-semibold text-black transition hover:bg-black hover:text-white"
              >
                Learn more
              </a>
            </div>
          </div>

          <div className="rounded-3xl border border-black/10 bg-white/90 p-6 shadow-[0_24px_80px_rgba(0,0,0,0.08)] backdrop-blur">
            <div className="flex items-center justify-between border-b border-black/10 pb-4">
              <div>
                <p className="text-xs font-medium uppercase tracking-[0.24em] text-black/45">Overview</p>
                <p className="mt-1 text-lg font-semibold text-black">Monochrome dashboard</p>
              </div>
              <div className="h-11 w-11 rounded-full border border-black/10 bg-black/5" />
            </div>
            <div className="grid gap-4 pt-5 sm:grid-cols-2">
              <div className="rounded-2xl border border-black/10 bg-black p-4 text-white">
                <p className="text-xs uppercase tracking-[0.2em] text-white/55">Projects</p>
                <p className="mt-3 text-3xl font-semibold">12</p>
                <p className="mt-2 text-sm text-white/65">Active workspaces in focus.</p>
              </div>
              <div className="rounded-2xl border border-black/10 bg-white p-4 text-black">
                <p className="text-xs uppercase tracking-[0.2em] text-black/45">Reports</p>
                <p className="mt-3 text-3xl font-semibold">08</p>
                <p className="mt-2 text-sm text-black/60">Generated and ready to review.</p>
              </div>
            </div>
            <div className="mt-4 rounded-2xl border border-black/10 bg-black/[0.03] p-4 text-sm leading-6 text-black/70">
              A restrained black-and-white surface keeps the emphasis on data, navigation, and task flow.
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

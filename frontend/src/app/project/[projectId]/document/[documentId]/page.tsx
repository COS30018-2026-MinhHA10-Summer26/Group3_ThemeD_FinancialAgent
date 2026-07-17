"use client";

/* eslint-disable react-hooks/set-state-in-effect */

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import { createApiClient, getApiErrorMessage } from "@/lib/api";
import { readPageCache, writePageCache } from "@/lib/page-cache";
import type {
  ChunkRow,
  DocumentChunksResponse,
  DocumentRow,
  RoleName,
  TokenPayload,
} from "@/components/project-detail/types";

/* ------------------------------------------------------------------ */
/*  Helpers                                                            */
/* ------------------------------------------------------------------ */

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

function sectionTypeBadgeColor(type: string | null | undefined): string {
  switch (type) {
    case "table":
      return "bg-amber-100 text-amber-700 border-amber-200";
    case "conclusion":
      return "bg-emerald-100 text-emerald-700 border-emerald-200";
    case "introduction":
      return "bg-blue-100 text-blue-700 border-blue-200";
    case "body":
    default:
      return "bg-slate-100 text-slate-600 border-slate-200";
  }
}

function formatDate(dateString: string | null | undefined): string {
  if (!dateString) return "—";
  return new Date(dateString).toLocaleDateString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

const DOCUMENT_CACHE_PREFIX = "project-document";

/* ------------------------------------------------------------------ */
/*  Component                                                          */
/* ------------------------------------------------------------------ */

export default function DocumentDetailPage() {
  const router = useRouter();
  const params = useParams<{ projectId: string | string[]; documentId: string | string[] }>();
  const { data: session, status } = useSession();

  const projectId = Array.isArray(params.projectId) ? params.projectId[0] : params.projectId;
  const documentId = Array.isArray(params.documentId) ? params.documentId[0] : params.documentId;

  /* ---- auth state ------------------------------------------------ */
  const [currentRole, setCurrentRole] = useState<RoleName | null>(null);
  const isAdmin = currentRole === "Admin";

  /* ---- data state ------------------------------------------------ */
  const [document, setDocument] = useState<DocumentRow | null>(null);
  const [chunks, setChunks] = useState<ChunkRow[]>([]);
  const [pdfUrl, setPdfUrl] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [deleting, setDeleting] = useState(false);

  /* ---- UI state -------------------------------------------------- */
  const [searchQuery, setSearchQuery] = useState("");
  const [activeChunkId, setActiveChunkId] = useState<string | null>(null);
  const [expandedChunks, setExpandedChunks] = useState<Set<string>>(new Set());
  const [mobileTab, setMobileTab] = useState<"chunks" | "pdf">("chunks");
  const iframeRef = useRef<HTMLIFrameElement | null>(null);

  /* ---- auth effect ----------------------------------------------- */
  useEffect(() => {
    if (status === "loading") return;

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
    if (effectiveRole) setCurrentRole(effectiveRole);

    if (sessionToken && !token) localStorage.setItem("access_token", sessionToken);
  }, [router, session, status]);

  /* ---- data loading ---------------------------------------------- */
  useEffect(() => {
    if (!documentId || !currentRole) return;

    const authToken =
      localStorage.getItem("access_token") ??
      (session as { backendToken?: string } | null)?.backendToken ??
      "";
    if (!authToken) return;

    let cancelled = false;
    const cacheKey = `${DOCUMENT_CACHE_PREFIX}:${documentId}`;
    const cachedPage = readPageCache<{
      document: DocumentRow | null;
      chunks: ChunkRow[];
      pdfUrl: string | null;
      currentRole: RoleName | null;
    }>(cacheKey);

    if (cachedPage) {
      setDocument(cachedPage.document);
      setChunks(cachedPage.chunks);
      setPdfUrl(cachedPage.pdfUrl);
      setCurrentRole(cachedPage.currentRole);
      setLoading(false);
    } else {
      setLoading(true);
    }

    async function load() {
      setError(null);

      try {
        const api = createApiClient(authToken);
        const [docRes, chunksRes, rawRes] = await Promise.all([
          api.get<DocumentRow>(`/documents/${documentId}`),
          api.get<DocumentChunksResponse>(`/documents/${documentId}/chunks`),
          api.get<{ signed_url: string }>(`/documents/${documentId}/raw-url`),
        ]);

        if (cancelled) return;

        setDocument(docRes.data);
        setChunks(chunksRes.data.chunks);
        setPdfUrl(rawRes.data.signed_url);
        writePageCache(cacheKey, {
          document: docRes.data,
          chunks: chunksRes.data.chunks,
          pdfUrl: rawRes.data.signed_url,
          currentRole,
        });
      } catch (loadError) {
        if (cancelled) return;
        setError(getApiErrorMessage(loadError, "Failed to load document details"));
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    load();
    return () => {
      cancelled = true;
    };
  }, [currentRole, documentId, session]);

  /* ---- handlers -------------------------------------------------- */
  const handleChunkClick = useCallback(
    (chunk: ChunkRow) => {
      setActiveChunkId(chunk.chunk_id);
      const page = chunk.chunk_metadata?.page;
      if (page && pdfUrl) {
        // Update iframe src to jump to the page
        const baseUrl = pdfUrl.split("#")[0];
        if (iframeRef.current) {
          iframeRef.current.src = `${baseUrl}#page=${page}`;
        }
      }
      // On mobile, switch to PDF tab when a chunk with page info is clicked
      if (page && window.innerWidth < 1024) {
        setMobileTab("pdf");
      }
    },
    [pdfUrl],
  );

  const toggleChunkExpand = useCallback((chunkId: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setExpandedChunks((prev) => {
      const next = new Set(prev);
      if (next.has(chunkId)) next.delete(chunkId);
      else next.add(chunkId);
      return next;
    });
  }, []);

  async function handleDelete() {
    if (!documentId || !isAdmin || deleting) return;
    if (!window.confirm("Are you sure you want to delete this document and all its chunks? This action cannot be undone.")) return;

    const token =
      localStorage.getItem("access_token") ??
      (session as { backendToken?: string } | null)?.backendToken ??
      "";
    if (!token) return;

    setDeleting(true);
    setError(null);

    try {
      const api = createApiClient(token);
      await api.delete(`/documents/${documentId}`);
      router.push(`/project/${projectId}`);
    } catch (deleteError) {
      setError(getApiErrorMessage(deleteError, "Failed to delete document"));
      setDeleting(false);
    }
  }

  /* ---- search / filter ------------------------------------------- */
  const filteredChunks = useMemo(() => {
    if (!searchQuery.trim()) return chunks;
    const query = searchQuery.toLowerCase();
    return chunks.filter(
      (c) =>
        c.content.toLowerCase().includes(query) ||
        c.chunk_metadata?.section_title?.toLowerCase().includes(query) ||
        c.chunk_metadata?.section_type?.toLowerCase().includes(query),
    );
  }, [chunks, searchQuery]);

  /* ---- render ---------------------------------------------------- */

  if (loading) {
    return (
      <section className="mx-auto max-w-7xl px-6 py-10 sm:px-10 lg:px-12">
        <div className="flex flex-col items-center justify-center py-32">
          <div className="h-10 w-10 animate-spin rounded-full border-4 border-slate-200 border-t-slate-700" />
          <p className="mt-4 text-sm text-slate-500">Loading document details…</p>
        </div>
      </section>
    );
  }

  if (error && !document) {
    return (
      <section className="mx-auto max-w-7xl px-6 py-10 sm:px-10 lg:px-12">
        <button
          onClick={() => router.push(`/project/${projectId}`)}
          className="mb-6 flex items-center gap-2 text-sm font-medium text-slate-500 transition hover:text-slate-800"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
          Back to project
        </button>
        <div className="rounded-2xl border border-rose-200 bg-rose-50 px-5 py-4 text-sm text-rose-700">{error}</div>
      </section>
    );
  }

  return (
    <section className="mx-auto max-w-[1600px] px-4 py-6 sm:px-6 lg:px-8">
      {/* ============================================================ */}
      {/* HEADER                                                       */}
      {/* ============================================================ */}
      <div className="mb-6">
        <button
          onClick={() => router.push(`/project/${projectId}`)}
          className="mb-4 flex items-center gap-2 text-sm font-medium text-slate-500 transition hover:text-slate-800"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
          Back to project
        </button>

        {error && (
          <div className="mb-4 rounded-2xl border border-rose-200 bg-rose-50 px-4 py-3 text-sm text-rose-700">{error}</div>
        )}

        <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
          <div className="min-w-0 flex-1">
            <div className="flex items-center gap-3">
              {/* PDF icon */}
              <div className="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br from-red-500 to-rose-600 shadow-lg shadow-red-200/50">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                </svg>
              </div>
              <div className="min-w-0">
                <h1 className="truncate text-2xl font-bold tracking-tight text-slate-900">
                  {document?.file_name}
                </h1>
                <p className="mt-0.5 text-sm text-slate-500">
                  Uploaded by {document?.uploader_email || "Unknown"} · {formatDate(document?.created_at)}
                </p>
              </div>
            </div>

            {/* metadata badges */}
            <div className="mt-4 flex flex-wrap gap-2">
              <span className="inline-flex items-center gap-1.5 rounded-full border border-slate-200 bg-white px-3 py-1 text-xs font-medium text-slate-600 shadow-sm">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                {document?.total_page} pages
              </span>
              <span className="inline-flex items-center gap-1.5 rounded-full border border-slate-200 bg-white px-3 py-1 text-xs font-medium text-slate-600 shadow-sm">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h7" />
                </svg>
                {document?.total_chunk} chunks
              </span>
              <span className="inline-flex items-center rounded-full border border-red-200 bg-red-50 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-red-600">
                PDF
              </span>
            </div>
          </div>

          {/* delete button */}
          {isAdmin && (
            <button
              onClick={handleDelete}
              disabled={deleting}
              className="flex items-center gap-2 rounded-xl border border-rose-200 bg-white px-4 py-2.5 text-sm font-semibold text-rose-600 shadow-sm transition hover:bg-rose-50 hover:border-rose-300 disabled:cursor-not-allowed disabled:opacity-50"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
              {deleting ? "Deleting…" : "Delete document"}
            </button>
          )}
        </div>
      </div>

      {/* ============================================================ */}
      {/* MOBILE TABS                                                   */}
      {/* ============================================================ */}
      <div className="mb-4 flex gap-1 rounded-xl bg-slate-100 p-1 lg:hidden">
        <button
          onClick={() => setMobileTab("chunks")}
          className={`flex-1 rounded-lg px-4 py-2 text-sm font-semibold transition ${
            mobileTab === "chunks"
              ? "bg-white text-slate-900 shadow-sm"
              : "text-slate-500 hover:text-slate-700"
          }`}
        >
          Chunks ({filteredChunks.length})
        </button>
        <button
          onClick={() => setMobileTab("pdf")}
          className={`flex-1 rounded-lg px-4 py-2 text-sm font-semibold transition ${
            mobileTab === "pdf"
              ? "bg-white text-slate-900 shadow-sm"
              : "text-slate-500 hover:text-slate-700"
          }`}
        >
          Raw PDF
        </button>
      </div>

      {/* ============================================================ */}
      {/* SPLIT LAYOUT                                                  */}
      {/* ============================================================ */}
      <div className="grid gap-6 lg:grid-cols-[1fr_1fr]" style={{ minHeight: "calc(100vh - 280px)" }}>
        {/* ---------------------------------------------------------- */}
        {/* LEFT: CHUNK LIST                                            */}
        {/* ---------------------------------------------------------- */}
        <div className={`flex flex-col ${mobileTab !== "chunks" ? "hidden lg:flex" : "flex"}`}>
          {/* search bar */}
          <div className="sticky top-0 z-10 mb-4 rounded-2xl border border-slate-200 bg-white/80 p-3 shadow-sm backdrop-blur-sm">
            <div className="relative">
              <svg xmlns="http://www.w3.org/2000/svg" className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              <input
                type="text"
                placeholder="Search chunks by content, title, or type…"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full rounded-xl border border-slate-200 bg-slate-50 py-2.5 pl-10 pr-4 text-sm outline-none transition focus:border-slate-400 focus:bg-white focus:ring-2 focus:ring-slate-200"
              />
            </div>
            <div className="mt-2 flex items-center justify-between text-xs text-slate-400">
              <span>
                {filteredChunks.length} of {chunks.length} chunks
              </span>
              {searchQuery && (
                <button onClick={() => setSearchQuery("")} className="text-slate-500 hover:text-slate-700">
                  Clear
                </button>
              )}
            </div>
          </div>

          {/* chunk cards */}
          <div className="flex-1 space-y-3 overflow-y-auto pb-4" style={{ maxHeight: "calc(100vh - 340px)" }}>
            {filteredChunks.length > 0 ? (
              filteredChunks.map((chunk) => {
                const isActive = chunk.chunk_id === activeChunkId;
                const isExpanded = expandedChunks.has(chunk.chunk_id);
                const meta = chunk.chunk_metadata;
                const contentLong = chunk.content.length > 300;

                return (
                  <article
                    key={chunk.chunk_id}
                    onClick={() => handleChunkClick(chunk)}
                    className={`cursor-pointer rounded-2xl border p-4 transition-all duration-200 ${
                      isActive
                        ? "border-slate-500 bg-slate-50 shadow-md ring-1 ring-slate-300"
                        : "border-slate-200 bg-white hover:border-slate-300 hover:shadow-sm"
                    }`}
                  >
                    {/* chunk header */}
                    <div className="flex items-center justify-between gap-2">
                      <div className="flex items-center gap-2">
                        <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-slate-900 text-xs font-bold text-white">
                          {chunk.chunk_index}
                        </span>
                        {meta?.section_title && (
                          <span className="truncate text-sm font-semibold text-slate-800">
                            {meta.section_title}
                          </span>
                        )}
                      </div>
                      <div className="flex items-center gap-1.5 flex-shrink-0">
                        {meta?.page != null && (
                          <span className="rounded-md border border-slate-200 bg-slate-50 px-2 py-0.5 text-[10px] font-medium text-slate-500">
                            p.{meta.page}
                          </span>
                        )}
                        <span
                          className={`rounded-md border px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wider ${sectionTypeBadgeColor(meta?.section_type)}`}
                        >
                          {meta?.section_type || "body"}
                        </span>
                        {chunk.token_count != null && (
                          <span className="rounded-md border border-slate-200 bg-slate-50 px-2 py-0.5 text-[10px] font-medium text-slate-500">
                            {chunk.token_count} tok
                          </span>
                        )}
                      </div>
                    </div>

                    {/* chunk content */}
                    <div className="mt-3">
                      <p
                        className={`whitespace-pre-wrap text-sm leading-relaxed text-slate-700 ${
                          !isExpanded && contentLong ? "line-clamp-4" : ""
                        }`}
                      >
                        {chunk.content}
                      </p>
                      {contentLong && (
                        <button
                          onClick={(e) => toggleChunkExpand(chunk.chunk_id, e)}
                          className="mt-1.5 text-xs font-medium text-slate-500 hover:text-slate-800"
                        >
                          {isExpanded ? "Show less ↑" : "Show more ↓"}
                        </button>
                      )}
                    </div>

                    {/* tables (rendered from HTML) */}
                    {meta?.original_content?.tables_html && meta.original_content.tables_html.length > 0 && (
                      <div className="mt-3 space-y-2">
                        <p className="text-[10px] font-semibold uppercase tracking-wider text-amber-600">
                          Tables ({meta.original_content.tables_html.length})
                        </p>
                        {meta.original_content.tables_html.map((html, i) => (
                          <div
                            key={i}
                            className="overflow-x-auto rounded-xl border border-amber-200 bg-amber-50/50 p-3 text-xs [&_table]:w-full [&_table]:border-collapse [&_th]:border [&_th]:border-amber-200 [&_th]:bg-amber-100 [&_th]:px-2 [&_th]:py-1 [&_th]:text-left [&_th]:font-semibold [&_td]:border [&_td]:border-amber-200 [&_td]:px-2 [&_td]:py-1"
                            dangerouslySetInnerHTML={{ __html: html }}
                          />
                        ))}
                      </div>
                    )}

                    {/* images (rendered from base64) */}
                    {meta?.original_content?.images_base64 && meta.original_content.images_base64.length > 0 && (
                      <div className="mt-3 space-y-2">
                        <p className="text-[10px] font-semibold uppercase tracking-wider text-blue-600">
                          Images ({meta.original_content.images_base64.length})
                        </p>
                        <div className="flex flex-wrap gap-2">
                          {meta.original_content.images_base64.map((b64, i) => (
                            <img
                              key={i}
                              src={b64.startsWith("data:") ? b64 : `data:image/png;base64,${b64}`}
                              alt={`Chunk ${chunk.chunk_index} image ${i + 1}`}
                              className="max-h-40 rounded-lg border border-blue-200 object-contain shadow-sm"
                            />
                          ))}
                        </div>
                      </div>
                    )}

                    {/* active indicator */}
                    {isActive && meta?.page != null && (
                      <div className="mt-2 flex items-center gap-1 text-[10px] font-medium text-slate-500">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                          <path strokeLinecap="round" strokeLinejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                        </svg>
                        Viewing page {meta.page} in PDF
                      </div>
                    )}
                  </article>
                );
              })
            ) : (
              <div className="flex flex-col items-center justify-center py-16 text-slate-400">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
                <p className="mt-3 text-sm">No chunks match your search.</p>
              </div>
            )}
          </div>
        </div>

        {/* ---------------------------------------------------------- */}
        {/* RIGHT: PDF VIEWER                                           */}
        {/* ---------------------------------------------------------- */}
        <div className={`${mobileTab !== "pdf" ? "hidden lg:block" : "block"}`}>
          <div className="sticky top-4 rounded-2xl border border-slate-200 bg-white shadow-sm overflow-hidden" style={{ height: "calc(100vh - 280px)" }}>
            {pdfUrl ? (
              <iframe
                ref={iframeRef}
                src={pdfUrl}
                title={`Raw PDF: ${document?.file_name}`}
                className="h-full w-full"
                style={{ border: "none" }}
              />
            ) : (
              <div className="flex h-full flex-col items-center justify-center text-slate-400">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                </svg>
                <p className="mt-3 text-sm">PDF preview is not available.</p>
                <p className="mt-1 text-xs text-slate-400">Supabase storage may not be configured.</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}

-- =============================================================================
-- Migration: Entity Facts – Indexes for Semantic Memory
-- Purpose  : Add UNIQUE constraint for upsert + HNSW vector index for fast
--            cosine-similarity recall.
-- Run once : psql $DATABASE_URL -f entity_facts_indexes.sql
-- =============================================================================

-- Enable pgvector extension (idempotent)
CREATE EXTENSION IF NOT EXISTS vector;

-- ── UNIQUE partial index for project-scoped upsert ───────────────────────────
-- Guarantees that (project_id, entity_name, fact_key) is unique when
-- conversation_id IS NULL (i.e. shared project-level facts).
-- Conversation-scoped facts (conversation_id IS NOT NULL) are NOT covered by
-- this constraint and will always INSERT a new row.
CREATE UNIQUE INDEX IF NOT EXISTS uix_entity_facts_project_scoped
    ON entity_facts (project_id, entity_name, fact_key)
    WHERE conversation_id IS NULL;

-- ── HNSW vector index for approximate nearest-neighbour search ───────────────
-- Uses cosine distance operator (<=>).  HNSW is preferred over IVFFlat for
-- tables that grow incrementally (no need to rebuild after INSERT).
-- m=16, ef_construction=64 are pgvector defaults; tune if needed.
CREATE INDEX IF NOT EXISTS idx_entity_facts_embedding_hnsw
    ON entity_facts
    USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);

-- ── Composite B-tree index for metadata filtering ────────────────────────────
-- Used by the WHERE clause in recall queries (project_id + conversation_id).
CREATE INDEX IF NOT EXISTS idx_entity_facts_project_conv
    ON entity_facts (project_id, conversation_id);

-- ── Optional: index on entity_name for quick name-based lookups ──────────────
CREATE INDEX IF NOT EXISTS idx_entity_facts_entity_name
    ON entity_facts (entity_name);

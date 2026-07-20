-- =============================================================================
-- Migration: User Preferences – Indexes for fast lookup and UPSERT support
-- Run once : psql $DATABASE_URL -f user_preferences_index.sql
-- =============================================================================

-- ── UNIQUE index for UPSERT deduplication (one record per user per key) ──────
-- Allows ON CONFLICT (user_id, pref_key) DO UPDATE semantics when implemented
-- at the application layer via SQLAlchemy ORM UPSERT pattern.
CREATE UNIQUE INDEX IF NOT EXISTS uix_user_preferences_user_pref_key
    ON user_preferences (user_id, pref_key);

-- ── B-tree index for fast per-user lookup ────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_user_preferences_user_id
    ON user_preferences (user_id);

"""
User Preference Memory for the multi-agent financial pipeline.

This module persists detected user preferences (analysis framework, report format,
visualization settings, sector interests, risk tolerance) into the
``user_preferences`` Postgres table.

On each request the :class:`PreferenceReader` loads the user's preferences and
the calling agent (AdvisorAgent) injects them into its system prompt so the
response style is personalised.  After a ``deep_advice`` session completes, the
:class:`PreferenceWriter` silently detects any new/changed preferences from the
query and final report and upserts them — no user confirmation required.

Preference keys
---------------
``preferred_framework``
    The analytical framework the user gravitates toward
    (e.g. ``"SWOT"``, ``"Porter's 5 Forces"``, ``"PESTEL"``, ``"DCF"``).

``report_format``
    Preferred verbosity: ``"brief"`` (concise bullet-points) or
    ``"detailed"`` (full narrative sections).

``visualization_preference``
    Whether the user wants charts/figures embedded in reports (``true``/``false``).

``interested_sectors``
    List of industry sectors the user cares about
    (e.g. ``["EV", "Technology", "Banking"]``).

``risk_tolerance``
    Investment risk stance: ``"conservative"``, ``"moderate"``, or
    ``"aggressive"``.

Storage format
--------------
Each preference is stored as a row in ``user_preferences``:
    ``user_id``    — FK to the user account (UUID)
    ``pref_key``   — one of the five keys above
    ``pref_value`` — JSON object, e.g. ``{"value": "SWOT", "confidence": 0.9}``

Deduplication
-------------
UPSERT by ``(user_id, pref_key)`` — one record per user per key.
Newer detections silently overwrite older values.

Public API
----------
* :class:`PreferenceReader` — load preferences and format for system prompt.
* :class:`PreferenceWriter` — LLM-based detection and DB upsert.
* :func:`get_reader` / :func:`get_writer` — factory functions using config.yaml.
* :func:`is_preference_memory_enabled` — config-level on/off switch.
"""

from __future__ import annotations

import json
import logging
import os
import traceback
import uuid as _uuid_module
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from sqlalchemy.orm import Session

# ---------------------------------------------------------------------------
# Env / path setup
# ---------------------------------------------------------------------------
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_ENV_PATH = _PROJECT_ROOT / "backend" / ".env"
load_dotenv(dotenv_path=str(_PROJECT_ROOT / ".env"))
load_dotenv(dotenv_path=str(_ENV_PATH))

_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Allowed values for validation
# ---------------------------------------------------------------------------

_DEFAULT_ALLOWED_FRAMEWORKS = ["SWOT", "Porter's 5 Forces", "PESTEL", "DCF", "CAPM"]
_DEFAULT_ALLOWED_FORMATS = ["brief", "detailed"]
_DEFAULT_ALLOWED_RISK = ["conservative", "moderate", "aggressive"]
_ALL_PREF_KEYS = {
    "preferred_framework",
    "report_format",
    "visualization_preference",
    "interested_sectors",
    "risk_tolerance",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _to_uuid(value: Any) -> _uuid_module.UUID | None:
    """Safely convert any UUID-like value to a Python uuid.UUID object."""
    if value is None:
        return None
    if isinstance(value, _uuid_module.UUID):
        return value
    try:
        return _uuid_module.UUID(str(value))
    except (ValueError, AttributeError):
        return None


def _get_openai_client():
    from openai import OpenAI  # noqa: PLC0415
    return OpenAI(api_key=_OPENAI_API_KEY)


def _get_db_session() -> Session:
    from api.database import SessionLocal  # noqa: PLC0415
    return SessionLocal()


def _load_preference_config() -> dict[str, Any]:
    config_path = _PROJECT_ROOT / "ai_integration" / "config.yaml"
    try:
        import yaml  # noqa: PLC0415
        with open(config_path) as fh:
            cfg = yaml.safe_load(fh) or {}
        return cfg.get("preference_memory", {})
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# PreferenceReader
# ---------------------------------------------------------------------------

class PreferenceReader:
    """Load and format a user's preferences for injection into agent prompts.

    Usage
    -----
    ::

        reader = PreferenceReader()
        prefs  = reader.load(user_id)          # dict[str, Any]
        block  = reader.format_for_prompt(prefs)  # str  — insert into system prompt
    """

    def load(self, user_id: Any) -> dict[str, Any]:
        """Return a dict mapping pref_key → raw pref_value for *user_id*.

        Returns an empty dict if the user has no stored preferences or if
        any DB/IO error occurs (safe to call unconditionally).

        Parameters
        ----------
        user_id:
            The user's UUID (str or uuid.UUID).

        Returns
        -------
        dict[str, Any]
            E.g. ``{"preferred_framework": {"value": "SWOT", "confidence": 0.9},
                    "report_format": {"value": "detailed"}, ...}``
        """
        uid = _to_uuid(user_id)
        if uid is None:
            logger.warning("PreferenceReader.load: invalid user_id '%s'.", user_id)
            return {}

        db = _get_db_session()
        try:
            from api.models import UserPreference  # noqa: PLC0415
            rows = (
                db.query(UserPreference)
                .filter(UserPreference.user_id == uid)
                .all()
            )
            return {row.pref_key: row.pref_value for row in rows}
        except Exception as exc:
            logger.warning(
                "PreferenceReader.load: DB error — %s\n%s",
                exc, traceback.format_exc(),
            )
            return {}
        finally:
            db.close()

    @staticmethod
    def format_for_prompt(preferences: dict[str, Any]) -> str:
        """Convert a preferences dict to a natural-language instruction block.

        Returns an empty string if *preferences* is empty.

        Parameters
        ----------
        preferences:
            Dict returned by :meth:`load`.

        Returns
        -------
        str
            A ready-to-embed section for an LLM system prompt, e.g.::

                USER PREFERENCES (please follow these personalisation guidelines):
                - Preferred analysis framework: SWOT
                - Report format: detailed
                - Include charts and visualizations: Yes
                - Sectors of interest: EV, Technology
                - Risk tolerance: moderate
        """
        if not preferences:
            return ""

        lines: list[str] = [
            "USER PREFERENCES (please follow these personalisation guidelines):"
        ]

        # preferred_framework
        fw = preferences.get("preferred_framework")
        if fw and isinstance(fw, dict) and fw.get("value"):
            lines.append(f"- Preferred analysis framework: {fw['value']}")

        # report_format
        fmt = preferences.get("report_format")
        if fmt and isinstance(fmt, dict) and fmt.get("value"):
            val = fmt["value"]
            desc = (
                "detailed (full narrative sections with headings)"
                if val == "detailed"
                else "brief (concise bullet-points and key takeaways)"
            )
            lines.append(f"- Report format: {desc}")

        # visualization_preference
        vis = preferences.get("visualization_preference")
        if vis and isinstance(vis, dict) and vis.get("value") is not None:
            include = "Yes" if vis["value"] else "No"
            lines.append(f"- Include charts and visualizations: {include}")

        # interested_sectors
        sec = preferences.get("interested_sectors")
        if sec and isinstance(sec, dict) and sec.get("value"):
            sectors = sec["value"]
            if isinstance(sectors, list) and sectors:
                lines.append(f"- Sectors of interest: {', '.join(sectors)}")

        # risk_tolerance
        risk = preferences.get("risk_tolerance")
        if risk and isinstance(risk, dict) and risk.get("value"):
            lines.append(f"- Risk tolerance: {risk['value']}")

        # Only return the block if we actually found at least one preference
        if len(lines) == 1:
            return ""

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# PreferenceWriter
# ---------------------------------------------------------------------------

_DETECTION_SYSTEM_PROMPT = """\
You are a user-preference detector for a financial analysis AI assistant.

Given a user query and the advisor's report that was generated in response,
identify which of the following user preferences are evident:

1. preferred_framework  — which analytical framework was used or clearly preferred
   Allowed values: {allowed_frameworks}
   Set to null if no clear framework preference is detectable.

2. report_format        — did the user want a brief or detailed answer?
   Allowed values: {allowed_formats}
   Infer from query length, question style ("quick overview" → brief;
   "thorough analysis" / "full report" → detailed).
   Set to null if ambiguous.

3. visualization_preference — did the user express interest in charts/graphs?
   Allowed values: true, false
   Set to null if not evident.

4. interested_sectors   — which industries/sectors did the user ask about?
   Extract as a list of short strings (e.g. ["EV", "Technology", "Banking"]).
   Maximum {max_sectors} sectors. Set to null if none mentioned.

5. risk_tolerance       — what investment risk level does the user appear to have?
   Allowed values: {allowed_risk_levels}
   Infer from language ("safe investment" → conservative; "high-growth" → aggressive).
   Set to null if not evident.

Return ONLY a JSON object with these exact keys. Use null for undetectable fields.
Do NOT invent preferences that are not evident from the text.

Example:
{{
  "preferred_framework": "SWOT",
  "report_format": "detailed",
  "visualization_preference": true,
  "interested_sectors": ["EV", "Technology"],
  "risk_tolerance": null
}}
"""

_DETECTION_USER_TEMPLATE = """\
User Query:
{query}

Advisor Report (excerpt, max 3000 chars):
{report_excerpt}
"""


class PreferenceWriter:
    """Detect user preferences from query+report and upsert them into the DB.

    Parameters
    ----------
    detection_model:
        OpenAI chat model used for preference detection.
    allowed_frameworks, allowed_formats, allowed_risk_levels:
        Validation whitelists — values outside these lists are discarded.
    max_sectors:
        Maximum number of sector strings to store.
    """

    def __init__(
        self,
        detection_model: str = "gpt-4o-mini",
        allowed_frameworks: list[str] | None = None,
        allowed_formats: list[str] | None = None,
        allowed_risk_levels: list[str] | None = None,
        max_sectors: int = 5,
    ) -> None:
        self.detection_model = detection_model
        self.allowed_frameworks = allowed_frameworks or _DEFAULT_ALLOWED_FRAMEWORKS
        self.allowed_formats = allowed_formats or _DEFAULT_ALLOWED_FORMATS
        self.allowed_risk_levels = allowed_risk_levels or _DEFAULT_ALLOWED_RISK
        self.max_sectors = max_sectors

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def detect_and_save(
        self,
        query: str,
        report: str,
        user_id: Any,
    ) -> dict[str, Any]:
        """Detect preferences from *query*+*report* and silently upsert to DB.

        Safe to call unconditionally — any DB or LLM failure is logged and
        swallowed; the function never raises.

        Parameters
        ----------
        query:
            The user's original query string.
        report:
            The final advisor report (Markdown).
        user_id:
            The user's UUID (str or uuid.UUID).

        Returns
        -------
        dict[str, Any]
            The validated preferences that were detected (may be empty).
        """
        uid = _to_uuid(user_id)
        if uid is None:
            logger.warning("PreferenceWriter: invalid user_id '%s', skipping.", user_id)
            return {}

        query = (query or "").strip()
        report = (report or "").strip()
        if not query and not report:
            return {}

        detected = self._detect_with_llm(query, report)
        if not detected:
            logger.info("PreferenceWriter: no preferences detected.")
            return {}

        validated = self._validate(detected)
        if not validated:
            logger.info("PreferenceWriter: all detected preferences failed validation.")
            return {}

        self._upsert_all(uid, validated)
        return validated

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _detect_with_llm(self, query: str, report: str) -> dict[str, Any]:
        """Call the LLM to extract preference signals. Returns {} on failure."""
        client = _get_openai_client()
        system_prompt = _DETECTION_SYSTEM_PROMPT.format(
            allowed_frameworks=", ".join(self.allowed_frameworks),
            allowed_formats=", ".join(self.allowed_formats),
            allowed_risk_levels=", ".join(self.allowed_risk_levels),
            max_sectors=self.max_sectors,
        )
        # Limit report to 3000 chars to stay within token budget
        report_excerpt = report[:3000] + ("..." if len(report) > 3000 else "")
        user_content = _DETECTION_USER_TEMPLATE.format(
            query=query, report_excerpt=report_excerpt
        )

        try:
            response = client.chat.completions.create(
                model=self.detection_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
                temperature=0,
                response_format={"type": "json_object"},
            )
            raw = (response.choices[0].message.content or "").strip()
        except Exception as exc:
            logger.error(
                "PreferenceWriter: LLM detection failed — %s\n%s",
                exc, traceback.format_exc(),
            )
            return {}

        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            logger.warning(
                "PreferenceWriter: could not parse LLM JSON. Raw: %.200s", raw
            )
            return {}

        if not isinstance(parsed, dict):
            return {}

        # Strip null values so we only store what was detected
        return {k: v for k, v in parsed.items() if v is not None and k in _ALL_PREF_KEYS}

    def _validate(self, raw: dict[str, Any]) -> dict[str, Any]:
        """Validate detected values against whitelists. Discards invalid entries."""
        validated: dict[str, Any] = {}

        # preferred_framework
        fw = raw.get("preferred_framework")
        if isinstance(fw, str) and fw in self.allowed_frameworks:
            validated["preferred_framework"] = {"value": fw, "confidence": 0.85}

        # report_format
        fmt = raw.get("report_format")
        if isinstance(fmt, str) and fmt in self.allowed_formats:
            validated["report_format"] = {"value": fmt}

        # visualization_preference
        vis = raw.get("visualization_preference")
        if isinstance(vis, bool):
            validated["visualization_preference"] = {"value": vis}

        # interested_sectors
        sectors = raw.get("interested_sectors")
        if isinstance(sectors, list):
            clean = [str(s).strip() for s in sectors if str(s).strip()][:self.max_sectors]
            if clean:
                validated["interested_sectors"] = {"value": clean}

        # risk_tolerance
        risk = raw.get("risk_tolerance")
        if isinstance(risk, str) and risk in self.allowed_risk_levels:
            validated["risk_tolerance"] = {"value": risk}

        return validated

    def _upsert_all(
        self, user_id: _uuid_module.UUID, preferences: dict[str, Any]
    ) -> None:
        """Upsert each preference key–value pair for *user_id*.

        Uses the ORM find-then-update pattern (compatible with all SA 2.x
        backends) rather than a raw INSERT … ON CONFLICT statement.
        """
        from api.models import UserPreference  # noqa: PLC0415

        db = _get_db_session()
        try:
            for pref_key, pref_value in preferences.items():
                try:
                    existing = (
                        db.query(UserPreference)
                        .filter(
                            UserPreference.user_id == user_id,
                            UserPreference.pref_key == pref_key,
                        )
                        .first()
                    )
                    if existing:
                        existing.pref_value = pref_value
                        db.add(existing)
                    else:
                        db.add(
                            UserPreference(
                                user_id=user_id,
                                pref_key=pref_key,
                                pref_value=pref_value,
                            )
                        )
                except Exception as exc:
                    logger.warning(
                        "PreferenceWriter: failed to upsert '%s' — %s", pref_key, exc
                    )
            db.commit()
            logger.info(
                "PreferenceWriter: upserted %d preferences for user %s.",
                len(preferences), user_id,
            )
        except Exception as exc:
            db.rollback()
            logger.error(
                "PreferenceWriter: DB commit failed — %s\n%s",
                exc, traceback.format_exc(),
            )
        finally:
            db.close()


# ---------------------------------------------------------------------------
# Factory helpers
# ---------------------------------------------------------------------------

def get_reader() -> PreferenceReader:
    """Return a :class:`PreferenceReader` (no config needed — stateless)."""
    return PreferenceReader()


def get_writer() -> PreferenceWriter:
    """Return a :class:`PreferenceWriter` configured from ``config.yaml``."""
    cfg = _load_preference_config()
    return PreferenceWriter(
        detection_model=str(cfg.get("detection_model", "gpt-4o-mini")),
        allowed_frameworks=cfg.get("allowed_frameworks", _DEFAULT_ALLOWED_FRAMEWORKS),
        allowed_formats=cfg.get("allowed_formats", _DEFAULT_ALLOWED_FORMATS),
        allowed_risk_levels=cfg.get("allowed_risk_levels", _DEFAULT_ALLOWED_RISK),
        max_sectors=int(cfg.get("max_sectors", 5)),
    )


def is_preference_memory_enabled() -> bool:
    """Return True if preference memory is enabled in config."""
    cfg = _load_preference_config()
    return bool(cfg.get("enabled", True))

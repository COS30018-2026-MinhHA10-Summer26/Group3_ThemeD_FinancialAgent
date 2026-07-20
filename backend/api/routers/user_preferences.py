"""
REST API endpoints for the UserPreference memory store.

Allows the current authenticated user to view, update, and reset their
personalisation preferences that are automatically detected and used by the
multi-agent pipeline.

Routes
------
GET    /users/me/preferences
    List all stored preferences for the current user.

PUT    /users/me/preferences/{pref_key}
    Explicitly set or update a single preference (overrides auto-detected value).

DELETE /users/me/preferences/{pref_key}
    Delete a single preference (the pipeline will stop applying it).

DELETE /users/me/preferences
    Reset ALL preferences for the current user.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict

from api.deps import db_dependency, get_current_user
from api.models import UserPreference

router = APIRouter(
    prefix="/users/me",
    tags=["user-preferences"],
)

# ──────────────────────────────────────────────────────────────────────────────
# Allowed preference keys and their valid value constraints
# ──────────────────────────────────────────────────────────────────────────────

_ALLOWED_KEYS = {
    "preferred_framework",
    "report_format",
    "visualization_preference",
    "interested_sectors",
    "risk_tolerance",
}

_ALLOWED_FRAMEWORKS = {"SWOT", "Porter's 5 Forces", "PESTEL", "DCF", "CAPM"}
_ALLOWED_FORMATS = {"brief", "detailed"}
_ALLOWED_RISK = {"conservative", "moderate", "aggressive"}


# ──────────────────────────────────────────────────────────────────────────────
# Pydantic schemas
# ──────────────────────────────────────────────────────────────────────────────

class PreferenceRead(BaseModel):
    preference_id: UUID
    user_id: UUID
    pref_key: str
    pref_value: Any
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class PreferenceUpdate(BaseModel):
    """Body for PUT /users/me/preferences/{pref_key}."""
    value: Any  # The inner value — will be wrapped in {"value": ...} for storage

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"value": "SWOT"},
                {"value": "detailed"},
                {"value": True},
                {"value": ["EV", "Technology"]},
                {"value": "moderate"},
            ]
        }
    )


class BulkDeleteResponse(BaseModel):
    deleted_count: int
    message: str


# ──────────────────────────────────────────────────────────────────────────────
# Validation helpers
# ──────────────────────────────────────────────────────────────────────────────

def _validate_pref_value(pref_key: str, value: Any) -> Any:
    """Validate the inner *value* for a given *pref_key*.

    Raises HTTPException 422 if the value is invalid for the key.
    Returns the (possibly coerced) value on success.
    """
    if pref_key == "preferred_framework":
        if not isinstance(value, str) or value not in _ALLOWED_FRAMEWORKS:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"preferred_framework must be one of: {sorted(_ALLOWED_FRAMEWORKS)}",
            )

    elif pref_key == "report_format":
        if not isinstance(value, str) or value not in _ALLOWED_FORMATS:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"report_format must be one of: {sorted(_ALLOWED_FORMATS)}",
            )

    elif pref_key == "visualization_preference":
        if not isinstance(value, bool):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="visualization_preference must be a boolean (true/false).",
            )

    elif pref_key == "interested_sectors":
        if not isinstance(value, list) or not all(isinstance(s, str) for s in value):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="interested_sectors must be a list of strings.",
            )
        value = [s.strip() for s in value if s.strip()][:5]

    elif pref_key == "risk_tolerance":
        if not isinstance(value, str) or value not in _ALLOWED_RISK:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"risk_tolerance must be one of: {sorted(_ALLOWED_RISK)}",
            )

    return value


def _get_user_uuid(current_user: dict) -> UUID:
    """Extract and return the user UUID from the JWT payload."""
    raw = current_user.get("id")
    if raw is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not determine user identity.",
        )
    try:
        return UUID(str(raw))
    except (ValueError, AttributeError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user identity format.",
        )


# ──────────────────────────────────────────────────────────────────────────────
# Endpoints
# ──────────────────────────────────────────────────────────────────────────────

@router.get(
    "/preferences",
    response_model=list[PreferenceRead],
    summary="List all preferences for the current user",
)
def list_preferences(
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    """Return all stored preferences for the authenticated user.

    Preferences are automatically detected and updated by the pipeline, but
    can also be set explicitly via PUT.
    """
    user_id = _get_user_uuid(current_user)
    rows = (
        db.query(UserPreference)
        .filter(UserPreference.user_id == user_id)
        .order_by(UserPreference.pref_key)
        .all()
    )
    return rows


@router.put(
    "/preferences/{pref_key}",
    response_model=PreferenceRead,
    summary="Explicitly set or update a preference",
)
def upsert_preference(
    pref_key: str,
    body: PreferenceUpdate,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    """Set (or overwrite) one preference for the current user.

    Allowed ``pref_key`` values: ``preferred_framework``, ``report_format``,
    ``visualization_preference``, ``interested_sectors``, ``risk_tolerance``.

    The ``value`` in the request body is validated against the allowed options
    for each key.
    """
    if pref_key not in _ALLOWED_KEYS:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Unknown pref_key '{pref_key}'. Allowed: {sorted(_ALLOWED_KEYS)}",
        )

    user_id = _get_user_uuid(current_user)
    validated_value = _validate_pref_value(pref_key, body.value)
    pref_value = {"value": validated_value, "source": "explicit"}

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
        db.commit()
        db.refresh(existing)
        return existing
    else:
        new_pref = UserPreference(
            user_id=user_id,
            pref_key=pref_key,
            pref_value=pref_value,
        )
        db.add(new_pref)
        db.commit()
        db.refresh(new_pref)
        return new_pref


@router.delete(
    "/preferences/{pref_key}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a single preference",
)
def delete_preference(
    pref_key: str,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    """Remove one preference by key for the current user.

    After deletion the pipeline will no longer apply this preference when
    generating reports.
    """
    if pref_key not in _ALLOWED_KEYS:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Unknown pref_key '{pref_key}'. Allowed: {sorted(_ALLOWED_KEYS)}",
        )

    user_id = _get_user_uuid(current_user)
    existing = (
        db.query(UserPreference)
        .filter(
            UserPreference.user_id == user_id,
            UserPreference.pref_key == pref_key,
        )
        .first()
    )

    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Preference '{pref_key}' not found for this user.",
        )

    db.delete(existing)
    db.commit()


@router.delete(
    "/preferences",
    response_model=BulkDeleteResponse,
    summary="Reset all preferences for the current user",
)
def reset_all_preferences(
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    """Delete ALL stored preferences for the current user.

    The pipeline will start fresh preference detection on the next
    ``deep_advice`` request.
    """
    user_id = _get_user_uuid(current_user)
    deleted = (
        db.query(UserPreference)
        .filter(UserPreference.user_id == user_id)
        .delete(synchronize_session=False)
    )
    db.commit()

    return BulkDeleteResponse(
        deleted_count=deleted,
        message=f"Deleted {deleted} preference(s) for user {user_id}.",
    )

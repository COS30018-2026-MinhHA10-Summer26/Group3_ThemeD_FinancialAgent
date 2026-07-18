"""Backend API package initialisation.

Ensure the repository root is available on ``sys.path`` so imports that reach
the sibling ``ai_integration`` package work whether Uvicorn is launched from
``backend`` or ``backend/api``.
"""

from __future__ import annotations

import sys
from pathlib import Path


_API_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _API_DIR.parent.parent

project_root_str = str(_PROJECT_ROOT)
if project_root_str not in sys.path:
	sys.path.insert(0, project_root_str)

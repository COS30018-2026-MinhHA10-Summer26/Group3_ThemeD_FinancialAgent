"""Compatibility module that exposes the AI_Integration package under a lowercase name."""

import sys
from pathlib import Path

_package_root = Path(__file__).resolve().parent / "AI_Integration"

__path__ = [str(_package_root)]
__package__ = __name__

sys.modules.setdefault("AI_Integration", sys.modules[__name__])

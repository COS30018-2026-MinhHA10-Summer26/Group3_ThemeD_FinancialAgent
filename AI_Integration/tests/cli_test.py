from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ai_integration.cli import main


def test_cli_dry_run():
    exit_code = main(
        [
            "--query",
            "Download Tesla annual reports from the official company website for 2024 and make a report",
            "--dry-run-downloads",
            "--show-state",
        ]
    )
    assert exit_code == 0


if __name__ == "__main__":
    test_cli_dry_run()

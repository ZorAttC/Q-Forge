"""Validate the finalized one-page-one-script video manuscript."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STORYBOARD = ROOT / "docs" / "STORYBOARD_CORE_SUMMARY_ZH_V2.md"
DEFAULT_NARRATION = ROOT / "video" / "narration.txt"

SCRIPT_PATTERN = re.compile(
    r"\*\*完整英文口播：\*\*\s*\n\s*```text\n(.*?)\n```",
    re.DOTALL,
)


def _normalize(text: str) -> str:
    return " ".join(text.split())


def load_finalized_narration(
    narration_path: Path = DEFAULT_NARRATION,
    storyboard_path: Path = DEFAULT_STORYBOARD,
) -> tuple[str, list[str]]:
    narration = narration_path.read_text(encoding="utf-8")
    paragraphs = [p.strip() for p in narration.split("\n\n") if p.strip()]
    if len(paragraphs) != 15:
        raise ValueError(
            f"Expected one finalized narration paragraph per slide (15 total), "
            f"found {len(paragraphs)}"
        )

    storyboard = storyboard_path.read_text(encoding="utf-8")
    storyboard_scripts = SCRIPT_PATTERN.findall(storyboard)
    if len(storyboard_scripts) != 15:
        raise ValueError(
            f"Expected 15 finalized storyboard scripts, found {len(storyboard_scripts)}"
        )

    for page, (storyboard_script, narration_script) in enumerate(
        zip(storyboard_scripts, paragraphs),
        start=1,
    ):
        if _normalize(storyboard_script) != _normalize(narration_script):
            raise ValueError(
                f"Storyboard and narration differ on page {page}; "
                "freeze the manuscript before generating media"
            )

    return narration, [_normalize(p) for p in paragraphs]

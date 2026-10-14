#!/usr/bin/env python3
"""Write the Project 1 pre-recording manifest with the required CSV schema."""
from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "project-submission-manifest.csv"
HEAD = "38c2f9fef188b0b5d36aac6b2d14d8902e47531a"
REPO = "https://github.com/cmainville/ibm-project-1"
FIELDS = [
    "item", "required", "location_or_url", "title", "duration_or_as_of",
    "timestamp_index", "access_checked", "frozen_or_commit_id", "notes",
]


def blob(path: str) -> str:
    return f"{REPO}/blob/main/{path}"


ROWS = [
    {
        "item": "Research-Evolution.pdf", "required": "yes",
        "location_or_url": blob("docs/Research-Evolution.pdf"),
        "title": "IBM Research Evolution — Edition A and Edition B",
        "duration_or_as_of": "September 1, 2026 valuation cutoff",
        "timestamp_index": "", "access_checked": "LOCAL_PATH_VERIFIED",
        "frozen_or_commit_id": "PENDING_FINALIZATION",
        "notes": "Repository file is docs/Research-Evolution.pdf. Edition A checkpoint remains PENDING_INSTRUCTOR_DETERMINATION.",
    },
    {
        "item": "Repository", "required": "yes", "location_or_url": REPO,
        "title": "cmainville/ibm-project-1", "duration_or_as_of": "Current review: October 14, 2026",
        "timestamp_index": "", "access_checked": "REMOTE_URL_VERIFIED; LOGGED_OUT_GRADER_ACCESS_PENDING",
        "frozen_or_commit_id": f"{HEAD} (current review commit; not final frozen)",
        "notes": "README, environment, model, tests, docs, and visible output are present. Instructional-team access must be personally verified before submission.",
    },
    {
        "item": "Visible executed output", "required": "yes",
        "location_or_url": blob("output/visible-base-output.html"),
        "title": "IBM visible executed base output", "duration_or_as_of": "September 1, 2026; base $182.29/share",
        "timestamp_index": "", "access_checked": "LOCAL_PATH_VERIFIED",
        "frozen_or_commit_id": "PENDING_FINALIZATION",
        "notes": "Standalone static HTML; not the interactive workbench. Final link/access check remains pending.",
    },
    {
        "item": "Decision memo or deck", "required": "yes",
        "location_or_url": blob("docs/Decision-Deck.pdf"),
        "title": "IBM Investment Decision Deck", "duration_or_as_of": "September 1, 2026; Watch / Defer",
        "timestamp_index": "", "access_checked": "LOCAL_PATH_VERIFIED",
        "frozen_or_commit_id": "PENDING_FINALIZATION",
        "notes": "Repository filename is Decision-Deck.pdf; Brightspace upload filename is Decision-Deck.pdf.",
    },
    {
        "item": "Validation-and-AI-Use.pdf", "required": "yes",
        "location_or_url": blob("docs/validation-and-ai-use.pdf"),
        "title": "IBM Validation and AI Use", "duration_or_as_of": "October 14, 2026; current 35-test extension",
        "timestamp_index": "", "access_checked": "LOCAL_PATH_VERIFIED",
        "frozen_or_commit_id": "PENDING_FINALIZATION",
        "notes": "Repository source uses lowercase filename. Upload a content-equivalent copy named Validation-and-AI-Use.pdf at final submission.",
    },
    {"item": "Video 1", "required": "yes", "location_or_url": "", "title": "", "duration_or_as_of": "", "timestamp_index": "", "access_checked": "", "frozen_or_commit_id": "", "notes": "PENDING_RECORDING — research evolution and AI-output check; maximum 3:00."},
    {"item": "Transcript Video 1", "required": "yes", "location_or_url": "", "title": "", "duration_or_as_of": "", "timestamp_index": "", "access_checked": "", "frozen_or_commit_id": "", "notes": "PENDING_RECORDING — create corrected docs/transcript-video-1.txt and attach it to Brightspace after recording."},
    {"item": "Video 2", "required": "yes", "location_or_url": "", "title": "", "duration_or_as_of": "", "timestamp_index": "", "access_checked": "", "frozen_or_commit_id": "", "notes": "PENDING_RECORDING — codebase walkthrough and high-risk validation; maximum 5:00."},
    {"item": "Transcript Video 2", "required": "yes", "location_or_url": "", "title": "", "duration_or_as_of": "", "timestamp_index": "", "access_checked": "", "frozen_or_commit_id": "", "notes": "PENDING_RECORDING — create corrected docs/transcript-video-2.txt and attach it to Brightspace after recording."},
    {"item": "Video 3", "required": "yes", "location_or_url": "", "title": "", "duration_or_as_of": "", "timestamp_index": "", "access_checked": "", "frozen_or_commit_id": "", "notes": "PENDING_RECORDING — must open with live product demonstration; maximum 5:00."},
    {"item": "Transcript Video 3", "required": "yes", "location_or_url": "", "title": "", "duration_or_as_of": "", "timestamp_index": "", "access_checked": "", "frozen_or_commit_id": "", "notes": "PENDING_RECORDING — create corrected docs/transcript-video-3.txt and attach it to Brightspace after recording."},
    {"item": "Optional deployed output", "required": "no", "location_or_url": "", "title": "", "duration_or_as_of": "", "timestamp_index": "", "access_checked": "", "frozen_or_commit_id": "", "notes": "NOT DEPLOYED — OPTIONAL. Local runnable workbench and visible static output are the required delivery."},
]


def main() -> None:
    if len(ROWS) != 12 or list(ROWS[0]) != FIELDS:
        raise ValueError("Manifest schema/row definition is invalid")
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(ROWS)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()

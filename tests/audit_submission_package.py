#!/usr/bin/env python3
"""Standard-library pre-recording/final checks for the Project 1 submission package.

This validator checks structure and locally inspectable artifacts. It deliberately
does not claim to verify private GitHub access, logged-out video playback,
visual/semantic video content, captions, or PDF meaning; those remain explicit
manual fields in the manifest and readiness record.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "project-submission-manifest.csv"
FIELDS = [
    "item", "required", "location_or_url", "title", "duration_or_as_of",
    "timestamp_index", "access_checked", "frozen_or_commit_id", "notes",
]
ITEMS = [
    "Research-Evolution.pdf", "Repository", "Visible executed output",
    "Decision memo or deck", "Validation-and-AI-Use.pdf", "Video 1",
    "Transcript Video 1", "Video 2", "Transcript Video 2", "Video 3",
    "Transcript Video 3", "Optional deployed output",
]
LOCAL_REQUIRED = {
    "Research-Evolution.pdf": "docs/Research-Evolution.pdf",
    "Visible executed output": "output/visible-base-output.html",
    "Decision memo or deck": "docs/Decision-Deck.pdf",
    "Validation-and-AI-Use.pdf": "docs/validation-and-ai-use.pdf",
}
VIDEO_ITEMS = {"Video 1", "Video 2", "Video 3"}
TRANSCRIPT_ITEMS = {"Transcript Video 1", "Transcript Video 2", "Transcript Video 3"}
GITHUB_BLOB = "https://github.com/cmainville/ibm-project-1/blob/main/"


def pdf_page_objects(path: Path) -> int:
    """Return a structural page-object count; not a semantic or visual audit."""
    raw = path.read_bytes()
    if not raw.startswith(b"%PDF-"):
        raise ValueError("missing PDF header")
    return len(re.findall(rb"/Type\s*/Page\b", raw))


def local_path_from_url(url: str) -> Path | None:
    if url.startswith(GITHUB_BLOB):
        return ROOT / unquote(url[len(GITHUB_BLOB):])
    if not url or url.startswith(("http://", "https://")):
        return None
    return ROOT / url.split("#", 1)[0]


def check_local_markdown_links(path: Path, failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = (path.parent / unquote(target.split("#", 1)[0])).resolve()
        if not target_path.exists():
            failures.append(f"broken local Markdown link in {path.relative_to(ROOT)}: {target}")


def pending_or_fail(mode: str, pending: list[str], failures: list[str], message: str) -> None:
    (failures if mode == "final" else pending).append(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pre-recording", action="store_true")
    group.add_argument("--final", action="store_true")
    args = parser.parse_args()
    mode = "pre-recording" if args.pre_recording else "final"
    failures: list[str] = []
    pending: list[str] = []

    try:
        with MANIFEST.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            if reader.fieldnames != FIELDS:
                failures.append(f"manifest columns must exactly equal {FIELDS}; got {reader.fieldnames}")
    except (OSError, csv.Error) as exc:
        failures.append(f"cannot parse manifest with csv module: {exc}")
        rows = []

    labels = [r.get("item", "") for r in rows]
    if len(rows) != 12:
        failures.append(f"manifest must contain exactly 12 artifact rows; found {len(rows)}")
    if labels != ITEMS or len(set(labels)) != len(labels):
        failures.append("manifest labels/order must exactly match the official 12-row list")
    if sum(r.get("required") == "yes" for r in rows) != 11 or sum(r.get("required") == "no" for r in rows) != 1:
        failures.append("manifest must have exactly 11 required rows and one optional row")

    by_item = {r.get("item"): r for r in rows}
    for item, path_text in LOCAL_REQUIRED.items():
        path = ROOT / path_text
        if not path.is_file():
            failures.append(f"required local artifact missing: {path_text}")
        row = by_item.get(item, {})
        if row.get("location_or_url") != GITHUB_BLOB + path_text:
            failures.append(f"{item} manifest URL must use the exact case-sensitive path {path_text}")
        if item.endswith(".pdf") and path.is_file():
            try:
                count = pdf_page_objects(path)
                if count < 1:
                    failures.append(f"{path_text} contains no detectable PDF page object")
                if item == "Decision memo or deck" and count > 8:
                    failures.append(f"Decision deck has {count} detectable PDF pages; maximum is eight main slides")
            except OSError as exc:
                failures.append(f"cannot read {path_text}: {exc}")
            except ValueError as exc:
                failures.append(f"{path_text} is not structurally readable as PDF: {exc}")

    readme = (ROOT / "README.md")
    if "[visible base output](output/visible-base-output.html)" not in readme.read_text(encoding="utf-8"):
        failures.append("README must link to output/visible-base-output.html")
    for md in (ROOT / "README.md", ROOT / "docs" / "final-submission-readiness.md"):
        if md.exists():
            check_local_markdown_links(md, failures)

    validation = (ROOT / "docs" / "validation-and-ai-use.md").read_text(encoding="utf-8")
    for phrase in ("Complete historical Locked Changed-Input AFTER record", "ChatGPT — OpenAI", "Codex — OpenAI"):
        if phrase not in validation:
            failures.append(f"validation record missing required evidence phrase: {phrase}")
    for phrase in ("35 tests", "six-page visual and text-extraction validation"):
        if phrase not in validation:
            failures.append(f"validation/PDF synchronization evidence missing: {phrase}")

    for item in VIDEO_ITEMS | TRANSCRIPT_ITEMS:
        row = by_item.get(item, {})
        missing = [field for field in ("location_or_url", "title", "duration_or_as_of", "timestamp_index", "access_checked") if not row.get(field, "").strip()]
        if missing:
            pending_or_fail(mode, pending, failures, f"{item}: missing {', '.join(missing)} (recording-dependent)")
    for item in VIDEO_ITEMS:
        notes = by_item.get(item, {}).get("notes", "")
        if "CAPTIONS_CORRECTED" not in notes:
            pending_or_fail(mode, pending, failures, f"{item}: captions-corrected confirmation is missing")
        if "LOGGED_OUT_ACCESS_VERIFIED" not in notes:
            pending_or_fail(mode, pending, failures, f"{item}: logged-out video access check is missing")
    for item in ("Research-Evolution.pdf", "Repository", "Visible executed output", "Decision memo or deck", "Validation-and-AI-Use.pdf"):
        value = by_item.get(item, {}).get("frozen_or_commit_id", "")
        if not value or "PENDING_FINALIZATION" in value or "not final frozen" in value:
            pending_or_fail(mode, pending, failures, f"{item}: final frozen commit identifier is pending")

    readiness = (ROOT / "docs" / "final-submission-readiness.md").read_text(encoding="utf-8")
    for marker in ("LOGGED_OUT_GRADER_ACCESS_PENDING", "PENDING_RECORDING", "Brightspace submission receipt"):
        if marker not in readiness and marker != "LOGGED_OUT_GRADER_ACCESS_PENDING":
            failures.append(f"readiness record missing manual-verification marker: {marker}")
    if "BRIGHTSPACE_SUBMISSION_RECEIPT_SAVED" not in readiness:
        pending_or_fail(mode, pending, failures, "Brightspace submission receipt confirmation is missing")

    print(f"Submission-package audit mode: {mode}")
    print(f"Manifest rows: {len(rows)}; required rows: {sum(r.get('required') == 'yes' for r in rows)}")
    for message in pending:
        print(f"PENDING: {message}")
    for message in failures:
        print(f"FAIL: {message}")
    if failures:
        return 1
    print("PASS: structural checks completed; manual pending items are listed above." if pending else "PASS: all automated structural checks completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Structural and submission-stage checks for the Project 1 package.

This local audit cannot verify YouTube playback, captions, GitHub access, or a
Brightspace receipt.  Those facts must be recorded explicitly; a missing manual
confirmation is a blocker in pre-submit/post-submit modes, never an automatic
pass.
"""
from __future__ import annotations

import argparse
import csv
import re
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
TRANSCRIPTS = {
    "Transcript Video 1": "docs/transcript-video-1.txt",
    "Transcript Video 2": "docs/transcript-video-2.txt",
    "Transcript Video 3": "docs/transcript-video-3.txt",
}
TRANSCRIPT_MARKERS = {
    "Transcript Video 1": "Hello, my name is Caden Mainville",
    "Transcript Video 2": "this is my IBM Project 1 repository",
    "Transcript Video 3": "recommendation to the investment committee",
}
VIDEO_DURATIONS = {"Video 1": "2:58.91", "Video 2": "approximately 4:32", "Video 3": "approximately 4:58.8"}
VIDEOS = ("Video 1", "Video 2", "Video 3")
GITHUB_BLOB = "https://github.com/cmainville/ibm-project-1/blob/main/"
REQUIRED_FINANCIAL_TEXT = (
    "$231.40", "$145.13", "$182.29", "$224.28", "7.07%", "2.5%",
    "15%", "Watch / Defer",
)


def pdf_page_objects(path: Path) -> int:
    raw = path.read_bytes()
    if not raw.startswith(b"%PDF-"):
        raise ValueError("missing PDF header")
    return len(re.findall(rb"/Type\s*/Page\b", raw))


def check_markdown_links(path: Path, failures: list[str]) -> None:
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if not (path.parent / unquote(target.split("#", 1)[0])).resolve().exists():
            failures.append(f"broken local Markdown link in {path.relative_to(ROOT)}: {target}")


def is_video_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and parsed.netloc in {"www.youtube.com", "youtube.com"} and parsed.path == "/watch" and bool(parsed.query)


def manual_confirmation_missing(row: dict[str, str], kind: str) -> bool:
    text = " ".join((row.get("access_checked", ""), row.get("notes", ""))).upper()
    return kind not in text


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pre-recording", action="store_true", help="legacy structural audit; manual items are reported as pending")
    group.add_argument("--pre-submit", action="store_true", help="require every pre-Brightspace requirement")
    group.add_argument("--post-submit", action="store_true", help="pre-submit checks plus a recorded Brightspace receipt")
    args = parser.parse_args()
    mode = "pre-recording" if args.pre_recording else "pre-submit" if args.pre_submit else "post-submit"
    failures: list[str] = []
    pending: list[str] = []

    def require(message: str) -> None:
        if mode == "pre-recording":
            pending.append(message)
        else:
            failures.append(message)

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

    for item, relative in LOCAL_REQUIRED.items():
        path = ROOT / relative
        row = by_item.get(item, {})
        if not path.is_file():
            failures.append(f"required local artifact missing: {relative}")
        if row.get("location_or_url") != GITHUB_BLOB + relative:
            failures.append(f"{item} manifest URL must use exact case-sensitive path {relative}")
        if relative.endswith(".pdf") and path.is_file():
            try:
                pages = pdf_page_objects(path)
                if pages < 1:
                    failures.append(f"{relative} has no detectable PDF page object")
                if item == "Decision memo or deck" and pages > 8:
                    failures.append("Decision deck exceeds eight detectable PDF pages")
            except (OSError, ValueError) as exc:
                failures.append(f"cannot validate {relative}: {exc}")

    for item, relative in TRANSCRIPTS.items():
        path = ROOT / relative
        row = by_item.get(item, {})
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        if not text.strip():
            failures.append(f"required transcript missing or empty: {relative}")
        elif "[0:00]" not in text:
            failures.append(f"transcript lacks source timestamp marker: {relative}")
        elif TRANSCRIPT_MARKERS[item] not in text:
            failures.append(f"transcript mapping/content marker is incorrect: {relative}")
        if row.get("location_or_url") != GITHUB_BLOB + relative:
            failures.append(f"{item} manifest URL must use exact case-sensitive path {relative}")

    readme = ROOT / "README.md"
    if not readme.is_file() or "[visible base output](output/visible-base-output.html)" not in readme.read_text(encoding="utf-8"):
        failures.append("README must link to output/visible-base-output.html")
    for path in (readme, ROOT / "docs" / "final-submission-readiness.md"):
        if path.exists():
            check_markdown_links(path, failures)

    validation = (ROOT / "docs" / "validation-and-ai-use.md").read_text(encoding="utf-8")
    for phrase in ("Complete historical Locked Changed-Input AFTER record", "ChatGPT — OpenAI", "Codex — OpenAI", "35 tests", "six-page visual and text-extraction validation"):
        if phrase not in validation:
            failures.append(f"validation evidence missing required phrase: {phrase}")
    financial_sources = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (readme, ROOT / "docs" / "Decision-Deck.html", ROOT / "docs" / "validation-and-ai-use.md")
        if path.is_file()
    )
    for phrase in REQUIRED_FINANCIAL_TEXT:
        if phrase not in financial_sources:
            failures.append(f"package evidence missing approved financial value/decision: {phrase}")

    for item in (*VIDEOS, *TRANSCRIPTS):
        row = by_item.get(item, {})
        missing = [field for field in ("location_or_url", "title", "duration_or_as_of", "timestamp_index", "access_checked") if not row.get(field, "").strip()]
        if missing:
            failures.append(f"{item}: missing {', '.join(missing)}")
    for item in VIDEOS:
        row = by_item.get(item, {})
        if not is_video_url(row.get("location_or_url", "")):
            failures.append(f"{item}: URL must be an HTTPS YouTube watch URL")
        if not row.get("timestamp_index", "").strip():
            failures.append(f"{item}: finalized timestamp index is missing")
        if row.get("duration_or_as_of") != VIDEO_DURATIONS[item]:
            failures.append(f"{item}: duration must equal supplied final duration {VIDEO_DURATIONS[item]}")
        transcript_row = by_item.get(f"Transcript {item}", {})
        if transcript_row.get("duration_or_as_of") != VIDEO_DURATIONS[item]:
            failures.append(f"Transcript {item.removeprefix('Video ')}: duration must match {item}")
        if manual_confirmation_missing(row, "CAPTIONS_CORRECTED"):
            require(f"{item}: documented corrected-caption confirmation is missing")
        if manual_confirmation_missing(row, "LOGGED_OUT_ACCESS_VERIFIED"):
            require(f"{item}: documented logged-out video access confirmation is missing")

    repository = by_item.get("Repository", {})
    if repository.get("location_or_url") != "https://github.com/cmainville/ibm-project-1":
        failures.append("Repository manifest URL is incorrect")
    if manual_confirmation_missing(repository, "LOGGED_OUT_GRADER_ACCESS_VERIFIED"):
        require("Repository: documented logged-out/grader access confirmation is missing")

    for item in ITEMS[:-1]:
        value = by_item.get(item, {}).get("frozen_or_commit_id", "")
        if not value or "PENDING_FINALIZATION" in value or "not final frozen" in value:
            require(f"{item}: stable submission snapshot identifier is pending")

    readiness = (ROOT / "docs" / "final-submission-readiness.md").read_text(encoding="utf-8")
    if "PENDING_INSTRUCTOR_DETERMINATION" not in readiness:
        failures.append("readiness record must retain the Edition A instructor-determination disclosure")
    if mode == "post-submit" and "BRIGHTSPACE_SUBMISSION_RECEIPT_SAVED" not in readiness:
        failures.append("Brightspace submission receipt confirmation is missing")

    print(f"Submission-package audit mode: {mode}")
    print(f"Manifest rows: {len(rows)}; required rows: {sum(r.get('required') == 'yes' for r in rows)}")
    for message in pending:
        print(f"PENDING: {message}")
    for message in failures:
        print(f"FAIL: {message}")
    if failures:
        return 1
    print("PASS: structural checks completed; manual pending items are listed above." if pending else "PASS: all checks required for this mode completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

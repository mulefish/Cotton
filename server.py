"""Flask server that serves static/public assets and exposes a summary API."""

from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from flask import Flask, abort, jsonify, request, send_from_directory

from data2json import FIELDS, parse_record

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"
STATIC_DIR = BASE_DIR / "static"
TEST_BALES_FILE = BASE_DIR / "data" / "TestBales01.txt"
DEFAULT_FIELDS: Tuple[str, ...] = ("colorGrade", "leafGrade", "stapleCode")
AVAILABLE_FIELDS = {name for name, *_ in FIELDS}

app = Flask(
    __name__,
    static_folder=str(STATIC_DIR),
    static_url_path="/static",
)


def _serve(directory: Path, file_path: str):
    target = directory / file_path
    if target.is_file():
        return send_from_directory(directory, file_path)
    abort(404)


@app.route("/")
def serve_root():
    index = PUBLIC_DIR / "index.html"
    if index.is_file():
        return send_from_directory(PUBLIC_DIR, "index.html")
    abort(404)


@app.route("/<path:file_path>")
def serve_public(file_path: str):
    return _serve(PUBLIC_DIR, file_path)


@app.route("/static/<path:file_path>")
def serve_static_files(file_path: str):
    return _serve(STATIC_DIR, file_path)


def _normalize_requested_fields(fields: Optional[Sequence[str]]) -> List[str]:
    """Return a sanitized (unique, known) list of requested fields."""
    normalized: List[str] = []
    seen = set()
    for field in fields or []:
        if field in AVAILABLE_FIELDS and field not in seen:
            normalized.append(field)
            seen.add(field)

    if not normalized:
        normalized = list(DEFAULT_FIELDS)
    return normalized


def build_summary(requested_fields: Optional[List[str]] = None) -> Tuple[List[Dict[str, str]], List[str]]:
    """Aggregate counts for unique combinations of requested fields from TestBales data."""
    if not TEST_BALES_FILE.exists():
        return [], _normalize_requested_fields(requested_fields)

    fields = _normalize_requested_fields(requested_fields)
    print(f"build_summary using fields: {fields}")
    counts: Dict[Tuple[str, ...], int] = defaultdict(int)

    with TEST_BALES_FILE.open(encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            if not line.strip():
                continue
            record = parse_record(line.rstrip("\n"))
            if not record:
                continue
            key = tuple(record.get(field, "") for field in fields)
            counts[key] += 1

    summary = []
    for combo, count in counts.items():
        entry = {field: value for field, value in zip(fields, combo)}
        entry["count"] = count
        summary.append(entry)

    summary.sort(key=lambda item: item["count"], reverse=True)
    return summary, fields


@app.route("/api/summary", methods=["POST"])
def api_summary():
    payload = request.get_json(silent=True) or {}
    requested_fields = payload.get("fields", [])
    summary, normalized_fields = build_summary(requested_fields)
    return jsonify({"summary": summary, "requestedFields": normalized_fields})


if __name__ == "__main__":
    app.run(debug=True)
from pathlib import Path

from flask import Flask, abort, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"
STATIC_DIR = BASE_DIR / "static"

app = Flask(
    __name__,
    static_folder=str(STATIC_DIR),
    static_url_path="/static",
)


def _serve(directory: Path, file_path: str):
    target = directory / file_path
    if target.is_file():
        return send_from_directory(directory, file_path)
    abort(404)


@app.route("/")
def serve_index():
    if (PUBLIC_DIR / "index.html").is_file():
        return send_from_directory(PUBLIC_DIR, "index.html")
    abort(404)

@app.route("/<path:file_path>")
def serve_public(file_path: str):
    return _serve(PUBLIC_DIR, file_path)


@app.route("/static/<path:file_path>")
def serve_static_files(file_path: str):
    return _serve(STATIC_DIR, file_path)


if __name__ == "__main__":
    app.run(debug=True)


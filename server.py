"""Flask server that serves static/public assets and exposes a summary API."""

from collections import defaultdict
import csv
from pathlib import Path
from typing import List, Dict

from flask import Flask, abort, jsonify, request, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"
STATIC_DIR = BASE_DIR / "static"
DATA_FILE = BASE_DIR / "color_staple_leaf.csv"

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


def build_summary() -> List[Dict[str, str]]:
    """Aggregate counts for (colorGrade, leafGrade, stapleCode)."""
    if not DATA_FILE.exists():
        return []

    counts: Dict[tuple, int] = defaultdict(int)
    with DATA_FILE.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            color = (row.get("colorGrade") or "").strip()
            leaf = (row.get("leafGrade") or "").strip()
            staple = (row.get("stapleCode") or "").strip()
            counts[(color, leaf, staple)] += 1

    summary = [
        {
            "colorGrade": color,
            "leafGrade": leaf,
            "stapleCode": staple,
            "count": count,
        }
        for (color, leaf, staple), count in counts.items()
    ]
    summary.sort(key=lambda item: item["count"], reverse=True)
    return summary


@app.route("/api/summary", methods=["POST"])
def api_summary():
    payload = request.get_json(silent=True) or {}
    requested_fields = payload.get("fields", [])
    summary = build_summary()
    return jsonify({"summary": summary, "requestedFields": requested_fields})


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


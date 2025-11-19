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


# ============================================================================
# RESTful API Demo - In-memory storage (simulating a database)
# ============================================================================

# In-memory storage for demo items
_items_storage: List[Dict] = []
_next_id = 1


def _initialize_sample_items():
    """Initialize the storage with sample items for demonstration."""
    global _items_storage, _next_id
    sample_items = [
        {"id": 1, "name": "Cotton Bale - Premium Grade", "description": "High-quality cotton bale with excellent fiber length and strength", "price": 1250.00},
        {"id": 2, "name": "Cotton Bale - Standard Grade", "description": "Standard quality cotton bale suitable for general textile production", "price": 980.50},
        {"id": 3, "name": "Cotton Bale - Organic", "description": "Certified organic cotton bale, sustainably sourced", "price": 1450.75},
        {"id": 4, "name": "Cotton Bale - Extra Long Staple", "description": "Premium extra long staple cotton for luxury textiles", "price": 1680.00},
        {"id": 5, "name": "Cotton Bale - Medium Staple", "description": "Medium staple length cotton, versatile for various applications", "price": 875.25},
    ]
    _items_storage.extend(sample_items)
    _next_id = len(sample_items) + 1


# Initialize with sample data
_initialize_sample_items()


@app.route("/api/items", methods=["GET"])
def get_all_items():
    """GET /api/items - Retrieve all items."""
    return jsonify(_items_storage), 200


@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id: int):
    """GET /api/items/<id> - Retrieve a specific item by ID."""
    item = next((item for item in _items_storage if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


@app.route("/api/items", methods=["POST"])
def create_item():
    """POST /api/items - Create a new item."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    # Validate required fields
    required_fields = ["name", "description", "price"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400
    
    # Validate price is a number
    try:
        price = float(data["price"])
        if price < 0:
            return jsonify({"error": "Price must be non-negative"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Price must be a valid number"}), 400
    
    # Create new item
    global _next_id
    new_item = {
        "id": _next_id,
        "name": str(data["name"]).strip(),
        "description": str(data["description"]).strip(),
        "price": price
    }
    _items_storage.append(new_item)
    _next_id += 1
    
    return jsonify(new_item), 201


@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id: int):
    """PUT /api/items/<id> - Update an existing item."""
    item = next((item for item in _items_storage if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    # Validate required fields
    required_fields = ["name", "description", "price"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400
    
    # Validate price is a number
    try:
        price = float(data["price"])
        if price < 0:
            return jsonify({"error": "Price must be non-negative"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Price must be a valid number"}), 400
    
    # Update item
    item["name"] = str(data["name"]).strip()
    item["description"] = str(data["description"]).strip()
    item["price"] = price
    
    return jsonify(item), 200


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id: int):
    """DELETE /api/items/<id> - Delete an item by ID."""
    global _items_storage
    item = next((item for item in _items_storage if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    
    _items_storage = [item for item in _items_storage if item["id"] != item_id]
    return jsonify({"message": "Item deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)


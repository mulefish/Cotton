"""Flask server that serves static/public assets and exposes a summary API."""

from collections import defaultdict
import json
import random
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


# ============================================================================
# Cotton Futures Trading Game
# ============================================================================

_game_state: Optional[Dict] = None
GAME_STATE_FILE = BASE_DIR / "game_state.json"

SEASONS = ["Spring", "Summer", "Harvest", "Winter"]
CONTRACT_MONTHS = ["Jan", "Mar", "May", "Jul", "Sep", "Nov"]
WEATHER_EVENTS = [
    {"name": "Perfect Weather", "price_impact": 0.05, "supply_impact": 0.10},
    {"name": "Drought", "price_impact": 0.15, "supply_impact": -0.20},
    {"name": "Heavy Rains", "price_impact": 0.10, "supply_impact": -0.15},
    {"name": "Pest Outbreak", "price_impact": 0.12, "supply_impact": -0.18},
    {"name": "Normal Conditions", "price_impact": 0.0, "supply_impact": 0.0},
]


def _load_game_state() -> Optional[Dict]:
    """Load game state from JSON file if it exists."""
    global _game_state
    if GAME_STATE_FILE.exists():
        try:
            with GAME_STATE_FILE.open('r', encoding='utf-8') as f:
                _game_state = json.load(f)
                return _game_state
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading game state: {e}")
            return None
    return None


def _save_game_state() -> None:
    """Save current game state to JSON file."""
    global _game_state
    if _game_state:
        try:
            with GAME_STATE_FILE.open('w', encoding='utf-8') as f:
                json.dump(_game_state, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving game state: {e}")


def _create_new_game() -> Dict:
    """Initialize a new game with players and starting state."""
    base_price = 0.75  # Starting price per lb
    
    players = [
        {
            "id": 1,
            "name": "Farmer Joe",
            "role": "farmer",
            "cash": 50000.0,
            "cotton": 0,
            "futuresContracts": [],
            "netWorth": 50000.0
        },
        {
            "id": 2,
            "name": "Textile Mill Co",
            "role": "mill",
            "cash": 100000.0,
            "cotton": 0,
            "futuresContracts": [],
            "netWorth": 100000.0
        },
        {
            "id": 3,
            "name": "Trader Max",
            "role": "speculator",
            "cash": 75000.0,
            "cotton": 0,
            "futuresContracts": [],
            "netWorth": 75000.0
        },
        {
            "id": 4,
            "name": "Cotton Merchant",
            "role": "merchant",
            "cash": 80000.0,
            "cotton": 50000,  # Starting inventory
            "futuresContracts": [],
            "netWorth": 117500.0  # cash + cotton value
        }
    ]
    
    # Create futures contracts for next 6 months
    futures_contracts = []
    for i, month in enumerate(CONTRACT_MONTHS[:6]):
        futures_contracts.append({
            "id": f"FUT-{month}",
            "month": month,
            "price": base_price * (1 + i * 0.02),  # Slight contango
            "priceChange": 0.0,
            "openInterest": 0
        })
    
    return {
        "turn": 1,
        "season": "Spring",
        "spotPrice": base_price,
        "futuresPrice": base_price * 1.01,
        "players": players,
        "futuresContracts": futures_contracts,
        "weatherEvent": None,
        "supply": 1000000,  # Total supply in lbs
        "demand": 950000    # Total demand in lbs
    }


def _calculate_net_worth(player: Dict, spot_price: float) -> float:
    """Calculate player's net worth including futures positions."""
    cash = player["cash"]
    cotton_value = player["cotton"] * spot_price
    
    # Calculate futures P&L
    futures_pnl = 0.0
    for contract in player["futuresContracts"]:
        # Find current contract price
        contract_data = next(
            (fc for fc in _game_state["futuresContracts"] if fc["id"] == contract["contractId"]),
            None
        )
        if contract_data:
            price_diff = contract_data["price"] - contract["entryPrice"]
            futures_pnl += price_diff * contract["quantity"] * 50000  # 50k lbs per contract
    
    return cash + cotton_value + futures_pnl


def _advance_turn() -> Dict:
    """Process one turn: update season, prices, events."""
    global _game_state
    
    if not _game_state:
        return _create_new_game()
    
    # Advance season
    current_season_idx = SEASONS.index(_game_state["season"])
    next_season_idx = (current_season_idx + 1) % len(SEASONS)
    _game_state["season"] = SEASONS[next_season_idx]
    _game_state["turn"] += 1
    
    # Random weather event (more likely in growing seasons)
    if _game_state["season"] in ["Spring", "Summer"]:
        if random.random() < 0.4:  # 40% chance of weather event
            event = random.choice(WEATHER_EVENTS)
            _game_state["weatherEvent"] = event
            _game_state["spotPrice"] *= (1 + event["price_impact"])
            _game_state["supply"] = int(_game_state["supply"] * (1 + event["supply_impact"]))
        else:
            _game_state["weatherEvent"] = None
    else:
        _game_state["weatherEvent"] = None
    
    # Price dynamics based on supply/demand
    supply_demand_ratio = _game_state["supply"] / max(_game_state["demand"], 1)
    if supply_demand_ratio > 1.1:  # Oversupply
        _game_state["spotPrice"] *= 0.98
    elif supply_demand_ratio < 0.9:  # Shortage
        _game_state["spotPrice"] *= 1.02
    
    # Add some random volatility
    volatility = random.uniform(-0.03, 0.03)
    _game_state["spotPrice"] *= (1 + volatility)
    _game_state["spotPrice"] = max(0.30, min(2.00, _game_state["spotPrice"]))  # Clamp price
    
    # Update futures prices (track spot with some basis)
    _game_state["futuresPrice"] = _game_state["spotPrice"] * random.uniform(0.98, 1.02)
    
    # Update futures contract prices
    for contract in _game_state["futuresContracts"]:
        old_price = contract["price"]
        # Futures price moves with spot, plus time decay
        contract["price"] = _game_state["spotPrice"] * random.uniform(0.99, 1.01)
        contract["priceChange"] = contract["price"] - old_price
    
    # Update player net worths
    for player in _game_state["players"]:
        player["netWorth"] = _calculate_net_worth(player, _game_state["spotPrice"])
    
    # Seasonal supply changes
    if _game_state["season"] == "Harvest":
        # Farmers produce cotton
        farmer = next((p for p in _game_state["players"] if p["role"] == "farmer"), None)
        if farmer:
            harvest = random.randint(200000, 400000)
            farmer["cotton"] += harvest
            _game_state["supply"] += harvest
    
    # Seasonal demand changes
    if _game_state["season"] in ["Winter", "Spring"]:
        _game_state["demand"] = int(_game_state["demand"] * random.uniform(1.0, 1.1))
    
    return _game_state


@app.route("/api/game/state", methods=["GET"])
def get_game_state():
    """GET /api/game/state - Get current game state."""
    global _game_state
    # Try to load from file if not in memory
    if not _game_state:
        _game_state = _load_game_state()
    if not _game_state:
        return jsonify({"error": "No active game"}), 404
    return jsonify(_game_state), 200


@app.route("/api/game/new", methods=["POST"])
def new_game():
    """POST /api/game/new - Start a new game."""
    global _game_state
    _game_state = _create_new_game()
    _save_game_state()
    return jsonify(_game_state), 200


@app.route("/api/game/turn", methods=["POST"])
def advance_turn():
    """POST /api/game/turn - Advance to next turn."""
    global _game_state
    if not _game_state:
        # Try to load from file
        _game_state = _load_game_state()
    if not _game_state:
        return jsonify({"error": "No active game. Start a new game first."}), 400
    _game_state = _advance_turn()
    _save_game_state()
    return jsonify(_game_state), 200


@app.route("/api/game/trade", methods=["POST"])
def execute_trade():
    """POST /api/game/trade - Execute a futures trade."""
    global _game_state
    if not _game_state:
        return jsonify({"error": "No active game"}), 400
    
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    player_id = data.get("playerId")
    contract_id = data.get("contractId")
    action = data.get("action")  # "buy" or "sell"
    quantity = data.get("quantity", 1)
    price = data.get("price")
    
    if not all([player_id, contract_id, action, price]):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Find player
    player = next((p for p in _game_state["players"] if p["id"] == player_id), None)
    if not player:
        return jsonify({"error": "Player not found"}), 404
    
    # Find contract
    contract = next((c for c in _game_state["futuresContracts"] if c["id"] == contract_id), None)
    if not contract:
        return jsonify({"error": "Contract not found"}), 404
    
    # Calculate margin requirement (simplified: 5% of contract value)
    contract_value = price * quantity * 50000  # 50k lbs per contract
    margin_required = contract_value * 0.05
    
    if player["cash"] < margin_required:
        return jsonify({"error": "Insufficient cash for margin requirement"}), 400
    
    # Execute trade
    if action == "buy":
        trade_quantity = quantity
    else:  # sell
        trade_quantity = -quantity
    
    # Check if player already has a position in this contract
    existing_position = next(
        (fc for fc in player["futuresContracts"] if fc["contractId"] == contract_id),
        None
    )
    
    if existing_position:
        # Update existing position
        existing_position["quantity"] += trade_quantity
        if existing_position["quantity"] == 0:
            # Position closed
            player["futuresContracts"].remove(existing_position)
        else:
            # Average entry price
            total_cost = existing_position["entryPrice"] * abs(existing_position["quantity"] - trade_quantity) + price * abs(trade_quantity)
            existing_position["entryPrice"] = total_cost / abs(existing_position["quantity"])
    else:
        # New position
        player["futuresContracts"].append({
            "contractId": contract_id,
            "quantity": trade_quantity,
            "entryPrice": price
        })
    
    # Deduct margin (simplified - in reality, margin is held, not spent)
    player["cash"] -= margin_required * 0.1  # Small transaction cost
    
    # Update open interest
    contract["openInterest"] += abs(trade_quantity)
    
    # Update player net worth
    player["netWorth"] = _calculate_net_worth(player, _game_state["spotPrice"])
    
    _save_game_state()
    return jsonify(_game_state), 200


if __name__ == "__main__":
    # Try to load existing game state on startup
    _game_state = _load_game_state()
    if _game_state:
        print(f"Loaded existing game: Turn {_game_state['turn']}, Season {_game_state['season']}")
    app.run(debug=True)


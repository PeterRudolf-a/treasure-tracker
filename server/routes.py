from flask import Blueprint, request, jsonify
from models import save_item, get_inventory, get_user_by_name, save_user
import uuid

routes = Blueprint('routes', __name__)

@routes.route("/collect", methods=["POST"])
def collect_item():
    data = request.get_json()
    user_id = data.get("user_id")
    item_name = data.get("item_name")
    rarity = data.get("rarity")
    collected_at = data.get("collected_at")

    if not user_id or not item_name or not rarity or not collected_at:
        return jsonify({"error": "Missing required fields"}), 400

    print(f"[COLLECT] {user_id=} {item_name=} {rarity=}")
    save_item(user_id, item_name, rarity, collected_at)
    return jsonify({"status": "success"}), 201

@routes.route("/inventory/<user_id>", methods=["GET"])
def inventory(user_id):
    items = get_inventory(user_id)
    return jsonify(items)

@routes.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    name = data.get("name", "").strip()
    if not name:
        return jsonify({"error": "Name cannot be empty"}), 400

    user_id = get_user_by_name(name)
    if user_id:
        print(f"[REGISTER] Existing user: {name=} {user_id=}")
        return jsonify({"user_id": user_id})

    new_user_id = str(uuid.uuid4())
    save_user(new_user_id, name)
    print(f"[REGISTER] New user: {name=} {new_user_id=}")
    return jsonify({"user_id": new_user_id})


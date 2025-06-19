from flask import Blueprint, request, jsonify
from models import save_item, get_inventory

routes = Blueprint('routes', __name__)

@routes.route("/collect", methods=["POST"])
def collect_item():
    data = request.get_json()
    save_item(data["user_id"], data["item_name"], data["rarity"], data["collected_at"])
    return jsonify({"status": "success"}), 201

@routes.route("/inventory/<user_id>", methods=["GET"])
def inventory(user_id):
    items = get_inventory(user_id)
    return jsonify(items)

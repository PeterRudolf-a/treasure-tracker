from flask import Blueprint, request, jsonify
from models import save_item, get_inventory, get_user_by_name, save_score
import uuid
import sqlite3
import os
DB_PATH = os.path.join(os.path.dirname(__file__), "db.sqlite3")


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

@routes.route("/submit_score", methods=["POST"])
def submit_score():
    data = request.get_json()
    save_score(data["user_id"], data["score"])
    return jsonify({"status": "score saved"}), 200


@routes.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    name = data["name"].strip()
    if not name:
        return jsonify({"error": "Name cannot be empty"}), 400

    # Reuse existing user if exists
    user_id = get_user_by_name(name)
    if user_id:
        return jsonify({"user_id": user_id})

    # Otherwise create new
    new_user_id = str(uuid.uuid4())
    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()
    cur.execute("INSERT INTO users (user_id, name) VALUES (?, ?)",
                (new_user_id, name))
    conn.commit()
    conn.close()
    return jsonify({"user_id": new_user_id})

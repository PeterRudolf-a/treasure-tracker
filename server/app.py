from flask import Flask, jsonify, request
from flask_cors import CORS
from routes import routes
from models import init_db, get_top_scores, save_score

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS
app.register_blueprint(routes)

# Custom score routes
@app.route("/scores", methods=["GET"])
def scores():
    top_scores = get_top_scores()
    return jsonify(top_scores)

@app.route("/submit_score", methods=["POST"])
def submit_score():
    data = request.json
    user_id = data.get("user_id")
    score = data.get("score")

    if user_id and score is not None:
        save_score(user_id, score)
        return jsonify({"status": "ok"})

    return jsonify({"error": "Invalid data"}), 400

# Run the app
if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)


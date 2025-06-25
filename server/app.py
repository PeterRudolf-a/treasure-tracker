from flask import Flask
from routes import routes
from models import init_db, get_top_scores, save_score
from flask import jsonify, request

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

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

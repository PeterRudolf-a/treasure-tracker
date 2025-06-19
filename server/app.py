from flask import Flask
from routes import routes
from models import init_db

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

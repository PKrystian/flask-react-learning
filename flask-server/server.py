from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["Topic 1", "Topic 2", "Topic 3"]}

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)

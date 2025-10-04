from flask_cors import CORS
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

app = Flask(__name__)
CORS(app)
DATA_FILE = "script/user_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/api/userdata", methods=["GET"])
def get_user_data():
    data = load_data()
    # 不回傳密碼雜湊
    safe_data = [
        {k: v for k, v in user.items() if k != "password_hash"}
        for user in data
    ]
    return jsonify(safe_data)

@app.route("/api/register", methods=["POST"])
def register_user():
    req = request.json
    username = req.get("username")
    password = req.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    data = load_data()
    if any(u["username"] == username for u in data):
        return jsonify({"error": "User already exists"}), 400
    password_hash = generate_password_hash(password)
    user = {"username": username, "password_hash": password_hash}
    data.append(user)
    save_data(data)
    return jsonify({"status": "ok"})

@app.route("/api/login", methods=["POST"])
def login_user():
    req = request.json
    username = req.get("username")
    password = req.get("password")
    data = load_data()
    user = next((u for u in data if u["username"] == username), None)
    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"error": "Invalid username or password"}), 401
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

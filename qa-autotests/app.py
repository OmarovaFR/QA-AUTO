from flask import Flask, jsonify, request

app = Flask(__name__)

USERS = {
    1: {"id": 1, "name": "Farida", "role": "qa"},
    2: {"id": 2, "name": "Amina", "role": "user"},
}


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/users/<int:user_id>")
def get_user(user_id):
    user = USERS.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.post("/users")
def create_user():
    data = request.get_json(silent=True) or {}

    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    new_id = max(USERS) + 1
    user = {"id": new_id, "name": data["name"], "role": data.get("role", "user")}
    USERS[new_id] = user
    return jsonify(user), 201


if __name__ == "__main__":
    app.run(debug=True)

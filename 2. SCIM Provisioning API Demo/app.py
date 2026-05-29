from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

users = []

@app.route("/Users", methods=["POST"])
def create_user():

    data = request.json

    new_user = {
        "id": str(uuid.uuid4()),
        "userName": data["userName"],
        "emails": data.get("emails", []),
        "active": True
    }

    users.append(new_user)

    return jsonify(new_user), 201

@app.route("/Users", methods=["GET"])
def list_users():
    return jsonify(users)

@app.route("/Users/<user_id>", methods=["DELETE"])
def deactivate_user(user_id):

    for user in users:

        if user["id"] == user_id:
            user["active"] = False
            return jsonify({
                "message": "User deactivated",
                "user": user
            })

    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

VALID_API_KEYS = {
    "employee-key": {
        "role": "employee",
        "device": "managed"
    },
    "admin-key": {
        "role": "admin",
        "device": "managed"
    }
}

@app.route("/secure-data")
def secure_data():

    api_key = request.headers.get("X-API-KEY")

    if not api_key:
        return jsonify({
            "error": "Missing API key"
        }), 401

    identity = VALID_API_KEYS.get(api_key)

    if not identity:
        return jsonify({
            "error": "Invalid credentials"
        }), 403

    if identity["device"] != "managed":
        return jsonify({
            "error": "Untrusted device"
        }), 403

    audit_log = {
        "timestamp": time.time(),
        "role": identity["role"],
        "action": "access_secure_data"
    }

    return jsonify({
        "message": "Access granted",
        "audit": audit_log
    })

if __name__ == "__main__":
    app.run(debug=True)
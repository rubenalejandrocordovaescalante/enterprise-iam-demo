from flask import Flask, jsonify

app = Flask(__name__)

roles = {
    "admin": [
        "create_user",
        "delete_user",
        "view_reports",
        "manage_servers"
    ],
    "employee": [
        "view_reports"
    ],
    "security_analyst": [
        "view_reports",
        "investigate_alerts"
    ]
}

def can_access(role, permission):

    allowed = roles.get(role, [])

    return permission in allowed

@app.route("/check/<role>/<permission>")
def check(role, permission):

    access = can_access(role, permission)

    return jsonify({
        "role": role,
        "permission": permission,
        "access_granted": access
    })

if __name__ == "__main__":
    app.run(debug=True)
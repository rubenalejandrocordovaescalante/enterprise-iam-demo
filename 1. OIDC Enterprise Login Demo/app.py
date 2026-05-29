from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)

# Session secret

app.secret_key = "supersecretkey" #Or Use Enviromental variable app.secret_key = os.getenv("FLASK_SECRET_KEY")

oauth = OAuth(app)

# ✔ FIX: use ONLY OIDC discovery (removes jwks_uri + metadata issues)
google = oauth.register(
    name='google',
    #client_id=os.getenv("GOOGLE_CLIENT_ID"),
    #client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    client_id="GOOGLE_CLIENT_ID",
    client_secret="GOOGLE_CLIENT_SECRET",

    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",

    client_kwargs={
        "scope": "openid email profile"
    }
)

@app.route("/")
def home():

    user = session.get("user")

    if user:
        return f"""
        <h1>Enterprise OIDC Login Demo</h1>
        <p>Authenticated User:</p>
        <ul>
            <li>Email: {user.get('email')}</li>
            <li>Name: {user.get('name')}</li>
        </ul>
        <a href='/logout'>Logout</a>
        """

    return """
    <h1>Enterprise OIDC Login Demo</h1>
    <a href='/login'>Login With Google</a>
    """

@app.route("/login")
def login():
    return google.authorize_redirect(
        redirect_uri=url_for('authorize', _external=True)
    )

@app.route("/authorize")
def authorize():

    token = google.authorize_access_token()

    # ✔ FIX: safe OIDC user extraction
    user = token.get("userinfo")

    # fallback (if provider returns differently)
    if not user:
        resp = google.get("userinfo")
        user = resp.json()

    session["user"] = user

    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
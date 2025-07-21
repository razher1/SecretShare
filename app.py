from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# In-memory storage for secrets (cleared when app restarts)
secrets = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_secret():
    secret_text = request.form.get("secret")

    if not secret_text:
        return "Secret can't be empty", 400

    secret_id = str(uuid.uuid4())[:8]
    secrets[secret_id] = secret_text

    return render_template("link.html", secret_id=secret_id)

@app.route("/secret/<secret_id>")
def view_secret(secret_id):
    secret_text = secrets.pop(secret_id, None)

    if secret_text is None:
        return render_template("expired.html"), 404

    return render_template("secret.html", secret=secret_text)

if __name__ == "__main__":
    app.run(debug=True)
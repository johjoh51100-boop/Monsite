from flask import Flask, request, render_template
import os
from datetime import datetime

app = Flask(__name__)
SECRET_PASSWORD = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        password = request.form.get("password")
        if password == SECRET_PASSWORD:
            user_ip = request.remote_addr
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            return render_template("success.html", ip=user_ip, date=now)
        else:
            message = "❌ Mot de passe incorrect"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
